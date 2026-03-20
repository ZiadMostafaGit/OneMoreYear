# Memory Hierarchy & Cache Performance
### A Backend Engineer's Field Guide
> CPU Registers → L1/L2/L3 Cache → RAM → SSD → Disk | Cache Lines | False Sharing | NUMA

---

## Who This Is For

You are a junior backend engineer building Go services, REST APIs, and database-backed systems. This guide teaches you to reason about where data lives in hardware and write code that respects it. Every concept maps directly to HRIS payroll loops, LLM call center agents, and PostgreSQL on production servers.

---

# Part 1: The Memory Hierarchy

Every time your code reads a variable, the CPU must fetch it from somewhere. That "somewhere" determines whether your instruction takes 0.3 nanoseconds or 10 milliseconds — a **30-million-to-one** difference. Understanding where data lives is the foundation of all performance engineering.

## 1.1 Latency at Every Level

The hierarchy below is ordered from fastest/smallest to slowest/largest. The CPU always tries the fastest level first, falling back down until it finds the data.

| Storage Level | Latency | Typical Size | Location |
|---|---|---|---|
| **CPU Registers** | ~0.3 ns | ~1 KB | On the CPU die, inside the core |
| **L1 Cache** | ~1 ns | 32–64 KB per core | On-die, per core |
| **L2 Cache** | ~4 ns | 256 KB – 1 MB per core | On-die, per core |
| **L3 Cache (LLC)** | ~30–40 ns | 8–64 MB shared | On-die, shared across cores |
| **RAM (DRAM)** | ~100 ns | 16 GB – 1 TB | Off-chip DIMM |
| **NVMe SSD** | ~100,000 ns (0.1 ms) | 256 GB – 8 TB | PCIe attached |
| **Spinning HDD** | ~10,000,000 ns (10 ms) | 1–20 TB | Mechanical seek |

> **Key ratio to memorise:** RAM is 100× slower than L3. SSD is 1,000× slower than RAM. HDD is 100× slower than SSD.

## 1.2 The Warehouse Analogy

| Cache Level | Real-world analogy |
|---|---|
| Registers | Your hands — zero travel time, holds 1–2 things |
| L1 | Your desk — grab anything in under a second |
| L2 / L3 | Your office bookshelf — fast but requires getting up |
| RAM | The building's filing room — 100 steps away |
| SSD | The warehouse across the street — 5 minutes |
| HDD | The archives in another city — half a day |

## 1.3 Why the Gap Exists

Speed and capacity trade off at the physics level:

- **Fast memory (SRAM)** — used in caches — requires 6 transistors per bit. Fast but expensive and power-hungry.
- **Slow memory (DRAM)** — used in RAM — uses 1 transistor + 1 capacitor per bit. Dense and cheap but slow.

You cannot have fast *and* large at the same time. The laws of physics prevent it.

**Key implication:** when you write a loop over 10 million records, performance is not determined by your algorithm's O(n) complexity alone. It is determined by how many **cache misses** you generate. A cache-friendly O(n) algorithm will always beat a cache-hostile O(n) algorithm on real hardware.

---

# Part 2: Cache Lines & Cache Misses

## 2.1 The 64-Byte Rule

The CPU **never fetches a single byte** from RAM. It always fetches **64 bytes at a time**, aligned to a 64-byte boundary. This chunk is called a **cache line**.

**Why 64 bytes?** The CPU bets that if you needed byte X, you will probably need bytes X+1, X+2 ... soon. This is called **spatial locality**. The bet pays off when your data is laid out contiguously in memory.

```
CPU needs:   int64 at address 0x1040          (8 bytes requested)
Actual fetch: addresses 0x1040 → 0x107F       (64 bytes loaded)

Result: the neighbouring 7 int64s are now FREE — already in L1 cache.
```

## 2.2 Cache Misses: Array vs Linked List

```
Array of 1,000,000 int64s:
  → Each cache line holds 8 int64s
  → Total cache misses ≈ 125,000
  → Fast ✓

Linked list of 1,000,000 nodes:
  → Each node pointer jumps to a random heap address
  → Total cache misses ≈ 1,000,000
  → Up to 8× slower ✗
```

### Sequential access — cache friendly

```go
// Walking a slice: ~125k misses for 1M int64s
sum := int64(0)
for _, v := range salaries {  // salaries []int64
    sum += v
}
```

### Random access — cache hostile

```go
// Following a linked list: ~1M misses for 1M nodes
type Node struct {
    Value int64
    Next  *Node   // pointer to a random heap address
}

sum := int64(0)
for n := head; n != nil; n = n.Next {
    sum += n.Value  // each access is likely a cache miss
}
```

> **Real-world impact:** I once replaced a linked-list traversal with a flat slice in a Go hot path — same algorithm, same data, same machine. Throughput went from 200k ops/sec to 4M ops/sec. The *only* change was memory layout.

---

# Part 3: Cache-Friendly Struct Design in Go

## 3.1 Alignment Padding — The Silent Memory Tax

Go never reorders your struct fields. The compiler inserts **padding bytes** between fields to satisfy alignment requirements. Each type must start at an address that is a multiple of its own size.

### Alignment rules

| Type | Size | Must start at address multiple of |
|---|---|---|
| `bool` / `int8` / `uint8` | 1 byte | Any address |
| `int16` / `uint16` | 2 bytes | Multiple of 2 |
| `int32` / `uint32` / `float32` | 4 bytes | Multiple of 4 |
| `int64` / `uint64` / `float64` / pointer | 8 bytes | Multiple of 8 |

### Naive layout — wastes 17 bytes (43% overhead)

```go
type Employee struct {
    Active    bool      // 1B @ offset 0
    //        [7B padding] ← aligning next int64
    ID        int64     // 8B @ offset 8
    IsManager bool      // 1B @ offset 16
    //        [7B padding] ← aligning next float64
    Salary    float64   // 8B @ offset 24
    Level     int32     // 4B @ offset 32
    IsRemote  bool      // 1B @ offset 36
    //        [3B padding] ← aligning struct end to 8B boundary
}
// Total: 40 bytes. Wasted: 17 bytes.
// At 1M records → 17 MB of wasted RAM dragged into cache for nothing
```

### Optimised layout — near-zero waste

```go
type Employee struct {
    ID        int64     // 8B @ offset 0  ← 8-byte types first
    Salary    float64   // 8B @ offset 8
    Level     int32     // 4B @ offset 16 ← 4-byte types next
    Active    bool      // 1B @ offset 20 ← 1-byte types last, grouped
    IsManager bool      // 1B @ offset 21
    IsRemote  bool      // 1B @ offset 22
    //        [1B padding]
}
// Total: 24 bytes. Wasted: 1 byte.
// Saves 16 bytes per record. At 1M records → 16 MB saved.
```

**The rule:** sort fields **largest alignment first, smallest last**. Group booleans together at the end.

```go
// Verify any struct with:
fmt.Println(unsafe.Sizeof(Employee{}))
```

## 3.2 Hot Path vs Cold Path

When a loop runs over millions of records and only touches 3 fields out of 20, you are dragging 17 cold fields into the CPU cache with every record fetch.

### The problem — everything in one struct

```go
// ❌ Bad: hot payroll loop drags 200B per record, uses only 16B
type Employee struct {
    ID           int64     // HOT: used in every loop
    IsActive     bool      // HOT: used in every loop
    DepartmentID int32     // HOT: used in every loop
    // -------- cold below — never touched in payroll loop --------
    FullName     string    // 16B (string header + heap pointer)
    HireDate     time.Time // 24B
    Address      string
    AvatarURL    string
    Bio          string
}
// 200 bytes per record → cache line holds 0.3 records
// 1M records = ~3.1M cache line fetches
```

### The fix — split hot and cold

```go
// ✅ Good: separate hot core from cold profile

type EmployeeCore struct {   // 16 bytes — fits 4 per cache line
    ID           int64
    DepartmentID int32
    IsActive     bool
    _            [3]byte  // explicit pad — document the intent
}
// 1M records = ~250,000 cache line fetches — 12× fewer misses

type EmployeeProfile struct { // loaded only when rendering a UI page
    EmployeeID int64
    FullName   string
    HireDate   time.Time
    Address    string
    AvatarURL  string
    Bio        string
}
```

### The database equivalent — same thinking, different layer

```sql
-- ❌ Bad: loads entire 400B row into 8KB Postgres buffer page
SELECT * FROM employees WHERE is_active = true;

-- ✅ Good: projects only hot columns — index-only scan possible
SELECT id, department_id, is_active
FROM employees
WHERE is_active = true;

-- ✅ Even better: split cold columns to a separate table at schema level
-- employees:         id, department_id, is_active, salary, level
-- employee_profiles: employee_id, full_name, hire_date, address, avatar_url, bio

-- Index covering hot columns (enables index-only scan for attendance job)
CREATE INDEX idx_employees_hot
    ON employees (is_active, department_id)
    INCLUDE (id);
```

> **The principle is identical at both layers.** In Go: don't load cold struct fields. In Postgres: don't load cold columns into buffer pages. `SELECT *` is the Go equivalent of the naive 200-byte struct.

## 3.3 Array of Structs vs Struct of Arrays (AoS vs SoA)

For batch processing large datasets column-by-column (like a payroll run), the layout of data in memory matters enormously.

### Array of Structs (AoS) — intuitive but column-hostile

```go
// AoS: records[0].Salary and records[1].Salary are 28 bytes apart
type PayrollRecord struct {
    EmployeeID int64    // 8B
    BaseSalary float64  // 8B  ← what we want
    Bonus      float64  // 8B
    TaxRate    float32  // 4B
}
var records []PayrollRecord

// Summing all salaries: fetches 28B per record to get 8B salary
// 64B cache line ≈ 2 records — 20B of each record is wasted bandwidth
total := 0.0
for _, r := range records {
    total += r.BaseSalary
}
```

### Struct of Arrays (SoA) — column-friendly

```go
// SoA: all salaries are contiguous — like a column-store database
type PayrollBatch struct {
    EmployeeIDs  []int64
    BaseSalaries []float64  // 8 values per 64B cache line — zero waste
    Bonuses      []float64
    TaxRates     []float32
}

// Summing all salaries: walks BaseSalaries only
// 64B cache line = 8 float64s — perfect cache utilisation
total := 0.0
for _, s := range batch.BaseSalaries {
    total += s
}
// ~3× faster than AoS for column-wise operations
```

> **This is exactly why columnar databases (ClickHouse, Redshift, Parquet) exist.** They store data in SoA format on disk. An analytics query that sums one column out of 50 reads 1/50th of the data a row-store would.

---

# Part 4: False Sharing in Multi-Threaded Code

## 4.1 What Is False Sharing

False sharing occurs when two goroutines update **different variables** that happen to reside on the **same 64-byte cache line**. Even though the variables are logically independent, the CPU cache coherence protocol treats the whole line as shared — forcing expensive invalidations on every write.

**The symptom:** no lock contention, healthy CPU utilisation, but throughput is 3–10× lower than expected. Standard profiling shows nothing. The problem is invisible until you know to look for it.

## 4.2 The MESI Protocol — Why It Hurts

Modern CPUs maintain cache coherence using **MESI** (Modified, Exclusive, Shared, Invalid):

```
Step 1: Core 0 writes counterA
        → broadcasts "INVALIDATE line 0x2000" to all other cores

Step 2: Core 1 wants to write counterB (same cache line)
        → its copy is now INVALID
        → must fetch the full 64B line from L3/RAM (~30–100 ns stall)

Step 3: Core 1 writes counterB
        → broadcasts "INVALIDATE line 0x2000" to all cores

Step 4: Core 0 wants to write counterA again
        → its copy is now INVALID again
        → another 30–100 ns stall

Result: two goroutines serialise on a cache line with zero mutexes.
```

## 4.3 The Bad Code

```go
// ❌ Bad: both counters share a 64-byte cache line
type WorkerMetrics struct {
    RequestsHandled int64  // offset 0
    ErrorsLogged    int64  // offset 8  ← same cache line!
}

var m WorkerMetrics
// goroutine 1 increments m.RequestsHandled
// goroutine 2 increments m.ErrorsLogged
// They invalidate each other's cache line on every write
```

## 4.4 The Fix — Padding to 64 Bytes

```go
// ✅ Good: each counter on its own cache line
type PaddedInt64 struct {
    Value int64
    _     [56]byte  // 8 + 56 = 64 bytes total — one full cache line
}

type WorkerMetrics struct {
    RequestsHandled PaddedInt64
    ErrorsLogged    PaddedInt64
}
// Core 0 writing RequestsHandled does NOT invalidate ErrorsLogged.
// Different cache lines → no coherence traffic between cores.
```

## 4.5 Benchmark — Run This Yourself

```go
package main

import (
    "fmt"
    "runtime"
    "sync"
    "time"
)

const N = 500_000_000

type SharedCounters struct{ A, B int64 }
type PaddedCounter  struct{ V int64; _ [56]byte }

func runShared() time.Duration {
    var c SharedCounters
    var wg sync.WaitGroup
    wg.Add(2)
    t := time.Now()
    go func() { defer wg.Done(); for i := 0; i < N; i++ { c.A++ } }()
    go func() { defer wg.Done(); for i := 0; i < N; i++ { c.B++ } }()
    wg.Wait()
    return time.Since(t)
}

func runPadded() time.Duration {
    var c [2]PaddedCounter
    var wg sync.WaitGroup
    wg.Add(2)
    t := time.Now()
    go func() { defer wg.Done(); for i := 0; i < N; i++ { c[0].V++ } }()
    go func() { defer wg.Done(); for i := 0; i < N; i++ { c[1].V++ } }()
    wg.Wait()
    return time.Since(t)
}

func main() {
    runtime.GOMAXPROCS(2)
    fmt.Printf("False sharing: %v\n", runShared())
    fmt.Printf("Padded:        %v\n", runPadded())
}

// Expected output on a modern machine:
// False sharing:  3.1s
// Padded:         0.9s   ← ~3.5× faster, zero algorithmic change
```

> **Where you will hit this in your systems:**
> - LLM call center agent: per-worker request counters in a shared metrics struct
> - Attendance job: multiple goroutines updating per-department aggregates
> - API server: per-worker error counters or rate-limit token buckets
>
> **Fix:** always pad hot per-goroutine counters to 64 bytes when concurrently written.

---

# Part 5: NUMA Architecture

## 5.1 What Is NUMA

On multi-socket servers, RAM is **not equally accessible** to all cores. Each CPU socket has a local memory bank physically wired to it:

- **Local RAM access:** ~100 ns
- **Remote RAM access (cross-socket):** ~200–400 ns — a **2–4× penalty**

**NUMA = Non-Uniform Memory Access.** It is the default architecture on any AWS instance with 32+ vCPUs, all bare-metal servers, and most production database machines you will ever manage.

## 5.2 Topology of a 2-Socket Server

```
┌─────────────────────────────┐   QPI/UPI    ┌─────────────────────────────┐
│       NUMA Node 0           │◄────────────►│       NUMA Node 1           │
│                             │  ~200-400ns  │                             │
│  Cores 0–15                 │              │  Cores 16–31                │
│  L3 Cache: 32 MB            │              │  L3 Cache: 32 MB            │
│  Local RAM: 64 GB           │              │  Local RAM: 64 GB           │
│  Local access: ~100 ns ✓    │              │  Cross-node: ~250 ns ✗      │
└─────────────────────────────┘              └─────────────────────────────┘

Node distances (from numactl --hardware):
  node   0   1
    0:  10  21    ← local=10, remote=21 means 2.1× penalty
```

## 5.3 Why Databases Suffer Most

PostgreSQL allocates `shared_buffers` at startup. If the OS allocates this pool across both NUMA nodes, every buffer read may cross the interconnect — and Postgres reads its buffer pool **millions of times per second**.

The result: a server with *more RAM and more cores* running *slower* than the old single-socket machine it replaced. DBAs get confused. Performance reviews happen. It's always NUMA.

## 5.4 Diagnosing NUMA Problems

```bash
# 1. Check if the server has multiple NUMA nodes
numactl --hardware

# 2. Check if Postgres is suffering cross-NUMA allocation
numastat -p $(pgrep -f 'postgres -D' | head -1)
# Look for: numa_miss >> 0  and  other_node >> 0

# 3. Check overall memory per node
numastat
```

## 5.5 Fixing NUMA for PostgreSQL

```bash
# Option 1: Pin Postgres to node 0 — both CPU and memory
numactl --cpunodebind=0 --membind=0 /usr/bin/postgres -D /var/lib/postgresql/data

# Option 2: Add to systemd service file
# /etc/systemd/system/postgresql.service
ExecStart=numactl --cpunodebind=0 --membind=0 /usr/bin/postgres $PGARGS

# Option 3: Interleave across both nodes
# (avoids hot-node memory exhaustion on very large servers, worse avg latency)
numactl --interleave=all /usr/bin/postgres -D /var/lib/postgresql/data
```

### postgresql.conf — NUMA-aware settings

```ini
# Keep shared_buffers within one node's RAM
# On a 2-socket 128GB server (64GB per node):
shared_buffers = 48GB      # comfortable within node 0's 64GB

# Reduces TLB pressure on large NUMA buffer pools
huge_pages = on
```

> **Rule of thumb for production servers:**
> - If your EC2 instance has ≥ 32 vCPUs, assume 2 NUMA nodes.
> - If self-hosting, always run `numactl --hardware` before tuning Postgres.
> - Keep `shared_buffers` at 70–75% of **one node's RAM**, not total system RAM.
> - A single `numactl` command = 20–30% throughput improvement, zero code changes.

---

# Part 6: Quick Reference Card

| Concept | One-line rule |
|---|---|
| Cache line size | Always 64 bytes — minimum unit the CPU fetches from RAM |
| Cache miss cost | L1 hit = 1 ns. RAM miss = 100 ns. That is a 100× penalty. |
| Struct layout | Largest fields first. Group bools at end. Verify with `unsafe.Sizeof`. |
| Hot/cold split | Separate frequently-accessed fields from rarely-touched ones. |
| AoS vs SoA | Column operations → SoA. Random record access → AoS is fine. |
| False sharing | Pad hot per-goroutine counters to 64 bytes each. |
| NUMA detection | `numactl --hardware` — if 2+ nodes, NUMA matters. |
| NUMA fix | `numactl --cpunodebind=0 --membind=0 postgres` |
| DB hot/cold | `SELECT` only the columns you need. Split cold columns to a separate table. |
| Measure first | Always benchmark before and after. Use `go test -bench=.` |

---

# Part 7: 20 Practice Questions

Work through these from first principles. No peeking. Reason from the cache line math.

| # | Question |
|---|---|
| 1 | If a CPU needs a value at memory address `0x1040`, what range of addresses gets loaded into cache? |
| 2 | An array of 1,000,000 `int64` values is iterated sequentially. Approximately how many cache line misses occur? |
| 3 | A linked list of 1,000,000 nodes is traversed. Why is the cache miss count potentially much higher than the array case? |
| 4 | You have a struct with fields: `bool` (1B), `int64` (8B), `bool` (1B), `float64` (8B). What is the size of this struct due to padding? |
| 5 | Rewrite the struct from Q4 in optimal field order. What is the new size? |
| 6 | Two goroutines each write to their own `int64` counter 500 million times. They run 10× slower than expected with no locks. What is the likely cause? |
| 7 | What is the minimum struct size that guarantees a field lives on its own cache line? Why? |
| 8 | Explain in one sentence what MESI stands for and why it matters for multi-core performance. |
| 9 | Your HRIS payroll job sums all employee salaries. You have a `[]PayrollRecord` where each record is 64 bytes but salary is only 8 bytes. What percentage of each cache line fetch is wasted? |
| 10 | How would you restructure the data in Q9 to eliminate this waste? What is the trade-off of that restructuring? |
| 11 | A server has 2 NUMA nodes. Core 0 (node 0) allocates a 32 GB buffer. Core 20 (node 1) reads from it constantly. What is the approximate latency penalty vs. local access? |
| 12 | What command tells you whether your PostgreSQL process is suffering from cross-NUMA memory access? |
| 13 | Your Go service has a struct accessed by 8 goroutines concurrently, each writing to its own field. What is the risk, and what is the fix? |
| 14 | When does a cache miss become a cache eviction? What determines which cache line gets evicted? |
| 15 | In a 2-socket NUMA machine with 128 GB RAM total (64 GB per node), what is the maximum safe value for PostgreSQL `shared_buffers`? |
| 16 | Explain why `SELECT * FROM employees` is cache-unfriendly at the PostgreSQL buffer pool level when you only need 3 columns. |
| 17 | A table has: `id` (8B), `name` (varchar), `is_active` (1B), `salary` (8B), `bio` (text), `avatar_url` (varchar). Which columns belong in the main table vs. a split profile table for a hot attendance query? |
| 18 | Write the `numactl` command to pin a PostgreSQL process to NUMA node 0 for both CPU and memory allocation. |
| 19 | Your Go struct is 72 bytes. How many cache lines does one instance span? Does the struct size alone make this a problem? When does it become a problem? |
| 20 | Describe a concrete scenario in your HRIS or LLM call center agent where false sharing could silently destroy throughput. Name the specific goroutines and the specific shared struct. |

---

# Part 8: Mini Project — HRIS Memory Profiler

Build this Go program. It benchmarks the concepts from this guide against real data that mirrors your HRIS workload. Run each benchmark, record the numbers, and **write a comment explaining each result**.

## Project Structure

```
hris-bench/
├── main.go
├── structs.go          // all type definitions
├── bench_access.go     // AoS vs SoA salary sum
├── bench_sharing.go    // false sharing vs padded
└── bench_hotcold.go    // full struct vs hot core
```

## structs.go

```go
package main

import "time"

// ── LAYOUT: naive (bad) ──────────────────────────────────────────
type EmployeeBad struct {
    Active      bool
    ID          int64
    IsManager   bool
    Salary      float64
    DeptID      int32
    HireDate    time.Time
    IsRemote    bool
    FullName    string
}

// ── LAYOUT: optimised (good) ─────────────────────────────────────
type EmployeeGood struct {
    ID          int64
    Salary      float64
    HireDate    time.Time
    FullName    string
    DeptID      int32
    Active      bool
    IsManager   bool
    IsRemote    bool
    _           [1]byte
}

// ── HOT CORE only ────────────────────────────────────────────────
type EmployeeCore struct {
    ID     int64
    DeptID int32
    Active bool
    _      [3]byte  // explicit pad — document intent
}

// ── AoS (bad for column operations) ──────────────────────────────
type PayrollRecord struct {
    EmployeeID int64
    Salary     float64
    Bonus      float64
    TaxRate    float32
}

// ── SoA (good for column operations) ─────────────────────────────
type PayrollBatch struct {
    EmployeeIDs []int64
    Salaries    []float64
    Bonuses     []float64
    TaxRates    []float32
}

// ── FALSE SHARING (bad) ───────────────────────────────────────────
type MetricsBad struct {
    Handled int64
    Errors  int64
}

// ── PADDED (good) ─────────────────────────────────────────────────
type MetricsGood struct {
    Handled int64
    _       [56]byte
    Errors  int64
    _2      [56]byte
}
```

## main.go

```go
package main

import (
    "fmt"
    "unsafe"
)

func main() {
    // ── Task 1: Print and compare struct sizes ──────────────────
    fmt.Println("=== Struct Sizes ===")
    fmt.Printf("EmployeeBad:   %d bytes\n", unsafe.Sizeof(EmployeeBad{}))
    fmt.Printf("EmployeeGood:  %d bytes\n", unsafe.Sizeof(EmployeeGood{}))
    fmt.Printf("EmployeeCore:  %d bytes\n", unsafe.Sizeof(EmployeeCore{}))
    fmt.Printf("PayrollRecord: %d bytes\n", unsafe.Sizeof(PayrollRecord{}))
    fmt.Printf("MetricsBad:    %d bytes\n", unsafe.Sizeof(MetricsBad{}))
    fmt.Printf("MetricsGood:   %d bytes\n", unsafe.Sizeof(MetricsGood{}))
    fmt.Println()

    // ── Task 2: AoS vs SoA ──────────────────────────────────────
    fmt.Println("=== AoS vs SoA (payroll salary sum, 1M records) ===")
    benchAoS()   // implement in bench_access.go
    benchSoA()
    fmt.Println()

    // ── Task 3: False sharing ────────────────────────────────────
    fmt.Println("=== False Sharing (500M increments, 2 goroutines) ===")
    benchShared()  // implement in bench_sharing.go
    benchPadded()
    fmt.Println()

    // ── Task 4: Hot core vs full struct ──────────────────────────
    fmt.Println("=== Hot Core vs Full Struct (dept sum, 1M records) ===")
    benchFullStruct()  // implement in bench_hotcold.go
    benchHotCore()
}
```

## Your Tasks

1. **Implement `bench_access.go`:** fill 1,000,000 `PayrollRecord`s and a `PayrollBatch` with random salaries. Benchmark summing all salaries in each. Print elapsed time.

2. **Implement `bench_sharing.go`:** two goroutines each increment their counter 500M times — once with `MetricsBad`, once with `MetricsGood`. Print elapsed time for both.

3. **Implement `bench_hotcold.go`:** fill 1M `EmployeeBad` and 1M `EmployeeCore`. Sum the `DeptID` field in both. Which is faster and by how much?

4. **Run the program.** Record all 6 numbers. For each pair, calculate the speedup ratio.

5. **Write a comment above each benchmark function** explaining the result in your own words — as if you're explaining it to a colleague.

## Expected Results (try before reading)

```
EmployeeBad:   ~80 bytes    EmployeeGood:  ~56 bytes    EmployeeCore: 16 bytes
AoS sum:       ~4 ms        SoA sum:       ~1.5 ms      (~3× faster)
False sharing: ~3.1s        Padded:        ~0.9s        (~3.5× faster)
Full struct:   ~2× slower than EmployeeCore for the same DeptID sum
```

---

*End of guide. Build the project, run the benchmarks, answer the 20 questions — in that order.*
