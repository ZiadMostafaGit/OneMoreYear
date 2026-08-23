# 🗺️ The Absolute Complete Backend & Distributed Systems Roadmap — SWARM Edition

## From "Django/DRF backend engineer" → the engineer who gets handed the hardest system in the company

> Same engine as before — Five Laws, the six-step Learning Loop, exit criteria on every project, exit exams per level — with the spine swapped to **SWARM**: a peer-to-peer distributed compute mesh where every node is simultaneously client and server. This is the complete topic coverage (replication, sharding, consistent hashing, consensus, caching, queues, the full system-design canon), sourced against the books you already own — *System Design Interview* Vol 1 & 2 (Alex Xu) and *Designing Data-Intensive Applications* v2 (Kleppmann) — with DSA practice woven into every level, not deferred to the end.
>
> **DSA integration note:** the daily grinding itself still runs through your `dsa-professor`/`dsa-mastery-reference`/`mock-interviewer` skills — that machinery already exists and shouldn't be duplicated. What's new here is that **each level names the DSA patterns that its systems work naturally reinforces**, so your interview prep and your systems depth compound instead of running as two disconnected tracks.

---

## I — The Five Laws (unchanged)

1. **Failure First** — every topic opens with a 🔥 Wall, a system you break before you're told why.
2. **Measure Everything** — every project ships 📈 numeric exit criteria.
3. **Write It Down** — every flagship ships a design doc or teardown.
4. **Ship Publicly** — its own repo, a real README, a working `make demo`.
5. **Review on a Schedule** — a spaced-repetition deck, 15 min/day, cards you wrote yourself.

## II — The Learning Loop (unchanged)

```
🔥 BREAK → 🔎 DIAGNOSE → 📖 THEORY → 🛠 REBUILD → 📈 MEASURE → ✍️ WRITE
```

## III — Two Tracks

```
TRACK 1 — DEPTH (this document)              Levels 0–6. ~85% of time.
TRACK 2 — DSA & INTERVIEW (your existing skills)  Daily, routed per-level below. ~15% of time.
```

---

## IV — The Spine Project: SWARM

**What it is:** a peer-to-peer distributed compute mesh. Any machine can join as a node; every node is simultaneously a **client** (submits jobs for the mesh to run) and a **server** (executes jobs submitted by others). There's no central cloud owner — the network itself cooperatively decides where a job runs, where its data lives, how it's replicated, and what happens when the node running it disappears mid-execution.

**The one-line pitch:** *"AWS Lambda, but the compute is contributed by the network itself, not owned by anyone — I built the scheduler, the storage layer, and the trust model that make that safe."*

**Why this is a stronger spine than a workflow engine, specifically:** every hard problem is *structurally forced*, not optional — there's no central server to fall back on if you get lazy about consensus, no fixed "the database" to lean on if you get lazy about sharding, and — the genuinely rare part — **you have to solve the "can I trust a stranger's computer to have actually run my code correctly" problem**, which almost no portfolio project ever touches and which pulls in real distributed-systems theory (redundant execution, majority-vote verification) that most backend engineers never encounter hands-on.

### What SWARM needs, and what each requirement forces you to master

| SWARM needs… | …forces you to master | Book chapter |
|---|---|---|
| Peer discovery, no central directory | Gossip protocols, SWIM membership, NAT traversal | DDIA Ch. 8 (partial failure) |
| "Who owns this job/data?" with no fixed servers | Consistent hashing / a DHT (Chord-style) | Xu Vol 1 Ch. 5 |
| Coordinating a mesh region without one server | **Raft**, leader election, replicated state machines | DDIA Ch. 9 |
| Trusting a stranger's execution result | Redundant execution + majority-vote verification | DDIA Ch. 9 (Byzantine section) |
| Code/data persisting somewhere on the mesh | Content-addressed storage, your own storage engine | DDIA Ch. 3 |
| A node vanishing mid-job | Failure detection, leases, exactly-once-ish re-execution | DDIA Ch. 8–9 |
| Untrusted code execution safety | Sandboxing (WASM/Firecracker-style isolation) | — (systems-specific) |
| An oversubscribed mesh | Load-aware placement, backpressure, admission control | Xu Vol 1 Ch. 1, 4 |
| Multiple users sharing the mesh | Multi-tenancy, per-peer quotas | Xu Vol 2 (multi-tenant chapters) |
| GPU peers serving inference | Your AI-infra branch, folded in as a job *type* | — |

### The 10 SWARM Milestones

| Milestone | Level | What you build | The invariant you must prove |
|---|---|---|---|
| **S0** | 0 | Single-node sandboxed job executor (WASM/subprocess isolation) + local durable task log | Survives `kill -9` mid-job with no corrupted state |
| **S1** | 1 | Peer wire protocol: job submission, result return, peer discovery, NAT traversal | Two peers behind different NATs can discover and exchange jobs |
| **S2** | A | Hexagonal core: scheduling logic has zero knowledge of network/storage/sandbox specifics | Swap the sandbox implementation with a one-line change |
| **S3** | 2 | Content-addressed storage for code/data artifacts — a mini IPFS on your own storage engine | Identical content always resolves to the identical address, verified by hash |
| **S4** | D | Deterministic simulation of the mesh under churn, partitions, and lying/malicious nodes | 10,000 seeded fault runs, zero invariant violations |
| **S5** | 3 | Consistent-hashing/DHT job-ownership routing + **Raft-coordinated mesh regions** | Kill a region's coordinator mid-commit; no job assignment is lost or duplicated |
| **S6** | 4/E | Load-aware placement, backpressure under an oversubscribed mesh | Goodput held under 5x offered-load overload via shedding, not collapse |
| **S7** | 5 | Multi-tenancy + redundant execution with majority-vote result verification | A single lying node cannot corrupt a job's accepted result |
| **S8** | G | GPU peers advertise inference capability; the mesh becomes a distributed LLM-serving marketplace | A job requesting inference is routed to a capable peer and billed correctly |
| **S9** | 6 | Full design doc + comparison against BOINC/IPFS/Golem/Ray + public demo | A stranger understands the architecture in 15 minutes |

---

## V — The 8 Flagship Projects

Each ≥8/10 on the Uniqueness Rubric (non-obvious premise, novel measurement, real correctness invariant, demoable in 60s, buildable solo in ≤3 weeks, a real "and then it broke" story, explainable in 2 sentences).

### 1. `c10k-arena` — six concurrency models, benchmarked to 50k connections (feeds SWARM S0/S1's networking layer)
Process-per-conn, thread-per-conn, bounded pool, epoll, io_uring, goroutines — built and benchmarked head to head.
📈 **Exit:** p99-latency and RSS charts across all six · io_uring shows measurably fewer syscalls/message than epoll · a named knee per model with the causing resource identified.

### 2. `dht-clean` — a from-scratch Chord-style DHT passing a real churn-conformance suite
Consistent hashing, finger tables, join/leave protocols, and correct key ownership under continuous node churn.
📈 **Exit:** correct key lookup under 30% simultaneous node churn · O(log N) hop count verified empirically at 3 network sizes · a chart of lookup latency vs. mesh size.

### 3. `simd-swarm` — deterministic simulation testing for the mesh (FoundationDB-style)
Simulated clock, network (with asymmetric partitions), disk, and scheduler, driven by 10,000+ nightly seeds, including **lying/malicious nodes** as an injectable fault type.
📈 **Exit:** 10,000+ seeds clean nightly · **≥3 real bugs found and documented with seed + trace** · a lying-node scenario caught by majority-vote verification, proven with a seed.

### 4. `verify-lite` — the redundant-execution/majority-vote trust layer
The specific "can I trust a stranger's computer" problem: jobs run on N peers, results compared, majority accepted, minority nodes flagged/penalized.
📈 **Exit:** a single lying node cannot corrupt an accepted result at N≥3 · measured overhead of redundant execution vs. single-execution trust · a reputation-scoring scheme that reduces redundancy needed for previously-reliable peers, measured.

### 5. `overload` — goodput collapse curves under an oversubscribed mesh
Offered load driven to 3–5x mesh capacity; naive vs. bounded-queue vs. deadline-aware-drop vs. adaptive-admission compared.
📈 **Exit:** the collapse curve and the graceful curve on one chart · "naive delivers X%, adaptive delivers Y% at 3x overload," quantified.

### 6. `pgshift` — zero-downtime, 50M-row schema migration under live load (the mesh's own metadata store)
Applied to SWARM's peer-registry/job-metadata schema instead of a generic table.
📈 **Exit:** zero errors, p99 degradation under 20%, full window on video · resumable backfill proven by a mid-run kill and restart.

### 7. `incident-lab` — 10 famous outages, reproduced and fixed locally
S3 2017, GitHub 2018, Cloudflare 2019 (×2), Meta 2021, Slack 2021, Roblox 2021, Knight Capital, GitLab 2017, cache stampede.
📈 **Exit:** 6 of 10 reproduced with before/after · a synthesis essay on the seven recurring failure patterns.

### 8. `llm-peer` — a GPU peer advertising and serving inference on the mesh
Token-aware rate limiting, semantic/prefix caching, streaming with cancellation, per-tenant cost accounting — wired in as a SWARM job type (S8), not a bolt-on gateway.
📈 **Exit:** measured cost reduction from caching ≥40% · a job requesting inference correctly routed, executed, and billed · killing the executing peer mid-inference correctly re-routes without double-billing the requester.
## VI — The Level Map

| Level | Name | SWARM milestone | Budget | DSA companion (patterns this level's work naturally reinforces) |
|---|---|---|---|---|
| **0** | Machine, OS & Runtime Foundations | S0 | 100–140h | Arrays/two-pointers, hashing, linked lists (from building the job log/sandbox) |
| **1** | Protocols & Peer Communication | S1 | 90–120h | Graphs (BFS/DFS for peer discovery), design-style problems (rate limiter, LRU) |
| **A** | Code Architecture & Patterns | S2 | 60–90h | Backtracking, tries (from clean scheduling-core design) |
| **2** | Databases & Storage Engines (15-445) | S3 | 140–180h | Trees/BSTs, heaps/top-K (from B-trees, buffer-pool eviction) |
| **D** | Testing & Correctness (DST/TLA+) | S4 | 70–100h | Backtracking/state-space search (maps directly onto model checking) |
| **3** | Distributed Systems Core (6.5840) | S5 | 180–260h | Union-find, graphs (DHT/consistent hashing), greedy+intervals |
| **4/E** | Reliability & Performance | S6 | 90–120h | Heaps (priority scheduling), sliding window (rate limiting) |
| **5** | Advanced Architecture & Multi-Tenancy | S7 | 70–100h | DP (optimal redundancy/cost tradeoffs), design problems |
| **G** | AI Infrastructure | S8 | 60–90h | — (systems-integration heavy, less DSA-dense) |
| **6** | Synthesis: System Design + Incidents | S9 | 80–120h | Full mock system-design loops |

**Total: ~940–1,320 hours** of depth work, DSA running in parallel throughout via your existing tools per the companion column above.

---

## VII — The Curriculum

---

### LEVEL 0 — Machine, OS & Runtime Foundations

> **Budget:** 100–140h · **SWARM milestone:** S0

#### 0.1 — Memory Hierarchy & Cache Behavior

🔥 **THE WALL:** two matrix-sum functions (row-major vs column-major), identical Big-O, 5–60x latency gap. Then a false-sharing reproduction on a padded vs unpadded two-counter struct.

📖 **Theory:** the full latency ladder, cache lines, spatial/temporal locality, MESI and false sharing, TLB/page faults, NUMA, the roofline model.

📄 **Source:** Drepper's "What Every Programmer Should Know About Memory" · CS:APP Ch. 6.

🛠 **PROJECT — `latency-lab`:** derive your own machine's cache sizes from a working-set sweep; produce a personal latency card.

📈 **Exit:** derived cache sizes match `lscpu` within one power of two · false-sharing fix ≥3x throughput improvement with `perf c2c` evidence.

**DSA companion:** two-pointer/sliding-window problems (the cache-locality intuition directly explains why these patterns are fast in practice, not just in Big-O).

#### 0.2 — Concurrency Models & C10K

🔥 **THE WALL:** a dumb TCP echo server dies at 10,000 concurrent connections — diagnose *how* (RAM exhaustion vs thread-creation failure vs scheduler thrashing).

📖 **Theory:** process/thread/coroutine cost, the scheduler, `select→poll→epoll→io_uring`, readiness vs completion models, Go's M:N scheduling, structured concurrency.

📄 **Source:** OSTEP Ch. 4–10, 25–33 · "The C10K Problem" (Kegel).

🛠 **FLAGSHIP #1 — `c10k-arena`:** six concurrency models, benchmarked to 50k connections — this becomes SWARM S0's networking substrate directly.

📈 **Exit:** all six pass identical correctness tests · six-line p99-vs-connections chart · io_uring's syscall reduction quantified against epoll.

**DSA companion:** linked-list and queue-based problems (directly maps to implementing your own bounded task queues for the job executor).

#### 0.3 — Sandboxed Execution & the Local Job Log (SWARM S0)

🔥 **THE WALL:** run untrusted code naively (raw `subprocess`/`exec`) and watch it read your filesystem, exhaust memory, or spin the CPU forever with no limit.

📖 **Theory:** namespaces/cgroups (Linux containment primitives), WASM as a sandboxing target (why WASM specifically is attractive for untrusted third-party code — deterministic, resource-limited, no raw syscall access by default), resource limiting (cgroup memory/CPU caps), and a durable local append-log for job state (directly reusing your `crashdb`-style storage-engine skills from Level 2, built early here as a minimal version).

🛠 **PROJECT — SWARM S0:** a single-node sandboxed job executor (WASM runtime, e.g., Wasmtime/Wasmer, or subprocess isolation with cgroups as a fallback) plus a local durable append-only task log.

📈 **Exit Criteria:** a malicious job attempting filesystem access outside its sandbox is blocked and logged · a memory-bomb job is killed at its configured limit while the host stays healthy · `kill -9` mid-job leaves the local log in a recoverable, non-corrupted state, verified over 500 kill cycles.

#### 0.4 — Linux as a Debugger

🔥 **THE WALL — Four Sick Servers:** memory leak, FD leak, lock contention, runaway syscall loop — diagnosed with only Linux tooling, under 10 minutes each.

📖 **Theory:** `strace`, `perf`, flame graphs, the USE method, off-CPU analysis.

📄 **Source:** "Linux Performance Analysis in 60,000 Milliseconds" (Gregg) · "Systems Performance" 2nd ed.

🛠 **PROJECT — `sickbay`:** 8 injectable pathologies with evidence-based solutions.

📈 **Exit:** median diagnosis time under 10 minutes on a shuffled re-run.

---

### LEVEL 1 — Protocols & Peer Communication

> **Budget:** 90–120h · **SWARM milestone:** S1

#### 1.1 — Binary Protocols: gRPC, Protobuf, HTTP/2

🔥 **THE WALL — The Field-Number Massacre:** retype/reuse a deleted protobuf field number; deserialize old bytes with the new schema and watch data silently corrupt.

📖 **Theory:** the protobuf wire format (hand-decode one message from hex), schema-evolution safety rules, HTTP/2 framing/HPACK/multiplexing, gRPC's deadline propagation and retry/hedging config.

📄 **Source:** protobuf.dev encoding spec · Xu Vol 1 Ch. 1 (basics of communication design).

🛠 **FLAGSHIP #2 — could be substituted here, but the primary protocol project is peer-to-peer specific below; `h2spec-clean` remains available as an optional secondary if you want the pure-conformance flex project.**

**DSA companion:** hashing and encoding problems (bit manipulation, serialize/deserialize-style LeetCode problems map directly onto hand-decoding protobuf).

#### 1.2 — Peer Discovery, Gossip & NAT Traversal (SWARM S1's core)

🔥 **THE WALL:** two SWARM nodes, each behind a different home-router NAT, cannot find each other at all with a naive "just connect to this IP" approach — the actual, real-world reason peer-to-peer software needs discovery infrastructure in the first place.

📖 **Theory:** gossip/epidemic protocols (SWIM specifically — how nodes learn "who else is in the mesh" without a directory), NAT traversal techniques (STUN-style hole punching, relay fallback), peer liveness/failure detection via heartbeats and phi-accrual-style detectors, bootstrapping a mesh from a small seed-peer list.

📄 **Source:** the SWIM paper ("SWIM: Scalable Weakly-consistent Infection-style Process Group Membership Protocol") · DDIA Ch. 8 (partial failure, failure detectors).

🛠 **PROJECT — SWARM S1:** the peer wire protocol — job submission format, result-return format, SWIM-based peer discovery, and NAT traversal via a lightweight relay/hole-punching scheme.

📈 **Exit Criteria:** two peers behind different NATs successfully discover each other and exchange a job/result pair · a peer joining a 20-node mesh is known to all other peers within a bounded number of gossip rounds, measured · a peer going silent is detected as failed within a bounded time window, with a false-positive rate measured under network jitter.

**DSA companion:** graph BFS/DFS (gossip propagation IS breadth-first traversal across a graph — this is one of the cleanest DSA-to-systems mappings in the whole roadmap; do LeetCode's graph-traversal set alongside this section specifically).

#### 1.3 — Real-Time Fan-Out (kept from general backend canon — useful transferable skill even outside SWARM)

🔥 **THE WALL:** two service instances behind a load balancer, a message sent from one never reaching a client on the other.

📖 **Theory:** WebSocket/SSE tradeoffs, fan-out architectures, presence, backpressure on a slow consumer, reconnect storms and jitter.

📄 **Source:** Xu Vol 2 (chat-system chapters) · Discord's "How Discord Stores Billions/Trillions of Messages."

🛠 **PROJECT — `notify-fanout`:** a standalone real-time fan-out system (kept as a portfolio piece independent of SWARM, since it's a directly hireable, common interview topic — Xu Vol 2 dedicates real space to exactly this).

📈 **Exit:** messages-lost-during-rolling-deploy driven to zero · reconnect-storm latency with/without jitter.

---

### LEVEL A — Code Architecture & Patterns

> **Budget:** 60–90h · **SWARM milestone:** S2

🔥 **THE WALL:** time yourself adding a feature, unit-testing a core calculation, and changing a rule in a deliberately tangled codebase; refactor; re-time.

📖 **Theory:** SOLID reframed by the pain each principle prevents, hexagonal/ports-and-adapters architecture, the "wrong abstraction is worse than duplication" counterweight, structured concurrency, bounded queues as a mandatory design rule.

📄 **Source:** "A Philosophy of Software Design" (Ousterhout).

🛠 **PROJECT — SWARM S2:** restructure the scheduling core into a hexagonal design with zero imports from network/storage/sandbox specifics.

📈 **Exit:** swapping the sandbox implementation (WASM ↔ subprocess) is a one-line change · full scheduler test suite runs in <2s with no real network, disk, or sandbox involved.

**DSA companion:** backtracking and trie problems (clean recursive scheduling-decision code shares real structural DNA with backtracking search — do this section's problems alongside the scheduler refactor).

---

### LEVEL 2 — Databases & Storage Engines

> **CMU 15-445 lives here in full — 80–120h of the budget.** Grounded in SWARM's content-addressed storage requirement instead of a generic table.
>
> **Budget:** 140–180h · **SWARM milestone:** S3

#### 2.1 — Storage Engines: How Bytes Land on Disk

🔥 **THE WALL — The Torn Write:** an append-only KV store, `kill -9`'d mid-write 500 times — torn records, garbage-that-parses-as-valid, an index pointing past EOF.

📖 **Theory:** B-Trees vs LSM-Trees and the RUM conjecture, WAL/ARIES/group commit, MVCC, the buffer pool.

📄 **Source:** DDIA Ch. 3 · CMU 15-445 lectures 3–7.

🛠 **PROJECT — `crashdb` + torture harness:** append log → CRC framing → compaction → Bloom filter → WAL+recovery, `kill -9`'d and syscall-fault-injected via `LD_PRELOAD`.

📈 **Exit:** 1,000 random-kill cycles, zero invariant violations · torn-write injection caught 100% of the time by checksums.

**DSA companion:** trees/BSTs and heaps (B+Tree structure and buffer-pool LRU-K eviction are literally these data structures under production constraints — do LeetCode's tree and heap sets here).

#### 2.2 — Content-Addressed Storage: SWARM's Mini-IPFS (S3)

🔥 **THE WALL:** two peers each store "the same" piece of code, but under a naive filename-based storage scheme they diverge silently (one has a stale version) with no way to detect it.

📖 **Theory:** content-addressing (an artifact's storage key is a cryptographic hash of its content, not an arbitrary name — meaning identical content always produces an identical address, and any tampering is instantly detectable), Merkle-DAG structures for referencing larger composite artifacts, garbage collection of unreferenced content, and how this connects back to 2.1's storage-engine work (the content store sits on your own engine, not a generic filesystem).

📄 **Source:** the IPFS whitepaper (for the content-addressing model specifically) · DDIA Ch. 3 (as the storage-engine foundation underneath it).

🛠 **PROJECT — SWARM S3:** content-addressed storage for job code/data artifacts on top of your `crashdb` engine.

📈 **Exit Criteria:** identical content always resolves to the identical address, verified by hash comparison across 10,000 random artifacts · a tampered artifact is detected on retrieval, not silently served · garbage collection correctly reclaims space from unreferenced artifacts without touching referenced ones, proven under concurrent access.

#### 2.3 — PostgreSQL to a Professional Standard

🔥 **THE WALL — The Four Disasters:** an unused index, a connection storm that reduces throughput, a vacuum death spiral, a lock pileup from a hot-table `ALTER`.

📖 **Theory:** `EXPLAIN (ANALYZE, BUFFERS)`, index types, composite index leftmost-prefix rule, `SKIP LOCKED`, connection pooling modes, partitioning.

📄 **Source:** "Use The Index, Luke!" (Winand, free) · DDIA Ch. 3.

🛠 **FLAGSHIP #6 — `pgshift`:** zero-downtime schema migration on SWARM's peer-registry/job-metadata table under live load.

📈 **Exit:** zero errors, p99 degradation under 20%, live-Grafana-proven · resumable backfill, killed-and-restarted mid-run.

#### 2.4 — Replication, Sharding & Consistent Hashing

🔥 **THE WALL:** a leader-follower replica lags; a read against it returns stale data immediately after a write to the leader.

📖 **Theory:** sync/async/semi-sync replication, read-your-writes/monotonic-reads/consistent-prefix-reads, leaderless/quorum replication (`W+R>N` and why it doesn't fully guarantee freshness), sharding strategies, and **consistent hashing built from first principles** — this is also SWARM's actual job-ownership mechanism, not a separate exercise.

📄 **Source:** DDIA Ch. 5–6 · Xu Vol 1 Ch. 5 (consistent hashing, dedicated chapter).

🛠 **PROJECT — `replica-lab`:** the four read-your-writes fixes, measured, plus a failover with measured RPO.

📈 **Exit:** p99 read/write latency and staleness bound per fix · measured data loss on unplanned failover.

**DSA companion:** union-find and modular-arithmetic-flavored problems (consistent hashing's ring structure and rebalancing logic connect directly to union-find-style problems — do this alongside the DHT work in Level 3).

---

### LEVEL D — Testing, Correctness & Verification

> **Budget:** 70–100h · **SWARM milestone:** S4

#### D.1–D.2 — Property Testing & Fuzzing

🔥 **THE WALL:** mutation-test an existing project — 85% line coverage, under 50% mutation score.

📖 **Theory:** fakes over mocks, model-based property testing, stateful property testing, differential fuzzing.

🛠 **PROJECT:** fuzz SWARM's peer wire protocol parser and content-addressed storage's artifact parser; find ≥3 real bugs with shrunk minimal reproducers.

#### D.3 — Deterministic Simulation Testing (the crown jewel)

🔥 **THE WALL:** SWARM passes all its unit tests. What happens if the network partitions asymmetrically, a disk `EIO`s, a clock jumps, and **a node starts lying about job results** — all at once? You cannot test that combination by hand.

📖 **Theory:** replacing every nondeterminism source with a simulated implementation under one seeded PRNG, and — new relative to a generic workflow engine — **modeling a Byzantine-lite fault type (a node that returns plausible-but-wrong results)** as a first-class injectable fault, since SWARM's trust problem doesn't exist in most DST examples.

📄 **Source:** "Testing Distributed Systems w/ Deterministic Simulation" (Will Wilson, Strange Loop 2014) · FoundationDB's SIGMOD 2021 paper.

🛠 **FLAGSHIP #3 — `simd-swarm`:** `SimClock`, `SimNetwork` (with asymmetric partitions), `SimDisk`, `SimScheduler`, and a `LyingNode` fault type, run across 10,000+ seeds nightly with an invariant checker (no job double-assigned, every job eventually completes or is explicitly failed, content-store integrity holds, majority-vote verification catches injected lies).

📈 **Exit:** 10,000+ seeds clean nightly · **≥3 real bugs found and documented with seed + trace** · a lying-node scenario specifically caught by the verification layer, with the seed that exposes it if the layer is disabled.

**DSA companion:** state-space search / backtracking (model checking and DST are structurally a search over possible execution interleavings — LeetCode's harder backtracking problems build the same "explore a state space systematically" muscle).

#### D.4 — TLA+ and the Trust Invariant

🔥 **THE WALL:** spec SWARM's majority-vote verification protocol in TLA+ — model-check it and find the edge case (e.g., exactly at the vote threshold with a tied result) where it doesn't behave as assumed.

📄 **Source:** learntla.com (Hillel Wayne, free).

📈 **Exit:** the spec model-checks clean for the safety invariant "a minority of lying nodes can never cause an incorrect result to be accepted" · at least one real design bug found by TLC and fixed.

---

### LEVEL 3 — Distributed Systems Core

> **MIT 6.5840 — the anchor of the entire roadmap. 80–150h of this level's budget is Lab 3 (Raft) alone.**
>
> **Budget:** 180–260h · **SWARM milestone:** S5

#### 3.1 — The Eight Fallacies, Made Concrete

🔥 **THE WALL:** using `tc netem`/`iptables`, demonstrate all eight, especially the asymmetric partition (A reaches B, B cannot reach A) — the case every naive SWARM peer-liveness check gets wrong.

📖 **Theory:** partial failure, FLP impossibility, CAP stated correctly, PACELC, retry amplification.

📄 **Source:** DDIA Ch. 8 · Xu Vol 1 Ch. 1.

#### 3.2 — Consensus & DHT Routing: Implement Raft and Chord, For Real

**MIT 6.5840** (`pdos.csail.mit.edu/6.824/`), Labs 1–5, no shortcuts.

| Lab | Builds | Hours |
|---|---|---|
| 1 | Fault-tolerant MapReduce | 15–25 |
| 2 | KV server, at-most-once RPC | 10–15 |
| 3 | **Raft** | **60–120** |
| 4 | Fault-tolerant KV atop your Raft | 25–40 |
| 5 | Sharded KV with reconfiguration | 30–50 |

📖 **Theory:** Raft in full (the Figure 8 commit-rule subtlety especially), quorum intersection, and — SWARM-specific — **Chord's finger-table routing and consistent hashing at scale**, since a DHT is the actual mechanism deciding "which peer owns this job."

📄 **Source:** "In Search of an Understandable Consensus Algorithm (Extended Version)" · the original Chord paper ("Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications") · Xu Vol 1 Ch. 5.

🛠 **FLAGSHIP #2 — `dht-clean`:** a from-scratch Chord-style DHT (finger tables, join/leave, correct key ownership under churn).

📈 **Exit:** correct lookup under 30% simultaneous churn · O(log N) hop count empirically verified · lookup-latency-vs-mesh-size chart.

🛠 **SWARM S5:** Raft-coordinated mesh regions on top of the DHT for job-ownership routing.

📈 **Exit:** kill a region's coordinator mid-commit under load; no job assignment is lost or double-assigned · Gossip Glomers 1–5 complete via Maelstrom.

**DSA companion:** union-find (Chord ring/join-leave logic), graph algorithms broadly (Dijkstra/BFS-adjacent thinking underlies routing-table maintenance) — this is the single richest DSA-to-systems overlap section in the roadmap; lean into it hard.

#### 3.3 — Time, Clocks & Fencing

🔥 **THE WALL:** move the clock backward mid-workload — duplicate timestamps, overlapping region-coordinator leases.

📖 **Theory:** monotonic vs wall clocks, Lamport/vector clocks, leases and fencing tokens.

🛠 **PROJECT — `clock-chaos`:** clock faults added to `simd-swarm`; a correctness violation with wall-clock leases, absent with fencing tokens.

---

*(Continued: Level 4/E through 6, plus the SWARM+DSA capstone integration, follow in the next file.)*
### LEVEL 4/E — Reliability & Performance

> **Budget:** 90–120h · **SWARM milestone:** S6

#### 4.1 — Load-Aware Placement & Admission Control

🔥 **THE WALL:** the mesh is driven to 3–5x its aggregate capacity with an open-loop generator — a naive scheduler's *goodput* collapses toward zero, since it keeps accepting jobs it can never finish in time.

📖 **Theory:** Little's Law and queueing basics, the offered-load-vs-goodput curve, bounded queues with an explicit full-queue policy, deadline-aware dropping, adaptive admission (Vegas-style, inferring capacity from observed latency rather than a fixed config number).

📄 **Source:** Xu Vol 1 Ch. 1, 4 (scale estimation and rate limiting fundamentals) · AWS Builders' Library's load-shedding articles.

🛠 **FLAGSHIP #5 — `overload`:** the same collapse-vs-graceful comparison as the general roadmap, applied to SWARM's job-submission path specifically.

📈 **Exit:** the collapse curve and the graceful curve on one chart · "naive delivers X%, adaptive delivers Y% at 3x overload," quantified · the adaptive limiter tracks a *changing* mesh capacity mid-test (simulate several peers leaving).

**DSA companion:** heap/priority-queue problems (job scheduling under load is fundamentally a priority-queue problem — "task scheduler," "meeting rooms," and similar LeetCode problems map directly).

#### 4.2 — Caching & Rate Limiting

🔥 **THE WALL:** cache stampede on hot job-metadata lookups, then a boundary-burst attack on a naive fixed-window rate limiter protecting the mesh's job-submission endpoint.

📖 **Theory:** W-TinyLFU beating LRU, the five rate-limiting algorithms and their exact tradeoffs, per-peer quotas as SWARM's version of multi-tenancy.

📄 **Source:** Xu Vol 1 Ch. 4, 6 (dedicated rate-limiter and cache chapters).

**DSA companion:** sliding-window problems (rate limiting IS a sliding-window algorithm — do LeetCode's sliding-window set here explicitly, it's a near-1:1 mapping).

#### 4.3 — Resilience: Retry Storms & Metastable Failures

🔥 **THE WALL:** a job chain across three peers, each retrying 3x, and one peer merely slow — the 9x load amplification kills it completely; then a metastable failure where removing the trigger doesn't fix the outage.

📖 **Theory:** deadline propagation, exponential backoff with full jitter, circuit breakers (and their honest critique), SLIs/SLOs.

📄 **Source:** DDIA Ch. 8 · AWS Builders' Library.

🛠 **PROJECT — `resilience-kit`:** an adversarial peer simulating slow/flapping/failing/lying behavior, with the retry-amplification story measured and a metastable failure reproduced-then-fixed.

---

### LEVEL 5 — Advanced Architecture: Multi-Tenancy & Trust

> **Budget:** 70–100h · **SWARM milestone:** S7

#### 5.1 — Redundant Execution & Majority-Vote Verification

🔥 **THE WALL:** run the same job on three peers with no verification — inject one lying peer that returns a plausible-but-wrong result. Nothing catches it. This is SWARM's core trust problem, unsolved.

📖 **Theory:** Byzantine-fault-tolerance basics (not full BFT consensus — the practical subset: redundant execution + majority vote is a lighter, more tractable trust model than full BFT, and knowing the distinction is itself valuable), reputation scoring (peers that have been consistently correct need less redundancy over time — an optimization with a real cost/trust tradeoff), and the economics of verification (more redundancy = more trust but more wasted compute).

📄 **Source:** DDIA Ch. 9 (the Byzantine-faults section specifically) · the BOINC project's own credit/verification-system documentation as a real-world precedent.

🛠 **FLAGSHIP #4 — `verify-lite`:** the redundant-execution/majority-vote layer with reputation scoring.

📈 **Exit:** a single lying node cannot corrupt an accepted result at N≥3 replicas · measured compute overhead of redundant execution vs. trusting a single peer · reputation scoring measurably reduces required redundancy for previously-reliable peers, with the tradeoff curve charted (trust built over time vs. redundancy cost saved).

**DSA companion:** DP and greedy problems (the redundancy-vs-cost tradeoff is a genuine optimization problem — "minimum cost to achieve X confidence" has real DP/greedy structure).

#### 5.2 — Multi-Tenancy on the Mesh

🔥 **THE WALL:** one tenant submits jobs at 100x normal volume; every other tenant's jobs starve.

📖 **Theory:** per-tenant quotas, fair queuing/weighted fair queuing, shuffle sharding for blast-radius reduction.

📈 **Exit:** one tenant at 100x load; other tenants' job-completion latency degrades by <10%.

---

### LEVEL G — AI Infrastructure: The Mesh as an Inference Marketplace

> **Budget:** 60–90h · **SWARM milestone:** S8

🔥 **THE WALL — The $18,000 Bill:** a naive LLM-serving job on the mesh — no batching, no caching, one slow peer blocking the requester, a retry loop double-billing.

📖 **Theory:** prefill vs decode and why the asymmetry drives serving design, continuous batching, KV-cache/PagedAttention, prefix caching, token-aware rate limiting — same theory as the general roadmap's AI-infra level, but the integration is different and better: **inference is just another job type the mesh routes**, executed by whichever peer advertises GPU capability.

📄 **Source:** "Efficient Memory Management for Large Language Model Serving with PagedAttention" (SOSP 2023).

🛠 **FLAGSHIP #8 — `llm-peer`:** GPU peers advertise inference capability; the scheduler (from Level 4's placement logic) routes inference jobs to capable peers with token-aware cost accounting and result streaming back through the mesh's normal result-return path.

📈 **Exit:** an inference job is correctly routed only to capability-advertising peers · streaming works end-to-end through the mesh, not just point-to-point · killing the executing peer mid-inference triggers correct re-routing without double-billing the requester · measured cost reduction from prefix caching on repeated system-prompt-shaped requests.

---

### LEVEL 6 — Synthesis

> **Budget:** 80–120h · **SWARM milestone:** S9

#### 6.1 — Incident Archaeology (unchanged from the general canon — universal failure patterns)

**FLAGSHIP #7 — `incident-lab`:** the same 10 outages (S3 2017, GitHub 2018, Cloudflare 2019×2, Meta 2021, Slack 2021, Roblox 2021, Knight Capital, GitLab 2017, cache stampede), reproduced locally with fixes.

📈 **Exit:** 6 of 10 reproduced with working before/after · a synthesis essay naming the seven recurring patterns.

#### 6.2 — System Design Canon (trimmed to 8, cross-referenced to your books)

For each: full design-doc format (Summary, Context, Goals, **Non-Goals**, Proposal, **Alternatives Considered — minimum three**, Risks, Rollout, Operational Impact). Route each through `mock-interviewer`.

1. **A distributed compute/job-scheduling system** — this is SWARM itself; you have the real answer. (Xu Vol 2 has a chapter structurally close to this.)
2. **A distributed cache** — consistent hashing, replication, resharding. (Xu Vol 1 Ch. 5, 6.)
3. **Rate limiter as a service.** (Xu Vol 1 Ch. 4.)
4. **A distributed file/object storage system** — direct extension of SWARM's content-addressed store. (DDIA Ch. 3 as foundation; Xu Vol 2 for the applied design.)
5. **A message queue.** (DDIA Ch. 11; Xu Vol 1 Ch. 11.)
6. **Chat/messaging.** (Xu Vol 2, dedicated chapters.)
7. **An LLM API platform** — token limits, GPU scheduling, streaming, cost attribution. (2026-relevant, not in either book — sourced from the vLLM paper instead.)
8. **A web crawler or search-indexing system** — good general-practice design, tests a different muscle (frontier management, dedup at scale) than the mesh-shaped problems above.

#### 6.3 — The SWARM Teardown (milestone S9)

The capstone: an architecture diagram a stranger understands in 15 minutes · the ≥3 bugs `simd-swarm` found that no test suite would have caught · measured numbers at every milestone (job throughput, p99 scheduling latency, DHT lookup hops, trust-layer overhead) · **an honest comparison against real systems** — BOINC (volunteer computing, decades of production experience with exactly the trust problem you solved), IPFS (content-addressing at scale), Golem/Akash (the closest real analogs to a compute marketplace), and Ray (the closest analog for the scheduling/execution-engine half) — naming where SWARM's design converges with or diverges from each, and why.

---

## VIII — Assessment: The Exit Exams

Same **Three Proofs** as before (Exam, Artifact, Teach-Back), plus **The Mock Loop** (route each level's hardest concepts into a `mock-interviewer` session before moving on). Per-level exit exams (8–9 questions, timed, pass = 7/8) generated on request as you approach the end of each level.

### The Final Gauntlet (before your first real interview loop)

| Day | Challenge | Pass condition |
|---|---|---|
| 1 | Debug a sabotaged SWARM build | Root cause in <45 min with evidence |
| 2 | 2 of the 8 system designs, 45 min each, on video, cross-checked against Xu Vol 1/2's own frameworks | Both hit the design-doc rubric |
| 3 | Teach-back: Raft, consistent hashing/DHT routing, deterministic simulation testing — 10 min each | No notes, correct, with diagrams |
| 4 | A DSA session covering the companion patterns from every level (your `dsa-professor` skill can compile this list) | 80%+ solved unaided |
| 5 | Full review against every rubric above | Honest scoring |

---

## IX — The Honest Timeline

| Level | Hours |
|---|---|
| 0 | 100–140 |
| 1 | 90–120 |
| A | 60–90 |
| 2 | 140–180 |
| D | 70–100 |
| 3 | 180–260 |
| 4/E | 90–120 |
| 5 | 70–100 |
| G | 60–90 |
| 6 | 80–120 |
| **Total** | **940–1,320** |

At 12–15h/week: **roughly 16–22 months.** MIT 6.5840 remains the anchor — build the schedule around it. DSA runs daily throughout via your existing skills, using the per-level companion patterns above so it never feels disconnected from the systems work.

---

## X — The Library, Cross-Referenced to What You Own

| Topic | Roadmap level | Your book |
|---|---|---|
| Scale estimation, basic building blocks | 0, throughout | Xu Vol 1 Ch. 1 |
| Rate limiting | 4.2 | Xu Vol 1 Ch. 4 |
| Consistent hashing | 2.4, 3.2, SWARM S5 | Xu Vol 1 Ch. 5 |
| Caching, CDN | 4.2 | Xu Vol 1 Ch. 6, 8 |
| Message queues | Level B-equivalent, 3.4 | Xu Vol 1 Ch. 11; DDIA Ch. 11 |
| Chat/messaging, notification systems | 1.3 | Xu Vol 2 |
| Distributed file/object storage | 2.2 (content-addressed store) | Xu Vol 2; DDIA Ch. 3 |
| Replication | 2.4 | DDIA Ch. 5 |
| Partitioning/sharding | 2.4 | DDIA Ch. 6 |
| Transactions, isolation | (general canon, Level 2) | DDIA Ch. 7 |
| Partial failure, distributed systems fundamentals | 3.1 | DDIA Ch. 8 |
| Consensus, consistency, Byzantine faults | 3.2, 5.1 | DDIA Ch. 9 |
| Batch/stream processing | (condensed, general canon) | DDIA Ch. 10–11 |
| Storage-engine internals (B-Trees, LSM) | 2.1 | DDIA Ch. 3; CMU 15-445 (no book substitute) |
| Raft specifically | 3.2 | the Raft paper — DDIA references it but doesn't replace implementing it |
| Chord/DHT specifically | 3.2 | the Chord paper — same, no book substitute |
| LLM serving | G | vLLM's PagedAttention paper — post-dates both books |

**The pattern worth noticing:** your two books cover the *applied system-design* layer (Xu) and the *theoretical distributed-systems* layer (DDIA) comprehensively — the gaps are exactly the primary-source papers (Raft, Chord, PagedAttention) that no textbook fully substitutes for, which is why those specific papers stay as required reading even though everything else routes to your existing library.

---

## Closing

This is the version built for what actually held your interest across this whole conversation: a genuinely creative, graph-and-algorithm-heavy system, with every hard distributed-systems problem structurally load-bearing rather than bolted on, DSA woven into the work instead of run as a separate track, and every theory topic pointing at a book you already own on your shelf. The scope is complete — replication, sharding, consistent hashing, consensus, caching, queues, the full system-design canon are all here, cross-referenced — and the spine is, for the first time in this conversation, one you said you actually like.
