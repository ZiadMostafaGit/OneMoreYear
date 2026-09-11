# 🗺️ The God-Level Backend Engineering Roadmap — v3

## From "I can build a REST API" → the engineer who gets handed the hardest system in the company

> **v3 is a rewrite, not a patch.** v2 was a very good *reading list with projects attached*. v3 is a **training program**: every topic is entered through a **failure you have to fix**, every project has **numeric exit criteria**, and every level ends with an **exam you either pass or repeat**. It also fixes the two holes that would have made v2 fatal for its stated goal — there was no algorithms track and no behavioral track, and those are half of every FAANG loop.

---

## 📖 Table of Contents

| # | Section | What it is |
|---|---|---|
| I | [The Five Laws](#i--the-five-laws) | How you're required to learn here |
| II | [The Learning Loop](#ii--the-learning-loop-break--diagnose--theory--rebuild--measure--write) | The 6-step cycle every topic uses |
| III | [The Three Tracks](#iii--the-three-tracks-run-them-in-parallel-every-week) | Depth / Interview / Portfolio |
| IV | [The Portfolio Strategy](#iv--the-portfolio-strategy-how-to-build-projects-nobody-else-has) | What makes a project one-of-a-kind |
| V | [The Spine Project: CHRONOS](#v--the-spine-project-chronos) | One system that grows across all 26 levels |
| VI | [The 8 Flagship Projects](#vi--the-8-flagship-projects) | The ones that get you the interview |
| VII | [Level Map](#vii--the-level-map) | All 14 levels and their dependencies |
| VIII | Levels 0 → 6 + A → J | The actual curriculum |
| IX | [Incident Archaeology](#63---incident-archaeology-rebuild-10-famous-outages) | Rebuild 10 real public outages |
| X | [Assessment & Exit Exams](#-assessment-the-exit-exams) | Proof you actually learned it |
| XI | [Honest Timelines](#-the-honest-timeline) | 3 realistic schedules, no lying |
| XII | [Resume & GitHub Translation](#-turning-this-into-a-resume-and-a-github-that-converts) | How this becomes offers |
| XIII | [The Complete Library](#-the-complete-library) | Books, courses, papers, blogs |

---

## I — The Five Laws

These are not suggestions. They are what separates this roadmap from every "backend roadmap 2026" repo on GitHub.

### Law 1 — Failure First. You do not get theory until you've been hurt by its absence.

Every topic in this roadmap opens with **🔥 The Wall** — a concrete broken system, a load test that collapses, a data corruption you caused, or a benchmark that's 50x slower than it should be. You must reproduce the failure *before* you're allowed to read the explanation.

**Why:** Knowledge acquired to *resolve a felt confusion* is retained roughly permanently. Knowledge acquired from a blog post you agreed with is gone in nine days. Interviewers can hear the difference instantly — the candidate who says "MVCC lets readers not block writers" versus the one who says "I once had a 40-second query because a long-running read transaction blocked autovacuum and the table bloated to 6GB; that's when I actually understood what MVCC costs you."

### Law 2 — Measure Everything. A number or it didn't happen.

Every project in v3 has **📈 Exit Criteria**: specific numbers you must produce and defend. Not "build a cache" — *"p99 read latency drops from X to Y, hit rate ≥ 92% at steady state, and you can explain the 8% miss."*

**Why:** "I built a caching layer" is a claim. "I cut p99 from 340ms to 21ms and here's the flame graph showing where the remaining 21ms lives" is evidence. Senior engineers speak in distributions and tradeoffs; juniors speak in nouns and frameworks.

### Law 3 — Write It Down. Every project ships a document, not just code.

Every flagship project produces a **design doc or teardown post** with: the problem, the options you rejected and why, the measurements, the failure modes you found, and what you'd do differently at 100x scale.

**Why:** Promotion at every large company is decided by written artifacts. Design docs, RFCs, and postmortems *are* the job at senior+. Also brutally practical: a well-written teardown post is the single highest-leverage thing you can put on the internet for getting inbound interest.

### Law 4 — Ship Publicly. If it's not on GitHub with a real README, it doesn't exist.

Every project gets its own repo (not one mega-repo), a README with a diagram and a benchmark chart, and a `make demo` that works on a clean machine.

**Why:** Recruiters and hiring managers scan for 20 seconds. A repo with a graph and a crisp README converts; a repo with 40 files and no README does not — regardless of the code quality inside.

### Law 5 — Review on a Schedule. You will forget 80% of this without spaced repetition.

Maintain one Anki deck (or plaintext equivalent) that you write yourself, one card per non-obvious fact. 15 minutes/day, non-negotiable. Cards you *write* work; decks you *download* don't.

**Why:** This roadmap contains thousands of retrievable facts. Interviews are retrieval under stress. If you can't produce "quorum requires W + R > N" in 2 seconds while someone watches you, you don't know it.

---

## II — The Learning Loop (Break → Diagnose → Theory → Rebuild → Measure → Write)

Every single topic in this document is structured as this 6-step loop. Do not skip steps. Do not reorder them.

```
┌──────────────────────────────────────────────────────────────────────────┐
│  1. 🔥 BREAK      Reproduce the failure. Make it hurt. Take a screenshot. │
│                   You may not read ahead until you've seen it break.     │
├──────────────────────────────────────────────────────────────────────────┤
│  2. 🔎 DIAGNOSE   Form a hypothesis. Instrument. Prove or kill it with    │
│                   evidence — strace, perf, EXPLAIN, tcpdump, pprof.      │
│                   Write the hypothesis down BEFORE you check.            │
├──────────────────────────────────────────────────────────────────────────┤
│  3. 📖 THEORY     NOW read. The article/chapter answers a question you    │
│                   are actively holding in your head. Retention: ~10x.    │
├──────────────────────────────────────────────────────────────────────────┤
│  4. 🛠 REBUILD    Implement the fix. Then implement the *wrong* fix too   │
│                   and prove why it's wrong. Both matter.                 │
├──────────────────────────────────────────────────────────────────────────┤
│  5. 📈 MEASURE    Before/after numbers. Chart it. Find the new bottleneck │
│                   your fix exposed — there is always one.                │
├──────────────────────────────────────────────────────────────────────────┤
│  6. ✍️ WRITE      3–10 paragraphs: what broke, why, what you tried, what  │
│                   the numbers said, what you'd do at 100x scale.         │
└──────────────────────────────────────────────────────────────────────────┘
```

**The compounding effect:** after ~40 of these loops you stop needing the roadmap. You will have built the reflex of "reproduce → instrument → hypothesize → measure," which is the actual skill that makes an engineer valuable. Everything else is vocabulary.

---

## III — The Three Tracks (run them in parallel, every week)

The single biggest structural flaw in v2 was treating this as one linear pipeline. It isn't. Three independent things must be true on offer day, and they train differently.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ TRACK 1 — DEPTH (60% of your time)                                          │
│ Levels 0–6, A–H. Systems knowledge. Builds the engineer.                    │
│ Cadence: deep work blocks, 90–180 min. Progress measured in projects shipped.│
├─────────────────────────────────────────────────────────────────────────────┤
│ TRACK 2 — INTERVIEW (30% of your time)  ← COMPLETELY ABSENT FROM v2         │
│ Level I. Algorithms, data structures, behavioral stories, mock loops.       │
│ Cadence: 45–60 min DAILY from week 1. Never batched. Never skipped.         │
│ You cannot cram this. 300 problems at 2/day = 5 months. Start on day one.   │
├─────────────────────────────────────────────────────────────────────────────┤
│ TRACK 3 — CRAFT & VISIBILITY (10% of your time)                             │
│ Level J. Design docs, code review, OSS contributions, writing, network.     │
│ Cadence: one artifact every 2 weeks. This is what generates inbound.        │
└─────────────────────────────────────────────────────────────────────────────┘
```

> **Read this twice:** A candidate with world-class systems depth and no DSA practice **fails the phone screen and never reaches the system design round.** A candidate with 500 LeetCode problems and no depth gets an L3 offer and stalls there for six years. This roadmap makes you both — but only if you run all three tracks concurrently from week one.

---

## IV — The Portfolio Strategy: how to build projects nobody else has

You correctly identified v2's biggest weakness: **the projects are the same projects everyone builds.** A task manager API. A URL shortener. A blog with GraphQL. A chat app. These are *tutorial completions*, and every hiring manager has seen 4,000 of them. They prove nothing except that you can follow a tutorial.

### The Uniqueness Rubric — score every project before you start it

A project is worth your time only if it scores **≥ 7/10**:

| # | Criterion | Points | Test |
|---|---|---|---|
| 1 | **Non-obvious premise** | 2 | Would a bootcamp grad think of this? If yes, 0 points. |
| 2 | **Produces a measurement or artifact that doesn't exist yet** | 2 | Does it generate a chart, dataset, or comparison someone would actually cite? |
| 3 | **Requires a hard idea to be correct, not just to run** | 2 | Is there an invariant that's *easy to violate silently*? |
| 4 | **Demoable in 60 seconds** | 1 | Can you show it working in one terminal + one graph? |
| 5 | **Buildable solo in ≤ 3 weeks** | 1 | Ambition that never ships is worth zero. |
| 6 | **Has a natural "and then it broke" story** | 1 | Interview gold. Every project must have one. |
| 7 | **You can explain it to a non-specialist in 2 sentences** | 1 | If you can't, recruiters can't pass it along. |

**Worked example — why "URL shortener" scores 2/10 and its replacement scores 9/10:**

| | URL Shortener | `pgshift` — online schema migrator |
|---|---|---|
| Non-obvious premise | ❌ 0 | ✅ 2 — most engineers have never done a zero-downtime migration |
| Novel artifact | ❌ 0 | ✅ 2 — publishes lock-wait/latency graphs during a 50M-row backfill |
| Hard correctness | ❌ 0 | ✅ 2 — dual-write consistency, backfill vs. live-write races |
| Demoable | ✅ 1 | ✅ 1 — live Grafana panel while the migration runs under load |
| ≤ 3 weeks | ✅ 1 | ✅ 1 |
| Breakage story | ❌ 0 | ✅ 1 — "the backfill took an ACCESS EXCLUSIVE lock and took prod down" |
| Explainable | ✅ 1 | ✅ 1 — "changes a database table's shape while it's serving traffic" |
| **Total** | **2/10** | **9/10** |

### The Four Project Archetypes That Always Score High

1. **The Reimplementation with a Twist** — build the thing everyone uses, but with a property nobody's version has (a Redis clone that's *deterministically simulatable*; an HTTP/2 server that *passes the full conformance suite*).
2. **The Instrument** — build the tool that *measures* something people argue about with no data (syscall cost per framework; real latency ladder on your own hardware; goodput under overload).
3. **The Autopsy** — reproduce a famous real-world failure end-to-end, then fix it. Extremely rare, extremely credible.
4. **The Adversary** — build the thing that *breaks* systems: a fuzzer, a consistency checker, a chaos harness, a fault injector. Anyone can build a system; almost nobody can build the thing that proves a system wrong.

> **Rule:** at least **one of your flagship projects must be an Adversary project.** It is the single strongest signal of engineering maturity that exists in a portfolio, because it demonstrates you think in invariants and failure modes rather than features.

---

## V — The Spine Project: CHRONOS

**The problem with v2's portfolio:** 30 disconnected toy projects. Real engineers are hired on the strength of *one system they own deeply*, not 30 they touched once.

**v3 introduces a spine:** a single system you build across the entire roadmap, one milestone per level. By the end it is a real distributed system with tens of thousands of lines, a design doc history, a benchmark suite, and a chaos harness — and you know every line of it.

### What Chronos is

**A durable execution engine.** A mini-[Temporal](https://temporal.io)/AWS-Step-Functions: you write ordinary code, and the engine guarantees it *runs to completion exactly once*, surviving process crashes, machine failures, and multi-day waits — by recording every side effect to a log and deterministically replaying the function after a crash.

**Why this is the perfect spine project:**

- It is a **one-line pitch that lands instantly**: *"I built a workflow engine that makes ordinary functions crash-proof."*
- It is **genuinely rare** on a portfolio. Thousands of people have built a chat app. Almost nobody has built durable execution.
- It **structurally requires** almost every topic in this roadmap — you cannot fake your way through it:

| Chronos needs… | …which forces you to master |
|---|---|
| Task storage + leases | Postgres internals, indexes, `SKIP LOCKED`, transaction isolation |
| Exactly-once side effects | Idempotency, outbox pattern, dedup keys, at-least-once vs exactly-once |
| Deterministic replay | Event sourcing, purity/determinism, versioning, side-effect capture |
| Timers ("sleep 30 days") | Timer wheels, durable scheduling, clock skew, monotonic vs wall clock |
| Worker fleet + heartbeats | Leases, failure detection, split-brain, fencing tokens |
| Retries + backoff | Exponential backoff w/ jitter, poison messages, DLQ, circuit breakers |
| Multi-region / HA control plane | Raft, leader election, consensus, replicated state machines |
| Scale-out | Sharding, consistent hashing, rebalancing, hot partitions |
| Multi-tenant SaaS | Isolation, quotas, noisy-neighbor, per-tenant rate limits, cost accounting |
| Observability | OpenTelemetry, traces spanning days, RED metrics, structured logs |
| Correctness proof | Deterministic simulation testing, property tests, TLA+ spec |
| Deployment | Docker, Kubernetes operator, CI/CD, blue-green, migrations under load |

### The 10 Chronos Milestones (one per level)

| Milestone | After Level | What you build | The invariant you must prove |
|---|---|---|---|
| **C0** | 0 | A single-process job runner using raw epoll + a memory-mapped append log | Survives `kill -9` at any instruction with no torn records |
| **C1** | 1 | gRPC API + protobuf task schema + streaming status | Client and server can be independently versioned without breakage |
| **C2** | A | Clean hexagonal core: engine has zero imports from storage or transport | Swap Postgres→in-memory with one line; full engine test suite runs in <2s |
| **C3** | 2 | Postgres-backed durable queue with `FOR UPDATE SKIP LOCKED` leases | No task ever runs twice concurrently, under 64 workers × 10k tasks |
| **C4** | B | Docker Compose stack → Kubernetes with a real CRD + operator | `kubectl apply -f workflow.yaml` runs a workflow; operator reconciles |
| **C5** | D | Deterministic simulation harness: simulated clock, network, disk | 10,000 randomized fault schedules, 0 invariant violations, seed-reproducible |
| **C6** | 3 | Raft-replicated control plane (your own Raft, from 6.5840) | Survives leader kill mid-commit; no committed workflow is ever lost |
| **C7** | 4 | Adaptive concurrency, load shedding, circuit breaking, full observability | Holds p99 SLO under 10x overload by shedding, not collapsing |
| **C8** | 5 | Sharded, multi-tenant, saga support, event-sourced history + snapshots | Rebalance shards live with zero dropped tasks; per-tenant isolation proven |
| **C9** | 6 | The full design doc + public teardown post + hosted demo | A stranger can understand the architecture in 10 minutes |

> **The interview payoff:** when an interviewer asks "tell me about the most technically challenging thing you've built," you have a 45-minute answer with diagrams, measurements, three real bugs you found via simulation testing, and a defensible reason for every tradeoff. That answer alone is worth more than everything else in this document.

---

## VI — The 8 Flagship Projects

These are the satellites around Chronos. Each is standalone, each is rare, each is 1–3 weeks, each scores ≥ 8/10 on the rubric. **Build at least 5.**

| # | Project | Level | One-line pitch | Why it's rare |
|---|---|---|---|---|
| 1 | **`c10k-arena`** | 0 | The same echo server built 6 ways — process-per-conn, thread-per-conn, thread pool, epoll, io_uring, goroutines — benchmarked to 50k connections | Almost nobody has actually *measured* this. The `io_uring` implementation alone puts you in a small club. |
| 2 | **`h2spec-clean`** | 1 | An HTTP/2 server written from scratch (HPACK, framing, flow control, multiplexing) that passes the full `h2spec` conformance suite | "146/146 conformance tests passing" is an unfakeable, verifiable claim |
| 3 | **`pgshift`** | 2 | Zero-downtime online schema migration: expand/contract + chunked backfill of 50M rows while serving 1k writes/s | A skill every company desperately needs and almost no candidate has practiced |
| 4 | **`elle-lite`** | D | A linearizability/consistency checker — and you use it to find a **real** anomaly in a real, misconfigured system | Adversary archetype. Proves you think in invariants. Extremely senior signal. |
| 5 | **`simd`** | D/3 | Deterministic simulation testing harness for Chronos: simulated time, network, and disk; 10k seeds; every bug reproducible from a seed integer | The FoundationDB/TigerBeetle technique. Vanishingly rare in portfolios. |
| 6 | **`overload`** | E | Adaptive concurrency limiter + load-shedding lab that publishes goodput-vs-offered-load curves showing collapse vs. graceful degradation | Everyone talks about backpressure; nobody has the graph |
| 7 | **`incident-lab`** | 6 | Local reproductions of 6 famous public outages (S3 2017, GitHub 2018, Cloudflare 2019, Slack 2022, …), each with a working fix | The Autopsy archetype. Nothing else on a resume reads like this. |
| 8 | **`llmgw`** | G | An LLM inference gateway: token-aware rate limiting, semantic caching, request batching, streaming, per-tenant cost accounting, failover | The most in-demand backend infra skill of 2026, and the projects out there are shallow wrappers |

**Each flagship ships with:** its own repo · a README with an architecture diagram and a results chart · a `make demo` that works clean · a written teardown · benchmarks that someone else can reproduce.

---

## VII — The Level Map

v2 had 9 levels with a confusing 0-1-A-2-B-3-4-5-6 numbering. v3 has 14, named by domain, with explicit dependencies.

```
                  ┌──────────────────────────────────────────┐
                  │ TRACK 2: LEVEL I — THE INTERVIEW MACHINE  │
                  │ DSA · Behavioral · Mocks · Negotiation    │
                  │ RUNS DAILY, WEEK 1 → OFFER DAY            │
                  └──────────────────────────────────────────┘
                  ┌──────────────────────────────────────────┐
                  │ TRACK 3: LEVEL J — SENIOR CRAFT           │
                  │ Design docs · Code review · OSS · On-call │
                  │ ONE ARTIFACT EVERY TWO WEEKS              │
                  └──────────────────────────────────────────┘

TRACK 1 — DEPTH:

  LEVEL 0 ─────────► LEVEL 1 ─────────┐
  Machine &          Protocols &      │
  OS Foundations     Communication    │
      │                               │
      ├──────────► LEVEL C ───────────┤
      │            Language &         │
      │            Runtime Mastery    │
      │                               │
      ├──────────► LEVEL A ───────────┤
      │            Code Architecture  │
      │            & Design Patterns  │
      │                               │
      └──────────► LEVEL 2 ───────────┤
                   Databases &        │
                   Storage Engines    │
                       │              │
                       ▼              ▼
                   LEVEL D ◄────► LEVEL B
                   Testing,       DevOps, Containers
                   Correctness &  & Orchestration
                   Verification
                       │              │
                       ▼              ▼
                   LEVEL 3 ◄────► LEVEL 4 ◄────► LEVEL E
                   Distributed    Infrastructure  Performance
                   Systems Core   & Reliability   Engineering
                       │              │              │
                       └──────┬───────┴──────────────┘
                              ▼
                          LEVEL 5 ◄────► LEVEL F ◄────► LEVEL G
                          Advanced       Cloud & Data    AI/ML Systems
                          Architecture   Platform        Infrastructure
                              │              │              │
                              └──────┬───────┴──────────────┘
                                     ▼
                                 LEVEL H
                                 Security, Privacy
                                 & Compliance
                                     │
                                     ▼
                                 LEVEL 6
                                 System Design Mastery
                                 + Incident Archaeology
```

| Level | Name | New in v3? | Why it exists |
|---|---|---|---|
| **0** | Machine & OS Foundations | rebuilt | The mental hardware model. Everything sits on it. |
| **1** | Protocols & Communication | rebuilt | How processes talk. At the byte level. |
| **C** | Language & Runtime Mastery | 🆕 **NEW** | GC, memory model, profilers, allocator. v2 had zero of this — it's where most "senior" candidates fall apart. |
| **A** | Code Architecture & Patterns | expanded | The layer between "it works" and "it survives 3 years." |
| **2** | Databases & Storage Engines | expanded | Where your data actually lives and how it gets corrupted. |
| **D** | Testing, Correctness & Verification | 🆕 **NEW** | Property tests, fuzzing, DST, Jepsen, TLA+. The rarest and most senior skill set in the industry. |
| **B** | DevOps, Containers & Orchestration | expanded | Own your service end to end. |
| **3** | Distributed Systems Core | expanded | Consensus, replication, time. The hard one. |
| **4** | Infrastructure & Reliability | expanded | Load balancing, caching, rate limiting, resilience, observability. |
| **E** | Performance Engineering | 🆕 **NEW** | Profiling, flame graphs, queueing theory, backpressure, load shedding. v2 said "benchmark it" 12 times and never taught how. |
| **5** | Advanced Architecture | expanded | Microservices, event sourcing, sagas, multi-tenancy, migrations. |
| **F** | Cloud & Data Platform | 🆕 **NEW** | AWS/GCP primitives, object storage, batch, columnar, warehouses, streaming ETL. |
| **G** | AI/ML Systems Infrastructure | 🆕 **NEW** | 2026 reality: inference serving, vector search, RAG infra, GPU scheduling, token economics. |
| **H** | Security, Privacy & Compliance | expanded | AuthN/Z, crypto, threat modeling, PII, GDPR, supply chain. |
| **6** | System Design Mastery | expanded | Synthesis + Incident Archaeology + 20 canonical designs. |
| **I** | 🎯 The Interview Machine | 🆕 **NEW** | DSA, behavioral, mocks, resume, negotiation. **Non-optional.** |
| **J** | 🧭 Senior Craft & Visibility | 🆕 **NEW** | Design docs, RFCs, code review, OSS, on-call, cost, influence. |

---
## ⚡ LEVEL 0 — Machine & OS Foundations

> **Goal:** build the mental hardware model. When someone says "why is it slow," you should be able to name the layer before you open a profiler.
>
> **⏱ Budget:** 90–130 hours · **Chronos milestone:** C0 · **Exit exam:** §0.X

---

### 0.1 — Memory Hierarchy: why your code is 60x slower than it should be

> 🔥 **THE WALL**
> Write two functions that both sum the same 4096×4096 `int32` matrix. One traverses row-major, one column-major. **Identical Big-O. Identical instruction count.** Run them. The column-major version is 5–60x slower depending on your machine.
>
> Now write a struct with two `int64` counters and have two threads increment one each, in a tight loop. Then pad the struct so the counters land on different 64-byte cache lines. **Same work. 3–10x throughput difference.**
>
> **You are not allowed to read the next section until both numbers are on your screen.**

#### 🔎 Diagnose (before you read anything)

Write your hypothesis down first. Then prove it with tools, not vibes:

```bash
perf stat -e cache-references,cache-misses,L1-dcache-load-misses,LLC-load-misses ./bench
perf stat -e cpu-cycles,instructions ./bench      # look at IPC — the smoking gun
```

The instruction counts will be nearly identical. The IPC (instructions per cycle) will not be. **That gap is the entire lesson of this section:** modern CPUs are not instruction-limited, they are memory-limited, and Big-O notation is silent about the thing that dominates.

#### 📖 Theory — you must be able to explain these cold

- The full ladder with **real numbers you measured yourself**: register → L1d → L2 → L3 → DRAM → NVMe → SATA SSD → spinning disk → same-DC network → cross-region network
- **Cache lines** (64 bytes on x86-64): the unit of transfer. Why touching 1 byte costs you 64.
- **Spatial and temporal locality** — and how array-of-structs vs struct-of-arrays flips both
- **False sharing**: two threads, two independent variables, one cache line, and the MESI protocol ping-ponging ownership between cores
- **Cache coherency (MESI/MOESI)**: why an *uncontended atomic increment* still costs ~20ns and a contended one costs ~100ns+
- **Prefetching**: why the hardware prefetcher rescues sequential access and cannot rescue pointer chasing
- **TLB and page faults**: virtual→physical translation, why huge pages matter for databases
- **NUMA**: on a 2-socket box, remote memory is ~1.5–2x the latency of local. Why Postgres/Redis/JVM tuning guides all talk about pinning.
- **Memory-bound vs compute-bound**: the roofline model, in one sentence

#### 📄 Sources

- **"What Every Programmer Should Know About Memory"** — Ulrich Drepper, LWN, 2007. Parts 1–3 and 6. Long, old, still unmatched.
- **"Latency Numbers Every Programmer Should Know"** — Jeff Dean's original; then Colin Scott's interactive version (`colin-scott.github.io/personal_website/research/interactive_latency.html`) which shows how the numbers moved over 20 years. **Note what changed and what didn't** — that's the real insight.
- **"CPU Caches and Why You Care"** — Scott Meyers, CppCon 2014 (video). The best visual explanation that exists.
- **"Gallery of Processor Cache Effects"** — Igor Ostrovsky. Ten short experiments; run all of them.
- **CS:APP Chapter 6** — *Computer Systems: A Programmer's Perspective*, Bryant & O'Hallaron. The canonical textbook treatment. **This book was missing from v2 and shouldn't have been.**
- **"Memory Barriers: a Hardware View for Software Hackers"** — Paul McKenney. For when you're ready for the deep end.

#### 🛠 PROJECT — `latency-lab` ⭐ *(Instrument archetype, 8/10)*

**Not** "write a cache benchmark." Build **a tool that measures the latency ladder of the machine it's running on and emits a personalized latency card.**

```
$ ./latency-lab --full
  ┌─ MEASURED ON: AMD Ryzen 9 5900X · 32GB DDR4-3600 · Samsung 980 Pro ─┐
  │ L1 cache hit ....................       1.1 ns    (Dean 2020: 1.0)  │
  │ L2 cache hit ....................       3.9 ns                      │
  │ L3 cache hit ....................      14.2 ns                      │
  │ DRAM access (random) ............      78.0 ns    (Dean 2020: 100)  │
  │ Atomic increment (uncontended) ..      18.3 ns                      │
  │ Atomic increment (2 threads) ....     104.7 ns    ← 5.7x            │
  │ Mutex lock/unlock (uncontended) .      21.0 ns                      │
  │ Branch mispredict ...............       5.2 ns                      │
  │ NVMe random 4K read .............      82.0 µs                      │
  │ Syscall (getpid) ................     412.0 ns                      │
  │ Context switch (same core) ......       1.9 µs                      │
  │ TCP roundtrip (localhost) .......      28.0 µs                      │
  │ TCP roundtrip (same AZ) .........     310.0 µs                      │
  └──────────────────────────────────────────────────────────────────────┘
```

Include: cache-size discovery by sweeping working-set size and finding the knees in the curve (you can *derive* your L1/L2/L3 sizes from the graph without asking the OS — do that), sequential vs random access at every size, false-sharing demo, and a `--markdown` flag that emits a table for your blog post.

📈 **Exit Criteria**
- [ ] Your derived cache sizes match `lscpu` within one power of two — and if they don't, you can explain why (inclusive vs exclusive caches, prefetching)
- [ ] Row-major vs column-major gap is **explained by measured LLC-miss counts**, not asserted
- [ ] False-sharing fix produces ≥3x throughput improvement and you show the `perf c2c` output
- [ ] A chart in the README: working-set size (log x) vs ns/access (y), with the L1/L2/L3/DRAM knees annotated
- [ ] You can recite the ladder from memory, in orders of magnitude, in under 20 seconds

⛓ **Problem Chain** — *what this drags you into next*
```
"Why is column-major slow?"          → cache lines → why DB rows live in 8KB pages (→ 2.1)
"Why is my atomic counter slow?"     → MESI/contention → why sharded counters exist (→ 4.3)
"Why does DRAM cost 80ns?"           → why an in-memory index still can't do 100M lookups/s (→ 2.1)
"Why is a syscall 400ns?"            → syscall cost → why io_uring exists (→ 0.2, flagship #1)
"Why is same-AZ RTT 300µs?"          → why N+1 queries kill you at 200 rows (→ 1.4, 2.2)
"Column-oriented is faster for scans"→ Parquet, OLAP, vectorized execution (→ F.4)
```

---

### 0.2 — Processes, Threads, Scheduling & the Concurrency Models

> 🔥 **THE WALL**
> Write the dumbest possible TCP echo server: `accept()` → spawn a thread → `read`/`write` loop. Point 10,000 concurrent connections at it with a load generator.
>
> Watch it die. Note *how* it dies: RAM exhaustion from 10k × 8MB default stacks, or `pthread_create: Resource temporarily unavailable`, or the scheduler thrashing at 40% system CPU doing nothing but context switches.
>
> Now do it again with `ulimit -n 1024` in place and watch it fail in a completely different way. **Both failures teach different things.**

#### 🔎 Diagnose

```bash
cat /proc/<pid>/status | grep -i threads     # how many threads before it fell over
pidstat -w -p <pid> 1                        # voluntary vs involuntary context switches/sec
cat /proc/<pid>/limits                       # the fd ceiling you just hit
ss -s                                        # socket state summary — how many in TIME_WAIT?
perf stat -e context-switches,cpu-migrations -p <pid>
strace -c -p <pid>                           # syscall histogram: where is time going?
```

**The key observation:** at 10k threads, your process spends more CPU on scheduling than on echoing bytes. That single measurement is why the entire async I/O industry exists.

#### 📖 Theory

- **Process vs thread vs coroutine vs green thread**: what each costs in bytes and in µs to create — *know the actual numbers on your machine, from `latency-lab`*
- **The Linux scheduler**: CFS/EEVDF, time slices, `nice`, why a CPU-bound thread starves I/O-bound ones, cgroup CPU throttling (this one will bite you in Kubernetes)
- **Context switch anatomy**: register save, page-table swap, TLB flush, cold caches. Why the *cache* cost dwarfs the *switch* cost.
- **Blocking vs non-blocking vs async vs asynchronous-completion**: four different things, routinely conflated
- **The `select` → `poll` → `epoll` → `io_uring` progression**: O(n) per call → O(n) → O(1) readiness → batched submission/completion queues with zero syscalls in the fast path
- **Readiness (epoll/kqueue) vs completion (IOCP/io_uring)** models — the fundamental design split
- **Thread pools, work stealing, M:N scheduling** — how Go's runtime actually schedules goroutines (G-M-P model), why a blocking syscall in Go doesn't stall the world
- **The async/await coloring problem** — why "async all the way down" is contagious, and why Go/Java-21-loom chose virtual threads instead
- **File descriptors**: what "everything is a file" actually costs; fd limits, `EMFILE` vs `ENFILE`
- **Signals, zombie processes, `fork` vs `posix_spawn`, copy-on-write** — and why COW makes Redis `BGSAVE` briefly double memory

#### 📄 Sources

- **OSTEP — *Operating Systems: Three Easy Pieces*** (Arpaci-Dusseau, free at `pages.cs.wisc.edu/~remzi/OSTEP/`). Chapters 4–10 (virtualization), 25–33 (concurrency). **The single best OS resource in existence and it was absent from v2.**
- **"The C10K Problem"** — Dan Kegel. Historically essential; read it as an artifact of how the industry got here.
- **"Blocking I/O, Nonblocking I/O, And Epoll"** — Evan Klitzke (eklitzke.org). Precise and short.
- **"Efficient IO with io_uring"** — Jens Axboe (the author of io_uring). The primary source.
- **"Inside NGINX: How We Designed for Performance and Scale"** — NGINX blog.
- **"The Go scheduler"** — Dmitry Vyukov's design doc + "Scheduling In Go" series by William Kennedy (Ardan Labs). Read all three parts.
- **"Fibers, Oh My!"** — Cloudflare blog. Coroutines in production.
- **"Notes on structured concurrency, or: Go statement considered harmful"** — Nathaniel J. Smith. Changes how you think about spawning anything.

#### 🛠 FLAGSHIP PROJECT #1 — `c10k-arena` ⭐⭐ *(Instrument archetype, 9/10)*

**Build the same TCP echo server six ways, and build the harness that benchmarks them all.**

| # | Model | Language |
|---|---|---|
| 1 | Process per connection (`fork`) | C or Go |
| 2 | Thread per connection | C or Go |
| 3 | Bounded thread pool + blocking I/O | C or Go |
| 4 | Single-threaded `epoll` event loop | C or Go (raw syscalls) |
| 5 | `io_uring` submission/completion queues | C (or Go via `iouring-go`) |
| 6 | Goroutines / virtual threads (runtime-managed M:N) | Go or Java 21+ |

Then build `arena` — the harness that runs all six at 100 / 1k / 10k / 50k concurrent connections and records: throughput (msg/s), p50/p99/p99.9 latency, RSS, thread count, context switches/s, syscalls/s (`strace -c`), and CPU split (user vs sys).

📈 **Exit Criteria**
- [ ] All six pass an identical correctness test (echo integrity under concurrent load, no interleaving)
- [ ] Six-line chart: connections (log) vs p99 latency, and a second chart for RSS
- [ ] You can state **exactly where each model's knee is** and name the resource that caused it
- [ ] The io_uring version shows **measurably fewer syscalls per message** than the epoll version — with the number
- [ ] Written teardown answering: *"at what connection count does thread-per-connection stop being the right answer, and what actually breaks first?"*
- [ ] Bonus: run under `cgroup` CPU limits and show how the ranking changes under CPU throttling (this is the Kubernetes reality)

⛓ **Problem Chain**
```
"10k threads = OOM"           → memory per thread → why goroutine stacks start at 2KB & grow (→ C.2)
"Too many context switches"   → scheduler cost → why event loops win → why Node is single-threaded (→ 0.2)
"epoll is still 2 syscalls"   → io_uring → why syscall cost drives modern I/O design (→ E.2)
"EMFILE at 1024 connections"  → fd limits → why LB connection pooling & keep-alive matter (→ 4.1)
"TIME_WAIT flooded my ports"  → TCP state machine → SO_REUSEADDR, ephemeral port exhaustion (→ 0.3)
"One slow handler stalls all" → head-of-line blocking → why HTTP/2 multiplexes → why HTTP/3 exists (→ 1.2)
"CPU-bound task froze the loop"→ why you need a worker pool next to your event loop (→ A.5)
```

#### 🛠 CORE PROJECT — `minidocker` *(Reimplementation archetype, 8/10)*

Build a container runtime in ~400 lines. Not "use Docker" — *be* Docker:

1. `clone()` with `CLONE_NEWPID | CLONE_NEWNS | CLONE_NEWNET | CLONE_NEWUTS | CLONE_NEWIPC`
2. `pivot_root` into an extracted rootfs (grab one with `docker export`)
3. Mount a fresh `/proc` — then run `ps aux` inside and see only your process
4. Write cgroup v2 files to cap memory at 100MB — then run a memory bomb inside and watch the OOM killer fire *inside the container only*
5. Set up a veth pair + bridge so the container can reach the internet
6. Drop capabilities and set a non-root uid

📈 **Exit Criteria**
- [ ] `ps aux` inside shows PID 1 = your process
- [ ] A 500MB allocation inside is OOM-killed while the host is fine — show the `dmesg` line
- [ ] `curl` works from inside the container
- [ ] You can explain, in one paragraph each, what namespaces, cgroups, and OverlayFS each do — **and what Docker adds on top that you didn't build**

> **Course option (strongly recommended):** **MIT 6.S081 — Operating System Engineering.** You implement pieces of the xv6 kernel: system calls, page tables, a copy-on-write fork, a lazy allocator, a file system with logging, and threads. Free, self-servable, ~80–120h. If you do this, you can skip half of Level 0's core projects — but not `c10k-arena`.

---

### 0.3 — Networking: TCP, DNS, TLS, and the Bytes on the Wire

> 🔥 **THE WALL**
> Three failures to reproduce, in order:
>
> 1. **The 200ms mystery.** Write a client that sends a 5-byte header then a 100-byte body as two separate `write()` calls, and a server that responds. Measure RTT on a loopback. You'll periodically see ~40ms or ~200ms stalls that make no sense. (Nagle's algorithm interacting with delayed ACK.) Fix it with `TCP_NODELAY` and watch the tail vanish.
> 2. **Port exhaustion.** Open and close 60,000 short-lived TCP connections as fast as you can. Watch `ss -s` fill with `TIME_WAIT` and then watch `connect()` start returning `EADDRNOTAVAIL`.
> 3. **The silent hang.** Start a request to a server, then `iptables -A INPUT -p tcp --dport 8080 -j DROP` (black-hole it, don't RST it). Your client hangs. For how long? Until the OS TCP retransmit timeout — potentially **15+ minutes**. This is why "every network call needs a timeout" is the most repeated advice in backend engineering.

#### 🔎 Diagnose

```bash
tcpdump -i lo -nn -A 'port 8080' -w cap.pcap   # then open in Wireshark. Read the actual bytes.
ss -tin                                         # cwnd, rtt, retransmits, per socket
ss -s                                           # TIME_WAIT / CLOSE_WAIT counts
cat /proc/net/netstat | grep -i listen          # ListenOverflows = your accept backlog is full
netstat -s | grep -i retrans
dig +trace example.com                          # full resolution chain, root → TLD → authoritative
openssl s_client -connect example.com:443 -tls1_3 -msg   # watch the actual handshake
```

**Mandatory exercise:** capture one HTTPS request in Wireshark and *annotate every single packet* — SYN, SYN-ACK, ACK, ClientHello, ServerHello, certificate, Finished, application data, FIN. Screenshot it. You will reference this mental image for the rest of your career.

#### 📖 Theory

- **The three-way handshake, and the four-way teardown.** Every state in the TCP state machine: `SYN_SENT`, `ESTABLISHED`, `FIN_WAIT_1/2`, `TIME_WAIT`, `CLOSE_WAIT`. **`CLOSE_WAIT` piling up always means your application forgot to close sockets — know this on sight.**
- **Why `TIME_WAIT` exists** (2×MSL, protecting against delayed duplicates), and why `SO_REUSEADDR`/`SO_REUSEPORT` are not the same thing
- **Flow control (receive window) vs congestion control (cwnd)** — different mechanisms, different problems
- **Slow start, congestion avoidance, fast retransmit, CUBIC vs BBR** — and why a 10MB transfer takes many RTTs to reach full speed. This is why **connection reuse and keep-alive matter more than bandwidth.**
- **Bandwidth-delay product**: why a fat, long link needs big windows
- **Head-of-line blocking** at three layers: TCP, HTTP/1.1 pipelining, HTTP/2 over TCP — and how QUIC/HTTP-3 sidesteps it by moving to UDP
- **MTU, MSS, fragmentation, PMTU black holes** — the classic "works everywhere except over the VPN" bug
- **The accept queue vs the SYN queue**, `somaxconn`, `ListenOverflows` — where dropped connections actually go
- **DNS**: the full chain, TTLs, negative caching, why a low TTL doesn't guarantee fast failover, why DNS-based load balancing is coarse, `SRV` records, DNS in Kubernetes (`ndots:5` and the famous latency bug)
- **TLS 1.3**: handshake in 1-RTT, 0-RTT resumption **and its replay risk**, certificate chains, SNI, ALPN, mTLS, OCSP stapling, why cert expiry causes so many outages
- **NAT, keep-alive, and idle timeouts** — why your long-lived connection dies silently after 350 seconds behind a cloud NAT gateway

#### 📄 Sources

- **"High Performance Browser Networking"** — Ilya Grigorik, free at `hpbn.co`. Chapters 1–4 and 11–12. Still the best networking book for engineers.
- **Beej's Guide to Network Programming** — free. For actually writing socket code.
- **"The Story of One Latency Spike"** — Marek Majkowski, Cloudflare. A real production TCP debugging story, told end to end.
- **"How to receive a million packets per second"** — Cloudflare. Where the ceilings actually are.
- **"HTTP/3 explained"** — Daniel Stenberg (free book) + **"HTTP/2 in Action"**.
- **"Let's code a TCP/IP stack"** — Saminda Peramune / the `saminiir.com` series. Read before CS144.
- **"TLS 1.3: 0-RTT, resumption and anti-replay"** — Cloudflare blog.
- **"Kubernetes DNS `ndots:5` and how it breaks your latency"** — multiple write-ups. A real, common, career-relevant bug.

#### 🛠 FLAGSHIP-GRADE COURSE PROJECT — **Stanford CS144: build your own TCP** ⭐⭐

`cs144.github.io` — free labs, self-servable. You implement, in C++, from nothing:
a byte stream → a stream reassembler → the TCP receiver (window, seqno unwrapping) → the TCP sender (retransmission, RTO backoff, window management) → the full TCP connection state machine → an ARP-speaking network interface → an IP router.

At the end **your TCP talks to real servers on the real internet.**

📈 **Exit Criteria**
- [ ] All lab test suites pass
- [ ] Your stack fetches a real webpage from a real host over the public internet
- [ ] You can draw the TCP state machine from memory
- [ ] You can explain exactly what your retransmission timer does when three packets are lost in a row

> This is the single highest-value fundamentals project in existence. **"I implemented TCP from scratch and it talks to real servers"** ends the networking portion of any interview immediately.

#### 🛠 CORE PROJECT — `wire` *(Instrument archetype, 8/10)*

A CLI that takes one logical operation — "fetch user 42 with their 10 most recent orders" — implemented over **REST-JSON, REST-JSON+gzip, gRPC-protobuf, and GraphQL**, and reports for each: bytes on the wire (headers + body, measured with `tcpdump`, not guessed), number of round trips, TLS handshake cost, syscalls, server CPU-ms, and p99 latency at 1 / 100 / 1000 concurrent clients.

📈 **Exit Criteria**
- [ ] A single comparison table with real measured bytes, not documentation claims
- [ ] Cold-start (new TLS handshake) vs warm (connection reused) numbers shown separately
- [ ] You can answer: *"at what payload size does protobuf's advantage over gzipped JSON disappear?"* — with your own data
- [ ] Published as a blog post. This is the kind of post that gets shared.

⛓ **Problem Chain**
```
"200ms stall"           → Nagle × delayed-ACK → why TCP_NODELAY is in every RPC library (→ 1.2)
"connect() EADDRNOTAVAIL"→ ephemeral ports → why you pool connections (→ 2.2 PgBouncer, 4.1)
"Request hung 15 min"   → no timeout → timeout budgets, deadline propagation (→ 4.4, 3.1)
"Slow start costs RTTs" → keep-alive, HTTP/2, connection warming (→ 1.2)
"CLOSE_WAIT climbing"   → leaked sockets → fd exhaustion → cascading failure (→ 0.4, 4.4)
"Cert expired at 3am"   → cert rotation, mTLS automation, why service meshes exist (→ 5.4, H.2)
"DNS TTL didn't fail over"→ health-check-based LB instead of DNS LB (→ 4.1)
"Works except over VPN" → PMTU black hole → MSS clamping (→ 0.3)
```

---

### 0.4 — Linux as a Debugger: the skill that makes you the person they call

> 🔥 **THE WALL — The Four Sick Servers**
> Build (or clone) four small services, each with exactly one pathology, and **do not label them**. Have a friend, or a script, pick one at random. Your job: identify the fault using only Linux tooling, within 10 minutes, and prove it with evidence.
>
> 1. **Memory leak** — RSS climbs 5MB/min until the OOM killer arrives
> 2. **FD leak** — works fine for 40 minutes, then every request returns `EMFILE`
> 3. **Lock contention** — CPU is at 15%, throughput is at 3% of expected, threads all blocked
> 4. **Runaway syscall loop** — 90% system CPU, ~0% user CPU, and it's not doing any useful work
>
> Then add three harder ones: **disk I/O saturation** (iowait), **a noisy neighbor in a cgroup** (CPU throttling), and **a DNS resolution stall** (5s hangs on every Nth request).

#### 📖 The Toolkit — know what each tool answers, not just its flags

| Question | Tool |
|---|---|
| What's the 60-second overview? | `uptime`, `dmesg -T \| tail`, `vmstat 1`, `mpstat -P ALL 1`, `pidstat 1`, `iostat -xz 1`, `free -m`, `sar -n DEV 1`, `top` |
| What syscalls is it making? | `strace -c -f -p PID` (histogram first, then `-e trace=` to narrow) |
| Where is the CPU going? | `perf top`, `perf record -F 99 -g -p PID` → **flame graph** |
| What files/sockets are open? | `lsof -p PID`, `ls -l /proc/PID/fd \| wc -l` |
| Who's talking to whom? | `ss -tanp`, `ss -tin`, `tcpdump` |
| Is the disk the problem? | `iostat -xz 1` (look at `%util` and `await`), `biolatency` (bcc) |
| Why is memory growing? | `pmap -x`, `/proc/PID/smaps_rollup`, `valgrind --tool=massif`, jemalloc/tcmalloc profilers, `heaptrack` |
| What's the kernel doing? | `bpftrace`, `bcc` tools (`execsnoop`, `opensnoop`, `tcpconnect`, `runqlat`, `offcputime`) |
| Why is it in a container and slow? | `cat /sys/fs/cgroup/cpu.stat` → **`nr_throttled` and `throttled_usec`** |

#### 📖 Methodologies (this is what separates you from someone who knows commands)

- **USE Method** (Brendan Gregg): for every resource — Utilization, Saturation, Errors. A checklist that finds problems *systematically* rather than by intuition.
- **RED Method**: for every service — Rate, Errors, Duration.
- **The 60-second checklist**: the exact 10 commands, in order, from Netflix's playbook.
- **Off-CPU analysis**: when CPU is low but latency is high, profile what threads are *blocked on*, not what they're running. Most engineers never learn this and it's where half of real latency lives.

#### 📄 Sources

- **"Linux Performance Analysis in 60,000 Milliseconds"** — Brendan Gregg, Netflix TechBlog.
- **"Systems Performance: Enterprise and the Cloud" 2nd ed.** — Brendan Gregg. The reference. Chapters 2, 5, 6, 9, 10.
- **"BPF Performance Tools"** — Brendan Gregg. The modern successor to strace-everything.
- **Julia Evans** (jvns.ca) — the zines and posts on strace, tcpdump, containers, and networking. Best on-ramp that exists.
- **"The USE Method"** and **"Off-CPU Analysis"** — brendangregg.com.

#### 🛠 CORE PROJECT — `sickbay` *(Adversary archetype, 8/10)*

Don't just *solve* the four sick servers — **package them.** Build a repo where `make sick-3` launches a containerized service with a randomly-selected injected pathology, and `make diagnose` gives the user a scratchpad. Ship 8 pathologies, each with a hidden `SOLUTION.md` containing the exact command sequence that reveals it and the fix.

📈 **Exit Criteria**
- [ ] 8 reproducible pathologies, each launching with one command on a clean machine
- [ ] Your own median time-to-diagnosis under 10 minutes across all 8, on a re-run with shuffled labels
- [ ] Each `SOLUTION.md` shows the *evidence*, not just the answer (the actual `strace`/`perf`/`ss` output that proves it)
- [ ] One flame graph committed to the repo, annotated

> **Why this scores high:** it's a teaching artifact. It gets stars, it gets used in interviews *as* an interview exercise, and it demonstrates you can think from the perspective of someone who has to debug your system.

---

### 0.X — 🎓 LEVEL 0 EXIT EXAM

Answer without notes. Time-box to 60 minutes.

1. Recite the latency ladder in orders of magnitude, register → cross-region network. Now: how many L1 hits fit in the time of one NVMe read?
2. You have 10,000 idle WebSocket connections. Estimate memory usage under (a) thread-per-connection, (b) an epoll event loop, (c) goroutines. Show your arithmetic.
3. `ss -s` shows 28,000 sockets in `CLOSE_WAIT`. What is wrong, and in whose code?
4. A service shows 8% CPU, 4% iowait, and p99 latency of 3 seconds. Name three plausible causes and the exact command that distinguishes them.
5. Draw the TCP connection lifecycle including `TIME_WAIT`. Why 2×MSL?
6. Your pod's CPU limit is `500m`. Your service does 200ms of CPU work per request at 10 RPS. What is your p99 and why is it far worse than 200ms? (Answer must include the word "throttling" and the CFS quota period.)
7. Explain false sharing to a smart junior engineer in 4 sentences, then give the fix.
8. What actually happens, in order, from `curl https://api.example.com/v1/x` to the first byte returned? Name at least 15 discrete steps.

**Pass = 7/8 answered confidently and correctly.** Below that, redo the failing topic's wall and project.

---

## ⚡ LEVEL 1 — Protocols & Communication

> **Goal:** you should be able to design a wire protocol, defend it, evolve it without breaking clients, and debug it from a packet capture.
>
> **⏱ Budget:** 70–100 hours · **Chronos milestone:** C1 · **Prereq:** 0.3

---

### 1.1 — HTTP & REST: the part beyond CRUD

> 🔥 **THE WALL — The Double Charge**
> Build a `POST /payments` endpoint backed by Postgres. Now write an adversarial client that: sends each request twice concurrently, kills the connection after the server has committed but before it responds, and retries on timeout with no backoff.
>
> **Charge the same card twice.** Then make it impossible. Then prove it's impossible with a test that runs 10,000 racing duplicate requests and asserts the ledger sums correctly.
>
> This one exercise contains: idempotency keys, unique constraints as a correctness tool, the difference between at-least-once delivery and exactly-once *effect*, request-vs-effect deduplication, and why `POST` retries are dangerous in a way `PUT` retries are not.

#### 📖 Theory

- **REST's actual constraints** (Fielding's dissertation, Ch. 5): client-server, stateless, cacheable, layered, uniform interface, HATEOAS. Then be honest: **almost nothing called REST is REST**, and know precisely which constraints your API does and doesn't satisfy.
- **Safety and idempotency as a contract**: `GET`/`HEAD` safe; `PUT`/`DELETE` idempotent; `POST`/`PATCH` neither. Why intermediaries (proxies, CDNs, retrying clients) are allowed to act on this.
- **Idempotency keys**: storage, TTL, the "in-flight" state, what to return on a key collision with a *different* body (409), and how Stripe does it.
- **Status codes as semantics**: 200 vs 201 vs 202 vs 204; 400 vs 404 vs 409 vs 410 vs 422; 429 with `Retry-After`; 502 vs 503 vs 504 (**know exactly who generated each** — that distinction solves outages).
- **Pagination**: offset (and why it breaks at page 5000 — the database must scan and discard), keyset/cursor, opaque cursors, stable sorts, and the deleted-row-shifts-the-page bug.
- **Conditional requests**: `ETag`, `If-None-Match`, `If-Match` for optimistic concurrency — **`If-Match` is how you get compare-and-swap over HTTP**, and nearly nobody uses it.
- **Caching**: `Cache-Control` directives in detail, `s-maxage`, `stale-while-revalidate`, `Vary`, and how a wrong `Vary` header poisons a shared CDN cache for everyone.
- **Versioning**: URL vs header vs media-type; the expand/contract approach; why Stripe's date-based versioning with per-account pinning is the strongest design anyone shipped.
- **Content negotiation, compression, and range requests.**
- **Error format discipline**: RFC 9457 (Problem Details). Machine-readable `type`, human `detail`, stable error codes clients can switch on.

#### 📄 Sources

- **Zalando RESTful API Guidelines** — `opensource.zalando.com/restful-api-guidelines/`. The most complete production API guide published. Read all of it once.
- **Google API Improvement Proposals (AIPs)** — `google.aip.dev`. How Google actually designs APIs internally. Better than most blog advice.
- **"Idempotency Keys"** and **"Designing robust and predictable APIs with idempotency"** — Brandur Leach / Stripe Engineering.
- **"APIs as infrastructure: future-proofing Stripe with versioning"** — Stripe Engineering. The canonical versioning case study.
- **RFC 9110 (HTTP Semantics)** and **RFC 9457 (Problem Details)**. Read RFC 9110 §9 (methods) and §15 (status codes) properly, once. It's shorter than you fear.
- **"Pagination: You're doing it wrong"** / keyset pagination writeups — `use-the-index-luke.com/no-offset`.

#### 🛠 CORE PROJECT — `ledger-api` *(replaces v2's "Task Manager API", 7/10)*

A money-movement API — because money makes correctness non-negotiable and gives you an invariant a test can check.

Requirements, each of which must be **proven by an adversarial test, not just implemented**:
1. `POST /transfers` with idempotency keys — proven by 10,000 racing duplicates producing exactly one transfer
2. Keyset pagination — proven correct while rows are being inserted and deleted mid-pagination
3. Optimistic concurrency via `ETag` + `If-Match` on `PATCH /accounts/{id}` — proven by a lost-update test that fails without it
4. RFC 9457 error bodies with stable machine-readable codes
5. Rate limiting with correct `429` + `Retry-After` + `RateLimit-*` headers
6. `OpenAPI 3.1` spec **generated from the code**, with schema-validation tests in CI so the spec can never drift
7. A **backward-compatibility test suite**: v1 client requests replayed against the v2 server must still pass

📈 **Exit Criteria**
- [ ] `make chaos` runs the duplicate/reorder/kill-connection adversary for 60s; the ledger balances to the cent afterward
- [ ] The lost-update test **fails** when you remove `If-Match` (prove your protection actually protects)
- [ ] Offset pagination benchmark at page 1 vs page 10,000 — show the latency curve and explain it with `EXPLAIN`
- [ ] CI fails if the OpenAPI spec drifts from the implementation

⛓ **Problem Chain**
```
"Double charge"           → idempotency → dedup storage → distributed dedup (→ 3.4, 5.2)
"Idempotency needs state" → where do you store keys? TTL? → Redis vs Postgres tradeoff (→ B.5)
"Page 10000 is slow"      → OFFSET scans and discards → keyset pagination → index design (→ 2.2)
"Two clients overwrote"   → lost update → optimistic locking → MVCC & versioning (→ 2.4)
"Client broke on deploy"  → versioning → expand/contract → contract testing (→ 5.3, D.5)
"429 without Retry-After" → clients hammer harder → retry storms → jitter & circuit breaking (→ 4.4)
"CDN served wrong user's data"→ Vary/cache-key bugs → cache poisoning (→ 4.2, H.3)
```

---

### 1.2 — Binary Protocols: gRPC, Protobuf, HTTP/2 & HTTP/3

> 🔥 **THE WALL — The Field-Number Massacre**
> Define a protobuf message. Serialize a value. Now, in the schema, **rename** a field (fine), **change its type** from `int32` to `int64` (mostly fine), **reuse a deleted field's number** for a different type (catastrophic), and **change `optional` to `repeated`** (interesting).
>
> Deserialize the old bytes with the new schema each time. Watch data silently become wrong — no error, no exception, just corrupted values flowing into your database. **Silent corruption is worse than a crash, and this exercise is why every serious company has schema-evolution rules enforced in CI.**
>
> Second wall: run a gRPC client and server, and `tcpdump` the connection. Find the HTTP/2 `SETTINGS` frame, the `HEADERS` frame with HPACK-compressed pseudo-headers, and the `DATA` frames. Now send 100 concurrent RPCs on one connection and watch them interleave on the same TCP socket.

#### 📖 Theory

- **Protobuf wire format**: varints, zigzag encoding for signed ints, field tags = `(field_number << 3) | wire_type`, length-delimited fields, packed repeated fields. **Hand-decode a protobuf message from hex once.** It takes 20 minutes and permanently demystifies binary protocols.
- **Schema evolution rules**: what's safe (adding optional fields, renaming), what's unsafe (changing types, reusing tags, changing cardinality), and `reserved` as the enforcement mechanism.
- **Protobuf vs JSON vs Avro vs Thrift vs MessagePack vs Cap'n Proto/FlatBuffers** — and the key axis nobody mentions: *is the schema shipped with the data (Avro) or out-of-band (Protobuf)?* That decision determines your whole data platform design.
- **HTTP/2**: binary framing, streams, multiplexing, HPACK header compression (and the dynamic table's security implications), flow control at both stream and connection level, server push (and why it died).
- **HTTP/2's TCP head-of-line blocking** — the multiplexing win is undone by one lost packet. Then **QUIC/HTTP-3**: per-stream loss recovery, 0-RTT, connection migration across networks.
- **gRPC**: the 4 modes (unary, server-stream, client-stream, bidi), deadlines (**gRPC deadlines propagate — this is the correct model, learn it**), metadata, interceptors, status codes, retries + hedging in the service config, load balancing (pick_first, round_robin, xDS).
- **When gRPC is the wrong answer**: browsers (needs grpc-web), public APIs, debuggability, and human-inspectable payloads.

#### 📄 Sources

- **"Protocol Buffers Encoding"** — protobuf.dev. The primary source. Read it with a hex editor open.
- **"Schema evolution in Avro, Protocol Buffers and Thrift"** — Martin Kleppmann. Short and clarifying.
- **DDIA Chapter 4** — "Encoding and Evolution."
- **"HTTP/2 in Action"** — Barry Pollard, or the free **"HTTP/2 explained"** by Daniel Stenberg.
- **"HTTP/3 explained"** — Daniel Stenberg (free).
- **gRPC official docs**: "Core concepts," "Deadlines," "Retry design" (`grpc/proposal` A6). The retry/hedging proposal is worth reading in full — it's a masterclass in reliability design.
- **"gRPC Load Balancing"** — grpc.io blog. Why L4 LBs break gRPC and what to do instead. **This exact issue causes real production incidents.**

#### 🛠 FLAGSHIP PROJECT #2 — `h2spec-clean` ⭐⭐ *(Reimplementation archetype, 9/10)*

**Write an HTTP/2 server from scratch — no HTTP/2 library — and pass the `h2spec` conformance suite.**

You implement: the connection preface, frame parsing (`DATA`, `HEADERS`, `PRIORITY`, `RST_STREAM`, `SETTINGS`, `PING`, `GOAWAY`, `WINDOW_UPDATE`, `CONTINUATION`), **HPACK** (static table, dynamic table, Huffman coding, and the size-update rules), the stream state machine, connection-level and stream-level flow control, and correct error handling (stream errors vs connection errors).

Then run `h2spec` against it and fix every failure.

📈 **Exit Criteria**
- [ ] **`h2spec` reports 146/146 passing** (screenshot it — this is the whole point)
- [ ] Your HPACK encoder is tested against the official `hpack-test-case` fixtures
- [ ] `curl --http2` and a real browser both work against it
- [ ] Benchmark: 100 concurrent streams on one connection vs 100 HTTP/1.1 connections — bytes on the wire and latency
- [ ] A blog post on the three spec details that were hardest to get right (candidates: dynamic table size updates, flow-control window accounting on `RST_STREAM`, `CONTINUATION` frame handling)

> **Why this is elite:** conformance suites are unfakeable. "My hand-written HTTP/2 implementation passes the full conformance suite" is a claim that survives any amount of interviewer skepticism, and there are maybe a few hundred people on earth who can say it.

#### 🛠 CORE PROJECT — Chronos C1

Give Chronos a gRPC API: `StartWorkflow`, `SignalWorkflow`, `GetHistory` (server-streaming), `PollForTask` (long-poll with deadline). Add interceptors for auth, tracing, and panic recovery. Write a client in a **different language** than the server.

📈 **Exit Criteria**
- [ ] Deadline set by the client actually cancels server-side work — prove it with a log line from the cancelled handler
- [ ] Adding a field to the proto doesn't break an old client — prove with a pinned old-client binary in CI
- [ ] `buf lint` + `buf breaking` run in CI and block backward-incompatible schema changes

⛓ **Problem Chain**
```
"Silent field corruption"   → schema evolution rules → registry & CI enforcement (→ F.5)
"gRPC pinned to one backend"→ L4 LB doesn't rebalance HTTP/2 → client-side LB / xDS (→ 4.1, 5.4)
"One slow stream stalls all"→ flow control, HOL blocking → QUIC (→ 1.2)
"Deadline exceeded cascade" → deadline budgets across hops → retry amplification (→ 4.4)
"Payload got huge"          → streaming vs unary → chunking, backpressure (→ E.4)
```

---

### 1.3 — Real-Time: WebSockets, SSE, and the Fan-Out Problem

> 🔥 **THE WALL — The Second Instance**
> Build a WebSocket chat with rooms. Works perfectly. Now run **two** instances behind a load balancer. Alice connects to instance A, Bob to instance B, same room. Alice sends a message. Bob never receives it.
>
> This trivial-seeming failure is the doorway to: sticky sessions, shared state, pub/sub fan-out, the fan-out-vs-fan-in tradeoff, presence tracking, and eventually the reason Slack/Discord/WhatsApp all have a dedicated "channel server" tier.
>
> **Second wall:** kill instance A. Alice's client reconnects to instance B. Which messages did she miss? Now design so she misses none — you have just invented cursors, resumable streams, and at-least-once delivery with client-side dedup.

#### 📖 Theory

- **The four options and their real costs**: polling, long-polling, SSE, WebSocket. SSE is underrated — HTTP-native, auto-reconnect with `Last-Event-ID`, works through every proxy, no upgrade dance. **Use SSE unless you need client→server streaming.**
- **The WebSocket upgrade handshake**, frames, masking, ping/pong keepalives, `permessage-deflate` and its memory cost
- **Fan-out architectures**: direct broadcast, Redis pub/sub relay (lossy!), Kafka-backed (durable), dedicated gateway tier with a routing table
- **Presence** — the hardest part. Who is online? Distributed, eventually consistent, and expensive at scale.
- **Backpressure on a socket**: what happens when your producer is faster than a client's downlink? (Unbounded buffer → OOM. Bounded → you must choose: drop, disconnect, or slow the producer.) **Every real-time system that has ever OOM'd did it here.**
- **Connection state at scale**: 1M connections = how many machines? How much memory per connection? How do you deploy without disconnecting everyone? (Answer: connection draining + client jittered reconnect. Without jitter, your redeploy becomes a self-inflicted DDoS — the **thundering herd on reconnect** is a classic real outage.)
- **Ordering and delivery guarantees** for a chat: per-room ordering, sequence numbers, gap detection, resume tokens

#### 📄 Sources

- **"How Discord handles two and a half million concurrent voice users using WebRTC"** — Discord Engineering.
- **"Real World Elixir/Erlang at Discord"** and **"How Discord Scaled Elixir to 5,000,000 Concurrent Users"** — the fan-out and presence problem, honestly described.
- **"Scaling WhatsApp to 2 million connections per server"** — the famous FreeBSD/Erlang talk. Still the reference point for what's physically possible.
- **"Slack's real-time messaging"** — Slack Engineering, on their edge/flannel architecture.
- **"Server-Sent Events vs WebSockets"** — Ably. Balanced.
- **"Building a distributed WebSocket gateway"** — search Centrifugo / Phoenix Channels design docs.

#### 🛠 CORE PROJECT — `fanout-lab` *(Instrument archetype, 8/10)*

Build **one** real-time app (a live collaborative cursor board — simple, visually demoable) but implement the fan-out layer **four ways**, behind an interface: (a) single instance, in-memory; (b) N instances + Redis pub/sub; (c) N instances + Kafka; (d) N instances + a consistent-hash routing tier where each room has a single owning node.

Then benchmark all four: message fan-out latency p50/p99, messages lost during a rolling restart, memory per connection, and behavior at 10k connections in one room (the "celebrity room" problem).

📈 **Exit Criteria**
- [ ] A table showing **messages lost during a rolling deploy** for each architecture — this is the number that matters and nobody measures it
- [ ] Slow-consumer handling proven: attach a client that reads at 1 msg/s while 10k msg/s are published, and show your server does not grow unbounded
- [ ] Reconnect storm test: kill an instance holding 10k connections; show reconnect latency distribution with and without jitter
- [ ] Answer with data: *"at what fan-out ratio does Redis pub/sub stop being viable?"*

⛓ **Problem Chain**
```
"Two instances can't talk"  → pub/sub → durable log vs lossy bus (→ 3.4)
"Redis pub/sub lost messages"→ no persistence → Redis Streams / Kafka (→ B.5, 3.4)
"Server OOM'd on slow client"→ backpressure → bounded queues → load shedding (→ E.4)
"Redeploy = 10k reconnects" → thundering herd → jitter, staged draining (→ 4.4)
"One room has 100k members" → celebrity problem → fan-out on read vs write (→ 6.2 Design 4)
"Who's online?"             → presence → CRDTs, gossip, TTL heartbeats (→ 3.5, 5.2)
```

---

### 1.4 — GraphQL, BFF & API Gateways: when the shape of the API is the problem

> 🔥 **THE WALL — The 1,247 Queries**
> Build a GraphQL API over a blog: posts → author → comments → comment author. Request 50 posts with authors and comments with comment-authors. Turn on SQL logging.
>
> Count the queries. It will be in the hundreds or thousands. Your one "efficient" GraphQL request just DDoS'd your own database.
>
> Then: send a **deeply nested recursive query** (`post → comments → post → comments → …` 15 levels deep). Watch your server die. You have just discovered that **GraphQL moves the denial-of-service surface from the network to the query planner**, and why every production GraphQL deployment needs depth limits, complexity budgets, and persisted queries.

#### 📖 Theory

- **The N+1 problem** and the **DataLoader** pattern: per-request batching + caching, why it must be per-request (cross-request caching leaks authorization), and why batching windows introduce latency
- **Query complexity analysis and depth limiting**: assigning cost to fields, static analysis vs runtime budget
- **Persisted queries / trusted documents**: the only real answer for public GraphQL — clients send a hash, not a query
- **Federation vs schema stitching vs a monolithic schema**; the Apollo Federation model, entity resolution, the `@key` directive
- **Authorization in GraphQL is genuinely hard** — field-level auth, and why "resolve then filter" leaks data through error messages and timing
- **BFF (Backend for Frontend)**: one API per client type instead of one API for everyone. Often the right answer where people reach for GraphQL.
- **API Gateway responsibilities**: authN, rate limiting, routing, request/response transformation, aggregation — and where the anti-pattern begins (business logic in the gateway)
- **When GraphQL is wrong**: internal service-to-service (use gRPC), file uploads, simple CRUD, when your team can't operate the extra complexity

#### 📄 Sources

- **"GraphQL: A data query language"** — Lee Byron / the original Facebook announcement; and Lee Byron's talks on why it was built (mobile bandwidth, not developer convenience).
- **"GitHub's GraphQL API"** design notes — GitHub Engineering. Includes their rate-limiting-by-complexity model, which is the interesting part.
- **"Shopify's GraphQL rate limiting: calculated query cost"** — Shopify docs. Read how they *price* a query.
- **"Solving the N+1 problem with DataLoader"** — the DataLoader README by Lee Byron is better than most blog posts about it.
- **"GraphQL Federation"** — Apollo docs, plus **"Why we moved off GraphQL"** posts for balance. Read at least one migration-away story.

#### 🛠 CORE PROJECT — `n+1-hunter`

Build the blog API in GraphQL **and** in REST **and** in gRPC. Then build a middleware that counts and logs every database query per HTTP request, plus a CI test that **fails the build if any endpoint exceeds N queries per request**.

📈 **Exit Criteria**
- [ ] Before/after DataLoader: query count 1,247 → ≤ 6 for the same request, with the numbers in the README
- [ ] A malicious 20-level nested query is rejected in <5ms by your complexity analyzer
- [ ] The CI query-budget test is real and blocks a deliberately-added N+1 in a test PR
- [ ] Table comparing the three APIs for the same operation: bytes on wire, DB queries, p99, and lines of client code

⛓ **Problem Chain**
```
"1,247 queries"      → N+1 → DataLoader → batching windows → why batching adds latency (→ E.3)
"Recursive query DoS"→ complexity budgets → persisted queries → why public GraphQL is rare (→ H.3)
"Auth leaked a field"→ field-level authz → policy engines (OPA), ReBAC (→ H.1)
"Cache is useless now"→ GraphQL breaks HTTP caching → why REST+CDN often wins (→ 4.2)
"5 teams, 1 schema"  → federation → schema ownership → Conway's law (→ 5.1)
```

---

### 1.X — 🎓 LEVEL 1 EXIT EXAM

1. A client sends `POST /orders`, times out at 5s, and retries. The server actually succeeded at 5.5s. Design the full fix. Now: where do idempotency records live, what's their TTL, and what happens if the same key arrives with a different body?
2. Hand-decode this protobuf: `08 96 01 12 03 61 62 63`. What are the field numbers, wire types, and values?
3. Why does one lost TCP packet hurt HTTP/2 more than it hurts six parallel HTTP/1.1 connections? What does HTTP/3 change?
4. You have 500k WebSocket connections across 20 nodes. Describe how a message reaches exactly the right 3,000 recipients, and what happens when one node dies.
5. Your GraphQL p99 is 4s. Name five distinct causes, ordered by likelihood, and the instrumentation that distinguishes them.
6. Design a versioning scheme for a public API used by 40,000 integrators, where you need to change a field's type. Walk through the full expand/contract migration and how you know when it's safe to remove the old field.
7. When is SSE strictly better than WebSockets? When is it strictly worse?
8. `502` vs `503` vs `504`: who generated each, and what does each tell you about where to look?

**Pass = 7/8.**

---
## ⚡ LEVEL C — Language & Runtime Mastery 🆕

> **Why this level exists:** v2 was language-agnostic to a fault. But in a real interview loop you write code in *one* language, and the senior signal is knowing what your runtime does underneath: where allocations go, when the GC runs, what the memory model guarantees, and how to profile it. This is where most "5 years experience" candidates get exposed.
>
> **⏱ Budget:** 60–90 hours · **Prereq:** Level 0

### Choose your primary. Then go deep enough to be dangerous.

| | **Go** | **Java/Kotlin** | **Python** | **Rust** |
|---|---|---|---|---|
| Best for | Infra, distributed systems, this roadmap's projects | Large enterprises, Android backend, big-data ecosystem | ML/AI backend, data, rapid services | Systems, performance-critical, new infra |
| FAANG presence | Google, Uber, Cloudflare, Dropbox, K8s ecosystem | Amazon, Netflix, LinkedIn, most of fintech | Meta, Google, all AI companies, Instagram | AWS (Firecracker, S3 components), Cloudflare, Discord |
| Interview coding | Acceptable, verbose for DSA | Common | **Best choice for DSA** — write your LeetCode in Python regardless of your backend language | Rarely chosen; slow to write under time pressure |

> **The pragmatic recommendation for this roadmap:** **Go as primary systems language + Python for interviews and data/AI work.** Go's runtime is small enough to actually understand end-to-end, its concurrency is first-class, and the entire cloud-native ecosystem (Kubernetes, etcd, Prometheus, Docker, Terraform) is written in it — which makes source-diving your best teacher. Add Rust later if you want a differentiator.

---

### C.1 — Memory Model & the Garbage Collector

> 🔥 **THE WALL — The Latency Sawtooth**
> Write a service that allocates a 10MB slice per request and holds it briefly. Load test it. Plot latency over time.
>
> You'll see a **sawtooth**: p50 is fine, but every few seconds p99 spikes by 10–100x. Now find out exactly why: `GODEBUG=gctrace=1` (Go) or `-Xlog:gc*` (JVM). Watch the GC cycles line up with the spikes.
>
> Then fix it three different ways and measure each: (1) reduce allocation rate via object pooling / `sync.Pool`, (2) tune `GOGC`/heap sizing, (3) restructure to avoid heap allocation entirely (escape analysis). **Which one wins, and by how much, is the actual lesson.**

#### 📖 Theory

- **Stack vs heap, and escape analysis**: why `go build -gcflags='-m'` is one of the most useful commands in the language. In the JVM: scalar replacement and escape analysis in C2.
- **How your GC actually works**: Go's concurrent tri-color mark-and-sweep with write barriers, no compaction, `GOGC` as a heap-growth ratio, `GOMEMLIMIT` as the soft ceiling that finally made Go container-friendly. JVM: generational hypothesis, G1's region model, ZGC/Shenandoah's colored pointers and sub-ms pauses.
- **Why GC pauses aren't the whole story**: write barriers, assist work charged to the allocating goroutine, and CPU stolen from your request path. **Throughput cost is usually bigger than pause cost, and everyone measures only pauses.**
- **Allocator behavior**: size classes, arenas, fragmentation, `malloc` vs jemalloc vs tcmalloc, why RSS doesn't go down after a workload spike (returning memory to the OS is a *policy*, not a law).
- **The memory model / happens-before**: what a data race actually is, why `sync/atomic` and `volatile` are not interchangeable, why "it worked in testing" means nothing for races. Read your language's memory model spec — it's short.
- **In containers:** why a JVM/Go process OOM-kills in Kubernetes even with "plenty of heap free" (off-heap, thread stacks, and the container limit counting *everything*). `GOMEMLIMIT` and `-XX:MaxRAMPercentage` exist because of this.

#### 📄 Sources

- **"A Guide to the Go Garbage Collector"** — go.dev official guide. Genuinely excellent; read it twice.
- **"Getting to Go: The Journey of Go's Garbage Collector"** — Rick Hudson, GopherCon 2018.
- **"Go memory model"** — go.dev/ref/mem. Short. Read it once fully.
- **"Java Performance: The Definitive Guide"** — Scott Oaks; or **"Optimizing Java"** — Evans/Gough/Newland.
- **"What Every Programmer Should Know About Memory"** (again — §4, virtual memory) if you're on the systems track.
- **CPython:** "CPython Internals" (Anthony Shaw), the GIL, reference counting + generational GC, and `__slots__`/dataclass memory layout. Plus **PEP 703 (free-threaded CPython)** — know the state of GIL removal; it's a live interview topic in 2026.

#### 🛠 CORE PROJECT — `gc-lab`

Instrument one service under four allocation profiles (tiny short-lived, large short-lived, large long-lived, pointer-heavy graph). For each, publish: allocation rate, GC cycles/s, GC CPU %, p99 latency, RSS over time. Then show the effect of each fix.

📈 **Exit Criteria**
- [ ] Chart: p99 latency over time with GC cycles overlaid — the correlation must be visible
- [ ] You reduce GC CPU by ≥50% on one workload and can explain the mechanism
- [ ] You demonstrate a case where object pooling makes things **worse** (it often does) and explain why
- [ ] You explain from memory why RSS stayed at 4GB after the load test ended

---

### C.2 — Profiling: reading the machine instead of guessing

> 🔥 **THE WALL — Your Intuition Is Wrong**
> Take any service you've written. **Write down where you think the time goes.** Percentages. Commit to it in a file.
>
> Now profile it. You will be wrong — usually badly. Most engineers guess "the database" and find 40% of CPU in JSON serialization, or logging, or `time.Now()`, or reflection.
>
> Repeat this three times over the roadmap. The goal is to stop trusting your intuition and start reaching for the profiler reflexively.

#### 📖 Theory & Toolkit

- **CPU profiling** (sampling): `pprof`, `perf record`, async-profiler (JVM), `py-spy` (Python — works on a *running production process without restarting it*, which is a superpower)
- **Flame graphs**: how to read one in 10 seconds — width = time, y-axis = stack depth, look for wide plateaus. **Icicle graphs** for the inverted view.
- **Off-CPU profiling**: where threads are *blocked* — `offcputime` (bcc), Go's block and mutex profiles. **The single most under-used technique in the industry.** If CPU is low and latency is high, on-CPU profiling tells you nothing.
- **Heap profiling**: `pprof -alloc_space` vs `-inuse_space` (allocation rate vs retained), and the difference between a leak and a cache
- **Continuous profiling in production**: Parca, Pyroscope/Grafana Phlare, Google-Wide Profiling. **Reading GWP's paper is a strong senior signal.**
- **Benchmarking methodology** — this is where most people go wrong:
  - Warm-up, steady state, and why the first 1000 iterations are lies
  - **Coordinated omission** — the reason your load-test p99 is a fantasy. Read Gil Tene. Use an open-loop generator (`wrk2`, `k6` with constant-arrival-rate, `vegeta`) not a closed-loop one.
  - Why the mean is useless and p99 of p99s isn't a thing
  - Statistical significance: run 5x, report distributions, use `benchstat`
  - Measuring on a laptop with turbo boost and thermal throttling ≠ measuring

#### 📄 Sources

- **"How NOT to Measure Latency"** — Gil Tene (video). **Mandatory.** Watch it before you publish any benchmark in this roadmap.
- **"Flame Graphs"** — Brendan Gregg. The original post + the CPU/off-CPU/memory variants.
- **"Profiling Go Programs"** — the official Go blog post + `pprof` docs.
- **"Google-Wide Profiling: A Continuous Profiling Infrastructure for Data Centers"** — Ren et al. (paper).
- **"Systems Performance" 2nd ed.** — Gregg, Ch. 6 (CPUs) and 13 (perf).
- **"Understanding Software Dynamics"** — Richard Sites. Underrated modern book on measuring where time actually goes.

#### 🛠 FLAGSHIP-ADJACENT PROJECT — `syscall-xray` ⭐ *(Instrument archetype, 8/10)*

**How expensive is "hello world" in each web framework?** Nobody has published good data on this.

Build the same trivial JSON endpoint in 8 stacks (Go net/http, Go+Gin, Python+Flask+gunicorn, Python+FastAPI+uvicorn, Node+Express, Node+Fastify, Java+Spring Boot, Rust+Axum). For each, per single request, measure: syscalls made (`strace -c -f`), CPU instructions (`perf stat`), context switches, bytes allocated, p50/p99 at 1 and 500 concurrency, RSS at idle and under load, and cold-start time.

Publish the table, the flame graphs, and — most importantly — **an explanation of *why* the outliers are outliers.**

📈 **Exit Criteria**
- [ ] Reproducible harness (containerized, pinned CPU, `taskset`, turbo disabled) that anyone can rerun
- [ ] All measurements taken with an **open-loop** load generator; you explicitly address coordinated omission
- [ ] A flame graph for the slowest and fastest stacks, annotated
- [ ] Written analysis of the biggest surprise you found

> This kind of post is bookmarked and cited for years. It's also a complete demonstration of measurement rigor — which is exactly what a senior interviewer is probing for.

---

### C.3 — Reading Source Code Like a Senior

> 🔥 **THE WALL** — Clone the Redis source. Answer, using only the source and `gdb`/`rr`: *what exactly happens between `GET foo` arriving on the socket and the reply being written?* Name every function in the path. Then answer: *why is `SET` with an existing key sometimes slower than with a new key?*

**Why this matters:** at FAANG you will be dropped into a 12-million-line codebase and asked to change something in week two. Nobody will explain it. The skill of *orienting in unfamiliar code fast* is more valuable than any framework knowledge, and it is trainable.

**The method:**
1. **Find the entry point** (`main`, the request handler, the CLI parser) and read *outward*, never top-down.
2. **Follow one request end-to-end** with a debugger or added log lines. One path, all the way. Don't browse.
3. **Read the tests first** for unfamiliar modules — they're executable documentation of intent.
4. **`git log -S "symbol"`** to find *why* a line exists. `git blame` → the PR → the discussion. Archaeology beats guessing.
5. **Draw the diagram yourself.** If you can't draw it, you don't understand it.

**Exercises (do 3):**
- Trace a `GET` through Redis (C, ~150k lines — the friendliest large C codebase in existence)
- Trace `kubectl apply` through the Kubernetes API server to a running pod (Go, huge — practice at navigating scale)
- Trace a `SELECT` through SQLite's parser → bytecode VM → B-tree → pager (the best-documented database source there is)
- Trace an HTTP request through Go's `net/http` from `Serve()` to your handler
- Find and read the actual implementation of `sync.Map`, and explain why it exists and when it's the wrong choice

📈 **Exit Criteria:** one written "code tour" post per exercise, with a diagram and permalinks to specific lines.

---

## ⚡ LEVEL A — Code Architecture & Design Patterns

> **Goal:** move from code that works to code that survives three years of other people changing it. This is the layer interviewers probe with "how would you structure this?" and the layer that determines whether you're trusted with a large surface area.
>
> **⏱ Budget:** 60–90 hours · **Chronos milestone:** C2 · **Prereq:** C.1

---

### A.1 — SOLID, and the honest case against it

> 🔥 **THE WALL — The Three-Day Feature**
> Clone a deliberately-bad service (write it yourself in 2 hours, or fork one of the many "legacy code kata" repos). Requirements, in order — **time yourself on each**:
> 1. Add a new payment method → you edit a 300-line `switch` in 4 files
> 2. Write a unit test for the order total calculation → **you can't, without a live database and an SMTP server**
> 3. Change the tax rule for one country → you break checkout for all of them
>
> Now refactor. Then re-do the same three tasks and time yourself again. **The ratio between the two timings is the entire argument for architecture,** and it's a number you can quote in an interview.

#### 📖 Theory

Each SOLID principle, framed as *the pain it prevents* (see v2's treatment, which was good — keep it) — plus the pushback that makes you sound senior rather than dogmatic:

- **SRP** — "one reason to change" is really "one *actor* who requests changes" (Martin's clarification, and it's much more useful than the folk version)
- **OCP** — the trap: you cannot predict which axis will vary. Premature OCP produces abstraction rubble. **Wait for the second instance before abstracting.**
- **LSP** — the classic `Square extends Rectangle`; in practice, the violations you'll hit are in interfaces that throw `NotImplementedError`
- **ISP** — small interfaces. Go's `io.Reader` is a single method and is the most reused abstraction in the language. *Accept interfaces, return structs.*
- **DIP** — the one that actually earns its keep, because it's what makes code testable
- **The counterweights, which you must be able to argue:**
  - **"The Wrong Abstraction"** — Sandi Metz: *duplication is far cheaper than the wrong abstraction*
  - **"A Philosophy of Software Design"** — John Ousterhout: **deep modules** (simple interface, complex implementation) beat many shallow ones; this book directly contradicts parts of Clean Code and is more right
  - **"Goodbye, Clean Code"** — Dan Abramov
  - **Locality of behaviour** vs. separation of concerns — the modern pushback

#### 🛠 CORE PROJECT — `fitness-functions` ⭐ *(Adversary archetype, 8/10)*

Don't just refactor — **make the architecture enforceable by CI.**

Refactor the bad service into layers, then add **automated architecture tests** that fail the build on violation: `import-linter` (Python), `go-arch-lint`/`depguard` (Go), or ArchUnit (Java). Rules like: *the domain package may not import the persistence package; nothing may import the HTTP layer except main; no package may have a cyclic dependency.*

Then open a PR that deliberately violates a rule and screenshot CI rejecting it.

📈 **Exit Criteria**
- [ ] The three timed tasks are ≥3x faster post-refactor — with your actual before/after timings in the README
- [ ] Domain-layer unit tests run with **zero** I/O, in under 2 seconds total
- [ ] Architecture rules enforced in CI, with a screenshot of a rejected violation PR
- [ ] A dependency graph diagram, generated (`godepgraph`, `pydeps`), before and after

> **Why the fitness functions matter so much:** anyone can say "I follow clean architecture." Almost nobody has made it mechanically impossible to violate. That's the difference between an opinion and an engineering practice.

---

### A.2 — The GoF Patterns as They Actually Appear

Keep v2's catalog — it was solid — but change the *pedagogy*. Don't learn patterns from a catalog; learn them from the wild.

> 🔥 **THE WALL** — Before reading any pattern definition: implement a payment system where you must support 6 providers, add logging/retry/caching to any of them without editing them, queue payments for later execution, notify 4 subsystems on completion, and model the payment lifecycle as states with illegal transitions rejected at compile time or by test.
>
> Build it however you want. Then read the pattern catalog and **find out which patterns you reinvented, which you should have used, and which you used badly.** Discovering that you independently invented Strategy and Decorator is worth 50 pages of reading.

#### 🛠 PROJECT — `pattern-archaeology` ⭐ *(Instrument archetype, 8/10)*

**Write the definitive post on design patterns in a real codebase.** Pick one large open-source project you'll use anyway (Kubernetes, Django, Redis, Postgres, Kafka) and find *real, cited* instances of at least 10 patterns — with permalinks to the exact lines, an explanation of the problem it solved there, and a note on where the textbook version was deliberately deviated from.

📈 **Exit Criteria**
- [ ] ≥10 patterns, each with a GitHub permalink to real production code
- [ ] At least 3 instances where the codebase *deviated* from the textbook pattern, with your analysis of why
- [ ] At least 1 instance you judge to be an over-application, argued
- [ ] Published; this is a genuinely useful artifact for other engineers

#### 🛠 PROJECT — `chaos-payments` (the pattern-driven build)

Build the payment system from The Wall properly, deliberately using: **Strategy** (providers), **Decorator** (retry/log/cache/metrics wrappers, composable in any order), **Command** (each payment is a serializable, queueable, replayable object), **Observer** (completion fan-out), **State** (lifecycle machine that rejects illegal transitions), **Factory** (provider construction from config), **Adapter** (a deliberately awful third-party API you must wrap), **Circuit Breaker** (a Proxy, really).

📈 **Exit Criteria**
- [ ] Adding a 7th provider requires **zero** edits to existing files — prove it with the diff
- [ ] All decorators compose in any order and the test suite proves the ordering semantics
- [ ] The state machine test enumerates all illegal transitions and asserts each is rejected
- [ ] Every provider swapped for a fake in tests; full suite runs offline in <3s

---

### A.3 — Application Architecture: Hexagonal, Repository, Service Layer, CQRS, Outbox

Keep v2's content (it was good) and add these, which were missing:

- **The Transactional Outbox in full** — including the part everyone skips: the **poller vs CDC** decision, ordering guarantees, at-least-once + consumer idempotency, and how the outbox table becomes a hot table you must clean up
- **The Inbox pattern** — the consumer-side twin. Dedup on the receiving end.
- **Transaction script vs domain model** — Fowler's actual guidance: most services should be transaction scripts, and reaching for a rich domain model too early is a common senior-engineer mistake
- **Anemic domain model** — the debate, and why "anemic" is often just fine
- **Modular monolith** — the architecture most teams should choose and almost nobody discusses. Module boundaries enforced in-process, with the *option* to extract later. **Being able to argue for a modular monolith over microservices is a strong senior signal in a design interview** (see also: Shopify's and Amazon Prime Video's public write-ups).
- **Dependency injection without a framework** — constructor injection and `main()` as the composition root. Why DI containers are usually unnecessary.
- **Feature flags and the strangler fig** — how you actually change a running system

#### 🛠 CHRONOS MILESTONE C2

Restructure Chronos into a hexagonal core: `engine/` (pure — no imports of `sql`, `net`, `time`), `ports/` (interfaces), `adapters/` (postgres, memory, grpc, http). The scheduling and state-transition logic must be testable with a **fake clock** and an **in-memory store**.

📈 **Exit Criteria**
- [ ] `go list -deps ./engine` (or equivalent) shows zero infrastructure dependencies — enforced in CI
- [ ] Full engine test suite runs in <2s with no Docker, no network, no real time
- [ ] Swapping Postgres → in-memory is a one-line change in `main()`
- [ ] Time is injectable everywhere: you can advance the clock by 30 days in a test in microseconds — **this becomes the foundation of Level D's simulation testing, which is why it must be right now**

---

### A.4 — Domain-Driven Design (strategic first, tactical second)

Keep v2's content, but reverse the emphasis: **strategic DDD (bounded contexts, context maps, ubiquitous language) is what pays in interviews and in real service decomposition. Tactical DDD (aggregates, value objects) is a code style you may or may not want.**

Additions v2 was missing:
- **EventStorming** — the workshop technique for discovering bounded contexts. Do one solo on a domain you know (run it on paper with sticky notes). It's the fastest way to make bounded contexts click.
- **Context mapping relationship types**: Partnership, Shared Kernel, Customer/Supplier, Conformist, Anti-Corruption Layer, Open Host Service, Published Language, Separate Ways. **Being able to name and choose these in a design interview is a differentiator.**
- **Aggregate design rules** (Vernon's four): reference other aggregates by identity only; one aggregate per transaction; small aggregates; use eventual consistency between aggregates. **The "one aggregate per transaction" rule is the single most practical thing in DDD** and it directly determines your service boundaries.
- **Domain events vs integration events** — the boundary-crossing distinction (Jimmy Bogard).

**Book upgrade:** start with **"Learning Domain-Driven Design"** (Vlad Khononov, 2021) — clearer, shorter, and more current than Evans. Read Evans' Blue Book afterward, as reference.

#### 🛠 PROJECT — `context-map`

Take a real, complex domain you actually understand (ride-hailing, hotel booking, payroll, a hospital, an airline). Produce: an EventStorming photo/diagram, a context map with named relationship types, the ubiquitous language glossary per context, and **a written argument for where you'd draw service boundaries and — critically — where you'd deliberately NOT split.**

📈 **Exit Criteria**
- [ ] ≥5 bounded contexts identified with explicit relationship types
- [ ] At least one place where the same word means different things in two contexts, documented
- [ ] A section titled "Why I would keep these three as one service" — arguing *against* decomposition is the senior move
- [ ] This becomes a reusable 10-minute answer for any "design X" interview in that domain

---

### A.5 — Concurrency Patterns

Keep v2's list (worker pool, fan-out/fan-in, pipeline, semaphore, context propagation, optimistic concurrency) and add what was missing:

- **Structured concurrency** — no goroutine outlives its parent scope; `errgroup`, nurseries, Java's `StructuredTaskScope`. This is the modern answer to leaked goroutines.
- **Goroutine/thread leaks** — the most common Go bug in production. Detect them with `goleak` in every test.
- **Bounded queues everywhere.** An unbounded channel or queue is a latent OOM. **Rule: every queue in your system has a maximum size and a defined policy for what happens when it's full** (block, drop-oldest, drop-newest, reject). Write the policy down.
- **Backpressure vs load shedding vs buffering** — three different responses to overload, and the difference decides whether you degrade or collapse (→ Level E).
- **Singleflight / request coalescing** — N concurrent identical cache misses become 1 backend call. This one pattern prevents a whole class of outage.
- **The actor model** — Erlang/Akka, and why "state owned by one goroutine, communicate via channel" is often better than a mutex
- **Lock-free and wait-free basics** — CAS loops, ABA, and knowing when *not* to reach for them
- **Deadlock, livelock, priority inversion, convoying, thundering herd** — name them, cause each one deliberately, then fix it

#### 🛠 CORE PROJECT — `race-museum` *(Adversary archetype, 8/10)*

Build a repo of **10 deliberately-broken concurrent programs**, each demonstrating a distinct pathology, each with a test that *reliably* fails (this is the hard part — reproducing races deterministically is itself the lesson) and a fix.

Pathologies: data race on a shared map · lost update (read-modify-write) · deadlock via inconsistent lock ordering · goroutine leak on early return · unbounded queue → OOM · thundering herd on cache expiry · double-close of a channel · context not propagated (work continues after cancellation) · time-of-check-to-time-of-use · false sharing.

📈 **Exit Criteria**
- [ ] Every failure is **deterministic** or reproduces within 100 runs — use `-race`, fault injection, or `GOMAXPROCS` manipulation to force it
- [ ] `-race` / TSan is clean after all fixes
- [ ] `goleak` verifies zero leaked goroutines after every test
- [ ] A README table: pathology → symptom in production → detection tool → fix

> **Interview payoff:** "tell me about a concurrency bug you've debugged" is a standard senior question. You'll have ten.

---

### A.X — 🎓 LEVEL A + C EXIT EXAM

1. Your service's p99 spikes every 8 seconds. Walk through your diagnosis, naming the exact commands.
2. Show a flame graph (bring one from your own project) and read it aloud: where's the time, what would you fix first, and what would you expect the improvement to be?
3. Explain why object pooling can *increase* latency.
4. When is duplication better than abstraction? Give a concrete example from your own code.
5. Argue for a modular monolith over microservices for a 15-engineer startup. Now argue the reverse. Which do you actually believe and why?
6. You have `Order` and `Inventory`. A business rule spans both. Do you put them in one aggregate? Walk through the tradeoff.
7. Design a worker pool that (a) bounds concurrency, (b) propagates cancellation, (c) never leaks a goroutine, (d) applies backpressure to the producer. Write it on a whiteboard.
8. What does `go build -gcflags='-m'` tell you and why do you care?

**Pass = 7/8.**

---
## ⚡ LEVEL 2 — Databases & Storage Engines

> **Goal:** stop being a database *user*. Understand the machine well enough that when it misbehaves you can predict what it's doing before you look.
>
> **⏱ Budget:** 120–160 hours · **Chronos milestone:** C3 · **Prereq:** 0.1, 0.4

> **⭐ THE SINGLE BEST THING IN THIS LEVEL: CMU 15-445 / 15-721** (Andy Pavlo, `15445.courses.cs.cmu.edu`). Free lectures, free projects. You implement, in C++, inside the BusTub database: a buffer pool manager with LRU-K replacement, a B+Tree index with concurrent latch crabbing, query execution operators (including hash join and aggregation), and multi-version concurrency control. **v2 omitted this entirely, and it is the highest-value database education available to anyone for free.** Budget 80–120 hours. Do it. It replaces half this level.

---

### 2.1 — Storage Engines: how bytes actually land on disk

> 🔥 **THE WALL — The Torn Write**
> Build the simplest possible durable key-value store: append `key,value` to a file, keep an in-memory hashmap of key → offset.
>
> Now: while it's writing, `kill -9` it. Restart. **Is your data correct?** Run this 500 times in a loop with random kill timing.
>
> You will find: truncated records, records that parse but are garbage, an index that points past EOF, and — the nastiest one — records that *look* valid but are half-old-half-new. Now discover that `write()` returning success means **nothing** was persisted (it's in the page cache), that `fsync()` is what actually persists, that `fsync()` costs ~1ms on spinning disks and ~100µs on NVMe, and that on some filesystems a failed `fsync` marks the pages clean anyway so **retrying `fsync` after an error can lose your data silently** (the "fsyncgate" that hit PostgreSQL).
>
> This one exercise is the entire reason WALs, checksums, and torn-page protection exist.

#### 📖 Theory

- **B-Trees**: pages, branching factor, why a 4-level B-tree indexes billions of rows, splits and merges, write amplification, in-place update, latch crabbing for concurrency, fill factor
- **LSM Trees**: memtable → immutable memtable → SSTables → leveled/tiered compaction, read amplification vs write amplification vs space amplification (**the RUM conjecture: you may optimize two of Read, Update, Memory — never all three**), Bloom filters to skip SSTables, tombstones and why deletes are the hardest operation in an LSM
- **B-Tree vs LSM, honestly**: LSM wins on write throughput and compression; B-Tree wins on predictable read latency and range scans; LSM compaction causes latency spikes and consumes background I/O you must budget for
- **WAL**: write-ahead logging, redo vs undo, ARIES, group commit, `synchronous_commit` levels, checkpointing, and the durability-vs-latency dial
- **Torn pages**: `full_page_writes`, double-write buffers (InnoDB), checksums, and why an 8KB page write is not atomic on a 4KB-sector device
- **MVCC in detail**: PostgreSQL's tuple versions with `xmin`/`xmax`, why `UPDATE` is `DELETE`+`INSERT`, **bloat**, `VACUUM` and autovacuum, transaction ID wraparound (**a real, famous cause of full outages** — Sentry's is the well-known write-up), and how MySQL's undo-log approach differs
- **The buffer pool**: why databases bypass the OS cache and manage their own, clock-sweep eviction, `shared_buffers` sizing, `pg_buffercache`
- **Page layout**: heap pages, tuple headers, HOT updates, TOAST for oversized values, fillfactor
- **Column stores**: layout, dictionary/RLE encoding, vectorized execution, why they're 100x faster for analytics (→ Level F)

#### 📄 Sources

- **DDIA Chapter 3.** Read it twice; second time after the project. *(Check for the 2nd edition — a substantially updated version has been in early release.)*
- **"Database Internals"** — Alex Petrov. Part I is the best single treatment of storage engines in print.
- **CMU 15-445 lectures 3–7** — buffer pool, hash tables, B+Trees, index concurrency.
- **"How RocksDB Works"** and the **RocksDB wiki** — the real-world LSM reference (used by MyRocks, CockroachDB, TiKV, Kafka Streams).
- **"Bitcask: A Log-Structured Hash Table"** — Riak paper. 6 pages. Your v1 target.
- **"PostgreSQL 14 Internals"** — Egor Rogov (free PDF, `postgrespro.com/community/books/internals`). **Outstanding, free, and unknown to most engineers.** Read the MVCC and vacuum chapters at minimum.
- **"Can Applications Recover from fsync Failures?"** — Rebello et al. (paper) + the PostgreSQL "fsyncgate" mailing-list thread.
- **"The RUM Conjecture"** — Athanassoulis et al.

#### 🛠 CORE PROJECT — `crashdb` ⭐ *(Adversary archetype, 9/10)*

Build a storage engine **and the harness that tries to destroy it.** The harness is what makes this project rare.

**The engine** (v1 → v5):
1. Append-only log + in-memory hash index (Bitcask)
2. CRC32 per record + record framing; detect and recover from partial tails
3. Log compaction/merge with hint files
4. Bloom filter per segment
5. WAL + crash recovery with a checkpoint

**The harness — `crashdb-torture`:**
- Runs a random workload while `kill -9`ing the process at random intervals
- Verifies after every restart: **every acknowledged write is present, no unacknowledged write is present, no key has a torn/garbage value, and the index never points outside the file**
- A mode that injects failures at the *syscall* level using `LD_PRELOAD` or a FUSE filesystem: `write()` succeeds but only writes half; `fsync()` returns `EIO`; the file is truncated at a random offset
- Runs 1,000 crash cycles in CI

📈 **Exit Criteria**
- [ ] 1,000 random-kill cycles, zero invariant violations
- [ ] Torn-write injection is caught by checksums 100% of the time (show a failing case *before* you added CRCs)
- [ ] Benchmark: writes/sec with `fsync` per write vs group commit vs no fsync — and a written argument for which one you'd ship and why
- [ ] Bloom filter measurably reduces disk reads for missing keys — with the number and the false-positive rate you configured
- [ ] Written: "what my database guarantees, and what it does not" — a real durability contract

> **Why this beats v2's version:** v2 said "build a Bitcask KV store," which thousands of people have done. **Nobody builds the crash-torture harness.** The harness is the senior artifact — it demonstrates that you think about correctness as something to be *proven*, not assumed.

⛓ **Problem Chain**
```
"kill -9 corrupted my data"  → fsync, WAL, checksums → durability levels (→ 2.4)
"fsync is 1ms"               → group commit → why throughput ≠ 1/latency (→ E.3)
"Compaction spiked latency"  → background I/O budget → why LSMs have p99 problems (→ E.1)
"Deletes made reads slower"  → tombstones → why range scans degrade in LSMs (→ 2.3)
"My index is bigger than RAM"→ B-tree fanout, buffer pool, page cache (→ 2.2)
"fsync returned EIO"         → fsyncgate → you cannot retry fsync → why DBs panic (→ D.3)
```

---

### 2.2 — PostgreSQL to a Professional Standard

> 🔥 **THE WALL — The Four Disasters**
> Load 50 million rows of realistic data. Then reproduce all four of these, and fix each:
>
> 1. **The index that isn't used.** Write a query with a perfect index on the column — and watch `EXPLAIN` choose a sequential scan anyway. (Causes: low selectivity, stale statistics, a function on the indexed column, type mismatch, `LIKE '%x'`.) You must be able to name *which* one it is.
> 2. **The connection storm.** Open 500 connections. Watch throughput *drop* as concurrency rises. Learn why Postgres's process-per-connection model means more connections = less work done, and why PgBouncer isn't optional.
> 3. **The vacuum death spiral.** Run a long-idle-in-transaction session while doing heavy updates. Watch the table bloat to 5x its size, watch autovacuum fail to reclaim anything, watch queries slow to a crawl. Then find it with `pg_stat_activity` and fix it.
> 4. **The lock pileup.** Run `ALTER TABLE ... ADD COLUMN ... DEFAULT (volatile)` on a large busy table (or an `ALTER` needing an `ACCESS EXCLUSIVE` lock) and watch every query queue behind it. Find the lock tree with `pg_locks`/`pg_blocking_pids`.

#### 📖 Theory

- **`EXPLAIN (ANALYZE, BUFFERS, VERBOSE)`** — read plans fluently. Node types (Seq Scan, Index Scan, Index Only Scan, Bitmap Heap Scan, Nested Loop, Hash Join, Merge Join, Sort, Gather). **Estimated vs actual rows — a big divergence is the #1 signal of a bad plan.** `buffers` tells you cache hit vs disk.
- **Index types and when each wins**: B-tree, Hash, GIN (JSONB, full-text, arrays), GiST (ranges, geometry), SP-GiST, BRIN (huge, naturally-ordered tables — a cheap superpower most people don't know), and **HNSW/IVFFlat via pgvector** (→ Level G)
- **Composite index column order** — the leftmost-prefix rule; why `(a,b)` serves `WHERE a=` and `WHERE a= AND b=` but not `WHERE b=`
- **Covering indexes / `INCLUDE`** → index-only scans, and the visibility-map requirement that makes them work
- **Partial and expression indexes** — often a 10–100x win for almost no cost
- **Statistics and the planner**: `ANALYZE`, `n_distinct`, `default_statistics_target`, extended statistics for correlated columns, and why the planner's row estimate being off by 1000x explains most bad plans
- **Locks**: the full table-lock conflict matrix, row locks, `FOR UPDATE` vs `FOR NO KEY UPDATE` vs `FOR SHARE`, **`SKIP LOCKED`** (the key to building a queue on Postgres — Chronos C3 uses this), advisory locks, `lock_timeout`
- **Connection management**: process-per-connection cost, PgBouncer in session vs transaction vs statement mode, **and what breaks in transaction mode** (prepared statements, `SET`, advisory locks, `LISTEN/NOTIFY`)
- **Partitioning**: declarative range/list/hash, partition pruning, and the operational win — *dropping a partition is instant; `DELETE FROM ... WHERE date <` is not*
- **`pg_stat_statements`, `auto_explain`, `pg_stat_user_tables`, `pgstattuple`** — the observability kit
- **JSONB**: when it's right, GIN index operator classes, and why it's a schema-design smell if it's your primary access path

#### 📄 Sources

- **"Use The Index, Luke!"** — `use-the-index-luke.com`, Markus Winand. Free. **The best practical indexing resource on the internet.** Read all of it.
- **"SQL Performance Explained"** — Winand's book version.
- **"PostgreSQL 14 Internals"** — Egor Rogov (free). Chapters on MVCC, vacuum, indexes, planner.
- **pganalyze blog** — "Explaining the Postgres Query Optimizer" series; the best plan-reading content anywhere.
- **"How Notion sharded their Postgres"** and **"Herding elephants: Lessons learned from sharding Postgres at Notion"** — Notion Engineering. The full multi-year story.
- **"Postgres at Scale"** talks from Citus/Crunchy Data.
- **"Zero-downtime Postgres migrations"** — the `braintree/pg_ha_migrations` README and Gitlab's migration style guide are the two best real-world references.

#### 🛠 FLAGSHIP PROJECT #3 — `pgshift` ⭐⭐ *(Reimplementation archetype, 9/10)*

**Change a table's shape while it's serving 1,000 writes/second, with zero downtime and zero errors.** This is a top-5 real-world backend skill and almost nobody practices it.

**Setup:** a 50M-row `users` table under continuous load (a writer doing 1k inserts/updates per second, a reader doing 500 QPS), with p99 latency monitored on a live Grafana dashboard.

**The migration:** change `user_id` from `INT` to `BIGINT` and split `full_name` into `first_name`/`last_name` — using **expand/contract**:
1. **Expand** — add new nullable columns (fast, no rewrite — but prove it: `ALTER TABLE ADD COLUMN` with a non-volatile default is metadata-only in PG11+; with a volatile default it rewrites the whole table. **Demonstrate both and show the latency graph difference.**)
2. **Dual-write** — application writes both old and new
3. **Backfill** — chunked, throttled, resumable: 5,000 rows per batch, keyed by primary key range, with an adaptive sleep that backs off when replication lag or p99 rises
4. **Verify** — a full comparison pass proving old and new agree for every row, including rows written *during* the backfill
5. **Switch reads** — behind a feature flag, with instant rollback
6. **Contract** — stop dual-writing, drop old columns

Then build `pgshift` itself: the reusable tool that does chunked, throttled, resumable backfills with lag-aware pacing.

📈 **Exit Criteria**
- [ ] **Zero errors and p99 degradation under 20%** for the entire migration, proven by the Grafana screenshot across the whole window
- [ ] Backfill is resumable: kill it at 40%, restart, it completes correctly
- [ ] A verification pass proves 50,000,000/50,000,000 rows match
- [ ] The "wrong way" is demonstrated too: run the naive `UPDATE users SET ...` with no batching, capture the lock wait and the outage, and put **both graphs side by side in the README**
- [ ] Written runbook: "how to change a column type on a hot table," with the checklist and the rollback plan at every step

> **Why this is a 9/10:** it is exactly the work that senior engineers do at scale, it produces two dramatic graphs, and the "here's what happens if you do it naively" comparison is a story that lands in every interview.

⛓ **Problem Chain**
```
"ALTER TABLE locked everything" → lock levels → expand/contract → online DDL (gh-ost, pt-osc)
"Backfill caused replica lag"   → lag-aware throttling → why replicas fall behind (→ 2.5)
"Dual write got inconsistent"   → ordering → outbox/CDC → why you verify, always (→ 5.2, F.5)
"Index build blocked writes"    → CREATE INDEX CONCURRENTLY → and its failure modes
"Planner picked a bad plan after migration" → stats → ANALYZE → plan stability (→ 2.2)
```

---

### 2.3 — The NoSQL Landscape: choosing by access pattern

> 🔥 **THE WALL — The Query You Can't Run**
> Model a Twitter-like feed in **DynamoDB** (or Cassandra) with a single table. Now answer: "give me all posts by users this user follows, newest first."
>
> In SQL: one join. In DynamoDB: **you cannot**, unless you designed the table for that query on day one. Discover that in a wide-column/KV store, **you model the queries, not the data** — and that a partition key choice made in week one determines what your product can do in year three.
>
> Then create a **hot partition**: put all data for one popular user under one partition key and watch throughput collapse to a single shard's limit while the rest of your cluster idles.

#### 📖 Theory

- **Document (MongoDB, DocumentDB)**: embedding vs referencing, the 16MB doc limit as a design constraint, the unbounded-array anti-pattern, indexes on nested fields
- **Wide-column (Cassandra, ScyllaDB, HBase, Bigtable)**: partition key vs clustering key, the query-first data model, denormalize-and-duplicate as *correct* practice, tunable consistency (`ONE`/`QUORUM`/`ALL`), hinted handoff, read repair, anti-entropy, tombstone hell and why `DELETE`-heavy workloads destroy Cassandra
- **Key-value (DynamoDB, Redis)**: single-table design, GSIs and LSIs, partition throughput limits, adaptive capacity, hot keys
- **Graph (Neo4j, dgraph)**: when traversal depth makes SQL joins untenable; index-free adjacency
- **Time-series (TimescaleDB, InfluxDB, Prometheus TSDB)**: hypertables, chunk pruning, downsampling, retention, delta-of-delta + Gorilla compression (**read the Gorilla paper** — it's short and beautiful)
- **Search (Elasticsearch/OpenSearch, Lucene)**: **inverted index construction**, term dictionary, postings lists, segments and merges, analyzers/tokenizers, TF-IDF and BM25 scoring, the deep-pagination problem, and why ES is *not* a system of record. **v2 barely mentioned search; it's a huge real-world category.**
- **NewSQL (CockroachDB, Spanner, TiDB, YugabyteDB)**: distributed SQL with serializable transactions, and what it costs in latency
- **The actual decision framework**: access patterns → consistency needs → scale → operational burden → team familiarity. **In an interview, "I'd use Cassandra" without stating the access pattern is an instant negative signal.**

#### 📄 Sources

- **DDIA Chapter 2** — data models and query languages.
- **"The DynamoDB Book"** — Alex DeBrie. The single-table-design bible. Also his free posts.
- **Dynamo (2007)** and **DynamoDB (USENIX ATC 2022, "Amazon DynamoDB: A Scalable, Predictably Performant, and Fully Available NoSQL Database")** — read the 2022 one; it's more current and describes what they actually learned.
- **Bigtable (2006)** and **Gorilla (VLDB 2015)** papers.
- **"How Discord Stores Billions of Messages"** (Cassandra) → **"How Discord Stores Trillions of Messages"** (ScyllaDB migration). Read them as a pair — it's the best public "we outgrew our first choice" story that exists.
- **"Elasticsearch: The Definitive Guide"** (free, older but the inverted-index chapters are timeless) + the Lucene `postings` format docs.

#### 🛠 CORE PROJECT — `access-pattern-lab`

Implement **the same feature** (a social feed with follows, posts, likes, and a "who liked this" view) on Postgres, DynamoDB-local, and Cassandra/Scylla. Same data volume, same query mix.

📈 **Exit Criteria**
- [ ] Latency table (p50/p99) for each of 6 query types on each of the 3 stores
- [ ] Storage-size comparison, including the duplication cost of the denormalized designs
- [ ] Demonstrate a hot partition and show the throughput collapse graph, then fix it with key sharding/salting
- [ ] Demonstrate one query that is trivial in Postgres and **impossible** in your Cassandra model, and explain what redesign would be required
- [ ] A written decision matrix you'd actually use in a design interview

#### 🛠 BONUS PROJECT — `tinysearch` *(Reimplementation, 8/10)*

Build a search engine from scratch: tokenizer → inverted index → postings lists with skip pointers → BM25 ranking → phrase queries → incremental segment merging. Index all of Wikipedia's abstracts (or 1M documents). Compare recall/latency vs Elasticsearch on the same corpus.

📈 **Exit:** sub-50ms p99 for single-term queries over 1M docs, correct BM25 scores validated against a reference implementation, and a written explanation of segment merging.

---

### 2.4 — Transactions, Isolation & the Anomalies

> 🔥 **THE WALL — Steal Money From Your Own Bank**
> Build accounts and transfers. Then write **five** attack scripts, one per anomaly, each of which *provably* corrupts your data at `READ COMMITTED`:
>
> 1. **Lost update** — two concurrent `balance = balance - 100`, one vanishes
> 2. **Write skew** — the doctor on-call rule: two doctors each check "at least one other on call" simultaneously, both go off-call, hospital has zero doctors. **No row was written twice. No constraint violated. Data is wrong anyway.** This is the anomaly that convinces people isolation levels matter.
> 3. **Read skew** — a report that sums two accounts mid-transfer and sees money that doesn't exist
> 4. **Phantom read** — a range check that passes, then a concurrent insert invalidates it
> 5. **The double-spend under retry** — combine with 1.1's idempotency wall
>
> Then fix each **three different ways** and measure the cost of each: pessimistic locking (`SELECT FOR UPDATE`), optimistic (version column + retry), and `SERIALIZABLE` isolation. **The measured throughput cost of `SERIALIZABLE` under contention is the number you'll quote in interviews.**

#### 📖 Theory

- **ACID, precisely.** Atomicity is not Consistency. "Consistency" in ACID is the *application's* invariant, not the database's — Kleppmann's point, and it's the one most people get wrong.
- **Isolation levels** and the anomalies each permits — build the full matrix yourself. Know that **PostgreSQL's `REPEATABLE READ` is actually snapshot isolation** and that `READ UNCOMMITTED` behaves as `READ COMMITTED`; know that Oracle's "serializable" is snapshot isolation; know that MySQL's default is `REPEATABLE READ` while Postgres's is `READ COMMITTED` — *and that this difference silently changes application correctness when you migrate.*
- **Snapshot isolation and write skew** — SI prevents everything except write skew and phantoms in a specific form. This is exactly why SSI exists.
- **Serializable Snapshot Isolation (SSI)** — PostgreSQL's optimistic approach: track read/write dependencies, abort on dangerous structures. Your app **must** handle `40001` serialization failures with a retry loop. Most don't.
- **2PL vs MVCC vs OCC** — the three families
- **Deadlocks**: how the detector works, victim selection, and the practice that eliminates most of them (**always acquire locks in a consistent global order**)
- **Long-running transactions** — the silent killer: they block vacuum, hold locks, and bloat tables
- **Distributed transactions**: 2PC and its blocking problem (coordinator dies → participants hold locks forever), why sagas exist, Percolator/Spanner-style transactions

#### 📄 Sources

- **DDIA Chapter 7.** Twice, slowly. The best chapter in the book.
- **"A Critique of ANSI SQL Isolation Levels"** — Berenson, Bernstein, Gray et al. (1995). The paper that named the anomalies the standard forgot.
- **"Generalized Isolation Level Definitions"** — Adya et al.
- **"Serializable Snapshot Isolation in PostgreSQL"** — Ports & Grittner (VLDB 2012).
- **Kyle Kingsbury's Jepsen analyses** (`jepsen.io/analyses`) — read three, ideally of databases you use. They are the highest-quality distributed-correctness writing in existence.
- **"Hermitage"** — Martin Kleppmann's repo of concrete test cases showing exactly which anomalies each database permits at each level. **Run it against Postgres and MySQL yourself.**

#### 🛠 CORE PROJECT — `isolation-museum` *(Adversary archetype, 8/10)*

Package all five anomalies as **runnable, deterministic reproductions** against Postgres, MySQL, and one more engine (CockroachDB or SQLite). For each: the attack, the observed corruption, the three fixes, and the measured throughput cost of each fix under 1/8/64 concurrent workers.

📈 **Exit Criteria**
- [ ] All 5 anomalies reproduce deterministically (use advisory barriers/sleeps to force the interleaving)
- [ ] A matrix: anomaly × database × isolation level → occurs / doesn't. **Compare your results to the documentation and note any surprise.**
- [ ] Throughput cost chart: `READ COMMITTED` vs `REPEATABLE READ` vs `SERIALIZABLE` at 1/8/64 workers
- [ ] A working serialization-failure retry loop with exponential backoff, and a measurement of retry rate under contention

---

### 2.5 — Replication, Sharding & Multi-Region

> 🔥 **THE WALL — "My Own Write Disappeared"**
> Set up Postgres primary + async replica. Point writes at the primary and reads at the replica. Now: `POST /profile` then immediately `GET /profile` — and watch your own change not be there.
>
> Then fix it four ways and understand what each costs: (1) read-your-writes via sticky routing to the primary for N seconds, (2) LSN tokens — the client carries the write position and the replica waits for it, (3) synchronous replication (and measure the write-latency cost), (4) don't read from replicas for that endpoint.
>
> Then **kill the primary during a write burst** and promote the replica. **How many acknowledged writes did you just lose?** Measure it. That number is your RPO, and it's the number an interviewer will ask for.

#### 📖 Theory

- **Replication mechanisms**: statement-based (dangerous — nondeterministic functions), WAL/physical (Postgres), logical/row-based (Postgres logical replication, MySQL binlog ROW), and trigger-based
- **Sync vs async vs semi-sync**, `synchronous_commit` levels, quorum commit, and the RPO/latency tradeoff dial
- **Replication lag**: causes (long transactions, single-threaded apply, network, vacuum), monitoring it, and designing around it
- **Consistency guarantees you can actually offer**: read-your-writes, monotonic reads, consistent prefix reads. **Name them precisely; interviewers notice.**
- **Failover**: automatic (Patroni, orchestrator) vs manual, **split-brain and fencing (STONITH)**, and why GitHub's 2018 outage is the canonical cautionary tale
- **Multi-leader**: when (multi-region writes, offline clients), conflict resolution (LWW and why it silently loses data, CRDTs, application-level merge)
- **Leaderless (Dynamo-style)**: quorums, `W + R > N`, sloppy quorums and hinted handoff, read repair, and **why `W + R > N` does *not* actually guarantee you read the latest write** in the presence of concurrent writes or failed writes — Kleppmann's key point
- **Sharding**: range vs hash vs directory; **consistent hashing with virtual nodes** (implement it — it's a common interview ask); rebalancing without downtime; **the cross-shard query and cross-shard transaction problems**; shard key selection and how to fix a bad one (you can't, easily — that's the lesson)
- **Multi-region**: latency floors imposed by the speed of light (~65ms US-east↔US-west RTT is physics, not engineering), active-active vs active-passive, and where consensus becomes too slow

#### 📄 Sources

- **DDIA Chapters 5 & 6.**
- **"Herding elephants: Sharding Postgres at Notion"** — the full case study, including how they chose the shard key.
- **"Vitess"** docs and the YouTube/PlanetScale sharding story.
- **"How GitHub's database outage happened" (Oct 2018 postmortem)** — split-brain across regions. Read the whole thing; you'll rebuild it in Incident Archaeology.
- **"Consistent Hashing with Bounded Loads"** — Google/Vimeo, and the original Karger et al. paper.
- **"Amazon Aurora: Design Considerations..."** (SIGMOD 2017) — how to redesign replication when you control the storage layer. One of the best systems papers of the last decade.

#### 🛠 CHRONOS MILESTONE C3 + PROJECT `replica-lab`

**C3:** Chronos's durable queue on Postgres using `SELECT ... FOR UPDATE SKIP LOCKED` with lease expiry, heartbeats, and visibility timeouts.

📈 **C3 Exit Criteria**
- [ ] 64 concurrent workers × 100,000 tasks: **every task executes exactly once** (verified by a unique-execution table with a unique constraint)
- [ ] Kill a worker mid-task: the task is re-leased after the visibility timeout and completes — and you can explain why this is at-least-once, not exactly-once, and where the idempotency boundary is
- [ ] Throughput benchmark and the identified bottleneck (it will be `fsync` or lock contention on the queue table — know which)
- [ ] You handle the "task took longer than its lease" case correctly (fencing tokens — a lease-expired worker must not be able to commit)

**`replica-lab`:** the four read-your-writes fixes, measured, plus a failover with measured RPO/RTO.

📈 **Exit:** a table of the four approaches with p99 read latency, p99 write latency, and staleness bound for each; plus your measured data loss on unplanned failover.

---

### 2.X — 🎓 LEVEL 2 EXIT EXAM

1. Draw an LSM tree and a B+Tree. For each, give a workload where it wins decisively and explain the amplification factors.
2. `EXPLAIN ANALYZE` shows `rows=1` estimated, `rows=2,400,000` actual. What went wrong, what are the three likely causes, and what do you run first?
3. Explain write skew with an example that isn't the doctors. Which isolation levels prevent it?
4. A table is 40GB but `SELECT count(*)` says 2 million small rows. Diagnose.
5. Design a queue on Postgres that supports 10,000 jobs/sec with exactly-one-consumer semantics and visibility timeouts. What's the bottleneck at 100,000/sec, and what would you change?
6. You must change a column type on a 200M-row table serving 5k QPS. Full plan, including rollback at every step.
7. Your read replica is 45 seconds behind. Give five possible causes and how you'd distinguish them.
8. `W=2, R=2, N=3`. A client writes and gets an ack. Another client reads. Is it guaranteed to see the write? Justify carefully — the naive answer is wrong.
9. Design the partition key for a chat application's message store in Cassandra. Now: what breaks when one channel has 50 million messages?

**Pass = 8/9.** This is the level where most candidates are separated.

---

## ⚡ LEVEL D — Testing, Correctness & Verification 🆕

> **Why this level exists:** v2 had no testing content at all. This is the rarest skill set in the industry and the highest-leverage differentiator on a portfolio. Anyone can build a system; almost nobody can *prove* one is correct. Two of your eight flagship projects live here.
>
> **⏱ Budget:** 70–110 hours · **Chronos milestone:** C5 · **Prereq:** A.3, 2.4

---

### D.1 — The Testing Pyramid, Honestly

> 🔥 **THE WALL** — Take a project you've already built in this roadmap. Run a mutation testing tool (`mutmut`/`cosmic-ray` for Python, `go-mutesting`, PIT for Java). It mutates your source (flips `>` to `>=`, deletes lines) and reports how many mutants your test suite *failed to kill*.
>
> Your coverage is probably 85%. Your mutation score will probably be under 50%. **This is the proof that line coverage measures nothing.**

#### 📖 Theory

- **Test doubles precisely**: dummy, stub, spy, mock, fake. **Prefer fakes.** An in-memory implementation of your repository port is a fake and it's better than a mock, because mocks test that you called a method, not that the behavior is right.
- **London vs Chicago (mockist vs classicist) schools** — and why over-mocking produces suites that pass while production burns
- **The test pyramid vs the testing trophy** — and the real criterion: *how fast does it run and how confident does it make you?*
- **Integration testing with real dependencies**: **Testcontainers**. Never mock the database. Test against real Postgres in Docker. This is now standard practice and if you're still using SQLite-in-tests-Postgres-in-prod you have an entire class of bug you cannot see.
- **Contract testing (Pact)** — consumer-driven contracts, so a provider's deploy can't break a consumer without CI knowing
- **Flaky tests** — the true cost, quarantine policies, and the top causes (time, ordering, shared state, real network)
- **What NOT to test** — and the courage to delete a test

#### 📄 Sources
- **"Unit Testing: Principles, Practices, and Patterns"** — Vladimir Khorikov. The best modern testing book. Replaces a decade of blog arguments.
- **"Working Effectively with Legacy Code"** — Michael Feathers. Seam-finding; how to get untestable code under test.
- **"Software Engineering at Google"** (free online) — Chapters 11–14 on testing at scale. Read the "Large Scale Changes" chapter too; it's unlike anything else published.
- **Testcontainers docs** and **Pact docs**.

---

### D.2 — Property-Based Testing & Fuzzing

> 🔥 **THE WALL** — Take your `crashdb`. Write a property test asserting: *for any sequence of puts, deletes, and gets, the store behaves identically to a Python dict / Go map.*
>
> Let Hypothesis/`testing/quick`/`gopter` generate 10,000 random sequences. **It will find a bug in under a minute** — an ordering issue, an empty-key edge case, a compaction race. Then watch it *shrink* the failing case from 400 operations down to the 3 that actually matter. That shrinking step is the magic.

#### 📖 Theory
- **Properties, not examples**: invariants (`sorted(x)` is always sorted, and a permutation of `x`), round-trips (`decode(encode(x)) == x`), **model-based testing** (compare against a simple reference implementation — the most powerful form), metamorphic relations
- **Stateful property testing** — generate sequences of *operations*, not just values. This is what finds real bugs in systems.
- **Shrinking** — why it's what makes PBT usable
- **Coverage-guided fuzzing**: AFL++, libFuzzer, Go's native `go test -fuzz`, Python's Atheris. **Structure-aware fuzzing** for protocol/parser code.
- **Differential fuzzing** — feed the same input to two implementations and diff the output. This is how real bugs get found in parsers, compressors, and TLS stacks.
- **OSS-Fuzz** — and the fact that you can get your project onto it

#### 🛠 CORE PROJECT — fuzz something real, find a real bug
Fuzz your own `h2spec-clean` HPACK decoder and your `crashdb` record parser. Then go further: pick a small, real open-source parser (a config format, a serialization library, an image decoder) and fuzz it for 24 hours.

📈 **Exit Criteria**
- [ ] ≥3 real bugs found by PBT/fuzzing in your own code, each with the shrunk minimal reproducer committed as a regression test
- [ ] A differential fuzz harness comparing your implementation to a reference
- [ ] Fuzzing wired into CI with a corpus committed
- [ ] **Stretch, and worth a lot:** find a bug in someone else's OSS project and report it responsibly. A merged fix from a fuzzing-found bug is a resume line by itself.

---

### D.3 — Deterministic Simulation Testing (DST)

> **This is the crown jewel of Level D and one of the rarest skills you can demonstrate.** FoundationDB, TigerBeetle, Antithesis, and increasingly the whole serious-distributed-systems world use it. Almost no candidate has heard of it.

> 🔥 **THE WALL** — Your Chronos passes all its tests. Now answer: *what happens if the network delays a message by 8 seconds, then the leader's disk returns `EIO`, then a clock jumps backward 4 seconds, then two workers claim the same lease?*
>
> You cannot test that combination by hand. There are millions of them. **So make the entire universe deterministic and let a random-number generator explore it for you.**

#### 📖 Theory & method

The idea: replace every source of nondeterminism with a *simulated* implementation controlled by a single seeded PRNG.

```
Real world                    Simulation
────────────────────────────────────────────────────────
time.Now()               →    sim.Clock (advances only when you say)
time.Sleep()             →    sim.Sleep (instant; advances virtual time)
net.Dial / RPC           →    sim.Network (can delay, drop, reorder, partition)
os.File / fsync          →    sim.Disk (can tear writes, return EIO, lose the tail)
goroutine scheduling     →    sim.Scheduler (deterministic single-threaded interleaving)
rand.Int()               →    rng.Int() (seeded)
```

Then: `for seed := 0; seed < 100_000; seed++ { run(seed) }`. Each run executes a *different* schedule of failures. When one violates an invariant, **you have a seed integer that reproduces it exactly, forever.**

Requirements: your core logic must be pure and single-threaded (this is why Chronos C2's hexagonal architecture with injectable time was mandatory), and you must define **invariants** that are checked continuously — not just at the end.

#### 📄 Sources
- **"Testing Distributed Systems w/ Deterministic Simulation"** — Will Wilson, Strange Loop 2014 (FoundationDB). **Watch this. It is the single most important 40 minutes in this entire roadmap.**
- **TigerBeetle's VOPR / simulation docs** and their blog posts on DST. Open source, readable, modern.
- **"Simulation testing"** posts from Antithesis, and **Resonate/Temporal**'s writing on deterministic replay.
- **`madsim`** (Rust) and **`sim` / `testing/synctest`** in the Go ecosystem — real implementations to study.
- **FoundationDB paper** (SIGMOD 2021) — §4 on simulation.

#### 🛠 FLAGSHIP PROJECT #5 — `simd` (Chronos milestone C5) ⭐⭐⭐ *(Adversary archetype, 10/10)*

Build the deterministic simulation harness for Chronos.

**Components:**
1. `SimClock` — virtual time, jumps instantly to the next scheduled event
2. `SimNetwork` — configurable per-link latency distribution, drop rate, reordering, duplication, and **partitions** (including asymmetric ones, where A can reach B but not vice versa — these find the nastiest bugs)
3. `SimDisk` — configurable fsync latency, torn writes, `EIO` injection, tail truncation on crash
4. `SimScheduler` — deterministic goroutine/task interleaving from the seed
5. **The invariant checker**, run after every simulated step:
   - No workflow task is ever executed concurrently by two workers
   - Every acknowledged workflow eventually completes or is explicitly failed
   - Workflow history is append-only and never rewritten
   - A workflow's replay produces byte-identical decisions
6. `nemesis` — the fault injector that randomly partitions, crashes, and slows components
7. The runner: N seeds in parallel; on failure, dump the seed + a human-readable event trace

📈 **Exit Criteria**
- [ ] **10,000+ seeds run clean in CI** (nightly), each simulating hours of virtual time in milliseconds of real time
- [ ] **You find at least 3 real bugs in Chronos this way** — document each in the README with its seed and the trace that exposed it. *This is the deliverable.* A DST harness that finds nothing means your fault injection isn't aggressive enough.
- [ ] Any failure is reproducible from its seed integer alone, on any machine
- [ ] A written post: "I found 3 bugs in my workflow engine that no test suite would have caught" — with the traces

> **Interview payoff:** describing this project marks you, instantly and unambiguously, as someone who operates at the level of infrastructure teams at FoundationDB/AWS/Cloudflare. There is no faster credibility signal available in a portfolio.

---

### D.4 — Consistency Checking & Jepsen-style Testing

> 🔥 **THE WALL** — Set up a distributed system with a *deliberately wrong* configuration (Postgres with async replication behind a naive proxy; MongoDB with `w:1`; Redis with Sentinel and default settings; etcd with a too-short election timeout). Now prove it violates the guarantee it appears to offer.
>
> This is harder than it sounds: you must record a history of concurrent operations with real-time bounds and then *check* whether that history is explicable by any valid serialization.

#### 📖 Theory
- **Consistency models as a lattice**: linearizability → sequential → causal → PRAM → eventual; and the transactional side: strict serializable → serializable → snapshot isolation → read committed. Know the Jepsen consistency-model map by heart.
- **Linearizability checking** — the Wing & Gong algorithm, why it's NP-hard in general, and how Knossos/Porcupine make it tractable
- **Elle** — Kyle Kingsbury's transactional-anomaly checker that infers a dependency graph from observed values and finds cycles. **Read the Elle paper**; it's a genuinely clever piece of engineering.
- **Nemesis design** — partitions (simple, bridge, ring, asymmetric), clock skew, process pauses (SIGSTOP is more realistic than SIGKILL), disk faults

#### 📄 Sources
- **Jepsen analyses** at `jepsen.io/analyses` — read the etcd, MongoDB, PostgreSQL, and Redis-Raft ones.
- **"Elle: Inferring Isolation Anomalies from Experimental Observations"** — Kingsbury & Alvaro (VLDB 2020).
- **"Strong consistency models"** and **"The trouble with timestamps"** — aphyr.com.
- **Porcupine** (Go linearizability checker) — small enough to read entirely.

#### 🛠 FLAGSHIP PROJECT #4 — `elle-lite` ⭐⭐ *(Adversary archetype, 9/10)*

1. Build a **history recorder**: a client wrapper that logs every operation with invoke/complete timestamps.
2. Build a **linearizability checker** for a register/KV model (implement Wing-Gong with the standard optimizations, or the P-compositionality trick).
3. Build a **cycle-detecting transactional checker** (a simplified Elle) for read-write registers.
4. Build a **nemesis** that partitions and pauses.
5. **Then use it.** Point it at: your own Chronos, your Raft implementation, and — critically — **a real system you've misconfigured**, and produce a report showing the anomaly you found with the exact history that proves it.

📈 **Exit Criteria**
- [ ] Your checker correctly flags a known-bad history and passes a known-good one (validate against Porcupine's or Knossos's test fixtures)
- [ ] **A real, reproduced anomaly in a real system**, with the history, the visualization, and an explanation of the configuration that caused it
- [ ] A visualization of the violating history (a timeline diagram) in the README
- [ ] Written up as a mini-Jepsen report, in Kingsbury's format

---

### D.5 — Formal Methods, Lite: TLA+

> Not academic. Amazon uses TLA+ on S3, DynamoDB, and EBS, and published a paper about the bugs it caught that testing never would have.

> 🔥 **THE WALL** — Write a TLA+ spec of your Chronos lease protocol. Model check it with TLC. **It will find a bug** — almost certainly a case where a worker whose lease expired still commits a result, or where two workers hold the lease simultaneously across a specific interleaving. Then find that same bug in your implementation.

#### 📖 What to learn
- PlusCal (the friendlier syntax), states/actions/behaviors, safety vs liveness, invariants, temporal properties, model checking with TLC, state-space explosion and how to bound it
- **What TLA+ is for:** protocols and concurrent algorithms — *not* code verification. Spec the 200 lines that matter.

#### 📄 Sources
- **"Learn TLA+"** — learntla.com (Hillel Wayne). The best on-ramp, free.
- **"Practical TLA+"** — Hillel Wayne (book).
- **"How Amazon Web Services Uses Formal Methods"** — Newcombe et al., CACM 2015. **Read this to understand why it's worth your time**; it lists the specific bugs TLA+ found in DynamoDB that had survived extensive testing.
- Leslie Lamport's **TLA+ Video Course**.

#### 🛠 CORE PROJECT — spec two protocols
1. Your Chronos lease/heartbeat protocol
2. A distributed lock or a two-phase commit variant

📈 **Exit Criteria**
- [ ] Both specs model-check clean for safety invariants
- [ ] **At least one real design bug found by TLC**, documented with the counterexample trace TLC produced
- [ ] A written comparison: what TLA+ found vs. what your DST harness found. They catch *different* classes of bug, and articulating that distinction is a genuinely senior insight.

---

### D.X — 🎓 LEVEL D EXIT EXAM

1. Your test suite has 92% coverage and a 40% mutation score. What does that mean and what do you do?
2. Explain deterministic simulation testing to a skeptical manager in 90 seconds, including what it costs to adopt.
3. Give an invariant for a payment system that a unit test cannot check but a simulation harness can.
4. What's the difference between a mock and a fake, and when does over-mocking cause a production incident?
5. `W=1, R=1` on a 3-node cluster with a partition. Sketch a history that violates linearizability. How would a checker detect it?
6. When is TLA+ worth it and when is it theatre?
7. Your CI has 40 flaky tests. What's your plan, in order, and what's your policy going forward?

**Pass = 6/7.**

---
## ⚡ LEVEL B — DevOps, Containers & Orchestration

> **Goal:** own your service end to end. v2's content here was good — v3 keeps the theory and replaces the projects with harder, rarer ones.
>
> **⏱ Budget:** 80–110 hours · **Chronos milestone:** C4 · **Prereq:** 0.2, 0.4

---

### B.1 — Containers (you already built one in Level 0)

Because you built `minidocker` in 0.2, you skip the "what is a namespace" phase and go straight to production concerns.

> 🔥 **THE WALL — The Container That Lies**
> Run a JVM or Go service in a container with `--memory=512m`. Set its heap to 400MB. Watch it get OOM-killed anyway with "plenty of heap free."
>
> Then: run a CPU-bound service with `--cpus=0.5`. Watch p99 latency go to 400ms for work that takes 20ms. Find `nr_throttled` in `cpu.stat`. **CFS quota throttling is one of the most common and least understood causes of latency in Kubernetes,** and it's invisible from inside the container.

#### 📖 Theory (beyond v2)
- Image layers, OverlayFS, multi-stage builds, distroless/scratch, non-root, `HEALTHCHECK`, `.dockerignore`, BuildKit cache mounts, **reproducible builds** and why image digests beat tags
- **Container ≠ VM security boundary.** Namespaces are not a hypervisor. gVisor, Kata, and Firecracker exist because of this. Know when you need one.
- **Signals and PID 1**: why `SIGTERM` doesn't reach your app when it's a child of a shell, `tini`/`--init`, and why this causes 30-second deploys and dropped connections
- **Graceful shutdown**: `SIGTERM` → stop accepting → drain in-flight → close → exit, within `terminationGracePeriodSeconds`. **Getting this wrong drops requests on every single deploy**, and almost every team has this bug.
- **The container memory/CPU model**: cgroup v2, `memory.max` vs `memory.high`, CPU shares vs quota, `GOMEMLIMIT` / `MaxRAMPercentage`, why `nproc` inside a container lies
- **Supply chain**: image signing (cosign/sigstore), SBOMs (syft), vulnerability scanning (trivy/grype), base image policy

#### 🛠 CORE PROJECT — `container-forensics`
Take one service and produce a measured report: naive image vs optimized (size, layers, build time cold/warm, cold-start time), the OOM-under-limit reproduction and its fix, the CPU-throttling reproduction with `nr_throttled` evidence and its fix, and a graceful-shutdown test that proves **zero dropped requests during a rolling restart under load** (this last one is the real deliverable — measure it before and after).

📈 **Exit:** a table with all of it; and a `SIGTERM` handling test that fails when you remove the drain logic.

---

### B.2 — Kubernetes: past `kubectl apply`

> 🔥 **THE WALL — Six Kubernetes Failures**
> Cause each of these deliberately in a local cluster (kind/k3d), diagnose each with `kubectl` + logs only, and write the fix:
> 1. `CrashLoopBackOff` from a missing ConfigMap key
> 2. `ImagePullBackOff` from a private registry with no `imagePullSecret`
> 3. `Pending` forever because no node satisfies the resource request
> 4. **OOMKilled** under a memory limit that seemed generous
> 5. **Requests dropped during a rolling update** because the readiness probe lies (returns 200 before dependencies are ready) — *and* because there's no `preStop` sleep, so the pod stops before endpoints propagate
> 6. **DNS latency**: every request takes an extra 5ms or occasionally 5s — the `ndots:5` + `search` domain problem

#### 📖 Theory
- Keep v2's full list (Pods, Deployments, Services, Ingress/Gateway API, ConfigMaps/Secrets, StatefulSets, DaemonSets, Jobs, PV/PVC, HPA/VPA/Cluster Autoscaler, affinity, taints, CNI, kube-proxy, CoreDNS) — it was accurate.
- **Add the control-plane mental model**, which is what interviews actually probe: **the reconciliation loop**. etcd holds desired state; controllers watch and drive actual → desired; the scheduler is just another controller; the kubelet reconciles pods on a node. **Everything in Kubernetes is `while true { observe; diff; act }`.** If you internalize only one thing, internalize this.
- **What actually happens on `kubectl apply`** — the full path: client-side → API server → authN → authZ (RBAC) → **admission (mutating then validating, then webhooks)** → etcd write → watch event → scheduler binds → kubelet → CRI → CNI → CSI → running container. **This is a top-5 most-asked K8s interview question.**
- **Probes precisely**: liveness (restart me) vs readiness (route to me) vs startup. **A liveness probe that checks a dependency creates cascading restarts** — a classic self-inflicted outage.
- **PodDisruptionBudgets, topology spread, priority & preemption, QoS classes** (Guaranteed/Burstable/BestEffort and eviction order)
- **Operators & CRDs** — the reconciliation pattern as an extension mechanism
- **GitOps** — Argo CD/Flux, drift detection, why `kubectl apply` from a laptop is an anti-pattern

#### 📄 Sources
- **"Kubernetes in Action" 2nd ed.** — Marko Lukša. Still the best book.
- **"Kubernetes: Up and Running"** — Burns, Beda, Hightower *(a book, not an article — v2 miscategorized it)*.
- **"Programming Kubernetes"** — Hausenblas & Schimanski. For operators/CRDs.
- **"Kubernetes Failure Stories"** — `k8s.af`. Read 10. This is the highest-density learning per minute in the whole ecosystem.
- **"Kubernetes the Hard Way"** — Kelsey Hightower. Do it once; you'll never be confused about the control plane again.
- **Borg paper** (2015) and **"Borg, Omega, and Kubernetes"** (CACM 2016) — the why.

#### 🛠 FLAGSHIP-ADJACENT PROJECT — Chronos C4: **write a real Kubernetes Operator** ⭐ *(8/10)*

Not "deploy to Kubernetes" (everyone has done that). **Extend Kubernetes.**

Define a CRD: `kind: Workflow`. Write a controller (controller-runtime / kubebuilder) that reconciles it — creating Jobs, tracking status, handling retries, updating `.status.conditions`, emitting Events, and cleaning up finished workflows. Add a validating admission webhook that rejects malformed workflow specs. Add finalizers so deletion cleans up properly.

📈 **Exit Criteria**
- [ ] `kubectl apply -f workflow.yaml && kubectl get workflows` shows real live status
- [ ] The reconciler is **idempotent and level-triggered** — prove it by deleting a child Job and watching it be recreated
- [ ] It survives being killed mid-reconcile with no duplicate work
- [ ] The admission webhook rejects an invalid spec with a clear message
- [ ] Written explanation of level-triggered vs edge-triggered reconciliation and why Kubernetes chose level

> "I wrote a Kubernetes operator" is a materially different claim from "I've used Kubernetes," and it's the one that gets you infrastructure-team interviews.

---

### B.3 — Message Queues & Task Systems

Keep v2's RabbitMQ/Celery theory (it was accurate and complete) and add the parts that separate a senior from a user:

> 🔥 **THE WALL — The Poison Pill Cascade**
> Build a Celery/worker system consuming from a queue. Now enqueue one message that causes a crash *during* processing (not an exception — a segfault or OOM). With `acks_late=True`, it's redelivered. It crashes the next worker. And the next.
>
> **You have just built a self-replicating worker killer that will take down your entire fleet in 90 seconds.** Watch it happen. Then fix it: delivery counts, DLQ after N attempts, and — the subtle one — **the difference between "the task failed" and "the worker died," which the broker cannot distinguish.**

#### 📖 Additional theory
- **Delivery semantics, precisely**: at-most-once, at-least-once, and why **exactly-once *delivery* is impossible** but exactly-once *processing* is achievable via idempotent consumers or transactional dedup. Being crisp about this distinction is a strong signal.
- **Poison messages, DLQ design, redrive**, and the operational question: who looks at the DLQ? (Answer: nobody, unless you alert on it.)
- **Prefetch/QoS and head-of-line blocking**: one slow message blocking a prefetched batch
- **Queue-per-tenant vs shared queue with priorities** — noisy-neighbor isolation
- **Backpressure**: what happens when the queue grows without bound — and why "the queue absorbs the spike" is only true until memory runs out
- **The scheduling problem**: delayed messages, timer wheels, why "sleep 30 days" is hard, and how Chronos will solve it
- **Kafka vs RabbitMQ vs SQS vs NATS vs Redis Streams** — with the honest guidance: **most task queues should just be Postgres** until proven otherwise (`SKIP LOCKED`, which you built in C3)

#### 🛠 CORE PROJECT — `queue-shootout`
Implement the same job workload on four backends (Postgres `SKIP LOCKED`, Redis Streams, RabbitMQ, Kafka). Measure: throughput, p99 end-to-end latency, message loss on broker restart, message loss on worker `kill -9`, behavior when consumers are 10x slower than producers, and operational complexity (lines of config, failure modes).

📈 **Exit Criteria**
- [ ] A loss matrix: for each backend × each failure mode → messages lost. Measured, not documented.
- [ ] Poison-pill cascade reproduced and fixed on all four
- [ ] A written recommendation: "for a team of 5 doing 500 jobs/sec, use X, because…"

---

### B.4 — Redis in Anger

Keep v2's data-structure catalog (it was genuinely good) and add:

> 🔥 **THE WALL — Three Redis Outages**
> 1. **`KEYS *` in production.** Run it against a 10M-key instance while serving traffic. Redis is single-threaded — watch every other request block for seconds. Now use `SCAN` and compare.
> 2. **Cache stampede.** Have 500 concurrent clients request a key that just expired. Watch 500 identical queries hit your database simultaneously. Fix with singleflight, then with probabilistic early expiration (XFetch), and measure both.
> 3. **The lock that isn't.** Implement a `SETNX` lock. Now have the lock holder pause (SIGSTOP) past the TTL while another client acquires it. Both now believe they hold the lock. **Read the Kleppmann/antirez Redlock exchange and understand why a lock without a fencing token is not a lock in an asynchronous system.**

#### Additional theory
- Single-threaded event loop → **any O(N) command is an outage**: `KEYS`, `SMEMBERS` on a huge set, `HGETALL`, big `DEL` (use `UNLINK`), Lua scripts that run long
- Memory: `maxmemory-policy` (all 8 of them — know `allkeys-lru` vs `volatile-lru` vs `noeviction` and what each does when full), fragmentation ratio, `MEMORY DOCTOR`
- Persistence tradeoffs (RDB fork + COW doubling memory, AOF rewrite), and why **`BGSAVE` on a 20GB instance can OOM the box**
- Cluster: hash slots, hash tags, MOVED/ASK redirects, why multi-key ops break, resharding
- **Redis is not a database**: what you lose (durability guarantees, transactions across nodes, consistency during failover — see the Jepsen Redis analyses)

#### 🛠 CORE PROJECT — `redis-patterns` (v2's version, sharpened)
Keep v2's 7 features (cache+TTL, leaderboard, sliding-window rate limit via Lua, distributed lock, pub/sub fanout, HyperLogLog, Streams audit log) but add the requirements that make it real:
- Every Lua script must be proven atomic under 1,000 concurrent clients
- The rate limiter must be **exactly correct** at the boundary — test with a burst precisely at the window edge
- The distributed lock must include a **fencing token**, and you must demonstrate the failure mode without one
- Cache stampede protection measured: DB QPS during a mass-expiry event, with and without

---

### B.5 — CI/CD & Infrastructure as Code

Keep v2's pipeline design; add what makes it senior:

- **Build reproducibility & caching** — why your CI takes 18 minutes and how to get it to 4
- **Deployment strategies with real mechanics**: rolling (and why it needs readiness gates + `maxUnavailable` tuning), blue/green (and the database problem — **you cannot blue/green a schema**), canary with automated analysis (Argo Rollouts/Flagger + metric-based abort), and **feature flags as the decoupling of deploy from release**
- **Progressive delivery and automatic rollback on SLO burn**
- **DORA metrics**: deployment frequency, lead time, change failure rate, MTTR. Measure them on your own repo.
- **Terraform in practice**: state, locking, `plan` in PR, drift, modules, and **the blast-radius discipline** (separate state per environment). Plus the OpenTofu fork's existence and why it happened.
- **Secrets**: never in env vars in the repo; External Secrets Operator, SOPS, Vault, cloud secret managers, and **short-lived credentials via OIDC federation from CI** (this is the modern correct answer and it impresses)

#### 🛠 CORE PROJECT — full pipeline + `deploy-metrics`
Build v2's 9-stage pipeline, then add: **a canary deploy with automated rollback triggered by a real metric**, and a small tool that computes your own DORA metrics from git + deployment history and renders them.

📈 **Exit Criteria**
- [ ] A deliberately-broken deploy is **automatically rolled back** by metric analysis, with the Grafana screenshot showing detection and rollback
- [ ] Pipeline p50 duration under 6 minutes, with a before/after showing what you cached
- [ ] CI authenticates to the cloud via OIDC with **zero long-lived secrets** in the repo
- [ ] Your DORA dashboard, with real numbers from your own commits

---

## ⚡ LEVEL 3 — Distributed Systems Core

> **The hard one.** This is where the roadmap earns its name. Budget more than you think.
>
> **⏱ Budget:** 180–260 hours (Raft alone is 80–150) · **Chronos milestone:** C6 · **Prereq:** Level 2, D.3

---

### 3.1 — The Eight Fallacies, Made Concrete

> 🔥 **THE WALL — Prove Each Fallacy Wrong, With Evidence**
> Don't read the list of eight fallacies. **Demonstrate each one** on a two-service setup using `tc netem` and `iptables`:
> 1. *The network is reliable* → `tc qdisc add dev eth0 root netem loss 3%` — now measure your error rate. It's not 3%.
> 2. *Latency is zero* → add 100ms and watch your N+1 service call turn a 50ms endpoint into 5 seconds
> 3. *Bandwidth is infinite* → `netem rate 1mbit` and watch your "small" JSON response time out
> 4. *The network is secure* → capture your own service-to-service traffic in plaintext
> 5. *Topology doesn't change* → kill a node and watch stale DNS/connection pools route to it for 60 seconds
> 6. *There is one administrator* → change a config in one place and watch it not propagate
> 7. *Transport cost is zero* → measure serialization CPU as a fraction of total (it's often 20-40%)
> 8. *The network is homogeneous* → MTU mismatch, PMTU blackhole
>
> **The most important one to reproduce is the asymmetric partition:** A can send to B, but B cannot send to A. Every naive failure detector gets this wrong, and it's how split-brain happens in the real world.

#### 📖 Theory
- **Partial failure** and why it's the defining property of distributed systems: you cannot distinguish "slow" from "dead"
- **Failure detectors**: the impossibility of a perfect one in an asynchronous network; heartbeats, timeouts, phi-accrual, and the **fundamental tradeoff between detection time and false positives**
- **FLP impossibility** — no deterministic consensus in an asynchronous system with even one crash fault. What it does and doesn't mean in practice (partial synchrony saves you).
- **CAP, stated correctly** — it's about *behavior during a partition*, not a permanent choice of two letters. Then **PACELC**, which is the more useful framing (during Partition: A or C; Else: Latency or Consistency).
- **Two Generals and Byzantine Generals**
- **Idempotency, retries, and retry amplification** — why a naive retry policy turns a small blip into a full outage (a 3x retry across 4 hops = 81x load)
- **Backpressure and load shedding as distributed-systems primitives** (→ Level E)

#### 📄 Sources
- **DDIA Chapter 8.**
- **"Notes on Distributed Systems for Young Bloods"** — Jeff Hodges. Read it once a year.
- **"A Note on Distributed Computing"** — Waldo et al. (1994). Why RPC's transparency is a lie.
- **"Fallacies of Distributed Computing Explained"** — Rotem-Gal-Oz.
- **"Metastable Failures in Distributed Systems"** (HotOS 2021) — **read this.** It explains the class of outage where a system stays broken after the trigger is removed. Almost nobody knows this concept and it's extremely impressive in a design interview.
- **"The Tail at Scale"** — Dean & Barroso (CACM 2013). Why p99 matters more than the mean, and hedged requests. **Essential.**

---

### 3.2 — Consensus: implement Raft, for real

> **This is the crown jewel of the roadmap. Do not skip it. Do not use a library.**

#### ⭐ MIT 6.5840 (formerly 6.824) — Distributed Systems
`pdos.csail.mit.edu/6.824/` — lectures, papers, and labs are all public.

| Lab | What you build | Realistic hours |
|---|---|---|
| 1 | MapReduce (coordinator + workers, fault-tolerant) | 15–25 |
| 2 | Key/Value server with at-most-once RPC semantics | 10–15 |
| 3 | **Raft**: leader election, log replication, persistence, snapshots | **60–120** |
| 4 | Fault-tolerant KV service on top of your Raft | 25–40 |
| 5 | Sharded KV with reconfiguration across Raft groups | 30–50 |

> **Honest warning that v2 didn't give you:** v2 budgeted "2–3 weeks" for all five labs. That is wrong by roughly 4x. Lab 3 alone defeats most people on the first attempt. Budget **8–14 weeks at 10–15 h/week**, expect to rewrite your Raft at least once, and expect the `TestFigure8Unreliable` test to humble you. Finishing this puts you ahead of the large majority of working senior engineers.

**Do this alongside it:** the **Fly.io Gossip Glomers** challenges (`fly.io/dist-sys/`) — 6 distributed-systems challenges (unique IDs, broadcast with partitions, grow-only counter, replicated log, totally-available transactions) using the Maelstrom test harness. Much shorter than 6.5840, immediately satisfying, and Maelstrom *checks your consistency for you* — which pairs perfectly with Level D.

#### 📖 Theory
- **Raft in full**: terms, election timeouts and randomization, the log-matching property, commit rules, **why a leader may not commit an entry from a previous term directly** (the Figure 8 case — this is *the* subtle part), membership changes (joint consensus vs single-server), log compaction and snapshots, and read-only optimizations (**ReadIndex and lease reads**, which is how etcd serves linearizable reads without a log write)
- **Paxos** — Single-decree, Multi-Paxos, and why Raft won on understandability. Read "Paxos Made Simple" *after* implementing Raft; it's much clearer then.
- **Consistency models**: linearizability (real-time ordering), sequential consistency, causal consistency (**the strongest model available under partition** — a great interview point), eventual consistency
- **Quorum intersection** as the underlying idea of everything
- **Replicated state machines** as the unifying abstraction
- **CRDTs** — G-Counter, PN-Counter, OR-Set, LWW-Register, and operational vs state-based. Where they beat consensus (collaborative editing, shopping carts, offline-first).
- **Gossip / epidemic protocols** — SWIM, and how Cassandra/Consul/Serf do membership

#### 📄 Sources
- **"In Search of an Understandable Consensus Algorithm (Extended Version)"** — Ongaro & Ousterhout. Read the *extended* version; the conference version omits crucial detail. Then read **Ongaro's PhD thesis** for membership changes and log compaction.
- **"Paxos Made Simple"** — Lamport; and **"Paxos Made Live"** — Chandra, Griesemer, Redstone (Google). The second one is more valuable: it's about all the things the paper doesn't tell you.
- **"Students' Guide to Raft"** — Jon Gjengset. The single most useful supplement while doing Lab 3.
- **The Raft visualization** at `thesecretlivesofdata.com/raft/` and `raft.github.io`.
- **DDIA Chapter 9.**
- **"A Comprehensive Study of CRDTs"** — Shapiro et al.; and Kleppmann's CRDT work / Automerge.

📈 **Exit Criteria for Level 3.2**
- [ ] All 6.5840 labs pass, including with `-race`, run 100 consecutive times without flake
- [ ] You can draw Raft's Figure 2 from memory
- [ ] You can explain the Figure 8 scenario at a whiteboard in under 5 minutes
- [ ] Gossip Glomers challenges 1–5 complete, verified by Maelstrom
- [ ] **Chronos C6:** Chronos's control plane runs on *your own* Raft implementation. Kill the leader mid-commit under load; prove no acknowledged workflow is lost.

⛓ **Problem Chain**
```
"Leader elected twice"      → terms, split votes → randomized timeouts → why (→ 3.2)
"Committed entry lost"      → Figure 8 → commit rules → the no-op-on-election trick
"Reads returned stale data" → linearizable reads → ReadIndex / lease reads → clock assumptions (→ 3.4)
"Consensus is slow"         → 1 RTT + fsync per op → batching, pipelining → why not everything is Raft
"Adding a node broke quorum"→ joint consensus / single-server changes
"Raft can't do 100k ops/s"  → sharding into multiple Raft groups → the Spanner/Cockroach model (→ 5.1)
```

---

### 3.3 — Time, Clocks & Ordering

> 🔥 **THE WALL — Move Time Backwards**
> Run a service that timestamps records with `time.Now()`. Now run `sudo date -s "-5 seconds"` (or use `libfaketime`) mid-workload.
>
> Watch: records with duplicate timestamps, records appearing to happen before their causes, a TTL that never expires, a leader lease that overlaps with the next leader's. **Then switch to a monotonic clock for durations and a logical clock for ordering, and see the problems disappear.**

#### 📖 Theory
- **Wall clock vs monotonic clock** — the single most practical thing in this section. **Never measure a duration with a wall clock.** Never. Know that `time.Since()` in Go uses the monotonic reading and why that's a deliberate design decision.
- **NTP**, clock drift, slew vs step, leap seconds and leap smearing
- **Lamport timestamps** — cause → effect ordering, but not the converse
- **Vector clocks** — detecting concurrency; and why they don't scale to many nodes
- **Hybrid Logical Clocks (HLC)** — CockroachDB's approach: causally consistent and close to physical time
- **TrueTime** — Spanner's atomic-clock-and-GPS uncertainty interval, and the `commit-wait` trick: *wait out the uncertainty so external consistency is guaranteed.* Understanding that Spanner buys consistency by **deliberately waiting** is a genuinely deep insight.
- **Leases and fencing tokens** — the correct pattern for "only one node may do X." Read Kleppmann's "How to do distributed locking" for the definitive treatment.

#### 📄 Sources
- **"Time, Clocks, and the Ordering of Events in a Distributed System"** — Lamport (1978). The most cited paper in the field. Read it; it's 8 pages.
- **"Spanner: Google's Globally-Distributed Database"** (OSDI 2012) and **"Spanner, TrueTime and the CAP Theorem"**.
- **"Living Without Atomic Clocks"** — CockroachDB blog, on HLC.
- **"How to do distributed locking"** — Martin Kleppmann. Then antirez's reply. Read both.
- **"There is No Now"** — Justin Sheehy (ACM Queue).

#### 🛠 CORE PROJECT — `clock-chaos`
Add clock faults to your `simd` harness: skew, jumps forward and backward, and drift. Then run your Chronos lease protocol under them.

📈 **Exit:** demonstrate a correctness violation with wall-clock leases, then show the fencing-token version surviving the same seeds. **This is a two-graph story that explains fencing tokens better than any article.**

---

### 3.4 — Logs, Streams & Kafka

> 🔥 **THE WALL — Lose Data Three Ways**
> With a real Kafka cluster:
> 1. Produce with `acks=1`, kill the leader broker mid-write, and **measure how many acknowledged messages vanished.**
> 2. Consume with auto-commit enabled, crash the consumer after committing but before processing. **Messages silently skipped.** Then crash after processing but before committing → duplicates. **You cannot have neither, without changing where the offset lives.**
> 3. Rebalance storm: add and remove consumers rapidly and watch the group spend all its time rebalancing and none consuming. (Then learn cooperative sticky assignment and static membership.)

#### 📖 Theory
- **The log as the fundamental abstraction** (Kreps) — and the realization that a database, a queue, a cache, and a replica are all just different views of a log
- Kafka internals: partitions as the unit of parallelism and ordering, the **ISR (in-sync replicas)** set, `min.insync.replicas` + `acks=all` as the actual durability contract, high watermark vs log end offset, leader epochs (and the truncation bug they fixed), KRaft replacing ZooKeeper
- **Consumer groups**: assignment strategies, rebalance protocols (eager vs cooperative incremental), and why rebalancing is the source of most Kafka operational pain
- **Delivery semantics**: at-least-once by default; **exactly-once via the idempotent producer + transactions** — and its exact scope (Kafka-to-Kafka only; your database write is *not* in that transaction, which is why the outbox pattern exists)
- **Log compaction** — the changelog/table duality
- **Partitioning and key choice**: ordering is per-partition only; a hot key is a hot partition; changing partition count breaks key→partition affinity forever
- **Consumer lag** as the primary health metric
- **CDC** — Debezium, logical decoding, the initial-snapshot problem, and CDC as the correct alternative to dual writes
- **Stream processing**: windowing (tumbling/hopping/session), watermarks, **event time vs processing time**, late data, stateful operators, exactly-once in Flink via checkpointing/Chandy-Lamport

#### 📄 Sources
- **"The Log: What every software engineer should know about real-time data's unifying abstraction"** — Jay Kreps. Long, foundational, worth every minute.
- **"Kafka: a Distributed Messaging System for Log Processing"** (2011) and **"Exactly Once Semantics in Apache Kafka"** — Confluent.
- **DDIA Chapters 11 & 12.**
- **"Streaming Systems"** — Akidau, Chernyak, Lax. The definitive book on event time, watermarks, and windowing. **Missing from v2 and it's the standard reference.**
- **"Turning the database inside-out"** — Martin Kleppmann (talk). Changes how you see everything.
- **"Delivering Billions of Messages Exactly Once"** — Segment Engineering. A great real-world dedup story.

#### 🛠 CORE PROJECT — `outbox-cdc-lab`
Build the same "order placed → email sent" integration **three ways** and break each one:
1. **Dual write** (DB + Kafka in the app) → prove inconsistency by crashing between the two writes
2. **Transactional outbox + poller** → prove correctness, then measure the polling latency and the outbox table's growth
3. **CDC via Debezium** → prove correctness, then explore the snapshot problem and schema-change handling

📈 **Exit Criteria**
- [ ] A crash-injection test that produces a **provable** inconsistency in approach 1 (an order with no event, or an event with no order)
- [ ] Approaches 2 and 3 survive 1,000 crash injections with zero inconsistencies
- [ ] Latency and throughput comparison across all three
- [ ] Written: "when I'd choose each, and what CDC costs operationally"

---

### 3.X — 🎓 LEVEL 3 EXIT EXAM

1. Draw Raft's Figure 2 from memory. Now explain the Figure 8 scenario and the rule that fixes it.
2. Your 5-node cluster partitions 3/2. What does each side do? What if the partition is asymmetric?
3. Explain why exactly-once delivery is impossible and exactly-once processing is achievable. Give a concrete implementation.
4. When is causal consistency the right choice over linearizability? Name a real system that made that call.
5. Your Kafka consumer lag is growing linearly. Give six causes and the metric that distinguishes each.
6. What is a metastable failure? Give an example and a mitigation.
7. Explain fencing tokens. Why is a TTL-based lock insufficient?
8. Design a system that must not lose an acknowledged write, ever. What's the minimum you need, and what does it cost in latency?
9. What does TrueTime buy Spanner and what does it cost?

**Pass = 8/9.**

---
## ⚡ LEVEL 4 — Infrastructure & Reliability

> **Goal:** build systems that degrade instead of collapsing, and that tell you what's wrong before a customer does.
>
> **⏱ Budget:** 90–120 hours · **Chronos milestone:** C7 · **Prereq:** Level 3 (partly parallel)

---

### 4.1 — Load Balancing, Proxies & Service Discovery

> 🔥 **THE WALL — The Load Balancer That Made It Worse**
> Put 3 backends behind round-robin. Make one backend 10x slower (not dead — *slow*). Measure overall p99.
>
> Round-robin keeps sending it a third of traffic; your p99 is now dominated by the slow node. Health checks say it's healthy — it returns 200s! Now implement **least-outstanding-requests** and measure again. Then implement **EWMA/peak-latency-aware** selection. The improvement is dramatic and it explains why "the load balancer is smarter than you think" at every large company.
>
> **Second wall:** put a **gRPC** service behind an L4 load balancer with 3 backends. Scale to 6 backends. Watch traffic stay pinned to the original 3, because HTTP/2 connections are long-lived and L4 balances *connections*, not requests. This is a real, common production incident.

#### 📖 Theory
- **L4 vs L7**, and why L7 is required for gRPC, retries, and per-request routing
- **Algorithms**: round-robin, weighted RR, least-connections, **least-outstanding-requests (the usual best default)**, **power of two random choices (P2C)** — near-optimal with almost no coordination; read the "Power of Two Choices" result, it's beautiful — EWMA/latency-aware, consistent hashing (for cache affinity), **and consistent hashing with bounded loads**
- **Health checks**: active vs passive, **shallow vs deep** — and the crucial trap: a deep health check that verifies the database will fail *all* your instances at once when the database blips, converting a degradation into a total outage. **Health-check design is a top-tier interview topic.**
- **Outlier detection / passive ejection** (Envoy's model) — eject a host based on observed error rate, then probe it back
- **Connection draining and graceful shutdown** across the LB + orchestrator boundary
- **Client-side LB and service meshes** (gRPC + xDS), and the tradeoff vs a central proxy
- **Service discovery**: DNS, Consul, etcd, Kubernetes Endpoints/EndpointSlices, and **propagation delay** as the thing that actually bites you
- **Anycast and GSLB** for global traffic; **Maglev** (Google's) and consistent hashing at the packet level

#### 📄 Sources
- **"Introduction to modern network load balancing and proxying"** — Matt Klein (Envoy's author). **The best single article on the topic, full stop.**
- **"The power of two random choices"** — Mitzenmacher; and the practical writeups (NGINX, HAProxy, Finagle).
- **"Maglev: A Fast and Reliable Software Network Load Balancer"** (NSDI 2016).
- **"Consistent Hashing with Bounded Loads"** — Google Research blog + paper.
- **"gRPC Load Balancing"** — grpc.io blog.

#### 🛠 CORE PROJECT — `lb-lab` *(Instrument archetype, 8/10)*
Write your own L7 load balancer (it's ~500 lines) implementing **six** algorithms, then benchmark all six against a backend pool where you can independently control each backend's latency distribution, error rate, and capacity.

Scenarios to test: homogeneous backends · one slow backend · one backend returning errors · a backend that's slow only at p99 · adding capacity mid-test · removing a backend mid-request.

📈 **Exit Criteria**
- [ ] Six-algorithm comparison chart of overall p99 under each scenario
- [ ] Demonstrate the **deep health check cascade**: show how a shared-dependency blip takes 100% of your fleet out, then fix it (fail-open, separate liveness from readiness, cached health status)
- [ ] Demonstrate the gRPC/L4 pinning problem and fix it with client-side LB
- [ ] Zero requests dropped during a backend removal — proven by a request-count assertion

---

### 4.2 — Caching at Every Layer

> 🔥 **THE WALL — The Cache That Caused the Outage**
> Three failures to cause on purpose:
> 1. **Stampede.** 10,000 clients, one hot key, TTL expires. Your database gets 10,000 identical queries in 50ms and falls over.
> 2. **Cold cache after deploy.** Restart your service. Every request is now a miss. Your database, sized for a 95% hit rate, now gets 20x its normal load. **This is how a routine deploy causes an outage** — and it's why cache warming and staged restarts exist.
> 3. **The stale-forever key.** Write-through cache, a failed invalidation, and a key that's now permanently wrong. Find it. (You won't, without a TTL as a backstop — which is the actual lesson: **always have a TTL, even on "invalidated" caches.**)

#### 📖 Theory
- **Patterns**: cache-aside, read-through, write-through, write-behind, refresh-ahead — and the failure mode of each
- **Invalidation**: TTL, event-driven, versioned keys (`user:42:v7` — never delete, just bump the version; this sidesteps a whole class of race), tag-based, and **why "there are only two hard things" is a real engineering statement**
- **Stampede protection**: request coalescing / singleflight, probabilistic early expiration (**XFetch** — read the paper, it's 3 pages and the formula is elegant), staggered TTLs with jitter, "never expire, refresh in background"
- **Eviction**: LRU, LFU, **TinyLFU/W-TinyLFU** (what Caffeine and Ristretto use, and it's substantially better than LRU — knowing this is a differentiator), ARC, S3-FIFO (the recent one), and the scan-resistance problem
- **Negative caching** — cache the misses too, or a nonexistent-key flood becomes a database DDoS
- **Multi-tier**: in-process L1 (nanoseconds, per-instance, inconsistent) → Redis L2 (sub-ms, shared) → CDN → browser. **Coherence across L1 instances is the hard part.**
- **CDN**: cache keys, `Vary`, `Cache-Control` vs `Surrogate-Control`, purge vs soft-purge, `stale-while-revalidate`, `stale-if-error` (**underused and excellent — serve stale content during an origin outage**), tiered caching, cache hit ratio economics
- **Consistency**: what staleness bound are you actually offering the user? Say it out loud in design interviews.

#### 📄 Sources
- **"Scaling Memcache at Facebook"** (NSDI 2013). **One of the best systems papers ever written for practitioners** — leases, gutter pools, stampede control, regional invalidation. Read it twice.
- **"TAO: Facebook's Distributed Data Store for the Social Graph"** (USENIX ATC 2013).
- **"Optimal Probabilistic Cache Stampede Prevention"** — Vattani, Chierichetti, Lowenstein (VLDB 2015).
- **"TinyLFU: A Highly Efficient Cache Admission Policy"** — Einziger, Friedman, Manes.
- **Caffeine's design docs** (GitHub wiki) — an unusually well-explained real cache implementation.

#### 🛠 CORE PROJECT — `cache-lab` *(Instrument archetype, 8/10)*
Build a multi-tier cache library: in-process W-TinyLFU L1 + Redis L2 + singleflight + probabilistic early expiration + negative caching + per-tier metrics.

Then build the **workload generator** with realistic access distributions (Zipfian with a configurable skew — real traffic is always Zipfian, and using a uniform distribution is why most cache benchmarks are meaningless).

📈 **Exit Criteria**
- [ ] Hit-rate comparison: LRU vs LFU vs W-TinyLFU vs S3-FIFO at the same memory budget, under Zipf(0.99) — **publish the chart; W-TinyLFU should win clearly, and you should be able to explain why**
- [ ] Stampede demo: DB QPS during mass expiry, with and without protection (expect ~1000x difference)
- [ ] Cold-start demo: origin load after a restart, with and without cache warming
- [ ] A scan-resistance test: a full-table scan should not evict your hot working set
- [ ] Written: "the staleness contract this cache offers"

---

### 4.3 — Rate Limiting, Quotas & Fairness

> 🔥 **THE WALL — The Boundary Burst**
> Implement a fixed-window rate limiter: 100 requests/minute. Now send 100 requests at 11:59:59 and 100 more at 12:00:00. **You just allowed 200 requests in one second** through a limiter that promised 100/minute. Reproduce it, then fix it with a sliding window, and prove the fix with the same attack.
>
> **Second wall:** run your Redis-backed limiter with 50 concurrent clients using GET-then-SET instead of an atomic Lua script. Count the actual allowed requests. It'll be well over the limit. **Race conditions in rate limiters are how "we had a limit" becomes "we had an outage."**

#### 📖 Theory
- **The five algorithms**, with their exact memory/accuracy tradeoffs: fixed window (cheap, bursty at boundaries), sliding window log (exact, memory-heavy), sliding window counter (the usual sweet spot), token bucket (allows controlled bursts — usually what you actually want), leaky bucket (smooths output)
- **Distributed rate limiting**: centralized Redis (accurate, adds a network hop and a SPOF), local with periodic sync (fast, approximate), and **the "sold quota" model** where a central authority leases capacity to each node
- **Concurrency limits vs rate limits** — limiting in-flight requests is often more useful than limiting arrival rate, because it self-adjusts to your actual capacity (→ Level E's adaptive limits)
- **Fairness and multi-tenancy**: per-tenant quotas, weighted fair queuing, **the noisy-neighbor problem**, and the shuffle-sharding trick from AWS (**read "Workload isolation using shuffle-sharding"** — an elegant idea that dramatically limits blast radius, and a great thing to bring up in a design interview)
- **What to do at the limit**: reject (429 + `Retry-After` + `RateLimit-*` headers per the IETF draft), queue, or degrade
- **Where to enforce**: edge/CDN, gateway, service, database. Usually all four, for different reasons.

#### 📄 Sources
- **"Scaling your API with rate limiters"** — Stripe Engineering. Their four limiter types and why each exists.
- **"An alternative approach to rate limiting"** — Figma Engineering (the sliding-window-with-weighting approach).
- **"Workload isolation using shuffle-sharding"** — AWS Builders' Library. Read the whole Builders' Library, honestly.
- **"How we built rate limiting capable of scaling to millions of domains"** — Cloudflare.
- **"Fair queuing"** and the Kubernetes API Priority and Fairness (APF) design doc.

#### 🛠 CORE PROJECT — `ratelimit` (library + attack suite)
All five algorithms, single-node and Redis-distributed (atomic Lua), plus **the adversarial test suite** that tries to exceed each limiter's promise (boundary bursts, concurrent races, clock skew between nodes, Redis failover mid-window).

📈 **Exit Criteria**
- [ ] Each limiter's promise holds under its attack — with the measured over-admission rate for each (some over-admission is acceptable; **you must state the bound**)
- [ ] Throughput/latency cost of each algorithm at 10k RPS
- [ ] Shuffle-sharding implemented, with a simulation showing blast radius: "with 8 shards of 2, a single abusive tenant affects X% of other tenants" — the combinatorics chart is a great artifact
- [ ] Correct `429` semantics with `Retry-After` and `RateLimit-*` headers

---

### 4.4 — Resilience: timeouts, retries, circuit breakers, bulkheads

> 🔥 **THE WALL — Build a Retry Storm**
> A → B → C. Give each hop 3 retries. Make C slow (not failing — *slow*).
>
> A's retries multiply B's retries multiply C's load: **3 × 3 = 9x amplification**, and if each retry also times out and retries, you get a positive feedback loop. Watch C, which was merely slow, become completely dead — **caused entirely by your own reliability mechanisms.** Then measure it, and fix it with: retry budgets (max 10% of requests may be retries), retries only at one layer, circuit breakers, and jittered backoff.
>
> **Then reproduce the metastable failure:** remove the original trigger and watch the system stay down because the retry load is now self-sustaining. Recovery requires shedding load, not just fixing the original problem. **This is one of the most valuable things you can learn to explain.**

#### 📖 Theory
- **Timeouts**: connect vs read vs total; **deadline propagation** across hops (the gRPC/context model — the correct design); why every timeout must be shorter than its caller's remaining budget; **and the fact that a timeout without a cancel just abandons work that keeps running**
- **Retries done right**: only on idempotent operations or with idempotency keys; only on retryable errors; **exponential backoff with full jitter** (read the AWS post — "full jitter" beats "equal jitter" and both crush no-jitter); retry budgets/token buckets; **never retry a timeout without exponential backoff, and never retry at more than one layer**
- **Hedged requests** — send a duplicate after p95 and take the first response. **The Tail at Scale's central technique.** Cost: ~5% more load for a dramatic p99 improvement.
- **Circuit breakers**: closed → open → half-open; error-rate vs consecutive-failure triggers; per-endpoint not per-service; and the honest critique — **circuit breakers are frequently mis-tuned and can cause the outage they're meant to prevent** (Netflix eventually moved away from Hystrix; know why)
- **Bulkheads**: separate connection pools/thread pools per dependency so one slow dependency can't consume all your concurrency
- **Graceful degradation**: serve stale, serve partial, serve a default. **Decide, per feature, what "degraded" means — and write it down before the incident.**
- **Load shedding and admission control** (→ Level E)
- **SLIs/SLOs/error budgets**: define an SLI as a ratio of good events to valid events; multi-window multi-burn-rate alerting (**the SRE Workbook's alerting chapter is the single most practically useful thing Google published**)
- **Chaos engineering**: hypothesis-driven, blast-radius-limited, in production eventually. Not "randomly break things."

#### 📄 Sources
- **AWS Builders' Library** — "Timeouts, retries and backoff with jitter," "Avoiding fallback in distributed systems," "Using load shedding to avoid overload," "Caching challenges and strategies," "Avoiding insurmountable queue backlogs." **This whole library is the best free reliability writing that exists. Read all ~20 articles.**
- **"Exponential Backoff and Jitter"** — Marc Brooker, AWS.
- **"The Tail at Scale"** — Dean & Barroso.
- **"Release It!" 2nd ed.** — Michael Nygard. **The origin of circuit breaker and bulkhead as named patterns. v2 omitted this book and it is the single most relevant book to this section.**
- **Google SRE Book** Ch. 3, 4, 6, 21, 22 (Addressing Cascading Failures) + **The SRE Workbook** Ch. 5 (Alerting on SLOs).
- **"Metastable Failures in Distributed Systems"** (HotOS 2021).

#### 🛠 CHRONOS C7 + PROJECT `resilience-kit`
Build the resilient client (timeout + deadline propagation + jittered retry with budget + circuit breaker + bulkhead + hedging) **and the adversarial dependency** that can be configured for: slow, flapping, failing, partial-failure, and "returns 200 with garbage."

📈 **Exit Criteria**
- [ ] **Retry amplification measured and charted** — 3 hops with and without retry budgets, showing the multiplication factor
- [ ] **Metastable failure reproduced and then made impossible** — two graphs
- [ ] Hedging: p99 improvement vs additional load, measured, with the crossover point where hedging stops being worth it
- [ ] Circuit breaker tuning study: show a configuration that makes things *worse*, and explain it
- [ ] Deadline propagation proven: a 100ms client deadline results in the 4th-hop service actually cancelling its database query — show the log line

---

### 4.5 — Observability

> 🔥 **THE WALL — Debug Blind**
> Take a 3-service system. Have someone inject a failure in service C that manifests as elevated latency in service A. Now debug it **with only logs**. Time yourself.
>
> Then add metrics. Time yourself again. Then add distributed tracing. Time yourself again. **The three numbers are the entire business case for observability**, and they're numbers you can quote when someone asks you to justify the cost.

#### 📖 Theory
- **Metrics**: counters/gauges/histograms/summaries; **why you almost always want histograms** (you can't average percentiles — averaging p99s across instances is meaningless and everybody does it); cardinality as the thing that will blow up your bill; Prometheus data model, PromQL (`rate`, `histogram_quantile`, `increase`, recording rules); exemplars linking metrics → traces
- **RED** (Rate, Errors, Duration) for services; **USE** (Utilization, Saturation, Errors) for resources; **the Four Golden Signals**
- **Structured logging**: JSON, levels, sampling (**log sampling at high volume is mandatory** and most people learn this from the bill), correlation/trace IDs on every line, and never logging PII/secrets
- **Distributed tracing**: spans, W3C `traceparent` propagation, head-based vs **tail-based sampling** (tail lets you keep 100% of the errors and slow traces, which is what you actually want), and the instrumentation cost
- **OpenTelemetry** — the standard; the Collector as a pipeline; why vendor-neutral instrumentation matters
- **Continuous profiling** as the fourth pillar (→ C.2)
- **Alerting philosophy**: alert on **symptoms** (SLO burn), not causes; every page must be actionable and urgent; **multi-window multi-burn-rate** alerts; runbook links in every alert
- **Cardinality and cost** — the practical reality that observability often costs more than the infrastructure it observes

#### 📄 Sources
- **"Observability Engineering"** — Majors, Fong-Jones, Miranda. The modern reference.
- **Google SRE Workbook Ch. 5** — "Alerting on SLOs." Multi-burn-rate alerting explained properly.
- **"Distributed Tracing at Uber"** / Jaeger papers; **Dapper** (Google, 2010) — the original.
- **"Prometheus: Up & Running"** 2nd ed., and the PromQL docs.
- **"Logs, metrics and traces: the three pillars is a lie"** — various critiques worth reading for balance (the argument that they're three views of the same events).

#### 🛠 CORE PROJECT — `observability-stack` (Chronos)
Full OTel instrumentation of Chronos: traces spanning the API → queue → worker → child workflow (**including a trace that spans a 30-day timer — this is genuinely hard and interesting**), RED dashboards, SLO definitions with error budgets, multi-burn-rate alerts, exemplars linking a latency spike to a specific trace, and continuous profiling.

📈 **Exit Criteria**
- [ ] Given an injected fault, **time-to-root-cause under 5 minutes** using only the dashboards — demonstrate it on video/GIF
- [ ] An SLO with a real error budget and a burn-rate alert that fires correctly in a fault drill (and does *not* fire on a brief blip)
- [ ] Trace context correctly propagated across an asynchronous queue boundary — screenshot the trace
- [ ] A cardinality audit: your metric label sets, and the estimated series count, with a justification for each high-cardinality label

---

## ⚡ LEVEL E — Performance Engineering 🆕

> **Why this level exists:** v2 said "benchmark it" a dozen times without ever teaching how to benchmark, how queueing works, or what to do when you're overloaded. Performance work is a distinct discipline, and the ability to reason about *queueing* rather than just *speed* is a hard senior signal.
>
> **⏱ Budget:** 60–90 hours · **Prereq:** C.2, 4.4

---

### E.1 — Queueing Theory for Engineers (the math that explains everything)

> 🔥 **THE WALL — The Cliff**
> Load test a service. Plot **offered load (x) vs p99 latency (y)** from 10% to 120% of capacity, in 5% increments.
>
> You will not see a gentle slope. You will see a **hockey stick**: latency is flat and boring up to ~70% utilization, starts bending at 80%, and goes vertical past 90%. **At 100% utilization, queueing latency is mathematically infinite.**
>
> This single graph explains: why you don't run servers at 90% CPU, why autoscaling thresholds are ~60-70%, why a small traffic increase caused a huge latency increase, and why "we just need one more server" is sometimes true and sometimes hopeless.

#### 📖 Theory — you need surprisingly little math, and it pays constantly
- **Little's Law: `L = λW`.** Concurrency = arrival rate × latency. Rearranged: if you know two, you know the third. **Use it constantly** — "we do 2000 RPS at 50ms, so we have ~100 requests in flight, so a pool of 20 connections is the bottleneck" is a 5-second calculation that most engineers never make.
- **Utilization law and the queueing curve**: for M/M/1, `W = S / (1 - ρ)`. At ρ=0.5, latency is 2×service time. At ρ=0.9, it's 10×. At ρ=0.99, it's 100×. **Memorize this shape.**
- **Why variance is the enemy**: with high service-time variance, the curve bends *much* earlier. This is why a single slow query type poisons an entire pool.
- **Multi-server queues (M/M/c)** and why one queue with c servers beats c queues with one server each (the supermarket-checkout result) — this is the argument for shared thread pools and for **least-outstanding-requests** load balancing
- **The Universal Scalability Law (USL)** — Gunther: throughput doesn't just plateau with added concurrency, it *decreases* past a point, because of contention (α) and crosstalk/coherency (β). **This is why adding workers made it slower**, and it's the most useful capacity model there is.
- **Amdahl's and Gustafson's laws**
- **Coordinated omission** (again — it's this important): a closed-loop load generator that waits for a response before sending the next request **cannot measure the latency of the requests it failed to send.** Your p99 is a lie. Use open-loop generators.
- **Percentiles compose badly**: the p99 of a request that makes 10 backend calls is roughly the p90 of the backend, not the p99. Fan-out multiplies tail latency — this is the core of "The Tail at Scale."

#### 📄 Sources
- **"Systems Performance"** — Gregg, Ch. 2 (Methodologies) — the queueing sections.
- **"Guerrilla Capacity Planning"** — Neil Gunther (USL).
- **"How NOT to Measure Latency"** — Gil Tene. Again. Yes, again.
- **"Performance Under Load"** — Netflix Tech Blog (adaptive concurrency limits).
- **Brendan Gregg's "The USE Method"** and Marc Brooker's blog (`brooker.co.za`) — **Brooker's posts on queueing, retries, and load are among the best systems writing being published.**

#### 🛠 PROJECT — `queue-theory-lab`
Build a simulator implementing M/M/1, M/M/c, and USL, then **validate the model against a real load test of one of your services.** Predict p99 at 85% utilization from measurements taken at 30% and 50%; then run at 85% and see how close you were.

📈 **Exit Criteria**
- [ ] Predicted vs actual p99 within 30% — and an explanation of the gap (it's usually variance)
- [ ] The hockey-stick chart for a real service, with the knee annotated
- [ ] A USL fit showing your system's α and β, and the concurrency level at which throughput *peaks and starts falling*
- [ ] Written: "the capacity model for this service and the utilization target I'd set, with justification"

---

### E.2 — Optimization in Practice

> 🔥 **THE WALL** — Take one endpoint and make it **10x faster.** Not 20%. 10x. Document every step: the profile, the hypothesis, the change, the measurement, and the new bottleneck. Most 10x wins come from removing work, not from making work faster — and discovering that yourself is the point.

#### 📖 The optimization hierarchy (in order of payoff)
1. **Don't do it** — cache it, precompute it, delete the feature
2. **Don't do it now** — make it async, return 202
3. **Don't do it N times** — batch, coalesce, fix the N+1
4. **Don't do it on the hot path** — move it to a background job
5. **Do less of it** — better algorithm, better index, less data over the wire
6. **Do it in parallel** — but mind the USL
7. **Do it faster** — micro-optimize, and only now: allocation reduction, SIMD, better serialization

#### 📖 Specific techniques
- **Serialization is usually 20-40% of a JSON API's CPU** — measure it before you assume it's the database
- **Compression tradeoffs**: gzip vs zstd vs lz4 vs brotli — the CPU-vs-bytes curve, and why zstd is usually the right default now
- **Connection pooling and reuse everywhere** (HTTP keep-alive, DB pools, gRPC channels); pool sizing via Little's Law
- **Batching**: the fundamental latency-vs-throughput dial; adaptive batching (batch until N items *or* T milliseconds)
- **Zero-copy**: `sendfile`, `splice`, `io_uring` fixed buffers, `mmap` and its pitfalls
- **Precomputation and materialized views**
- **The database is usually the answer** — index, query shape, or round trips

#### 🛠 PROJECT — `10x` (a written case study)
Pick the slowest endpoint across all your roadmap projects. Get 10x. Write it up as a narrative with the flame graph at each stage.

📈 **Exit:** ≥10x on p99 with the profile-driven story; **and an explicit statement of what you did NOT optimize and why** (knowing when to stop is the senior part).

---

### E.3 — Overload: backpressure, load shedding & admission control

> 🔥 **THE WALL — Goodput Collapse**
> Drive your service to 3x its capacity with an open-loop generator. Plot **offered load vs *successful* responses per second (goodput)**.
>
> A naive service's goodput doesn't plateau at capacity — **it collapses toward zero.** The server spends all its resources on requests that will time out before they're answered. Every one of those is wasted work. **This graph is the single most persuasive artifact in performance engineering** and almost nobody has produced one.
>
> Then implement, in order, and re-measure each time: (1) bounded queues, (2) **drop requests whose deadline has already passed** (the cheapest huge win — never work on a request nobody is waiting for), (3) LIFO queueing under overload (counterintuitive and correct: under overload, serving the newest request means at least *someone* gets a fresh answer), (4) adaptive concurrency limits (Little's-Law-based, TCP-Vegas-style), (5) priority-based shedding.

#### 📖 Theory
- **Backpressure vs load shedding vs buffering** — propagate the signal upstream, drop, or absorb. Buffering is the one that looks like it works and then kills you (**"queues are where latency goes to die"**).
- **Admission control** — decide at the door, cheaply, before you've spent resources
- **Deadline-aware processing** — check the deadline at each stage and abandon expired work
- **LIFO vs FIFO under overload** — Facebook's finding; FIFO means everyone gets a timed-out response, LIFO means some people get a good one
- **Adaptive concurrency limits** — Netflix's `concurrency-limits` (AIMD / gradient / Vegas-style): infer capacity from observed latency instead of configuring a fixed number. **This is the modern correct answer and it's a great thing to bring into a design interview.**
- **Priority and QoS**: shed the cheapest/least-important traffic first; separate critical from bulk paths
- **Brownout / graceful degradation**: turn off recommendations before you turn off checkout
- **Cell-based architecture and shuffle sharding** as blast-radius control

#### 📄 Sources
- **"Using load shedding to avoid overload"** and **"Avoiding insurmountable queue backlogs"** — AWS Builders' Library.
- **"Performance Under Load: Adaptive Concurrency Limits at Netflix"** — Netflix Tech Blog. Plus the `Netflix/concurrency-limits` source.
- **Google SRE Book Ch. 21 (Handling Overload) and Ch. 22 (Addressing Cascading Failures).** Chapter 22 is possibly the most valuable chapter in the book.
- **"Fail at Scale"** — Facebook, ACM Queue (the LIFO/adaptive-timeout findings).
- **Marc Brooker on "Will circuit breakers solve my problems?"** — the honest critique.

#### 🛠 FLAGSHIP PROJECT #6 — `overload` ⭐⭐ *(Instrument archetype, 9/10)*

**Build the goodput lab, and publish the curves nobody publishes.**

A service, an open-loop load generator, and six configurations: naive · bounded queue · + deadline-aware dropping · + LIFO under overload · + adaptive concurrency limit · + priority shedding.

For each, plot: offered load (0.5x → 5x capacity) vs **goodput**, vs p99 of *successful* requests, vs wasted work (CPU spent on requests that timed out).

📈 **Exit Criteria**
- [ ] The collapse curve and the graceful curve on the same chart — this is the money graph
- [ ] Quantified: "at 3x overload, the naive service delivers X% of capacity; the adaptive service delivers Y%"
- [ ] Adaptive limiter tracks a *changing* backend capacity (make the backend slower mid-test and show the limiter adapting)
- [ ] Wasted-work metric: CPU-seconds spent on requests that were never delivered
- [ ] Written up. This is a post that gets shared, because everyone's system has this problem and almost nobody has measured it.

---

### E.X — 🎓 LEVEL 4 + E EXIT EXAM

1. Your service runs at 70% CPU and p99 is 80ms. Traffic increases 20%. Estimate the new p99 and explain the model you used.
2. A → B → C, each with 3 retries. C gets slow. Draw the load amplification and explain how to fix it in three ways.
3. Explain coordinated omission and how you'd design a load test that avoids it.
4. Design a health check for a service that depends on a database. What does it check, and what happens when the database is degraded but not down?
5. You have 200ms of budget. A must call B (p99 50ms) and C (p99 120ms) and D (p99 30ms). Design the call pattern and the timeout for each.
6. Why does adding more worker threads sometimes reduce throughput? Name the model.
7. Your cache hit rate is 94%. You want 97%. What do you measure first, and what are the three most likely levers?
8. Your service is at 3x capacity. Rank your options and justify the order.
9. Why can't you average p99s across instances? What should you do instead?

**Pass = 8/9.**

---
## ⚡ LEVEL 5 — Advanced Architecture

> **⏱ Budget:** 90–130 hours · **Chronos milestone:** C8 · **Prereq:** Level 3, Level 4

---

### 5.1 — Service Decomposition (and the courage not to)

> 🔥 **THE WALL — The Distributed Monolith**
> Split a working monolith into 4 services *badly*, on purpose: split by technical layer instead of business capability, share one database between services, and make every user action require 3 synchronous hops.
>
> Now measure what you've done: p99 latency (worse), failure modes (any service down = everything down), deployment coupling (you must deploy them together), and debugging difficulty. **You've built a distributed monolith — all the costs of microservices, none of the benefits.**
>
> Then re-split correctly along bounded contexts with owned data and async integration, and measure again. **This exercise, and the ability to narrate it, is worth more in an architecture interview than any amount of microservices vocabulary.**

#### 📖 Theory
- **When to split, honestly**: team autonomy (Conway's law is the real driver — you're designing an org chart), independent scaling, independent deploy cadence, fault isolation, technology heterogeneity. **Not: "it's more modern."**
- **When NOT to split**: <20 engineers, unclear domain boundaries, no operational maturity (if you can't do observability and CI/CD well, microservices will destroy you), transactional consistency requirements across the boundary
- **The modular monolith** as the default. Extract when a module proves it needs independence. **Read Shopify's "Deconstructing the Monolith" and Amazon Prime Video's "Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%" (they moved from microservices *back* to a monolith).** Being able to argue both directions is the senior signal.
- **Data ownership**: one service owns each piece of data; **no shared databases, ever**; read models via events; **and the honest cost — you now have eventual consistency everywhere**
- **Sync vs async integration**: request/response couples availability (your uptime becomes the product of your dependencies'); events decouple but make flows hard to trace
- **Sagas**: choreography (events, decentralized, hard to see the whole flow) vs orchestration (a coordinator — which is exactly what Chronos is); **compensating transactions and why they're not rollbacks** (you can't un-send an email; you send an apology)
- **API gateway vs BFF vs service mesh** — three different jobs, routinely conflated
- **Anti-patterns**: distributed monolith, shared database, chatty interfaces, nano-services, the entity service ("UserService" that everything calls is a bottleneck and a coupling magnet)
- **Strangler fig** — how you actually migrate a live system, incrementally, with a reversible step at every stage

#### 📄 Sources
- **"Building Microservices" 2nd ed.** — Sam Newman. The reference.
- **"Monolith to Microservices"** — Sam Newman. More practically useful than the first book.
- **"Software Architecture: The Hard Parts"** — Ford & Richards. Especially the data-decomposition chapters.
- **"Fundamentals of Software Architecture"** — Ford & Richards. Read before Hard Parts.
- **"The Majestic Monolith"** — DHH; **"Prime Video: reducing costs by 90%"** — AWS; **"Deconstructing the Monolith"** — Shopify. Read all three for the counterweight.
- **"Pattern: Saga"** and the rest of `microservices.io` — Chris Richardson's pattern catalog.

#### 🛠 CORE PROJECT — `decompose` (two-part)
Part 1: the deliberately-bad split, measured. Part 2: the correct split, measured. Publish both, side by side, with the numbers.

📈 **Exit Criteria**
- [ ] p99, availability (computed from dependency availability), and deploy-coupling comparison between the two designs
- [ ] A saga implemented **both ways** (choreography and orchestration) for the same flow, with an honest assessment of debuggability
- [ ] A compensating transaction that handles the "compensation itself fails" case
- [ ] A written ADR: "why we split here and not there"

---

### 5.2 — Event Sourcing & CQRS

> 🔥 **THE WALL — The Unfixable Bug**
> Build an event-sourced ledger. Deploy. Now discover a bug in an event handler that has been silently producing wrong projections for 6 months.
>
> Fix the handler and replay. **Your events are immutable — but your handler wasn't, and now you must reason about versioning, upcasting old event schemas, and what to do about the side effects those old events already caused** (emails were sent; you can't un-send them by replaying).
>
> This teaches: event schema versioning, upcasters, the distinction between rebuildable projections and irreversible side effects, and why event sourcing is powerful *and* a serious long-term commitment.

#### 📖 Theory
- Events as the source of truth; state as a fold over events; the append-only store
- **Projections/read models**, rebuild from zero, and the operational reality of rebuilding a 500M-event projection
- **Snapshots** — and why they're a cache, never a source of truth
- **Event schema versioning**: upcasting, weak schema, and never changing a published event's meaning
- **CQRS** — the read/write split; **and the honest note that CQRS does not require event sourcing and event sourcing does not require CQRS**; they're independently useful
- **Eventual consistency in the UI** — the read-your-own-writes problem after a command, and the three standard fixes
- **When event sourcing is right**: audit is a requirement (finance, healthcare), temporal queries ("what did we believe on March 3rd?"), complex domains with many derived views. **When it's wrong: CRUD apps, small teams, unclear domains.**

#### 📄 Sources
- **"Event Sourcing"** and **"CQRS"** — Martin Fowler.
- **Greg Young's** talks and the "CQRS Documents."
- **"Versioning in an Event Sourced System"** — Greg Young (free book). The part everyone skips and then regrets.
- **"Building a Secure Money Transfer Service"** and the ledger posts — Monzo Engineering.
- **"Immutability Changes Everything"** — Pat Helland (CACM). Read anything by Pat Helland; also **"Life Beyond Distributed Transactions"** and **"Data on the Outside vs Data on the Inside"** — all three are short, deep, and quotable.

#### 🛠 CORE PROJECT — `ledger` ⭐ *(8/10)*
An event-sourced **double-entry** ledger — because double-entry gives you an invariant a machine can check: **every transaction's debits equal its credits, and the sum of all account balances is always zero.**

Requirements: command handlers with optimistic concurrency on the aggregate version · projections (balances, statements, a daily-close report) · snapshotting · schema versioning with at least one upcast · a full rebuild-from-zero path · **an invariant checker that runs continuously** · and a chaos test doing 10,000 concurrent transfers across 100 accounts with random crashes.

📈 **Exit Criteria**
- [ ] After 10,000 concurrent transfers with random process kills, **the ledger sums to zero to the cent** — automated assertion
- [ ] Full projection rebuild from 1M events, with the measured wall-clock time
- [ ] An event schema change handled by an upcaster, with old events still replaying correctly
- [ ] Time-travel query: "what was account X's balance at timestamp T" — answered from events alone
- [ ] A deliberately wrong handler, fixed, and the projection rebuilt — with a written analysis of the already-emitted side effects

---

### 5.3 — Multi-Tenancy & Platform Concerns 🆕

> **v2 had nothing on multi-tenancy, and it's the defining architectural concern of essentially every SaaS backend job.**

> 🔥 **THE WALL — The Noisy Neighbor**
> Build a multi-tenant API. Now have one tenant send 50,000 requests/second and one submit a query that scans 200M rows. **Watch every other tenant's latency go to hell.** Then implement isolation and measure how much you recovered.

#### 📖 Theory
- **Isolation models, from cheap to expensive**: shared everything (row-level `tenant_id`) → shared schema, separate row-level security → schema-per-tenant → database-per-tenant → cluster-per-tenant (**"silo"**). Cost, blast radius, and per-tenant customization tradeoffs at each level.
- **Row-Level Security (Postgres RLS)** — enforcement at the database rather than trusting every query. **The `tenant_id` you forgot in one `WHERE` clause is a data breach**, and RLS is the structural fix.
- **Noisy-neighbor control**: per-tenant rate limits, quotas, concurrency caps, query timeouts, separate worker pools, and **shuffle sharding** for blast-radius reduction
- **Per-tenant cost accounting** — attributing compute, storage, and egress to tenants. **The bridge between engineering and the business, and a strong senior signal.**
- **Cell-based architecture** — partition the whole stack into cells; a failure affects one cell. AWS's model. Read the Builders' Library article.
- **Tenant lifecycle**: onboarding, data export, and **deletion (which GDPR makes a hard requirement, and which is genuinely hard when data is spread across 12 systems and a data lake)**
- **Per-tenant migrations** — you now have 5,000 databases to migrate; how?

#### 📄 Sources
- **AWS SaaS Factory** whitepapers on multi-tenant patterns; **"Reducing the Scope of Impact with Cell-based Architecture"** (AWS).
- **Postgres RLS docs** + Citus/Crunchy multi-tenant guides.
- **"Multi-tenant data isolation"** — the Neon/PlanetScale/Supabase engineering blogs are all good here.

#### 🛠 CHRONOS C8 — make Chronos multi-tenant
Per-tenant queues, quotas, concurrency limits, RLS-enforced data isolation, per-tenant cost accounting (workflow-seconds, storage, API calls), and a tenant-deletion path that provably removes everything.

📈 **Exit Criteria**
- [ ] Noisy-neighbor test: one tenant at 100x normal load; **other tenants' p99 degrades by <10%** — measured
- [ ] A deliberate missing-`tenant_id` query is blocked by RLS — with the test proving it
- [ ] A cost report per tenant that reconciles to total infrastructure cost within 5%
- [ ] Tenant deletion verified by a scan proving zero residual rows across all stores

---

### 5.4 — Service Mesh, Gateways & Zero Trust

Keep v2's content and add the honest framing:

- **What a mesh actually gives you**: mTLS everywhere without app changes, uniform retries/timeouts/circuit-breaking, traffic splitting for canaries, and golden signals for free
- **What it costs**: a sidecar per pod (memory, CPU, +1-3ms per hop), a control plane to operate, and a genuinely steep debugging story. **Ambient/sidecar-less modes exist now precisely because of this.**
- **When you don't need one**: <20 services, or when a good client library gets you 80% of the value
- **Gateway API** replacing Ingress; **xDS** as the universal config protocol
- **Zero trust**: authenticate every request, no network-perimeter trust, **SPIFFE/SPIRE for workload identity** (the standard worth knowing by name)

#### 🛠 CORE PROJECT
Chronos on Kubernetes with Istio/Linkerd: automatic mTLS, a canary rollout with traffic split and automated abort on error-rate, and a distributed trace across the mesh.

📈 **Exit:** measure the mesh's latency tax per hop and its memory cost per pod, and write the honest verdict on whether it was worth it for a system of your size.

---

## ⚡ LEVEL F — Cloud & Data Platform 🆕

> **Why this level exists:** v2 mentioned S3 twice and never covered cloud primitives, batch processing, columnar formats, or data warehousing. Most backend roles require at least one cloud deeply, and data-adjacent work is now a majority of backend work.
>
> **⏱ Budget:** 70–100 hours

---

### F.1 — Cloud Primitives (pick AWS unless you have a reason not to)

> 🔥 **THE WALL — The $4,000 Weekend**
> Build a small system on real cloud infrastructure with a budget alert at $20. Then deliberately create three cost disasters in a sandbox: a NAT gateway processing 500GB of traffic, cross-AZ data transfer in a chatty service, and an un-lifecycled S3 bucket with versioning. **Understanding cloud pricing as an architectural constraint separates senior engineers from everyone else** — most cloud bills are architecture problems wearing a finance costume.

#### 📖 What to actually know
- **Compute**: EC2 instance families and when each matters, spot/preemptible economics, Lambda (cold starts, concurrency limits, the 15-min ceiling, when serverless is wrong), Fargate/Cloud Run, ECS vs EKS
- **Storage**: **S3 in depth** — the consistency model (strong read-after-write since 2020, and know what it was before and why that mattered), storage classes, lifecycle policies, multipart upload, presigned URLs, S3 Select, event notifications, **and the request-rate scaling behavior by key prefix**. EBS vs EFS vs instance store. **Object storage is the foundation of modern data infrastructure — know it cold.**
- **Networking**: VPC, subnets, route tables, security groups vs NACLs, NAT gateway (and its cost), VPC endpoints, PrivateLink, ALB/NLB, Route 53, CloudFront
- **Managed data**: RDS/Aurora (and how Aurora's storage disaggregation works — read the paper), DynamoDB, ElastiCache, MSK, SQS/SNS/EventBridge, Kinesis
- **IAM**: policies, roles, assume-role, instance profiles, **OIDC federation for CI (no long-lived keys)**, least privilege, and the confused-deputy problem
- **Cost engineering**: on-demand vs reserved vs savings plans vs spot; **data transfer as the hidden killer** (cross-AZ, NAT, egress); right-sizing; tagging for attribution; FinOps basics
- **Regions, AZs, and what a "multi-AZ" guarantee actually promises**

#### 📄 Sources
- **AWS Builders' Library** (again — it's the best thing AWS publishes).
- **"Amazon Aurora: Design Considerations for High Throughput Cloud-Native Relational Databases"** (SIGMOD 2017).
- **"AWS Well-Architected Framework"** — skim all six pillars once; it's how cloud architects are expected to think.
- **"The Cloud Resume Challenge"** / **"How I passed the AWS SA-Pro"** style guides only if you want the cert. **The cert is worth little compared to a built system — but it does get past some resume filters.**

#### 🛠 CORE PROJECT — deploy Chronos to real cloud, with a cost model
Terraform-defined: VPC, EKS or ECS, RDS, ElastiCache, S3, ALB, and an OIDC-federated CI pipeline. Then produce **a cost model**: cost per 1,000 workflow executions, broken down by component, with the three biggest levers identified.

📈 **Exit Criteria**
- [ ] `terraform apply` from zero to a working system, and `terraform destroy` leaving nothing behind
- [ ] A unit-economics document: "$X per 1,000 workflows, of which Y% is compute, Z% is data transfer"
- [ ] Three cost optimizations implemented with measured savings
- [ ] Zero long-lived cloud credentials anywhere in the repo or CI

---

### F.2 — Batch Processing & Distributed Compute

> 🔥 **THE WALL — The Job That Takes 14 Hours**
> Write a naive aggregation over 100GB of data on a single machine. It takes hours or OOMs. Then: partition it, process in parallel, and discover **data skew** — one partition holds 60% of the data because you keyed on something with a power-law distribution, and one worker runs for hours while 63 idle.
>
> Skew is *the* defining problem of distributed data processing, and salting/repartitioning is the fix nobody teaches until you've hit it.

#### 📖 Theory
- **MapReduce** and its descendants; why the shuffle is the expensive part
- **Spark**: RDD/DataFrame, lazy evaluation and the DAG, narrow vs wide transformations, the shuffle, partitioning strategies, broadcast joins vs sort-merge joins, **skew handling (salting, AQE)**, caching/persistence, and reading a Spark UI
- **Columnar formats**: **Parquet** (row groups, column chunks, pages, dictionary/RLE encoding, min/max statistics for predicate pushdown), ORC, Arrow as the in-memory standard. **Understanding why Parquet + predicate pushdown gives a 100x scan speedup is a genuinely useful mental model.**
- **Table formats**: Iceberg, Delta Lake, Hudi — ACID on object storage, snapshot isolation, time travel, schema evolution, compaction. **Iceberg is where the industry has converged; know its manifest/metadata design.**
- **Orchestration**: Airflow/Dagster/Prefect — DAGs, idempotent tasks, backfills, and the golden rule: **every batch job must be idempotent and re-runnable for any date**
- **Batch vs streaming**, the Lambda and Kappa architectures, and the modern "just use one engine" position

#### 📄 Sources
- **DDIA Chapter 10.**
- **MapReduce (2004)**, **GFS (2003)**, **Spark/RDD (NSDI 2012)**, **Dremel (2010)** papers.
- **"Spark: The Definitive Guide"** or **"Learning Spark" 2nd ed.**
- **"Designing Data-Intensive Applications" Ch. 10-12** + **"Fundamentals of Data Engineering"** — Reis & Housley (the best modern overview of the data platform landscape).
- **Apache Iceberg spec** — read the table spec; it's clear and short.

#### 🛠 CORE PROJECT — `skew-lab`
Process a 50–100GB dataset (NYC taxi, GitHub Archive, Common Crawl index) with Spark. Deliberately create a skewed join, diagnose it in the Spark UI, and fix it three ways (salting, broadcast join, AQE). Then convert the source from CSV/JSON to Parquet and measure the scan-time and cost difference.

📈 **Exit Criteria**
- [ ] Before/after skew fix: wall clock and the task-duration distribution chart from the Spark UI
- [ ] CSV vs Parquet: bytes scanned, wall clock, and cost, for the same query — expect 10–100x
- [ ] Predicate/projection pushdown demonstrated with the bytes-read metric
- [ ] An Airflow/Dagster DAG that is provably idempotent — run the same day twice and show identical output

---

### F.3 — The Analytics Side: OLAP & Warehouses

- **OLTP vs OLAP** — row store vs column store, and why you should never run analytics on your production primary
- **Warehouses** (Snowflake, BigQuery, Redshift) vs **lakehouses** (Databricks, Iceberg + Trino) vs **real-time OLAP** (ClickHouse, Druid, Pinot). **ClickHouse in particular is worth hands-on time — it's fast, free, and increasingly the default for real-time analytics.**
- **Vectorized execution and late materialization** — the reasons columnar engines are 100x faster
- **Star schema, dimensional modeling, slowly changing dimensions**
- **Serving analytics to users**: pre-aggregation, materialized views, approximate algorithms (HyperLogLog, t-digest for quantiles, count-min sketch) — **probabilistic data structures are a great interview topic and a genuinely useful tool**

#### 🛠 PROJECT — `realtime-analytics`
Build a user-facing analytics dashboard: events → Kafka → ClickHouse (with materialized views for pre-aggregation) → a query API with sub-200ms p99 over 1B rows.

📈 **Exit:** p99 < 200ms for a 1B-row aggregation; a comparison against the same query on Postgres (which will be minutes or impossible); and HyperLogLog-based unique counts with measured error vs exact.

---

### F.4 — Data Contracts, Quality & Governance

- **Schema registry** (Confluent/Apicurio), compatibility modes (backward, forward, full, transitive) — the CI gate that prevents a producer from breaking every consumer
- **Data contracts** — the modern practice: producers commit to a schema and SLA, enforced in CI
- **Data quality**: Great Expectations / dbt tests / Soda — freshness, volume, distribution, and null checks as first-class monitored assertions
- **Lineage** (OpenLineage, DataHub) — "which dashboards break if I change this column?"
- **PII handling in the data platform**: classification, tokenization, deletion propagation (→ Level H)

---

## ⚡ LEVEL G — AI/ML Systems Infrastructure 🆕

> **Why this level exists:** it is 2026. A large and growing share of backend work is serving models, building retrieval systems, and operating GPU-bound infrastructure. v2 had zero coverage. **This is currently the highest-leverage differentiator available to a backend engineer** — the demand vastly exceeds the supply of people who understand both distributed systems and inference economics.
>
> **⏱ Budget:** 60–90 hours · **Prereq:** Level 4, E.3
>
> **Note:** this is *systems* work, not ML research. You do not need to train models or know backpropagation. You need to know how to serve, scale, cache, batch, evaluate, and pay for them.

---

### G.1 — Inference Serving & Token Economics

> 🔥 **THE WALL — The $18,000 Bill**
> Build a naive LLM-backed endpoint: user request → API call → response. Now load test it, and measure four things nobody measures: **time to first token (TTFT)**, **inter-token latency**, **tokens per second per user under concurrency**, and **cost per request**.
>
> Then discover: your p99 TTFT is 8 seconds under load; you're paying for the same prompt prefix 10,000 times a day; one user's 100k-token request blocks everyone; and a retry loop on a timeout doubles your bill while the original request is still running.

#### 📖 Theory
- **The inference request lifecycle**: prefill (compute-bound, parallel over the prompt) vs decode (memory-bandwidth-bound, sequential per token). **This asymmetry explains nearly every performance property of LLM serving.**
- **Latency metrics that matter**: TTFT, TPOT/ITL, end-to-end, and why the usual p99-of-total-latency is the wrong metric for a streaming response
- **Continuous/in-flight batching** — the single biggest throughput win (vLLM, TensorRT-LLM); why static batching wastes the GPU
- **KV cache**: what it is, why it dominates GPU memory, PagedAttention, and **prefix caching** (shared system prompts cached across requests — often a 50%+ cost reduction for free)
- **Streaming**: SSE for token streaming, backpressure on a slow client, and cancellation (**a cancelled request must actually stop generating, or you pay for tokens nobody reads**)
- **Token-aware rate limiting** — requests-per-minute is the wrong unit; you need TPM and RPM, and you must *estimate* the cost before admitting the request
- **Semantic caching** — embed the query, look up near-duplicates, and the accuracy/staleness tradeoff
- **Routing and fallback** — small model first, escalate on difficulty; multi-provider failover; and the fact that **providers have outages and rate limits, so your reliability engineering from Level 4 applies directly**
- **Cost accounting** — per-request, per-tenant, per-feature, with token counts attributed
- **Self-hosted vs API**: GPU economics, utilization, cold starts on GPU nodes, quantization (INT8/FP8/AWQ/GPTQ) and its quality tradeoff, speculative decoding

#### 📄 Sources
- **vLLM's paper: "Efficient Memory Management for Large Language Model Serving with PagedAttention"** (SOSP 2023). Read it — it's the clearest explanation of why inference serving is hard.
- **"AI Engineering"** — Chip Huyen (2025). The best systems-oriented book on building with models.
- **"Designing Machine Learning Systems"** — Chip Huyen. For the classical-ML side.
- **Anthropic and OpenAI API docs** on prompt caching, batching, and streaming — the actual mechanics you'll build against.
- **vLLM / SGLang / TensorRT-LLM docs** for self-hosted serving.
- **"LLM Inference Performance Engineering: Best Practices"** — Databricks/MosaicML.

#### 🛠 FLAGSHIP PROJECT #8 — `llmgw` ⭐⭐ *(9/10)*

**An LLM inference gateway** — the piece every company building with models needs and few have done well.

Features: multi-provider routing with automatic failover · **token-aware rate limiting** (TPM + RPM per tenant, with pre-request cost estimation) · **semantic caching** (embedding-based near-duplicate detection with a configurable similarity threshold) · exact prefix caching · request batching where the provider supports it · SSE streaming pass-through **with correct cancellation propagation** · per-tenant cost accounting and budgets with hard cutoffs · retries with jitter that **do not** double-bill · full observability (TTFT, ITL, tokens/sec, cost per request, cache hit rate) · and a fallback chain (big model → small model → cached → graceful error).

📈 **Exit Criteria**
- [ ] **Measured cost reduction** from semantic + prefix caching on a realistic workload — target ≥40%, and report the cache hit rate and any quality impact
- [ ] TTFT p99 under load, with and without batching/queueing — charted
- [ ] Client disconnect **provably** stops generation (show the provider-side token count for a cancelled request)
- [ ] A tenant hitting their budget is cut off cleanly, with a correct error, and no over-spend
- [ ] Chaos test: primary provider returns 429s and 500s; the gateway degrades to the fallback chain with **zero user-visible errors**
- [ ] A cost dashboard by tenant and by feature

> **Why this is a 9/10 in 2026:** it sits exactly at the intersection of "classic backend engineering" (rate limiting, caching, failover, streaming, multi-tenancy, cost) and "the thing every company is currently building." It demonstrates that your Level 4 skills transfer to the newest problem domain, which is precisely what hiring managers are trying to determine.

---

### G.2 — Vector Search & Retrieval Infrastructure

> 🔥 **THE WALL — Recall You Can't See**
> Build semantic search with an approximate nearest-neighbor index. It returns results. They look fine. **But you have no idea what you're missing** — ANN indexes trade recall for speed, and the failure is silent.
>
> Compute ground truth with brute-force exact search on 100k vectors, then measure your index's **recall@10**. It may well be 0.75 when you assumed 1.0. Now tune it and plot the **recall-vs-latency curve** — the fundamental tradeoff of the entire field.

#### 📖 Theory
- **Embeddings** as opaque vectors; cosine vs dot vs L2, and normalization
- **The exact-search cost**: brute force is O(N·d) — fine at 100k vectors, impossible at 100M
- **ANN algorithms**: **HNSW** (hierarchical navigable small world graphs — `M`, `efConstruction`, `efSearch` and what each controls), IVF-PQ (inverted file + product quantization), ScaNN, DiskANN for billion-scale on SSD
- **Quantization** — scalar, product, and binary — the memory/recall tradeoff
- **The metrics that matter**: recall@k, QPS, p99 latency, index build time, memory per vector. **A vector DB benchmark without recall is meaningless, and most published ones are.**
- **Filtering + ANN (the hard part)**: pre-filter destroys the graph's connectivity, post-filter destroys recall. This is where most real systems break.
- **Hybrid search**: BM25 + vector, fused with Reciprocal Rank Fusion; **and the fact that keyword search often beats pure vector search for real queries**
- **Reranking** — cross-encoders as a second stage
- **Where to put it**: pgvector (usually the right first answer — one fewer system to operate), Qdrant/Weaviate/Milvus, Elasticsearch/OpenSearch kNN, or a managed service
- **Incremental indexing, deletes, and index rebuilds** — the operational reality nobody discusses

#### 📄 Sources
- **"Efficient and robust approximate nearest neighbor search using HNSW graphs"** — Malkov & Yashunin. The HNSW paper; readable.
- **`ann-benchmarks.com`** — the standard benchmark suite and its methodology.
- **pgvector's README and the HNSW implementation** — short enough to read entirely.
- **"Product Quantization for Nearest Neighbor Search"** — Jégou et al.

#### 🛠 CORE PROJECT — `hnsw-from-scratch` *(Reimplementation, 8/10)*
Implement HNSW yourself (~400 lines), index 1M vectors, and produce the **recall-vs-latency curve** against exact brute-force ground truth. Then benchmark against pgvector and one dedicated vector DB on identical data.

📈 **Exit Criteria**
- [ ] recall@10 vs QPS curve for your implementation at several `efSearch` values
- [ ] Your implementation within 3x of pgvector's QPS at equal recall (or a written analysis of why not)
- [ ] Filtered search implemented, with the recall degradation measured — **this is the number that matters in production and nobody publishes it**
- [ ] Memory per vector measured for each quantization level, with the recall cost

---

### G.3 — RAG & Agent Infrastructure (as a systems problem)

- **The ingestion pipeline** as a real data pipeline: chunking strategies and their measurable effect on retrieval quality, incremental re-indexing, deduplication, **and document-level access control that must be enforced at retrieval time** (a retrieval system that ignores permissions is a data breach with extra steps)
- **Evaluation as engineering**: a golden dataset, retrieval metrics (recall@k, MRR, nDCG), end-to-end metrics, LLM-as-judge and its biases, and **regression testing for prompt/model changes in CI**. Shipping a prompt change without an eval suite is shipping untested code.
- **Agent execution as a distributed systems problem**: tool calls are RPCs (they need timeouts, retries, idempotency, and circuit breakers), multi-step agents need **durable execution** (this is literally Chronos — connect them), loops need budget caps, and every tool call is an authorization decision
- **Guardrails**: input validation, prompt-injection defense as an *architectural* problem (untrusted content must never gain the authority of an instruction; capability-limiting beats filtering), output validation, PII redaction
- **Observability for nondeterministic systems**: tracing multi-step chains, capturing inputs/outputs for replay, and versioning prompts as artifacts

#### 🛠 PROJECT — connect Chronos to G.3
Run a multi-step agent workflow **on Chronos**: each tool call is a durable activity with retries and timeouts; the workflow survives a worker crash mid-agent-run and resumes exactly where it left off; and a budget cap kills runaway loops.

📈 **Exit:** kill the worker mid-agent-run and show it resumes without repeating completed tool calls (this is exactly the durable-execution value proposition, demonstrated concretely) · a golden eval suite running in CI · and a per-run cost cap that provably holds.

---

## ⚡ LEVEL H — Security, Privacy & Compliance

> **⏱ Budget:** 50–70 hours · **Prereq:** Level 1, Level 5

---

### H.1 — AuthN & AuthZ, Properly

> 🔥 **THE WALL — Break Your Own Auth**
> Build a JWT-based auth system, then attack it yourself:
> 1. Set `alg: none` and see if it's accepted (the classic)
> 2. Sign with the public key using HMAC when the server expects RS256 (algorithm confusion)
> 3. Log out, then keep using the old token. **It works — for up to 15 minutes.** JWTs cannot be revoked, and this is the single most important thing to understand about them.
> 4. Steal a refresh token and use it twice — does the system detect the theft? (It should: **refresh token rotation with reuse detection** is the correct design.)
> 5. **IDOR**: change the ID in a URL and read another user's data. This remains the #1 real-world API vulnerability.

#### 📖 Theory
- **Passwords**: Argon2id (or bcrypt/scrypt), correct parameters, why "salting" is table stakes and peppering is optional, timing-safe comparison, breach-list checks
- **Sessions vs JWTs, honestly**: sessions are revocable, simple, and correct for most apps. JWTs trade revocability for statelessness. **Short access token + rotating refresh token + a revocation list is the standard compromise.** Read "Stop using JWT for sessions" and be able to argue both sides.
- **JWT security**: always pin the algorithm server-side, validate `iss`/`aud`/`exp`/`nbf`, key rotation via JWKS, never put secrets in the payload
- **OAuth 2.0 / OIDC**: authorization code + **PKCE** (the only correct flow for public clients now), client credentials for service-to-service, why implicit and password grants are deprecated, and the difference between **authentication (OIDC) and authorization (OAuth)** — routinely confused
- **Authorization models**: RBAC → ABAC → **ReBAC** (Google Zanzibar — read the paper; it's how Google Docs sharing works and it's the model everyone is copying); policy engines (OPA/Cedar); and **where authorization is enforced** (never only in the UI, never only in the gateway)
- **Service-to-service identity**: mTLS, SPIFFE, workload identity federation

#### 📄 Sources
- **"OAuth 2.0 Simplified"** — Aaron Parecki; **RFC 9700 (OAuth 2.0 Security Best Current Practice)**; **RFC 8725 (JWT BCP)**.
- **"Zanzibar: Google's Consistent, Global Authorization System"** (USENIX ATC 2019). **One of the most practically influential papers of the last decade.**
- **OWASP API Security Top 10** and the **OWASP Cheat Sheet Series** — the single most useful free security resource for backend engineers.

#### 🛠 CORE PROJECT — `authlab` *(Adversary archetype, 8/10)*
Build the auth service (Argon2id, short-lived access tokens, rotating refresh tokens **with reuse detection**, revocation via a Redis denylist, OIDC login, MFA/TOTP, per-account rate limiting on auth endpoints, secure cookie flags) — **and the attack suite that tries all five wall attacks plus token replay, session fixation, and IDOR across every endpoint.**

📈 **Exit Criteria**
- [ ] All attacks in the suite fail against the final version — and **each one succeeds against a "vulnerable" branch you keep for comparison**, with the diff showing the fix
- [ ] Refresh-token reuse detection revokes the entire token family and logs a security event
- [ ] An automated IDOR scanner that walks every endpoint with two users' credentials and asserts isolation
- [ ] A written threat model for the service (STRIDE)

---

### H.2 — Application & Infrastructure Security

- **The OWASP Top 10 and API Top 10 — exploit each one in your own code**, then fix it. Reading about SQL injection teaches nothing; extracting your own database with `' OR 1=1--` teaches permanently.
- **Injection**: SQL (and why parameterized queries, not escaping), NoSQL, command, template, LDAP
- **SSRF** — the one that gets cloud services owned (metadata endpoint `169.254.169.254`, IMDSv2 as the fix); **read the Capital One breach post-mortem**
- **Deserialization, XXE, path traversal, mass assignment**
- **Secrets management**: Vault/cloud secret managers, dynamic short-lived credentials, secret scanning in CI (gitleaks), and **rotation as a practiced procedure, not a policy document**
- **Supply chain**: dependency pinning and lockfiles, SBOM, `cosign` signing, SLSA levels, provenance. **Read the `event-stream`, SolarWinds, and `xz-utils` incidents** — the last one especially; it's the most sophisticated supply-chain attack ever publicly caught.
- **Crypto for engineers**: what to use (libsodium, AES-GCM, TLS 1.3, Argon2), what never to do (roll your own, ECB, static IVs, `==` on secrets), envelope encryption with a KMS, encryption at rest vs in transit vs in use
- **Threat modeling**: STRIDE, data-flow diagrams, trust boundaries. **Do one for Chronos.**
- **Rate limiting and abuse prevention as security controls** (credential stuffing, enumeration, scraping)

#### 🛠 PROJECT — `vulnlab`
Take one of your own services, introduce 10 real vulnerabilities on a branch, write working exploits for each, then fix each and write the detection (a test, a lint rule, a WAF rule, or a monitoring alert).

📈 **Exit:** 10 working exploits + 10 fixes + 10 detections + a STRIDE threat model. **This is also excellent interview material** — "walk me through a security issue you found" becomes a strong answer.

---

### H.3 — Privacy, Data Protection & Compliance

> **v2 had nothing here, and it's a routine part of senior backend work at any company with EU or California users.**

- **PII classification and data mapping** — you cannot protect what you haven't inventoried
- **GDPR's engineering consequences**: lawful basis, data minimization, **the right to erasure (Article 17) — which is genuinely hard when data is in Postgres + Kafka + S3 + a warehouse + backups + a vendor's system**, the right to access/portability, breach notification within 72 hours
- **Deletion strategies**: hard delete, soft delete + purge job, **crypto-shredding (encrypt each user's data with a per-user key; delete the key)** — the elegant answer for immutable stores and backups, and a great design-interview answer
- **Data residency** and regional isolation
- **Pseudonymization vs anonymization vs tokenization** — and why "we removed the names" is not anonymization
- **Audit logging**: what, immutability, retention, and the fact that audit logs themselves contain PII
- **SOC 2 / ISO 27001 / PCI-DSS / HIPAA** — what they actually require of an engineer (access control, change management, logging, encryption, vendor review). You don't need to be an expert; you need to not be surprised.

#### 🛠 PROJECT — `gdpr-ready`
Implement, in Chronos or the ledger: a data inventory, per-user crypto-shredding, a working "export all my data" endpoint, a deletion pipeline that propagates across Postgres + object storage + the event log + the analytics store, and an immutable audit log.

📈 **Exit:** a deletion request provably removes or renders-unreadable every trace across all five stores, verified by an automated scan · and a written data-flow map with trust boundaries.

---
## ⚡ LEVEL 6 — System Design Mastery

> **⏱ Budget:** 80–120 hours · **Chronos milestone:** C9 · **Prereq:** everything

---

### 6.1 — The Framework (and what interviewers are actually scoring)

#### The 45-minute structure

| Minutes | Phase | What you must do |
|---|---|---|
| 0–5 | **Requirements** | Functional (what it does) + **non-functional (scale, latency, consistency, availability)**. Write them on the board. Ask: how many users? read/write ratio? latency target? can we lose data? |
| 5–10 | **Estimation** | QPS, storage/year, bandwidth, memory for cache. **Round aggressively.** Show the arithmetic. |
| 10–15 | **API + data model** | The 3-5 endpoints that matter. The core entities. This anchors everything after. |
| 15–25 | **High-level design** | Boxes and arrows. Data flow for the primary read path and the primary write path. **State your choices as choices.** |
| 25–40 | **Deep dive** | The interviewer picks. Go deep. This is where the grade is decided. |
| 40–45 | **Failure modes + scale** | What breaks first? What happens when a component dies? What at 10x? What do you monitor? |

#### The rubric interviewers are actually filling in

| Signal | Weak (L3) | Strong (L5+) |
|---|---|---|
| **Requirements** | Starts drawing immediately | Spends 5 min narrowing scope; states what's out of scope |
| **Estimation** | Skips it or hand-waves | "100M DAU × 10 posts read = 1B reads/day ≈ 12k QPS average, 40k peak" |
| **Tradeoffs** | "I'll use Cassandra" | "I'll use Cassandra because writes dominate and I need multi-DC — but I'm giving up ad-hoc queries and I'll need a separate store for analytics" |
| **Failure modes** | Assumes everything works | "When the cache tier restarts, origin load goes 20x — so I need staged restarts and request coalescing" |
| **Numbers** | Vague | Quotes real latencies and capacities from measurements they've taken |
| **Depth** | Same altitude throughout | Zooms from architecture to a specific index and back |
| **Communication** | Silent or rambling | Narrates thinking; checks in; adjusts on hints |

> **The single highest-leverage habit:** say the words *"I'm optimizing for X, which costs me Y."* Every time. It is the phrase that separates senior candidates from everyone else, and it's trainable.

#### Estimation numbers to memorize

```
1 machine:      ~10-50k QPS simple requests · ~64-256GB RAM · ~10-40 cores
Postgres:       ~5-50k simple QPS/instance · ~1-5k writes/s w/ fsync (higher w/ group commit)
Redis:          ~100k-1M ops/s single instance (single-threaded!)
Kafka:          ~100k-1M msg/s per broker (small messages, batched)
Disk:           NVMe ~500k-1M IOPS · ~3-7 GB/s · HDD ~100-200 IOPS
Network:        10 Gbps NIC = 1.25 GB/s · same-AZ RTT ~0.3-0.5ms · cross-region 30-150ms
Storage:        1 char ≈ 1 byte · UUID = 16 bytes · timestamp = 8 · a "row" ≈ 100-1000 bytes
Time:           1 day = 86,400s ≈ 10^5 · 1 month ≈ 2.6M s · 1 year ≈ 31.5M s
Handy:          1M req/day ≈ 12 QPS · 1B req/day ≈ 12k QPS
```

---

### 6.2 — The 20 Canonical Designs (build the doc, not just the whiteboard)

For each: produce a **written design doc** (§J.1's template) with requirements, estimates, the diagram, the data model, **three alternatives you rejected with reasons**, failure modes, and the scaling story. Twenty of these is a portfolio in itself.

**Tier 1 — the fundamentals (do all 8)**
1. **URL shortener** — hashing vs counters, the base62 encoding, cache design, analytics fan-out, custom aliases and the collision problem
2. **Rate limiter as a service** — distributed counters, the accuracy/latency tradeoff, multi-tenancy
3. **Distributed cache (Redis-like)** — consistent hashing, replication, eviction, cluster resharding
4. **News feed / timeline** — fan-out on write vs read, **the celebrity problem and the hybrid solution**, ranking, pagination with a moving feed
5. **Chat / messaging** — delivery guarantees, ordering, presence, read receipts, offline delivery, group scaling, end-to-end encryption implications
6. **Notification system** — multi-channel, priority, deduplication, rate limiting per user, delivery tracking, quiet hours, and the "don't notify 10M people at once" problem
7. **Web crawler** — frontier management, politeness, dedup at scale (Bloom filters), distributed coordination, trap detection
8. **Search autocomplete** — trie vs FST, distributed sharding, ranking, personalization, and the sub-50ms latency budget

**Tier 2 — the infrastructure designs (do 6)**
9. **A message queue (Kafka-like)** — partitioning, replication, ISR, consumer groups, exactly-once
10. **Object storage (S3-like)** — metadata service, erasure coding vs replication, consistency, multipart, lifecycle
11. **A distributed job scheduler (this is Chronos — you have the real answer)**
12. **Container orchestrator (Kubernetes-like)** — the reconciliation loop, scheduler design, etcd as the state store, and how the control plane survives its own restart
13. **CI/CD system (GitHub Actions-like)** — job scheduling, runner fleets, artifact storage, secret injection, tenant isolation for untrusted code
14. **Monitoring/metrics system (Prometheus-like)** — the TSDB, ingestion, cardinality limits, query engine, long-term storage, downsampling

**Tier 3 — the product-scale designs (do 6)**
15. **Ride sharing (Uber)** — geospatial indexing (**geohash vs S2 vs H3** — know all three), matching, real-time location updates at scale, surge, and the dispatch consistency problem
16. **Video streaming (YouTube/Netflix)** — upload, transcoding pipeline, adaptive bitrate, CDN strategy, recommendations, and the thumbnail/metadata read path
17. **Payment system** — idempotency, double-entry ledger, reconciliation, the saga across payment-processor boundaries, PCI scope, and **what happens when the processor times out** (the hardest question in the design)
18. **Google Docs / collaborative editing** — **OT vs CRDT** (know the difference and the tradeoff), presence, offline, conflict resolution, and the history/undo model
19. **Ticketmaster / flash sale** — the extreme-contention problem: inventory reservation, virtual waiting rooms, queue-based admission, and preventing overselling **without** a global lock
20. **An LLM API platform** — token-based rate limiting, GPU scheduling and batching, streaming, cost attribution, multi-tenancy, model versioning, and safety filtering (**increasingly asked in 2026 interviews**)

> **How to practice:** one design every 3 days. First pass alone with a 45-minute timer. Second pass: read how the real company did it (the engineering blogs). Third pass: write the doc. Fourth pass: explain it out loud to a camera in 45 minutes and watch it back. **The fourth step is the one everyone skips and it's the one that improves you fastest.**

---

### 6.3 — 🔥 INCIDENT ARCHAEOLOGY: Rebuild 10 Famous Outages

> **This is the most unique section of this roadmap.** Nobody does this, and it is the most efficient way to learn failure modes that exist — because every one of these took down a multi-billion-dollar company, was written up publicly in detail, and has a reproducible core mechanism.
>
> **For each:** read the public postmortem → **build a minimal local reproduction** → observe the failure → implement the fix → write your own analysis of what you'd have done differently. Each takes 4–12 hours.

#### FLAGSHIP PROJECT #7 — `incident-lab` ⭐⭐⭐ *(Autopsy archetype, 10/10)*

| # | Incident | The mechanism you'll reproduce | What it teaches |
|---|---|---|---|
| 1 | **AWS S3 outage, Feb 2017** | An operator command with a typo removed far more capacity than intended; the subsystem's restart had never been tested at that scale and took hours | Blast radius of operational tooling · **never-tested recovery paths** · why the status page depended on S3 (circular dependency) |
| 2 | **GitHub outage, Oct 2018** | A 43-second network partition between coasts caused an automated failover; the two sides then accepted conflicting writes → 24 hours of manual reconciliation | **Split-brain** · orchestrated failover across regions · why "automatic failover" needs fencing · RPO in practice |
| 3 | **Cloudflare outage, July 2019** | A regex with catastrophic backtracking deployed globally in one step consumed 100% CPU on every edge machine | **ReDoS** · global config deploys need staged rollout · CPU limits on user-supplied patterns · the value of a kill switch |
| 4 | **Cloudflare outage, July 2020** | A router config change caused a backbone withdrawal cascading across regions | Config as the #1 cause of outages · staged rollout for network config |
| 5 | **Facebook/Meta outage, Oct 2021** | A backbone config change withdrew BGP routes for the authoritative DNS servers; the entire company vanished from the internet — **including the internal tools and badge readers needed to fix it** | **Circular dependencies in recovery** · DNS as a single point of failure · out-of-band access |
| 6 | **Slack outage, Jan 2021** | Traffic ramp after the holidays → autoscaling was slow → cascading saturation with a retry-driven feedback loop | **Metastable failure** · retry storms · why autoscaling is not a reliability strategy |
| 7 | **Roblox outage, Oct 2021 (73 hours)** | Consul's streaming feature under load → contention → the cluster couldn't recover; **plus the observability system depended on the failed cluster** | Metastable failure at scale · **observability must not depend on the system it observes** · why recovery took 3 days |
| 8 | **Knight Capital, 2012 ($440M in 45 min)** | A deploy to 7 of 8 servers left one running old code, which reactivated a repurposed feature flag | **Partial deploys** · flag reuse · why the kill switch matters more than the feature |
| 9 | **GitLab data loss, 2017** | An engineer ran `rm -rf` on the wrong host during an incident; **then discovered 5 of 5 backup methods had silently been failing** | **Untested backups are not backups** · human factors in incidents · the value of their radical transparency |
| 10 | **Thundering herd / cache stampede** (many companies) | A cache tier restart or mass key expiry → origin sees 20-100x load → collapse | Cold caches · request coalescing · staged restarts · the outage you'll personally cause someday |

**Bonus incidents worth reproducing:** the Postgres transaction-ID wraparound outage (Sentry's write-up), the `left-pad` incident (dependency fragility), the Datadog 2023 multi-region outage (a systemd update restarting the network stack), and the CrowdStrike 2024 global outage (untested content update, no staged rollout, and no safe rollback for a kernel-mode driver — the largest IT outage in history and a masterclass in deployment-safety failures).

**For each reproduction, deliverable:**
- A `docker compose up` that stands up the minimal system
- A trigger script that causes the failure
- Instrumentation showing the failure as it happens (a Grafana dashboard)
- The fix, applied, with the same trigger now failing to cause an outage
- A written analysis: the trigger, the amplifier, the failure of containment, the recovery obstacle, and **the three controls that would have prevented or bounded it**

📈 **Exit Criteria**
- [ ] **6 of 10 reproduced** with a working before/after
- [ ] A single README with a table of all 10, each linked to the official postmortem
- [ ] A synthesis essay: **"the seven patterns behind every major outage"** — you will find them, and they are: config changes, circular dependencies, untested recovery paths, retry amplification, cold caches/thundering herds, silent backup failure, and unbounded resource growth
- [ ] Published

> **Why this is a 10/10:** it's memorable, it's unique, it's directly useful to other engineers, and — most importantly — it gives you a *specific, evidence-backed answer* to every "what could go wrong?" question in every system design interview for the rest of your career. When an interviewer asks "what happens if this config change is bad?", you don't speculate. You say "this is exactly how Cloudflare went down in 2019, and here's the control that prevents it."

---

### 6.4 — Papers That Built the Industry

Read these properly — with the "three-pass" method (Keshav's "How to Read a Paper"): skim for structure, read for content, reconstruct the argument.

| Paper | Year | Built | Why you read it |
|---|---|---|---|
| **The Google File System** | 2003 | HDFS, all distributed FS | Design for the failure model you actually have |
| **MapReduce** | 2004 | Hadoop, Spark | The programming model that made big data tractable |
| **Bigtable** | 2006 | HBase, Cassandra, Scylla | Wide-column data model + SSTables |
| **Chubby** | 2006 | ZooKeeper, etcd | Consensus as a *service*; the lock-service pattern |
| **Dynamo** | 2007 | DynamoDB, Cassandra, Riak | Leaderless replication, quorums, vector clocks, AP tradeoffs |
| **Spanner** | 2012 | CockroachDB, Cloud Spanner | Global consistency via TrueTime; the commit-wait insight |
| **Kafka** | 2011 | Kafka, Pulsar, Redpanda | The log as universal abstraction |
| **Raft** | 2014 | etcd, Consul, CockroachDB, TiKV | Consensus you can actually implement |
| **Dapper** | 2010 | Jaeger, Zipkin, OTel | Distributed tracing |
| **Borg** | 2015 | Kubernetes | Cluster management at scale |
| **TAO** | 2013 | FB social graph | Read-optimized graph serving on top of MySQL |
| **Scaling Memcache at Facebook** | 2013 | — | **The most practically useful paper on this list** |
| **The Tail at Scale** | 2013 | — | Tail latency; hedged requests |
| **Chord / Consistent Hashing** | 1997/2001 | Every sharded system | The idea underneath partitioning |
| **Zanzibar** | 2019 | Authz systems everywhere | Global authorization, done right |
| **Amazon Aurora** | 2017 | Aurora, Neon | Redesigning the DB when you own the storage layer |
| **FoundationDB** | 2021 | FDB, TigerBeetle's approach | **Deterministic simulation testing** |
| **PagedAttention / vLLM** | 2023 | Modern LLM serving | Why inference infrastructure looks the way it does |
| **Gorilla** | 2015 | Prometheus TSDB, all TSDBs | Time-series compression |
| **Dremel** | 2010 | BigQuery, Parquet | Columnar storage + nested data |
| **Calvin / Percolator** | 2012 | Distributed txn systems | Two very different answers to distributed transactions |
| **Metastable Failures** | 2021 | — | The failure class nobody names |

**How to make this stick:** for each paper, write a **one-page summary** answering: what problem, what was the key insight, what did they give up, what would you do differently in 2026, and what system today embodies it. Twenty-two one-pagers is a genuinely impressive public artifact.

---

### 6.5 — Engineering Blogs & People to Follow

**Company blogs (primary sources):** Netflix · Uber · Discord · Cloudflare · Stripe · Meta · Airbnb · Dropbox · LinkedIn · GitHub · DoorDash · Shopify · Figma · Slack · Canva · Datadog · Segment · PlanetScale · Notion · Monzo · Zerodha · **AWS Builders' Library** (the best of all of them) · **the Anthropic and OpenAI engineering blogs** for inference infrastructure.

**Individuals:** Martin Kleppmann · Martin Fowler · Brendan Gregg · Julia Evans · Dan Luu · **Marc Brooker** (`brooker.co.za` — AWS principal engineer; the best working systems writer today) · Kyle Kingsbury (aphyr) · Charity Majors · Werner Vogels · **Hillel Wayne** (formal methods, and the best writing on software-engineering epistemology) · **Alex Petrov** · **Murat Demirbas** (`muratbuffalo.blogspot.com` — paper reviews) · Simon Willison (for the AI-systems side) · Gergely Orosz (**The Pragmatic Engineer** — for the industry/career side).

**Newsletters and aggregators worth the time:** The Morning Paper archive (defunct but the archive is gold) · ByteByteGo · Pointer · Hacker News (the comments on outage postmortems are often better than the postmortems).

---
## 🎯 LEVEL I — The Interview Machine 🆕

> **This level did not exist in v2, and its absence would have been fatal.** You can complete every other level in this document — build a Raft implementation, a workflow engine, a simulation harness — and still be rejected in a 45-minute phone screen because you couldn't invert a binary tree under time pressure.
>
> **This runs DAILY from week 1. 45–60 minutes. It is never batched and never skipped.** Depth work can flex; this cannot, because it is the one thing that cannot be crammed.
>
> **⏱ Budget:** 250–400 hours, spread over the entire program.

---

### I.1 — Data Structures & Algorithms

#### The honest reality of what's tested

Roughly 50% of a FAANG loop is coding. It is not a test of computer science; it is a test of **pattern recognition under time pressure while narrating your thinking**. That is a trainable skill with a known curriculum.

#### The curriculum: ~300 problems, by pattern, not by list

Do **not** grind randomly. Work pattern by pattern. For each pattern: learn the template, do 8–15 problems, then move on and let spaced repetition bring them back.

| # | Pattern | Problems | Must-know representatives |
|---|---|---|---|
| 1 | Arrays, two pointers, sliding window | 25 | Longest substring w/o repeats · container with most water · min window substring |
| 2 | Hashing / prefix sums | 15 | Subarray sum = K · group anagrams |
| 3 | Binary search (incl. on answer) | 20 | Search in rotated array · median of two sorted arrays · **koko eating bananas (binary search on the answer — the pattern people miss)** |
| 4 | Linked lists | 12 | Reverse in k-groups · LRU cache (**build it, don't recall it**) · merge k sorted |
| 5 | Stacks & monotonic stacks | 15 | Largest rectangle in histogram · daily temperatures · valid parentheses variants |
| 6 | Trees & BSTs (DFS/BFS) | 30 | Serialize/deserialize · lowest common ancestor · validate BST · right side view |
| 7 | Heaps / top-K | 15 | Merge k sorted · find median from data stream · task scheduler |
| 8 | Graphs (BFS/DFS/topo/union-find) | 30 | Course schedule · number of islands · word ladder · **union-find — know it cold** · Dijkstra |
| 9 | Backtracking | 15 | Subsets · permutations · N-queens · word search |
| 10 | Dynamic programming | 40 | Climbing stairs → house robber → coin change → LIS → edit distance → knapsack → **LCS** → matrix DP → state-machine DP (stock problems) |
| 11 | Greedy + intervals | 15 | Merge intervals · meeting rooms II · jump game · gas station |
| 12 | Tries | 8 | Implement trie · word search II · autocomplete |
| 13 | Bit manipulation | 8 | Single number · counting bits · subsets via bitmask |
| 14 | Math & geometry | 10 | Pow(x,n) · rotate image · spiral matrix |
| 15 | Design (OOD-in-code) | 15 | LRU/LFU cache · rate limiter · Twitter · hit counter · **these bridge to system design** |
| 16 | Concurrency (increasingly common) | 8 | Bounded blocking queue · print in order · dining philosophers · **web crawler multi-threaded** |

**Total: ~280 problems.** At 2/day that's 20 weeks. **Start on day one.**

#### The method that actually works (and the one that doesn't)

❌ **Doesn't work:** reading solutions, "doing" 500 problems, grinding a list top to bottom.

✅ **Works:**
1. **20-minute timer.** If stuck, spend 5 more on hints only. Then read the solution.
2. **After reading the solution, close it and implement from scratch.** If you can't, you didn't learn it.
3. **Write the pattern down in your own words** in a notes file: "when I see X, consider Y."
4. **Re-do it 3 days later, 10 days later, 30 days later.** Spaced repetition on problems, not just facts. **This is the single biggest determinant of retention.**
5. **Narrate out loud, always.** Silent solving trains the wrong skill. You are being graded on communication as much as correctness.
6. **Write real code**: correct edge cases, no pseudo-code, and state your complexity before you write.
7. **Track a spreadsheet**: problem, pattern, date, time taken, solved unaided (Y/N), next review date.

#### Resources
- **NeetCode 150 / NeetCode 250** (`neetcode.io`) — the best-organized free list, grouped by pattern. **Start here.**
- **LeetCode company-tagged lists** (Premium is genuinely worth $35 for two months before an interview loop)
- **"Elements of Programming Interviews"** — harder and better than *Cracking the Coding Interview*, which is now dated
- **"Algorithm Design Manual"** — Skiena, for actually understanding rather than pattern-matching. The "war stories" are excellent.
- **Codeforces Div 3/4** for speed if you plateau — competitive practice sharpens implementation velocity
- **`interviewing.io`** recorded interviews — watch strong and weak candidates on the same problem. Enormously calibrating.

📈 **Exit Criteria for I.1**
- [ ] 280+ problems, tracked, ≥70% solved unaided on first attempt within 25 minutes
- [ ] A random Medium from an unseen list, solved and narrated in ≤25 min, ≥80% of the time
- [ ] You can state time and space complexity before writing code, every time
- [ ] 15+ Hard problems solved
- [ ] Your review queue is empty (spaced repetition current)

---

### I.2 — The Behavioral Interview

> **At Amazon this is ~50% of the loop. At Google it's "Googleyness & Leadership." At Meta it's the "Jedi" round. Everywhere, it is a real, scored, failable round — and strong technical candidates fail it constantly** because they treat it as small talk.

#### Build your Story Bank: 14 stories, written out

Each story is written in **STAR-L** format — Situation, Task, Action (**60% of the words — and use "I", not "we"**), Result (**with a number**), Learning.

The 14 slots each story must cover (one story can serve 2–3 slots):

| # | The prompt behind it |
|---|---|
| 1 | A technically hard problem you solved |
| 2 | A time you disagreed with your manager or a senior engineer |
| 3 | A time you failed, and what changed afterward |
| 4 | A conflict with a teammate |
| 5 | A time you had to decide with incomplete information |
| 6 | A time you influenced without authority |
| 7 | A time you delivered under a hard deadline / made a scope tradeoff |
| 8 | A time you improved something nobody asked you to improve |
| 9 | A production incident you handled |
| 10 | A time you mentored or unblocked someone |
| 11 | A time you pushed back on a requirement |
| 12 | A time you had to learn something entirely new, fast |
| 13 | Your proudest technical achievement |
| 14 | A time you made the wrong call and had to reverse it |

#### The rules that decide the score
- **Numbers, always.** "Improved performance" is nothing. "Cut p99 from 340ms to 21ms, which let us drop from 12 instances to 4, saving ~$4k/month" is a story.
- **"I," not "we."** The interviewer is scoring *you*. Say "the team decided X; I owned Y."
- **The Learning is not optional.** A failure story without a specific behavior change is a failure story.
- **90 seconds, then stop.** Long answers read as poor judgment. Let them ask follow-ups.
- **Amazon specifically:** map each story to explicit Leadership Principles. Expect 2–3 LP questions per interviewer across a 5-person loop, with deep follow-ups ("what would you do differently?", "what data did you have?", "what did your teammate say?"). **Amazon's follow-up drilling is what catches fabricated stories** — so use real ones.

#### Practice protocol
Record yourself answering each of the 14 on video. Watch it back. It will be uncomfortable and it is the fastest improvement available. Then do 5 mock behavioral interviews with a human.

📈 **Exit Criteria**
- [ ] 14 stories written out, each ≤250 words, each with a quantified result
- [ ] Each delivered in 90 seconds from memory, on video, without notes
- [ ] A matrix mapping stories → Amazon's Leadership Principles and Google/Meta's competencies
- [ ] 5 recorded mock behavioral rounds with feedback

---

### I.3 — Mock Interviews & The Loop

**The most under-used, highest-ROI activity in the entire job search.** Reading about interviews is worthless; doing them under observation is transformative.

- **`interviewing.io`** — anonymous mocks with real FAANG engineers. Paid, and worth more than any course.
- **Pramp / Exponent** — free peer mocks. Lower quality feedback but unlimited volume.
- **A friend with a whiteboard** — better than nothing, and free.
- **Yourself + a camera** — do this weekly regardless.

**Volume target: 20+ mock interviews before your first real loop.** 12 coding, 6 system design, 5 behavioral.

#### What the loops actually look like (2026, approximately — verify with your recruiter)

| Company | Typical loop |
|---|---|
| **Google** | Phone screen (1 coding) → onsite: 2–3 coding, 1 system design (L5+), 1 "Googleyness & Leadership." Then **hiring committee** and **team matching** — a strong loop can still stall at team match, which is normal and not a rejection. |
| **Meta** | Phone screen (2 problems in 45 min — **speed matters more here than anywhere**) → onsite: 2 coding ("Ninja"), 1 system design ("Pirate", E5+), 1 behavioral ("Jedi"). |
| **Amazon** | OA (2 problems + work simulation) → onsite: 4–5 rounds, **every round includes Leadership Principle questions**, plus system design and often an OOD/LLD round. The "Bar Raiser" is an interviewer from outside the team with veto power. |
| **Apple** | Team-specific and highly variable. More domain depth, less algorithmic puzzle. Expect to discuss your actual past work in detail. |
| **Netflix** | Fewer, deeper rounds. Heavy culture emphasis. Senior-only hiring — expect to be treated as a peer and to defend real architectural opinions. |
| **Microsoft** | Coding + design + "as appropriate" (AA) round with a senior leader. |
| **Stripe / Databricks / Anthropic / OpenAI and similar** | Practical over puzzle: debugging an unfamiliar codebase, extending real code, an integration exercise, plus system design. **This roadmap prepares you unusually well for these** because it's all hands-on. |

#### Leveling — know what you're aiming at
Roughly: L3/E3 (new grad) → **L4/E4 (2–5 yrs — solid execution on well-defined tasks)** → **L5/E5 (5+ yrs — owns ambiguous projects end-to-end, the level system design really starts mattering)** → L6+ (multi-team scope). **Interview for the level your evidence supports.** Down-leveling is common; being under-leveled costs years of compensation, so it's worth pushing back with evidence if the loop went well.

---

### I.4 — Resume, Applications & Negotiation

#### The resume (one page, ruthlessly)

Every bullet uses the **X-Y-Z formula** (Google's own advice): *"Accomplished [X] as measured by [Y], by doing [Z]."*

❌ "Worked on backend services using Python and Docker."
✅ "Cut p99 checkout latency 94% (340ms → 21ms) by replacing N+1 ORM queries with a batched DataLoader and adding a two-tier cache, enabling a 3x traffic increase on the same fleet."

**Structure:** Name/contact/GitHub/LinkedIn → a 2-line summary (only if you're changing tracks) → Experience (most space) → **Projects (this is where this roadmap pays)** → Skills → Education.

**Your projects section, written from this roadmap, will look like:**
> **Chronos — Durable Execution Engine** · Go, Postgres, Raft, Kubernetes · [github]
> Workflow engine guaranteeing exactly-once execution across crashes. Implemented Raft consensus from scratch for the control plane; built a deterministic simulation harness running 10,000 seeded fault schedules nightly that surfaced 3 correctness bugs no conventional test caught. Sustains 12k workflow-steps/sec with p99 < 45ms; holds SLO under 10x overload via adaptive load shedding.

That is not a portfolio-project bullet. That is a **staff-engineer-at-an-infrastructure-company** bullet, and it is achievable by following this document.

#### Applications
- **Referrals convert 5–10x better than cold applications.** Get them by being visible (Level J), not by cold-messaging strangers with "can you refer me."
- Apply to **30–60 companies**, not 5. Include second-tier-brand companies with first-tier engineering (Stripe, Cloudflare, Datadog, Databricks, Ramp, Figma, Vercel, Neon, Temporal, ClickHouse, Anthropic, and the many infrastructure startups) — **the work is often better and the interviews reward exactly what this roadmap builds.**
- **Sequence your loops**: interview at 3–4 companies you care less about *first*. Your 5th loop will be dramatically better than your 1st.
- Time your loops to overlap so offers arrive within ~2 weeks of each other.

#### Negotiation (the highest hourly-rate work you will ever do)
- **Never give a number first.** "I'd like to focus on whether this is the right fit; I'm confident we can align on compensation."
- **Competing offers are the only real leverage.** This is why you sequence loops to overlap.
- Negotiate the **whole package**: base, equity (and the vesting schedule — 25/25/25/25 vs Amazon's back-loaded 5/15/40/40), sign-on (the most flexible component), level (**worth more than any of the above over 3 years**), start date, remote flexibility.
- Use `levels.fyi` for market data at your target level, location, and company.
- **Read:** "Ten Rules for Negotiating a Job Offer" — Haseeb Qureshi. The single best free resource on this, and it will plausibly earn you a five-figure sum for two hours of reading.
- Be gracious throughout. You will work with these people.

---

## 🧭 LEVEL J — Senior Craft & Visibility 🆕

> **What separates an L4 from an L5 is not knowing more systems facts. It's judgment, communication, and impact beyond your own keyboard.** This level is how you demonstrate that — and it's also how opportunities start coming to you instead of you chasing them.
>
> **Cadence:** one artifact every two weeks, forever.

---

### J.1 — Design Docs & RFCs (the actual currency of senior engineering)

> At every large company, promotion is decided by **written artifacts**. The design doc is the unit of senior technical work.

**The template — use it for every one of the 20 canonical designs and every Chronos milestone:**

```markdown
# [Title]
**Author** · **Reviewers** · **Status:** Draft/Review/Approved · **Date**

## 1. Summary            (3 sentences. What and why. A reader should be able to stop here.)
## 2. Context & Problem  (What exists today. What's broken. With DATA — graphs, incident links, numbers.)
## 3. Goals              (Bulleted, measurable.)
## 4. Non-Goals          (Explicit. This is where scope creep dies. The most under-used section.)
## 5. Proposal           (The design. Diagrams. Data model. API. Sequence for the critical paths.)
## 6. Alternatives Considered   ← THE SECTION THAT DISTINGUISHES SENIOR WRITING
      For each: what it is, why it's attractive, why we rejected it.
      Minimum three. "Do nothing" is always one of them.
## 7. Risks & Failure Modes     (What breaks. Blast radius. Detection. Mitigation.)
## 8. Rollout Plan       (Phases. Feature flags. Migration. **Rollback at every step.**)
## 9. Operational Impact (Monitoring, alerts, runbook, on-call burden, cost delta.)
## 10. Open Questions
```

**The two sections that separate senior from mid:** *Alternatives Considered* and *Non-Goals*. A doc without a serious alternatives section reads as advocacy, not engineering.

**Also learn:** the **ADR** (Architecture Decision Record) — a 1-page, immutable record of one decision, its context, and its consequences. Keep an `adr/` directory in every project in this roadmap. Cheap to write, extremely senior-looking.

📈 **Exit:** 10+ design docs and 20+ ADRs across your projects, public.

---

### J.2 — Code Review & Working in Large Codebases

**Reviewing well is a leadership act.** Google's Code Review Developer Guide (free, in the `eng-practices` repo) is the standard and should be read in full — it's short.

Key principles worth internalizing:
- **Approve when it improves the codebase, not when it's perfect.** Blocking on preference is how reviews become a bottleneck and how you become the person nobody wants to be reviewed by.
- Distinguish **blocking** from **non-blocking** explicitly. Prefix optional comments with `nit:`.
- Ask questions instead of issuing commands: *"what happens if this is called concurrently?"* teaches; *"add a mutex"* doesn't.
- **Review the tests first.** They tell you what the author believed the code should do.
- Praise good code in review. It's free and it changes team culture.
- **Small PRs.** A 2,000-line PR gets a rubber stamp; a 200-line PR gets a real review. This is the single biggest lever on review quality.

**Practice it for real:** review PRs in an OSS project you use. Even as a non-maintainer, thoughtful review comments are welcome and highly visible.

---

### J.3 — Open Source Contribution

> **A merged PR into a project people have heard of is worth more on a resume than three personal projects**, because it's externally validated: someone with commit rights judged your code good enough to ship.

**The ladder that actually works:**
1. **Use** a project seriously (you already will — Postgres, Kafka, Prometheus, Kubernetes, vLLM, Temporal, ClickHouse, Redis…)
2. **Fix the docs** where they confused you. Real contribution, tiny barrier, gets you through the CLA/CI process once.
3. **Fix a `good first issue`.**
4. **Fix a bug you personally hit.** The best kind — you have the reproduction and the motivation.
5. **Report a bug found by fuzzing** (Level D.2) — high-value, and maintainers love a minimal reproducer.
6. **Implement a requested feature** after discussing the design in an issue first.
7. **Become a regular** in one project. This is where career-changing opportunities come from.

**Target: 5+ merged PRs across 2+ projects.** One should be non-trivial.

**Highest-leverage targets given this roadmap:** whichever database, queue, or orchestrator you spent the most time inside. You'll already know the code — that's the hard part, and you've done it.

---

### J.4 — On-Call, Incidents & Postmortems

Even without a production system, you can build the muscles:

- **Write runbooks** for every service you build: symptoms → diagnosis steps → fixes → escalation. **A service without a runbook is not finished.**
- **Run game days**: schedule a fault injection into your own system, and respond to it as if it were real, with a timer.
- **Write blameless postmortems** for your own `incident-lab` reproductions and for any real failure in your projects. Format: timeline (with timestamps) → impact (quantified) → root cause(s) → **what went well** → what went poorly → action items with owners.
- **Learn the incident-command vocabulary**: incident commander, comms lead, ops lead, severity levels, "stop the bleeding before you find the root cause," and the discipline of **mitigating first, diagnosing second**.
- **Read others' postmortems weekly.** The `danluu/post-mortems` repo is a curated collection.

**"Blameless" means:** the question is never "who," it's "what about the system allowed a reasonable person to do this?" A postmortem that names a person has failed.

---

### J.5 — Writing, Speaking & Visibility

**This is the multiplier.** Everything else in this roadmap makes you good. This makes people know it.

- **Write up every flagship project.** Not a README — a post: the problem, the surprise, the measurements, the mistake you made. **The mistake is the part people remember and share.**
- **Publish the benchmarks.** `c10k-arena`, `syscall-xray`, `overload`, `cache-lab` all produce charts that don't currently exist on the internet. That is the definition of a post worth writing.
- Post where engineers are: your own blog (own the domain), plus cross-posting to Hacker News, Lobsters, and the relevant subreddit. **One post that reaches the front page of HN generates more inbound recruiting than 200 applications.**
- **Give one talk.** A local meetup counts. Explaining Raft or DST out loud to strangers will expose every gap in your understanding, which is exactly why it's valuable.
- **Answer questions in public** — Stack Overflow, project Discords, GitHub discussions. Public helpfulness compounds.

📈 **Exit:** 8+ technical posts · 1 talk · a GitHub profile README that presents the flagship projects clearly with the charts inline.

---
## 📊 ASSESSMENT: The Exit Exams

Each level has an exam above. Here is the meta-system.

### The Three Proofs

You do not "finish" a level. You **prove** it, three ways:

| Proof | What it is | Why |
|---|---|---|
| **1. The Exam** | The written questions at the end of each level, answered without notes, timed | Tests retrieval under pressure — the interview condition |
| **2. The Artifact** | The project, with its exit criteria met and its numbers published | Tests that you can actually build it |
| **3. The Teach-Back** | Explain the level's hardest concept to a camera in 10 minutes, no notes, with a diagram | **The strictest test there is.** You cannot fake teaching. |

**If you fail any of the three, the level is not done.** This is the discipline that makes the difference between someone who "went through" a roadmap and someone who is dangerous.

### The Final Gauntlet — do this before your first real interview

A one-week self-administered assessment:

| Day | Challenge | Pass condition |
|---|---|---|
| 1 | 4 LeetCode Mediums + 1 Hard, timed, narrated aloud, recorded | 4/5 solved unaided within time |
| 2 | 2 system designs from Tier 2 or 3, 45 min each, on video | Both hit the rubric in §6.1 |
| 3 | Debug a sabotaged service (have someone break one of your own projects) | Root cause in <45 min with evidence |
| 4 | All 14 behavioral stories on video, cold | Each ≤90s, quantified, in first person |
| 5 | Write a full design doc for a novel problem in 3 hours | All 10 sections, 3+ real alternatives |
| 6 | Teach-back: Raft, MVCC, and deterministic simulation testing, 10 min each | No notes, correct, with diagrams |
| 7 | Review: watch every video from days 1–6 and grade yourself against the rubrics | Honest scoring |

**Pass = ready to interview.** Fail any day → that's your next two weeks of work.

### The Spaced Repetition Deck

Build it as you go — one card per non-obvious fact. Target ~800 cards by the end. Categories: latency numbers · protocol details · isolation-level anomalies · Raft rules · algorithm complexities · Linux commands and what they answer · failure modes · estimation constants.

**Write your own cards. 15 min/day. Non-negotiable.** This is what makes the difference between knowing something in month 3 and knowing it in month 14 when the interview happens.

---

## 📅 THE HONEST TIMELINE

> **v2 claimed "26–32 weeks at 2 hours/day" — roughly 400 hours — for material that includes MIT 6.5840 (150–250h alone), a full DSA track (250–400h), and a dozen substantial systems projects. That estimate was off by about 4x, and following it would have set you up to feel like a failure while doing everything right.**
>
> Here are three honest paths. All three assume the Interview Track runs daily throughout.

### The realistic total

| Track | Hours |
|---|---|
| Depth (Levels 0–6, A–H) | 1,100 – 1,600 |
| Interview (Level I) | 250 – 400 |
| Craft & Visibility (Level J) | 100 – 150 |
| **Total** | **1,450 – 2,150 hours** |

### Path A — "Employed, serious" · 15 h/week · **~24 months**

```
Mon–Fri: 1h interview track (DSA/behavioral) + 1h depth, alternating focus
Sat:     4h deep work (the project block — this is where real progress happens)
Sun:     3h deep work + 1h review/writing
```
**Interview at month 14–16** even if not "done." You will not feel ready. Interview anyway — the first three loops are practice and they calibrate everything else.

### Path B — "Aggressive, employed" · 25 h/week · **~15 months**
2h weekdays + 7h weekends. Sustainable for about a year with genuine discipline. **Plan a deliberate rest week every 8 weeks** or you will burn out around month 5, which is the most common failure mode of programs like this.

### Path C — "Full time" · 45 h/week · **~8–9 months**
```
Morning   (3h): Depth track — hardest material when you're freshest. Never negotiate this block.
Midday    (1h): Interview track — DSA
Afternoon (3h): Project work
Evening   (1h): Reading, review deck, writing
```
Do **not** exceed 45 focused hours/week. Diminishing returns are steep and burnout is the single largest cause of failure on multi-month programs like this one.

### The Phased Schedule (Path A/B; scale for C)

| Phase | Months (A) | Levels | Chronos | Flagships shipped |
|---|---|---|---|---|
| **1 — Foundations** | 1–4 | 0, C, 1 | C0, C1 | `c10k-arena`, `latency-lab`, `syscall-xray` |
| **2 — Structure & Storage** | 4–9 | A, 2, D.1–2 | C2, C3 | `h2spec-clean`, `pgshift`, `crashdb` |
| **3 — Operations** | 8–12 | B, 4, E | C4, C7 | `overload`, `cache-lab`, `lb-lab` |
| **4 — The Hard Part** | 11–17 | 3, D.3–5 | C5, C6 | `simd`, `elle-lite`, Raft |
| **5 — Architecture & Platform** | 16–20 | 5, F, G, H | C8 | `llmgw`, `ledger` |
| **6 — Synthesis** | 19–24 | 6, J | C9 | `incident-lab`, 20 design docs |
| **Interview loops** | 14→ | ongoing | | |

> **Note the overlaps.** They're intentional — this is the BFS principle from v2, which was right. While Raft compiles, you're doing design docs. While a load test runs, you're doing DSA.

### The Weekly Template

```
┌─────────────────────────────────────────────────────────────────────┐
│ EVERY DAY (45–75 min)                                               │
│  · 15 min  spaced repetition deck                                   │
│  · 30–60 min  DSA (2 problems) or behavioral prep                   │
├─────────────────────────────────────────────────────────────────────┤
│ WEEKDAY DEPTH (60–120 min)  — one Learning Loop step per session    │
│  Mon: Break + Diagnose      Tue: Theory                             │
│  Wed: Rebuild               Thu: Measure                            │
│  Fri: Write it up                                                   │
├─────────────────────────────────────────────────────────────────────┤
│ WEEKEND (4–8 h)  — the project block. Long uninterrupted work.      │
│  Nothing hard ever gets built in 45-minute slices.                  │
├─────────────────────────────────────────────────────────────────────┤
│ BIWEEKLY  · one published artifact (post, design doc, or OSS PR)    │
│ MONTHLY   · one mock interview · review your tracking spreadsheet   │
│ QUARTERLY · a level exit exam · update resume/GitHub with new work  │
└─────────────────────────────────────────────────────────────────────┘
```

### When you fall behind (you will)

- **Never drop the daily interview track.** Drop depth instead. Depth can be made up; DSA fluency decays.
- **Never drop the review deck.** 15 minutes.
- **Ship something small rather than nothing.** A finished 60%-scope project beats an abandoned 100%-scope one, every time.
- **Cut the "nice" levels first if you must:** F (Cloud/Data) and G (AI systems) are the most cuttable for a pure-distributed-systems role — though G is currently the highest-differentiation-per-hour section in the whole document.

---

## 💼 Turning This Into a Resume and a GitHub That Converts

### Your GitHub profile, after this roadmap

A pinned-repo strategy. Six pins, chosen for *legibility*, not for what took longest:

```
📌 chronos          Durable execution engine · Go · Raft · deterministic simulation
                    ★ diagram + throughput chart + "3 bugs found by simulation" in README

📌 incident-lab     Local reproductions of 6 famous production outages, with fixes
                    ★ the table of outages is the hook; every engineer wants to read this

📌 overload         Load shedding & adaptive concurrency lab · the goodput-collapse curves
                    ★ one chart tells the entire story

📌 c10k-arena       Six concurrency models benchmarked to 50k connections (incl. io_uring)
                    ★ the six-line latency chart

📌 h2spec-clean     HTTP/2 from scratch · 146/146 conformance tests passing
                    ★ the passing conformance output, screenshotted

📌 pgshift          Zero-downtime schema migration: 50M rows backfilled under live load
                    ★ the two side-by-side latency graphs (naive vs correct)
```

**Every README must have, in the first screen:** one sentence saying what it is · an architecture diagram · the headline number or chart · `make demo`.

**Your profile README:** three sentences about what you work on, then the six projects with their headline numbers. No badge walls. No "languages I know" charts.

### The Resume Projects Section

Three projects, three lines each, every line with a number:

> **Chronos — Durable Execution Engine** · Go, PostgreSQL, Raft, Kubernetes · [repo]
> · Built a workflow engine guaranteeing exactly-once execution across process and machine failures; implemented Raft from scratch for the control plane (passes MIT 6.5840 Labs 2–4).
> · Built a deterministic simulation harness (10k seeded fault schedules nightly) that found 3 correctness bugs invisible to conventional tests; every failure reproducible from a seed integer.
> · Sustains 12k workflow-steps/sec at p99 < 45ms; holds SLO under 10x overload via adaptive concurrency limiting and deadline-aware shedding.

> **incident-lab — Production Outage Reproductions** · Docker, Grafana · [repo]
> · Reproduced 6 major public outages (AWS S3 '17, GitHub '18, Cloudflare '19, Meta '21, Slack '21, Roblox '21) as minimal local systems, each with instrumentation showing the failure and a verified fix.
> · Synthesized the seven recurring mechanisms behind large-scale outages; published, 40k+ reads.

> **overload — Load Shedding & Adaptive Concurrency Lab** · Go, k6 · [repo]
> · Measured goodput collapse under 5x overload across 6 admission-control strategies; naive service delivered 8% of capacity, adaptive limiter delivered 94%.
> · Implemented Vegas-style adaptive concurrency limits that track a changing backend capacity without configuration.

**Notice what these bullets do:** they name a hard thing, quantify it, and imply judgment. No frameworks listed for their own sake. No "responsible for."

### The Interview Answer This Roadmap Buys You

> *"Tell me about the most technically challenging thing you've built."*

You now have a 40-minute answer with: an architecture diagram you can draw from memory · three specific bugs and how you found them · measured performance numbers and where the bottleneck is · a defensible reason for every technology choice · the alternatives you rejected · and what you'd do differently at 100x scale.

**That answer, alone, is worth more than every certification and every course completion certificate in existence.**

---

## 📚 THE COMPLETE LIBRARY

### The Spine (read these, in this order, alongside the levels)

| # | Book | When | Why |
|---|---|---|---|
| 1 | **Designing Data-Intensive Applications** — Kleppmann | Ch. 1 at Level 0, then one chapter/2 weeks | Still the most important backend book. *(Check for the 2nd edition — a substantially updated version has been in early release.)* |
| 2 | **Operating Systems: Three Easy Pieces** — Arpaci-Dusseau *(free)* | Level 0 | 🆕 The OS foundation v2 skipped |
| 3 | **Computer Systems: A Programmer's Perspective** — Bryant & O'Hallaron | Level 0/C, reference | 🆕 Ch. 6 (memory) and 9 (VM) are essential |
| 4 | **A Philosophy of Software Design** — Ousterhout | Level A | 🆕 Short, sharp, better than most of *Clean Code* |
| 5 | **Clean Architecture** — Martin | Level A | Boundaries and dependency rules |
| 6 | **Design Patterns (GoF)** + **Head First Design Patterns** | Level A, as reference | Read to recognize, not memorize |
| 7 | **Learning Domain-Driven Design** — Khononov | Level A | 🆕 Better entry point than Evans |
| 8 | **Database Internals** — Petrov | Level 2 | Deeper than DDIA on storage |
| 9 | **PostgreSQL 14 Internals** — Rogov *(free)* | Level 2 | 🆕 Outstanding and largely unknown |
| 10 | **Unit Testing: Principles, Practices & Patterns** — Khorikov | Level D | 🆕 The testing book |
| 11 | **Release It! (2nd ed.)** — Nygard | Level 4 | 🆕 **The source of circuit breaker/bulkhead. v2's omission of this was a real gap.** |
| 12 | **Systems Performance (2nd ed.)** — Gregg | Level E | 🆕 The performance reference |
| 13 | **Site Reliability Engineering** + **The SRE Workbook** *(free)* | Level 4 | Ch. 3, 4, 6, 21, 22 + Workbook Ch. 5 |
| 14 | **Observability Engineering** — Majors et al. | Level 4 | 🆕 The modern observability reference |
| 15 | **Building Microservices (2nd ed.)** + **Monolith to Microservices** — Newman | Level 5 | Decomposition, honestly |
| 16 | **Software Architecture: The Hard Parts** — Ford & Richards | Level 5 | Trade-off analysis at architecture scale |
| 17 | **Streaming Systems** — Akidau et al. | Level 3/F | 🆕 Event time, watermarks, windowing |
| 18 | **Fundamentals of Data Engineering** — Reis & Housley | Level F | 🆕 The data platform landscape |
| 19 | **AI Engineering** — Chip Huyen | Level G | 🆕 The systems view of building with models |
| 20 | **Kubernetes in Action (2nd ed.)** — Lukša | Level B | Still the best K8s book |
| 21 | **Working Effectively with Legacy Code** — Feathers | Level A/D | 🆕 The skill you'll use on day one of a real job |
| 22 | **Software Engineering at Google** *(free)* — Winters et al. | Level J | 🆕 How engineering works at scale |
| 23 | **The Staff Engineer's Path** — Tanya Reilly | Level J | 🆕 What comes after senior |
| 24 | **Elements of Programming Interviews** / **Algorithm Design Manual** — Skiena | Level I | Interview prep + real understanding |

### Free Courses That Are Pure Learn-By-Doing 🆕

**v2 listed none of these except 6.824. This is the biggest single upgrade in resources.**

| Course | What you build | Hours |
|---|---|---|
| **MIT 6.5840** Distributed Systems | MapReduce, **Raft**, fault-tolerant sharded KV | 150–250 |
| **CMU 15-445** Database Systems (Pavlo) | Buffer pool, **B+Tree**, query execution, MVCC — inside BusTub | 80–120 |
| **Stanford CS144** Computer Networking | **A working TCP/IP stack that talks to the real internet** | 60–100 |
| **MIT 6.S081** Operating System Engineering | xv6 kernel: syscalls, page tables, COW fork, filesystem | 80–120 |
| **Fly.io Gossip Glomers** | 6 distributed-systems challenges, verified by Maelstrom | 20–40 |
| **Protohackers** | Network protocol challenges against a live grader | 15–30 |
| **Codecrafters** *(paid)* | Build your own Redis / Git / SQLite / Kafka / DNS server / shell | varies |
| **MIT Missing Semester** | Shell, git, debugging, tooling — the stuff nobody teaches | 10 |
| **CMU 15-721** Advanced Database Systems | Modern OLAP internals, vectorization | 40+ |

### Free Reference Sites Worth Bookmarking
`use-the-index-luke.com` · `hpbn.co` · `cosmicpython.com` · `refactoring.guru` · `microservices.io` · `aws.amazon.com/builders-library` · `jepsen.io/analyses` · `k8s.af` · `learntla.com` · `postgrespro.com/community/books/internals` · `sre.google/books` · `google.github.io/eng-practices` · `github.com/danluu/post-mortems` · `neetcode.io` · `levels.fyi`

---

## ✅ THE COMPLETE PROJECT CATALOG

**Legend:** ⭐⭐⭐ flagship (build these) · ⭐⭐ high-value · ⭐ core

### Level 0 — Foundations
- [ ] ⭐⭐ `latency-lab` — measure your machine's real latency ladder, emit a personalized card
- [ ] ⭐⭐⭐ **`c10k-arena`** — 6 concurrency models to 50k connections, incl. io_uring *(FLAGSHIP 1)*
- [ ] ⭐ `minidocker` — a container runtime in 400 lines
- [ ] ⭐⭐ **CS144** — build TCP from scratch; it talks to real servers
- [ ] ⭐ `wire` — REST vs gRPC vs GraphQL, measured on the wire
- [ ] ⭐ `sickbay` — 8 injectable production pathologies + solutions

### Level 1 — Protocols
- [ ] ⭐⭐⭐ **`h2spec-clean`** — HTTP/2 from scratch, 146/146 conformance *(FLAGSHIP 2)*
- [ ] ⭐ `ledger-api` — idempotency, keyset pagination, `If-Match` CAS, proven adversarially
- [ ] ⭐⭐ `fanout-lab` — 4 real-time fan-out architectures, message loss measured
- [ ] ⭐ `n+1-hunter` — GraphQL/REST/gRPC compared + a CI query budget

### Level C — Runtime
- [ ] ⭐ `gc-lab` — GC behavior under 4 allocation profiles
- [ ] ⭐⭐ `syscall-xray` — the true cost of "hello world" in 8 frameworks
- [ ] ⭐ Three source-code tours (Redis, Kubernetes, SQLite)

### Level A — Architecture
- [ ] ⭐⭐ `fitness-functions` — architecture rules enforced by CI, with a rejected PR
- [ ] ⭐⭐ `pattern-archaeology` — 10 patterns found in real production code, cited
- [ ] ⭐ `chaos-payments` — 8 patterns applied deliberately
- [ ] ⭐ `context-map` — bounded contexts for a real domain, incl. where NOT to split
- [ ] ⭐⭐ `race-museum` — 10 concurrency pathologies, deterministically reproduced

### Level 2 — Data
- [ ] ⭐⭐⭐ `crashdb` + **`crashdb-torture`** — a storage engine and the harness that destroys it
- [ ] ⭐⭐⭐ **`pgshift`** — 50M-row migration under live load, zero downtime *(FLAGSHIP 3)*
- [ ] ⭐ `access-pattern-lab` — the same feature on 3 stores, benchmarked
- [ ] ⭐⭐ `isolation-museum` — 5 anomalies × 3 databases × 3 fixes, measured
- [ ] ⭐ `tinysearch` — inverted index + BM25 over 1M documents
- [ ] ⭐⭐ **CMU 15-445 BusTub** — buffer pool, B+Tree, MVCC

### Level D — Correctness
- [ ] ⭐⭐⭐ **`simd`** — deterministic simulation testing, 10k seeds, ≥3 real bugs found *(FLAGSHIP 5)*
- [ ] ⭐⭐⭐ **`elle-lite`** — a consistency checker that finds a real anomaly *(FLAGSHIP 4)*
- [ ] ⭐⭐ Fuzzing campaign — ≥3 bugs found, ideally one in someone else's project
- [ ] ⭐⭐ TLA+ specs of two protocols, with a real design bug found by TLC

### Level B — Operations
- [ ] ⭐ `container-forensics` — OOM, CPU throttling, and zero-drop graceful shutdown
- [ ] ⭐⭐ **A Kubernetes Operator** for Chronos (CRD + controller + webhook)
- [ ] ⭐ `queue-shootout` — 4 brokers, a message-loss matrix
- [ ] ⭐ `redis-patterns` — 7 features with atomicity and fencing proven
- [ ] ⭐ Full CI/CD with metric-triggered automatic rollback + DORA dashboard

### Level 3 — Distributed
- [ ] ⭐⭐⭐ **MIT 6.5840 Labs 1–5** — including your own Raft *(the crown jewel)*
- [ ] ⭐⭐ **Gossip Glomers** 1–5
- [ ] ⭐ `clock-chaos` — clock faults vs leases, and fencing tokens proven
- [ ] ⭐⭐ `outbox-cdc-lab` — dual-write vs outbox vs CDC, crash-tested

### Level 4 + E — Reliability & Performance
- [ ] ⭐⭐ `lb-lab` — 6 LB algorithms + the health-check cascade demo
- [ ] ⭐⭐ `cache-lab` — W-TinyLFU vs LRU under Zipf; stampede and cold-start demos
- [ ] ⭐ `ratelimit` — 5 algorithms + an attack suite + shuffle sharding
- [ ] ⭐⭐ `resilience-kit` — retry amplification and metastable failure, measured and fixed
- [ ] ⭐⭐⭐ **`overload`** — the goodput collapse curves *(FLAGSHIP 6)*
- [ ] ⭐ `queue-theory-lab` — predict p99 at 85% utilization, then verify
- [ ] ⭐ `observability-stack` — trace spanning a 30-day timer; <5 min time-to-root-cause

### Level 5, F, G, H — Architecture, Platform, AI, Security
- [ ] ⭐⭐ `decompose` — the bad split and the good split, both measured
- [ ] ⭐⭐ `ledger` — event-sourced double-entry that sums to zero under chaos
- [ ] ⭐⭐ Multi-tenant Chronos — noisy-neighbor isolation proven, cost per tenant
- [ ] ⭐ `skew-lab` — data skew diagnosed and fixed; CSV vs Parquet measured
- [ ] ⭐ `realtime-analytics` — sub-200ms p99 over 1B rows
- [ ] ⭐⭐⭐ **`llmgw`** — LLM gateway: token limits, semantic cache, cost accounting *(FLAGSHIP 8)*
- [ ] ⭐⭐ `hnsw-from-scratch` — with the recall-vs-latency curve
- [ ] ⭐⭐ `authlab` — auth service + the attack suite that breaks the vulnerable branch
- [ ] ⭐ `vulnlab` — 10 vulnerabilities, 10 exploits, 10 fixes, 10 detections
- [ ] ⭐ `gdpr-ready` — crypto-shredding + verified deletion across 5 stores

### Level 6 — Synthesis
- [ ] ⭐⭐⭐ **`incident-lab`** — 6+ famous outages reproduced and fixed *(FLAGSHIP 7)*
- [ ] ⭐⭐ 20 canonical system design documents
- [ ] ⭐⭐ 22 paper one-pagers
- [ ] ⭐⭐⭐ **Chronos C9** — the full design doc, the teardown post, the hosted demo

---

## 🎓 THE FINAL READINESS CHECKLIST

### Can you build it?
- [ ] A storage engine that survives 1,000 random kills with zero data loss
- [ ] Raft, from the paper, passing 100 consecutive test runs with `-race`
- [ ] An HTTP/2 server that passes the full conformance suite
- [ ] A simulation harness that finds bugs your test suite can't
- [ ] A service that holds its SLO at 10x overload
- [ ] A schema migration on 50M rows with zero downtime

### Can you explain it?
- [ ] Raft's Figure 8, at a whiteboard, in 5 minutes
- [ ] Why `W + R > N` doesn't guarantee you read the latest write
- [ ] The difference between exactly-once delivery and exactly-once processing
- [ ] What happens between `kubectl apply` and a running pod — 15+ steps
- [ ] Write skew, with an example that isn't the doctors
- [ ] Why p99 latency goes vertical at 90% utilization
- [ ] What a metastable failure is and how to get out of one
- [ ] Deterministic simulation testing, to a skeptical manager, in 90 seconds
- [ ] Why you'd choose a modular monolith — and then why you wouldn't

### Can you diagnose it?
- [ ] Root-cause a sabotaged service in under 45 minutes, with evidence
- [ ] Read a flame graph in 10 seconds and say what you'd fix
- [ ] Given "p99 is 3s, CPU is 8%", name three causes and the command that distinguishes them
- [ ] Given a bad query plan, say why the planner chose it
- [ ] Given growing consumer lag, name six causes and the metric for each

### Can you interview?
- [ ] 280+ DSA problems, ≥70% solved unaided in 25 minutes
- [ ] A random Medium, narrated, in 25 minutes, on video, repeatedly
- [ ] 20 system designs, 45 minutes each, hitting the rubric
- [ ] 14 behavioral stories, ≤90s each, quantified, in first person
- [ ] 20+ mock interviews completed
- [ ] The Final Gauntlet passed

### Do they know you exist?
- [ ] 6 pinned repos, each with a diagram and a headline number
- [ ] 8+ technical posts published
- [ ] 5+ merged OSS PRs
- [ ] One talk given
- [ ] A resume where every bullet has a number

---

## 📌 What Changed From v2 — the honest changelog

**What v2 got right and v3 keeps:** the BFS/parallel-levels structure · DDIA as the spine with a chapter map · the design-patterns and DevOps levels · the "why it matters" framing on every topic · most of the article curation (which was genuinely good) · the papers table · the blogs list.

**What was wrong and is fixed:**

| Problem in v2 | Fix in v3 |
|---|---|
| **No algorithms track** — completing v2 would still fail a phone screen | Level I, run daily from week 1: 280 problems by pattern, spaced repetition, 20 mocks |
| **No behavioral track** — ~50% of Amazon's loop | Level I.2: 14-story bank in STAR-L, videoed, mapped to LPs |
| Generic projects (task manager, URL shortener, blog, whiteboard) | Every project replaced or sharpened; a uniqueness rubric; 8 flagships that score ≥8/10 |
| Projects with no definition of done | **📈 Exit Criteria with numbers on every project** |
| Article-first learning | **🔥 The Wall** — every topic opens with a failure you must reproduce first |
| No problem→discovery chains | **⛓ Problem Chains** throughout, exactly as you asked |
| 30 disconnected projects, no narrative | **Chronos** — one spine system, 10 milestones, one deep answer for interviews |
| No testing/correctness content | **Level D** — property testing, fuzzing, **deterministic simulation testing**, Jepsen-style checking, TLA+ |
| No performance methodology | **Level E** — profiling, queueing theory, coordinated omission, load shedding, goodput |
| No language/runtime depth | **Level C** — GC, memory model, escape analysis, profilers, source-reading |
| No cloud/data platform | **Level F** — AWS primitives, S3, Spark, Parquet, Iceberg, OLAP, cost engineering |
| No AI/ML systems (in 2026) | **Level G** — inference serving, token economics, vector search, RAG/agent infra |
| Thin security, no privacy/compliance | **Level H** expanded — attack-your-own-system, supply chain, GDPR, crypto-shredding |
| No senior-craft content | **Level J** — design docs, ADRs, code review, OSS, on-call, postmortems, writing |
| Missing the best free hands-on courses | CMU 15-445, CS144, 6.S081, Gossip Glomers, Protohackers, Codecrafters |
| Missing foundational books | OSTEP, CS:APP, **Release It!**, A Philosophy of Software Design, Khorikov, Streaming Systems |
| No assessment mechanism | Exit exams per level, the Three Proofs, the Final Gauntlet |
| Timeline off by ~4x | Honest 1,450–2,150 hours across three named paths |
| Citation errors | Fixed: "How Does a Relational Database Work?" is **Christophe Kalenzaga**; "Blocking I/O, Nonblocking I/O, And Epoll" is **Evan Klitzke**; *Kubernetes: Up and Running* is a **book** by Burns/Beda/Hightower; Discord's posts are "How Discord Stores **Billions**/**Trillions** of Messages"; MIT 6.824 is now **6.5840** |
| Nothing genuinely one-of-a-kind | **Incident Archaeology** — rebuild 10 famous outages, find the seven recurring mechanisms |

---

## 🏁 Closing

Three things determine whether this works:

**1. You must actually reproduce the failures.** The Walls are not flavor text. Reading "cache stampedes cause outages" produces a fact you'll forget. Watching your own database fall over because 10,000 clients hit an expired key at once produces an instinct you'll have for twenty years. Every single 🔥 in this document is there because that specific failure is worth having felt.

**2. You must run all three tracks at once.** Depth without the interview track means you never get to show anyone the depth. The interview track without depth gets you hired at a level you'll be stuck at. Craft without either is empty. It is genuinely harder to run three tracks than one, and it is the reason most people who "study systems for a year" don't convert it into an offer.

**3. You must ship publicly.** The gap between "I understand distributed systems" and "here is my Raft implementation, my simulation harness that found three bugs in it, and my write-up of what surprised me" is the entire difference between a candidate and a hire.

This document is roughly 1,500–2,100 hours of work. That is not a small thing, and it is worth being clear-eyed about it: it is one to two years of consistent effort. But the output is not "a person who has finished a roadmap." The output is an engineer who has built a consensus algorithm, written a storage engine that survives being killed a thousand times, found real bugs with a simulation harness, reproduced the outages that took down S3 and GitHub, and can explain any of it at a whiteboard from memory.

There are not many of those. That's the point.

---

*This roadmap is comprehensive but not exhaustive. Distributed systems and software architecture are lifetimes of study. The goal is not to know everything — it's to have built the reflex of **reproduce, instrument, hypothesize, measure, write** so thoroughly that you can learn any new system faster than the people who built it can explain it to you.*

**Now go break something on purpose.**
