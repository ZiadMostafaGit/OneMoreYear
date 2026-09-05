# ΑΙΩΝ · AION — The Twelve-Month Backend & Distributed Systems Roadmap

## From "backend engineer with one year of experience" → the engineer who gets handed the hardest system in the company

**Αἰών** — *unbounded time.* Batch systems process bounded data. Streams are unbounded. That distinction is the whole project, and the name states it.

**Built for one person:** Ziad Mostafa Elsaid · Cairo, Egypt · ~1 year at Logic Leap · BSc Management Information Systems · Codeforces 1450 · targeting **backend roles with an infrastructure and systems intersection** at Google, Meta, Amazon, Microsoft, Stripe, Datadog, Cloudflare, Confluent, Databricks and their European offices.

**Week 1 begins Monday 2026-09-07. Week 52 ends Sunday 2027-09-05.**

> This is a **training program**, not a reading list. Every topic is entered through a **failure you reproduce before you are allowed the explanation.** Every project has **numeric exit criteria.** Every level ends with an **exam you pass or repeat.** Every claim about the job market carries **its number from your own dataset of 569 real postings.** Every week has a date. And unlike the plan this replaces, **every headline number is measured on real data**, not simulated.

---

## 📖 Contents

| # | Section |
|---|---|
| I | [What the Data Actually Said](#i--what-the-data-actually-said) |
| II | [The Five Decisions](#ii--the-five-decisions) |
| III | [The Evidence Base](#iii--the-evidence-base) |
| IV | [The Six Laws](#iv--the-six-laws) |
| V | [The Learning Loop](#v--the-learning-loop) |
| VI | [The Three Tracks](#vi--the-three-tracks) |
| VII | [**The Spine: AION**](#vii--the-spine-aion) |
| VIII | [The Eight Flagships](#viii--the-eight-flagships) |
| IX | [The Level Map](#ix--the-level-map) |
| X | [Levels 0–12 — the curriculum](#-level-0--machine-memory--measurement) |
| XI | [Track F — Fundamentals](#-track-f--the-gap-filling-curriculum) |
| XII | [Track I — The Interview Machine](#-track-i--the-interview-machine) |
| XIII | [Track J — Craft, Career & Visibility](#-track-j--craft-career--visibility) |
| XIV | [The 52-Week Calendar](#-the-52-week-calendar) |
| XV | [The Cut Order](#-the-cut-order) |
| XVI | [Assessment](#-assessment-the-three-proofs) |
| XVII | [Tracking & Re-planning](#-tracking--re-planning) |
| XVIII | [Résumé & GitHub Translation](#-résumé--github-translation) |
| XIX | [The Library](#-the-library) |
| XX | [Project Catalog](#-the-complete-project-catalog) |
| XXI | [Final Readiness Checklist](#-the-final-readiness-checklist) |

---

## I — What the Data Actually Said

Before the plan, the finding that produced it. We modelled eight candidate projects against all 569 postings, scoring each on what fraction of a posting's **technical** skills you could evidence after building it. The result overturned the question.

| What you add | Coverage, backend+infra postings |
|---|---|
| Nothing — you today | **1.0%** |
| The operational shell alone (K8s, AWS, Terraform, observability, on-call, SRE, security) | 15.1% |
| A columnar-database core, no shell | 3.0% |
| An edge/CDN core, no shell | 1.5% |
| A distributed-systems core, no shell | 6.5% |
| Shell + edge/CDN core | 17.6% |
| Shell + streaming core | 17.6% |
| Shell + columnar-database core | 21.1% |
| **Shell + distributed-systems core** | **41.2%** |
| **… + Java** | **58.8%** |

**Three conclusions, and they are the architecture of this document.**

**1. A distributed-systems core is worth double a storage core and 2.3× a networking core.** Not because meshes are more interesting — because *"Distributed systems"* is named in **44.5%** of postings while *"storage engines"* is named in **0.5%** and *"CDN"* in **0.5%**. Storage internals and packet-level networking are **interview** content. Distributed systems is **screening** content. AION is therefore a distributed system first and everything else second.

**2. Java was worth more than every project choice combined: +14.1 points, 44.7% → 58.8%.** It is 46.8% of your entire residual skill gap and 52.7% of backend postings — the single most-demanded skill in your corpus, above AWS. You ruled it out; the number reopened it. AION has a real Java service doing real work, not a token one.

**3. Within the distributed-systems family, the specific domain is worth about four points.** Which means the domain must be chosen on the two things coverage does *not* discriminate on: **whether you will still open the repository at 11pm in month nine**, and **which system gives the best forty-five minutes.**

That is why this plan exists and why it looks the way it does.

---

## II — The Five Decisions

**1. Budget: zero.** Everything runs on free tiers.
- **Oracle Cloud always-free** — 4 ARM Ampere cores / 24GB RAM, **no expiry.** AION's always-on cluster member, the ARM port target, and the machine that proves it runs somewhere other than your desk.
- **AWS 12-month free tier** — the AWS-specific work in Level 8. AWS is 33.6% of backend postings and 48.4% of the skills they name. **Sign up in Week 14, not Week 1**, so the twelve months cover Weeks 14–52 when you actually need it.
- **GCP $300 / 90-day credit** — spent in **one planned 72-hour window** in Level 8, running the cluster at a scale your workstation cannot reach.

**2. Hardware: 64GB+ workstation.** This is what makes AION feasible solo — you can run a **12–20 node cluster locally** with realistic memory footprints and process a real firehose against it. Measure the actual ceiling in Week 2 before anything depends on it.

**3. Applications open Week 40 (2027-06-07).** **Google and Meta run 6–12 month cooldowns after a failed loop.** Applying early does not buy feedback; it burns the company for the year. *One adjustment that does not move that date:* from **Week 30**, 2–3 applications/month to non-target regional companies purely for loop calibration. By Week 40 you will have had 15–20 real interview rounds before the first application that matters.

**4. Fully mobile. Read this in Week 1, not month 10.**

> **US H-1B cap registration happens once a year, in March.** A June 2027 start misses March 2027; a cap-subject US role then means register March 2028 → lottery → start October 2028. **Europe has no lottery** — Ireland's Critical Skills permit, the EU Blue Card, the Netherlands scheme and the UK Skilled Worker visa are continuous and reachable in 2027. **EMEA offices are the primary target, not the fallback.** The US is a two-to-three-year move via an EMEA office. *Verify current rules yourself in Week 1.*

**5. Four languages, each doing real work.** Not affectation — the system is genuinely large enough that each earns its place, and this is exactly how Flink, Spark and Kafka are actually built.

| Language | Owns | Corpus | Why it, specifically |
|---|---|---|---|
| **C++** | Execution kernels, state backend, zero-copy paths, SIMD aggregation | 23.4% backend | The hot path. Where cache lines and microseconds live. |
| **Java 21** | Job runtime, operator scheduler, checkpoint coordinator, the user-facing SDK | **52.7% backend** | How Flink, Spark and Kafka Streams actually work. Virtual threads for the operator scheduler is a current, credible story. **Closes 46.8% of your residual gap.** |
| **Go** | Control plane: Raft shard assignment, rebalancing, gateway, quotas, multi-tenant API | 35.9% backend | Connection handling and concurrent state machines. |
| **Python** | Firehose replay, fault injection, benchmarks, analysis, the adversary | 44.5% backend | Analysis and experimentation, and the highest-frequency language in the corpus. |

**Rust is deliberately dropped.** It does not appear in the top 28 backend skills and is 10.7% of your residual gap against Java's 46.8%. Keeping it would be a fifth language bought at the price of the first.

### 🌙 The Egyptian calendar, budgeted rather than discovered

**Ramadan 2027 ≈ 8 Feb – 9 Mar** lands on Level 6 — the hardest correctness level. **Weeks 23–25 are budgeted at 20h, not 32**, with scope moved out in advance. **Eid al-Fitr ≈ Mar 9–11** (Week 27, 26h). **Eid al-Adha ≈ May 16–19** (Week 37, 26h).

### ⚙️ Scope decision: the two famous courses

**MIT 6.5840 and CMU 15-445 are NOT run as full courses.** Together they are 230–370h against a depth budget of ~870h. Taking both leaves too little to actually build AION, and AION is the thing that gets you hired.

**Instead:** **Raft is implemented directly as AION's shard coordinator** (~50h, Level 5) from the extended paper plus Gjengset's *Students' Guide*, with your own seeded deterministic harness. **Storage internals come from building `statestore`** (~45h, Level 3), with 15-445 lectures 3–7 as *reference consulted when stuck*, not a course to complete. **Optional warm-ups** if you have slack: Fly.io Gossip Glomers 1–4 (Maelstrom-verified, ~15h) in Week 21's buffer.

> **🔀 THE EXTENDED TRACK.** If you want the full 6.5840 and 15-445 experience this becomes an **18-month plan.** Insert 15-445 as a 3-month block after Level 3 and 6.5840 Labs 1–5 as a 4-month block replacing Level 5, then resume at Level 6; everything shifts right by six months and applications open at Week 66. **Decide in Week 1 or at the Week-26 half-year gate, not later.**

---

## III — The Evidence Base

Everything here traces to a dataset you collected in **August 2026: 569 verified postings, 83 companies, 937 distinct named skills.** Where a number is not stated, no claim is being made.

**The corpus splits by function:** infra 19.7% · **backend 16.3%** · ML 14.9% · security 9.8% · fullstack 9.7% · data 6.2% · systems 4.9% · frontend 4.9% · mobile 4.4% · embedded 4.2%. Percentages below are against **backend (n=93)** or **backend+infra (n=205)**, stated each time.

### The degree question. Settled here. Never raised again.

| Question | Answer | Of |
|---|---|---|
| Postings requiring a PhD with no stated alternative | **5** (0.9%) | 569 |
| Postings demanding a CS degree, no alternative field, no experience route | **1** (0.18%) | 569 |
| — and that one is | **a student internship** | |
| **Backend postings stating no degree requirement at all** | **51 of 93 (54.8%)** | 93 |
| Backend postings that are CS-strict | 35 (37.6%) | 93 |
| — of which carry an equivalent-experience clause | 19 | |
| Backend postings requiring a PhD | **2** | 93 |

**More than half of backend postings state no degree gate at all.** Of the third that do, most carry the equivalent-experience clause. **That clause is the route, and something has to fill it. AION is what fills it.** Zero hours on credential anxiety. Zero hours on certifications that are not free and incidental.

### What backend postings actually demand (n=93)

| Skill | Share | Skill | Share |
|---|---|---|---|
| **Java** | **52.7%** | System design | 23.7% |
| AWS | 48.4% | GCP | 21.5% |
| **Distributed systems** | **48.4%** | **Kafka** | **20.4%** |
| Python | 43.0% | C++ | 19.4% |
| Go | 37.6% | CI/CD | 19.4% |
| Mentoring | 36.6% | **PostgreSQL** | **19.4%** |
| REST/API design | 34.4% | Microservices | 18.3% |
| Communication | 34.4% | Data structures | 17.2% |
| Scalability | 31.2% | On-call | 17.2% |
| Collaboration | 31.2% | Docker | 17.2% |
| Kubernetes | 30.1% | Testing | 15.1% |

### 🔴 The number that reorganised this plan

| Interview round | Named in backend postings |
|---|---|
| **System design** | **76.3%** |
| Algorithms / DSA | **18.3%** |

The plan this replaces spent 340 hours on DSA and gave system design a sub-thread. **That is inverted.** But DSA is still a *gate* — frequency is irrelevant when 100% of the loops behind those postings contain two coding rounds, and you are right that the bar has risen. So: **~300h DSA aimed at hard-problem fluency, and ~150h of dedicated system design as its own first-class track.** Both to passing standard. Neither optional.

### What backend engineers are actually asked to do (n=93)

Work across teams 59.1% · **build and ship services 55.9%** · test and assure quality 48.4% · **scale systems for growth 45.2%** · **design system architecture 41.9%** · **ensure reliability 38.7%** · mentor 34.4% · **optimise performance and latency 31.2%** · lead projects 30.1% · **build observability 22.6%** · **carry the pager 18.3%** · secure and comply 18.3%.

**AION is built so that eight of those twelve are things you have actually done**, not things you have read about.

### The residual gaps no solo project can close

**Mentoring 33.2% · Leadership 21.5% · Cross-functional work 9.8%.** You chose to source these from Logic Leap. That is correct — but it must be **deliberate**, not assumed. See Track J §J.5: specific situations to seek out at work, and the stories they become.

### 🔴 The split — the most important paragraph here

AION has two halves doing different jobs, and confusing them is how portfolios fail.

**The correctness and performance core** — distributed checkpointing, exactly-once semantics, the state backend, vectorized kernels, deterministic simulation — is the real intellectual content and it is what you talk about for forty-five minutes. **Algorithms are named in only 7.8% of the whole corpus.** If your CV said only *"I built a stream processor,"* the screen would not read it.

**The operational shell** — running it, sharding it, observing it, deploying it, breaking it, keeping it up, and letting strangers use it — is what the screen reads. Distributed systems 48.4%, AWS 48.4%, scalability 31.2%, Kubernetes 30.1%, observability 22.6%, on-call 17.2%.

**Why build the core at all?** Because it is the forty-five-minute answer; because *"I deployed a service on Kubernetes"* is what every candidate says and *"here is why a naive checkpoint barrier deadlocks under backpressure, and here is the seed that reproduces it"* is not; because a CS degree **asserts** you can do this and you have no such assertion, so a working exactly-once protocol with a recovery-time curve is a stronger claim *because it is checkable*; and because a year of YAML will not keep you going, and a plan you abandon in month four delivers nothing.

**The rule: the shell is never optional and never deferred past Level 8.** If the year goes badly, cut core depth before you cut shell — the cut order in §XV says exactly how.

---

## IV — The Six Laws

**1. Failure First.** Every topic opens with **🔥 THE WALL** — a broken system you reproduce. **You may not read the explanation until the failure is on your screen.** Knowledge acquired to resolve a felt confusion is retained permanently; knowledge from a blog post you nodded at is gone in nine days. Interviewers hear the difference instantly.

**2. Measure Everything.** Every project ships **📈 EXIT CRITERIA** with numbers. **A speedup you cannot attribute to a named mechanism is a coincidence.** Every optimisation reports wall time *and* the relevant hardware counter *and* the mechanism — or is marked "unattributed."

**3. Set the target before you measure. Record both numbers.** Every target here was written before any measurement existed. Some are wrong. **Record the pre-measurement target and the actual side by side**, and revise with a written reason. The pattern of how wrong you were becomes `RETROSPECTIVE.md` in Week 51 — a document almost no candidate has.

**4. Real data, always.** The plan this replaces measured everything in simulation. AION processes **real events from GH Archive** — billions of them, public, reproducible, and messy in ways synthetic data never is. When you must simulate, say so, and validate the simulator against the real system.

**5. Ship publicly.** Own repo, README with a diagram and a chart in the first screen, `make demo` that works on a clean machine.

**6. Be honest about prior art.** **Apache Flink has solved distributed exactly-once stream processing in production since 2015.** Spark Structured Streaming, Kafka Streams, Materialize, RisingWave, Arroyo and Bytewax all exist. **You are not inventing stream processing.** Say this first, unprompted, every time. **You are never allowed to say "unsolved", "first", or "nobody has done this."** State the gap precisely instead — it is a stronger answer and the only one that survives an interviewer who has used Flink.

---

## V — The Learning Loop

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. 🔥 BREAK      Reproduce the failure. Make it hurt. Screenshot it.        │
│                  You may not read ahead until it is on your screen.         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. 🔎 DIAGNOSE   Write the hypothesis down BEFORE you check. Then           │
│                  instrument: perf, strace, async-profiler, pprof, the sim.  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. 📖 THEORY     NOW read. The chapter answers a question you're holding.   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. 🛠 REBUILD    Implement the fix. Then implement the WRONG fix and prove  │
│                  why it's wrong. Both matter.                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. 📈 MEASURE    Before/after. Chart it. Find the NEW bottleneck your fix   │
│                  exposed — there is always one.                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 6. ✍️ WRITE      3–10 paragraphs: what broke, why, what the numbers said.   │
└─────────────────────────────────────────────────────────────────────────────┘
```

After ~40 of these you stop needing the roadmap. You will have the reflex of **reproduce → instrument → hypothesise → measure → write.** Everything else is vocabulary.

---

## VI — The Three Tracks

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ TRACK D — DEPTH  (59% · 19h/week)                                             │
│ Levels 0–12 + Track F. Builds the engineer. Builds AION.                      │
│ Long weekend blocks. Nothing hard is ever built in 45-minute slices.          │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK I — INTERVIEW  (25% · 8h/week → 12h from W40)                           │
│ DSA 5.5h + SYSTEM DESIGN 2.5h. DAILY from week 1. Never batched, never        │
│ skipped. System design is a first-class thread because it is 76.3%.           │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK J — CRAFT, CAREER & VISIBILITY  (16% · 5h/week → 8h from W40)           │
│ Design docs, ADRs, writing, OSS, referral pipeline, CV, applications, and     │
│ the Logic Leap mentoring/leadership evidence. Referrals open WEEK 18.         │
└───────────────────────────────────────────────────────────────────────────────┘
```

**Standard week: 32h = 19 Depth / 8 Interview / 3 Fundamentals / 2 Craft.**
**From Week 40: 32h = 12 Depth / 12 Interview / 8 Career.**

Your stated schedule: **4h weekdays + 6h each weekend day.** Nothing hard is built on a weekday evening — weekday hours are DSA, system design, fundamentals and reading; the weekend blocks are where AION is built.

> **Read twice.** Depth without the interview track means nobody sees the depth — you fail the phone screen and never reach system design. The interview track without depth gets you an L4 offer and a six-year stall. **If you have only one hour on a given day, spend it on Track I** — it is the only track that degrades irreversibly when skipped.

**Budget:** 52 × 32 = 1,664 nominal. −88 (four rest weeks at 10h) −36 (Ramadan W23–25 at 20h) −12 (two Eid weeks at 26h) = **≈ 1,528 effective hours.**

| Track | Hours | Share |
|---|---|---|
| Depth — AION + flagships | ~870 | 57% |
| Interview — DSA ~300h + system design ~150h | ~450 | 29% |
| Fundamentals | ~130 | 9% |
| Craft & Career | ~200 | 13% |

*(Totals exceed 100% because Fundamentals hours are counted inside Depth in the weekly split; the calendar in §XIV is authoritative.)*

---

## VII — The Spine: AION

**One system, built across all thirteen levels, one milestone per level.**

### What it is

**A multi-tenant distributed stream-processing platform.** Users submit jobs — their own code, written against your SDK — which you run *continuously*, sharded across a cluster, over a real high-volume event firehose, with **exactly-once semantics** and sub-second serving of the results.

**The pitch:** *"Flink, built from scratch and small enough to understand. I run 1.4 billion real GitHub events through a cluster I wrote, kill workers at the worst possible moment in the checkpoint protocol, and exactly-once still holds — and I measured what exactly-once actually costs you in throughput, which nobody publishes."*

### 🔴 The honesty statement — say this FIRST, every time

> Distributed stream processing is a solved problem and I did not invent it. **Apache Flink has run exactly-once stateful streaming in production since 2015**, using the Chandy–Lamport-derived asynchronous barrier snapshotting algorithm that I also implement. **Spark Structured Streaming, Kafka Streams, Materialize, RisingWave, Arroyo and Bytewax** all exist. Flink is battle-tested at a scale I will never reach.

**The gaps that are actually real, and each is measurable:**

1. **Nobody publishes the exactly-once cost curve.** Everyone says exactly-once is "expensive." *How* expensive — throughput and p99 with and without, across checkpoint intervals and state sizes — is not published as a curve anywhere. **That is measurable, and I measure it.** (Flagship #6.)
2. **Nobody publishes recovery time against state size** for a real engine, with the algorithm's phases broken out.
3. **Deterministic simulation of the checkpoint protocol is rare.** FoundationDB and TigerBeetle simulate storage systems; nobody publishes a simulator that injects worker death at *every* point in a distributed barrier-snapshot protocol and proves the invariant across ten thousand seeds. (Flagship #4.)
4. **There is no small, readable, benchmarked implementation.** Flink is ~2 million lines. A correct, measured, 30k-line engine that a person can read in a weekend does not exist.

**The sentence you are allowed to say:** *"Stream processing is solved — Flink has done exactly-once since 2015. What isn't published is what exactly-once actually costs, or how recovery time scales with state. I built an engine small enough to instrument completely and I have both curves."*

### 🔴 The scale statement — the other thing you say unprompted

> **This cluster is 12–20 workers on one workstation plus an always-free ARM cloud instance, processing a real public firehose.** It has never served a paying customer. Everything about *scale* beyond twenty nodes is measured in a deterministic simulator, and the simulator is validated against the real cluster at sizes where both run — that validation is in `docs/analysis/sim-fidelity.md`.

**But the data is real**, and that is the difference from most portfolio projects. GH Archive is billions of genuine events with genuine skew, genuine hot keys, genuine schema drift and genuine garbage in it. Nothing you learn from it is an artifact of your generator.

### Why this is a strong spine: every hard problem is structurally forced

There is no single node to fall back on when you get lazy about distribution, no way to skip state because streaming state is the whole difficulty, and **no way to skip exactly-once**, because the premise is that a user's job produces the right answer while machines are dying underneath it.

| AION needs… | …forces you to master | Level |
|---|---|---|
| Keeping up with a firehose that never stops | **Backpressure, batching, the memory hierarchy** | 1 |
| Reading from a partitioned log without losing or duplicating | **Kafka internals, consumer groups, offset semantics** | 2 |
| Operator state that survives `kill -9` | **A storage engine: WAL, fsync, compaction, recovery** | 3 |
| Users writing jobs against an SDK | **Operator DAGs, scheduling, the JNI boundary, API design** | 4 |
| Deciding which worker owns which shard, with no fixed master | **Raft, leader election, rebalancing, membership** | 5 |
| Correct results while workers die mid-computation | **Distributed snapshots, exactly-once, recovery** | 6 |
| More events arriving than the cluster can process | **Admission control, shedding, goodput, autoscaling** | 7 |
| Running a stranger's code without it eating the cluster | **Sandboxing, resource metering, multi-tenancy, quotas** | 8 |
| Answering queries over continuously-updating results | **Materialized views, low-latency serving, consistency** | 9 |
| Keeping it up when you are the only one on call | **Observability, chaos, runbooks, SLOs** | 10 |

### The service and component map

| Component | Language | Appears | Purpose |
|---|---|---|---|
| `aion-kernels/ingest` | C++ | W3 | Zero-copy decode, batching, arena allocation |
| `aion-kernels/ops` | C++ | W4 | Vectorized map/filter/aggregate, SIMD |
| `aion-kernels/state` | C++ | W10 | LSM state backend: WAL, compaction, snapshots |
| `aion-kernels/window` | C++ | W12 | Windowing, watermarks, late-event handling |
| `aion-runtime` | **Java 21** | W14 | Operator DAG, scheduler (virtual threads), task lifecycle |
| `aion-sdk` | **Java 21** | W15 | The user-facing job API. What a tenant writes against. |
| `aion-checkpoint` | **Java 21** | W23 | Asynchronous barrier snapshotting, exactly-once, recovery |
| `aion-jni` | C++/Java | W14 | The kernel boundary. ADR-0001. |
| `aiond/coord` | Go | W18 | Raft: shard assignment, membership, rebalancing |
| `aiond/gateway` | Go | W8 | Job submission API, OpenAPI, auth, quotas |
| `aiond/scheduler` | Go | W27 | Placement, admission control, backpressure, autoscaling |
| `aiond/serve` | Go | W36 | Low-latency serving of materialized results |
| `aiond/tenant` | Go | W31 | Multi-tenancy, isolation, fair queuing, cost accounting |
| `aiond/admin` | Go | W47 | Ops surface: cluster health, shard state, manual drain |
| `aion-sandbox` | C++ | W31 | Untrusted job execution — **separate process** |
| `aionlab/sim` | Python+Java | W24 | Deterministic simulation of the checkpoint protocol |
| `aionlab/bench` | Python | W2 | The benchmark harness, used all year |
| `aionlab/analysis` | Python | W10 | Curves, plots, the Flink comparison |

**The C++/Java boundary — ADR-0001.** Kernels are compiled as a **static library with a C ABI**, called from `aion-runtime` over **JNI with off-heap direct buffers**, because operators are invoked at extremely high frequency on large batches and the JVM's garbage collector must never see the data plane. **The sandbox runs as a separate process** with a pipe protocol, because it executes untrusted code and **must not share a crash or memory domain with the runtime.** That asymmetry — JNI for trusted hot paths, process isolation for untrusted execution — is a real decision with a real rationale, and it is the first ADR.

### The real data

| Source | What | Volume | Used for |
|---|---|---|---|
| **GH Archive** | Every public GitHub event since 2011, hourly JSON | **~6 billion events, ~10TB** | The primary firehose. Real skew, real hot keys, real schema drift. |
| **GH Archive live** | The current hour, continuously | ~2–5M events/day | The streaming path, watermarks, late data |
| **Wikipedia EventStreams** | Live edit firehose, SSE | ~50–200 events/sec | A second source with different shape, for the multi-source path |
| **Synthetic amplifier** | Replay GH Archive at 100× wall-clock speed | tunable to millions/sec | Load testing, overload curves, the goodput chart |

**The Week-2 deliverable is `docs/SCALE-RISK.md`:** how many worker processes fit on your box at realistic state sizes, how fast you can actually decode GH Archive JSON, whether your disk sustains the write rate, and **a signed go/no-go on the local-cluster-plus-simulator strategy.** Do not defer this.

### The 12 milestones

| # | Level | Week | What you build | The invariant you must prove |
|---|---|---|---|---|
| **A0** | 1 | W4 | Single-node windowed aggregation over real GH Archive | Correct counts against a DuckDB ground truth on 100M real events; keeps up with 10× replay |
| **A1** | 2 | W9 | Partitioned ingest from Kafka, multiple consumers | No event lost or duplicated across a consumer rebalance, 500 forced rebalances |
| **A2** | 3 | W13 | C++ LSM state backend | `kill -9` mid-write, 1,000 cycles: state always recoverable, never corrupt |
| **A3** | 4 | W17 | Java runtime + SDK; a user job runs as an operator DAG | A job written against the SDK produces identical results to the hand-written pipeline |
| **A4** | 5 | W22 | Raft-coordinated shard assignment across N workers | Kill the coordinator mid-rebalance: **no shard unassigned, none double-assigned** |
| **A5** | 6 | W26 | **Distributed exactly-once checkpointing** | **Kill a worker at every phase of the barrier protocol, 500 seeds: output is exactly-once, always** |
| **A6** | 7 | W30 | Backpressure, admission control, cluster on k8s | Goodput held at 5× offered load by shedding, not collapse |
| **A7** | 8 | W35 | Multi-tenancy + untrusted job sandbox | One tenant at 100× load degrades others' p99 by <10%; a malicious job cannot escape |
| **A8** | 9 | W39 | Low-latency serving of materialized results | p99 < 50ms serving reads while ingest runs at full rate |
| **A9** | 10–11 | W47 | Public API, admin surface, chaos programme | 20+ logged incidents with runbooks; a peer resolves one using only the docs |
| **A10** | 12 | W52 | The Flink benchmark, ADRs, teardown | A stranger understands the architecture in 15 minutes |

### Non-goals — if you are doing one of these, stop

- **A SQL parser and optimizer.** Tempting, enormous, and it is a *compiler* project wearing a streaming costume. A minimal declarative job spec is in scope; SQL-over-streams is the **first thing on the cut list** (§XV).
- **Beating Flink on throughput.** You will not. Measure honestly, explain the gap, and that is a better answer than a rigged benchmark.
- **A polished web frontend.** A functional cluster dashboard, yes. A design system, no. Frontend is ~0% of your target postings.
- **Your own consensus algorithm.** Implement Raft from the paper. Inventing one is a research career, not a milestone.
- **A fifth language.** No Rust, no Scala, no Kotlin.
- **Training models.** There is no ML in this project and that is deliberate.
- **Kubernetes operators as a headline.** You deploy on k8s; you do not write a controller unless Level 11 has slack.

---

## VIII — The Eight Flagships

### The uniqueness rubric — score before you start. Build only if ≥7/10.

| # | Criterion | Pts | Test |
|---|---|---|---|
| 1 | Non-obvious premise | 2 | Would a bootcamp grad think of this? If yes, 0. |
| 2 | Produces an artifact that does not exist yet | 2 | A chart, dataset or comparison someone would cite |
| 3 | Requires a hard idea to be **correct**, not just to run | 2 | Is there an invariant that is easy to violate **silently**? |
| 4 | Demoable in 60 seconds | 1 | One terminal + one graph |
| 5 | Buildable solo in ≤3 weeks | 1 | Ambition that never ships is worth zero |
| 6 | Has a natural "and then it broke" story | 1 | Interview gold |
| 7 | Explainable to a non-specialist in 2 sentences | 1 | If you cannot, recruiters cannot pass it along |

**The four archetypes:** *Reimplementation with a twist* · *Instrument* (measures what people argue about with no data) · *Autopsy* (reproduce a real failure) · **Adversary** (builds the thing that proves a system wrong). **At least one flagship must be an Adversary.** AION has three.

| # | Project | Level | Archetype | Score | Pitch | Corpus |
|---|---|---|---|---|---|---|
| 1 | **`statestore`** | 3 | **Adversary** | 9 | A C++ LSM state backend — and the torture harness that `kill -9`s it 1,000 times and injects `fsync` failures at the syscall level | Testing 15.1% |
| 2 | **`raft`** | 5 | Reimplementation | 8 | Raft from the extended paper with a seeded deterministic harness making every failure reproducible from an integer | Distributed 48.4% |
| 3 | **`aionsim`** | 6 | **Adversary** | **10** | Deterministic simulation of the whole cluster — simulated clock, network with asymmetric partitions, disk, scheduler — **injecting worker death at every phase of the checkpoint barrier protocol.** 10,000 seeds nightly. | Testing 15.1% |
| 4 | **`overload`** | 7 | Instrument | 9 | The goodput-collapse curve: offered load to 5× cluster capacity across six admission strategies, collapse and graceful on the same axes | Scalability 31.2% |
| 5 | **`sandbox`** | 8 | **Adversary** | 9 | Untrusted tenant code with fuel metering and cgroup backstops, plus the four attacks that all work against the naive version | Security 10.9% |
| 6 | **`exactly-once-cost`** | 6+10 | **Instrument** | **10** | **The curve nobody publishes:** throughput and p99 with and against exactly-once, across checkpoint intervals and state sizes, plus recovery time against state size | Distributed 48.4% |
| 7 | **`flinkbench`** | 10 | **Instrument** | **10** | **Head-to-head against Apache Flink on the identical real firehose**, same hardware, same job, reproducible by one script — with an honest *"I am N× slower and here is precisely why"* | Distributed 48.4%, Perf 31.2% |
| 8 | **`incident-lab`** | 10 | **Autopsy** | **10** | Eight famous public outages reproduced locally with instrumentation and verified fixes, plus 20 self-inflicted incidents in AION | **On-call 17.2%, Observability 22.6%** |

**Core projects** (smaller, closing specific gaps): `latency-lab` (L0) · `sickbay` (L0, diagnosis under time pressure) · `c10k-arena` (L2, concurrency models) · `gatekeep` (L8, mTLS + secrets, Security 10.9%) · `costwatch` (L8, AWS 48.4%) · `pgshift` (L11, a 50M-row migration under live load, PostgreSQL 19.4%).

**Worked rubric — why `exactly-once-cost` scores 10:**

| Criterion | Score | Why |
|---|---|---|
| Non-obvious premise | 2 | "Everyone says exactly-once is expensive — how expensive?" is a question almost nobody has asked with numbers |
| Novel artifact | 2 | The curve does not exist publicly. Flink documents the mechanism; nobody publishes the cost. |
| Hard correctness | 2 | **Silently violable** — a checkpoint protocol that loses one event under one interleaving looks identical to a correct one |
| Demoable | 1 | One command kills a worker mid-barrier; one chart shows the cost |
| ≤3 weeks | 1 | Yes, given the engine and simulator exist |
| Breakage story | 1 | "My first barrier implementation deadlocked under backpressure and my own simulator found it at seed 4,187" |
| Explainable | 1 | "Measures what it costs to never lose or double-count an event when machines die" |

---

## IX — The Level Map

```
              ┌────────────────────────────────────────────────────────────┐
              │ TRACK I — THE INTERVIEW MACHINE                            │
              │ DSA (5.5h) + SYSTEM DESIGN (2.5h) · behavioural · mocks    │
              │ DAILY, W1 → OFFER DAY. Each level names the DSA patterns   │
              │ and the design problems its systems work reinforces.       │
              └────────────────────────────────────────────────────────────┘
              ┌────────────────────────────────────────────────────────────┐
              │ TRACK J — CRAFT, CAREER & VISIBILITY                       │
              │ Design docs · ADRs · writing · OSS · referrals · CV        │
              │ + the Logic Leap mentoring evidence. REFERRALS OPEN W18.   │
              └────────────────────────────────────────────────────────────┘
              ┌────────────────────────────────────────────────────────────┐
              │ TRACK F — FUNDAMENTALS (F1…F16)                            │
              │ Each block lands the week the project first needs it.      │
              └────────────────────────────────────────────────────────────┘

TRACK D — DEPTH:

  L0  Machine, Memory & Measurement ──►  W1–2    Sep 2026
  L1  The Firehose                  ──►  W3–4    Sep–Oct     A0
  L2  The Log & Concurrency         ──►  W5–9    Oct–Nov     A1
  L3  State                         ──►  W10–13  Nov–Dec     A2   ⚑ CV v1
  L4  The Runtime & SDK  ☕Java      ──►  W14–17  Dec–Jan     A3
  L5  Distribution & Consensus      ──►  W18–22  Jan–Feb     A4
  L6  Exactly-Once                  ──►  W23–26  Feb–Mar     A5  ⚑ CV v2  🌙 Ramadan
  L7  Overload, Backpressure & K8s  ──►  W27–30  Mar–Apr     A6
  L8  Multi-Tenancy, Sandbox, Cloud ──►  W31–35  Apr–May     A7  ⚑ CV v3
  L9  Serving & Query               ──►  W36–39  May–Jun     A8
  L10 Operations, Chaos & On-Call   ──►  W40–43  Jun–Jul     ⚑ CV v4  🎯 APPLY
  L11 Platform Completion           ──►  W44–48  Jul–Aug     A9
  L12 Synthesis & Conversion        ──►  W49–52  Aug–Sep     A10
```

| Lvl | Name | Weeks | Dates | Milestone | Flagship | Depth h |
|---|---|---|---|---|---|---|
| **0** | Machine, Memory & Measurement | 1–2 | Sep 7–20 2026 | — | `latency-lab`, `sickbay` | 32 |
| **1** | The Firehose | 3–4 | Sep 21 – Oct 4 | **A0** | — | 40 |
| **2** | The Log & Concurrency | 5–9 | Oct 5 – Nov 8 | **A1** | `c10k-arena` | 95 |
| **3** | State | 10–13 | Nov 9 – Dec 6 | **A2** | **#1 `statestore`** | 68 |
| **4** | The Runtime & SDK ☕ | 14–17 | Dec 7 – Jan 3 | **A3** | — | 76 |
| **5** | Distribution & Consensus | 18–22 | Jan 4 – Feb 7 | **A4** | **#2 `raft`** | 95 |
| **6** | Exactly-Once | 23–26 | Feb 8 – Mar 7 | **A5** | **#3 `aionsim`**, **#6 curve** | 42 🌙 |
| **7** | Overload, Backpressure & K8s | 27–30 | Mar 8 – Apr 4 | **A6** | **#4 `overload`** | 72 |
| **8** | Multi-Tenancy, Sandbox & Cloud | 31–35 | Apr 5 – May 9 | **A7** | **#5 `sandbox`**, `costwatch` | 95 |
| **9** | Serving & Query | 36–39 | May 10 – Jun 6 | **A8** | — | 66 |
| **10** | Operations, Chaos & On-Call | 40–43 | Jun 7 – Jul 4 | — | **#7 `flinkbench`**, **#8 `incident-lab`** | 48 |
| **11** | Platform Completion | 44–48 | Jul 5 – Aug 8 | **A9** | `pgshift` | 60 |
| **12** | Synthesis & Conversion | 49–52 | Aug 9 – Sep 5 | **A10** | — | 40 |

**Rest weeks: 13, 26, 39, 48** (10h, no new scope). **Buffer weeks: 22, 35, 43** (catch-up only; rest if on schedule).

---
---

# ⚡ LEVEL 0 — Machine, Memory & Measurement

> **Goal:** build the hardware mental model, and make every number you produce this year trustworthy.
> **⏱ Weeks 1–2 · 32h depth** · **Prereq:** none · **Fundamentals F1**

## 0.1 — The memory hierarchy, measured on your own machine

> ### 🔥 THE WALL
> Two functions summing the same 4096×4096 `int32` matrix — row-major and column-major. **Identical Big-O, identical instruction count.** Column-major will be 5–60× slower.
>
> Then two `int64` counters in one struct, two threads incrementing one each; then padded onto separate 64-byte cache lines. **Same work, 3–10× throughput difference.**
>
> **You may not read on until both numbers are on your screen.**

### 🔎 DIAGNOSE
```bash
perf stat -e cache-references,cache-misses,L1-dcache-load-misses,LLC-load-misses ./bench
perf stat -e cpu-cycles,instructions ./bench       # IPC is the smoking gun
perf c2c record ./false_sharing_bench              # cache-to-cache: false sharing, visualised
lscpu | grep -i cache && numactl --hardware
```
Instruction counts nearly identical, IPC not. **Modern CPUs are memory-limited, not instruction-limited, and Big-O is silent about the thing that dominates.**

### 📖 THEORY
The latency ladder with numbers you measured · cache lines (64B: touching one byte costs 64) · spatial and temporal locality · **AoS vs SoA — this is the columnar-versus-row argument and you will make it for real in Level 4** · **false sharing and MESI** · why an uncontended atomic costs ~20ns and a contended one ~100ns+ · prefetching rescues sequential access and cannot rescue pointer chasing · TLB and huge pages · NUMA.

**Why this is Week 1 and not Week 30:** in Week 4 you write vectorized operators, in Week 10 an LSM state backend, in Week 12 windowing over billions of events. **Every one of those is a memory-layout decision, and you make them all with these numbers in front of you.**

### 📄 SOURCES
- **Bryant & O'Hallaron, *CS:APP* 3rd ed. — §6.2–6.4 only** (~40 pages). Skip §6.1.
- **Drepper, "What Every Programmer Should Know About Memory" — §3 in full**, §6.2–6.4. Skip §4–5.
- **Igor Ostrovsky, "Gallery of Processor Cache Effects"** — ten experiments, run all of them.
- **Colin Scott's interactive latency numbers** — note what changed over 20 years and what did not.

### 🛠 CORE PROJECT — `latency-lab` *(Instrument, 8/10)* · 6h
A tool that measures the latency ladder of the machine it runs on and emits a personalised card: L1/L2/L3/DRAM, uncontended vs contended atomic, mutex, branch mispredict, NVMe 4K read, syscall, context switch, TCP loopback RTT. **Derive your cache sizes from a working-set sweep, without asking the OS.**

📈 **EXIT CRITERIA**
- [ ] Derived cache sizes match `lscpu` within one power of two — or you can explain why not
- [ ] Row-major vs column-major gap **explained by measured LLC-miss counts**, not asserted
- [ ] False-sharing fix ≥3× throughput, with `perf c2c` output committed
- [ ] A chart: working-set size (log x) vs ns/access, with the knees annotated
- [ ] You can recite the ladder in orders of magnitude in under 20 seconds

⛓ **PROBLEM CHAIN**
```
"Column-major is 40× slower"      → cache lines → columnar batch layout for operators   (→ L4)
"Contended atomic is 5×"          → MESI → why the shard table is read-mostly           (→ L5)
"Pointer chasing can't prefetch"  → why the LSM index is flat, not a node graph         (→ L3)
"DRAM is 78ns"                    → 20 workers × their state → the local ceiling        (→ 0.3)
"Syscall is 400ns"                → why ingest batches, and why the sandbox uses a pipe (→ L1, L8)
```

## 0.2 — Benchmark methodology: your numbers are lying to you

> ### 🔥 THE WALL
> Benchmark a trivial function five times. **The numbers differ by 15–40%.** Find out why, one cause at a time: frequency scaling, turbo, thermal throttling, ASLR changing alignment, thread migration, cold first iterations.
>
> Then build a **closed-loop** load generator (send the next event after the previous is acknowledged) and an **open-loop** one (fixed arrival rate regardless). Point both at a pipeline that stalls 200ms once a second. **The closed-loop harness reports a beautiful p99. It is a lie.**

### 📖 THEORY
**Coordinated omission** — a closed-loop generator cannot measure the latency of events it failed to send. When the pipeline stalls, the generator stalls with it, and every event that *should* have arrived does not exist in the data. **This matters more here than in almost any system**, because a stream processor's entire job is to keep up with a source that does not wait for it. An open-loop generator is not a nicety; it is the only honest model of a firehose.
**You cannot average percentiles.** The p99 of a pipeline of five operators is not the p99 of one. **Tail latency compounds through a DAG** — this is the whole of Level 7.
Warm-up, steady state, `benchstat`, ≥5 runs, report distributions.

**Reporting discipline for this repo:** every benchmark reports p50/p90/p99, peak RSS, **and the relevant hardware counter.** A latency number without one is not a result.

### 📄 SOURCES
- **Gil Tene, "How NOT to Measure Latency"** — in full, before you publish any benchmark this year.
- **Dean & Barroso, "The Tail at Scale", CACM 56(2), 2013** — eight pages.
- **Gregg, *Systems Performance* 2nd ed. — ch. 6 §6.6, ch. 13.** Reference.

### 🛠 CORE PROJECT — `aionlab/bench` + `sickbay` · 14h
The harness you use all year: fixed workloads, warm-up, percentiles, `perf stat` integration, **open-loop by default**, CI regression gate.
**`sickbay`:** 8 injectable pathologies in a container (memory leak, FD leak, lock contention, runaway syscall loop, disk saturation, CPU throttling under cgroup, DNS stall, **JVM GC pause**) each with a hidden `SOLUTION.md` showing the *evidence* that reveals it.

📈 **EXIT CRITERIA**
- [ ] Two runs produce byte-identical result sets (fixed seeds, stable tie-breaking)
- [ ] Harness is **open-loop by default**; you can explain why in one paragraph
- [ ] CPU pinning and governor applied inside the harness
- [ ] A deliberate 5% regression is caught by `benchstat` in CI
- [ ] **`sickbay`: median diagnosis under 10 minutes across all 8, on a shuffled re-run**

> ⚠️ **You revisit this in Week 28 (F12).** If your harness turns out to have coordinated omission, you **re-run every benchmark** and put the before/after in `bench/RESULTS.md`. *"I found coordinated omission in my own harness and re-measured six months of results"* is one of the strongest sentences you can say in an interview.

## 0.3 — How big can your cluster actually be, and how fast is the real data?

> ### 🔥 THE WALL
> Before any engine work: **download one day of GH Archive** (~24 files, ~2–4GB gzipped JSON). Decode it with the most obvious code you can write — `json.loads` in Python, then `nlohmann/json` in C++. Measure events/second.
>
> Then start **20 JVM worker processes**, each holding a 500MB heap, and watch what breaks first — RAM, file descriptors, or the page cache.
>
> **Those two numbers are the ceiling on your entire year**, and you need them in Week 2, not Week 30.

📈 **EXIT CRITERIA — `docs/SCALE-RISK.md`**
- [ ] **Real decode throughput measured** for naive JSON, and the gap to your target stated
- [ ] Measured max concurrent worker processes at realistic heap, with the binding resource named
- [ ] Disk sustained write rate measured — the state backend cannot exceed it
- [ ] `ulimit -n`, cgroup limits, and JVM heap/off-heap split documented
- [ ] Oracle always-free instance provisioned; a worker runs on it; `$0.00` confirmed
- [ ] **Signed, dated go/no-go on the local-cluster-plus-simulator strategy**

## 🎓 LEVEL 0 EXIT EXAM
1. Recite the latency ladder in orders of magnitude. How many L1 hits fit in one DRAM access? One NVMe read?
2. You store a batch of events as array-of-structs vs struct-of-arrays. For an aggregation touching one field of 1,000 events, how many cache lines each?
3. Explain false sharing in four sentences, then the fix.
4. What is coordinated omission? Sketch a harness where a 200ms stall is invisible.
5. Why can't you average p99s across a five-operator pipeline? What do you do instead?
6. Your box runs 18 workers and dies at 19. Name three possible binding resources and the command that identifies each.

**Pass = 5/6.**

**🔗 Track I companion (W1–2):** **DSA** — arrays, hashing, prefix sums, two pointers, sliding window. The cache intuition you just built is *why* these are fast in practice, not just in Big-O. **System design** — the estimation module: back-of-envelope arithmetic, the numbers to memorise (§XII).

---
---

# ⚡ LEVEL 1 — The Firehose

> **Goal:** process real, messy, high-volume data on one machine, correctly, and keep up with it.
> **⏱ Weeks 3–4 · Sep 21 – Oct 4 2026 · 40h** · **Milestone A0** · **Fundamentals F2**
>
> **From this week the project runs on real data.** Not a generator, not a simulator — six billion actual GitHub events with actual skew, actual schema drift and actual garbage in them. Everything you measure for the next twelve months is measured on this.

---

## 1.1 — Keeping up with something that does not wait

> ### 🔥 THE WALL — four failures, in order
> Write the obvious pipeline: read GH Archive line by line, `json.loads`, group by `repo.name`, count. Point it at one day of data (~4M events).
> 1. **It is 40× too slow.** JSON decoding dominates everything. Profile it and see.
> 2. **Then it runs out of memory.** Your hash map of repo→count is unbounded, and GitHub has a lot of repositories.
> 3. **Then the numbers are wrong.** Some events have a null actor. Some have a `repo` field that changed shape in 2015. Real data does this.
> 4. **Then you point it at the live stream and it falls behind, permanently.** There is no "catch up later" — the source keeps producing, and your lag grows without bound.
>
> **Screenshot all four.** Failure 4 is the one that defines the whole project: **a stream processor's only real requirement is that it keeps up.**

### 🔎 DIAGNOSE
```bash
perf record -g ./naive_pipeline && perf report      # where does the time actually go?
/usr/bin/time -v ./naive_pipeline                   # peak RSS — watch it climb
strace -c -f ./naive_pipeline                       # syscalls per event: the batching argument
```

### 📖 THEORY
- **Why decoding dominates.** A general-purpose JSON parser allocates, validates and copies. **You need three fields out of forty.** Selective parsing, `simdjson`'s approach (SIMD-based structural indexing), zero-copy string views into the input buffer, and arena allocation so you never `free` per event.
- **Batching as the fundamental unit.** Per-event processing means per-event syscalls, per-event allocations and per-event virtual calls. **Batches of 1,024–8,192 events amortise all three** and let the operator loop vectorize. This is why every serious engine — Flink, Spark, ClickHouse, DuckDB — is batch-at-a-time internally even when it is "streaming."
- **Bounded state is not optional.** An unbounded aggregation over an unbounded stream is a memory leak with a business justification. Windowing, and eviction.
- **Backpressure, stated early:** when a downstream stage is slower than an upstream one, the *only* correct responses are to slow the source, buffer with a bound, or drop with a policy. Unbounded buffering is the fourth option and it is how systems die.

### 📄 SOURCES
- **Arpaci-Dusseau, *OSTEP* — ch. 4–7** (processes, the API, direct execution, scheduling). Free.
- **Langdale & Lemire, "Parsing Gigabytes of JSON per Second"** — the simdjson paper. Read §2–4; it will change how you think about parsing.
- **Kleppmann, *DDIA* — ch. 11, first half** (streams, event logs) — read now, re-read at Level 6.
- **The GH Archive documentation and schema.** Read what the data actually is before you write code against it.

### 🛠 MILESTONE A0 — single-node windowed aggregation over real data · 30h

`aion-kernels/ingest` (C++): batched decode, arena allocation, selective field extraction. A hand-written pipeline computing tumbling-window counts by repository and by event type.

📈 **EXIT CRITERIA**
- [ ] **Decode throughput ≥ 500k events/sec/core**, measured, with the gap from the naive version attributed to named mechanisms (SIMD structural parse, arena allocation, selective extraction)
- [ ] **Correctness against ground truth:** the same aggregation computed in DuckDB over the same 100M real events, **matching exactly.** Any divergence is your bug, and finding it is the point
- [ ] Bounded memory: peak RSS flat across a 24-hour replay, with the eviction policy documented
- [ ] **Malformed and schema-drifted events handled explicitly** — counted, categorised, never silently dropped. Report the real rate you found in GH Archive
- [ ] **Keeps up with a 10× replay of the live firehose** with lag flat, not growing
- [ ] Batch size swept and the throughput curve plotted; the chosen size justified from it
- [ ] `docs/design/event-model.md` — the internal event representation and why

⛓ **PROBLEM CHAIN**
```
"JSON decode is 40× too slow"  → SIMD parse → selective extraction → arena allocation
"Per-event syscalls"           → batching → and batching enables vectorization           (→ L4)
"Unbounded hash map"           → windowing → eviction → and where does window state live? (→ L3)
"Real data has broken records" → explicit error channel → never silently drop
"It fell behind forever"       → backpressure → the only three correct responses          (→ L7)
"One machine isn't enough"     → partition the keyspace → but who owns which partition?    (→ L2, L5)
```

## 🎤 INTERVIEW PARAGRAPH — Week 4

> I'm building a distributed stream-processing platform — users submit jobs, I run them continuously over a real firehose with exactly-once semantics. Stream processing isn't new; Flink has done exactly-once in production since 2015 and I implement the same barrier-snapshot algorithm. What I'm building is a version small enough to instrument completely, and the thing I want to measure is what nobody publishes: what exactly-once actually costs you in throughput, and how recovery time scales with state size. Right now I'm four weeks in and deliberately still on one machine. The data is real from day one — GitHub Archive, about six billion events — and the first thing I did was write the naive pipeline and watch it fail four ways: JSON decoding was forty times too slow, the aggregation state was unbounded, real events have schema drift that silently corrupted my counts, and when I pointed it at the live stream it fell behind permanently. That last one is the whole project in one failure: a stream processor's only hard requirement is that it keeps up, because the source does not wait for you. So decode is SIMD-based selective parsing into arena-allocated batches now, at half a million events per second per core, and I verify correctness against the same aggregation run in DuckDB over a hundred million real events — they match exactly, which took three attempts.

## 🎓 LEVEL 1 EXIT EXAM
1. Why does a general-purpose JSON parser lose to a selective one by an order of magnitude? Name three mechanisms.
2. Why is every serious "streaming" engine actually batch-at-a-time internally?
3. Your aggregation state grows without bound. Give three bounding strategies and what each costs you.
4. A downstream stage is slower than upstream. Name every correct response, and the one that kills systems.
5. You found 0.3% malformed events. What are the three possible policies, and which does a billing pipeline need versus an analytics one?
6. How do you know your aggregation is correct? Answer without using the word "tests."

**Pass = 5/6.**

**🔗 Track I companion (W3–4):** **DSA** — binary search including **binary search on the answer** (batch-size tuning is literally this), stack and monotonic stack. **System design** — design a URL shortener and a rate limiter; both are estimation-and-storage warm-ups.

---
---

# ⚡ LEVEL 2 — The Log & Concurrency

> **Goal:** get events off a partitioned log into many concurrent consumers without losing or duplicating a single one, at rate.
> **⏱ Weeks 5–9 · Oct 5 – Nov 8 2026 · 95h** · **Milestone A1** · **Core: `c10k-arena`** · **Fundamentals F3, F4**
>
> **Kafka is 20.4% of backend postings** — the highest-frequency single system in your corpus after the cloud providers. This level is where you stop being someone who has *used* Kafka and become someone who knows what it guarantees and what it does not.

---

## 2.1 — Concurrency models, and the one the ingest path needs

> ### 🔥 THE WALL
> Write the dumbest possible ingest server: `accept()` → spawn a thread → read/decode/forward. Point 10,000 connections at it.
>
> Watch it die, and note **how** — RAM exhaustion from 10k × 8MB default stacks, or `pthread_create: Resource temporarily unavailable`, or the scheduler burning 40% system CPU on context switches. Then run it again with `ulimit -n 1024` and watch it fail in a completely different way. **Both failures teach different things.**

### 📖 THEORY
Process vs thread vs goroutine vs **virtual thread** cost in bytes and microseconds · the Linux scheduler and cgroup CPU throttling · **context switch anatomy: the cache cost dwarfs the switch cost** · `select → poll → epoll → io_uring` · readiness (epoll) vs completion (io_uring) models · Go's G-M-P scheduler and why a blocking syscall does not stall the world · **JVM virtual threads (Project Loom) and how they compare to goroutines** — you will use these in Level 4 and you should have measured them here · **file descriptors, `EMFILE` vs `ENFILE`.**

### 📄 SOURCES
- **OSTEP — ch. 25–33** (concurrency). Free.
- **Dan Kegel, "The C10K Problem"** — read as an artifact of how the industry got here.
- **Evan Klitzke, "Blocking I/O, Nonblocking I/O, And Epoll"** — precise and short.
- **Jens Axboe, "Efficient IO with io_uring"** — the primary source.
- **William Kennedy (Ardan Labs), "Scheduling In Go"** — all three parts.
- **JEP 444 (Virtual Threads)** and Ron Pressler's "State of Loom" — because Level 4's scheduler is built on this.

### 🛠 CORE PROJECT — `c10k-arena` *(Instrument, 9/10)* · 16h
The same echo server seven ways — process-per-connection, thread-per-connection, bounded thread pool, single-threaded `epoll`, `io_uring`, **goroutines**, **JVM virtual threads** — plus the harness benchmarking all seven at 100 / 1k / 10k / 50k connections.

📈 **EXIT CRITERIA**
- [ ] All seven pass an identical correctness test (echo integrity under concurrent load, no interleaving)
- [ ] Seven-line chart: connections (log) vs p99 latency; second chart for RSS
- [ ] **You can state exactly where each model's knee is and name the resource that caused it**
- [ ] io_uring shows **measurably fewer syscalls per message** than epoll — with the number from `strace -c`
- [ ] **Goroutines vs virtual threads compared directly** — this is a genuinely current comparison and almost nobody has the numbers
- [ ] Run under a cgroup CPU limit and show **how the ranking changes under throttling** — the Kubernetes reality, and almost nobody benchmarks it
- [ ] **The written conclusion: which model each AION component uses and why**, with the numbers

## 2.2 — What a partitioned log actually guarantees

> ### 🔥 THE WALL
> Run three consumers in a group over a 12-partition topic, processing GH Archive. Now kill one consumer mid-batch.
>
> Watch the rebalance. Then check your output: **you have duplicates.** The dead consumer processed events 400–450 and died before committing offset 450, so its replacement starts at 400 and does it again.
>
> Now "fix" it by committing the offset *before* processing. Kill it again. **Now you have missing events.** You have just derived, by hand, why at-least-once and at-most-once are the only two things a log gives you for free, and why exactly-once needs something else entirely.
>
> **This failure is the seed of Level 6. Keep the screenshots.**

### 🔎 DIAGNOSE
```bash
kafka-consumer-groups.sh --describe --group aion   # lag per partition — watch it during a rebalance
# diff your output against the DuckDB ground truth from Level 1: exactly which events are dupes?
```

### 📖 THEORY
- **The log as an abstraction** — an append-only, partitioned, offset-addressed sequence. Ordering is guaranteed **within a partition, never across**. Every design decision downstream follows from that one sentence.
- **Partitioning and keying** — the partition key determines which events share ordering *and* which worker will own them. Choose it wrong and you have a hot partition; GH Archive by `repo.name` has a severe one and you should find it.
- **Consumer groups and rebalancing** — how assignment happens, why a rebalance stops the world, cooperative vs eager rebalancing, and why a long processing loop causes a rebalance storm (`max.poll.interval.ms`).
- **Delivery semantics, precisely.** At-most-once, at-least-once, and why **"exactly-once delivery" is impossible** while **"exactly-once processing" is achievable** — the distinction Level 6 is built on, and one most engineers get wrong in interviews.
- **Offsets, commits and the gap** — the window between processing and committing is where duplicates live. Idempotence and transactional writes as the two escapes.
- **Retention, compaction, and the log as a database** — Kreps's "The Log" argument.

### 📄 SOURCES
- **Jay Kreps, "The Log: What every software engineer should know about real-time data's unifying abstraction."** Read it fully.
- **Kleppmann, *DDIA* — ch. 11 in full.** The exactly-once section is the one you will be asked about.
- **The Kafka documentation on consumer groups, rebalance protocols, and `enable.idempotence`.** The actual docs, not a blog summary.
- **Kleppmann, "Is Kafka a database?"** or *Making Sense of Stream Processing* (free) ch. 1–3.

### 🛠 MILESTONE A1 — partitioned distributed ingest · 45h

`aiond/gateway` (Go): the job submission and ingest API. Go consumers reading a 12-partition topic, feeding the C++ decode kernels, with explicit offset management.

📈 **EXIT CRITERIA**
- [ ] Real GH Archive loaded into Kafka; **partition skew measured and reported** — find the hot repositories and say what fraction of traffic they are
- [ ] **500 forced rebalances during sustained ingest: zero events lost.** Duplicates are permitted and **counted** — you fix them in Level 6, and knowing the exact duplicate rate now is what makes that improvement measurable
- [ ] Consumer lag stays flat under sustained load; the lag chart is in the README
- [ ] Cooperative rebalancing vs eager compared: **stop-the-world duration measured for both**
- [ ] A slow consumer is diagnosed via `max.poll.interval.ms` and fixed — reproduce the rebalance storm first
- [ ] `aiond/gateway`: submit-job REST API with OpenAPI, auth, and request validation *(REST/API design is 34.4%)*
- [ ] gRPC between gateway and workers, with a versioned protobuf schema; **an old worker and a new gateway interoperate**, asserted by a test with a pinned binary
- [ ] `docs/design/delivery-semantics.md` — **what AION guarantees today (at-least-once), what it does not, and what Level 6 will change.** Written now, revised then.

⛓ **PROBLEM CHAIN**
```
"10k threads killed the server"→ epoll → goroutines vs virtual threads → measure both
"Rebalance produced duplicates"→ at-least-once → commit-before vs commit-after → neither works (→ L6)
"One partition has 40% of traffic"→ key choice → hot keys → this haunts you at every level
"Rebalance storm"             → max.poll.interval → long processing loops → batching again
"Ordering broke across shards"→ per-partition ordering only → the fundamental constraint
"Where does the count live?"  → operator state → and it must survive a crash              (→ L3)
```

## 🎤 INTERVIEW PARAGRAPH — Week 9

> The ingest path is distributed now and the failure that taught me the most is one I caused deliberately. I ran three consumers over a twelve-partition topic and killed one mid-batch. The rebalance worked, but my output had duplicates — the dead consumer had processed fifty events and died before committing the offset, so its replacement redid them. So I moved the commit before processing, killed it again, and now events were *missing*. That's the whole delivery-semantics problem derived by hand in an afternoon: a log gives you at-least-once or at-most-once for free and nothing else, and exactly-once *delivery* is actually impossible — what's achievable is exactly-once *processing*, which needs coordinated snapshots, and that's what I build in month six. I also measured the partition skew in real GitHub data rather than assuming it was uniform, and it isn't remotely — a handful of repositories dominate, which means naive key-based partitioning gives you one worker doing forty percent of the work. On the concurrency side I benchmarked seven server models to fifty thousand connections including goroutines against JVM virtual threads, which is a comparison I couldn't find published anywhere, and I ran them all again under a cgroup CPU limit because that's the Kubernetes reality and it changes the ranking.

## 🎓 LEVEL 2 EXIT EXAM
1. What ordering does a partitioned log guarantee, and what does that force on your design?
2. Commit offsets before processing, or after? Give the failure mode of each.
3. Why is exactly-once *delivery* impossible but exactly-once *processing* achievable? Be precise.
4. Your partition key produces a 40% hot partition. Three fixes and what each costs.
5. Cooperative vs eager rebalancing. What is the actual difference and when does it matter?
6. Goroutines vs virtual threads vs epoll — when does each win? Answer from your own chart.
7. A consumer is "stuck." Name four causes and the command that distinguishes each.

**Pass = 6/7.**

**🔗 Track I companion (W5–9):** **DSA** — graph BFS/DFS, linked lists, trees, heaps, and design problems (LRU cache, rate limiter). **System design** — design a distributed message queue, and design a notification system. You are building the first one; use that.

---
---

# ⚡ LEVEL 3 — State

> **Goal:** a state backend that survives being killed, because streaming state is the whole difficulty of streaming.
> **⏱ Weeks 10–13 · Nov 9 – Dec 6 2026 · 68h** · **Milestone A2** · **🚩 Flagship #1: `statestore`** · **⚑ CV v1** · **W13 = REST WEEK** · **Fundamentals F5, F6**
>
> **Stateless stream processing is trivial and nobody needs it.** Every interesting job — windowed aggregation, joins, deduplication, sessionisation — is *stateful*, and the state is larger than memory, must survive crashes, and must be snapshottable while being written to. That last requirement is what makes Level 6 possible and it is why this level comes before it.

---

## 3.1 — 🚩 FLAGSHIP #1: `statestore` — the engine and the adversary

> ### 🔥 THE WALL — the torn write
> Build the simplest durable state: append `key,value` to a file, keep an in-memory hashmap of key → offset. **Now `kill -9` it mid-write. Restart. Is the state correct?** Do it 500 times with random kill timing.
>
> You will find: truncated records · records that parse but are garbage · an index pointing past EOF · and the nastiest — **records that look valid but are half-old, half-new.**
>
> Then discover, in order:
> - **`write()` returning success means nothing was persisted.** It is in the page cache.
> - **`fsync()` is what persists**, and costs ~100µs on NVMe.
> - **On some filesystems a failed `fsync` marks the pages clean anyway** — so retrying `fsync` after an error can silently lose your data. That is "fsyncgate," and it hit PostgreSQL. **You cannot retry an fsync failure; you must treat it as fatal.**

### 📖 THEORY
- **B-Trees vs LSM-Trees and the RUM conjecture** — you may optimise two of Read amplification, Update amplification and Memory; never all three. **Streaming state is write-dominated with point lookups**, which is why RocksDB (an LSM) backs Flink's state and why you build an LSM here. State which two you chose and why.
- **WAL** — redo logging, group commit, checkpointing, and the durability/latency dial (`fsync` per write vs group commit vs none). **Measure all three.**
- **Checksums and framing** — every record carries a CRC and a length; a torn tail is detected, not parsed.
- **Bloom filters** — skip an SST without reading it. Report the configured false-positive rate and the measured disk-read reduction.
- **Compaction** — and why it causes latency spikes you must budget background I/O for. **In a streaming system a compaction stall becomes consumer lag becomes a rebalance**, so this is not academic.
- **🔴 Consistent snapshots while writing continues.** This is the requirement Level 6 depends on absolutely: you must be able to say "give me the state as of exactly here" without stopping the world. LSM makes this natural — immutable SSTs plus a manifest — and that is not a coincidence.
- **MVCC and isolation** *(via F6)* — the vocabulary for Level 11's metadata store, and for understanding what your engine does *not* provide.

### 📄 SOURCES
- **Kleppmann, *DDIA* — ch. 3 in full.** Read it twice; the second time after the project.
- **Petrov, *Database Internals* — ch. 2–4** (B-trees), **ch. 5** (transaction processing, recovery, WAL/ARIES conceptually). Part I is the best storage-engine treatment in print. Skip Part II.
- **"Bitcask: A Log-Structured Hash Table for Fast Key/Value Data"** (Riak) — 6 pages, your v1 target.
- **The RocksDB wiki on column families, snapshots and checkpoints** — because this is exactly the API Flink uses and you are rebuilding it.
- **CMU 15-445 lectures 3–7** — buffer pool, hash tables, B+Trees. **Reference consulted when stuck. Not a course to complete.**
- **Rebello et al., "Can Applications Recover from fsync Failures?"** + the PostgreSQL fsyncgate thread.
- **Athanassoulis et al., "The RUM Conjecture."**

### 🛠 THE BUILD · 34h — `aion-kernels/state` (C++)

**The engine (v1→v5):** append log + in-memory index → CRC framing and partial-tail recovery → SST files and compaction → Bloom filter per SST → **consistent snapshot via immutable SSTs + manifest.**

**`statestore-torture` — the adversary, and the reason this scores 9/10:**
- Random workload while `kill -9`ing at random intervals
- **After every restart, verify four invariants:** every acknowledged write is present · no unacknowledged write is present · no key has a torn or garbage value · the index never points outside a file
- **Syscall-level fault injection via `LD_PRELOAD`:** `write()` succeeds but writes only half · `fsync()` returns `EIO` · a file is truncated at a random offset
- 1,000 cycles in CI

📈 **EXIT CRITERIA**
- [ ] **1,000 random-kill cycles, zero invariant violations**
- [ ] **Torn-write injection caught by checksums 100% of the time** — keep the pre-CRC branch to show a failing case
- [ ] Throughput: `fsync`-per-write vs group commit vs no-fsync, all three measured, **with a written argument for which AION ships and why**
- [ ] Bloom filter measurably reduces reads for missing keys, with configured *and measured* false-positive rate
- [ ] **Compaction's effect on p99 measured during a compaction** — and the write-stall behaviour under sustained ingest
- [ ] **🔴 A consistent snapshot is taken while writes continue, and reading it returns exactly the state as of the snapshot point.** Property-tested. **Level 6 cannot exist without this.**
- [ ] Snapshot cost measured: time and space, against state size — **the first half of the recovery-time curve**
- [ ] `docs/design/durability-contract.md` — what this engine guarantees and what it does not, in DDIA ch. 3's language

> **Why this is a flagship and "build a KV store" is not:** thousands of people have written Bitcask. **Almost nobody writes the torture harness.** The harness is the senior artifact — it demonstrates that correctness is something you *prove*, not assume.

## 3.2 — The injectable universe

> ### 🔥 THE WALL
> Try to write a test that asserts: *"if a worker takes a checkpoint, then dies 40 seconds later, recovery produces exactly the pre-death output plus the un-checkpointed suffix."*
>
> **You cannot, in under 40 seconds of real time, without real disk and real sleeps** — and the test will be flaky forever. Now try to test what happens if the clock jumps backwards mid-snapshot. **You cannot at all.**
>
> **This is the wall that forces the architecture**, and it is the single highest-leverage refactor of the year: it is what makes Level 6's simulator possible.

### 📖 THEORY
Hexagonal / ports-and-adapters · **every source of nondeterminism becomes an injectable port**: clock, network, disk, scheduler, random · **deep modules beat many shallow ones** (Ousterhout) and *"duplication is far cheaper than the wrong abstraction"* (Metz) · structured concurrency and **bounded queues as a mandatory design rule**: every queue has a maximum size and a written full-queue policy.

### 📄 SOURCES
- **Ousterhout, *A Philosophy of Software Design*** — short, sharp, and more right than *Clean Code* where they disagree.
- **Nathaniel J. Smith, "Notes on structured concurrency, or: Go statement considered harmful."**

📈 **EXIT CRITERIA**
- [ ] The state and pipeline core has **zero direct calls** to wall-clock, filesystem or network APIs — **enforced in CI** by a dependency lint, with a screenshot of a rejected violation
- [ ] **Core test suite runs in under 2 seconds** with no real time, disk or network
- [ ] **You can advance the clock 40 seconds in a test in microseconds**
- [ ] Swapping the state backend (LSM ↔ in-memory) is a **one-line change** in the composition root
- [ ] Every queue in the system has a maximum size and a documented full policy

## 🎤 INTERVIEW PARAGRAPH — Week 13 (and CV v1)

> Stateless stream processing is trivial and nobody needs it — every job worth running is stateful, so this month was the state backend, and I wrote it in C++ as an LSM tree. The part I'd point at isn't the engine, it's the torture harness that tries to destroy it: random workload while killing the process at random intervals, and after every restart it checks four invariants — every acknowledged write present, no unacknowledged write present, no torn values, index never points outside a file. A thousand cycles in CI. It also injects failures at the syscall level with LD_PRELOAD — a `write` that succeeds but only writes half, an `fsync` that returns EIO. That last one taught me something I'd have got wrong: on some filesystems a failed fsync marks the pages clean anyway, so you cannot retry it, you have to treat it as fatal. That's the bug that hit PostgreSQL.
>
> The requirement that actually drove the design, though, is one that only matters later: I need a **consistent snapshot of state while writes are still happening**, because month six is distributed exactly-once checkpointing and it's impossible without it. LSM makes that natural — immutable sorted files plus a manifest — and realising that the storage choice was really a checkpointing choice was the moment the architecture clicked. I also measured snapshot cost against state size, which is half of the recovery-time curve I publish later.

## 🎓 LEVEL 3 EXIT EXAM
1. Draw an LSM tree and a B+Tree. Give a workload where each wins decisively, and name the amplification factors.
2. Why is streaming state write-dominated, and what does that imply for the engine choice?
3. `fsync` returns EIO. What do you do, and why can't you retry?
4. Your torture harness found zero bugs. What do you conclude, and what do you do next?
5. How do you take a consistent snapshot while writes continue? Why does month six depend on it?
6. Compaction causes a 400ms write stall. Trace the consequence all the way to a consumer rebalance.
7. Why must the pipeline core have no wall-clock dependency? What becomes possible in month six because of it?

**Pass = 6/7.**

**🔗 Track I companion (W10–13):** **DSA** — trees and BSTs, heaps and top-K, tries. These *are* the structures you just built under production constraints. **System design** — design a key-value store, and design a distributed cache. You have opinions now; use them.

---
---

# ⚡ LEVEL 4 — The Runtime & SDK ☕

> **Goal:** turn a hand-written pipeline into a *platform* — users describe a job, you execute it as a scheduled operator graph.
> **⏱ Weeks 14–17 · Dec 7 2026 – Jan 3 2027 · 76h** · **Milestone A3** · **Fundamentals F7, F8**
>
> **☕ This is the Java level, and Java is 52.7% of your target backend postings — the single most-demanded skill in your corpus.** It is not here as a keyword. The runtime, the scheduler and the SDK are genuinely the right place for a managed language: this is exactly how Flink, Spark and Kafka Streams are built, and the reason is that user code lives here and user code must not be able to corrupt the data plane.

---

## 4.1 — Java 21, learned properly and fast

> ### 🔥 THE WALL
> Port your Level-1 aggregation to Java, naively — `ArrayList<Event>`, `HashMap<String, Long>`, streams API, objects everywhere. Run it on 100M real events beside the C++ version.
>
> It will be **5–20× slower and use 10× the memory.** Then look at where it actually went: not "Java is slow" but **allocation rate, pointer chasing through boxed objects, and GC pressure.** Turn on `-Xlog:gc*` and watch it.
>
> Then fix it the way real engines do — **off-heap `ByteBuffer`s, primitive arrays, object reuse, no allocation in the hot loop** — and get most of it back. **You have just learned the single most important thing about the JVM: it is fast when you stop making garbage.**

### 🔎 DIAGNOSE
```bash
java -Xlog:gc*:file=gc.log ...            # allocation rate and pause times
async-profiler -e alloc -d 30 <pid>       # WHERE the allocation happens — the killer tool
jcmd <pid> GC.heap_info; jcmd <pid> Thread.print
```

### 📖 THEORY
- **Modern Java, not 2011 Java.** Records, sealed interfaces, pattern matching for `switch`, `var`, text blocks. Your operator DAG is a sealed hierarchy of records — that is idiomatic Java 21 and it reads nothing like the Java people complain about.
- **The memory model and `volatile`, `final`, happens-before.** You are writing a concurrent scheduler; this is not optional.
- **Virtual threads (JEP 444)** — the operator scheduler runs thousands of tasks. Virtual threads make a blocking-style scheduler viable without a thread per task. **You benchmarked them against goroutines in Level 2**; now use them and report the real behaviour under load, including where they pin.
- **GC as an engineering parameter** — G1 vs ZGC, allocation rate as the thing you actually control, why `-Xmx` is not the interesting knob. **A GC pause in a stream processor becomes consumer lag becomes a rebalance** — same chain as compaction in Level 3.
- **Off-heap and the FFI boundary.** `ByteBuffer.allocateDirect`, and **JNI vs the Foreign Function & Memory API (JEP 442)**. Choose one, measure the per-call overhead, and write ADR-0001.
- **The operator DAG.** Sources, operators, sinks; logical plan → physical plan → task graph; chaining operators to avoid serialisation between them; parallelism per operator.

### 📄 SOURCES
- **Brian Goetz et al., *Java Concurrency in Practice* — ch. 3 (sharing objects), 5 (building blocks), 10 (avoiding liveness hazards), 11 (performance).** Still the reference; skip the dated executor material.
- **Ron Pressler, "State of Loom"** and **JEP 444** — for virtual threads as they actually are.
- **Aleksey Shipilëv's blog on JVM anatomy** — the "JVM Anatomy Quarks" series, specifically the allocation and GC entries. The best JVM performance writing that exists.
- **The Flink documentation on the job graph, operator chaining, and task slots.** You are rebuilding this; read how they explain it.
- **JEP 442 (FFM API)** — read before choosing JNI.

## 4.2 — The SDK: what a stranger writes against

> ### 🔥 THE WALL
> Hand your SDK to someone else — or to yourself in a fresh directory with no context — and ask them to write a job that counts events per repository in five-minute windows.
>
> **Watch where they get stuck.** Every place they hesitate is an API design bug. Then look at what you have to do when their job throws an exception on event 4 million: does the whole cluster die?

### 📖 THEORY
**API design as a first-class concern** *(REST/API design is 34.4% of backend postings and this is the interview-defensible version of it).* Fluent builder vs declarative spec · what is a compile-time error versus a runtime one · **serialisability of user functions** — a lambda capturing an unserialisable field is the classic Flink footgun and you will reproduce it · versioning the SDK against a running cluster · **failure isolation: user code throws, and the platform must degrade that job only.**

### 🛠 MILESTONE A3 — the runtime and SDK · 46h

`aion-runtime` (Java 21): operator DAG, task scheduling on virtual threads, operator chaining, the C++ kernel boundary. `aion-sdk` (Java 21): the job API. `aion-jni`: the boundary.

📈 **EXIT CRITERIA**
- [ ] **A job written against the SDK produces bit-identical results to the Level-1 hand-written pipeline** on 100M real events. This is the correctness gate for the whole level
- [ ] **Java pipeline within 2× of the C++ pipeline** end-to-end, with the remaining gap attributed to named mechanisms — or a written explanation of why not
- [ ] **Zero allocation in the steady-state hot loop**, proven by `async-profiler -e alloc` showing a flat allocation profile during a 10-minute run
- [ ] Operator chaining implemented; **the throughput difference between chained and unchained measured**
- [ ] **JNI/FFM per-call overhead measured** and the batch size chosen so it is <2% of operator time. **ADR-0001 written**
- [ ] Virtual-thread scheduler runs ≥10,000 concurrent operator tasks; **pinning incidents detected and reported** (`jdk.tracePinnedThreads`)
- [ ] A user job that throws on a poison event **fails that job only** — the cluster and other jobs are unaffected, asserted by test
- [ ] An unserialisable lambda capture produces a **clear error at submit time, not a mysterious one at runtime**
- [ ] `docs/design/job-model.md` + the SDK usability test with a real human, sticking points recorded and fixed

⛓ **PROBLEM CHAIN**
```
"Java was 15× slower"          → allocation rate → off-heap → object reuse → not "Java is slow"
"GC pause became consumer lag" → the same chain as compaction → latency budgets everywhere
"JNI call per event"           → batch across the boundary → measure the crossing cost
"User lambda captured a socket"→ serialisability → fail at submit, not at runtime
"One bad job killed everything"→ failure isolation → and this becomes multi-tenancy       (→ L8)
"Which worker runs which task?"→ scheduling → but who decides, with no master?            (→ L5)
```

## 🎤 INTERVIEW PARAGRAPH — Week 17

> This month AION stopped being a pipeline and became a platform: users write a job against an SDK and I compile it into an operator graph and schedule it. The runtime is Java 21, which is the right call and not a fashionable one — user code lives in the runtime, and this is how Flink, Spark and Kafka Streams are all built. The first thing I did was port my C++ pipeline to naive Java and it was fifteen times slower, which is the interesting part, because it wasn't "Java is slow" — `async-profiler` showed it was allocation rate and pointer chasing through boxed objects. Off-heap buffers, primitive arrays and object reuse got most of it back, and the steady-state hot loop now allocates nothing, which I prove with a flat allocation profile over a ten-minute run. The scheduler runs on virtual threads, so I can have ten thousand blocking-style operator tasks without ten thousand platform threads, and I report pinning incidents because that's the failure mode people hit. The API design lesson was sharper than I expected: I handed the SDK to someone and watched where they hesitated, and every hesitation was a design bug. The one I'm proudest of fixing is that capturing an unserialisable field in a user lambda now fails at submit time with a readable message, instead of throwing something mysterious on the cluster twenty minutes in — that's the classic Flink footgun and I reproduced it before I fixed it.

## 🎓 LEVEL 4 EXIT EXAM
1. Your Java version is 15× slower than C++. Name the three real causes, in order, and how you'd confirm each.
2. What is operator chaining and what does it save? Give the number from your own benchmark.
3. Virtual threads vs platform threads vs goroutines. When does each win? What is pinning?
4. Why does a GC pause in a stream processor become a consumer rebalance? Trace it.
5. A user's lambda captures a database connection. What should happen, when, and why?
6. JNI vs FFM. Which did you choose, what does a crossing cost, and how did you make it not matter?
7. A user job throws on one event in ten million. Design the policy. There are at least four defensible answers.

**Pass = 6/7.**

**🔗 Track I companion (W14–17):** **DSA** — dynamic programming (1-D, 2-D, knapsack) and greedy. **System design** — design a job scheduler and design a metrics/monitoring system. You are building the first; the second is next year's job.

---
---

# ⚡ LEVEL 5 — Distribution & Consensus

> **Goal:** many workers, no fixed master, and agreement on who owns what — while the membership changes underneath you.
> **⏱ Weeks 18–22 · Jan 4 – Feb 7 2027 · 95h** · **Milestone A4** · **🚩 Flagship #2: `raft`** · **🤝 Referral pipeline opens W18** · **Fundamentals F9, F10** · **W22 = buffer + pre-Ramadan pull-forward**
>
> **This is the level the whole plan was chosen for.** "Distributed systems" is named in **48.4% of backend postings** — tied for the highest single technical skill in your corpus — and this is where you earn it.

---

## 5.1 — Why a hash function is not enough

> ### 🔥 THE WALL
> Assign shards to workers with `hash(shard) % N`. Run 12 workers. Now **one worker leaves.** N becomes 11.
>
> **Almost every shard now maps to a different worker** — roughly (N−1)/N of them. And a shard moving means its *state* moves: gigabytes of LSM data over the network, while the stream keeps arriving. Measure how long the cluster is degraded. **On a system with any churn you would spend all your time moving state and none processing events.**
>
> Then implement consistent hashing and measure again. **Then the harder wall:** two workers both believe they own shard 7, and both write to the sink. **Consistent hashing did not prevent that, because it is not an agreement protocol.**

### 📖 THEORY
- **Consistent hashing and virtual nodes** — a departure moves 1/N of shards, not (N−1)/N. Virtual nodes fix load imbalance and the "one departure dumps everything on one neighbour" problem. **Measure load variance at 1, 10, 100 and 500 vnodes.** *(Alex Xu Vol 1 ch. 5 is the applied treatment; you own it.)*
- **Why you still need consensus.** Consistent hashing tells you who *should* own a shard. It does not stop two workers from *believing* they do during a partition, and in a stateful system that means two writers to the same state and duplicated output. **Assignment must be agreed, not computed.**
- **Raft in full:** terms · randomised election timeouts and why randomisation is load-bearing · RequestVote and the up-to-date-log check · AppendEntries · the **log matching property** · commit index advancement · applying to the state machine · membership changes.
- **🔴 The Figure 8 case** — why a leader may not directly commit an entry from a *previous* term, and the no-op-on-election fix. **This is the subtle part of Raft, it is what interviewers probe, and you must be able to draw it.**
- **Read-only optimisations** — ReadIndex and lease reads: how etcd serves linearizable reads without a log write.
- **Leases and fencing tokens** — a worker whose lease expired **must not be able to write to its shard's sink.** A TTL-based lock is not a lock in an asynchronous system. Kleppmann's argument, applied directly to shard ownership.
- **Rebalancing without stopping** — the hard operational problem: move shard ownership while events keep arriving. Drain, hand off state, resume from a known offset. **This is where Level 3's consistent snapshot earns its keep.**
- **Consistency models** — place AION on the map: what is linearizable (shard assignment), what is eventual (metrics, job status). F9's exercise, and ADR-0003.

### 📄 SOURCES
- **Ongaro & Ousterhout, "In Search of an Understandable Consensus Algorithm" — the EXTENDED version.** §5 in full, §6 (membership) carefully. The conference version omits crucial detail.
- **Ongaro's PhD thesis** — for log compaction and membership changes done properly.
- **Jon Gjengset, "Students' Guide to Raft"** — the single most useful supplement while implementing. Read it *before* you start.
- **DDIA ch. 8 in full** (partial failure, unreliable networks and clocks — **you cannot distinguish slow from dead**) and **ch. 9 in full** (consistency and consensus).
- **Jepsen's consistency model map** (`jepsen.io/consistency`) — one page. Memorise the hierarchy.
- **Kleppmann, "How to do distributed locking"** — then antirez's reply. **Read both.** Fencing tokens.
- **`thesecretlivesofdata.com/raft/`** — the visualisation, for intuition before the paper.
- **Karger et al., "Consistent Hashing and Random Trees" (STOC 1997)** — the original.
- *Optional in W22's buffer:* **Fly.io Gossip Glomers 1–4** — Maelstrom checks your consistency for you, which pairs perfectly with Level 6.

### 🛠 🚩 FLAGSHIP #2 + MILESTONE A4 · 70h

`raft` as a standalone, reusable Go library with its own seeded deterministic harness, then `aiond/coord` on top of it.

📈 **EXIT CRITERIA**
- [ ] Leader elected from 5 nodes; **re-elected within the timeout after a leader kill; no split-brain across 1,000 randomised runs**
- [ ] Log replication with the log-matching property, verified by a property test
- [ ] **Partition test: a minority partition CANNOT commit, across 500 randomised partition schedules.** On heal, the minority's uncommitted entries are correctly overwritten
- [ ] **The Figure 8 scenario constructed deliberately as a test**, and the commit rule shown to prevent it. Then: **you can draw it at a whiteboard in under five minutes, from memory.** Tested by a human in Week 21
- [ ] ReadIndex or lease reads implemented; **linearizable reads served without a log write**, latency difference measured
- [ ] Membership change (add and remove a worker) without losing availability
- [ ] **Every failure reproducible from a seed integer alone, on any machine.** The harness that makes this true is what makes Level 6 possible
- [ ] **A4: kill the coordinator mid-rebalance under sustained ingest — no shard left unassigned, none double-assigned.** Verified by an assignment table with a uniqueness constraint
- [ ] **Fencing tokens: a worker whose lease expired cannot write to its shard's sink.** Demonstrate the violation without them and the fix with them, same seed
- [ ] **Rebalance under load: shard ownership moves with state, zero events lost, and the degraded window measured** — plotted against state size
- [ ] Consistent hashing vs `mod N`: shards-moved-per-departure, both curves, one chart; load variance at 1/10/100/500 vnodes
- [ ] `docs/design/consistency.md` — what is linearizable, what is not, and what a job is actually promised

⛓ **PROBLEM CHAIN**
```
"mod N moved every shard"     → consistent hashing → vnodes → and shards carry STATE
"Two workers owned shard 7"   → hashing isn't agreement → Raft
"Can't tell slow from dead"   → you never can → design for at-least-once + fencing
"Split votes never resolved"  → randomised election timeouts → randomness is load-bearing
"Committed entry vanished"    → Figure 8 → the previous-term commit rule
"Expired lease-holder wrote"  → fencing tokens → a TTL is not a lock
"Rebalance moved 8GB of state"→ drain + handoff + resume-from-offset → snapshots earn out  (→ L3)
"How do I test all of this?"  → you can't by hand → deterministic simulation               (→ L6)
```

## 🎤 INTERVIEW PARAGRAPH — Week 22

> The cluster is real now, and the interesting part is *where* I put consensus. Consistent hashing tells you which worker should own a shard, and that's necessary — I measured mod-N against consistent hashing and mod-N remaps almost every shard when one worker leaves, which in a *stateful* system means moving gigabytes of state while the stream keeps arriving. But hashing is not an agreement protocol. During a partition two workers can both believe they own shard seven, and because they're stateful they both write to the sink and you get duplicated output. And you can never distinguish a slow worker from a dead one, which is DDIA chapter eight's central point. So assignment goes through Raft, which I implemented from the extended paper. The part that took longest was Figure 8 — the case where a leader must not directly commit an entry from a previous term — and I built that scenario as a deliberate test rather than waiting to hit it. Two things I'd flag. Fencing tokens: a worker whose lease expired must not be able to write to its shard's sink, and I can show you the same seed producing duplicated output without them and correctness with them. And rebalancing under load is much harder than electing a leader — you have to drain a shard, hand its state to a new owner, and resume from a known offset without losing an event, and the degraded window scales with state size. I have that curve.

## 🎓 LEVEL 5 EXIT EXAM
1. Why does `hash(shard) % N` move ~(N−1)/N of shards on one departure? Derive it. Why is it worse for stateful shards?
2. What do virtual nodes fix? Give two distinct problems.
3. Draw Raft's Figure 2 from memory.
4. Explain the Figure 8 scenario and the rule that fixes it. Five minutes, whiteboard.
5. Why is randomising the election timeout load-bearing rather than a detail?
6. Explain fencing tokens. Why is a TTL-based lease insufficient? Give AION's concrete failure without them.
7. Walk through rebalancing a 4GB stateful shard while events keep arriving. Every step, including the failure at each.
8. Place AION on the consistency map, component by component.

**Pass = 7/8.**

**🔗 Track I companion (W18–22):** **DSA** — union-find (shard ring membership), reductions and NP-hardness (Skiena ch. 9 — W18 is a *proving* week, three written reductions), bit manipulation, math. **System design** — design a distributed lock service and design a sharded database. **W21: first human mock + the Figure 8 whiteboard test.**

---
---

# ⚡ LEVEL 6 — Exactly-Once

> **Goal:** correct results while machines die underneath you. **This is the level the project exists for.**
> **⏱ Weeks 23–26 · Feb 8 – Mar 7 2027 · 42h** · **Milestone A5** · **🚩 Flagship #3 `aionsim`, #6 the cost curve** · **⚑ CV v2** · **W26 = REST WEEK** · **Fundamentals F11**

> ## 🌙 RAMADAN — READ BEFORE STARTING
> **Ramadan 2027 ≈ 8 Feb – 9 Mar**, colliding almost exactly with this level. **Weeks 23–25 are budgeted at 20 hours, not 32.** Week 26 is a rest week at 10h. A deliberate ~40-hour reduction.
>
> **Mitigations already applied:** the Chandy–Lamport and Flink snapshot papers are read in Week 22; the injectable-port architecture was built in Week 11, so this level is *harness construction*, not refactoring; the consistent-snapshot primitive already exists from Level 3; TLA+ is scoped to **one** protocol.
>
> **Do not try to run this at 32 hours.** You will lose Weeks 27 and 28, and Level 7 is not the one to start tired. Week 35 is the buffer that absorbs a slip.
>
> Reduced split: **11h Depth / 5h Interview / 2h Fundamentals / 2h Craft.** The interview track drops to 5h. **It does not stop.**

---

## 6.1 — The barrier, and why it is subtle

> ### 🔥 THE WALL
> You have a cluster, sharded state, and at-least-once delivery. Now answer: **what is "the state of the whole cluster at a single point in time"?**
>
> There is no such thing. There is no global clock, workers are at different offsets, and events are in flight between operators. Try the obvious approach — pause everything, snapshot, resume — and measure it: **the pause is proportional to the largest state in the cluster and the stream does not pause with you.** At 4GB of state you stall for seconds, lag explodes, and a rebalance triggers.
>
> Then try snapshotting each worker independently without coordination. **Now recovery produces a state that never existed** — worker A at offset 900, worker B at offset 400, an event counted by A but not B. **You have just rediscovered why Chandy and Lamport wrote their paper in 1985.**

### 📖 THEORY
- **Chandy–Lamport distributed snapshots**, and **Flink's asynchronous barrier snapshotting** — the practical derivative. Barriers are injected at the sources and flow *with* the data through the DAG; an operator snapshots when it has received the barrier on all inputs; **alignment** means buffering the fast inputs until the slow one arrives. The snapshot is consistent without ever stopping the world.
- **🔴 The three things that go wrong, and you will hit all of them.** *Alignment blocks under backpressure* — buffering a fast input while waiting for a slow one is exactly the wrong behaviour when you are already behind, which is why unaligned checkpoints exist. *State size dominates snapshot time* — hence incremental checkpoints on top of Level 3's immutable SSTs. *A worker dying mid-barrier* leaves partial snapshots that must be garbage-collected without deleting a live one.
- **Exactly-once processing, precisely defined.** Not "each event is delivered once" — that is impossible. It is: **the observable output is as if each event affected the state exactly once.** Achieved by: replayable sources (offsets) + coordinated state snapshots + **transactional or idempotent sinks.** Say all three; candidates who name only the middle one are the ones who have read about it rather than built it.
- **The sink problem.** Your state can be perfect and your output still wrong if the sink is not transactional or idempotent. Two-phase commit sinks, or idempotent writes keyed on `(job, operator, offset)`.
- **Recovery** — restore state from the last complete snapshot, reset sources to that snapshot's offsets, resume. **Recovery time = restore time + reprocessing time**, and the checkpoint interval trades one against the other. That trade is Flagship #6.

### 📄 SOURCES
- **Chandy & Lamport, "Distributed Snapshots: Determining Global States of Distributed Systems" (1985).** Eleven pages. Read it fully — it is one of the clearest papers in the field.
- **Carbone et al., "Lightweight Asynchronous Snapshots for Distributed Dataflows" (2015)** — the Flink algorithm. **This is the paper you implement.**
- **Carbone et al., "State Management in Apache Flink" (VLDB 2017).**
- **The Flink documentation on checkpointing, unaligned checkpoints, and end-to-end exactly-once.** Read how they explain the sink requirement.
- **DDIA ch. 11's exactly-once section**, re-read now that you have hit the problem.

## 6.2 — 🚩 FLAGSHIP #3: `aionsim` — deterministic simulation

> ### 🔥 THE WALL
> AION passes every test you have. Now answer: **what happens if a worker dies after emitting a barrier but before completing its snapshot, while a second worker is blocked on alignment, while the coordinator is mid-election, while the disk returns EIO — all within the same two seconds?**
>
> You cannot construct that by hand. There are millions of orderings. **So make the entire universe deterministic and let a seeded PRNG explore it for you.**

### 📖 THEORY

```
Real                        Simulated
──────────────────────────────────────────────────────────────────
System.nanoTime()      →    sim.Clock      (advances only when you say)
sleep / timers         →    sim.Timer      (instant; advances virtual time)
network / RPC          →    sim.Network    (delay, drop, reorder, duplicate, PARTITION)
disk / fsync           →    sim.Disk       (torn writes, EIO, tail truncation on crash)
task scheduling        →    sim.Scheduler  (deterministic single-threaded interleaving)
rand                   →    rng            (seeded)
a worker's death       →    sim.Kill       (at ANY phase of the barrier protocol) ← the AION one
```

Then `for seed in 0..100_000 { run(seed) }`. **When one violates an invariant you have a seed integer that reproduces it exactly, forever, on any machine.**

**🔴 The AION-specific contribution: killing a worker at every phase of the checkpoint protocol.** FoundationDB's and TigerBeetle's simulators model crashes, partitions and disk faults in *storage* systems. Nobody publishes a simulator that enumerates death points inside a distributed barrier-snapshot protocol — before the barrier, during alignment, after snapshot start, after snapshot completion but before acknowledgement, during coordinator commit. **Those five points have different failure semantics and the last two are where the real bugs live.**

**The invariants, checked continuously:**
1. **Exactly-once: the output multiset after recovery equals the output of a failure-free run.** This is the headline.
2. No shard is owned by two workers concurrently
3. Every completed checkpoint is restorable; no live snapshot is garbage-collected
4. State never contains an update from an event beyond the checkpoint's offsets
5. Recovery never resets a source to an offset before a completed checkpoint
6. No acknowledged shard assignment is lost across a coordinator change

### 📄 SOURCES
- **Will Wilson, "Testing Distributed Systems w/ Deterministic Simulation" (Strange Loop 2014).** **Watch in Week 22. The most valuable 40 minutes in this roadmap.**
- **Zhou et al., "FoundationDB" (SIGMOD 2021) — §4 on simulation.**
- **TigerBeetle's VOPR and simulation posts** — open source, readable, modern. Study the code.
- **Hillel Wayne, `learntla.com`** — free, and Ramadan-appropriate: reading, not grinding.
- **Newcombe et al., "How Amazon Web Services Uses Formal Methods" (CACM 2015)** — read first, to know why the hours are worth it.

### 🛠 THE BUILD · 32h — MILESTONE A5 + Flagships #3 and #6

📈 **EXIT CRITERIA**
- [ ] Aligned barrier snapshotting implemented end-to-end; **exactly-once verified against the failure-free baseline output**
- [ ] **A5: a worker killed at each of the five barrier-protocol phases, 500 seeds each — output is exactly-once every time**
- [ ] Idempotent sink keyed on `(job, operator, checkpoint)`; **the non-idempotent sink failure demonstrated first**, so the requirement is earned
- [ ] Incremental checkpoints on Level 3's immutable SSTs; **snapshot time vs state size, plotted, incremental against full**
- [ ] **The alignment-under-backpressure deadlock reproduced**, then fixed or explicitly bounded. If you implement unaligned checkpoints, measure what they cost
- [ ] `aionsim`: all seven simulated components, **10,000+ seeds nightly in CI**, simulated time ≥1,000× real
- [ ] **🔴 ≥3 real bugs found this way, each documented with its seed and a human-readable event trace.** *This is the deliverable.* **A harness that finds nothing means your fault injection is too gentle — go and make it worse**
- [ ] TLA+ spec of the barrier protocol; model-checks the exactly-once safety invariant; **≥1 real design bug found by TLC**, with its counterexample trace
- [ ] `docs/analysis/tla-vs-dst.md` — they catch **different** classes of bug; articulating that distinction is a genuinely senior insight
- [ ] **🔴 FLAGSHIP #6, part 1 — `docs/analysis/exactly-once-cost.md`:** throughput and p99 **with and without** exactly-once, swept across checkpoint intervals (1s → 60s) and state sizes (100MB → 10GB). **Overlaid: recovery time.** *This curve does not exist publicly.*
- [ ] **Published post: "Three bugs in my stream processor that no test suite would have caught."** With the seeds.

⛓ **PROBLEM CHAIN**
```
"Stop-the-world snapshot stalled 4s"→ asynchronous barriers → Chandy-Lamport
"Independent snapshots → impossible state"→ coordination is mandatory
"Alignment deadlocked under backpressure"→ unaligned checkpoints → and measure the cost
"Snapshot time grew with state"    → incremental → immutable SSTs earn out                (→ L3)
"State perfect, output still wrong"→ THE SINK → idempotent or transactional, say all three
"Can't test 5 simultaneous faults" → deterministic simulation → seeds
"Simulator found nothing"          → faults too gentle → make them worse
"How much does this cost me?"      → THE CURVE → the artifact nobody has                  (→ L10)
```

## 🎤 INTERVIEW PARAGRAPH — Week 26 (and CV v2)

> This is the month the project exists for. The question is: what does "the state of the whole cluster at one point in time" even mean, when there's no global clock and every worker is at a different offset? Stopping the world to snapshot works and I measured it — at four gigabytes of state you stall for seconds, the stream doesn't stall with you, lag explodes and you trigger a rebalance. Snapshotting workers independently is worse: recovery produces a state that never existed. So it's asynchronous barrier snapshotting — Chandy–Lamport's 1985 result as Flink implements it. Barriers are injected at the sources and flow with the data; an operator snapshots when it has the barrier on every input.
>
> Three things bit me. Alignment — buffering a fast input while waiting for a slow one — is exactly the wrong behaviour when you're already backpressured, and it deadlocked; that's why unaligned checkpoints exist and I measured what they cost. Snapshot time grew with state until I made it incremental on top of the immutable SST files from month three, which is when I realised my storage choice had really been a checkpointing choice. And the one I'd want to be asked about: my state was perfectly correct and my **output** was still wrong, because exactly-once isn't one mechanism, it's three — replayable sources, coordinated snapshots, *and* an idempotent or transactional sink. Most people name the middle one.
>
> I test it with deterministic simulation. Every source of nondeterminism is an injectable port, so a whole run is a pure function of one integer, and I kill a worker at each of five distinct phases of the barrier protocol across ten thousand seeds a night. It found three real bugs, two of them at the phase between "snapshot complete" and "acknowledgement received," which is exactly where I'd have guessed wrong. And I published the thing nobody publishes: what exactly-once actually costs — throughput and p99 with and without it, swept across checkpoint intervals and state sizes, with recovery time on the same axes.

## 🎓 LEVEL 6 EXIT EXAM
1. Why can't you just stop the world and snapshot? Give the number from your own measurement.
2. Explain asynchronous barrier snapshotting to someone who knows Chandy–Lamport. What is alignment and what does it cost?
3. Define exactly-once processing precisely. Name all three required mechanisms.
4. Your state is correct and your output is wrong. What happened?
5. Name the five phases at which a worker can die during a checkpoint. Which two have the nastiest semantics and why?
6. Checkpoint interval: 1 second vs 60 seconds. What does each buy and cost? Answer from your curve.
7. TLA+ and DST catch different bugs. Give an example of each that the other would miss.
8. Your simulator ran clean for 10,000 seeds. What does that prove, and what does it not?

**Pass = 7/8.**

**🔗 Track I companion (W23–26, reduced to 5h):** **review and re-solve only. No new topics.** Backtracking and state-space search is the natural pairing — model checking and DST are structurally a systematic search over interleavings — but during Ramadan keep the streak and re-solve from the failure log. **Do the failure-category count in W26.**

> ### 🚩 HALF-YEAR GATE — end of Week 26
> Six months. Check honestly: **is there a working cluster — real events ingested from a partitioned log, sharded across workers with state that survives crashes, assignment agreed by Raft, and exactly-once output verified by a simulator?**
>
> If yes, you are on plan and the second half is where the corpus gaps close.
> If no, read the re-plan triggers in §XVII **now**, before Level 7, and reconsider the **Extended Track**. Eighteen months is a legitimate choice; a rushed Level 7–10 is not.

---
---

# ⚡ LEVEL 7 — Overload, Backpressure & Kubernetes

> **Goal:** stay useful when far more work arrives than the cluster can do. **This is where the corpus percentages start closing.**
> **⏱ Weeks 27–30 · Mar 8 – Apr 4 2027 · 72h** · **Milestone A6** · **🚩 Flagship #4: `overload`** · **Fundamentals F12, F13, F14**
>
> **Eid al-Fitr ≈ Mar 9–11 falls in Week 27** — budgeted at 26h.

---

## 7.1 — 🚩 FLAGSHIP #4: `overload` — the goodput curve

> ### 🔥 THE WALL
> Replay GH Archive at 3–5× the cluster's capacity with an **open-loop** generator. Plot offered load against **events successfully processed and checkpointed per second (goodput)**.
>
> It does not plateau at capacity. **It collapses toward zero.** Queues grow, checkpoint alignment takes longer because inputs are more skewed, checkpoints start failing their timeout, and a failed checkpoint means the next recovery replays more — so recovery gets *more* expensive exactly when you can least afford it. **Overload in a stateful streaming system is worse than in a stateless one, and the death spiral is checkpoint-mediated.** That is a genuinely non-obvious finding and it is yours to publish.
>
> **That graph is the most persuasive artifact in performance engineering and almost nobody has produced one.**

### 📖 THEORY
- **Little's Law: `L = λW`.** Concurrency = arrival rate × latency. A five-second calculation most engineers never make.
- **The queueing curve.** M/M/1: `W = S/(1−ρ)`. At ρ=0.5, 2× service time. At ρ=0.9, 10×. At ρ=0.99, 100×. **Memorise this shape** — it explains why you do not run at 90% utilisation.
- **Backpressure, properly.** Credit-based flow control between operators; how backpressure propagates from sink to source; and **why a stream processor's correct response to overload is to slow the source, not to drop** — unlike a request/response service. Dropping means data loss; slowing means lag. Know when each is acceptable and say so.
- **Overload responses in order:** bounded queues → **credit-based backpressure to the source** → **shed by key or by job priority, never randomly** (random shedding corrupts every aggregate) → **adaptive checkpoint interval** → autoscale.
- **Retry amplification** and **metastable failure** — the system stays broken after the trigger is removed because the backlog is now self-sustaining. **Recovery requires shedding or draining, not just fixing the trigger.** Extremely impressive in a design interview and almost nobody knows it by name.
- **Autoscaling a stateful system is not autoscaling a stateless one.** Adding a worker means moving state, which costs throughput exactly when you are behind. Measure the scale-up cost curve and the point where scaling up makes things worse before better.

### 📄 SOURCES
- **Dean & Barroso, "The Tail at Scale."** Re-read; you are living it.
- **AWS Builders' Library** — *"Using load shedding to avoid overload"*, *"Timeouts, retries and backoff with jitter"*, *"Avoiding insurmountable queue backlogs"*, *"Workload isolation using shuffle-sharding"*. **Read the whole library across Levels 7–10; the best free reliability writing that exists.**
- **Netflix, "Performance Under Load: Adaptive Concurrency Limits"** + the `Netflix/concurrency-limits` source.
- **Google SRE Book ch. 21 (Handling Overload) and ch. 22 (Cascading Failures).** **Ch. 22 may be the most valuable chapter in the book.**
- **Bronson et al., "Metastable Failures in Distributed Systems" (HotOS 2021).**
- **The Flink docs on credit-based flow control and backpressure monitoring.**
- **Alex Xu, *System Design Interview* Vol. 1, ch. 1 and ch. 4.** You own it.

## 7.2 — Kubernetes, and observability

> ### 🔥 THE WALL — six failures, caused deliberately
> 1. `CrashLoopBackOff` from a missing ConfigMap key
> 2. `Pending` forever — no node satisfies the resource request
> 3. **OOMKilled under a "generous" limit** — because the container limit counts the JVM's *whole* footprint: heap, metaspace, thread stacks, direct buffers and your C++ arena. Set `-XX:MaxRAMPercentage` and `MALLOC_ARENA_MAX` and re-run. **This one is specifically vicious for AION because you deliberately allocate off-heap**
> 4. **CPU throttling** — give a worker `cpus=0.5`, watch p99 go to 400ms for 20ms of work. Find `nr_throttled` in `cpu.stat`. **Invisible from inside the container**
> 5. **A rolling update loses in-flight state** — because the pod dies before its checkpoint completes and there is no `preStop` drain
> 6. **DNS latency** — the `ndots:5` search-domain problem

### 📖 THEORY
- **The reconciliation loop** — etcd holds desired state, controllers drive actual → desired. **Everything in Kubernetes is `while true { observe; diff; act }`.** If you internalise one thing, this.
- **What happens on `kubectl apply`** — client → API server → authN → authZ (RBAC) → admission → etcd → watch → scheduler binds → kubelet → CRI → CNI. **A top-5 most-asked Kubernetes interview question.**
- **cgroups v2 and the JVM** — `memory.max` vs `memory.high`, CPU shares vs quota, container-aware heap sizing, why `nproc` lies inside a container.
- **Graceful shutdown for a stateful worker** — SIGTERM → stop taking new work → **complete or abort the in-flight checkpoint** → hand off shards → exit within `terminationGracePeriodSeconds`. Getting this wrong loses work on **every deploy**.
- **RED per service, USE per resource.** Histograms, not summaries — **you cannot average percentiles.** Cardinality as the thing that blows up the bill. **And the streaming-specific signals: consumer lag, checkpoint duration, checkpoint failure rate, backpressure ratio, watermark skew.** Those five are the dashboard you would actually open at 3am.

### 📄 SOURCES
- **Lukša, *Kubernetes in Action* 2nd ed. — ch. 1–7, 12, 17.**
- **"Kubernetes Failure Stories"** (`k8s.af`) — **read 10.** Highest learning-per-minute in the ecosystem.
- **Google SRE Workbook ch. 5, "Alerting on SLOs"** — multi-window multi-burn-rate alerting.
- **Majors, Fong-Jones, Miranda, *Observability Engineering* — ch. 1–6.**
- **Gil Tene, "How NOT to Measure Latency"** *(F12 — audit your own harness this week)*.

📈 **EXIT CRITERIA — Level 7 / A6**
- [ ] **🔴 THE GOODPUT CHART:** offered load 0.5×→5× capacity vs successfully checkpointed events/sec, for **six configurations** (naive · bounded queues · +credit-based backpressure · +priority shedding · +adaptive checkpoint interval · +autoscale). **Collapse and graceful on the same axes**
- [ ] Quantified: *"at 3× overload the naive cluster delivers X% of capacity; the adaptive one delivers Y%"*
- [ ] **The checkpoint death spiral demonstrated** — overload → longer alignment → checkpoint timeouts → longer recovery → worse overload — and then broken
- [ ] **A metastable failure reproduced, then made impossible.** Two graphs
- [ ] Autoscaling a stateful cluster: **the scale-up cost curve**, showing where adding a worker makes throughput worse before better
- [ ] Shedding is **by key or job priority, never random** — and you can explain what random shedding does to an aggregate
- [ ] Multi-stage Dockerfiles; images recorded; **`kubectl apply -k deploy/` brings up a 12-worker cluster on local k3s from nothing** *(Kubernetes 30.1%)*
- [ ] **Rolling restart of all workers with ZERO events lost and zero duplicated**, under sustained ingest. Harder than it sounds and it is the real lesson
- [ ] Prometheus + Grafana; RED per component **plus the five streaming signals**; **a dashboard you would actually open at 3am** *(Observability 22.6%)*
- [ ] Given an injected fault, **time-to-root-cause under 5 minutes using only the dashboards.** Demonstrate on video
- [ ] **F12 audit done: if your harness had coordinated omission, every benchmark is re-run and before/after is in `bench/RESULTS.md`**

## 🎤 INTERVIEW PARAGRAPH — Week 30

> This level was overload, and the finding I'd lead with is that a *stateful* streaming system fails differently from a stateless service. I drove the cluster to five times capacity with an open-loop generator and plotted goodput — successfully checkpointed events per second. It doesn't plateau, it collapses, and the mechanism is checkpoint-mediated: overload skews the inputs, skew makes barrier alignment take longer, longer alignment makes checkpoints time out, and a failed checkpoint means the next recovery has more to replay — so recovery gets more expensive exactly when you can least afford it. That death spiral isn't in the textbooks and I have the graph for it.
>
> The fixes are ordered: bounded queues, then credit-based backpressure to the source, then shedding — and shedding in a streaming system has a constraint a request/response service doesn't have, because dropping a random one percent of events silently corrupts every aggregate downstream. So shedding is by key or by job priority and never random. Then an adaptive checkpoint interval, and last, autoscaling — which for a stateful system is counter-intuitive, because adding a worker means moving state, which costs you throughput exactly when you're already behind. I measured the point where scaling up makes things worse before better.
>
> On Kubernetes the failure that taught me most was OOMKilled under a limit I thought was generous, because the container counts the JVM's whole footprint plus my off-heap arenas, not just the heap. And rolling restarts losing in-flight work until I wrote a `preStop` that completes the checkpoint and hands off shards before the pod dies.

## 🎓 LEVEL 7 EXIT EXAM
1. The cluster runs at 70% utilisation with p99 of 800ms. Load rises 20%. Estimate the new p99 and name the model.
2. Explain the checkpoint death spiral, in order, from your own data.
3. Why is random load shedding unacceptable in a streaming system but fine in a request/response one?
4. Explain coordinated omission and design a load test that avoids it.
5. Your JVM worker is OOMKilled at a 4GB limit with `-Xmx3g`. Name four things consuming the difference.
6. Autoscaling a stateful cluster under load: why can adding a worker make it worse? For how long?
7. What happens between `kubectl apply` and a running pod? 12+ steps.
8. What is a metastable failure? Give AION's and its mitigation.
9. Name the five streaming-specific signals on your 3am dashboard and what each tells you.

**Pass = 8/9.** *This is the level that separates candidates.*

**🔗 Track I companion (W27–30):** **DSA** — heaps and priority queues (scheduling under load *is* a priority-queue problem), sliding window (rate limiting literally is one), advanced graphs. **System design** — design a rate limiter, and design an analytics/metrics pipeline. You have built the second.

---
---

# ⚡ LEVEL 8 — Multi-Tenancy, Sandboxing & Cloud

> **Goal:** let strangers run their code on your cluster without them destroying it, each other, or your bill.
> **⏱ Weeks 31–35 · Apr 5 – May 9 2027 · 95h** · **Milestone A7** · **🚩 Flagship #5 `sandbox`, Core `costwatch`, `gatekeep`** · **⚑ CV v3** · **W35 = buffer** · **Fundamentals F15, F16**

---

## 8.1 — 🚩 FLAGSHIP #5: `sandbox` — running a stranger's code

> ### 🔥 THE WALL — four attacks, all of which work
> Your SDK lets a user submit a job. Submit four hostile ones and watch each win:
> 1. **`new File(System.getProperty("user.home") + "/.ssh/id_rsa")`** — the job reads your key and emits it as output.
> 2. **A memory bomb** — allocate in a loop. The OOM killer picks a victim and it may not be the offender.
> 3. **`while(true){}` in an operator** — one core pinned forever. **No timeout fires, because the task is "healthy," just useless. And the checkpoint barrier it should have forwarded never arrives, so the entire job's checkpointing stalls** — one tenant's infinite loop stops another tenant's progress.
> 4. **A job that opens an HTTP connection and exfiltrates the cluster's environment**, including cloud credentials.
>
> **Screenshot all four.** Attack 3 is the one specific to your architecture and it is the most interesting.

### 📖 THEORY
- **Why a JVM `SecurityManager` is not the answer** — deprecated for removal in JEP 411, and it was never a real boundary anyway. **Say this in interviews; most Java engineers do not know it was removed.**
- **The layers, and why several.** A **separate OS process** per tenant job (crash and memory domain isolation) · **cgroups v2** (`memory.max`, CPU quota — the hard backstop) · **seccomp** (syscall filter) · **no network namespace access by default**, with an explicit allowlist · and **fuel/deadline metering inside the runtime** so an operator that never yields is detected and killed rather than stalling the barrier.
- **Defence in depth, stated as a principle:** each layer assumes the one above it failed. ADR material, and how security people think.
- **Resource accounting per tenant** — CPU-seconds, bytes processed, state bytes, checkpoint storage. You cannot enforce quotas on what you do not measure.
- **Multi-tenancy proper:** per-tenant quotas and concurrency caps · **weighted fair queuing** · **shuffle sharding** (AWS's technique — the combinatorics chart showing blast-radius reduction is a great artifact and a great interview answer) · isolating one tenant's checkpoint failures from another's.

### 📄 SOURCES
- **"Understanding and Hardening Linux Containers" (NCC Group)** — the namespace-escape sections. This will stop you claiming your sandbox is stronger than it is.
- **Linux cgroups v2 kernel documentation — the `memory` and `cpu` controllers.** The actual doc.
- **JEP 411 (Deprecate the Security Manager)** — read the rationale.
- **AWS Builders' Library, "Workload isolation using shuffle-sharding."**
- **The Kubernetes API Priority and Fairness design doc** — a real production fair-queuing design.

📈 **EXIT CRITERIA — A7**
- [ ] **All four attacks fail**, each with a test asserting the failure mode and the log entry
- [ ] **Attack 3 specifically: a non-yielding operator is detected and its job killed, and other tenants' checkpoints complete normally.** This is the one that matters
- [ ] A memory-bomb job is killed at its limit; the worker stays healthy and other jobs are unaffected
- [ ] Network denied by default; an allowlisted job reaches only the allowed host, asserted
- [ ] Per-tenant resource accounting reconciling to total cluster CPU within 5%
- [ ] **One tenant at 100× load: other tenants' end-to-end p99 degrades by <10%.** Measured
- [ ] Shuffle sharding implemented with the **blast-radius combinatorics chart**
- [ ] A tenant hitting quota is rejected cleanly with correct `429` and `Retry-After`
- [ ] `docs/design/threat-model.md` — the layers, what each assumes has already failed, and **an honest statement of what you do NOT defend against** (a JVM 0-day, a kernel escape, a job that is merely slow and expensive)

## 8.2 — Cloud, ARM, and $0.00

> ### 🔥 THE WALL
> Deploy to Oracle's always-free instance. **`aion-kernels` does not build.** It is ARM — x86 intrinsics, `-march=native` assumptions, alignment, and whatever SIMD you wrote in Level 1 and 4.
>
> Port it. Then re-run the whole benchmark suite on ARM and compare. **The delta will not be uniform across components** — JSON decode, aggregation kernels, LSM compaction and the JVM runtime will all move differently — and working out why is a free, genuinely interesting result almost no candidate has.

### 📖 THEORY
**AWS, exactly the subset you need** — **do not study for a certification**; it closes no gap this level does not close better, with a running system as evidence instead of a badge:
**IAM** (roles vs users, assume-role, least privilege, **OIDC federation from CI so there are zero long-lived credentials** — the modern correct answer and the one AWS topic actually asked about in interviews) · **VPC** (subnets, SGs vs NACLs, **NAT gateway cost** — the classic surprise bill) · **S3** (consistency, storage classes, lifecycle, prefix scaling — used here for **checkpoint storage**, which is a real architectural use, not a contrived one) · **EC2** (t4g free tier) · **CloudWatch** (metrics, alarms, **the $1 billing alarm**).
**Cost as an architectural constraint** — most cloud bills are architecture problems wearing a finance costume. **Checkpoint storage is AION's cost driver**, and the checkpoint-interval knob you tuned in Level 6 for recovery time is *also* a dollars knob. Show both axes.

### 🛠 CORE PROJECTS · `costwatch` (12h) + `gatekeep` (10h)
**`costwatch`:** all AWS infrastructure in Terraform (`apply` from zero, `destroy` to nothing) · hand-written least-privilege IAM verified with the policy simulator · a **CloudWatch billing alarm at $1, tested by deliberately triggering it** (an untested alarm is not an alarm) · **free-tier drift detection** that fails CI if any non-free-tier resource is created.
**`gatekeep`:** mTLS between all cluster components · per-tenant API credentials, rotation, revocation · secrets out of git (`gitleaks` in CI) · **certificate expiry alerting tested by fast-forwarding a clock.**

📈 **EXIT CRITERIA — Level 8**
- [ ] Oracle always-free provisioned; a worker runs there in the real cluster over the real internet; latency cost measured
- [ ] **`aion-kernels` builds and passes all tests on aarch64**
- [ ] **`docs/analysis/arch.md`: x86 vs ARM across JSON decode, aggregation kernels, LSM compaction and JVM runtime — per-component delta, attributed** to cache sizes, memory bandwidth, vector width
- [ ] **S3 as checkpoint storage**, with the durability argument written down and restore-from-S3 timed
- [ ] **The checkpoint interval plotted against BOTH recovery time and monthly storage cost** — the two-axis version of Level 6's curve
- [ ] Terraform: `apply` from zero, `destroy` to nothing. **Nothing configured by hand**
- [ ] Billing alarm **tested by triggering it**; **$0.00 verified from both consoles and screenshotted — every month from here**
- [ ] The GCP $300 window planned in `docs/design/gcp-window.md` **before** spending a cent: one 72-hour run at a scale the workstation cannot reach, to validate the simulator
- [ ] **`docs/analysis/sim-fidelity.md`** — same experiments on the real 12-worker cluster and a 12-worker simulation. Where do they agree, where do they diverge, by how much, and does divergence grow with the GCP window's larger cluster? **A simulator you have not validated is a fantasy generator**
- [ ] `docs/design/slo.md` — SLOs with error budgets, **derived from measured numbers, not aspirational**
- [ ] **CV v3 written**

## 🎤 INTERVIEW PARAGRAPH — Week 35 (and CV v3)

> This level is where AION became multi-tenant, which means running strangers' code. I wrote four hostile jobs against my own platform and all four worked: one read my SSH key and returned it as output, one was a memory bomb that got the wrong process OOM-killed, one exfiltrated the environment including cloud credentials, and the fourth is the one specific to my architecture — an operator with an infinite loop. It doesn't crash anything. The task looks healthy. But it never forwards the checkpoint barrier, so **another tenant's** job stops checkpointing. One tenant's infinite loop silently stalls a different tenant's correctness guarantee, and that's a failure mode you only find by building both halves.
>
> So jobs run in separate processes with cgroup limits, seccomp filters and no network by default, plus deadline metering inside the runtime so a non-yielding operator gets killed instead of stalling a barrier. And I'd say plainly that the JVM SecurityManager is not a boundary and was deprecated for removal in JEP 411 — a lot of Java engineers still reach for it.
>
> The other thing worth mentioning is cost as architecture. Checkpoint storage on S3 is my main cost driver, and the checkpoint interval I'd tuned in month six for recovery time turns out to be the same knob that sets my monthly bill. So I plot it against both axes now. The whole thing runs at zero dollars a month across Oracle and AWS free tiers, verified from the consoles, and I ported the C++ kernels to ARM and published the per-component x86-versus-ARM delta, which is a free result almost nobody has.

## 🎓 LEVEL 8 EXIT EXAM
1. Why is the JVM SecurityManager not a security boundary? What replaced it?
2. Your sandbox has four layers. For each, state what it assumes has already failed.
3. A tenant's operator never yields. What breaks for *other* tenants, and why?
4. A tenant sends 100× load. Name three isolation mechanisms and each one's blast radius.
5. Your JVM worker is killed at a 4GB cgroup limit with a 3GB heap. Where did the rest go?
6. Your cloud bill is $0.00. Name three ways it becomes $400 next month and the control for each.
7. Your simulator says X and the real cluster says Y. What do you do, and what does the gap tell you?
8. The checkpoint interval sets recovery time *and* storage cost. Walk through choosing it for a customer with a 5-minute RTO.

**Pass = 7/8.**

> ### 🚩 TWO-THIRDS GATE — end of Week 35
> Eight months in. **The employment-critical half is built.** From here: serving (L9), operations (L10), conversion (L11–12).
> **More than two weeks behind? Go to §XV and cut in the stated order.** **Do not cut Level 10.** On-call is 17.2% and nothing else in this plan closes it.

**🔗 Track I companion (W31–35):** **DSA** — DP and greedy, segment trees and Fenwick trees, binary lifting, strings. **System design** — design a multi-tenant SaaS platform, and design a system with quotas and fair sharing. You have built both.

---
---

# ⚡ LEVEL 9 — Serving & Query

> **Goal:** answer questions about continuously-updating results in milliseconds, while ingest runs at full rate.
> **⏱ Weeks 36–39 · May 10 – Jun 6 2027 · 66h** · **Milestone A8** · **W39 = REST WEEK**
>
> **Eid al-Adha ≈ May 16–19 falls in Week 37** — budgeted at 26h.

---

## 9.1 — Reading what is still being written

> ### 🔥 THE WALL
> Add a read API over the live aggregation state and hammer it while ingest runs at full rate.
> 1. **Reads block writes**, or writes block reads, and your ingest throughput drops 40%.
> 2. **Two reads a millisecond apart return inconsistent answers** — one shard has processed up to offset 900 and another to 400, so a "total" is a number that was never true at any instant.
> 3. **A read during recovery returns state from before the failure**, silently.
>
> **Failure 2 is the interesting one.** In a sharded streaming system, "what is the current total?" has no well-defined answer unless you define one. **Most portfolio projects never notice this. Defining it is a senior act.**

### 📖 THEORY
- **Reading consistently from state that is being written** — MVCC snapshots on the LSM, or serving only from the last completed checkpoint. **The tradeoff is freshness against consistency and you must choose explicitly and document it.**
- **Watermarks as the answer to failure 2** — serve results only up to a watermark that all shards have passed, so every answer corresponds to a real point in stream time. Freshness cost measured.
- **Event time vs processing time**, and **late data**: what happens to an event that arrives after its window closed? Allowed lateness, side outputs, retractions. **This is the single most misunderstood topic in stream processing** and being crisp on it is a strong signal.
- **Materialized views and incremental maintenance.** A query registered once and kept fresh, rather than run repeatedly.
- **Serving-path design** — read path isolated from the ingest path so a hot query cannot cause consumer lag; caching with correct invalidation on state update.

### 📄 SOURCES
- **Akidau et al., "The Dataflow Model" (VLDB 2015)** — the definitive treatment of event time, windows, triggers and watermarks. **The most important paper in this level.**
- **Akidau, "Streaming 101 and 102"** — the accessible version. Read first.
- **Kleppmann, *DDIA* ch. 11's "Processing Streams" section** on time reasoning.
- **The Flink docs on event time, watermarks and allowed lateness.**

📈 **EXIT CRITERIA — A8**
- [ ] **p99 serving latency < 50ms while ingest runs at full rate**, and **ingest throughput degrades <5%** with the read path saturated
- [ ] **Watermark-consistent reads:** every answer corresponds to a real stream-time point across all shards, asserted by a test that would fail under naive per-shard reads
- [ ] **Freshness vs consistency measured** — how far behind is a consistent answer, plotted
- [ ] Event-time windowing with watermarks over real GH Archive, and the **real late-data rate reported** (GitHub events arrive out of order; find out by how much)
- [ ] Allowed lateness and a side output for events beyond it; **nothing silently dropped**
- [ ] A read during recovery either blocks or returns a clearly-stale-and-labelled answer — **never a silently wrong one**
- [ ] Read path isolated: a saturating query load does not increase consumer lag
- [ ] `docs/design/time-model.md` — event time, processing time, watermark generation, lateness policy, and **what a query result actually means**

## 🎤 INTERVIEW PARAGRAPH — Week 39

> This month was the read path, and it surfaced a question I hadn't thought hard enough about: in a sharded streaming system, what does "the current total" even mean? Two reads a millisecond apart gave me inconsistent answers, because one shard had processed to offset nine hundred and another to four hundred, so the total I returned was a number that had never been true at any instant. Most projects never notice that. The fix is watermarks — serve only up to a stream-time point that every shard has passed, so every answer corresponds to a real moment — and it costs freshness, which I measured and plotted.
>
> The related thing is event time versus processing time. Real GitHub events arrive out of order, and I measured the actual lateness distribution rather than assuming it, which tells you what your allowed-lateness window should be. Anything beyond it goes to a side output and is counted; nothing is silently dropped, because silently dropping late data is how you get an aggregate that's quietly wrong forever. And the read path is isolated from ingest, so somebody hammering queries can't turn into consumer lag — I verified ingest degrades under five percent with the read path saturated.

## 🎓 LEVEL 9 EXIT EXAM
1. Two reads a millisecond apart disagree. Why, and what is the fix?
2. Event time vs processing time. Give a concrete case where using the wrong one gives a wrong answer.
3. What is a watermark, how is it generated, and what does it cost you?
4. An event arrives after its window closed. Name four defensible policies and the domain each suits.
5. How do you serve reads from state that is actively being written? Two approaches and their tradeoffs.
6. A read arrives during recovery. What are the three defensible behaviours, and which is never acceptable?
7. Your real data had X% late events. How did you find out, and what did you change because of it?

**Pass = 6/7.**

**🔗 Track I companion (W36–39):** **DSA** — probability and expectation, randomised algorithms, reservoir sampling and sketching (you may actually need HyperLogLog here). **System design** — design a real-time leaderboard, and design a time-series database. **W38: FULL TIMED LOOP #1.**

---
---

# ⚡ LEVEL 10 — Operations, Chaos & On-Call

> **Goal:** close the gap with the least alternative route — **On-call, 17.2%** — produce the benchmark that ends arguments, and **start applying.**
> **⏱ Weeks 40–43 · Jun 7 – Jul 4 2027 · 48h depth** · **🚩 Flagship #7 `flinkbench`, #8 `incident-lab`** · **⚑ CV v4** · **🎯 APPLICATIONS OPEN W40** · **W43 = buffer**
>
> **The split changes from Week 40: 12h Depth / 12h Interview / 8h Career.** Applications are live; interview readiness is now the binding constraint.

---

## 10.1 — 🚩 FLAGSHIP #7: `flinkbench` — the comparison that ends the argument

> ### 🔥 THE WALL
> Run Apache Flink on the same hardware, over the same GH Archive firehose, computing the same windowed aggregation with exactly-once enabled. Then run AION.
>
> **You will lose.** Flink has had a decade of engineering and you have had ten months. **The number is not the point — the explanation is.** Find out precisely where the gap is: is it the network stack, the serialisation format, operator chaining, checkpoint alignment, the JNI boundary, the JVM's escape analysis? Attribute every part of the difference to a named mechanism.

### 📖 THEORY
Fair benchmarking: identical hardware, identical data, identical semantics (**if Flink is exactly-once, yours must be too — comparing your at-least-once to their exactly-once is a rigged benchmark and a reviewer will catch it**), warm-up, multiple runs, distributions not means. State versions. State configuration. **Publish the configuration files.**

📈 **EXIT CRITERIA**
- [ ] **The table:** throughput, p50/p99 end-to-end latency, checkpoint duration, recovery time, CPU and memory per million events — AION vs Flink, same job, same data, same semantics
- [ ] **One script reproduces every number.** A benchmark you cannot reproduce is a marketing claim
- [ ] **Every part of the gap attributed to a named mechanism**, with the profile that shows it
- [ ] At least one place where **AION wins**, honestly found and honestly explained (likely startup time, memory footprint, or simplicity of a specific path) — and if there is none, say that
- [ ] `docs/analysis/vs-flink.md` — written as an engineer, not a marketer. **"I am 3.2× slower and here are the four reasons in order of size"** is a far stronger artifact than a win
- [ ] **Flagship #6 completed:** the exactly-once cost curve and the recovery-time-vs-state-size curve, final, on the real cluster

## 10.2 — 🚩 FLAGSHIP #8: `incident-lab`

### Part A — Six famous outages, reproduced locally

**For each:** read the postmortem → **build a minimal local reproduction** → observe with instrumentation → implement the fix → write your own analysis. 4–8h each; **do six minimum.**

| # | Incident | The mechanism | What it teaches you about AION |
|---|---|---|---|
| 1 | **AWS S3, Feb 2017** | An operator command removed more capacity than intended; the restart path had never been tested at that scale | **Never-tested recovery paths — your full-cluster cold start from S3 checkpoints is one, and you have never run it at 12 workers** |
| 2 | **GitHub, Oct 2018** | A 43-second partition triggered failover; both sides accepted conflicting writes → 24h of reconciliation | **Split-brain.** You built Raft and fencing tokens for exactly this. Reproduce it *without* them, then show yours surviving |
| 3 | **Cloudflare, July 2019** | A regex with catastrophic backtracking deployed globally in one step | **Global deploys need staged rollout — and you deploy tenant code to workers** |
| 4 | **Meta, Oct 2021** | A backbone change withdrew BGP routes for DNS; the company vanished, **including the tools needed to fix it** | 🔴 **Circular dependency in recovery. Does your admin surface depend on the cluster it administers? Does your checkpoint storage depend on something the cluster provides? Check** |
| 5 | **Slack, Jan 2021** | Traffic ramp → slow autoscaling → cascading saturation with a retry feedback loop | **Metastable failure.** You reproduced one in Level 7; this is the production version |
| 6 | **Roblox, Oct 2021 (73 hours)** | Consul streaming under load → contention → could not recover; **and the observability system depended on the failed cluster** | 🔴 **Your monitoring must not depend on the cluster it monitors** |
| 7 | **GitLab, 2017** | `rm -rf` on the wrong host — then the discovery that **5 of 5 backup methods had silently been failing** | **Untested backups are not backups. Your S3 checkpoint store is a backup you have restored from exactly once** |
| 8 | **Knight Capital, 2012** | Partial deploy + reused feature flag; $440M in 45 minutes | **You deploy code to workers you do not watch during the deploy** |

**Deliverable per reproduction:** `docker compose up` for the minimal system · a trigger script · **instrumentation showing the failure as it happens** · the fix with the same trigger now harmless · and an analysis naming **the trigger, the amplifier, the containment failure, the recovery obstacle, and the three controls that would have prevented or bounded it.**

### Part B — Twenty incidents in your own cluster

**≥20 logged incidents**, each with: the alert that fired (**or the alert that should have and did not**), a timestamped timeline, root cause, and a runbook entry.

**Injections:** worker kill mid-checkpoint · coordinator kill mid-rebalance · **asymmetric partition** · disk fill on a worker holding state · S3 unavailable during checkpoint · certificate expiry · a poison event that crashes one operator · **all 12 workers restarting simultaneously** · Kafka broker loss · a tenant job that never yields · consumer lag spike from a hot key · JVM GC pause storm · **clock skew.**

> ### 🔥 THE CLOCK SKEW INCIDENT — do this one properly
> Skew one worker's clock by four seconds. **Nothing fails loudly.**
>
> Watermarks generated on that worker are wrong, so windows close early or late. Lease expiry is computed against a clock that disagrees with the coordinator's. Event-time results are subtly wrong while every dashboard stays green and the error rate stays zero. **The worker does not crash — it quietly produces incorrect answers.**
>
> Then write the invariant check that catches it: **workers report clock offset relative to the coordinator, and a worker beyond a threshold is quarantined from watermark generation and shard ownership.** And note the deeper lesson — you built fencing tokens in Level 5 precisely because you cannot trust a clock, and this is the incident that proves you were right.

### 📄 SOURCES
- **Michael Nygard, *Release It!* 2nd ed.** — circuit breaker and bulkhead as named patterns. **The most relevant book to this level.**
- **Google SRE Book ch. 21, 22.** Ch. 22 is the most valuable chapter in the book.
- **`github.com/danluu/post-mortems`** — read one a week for the rest of the year.
- **Lamport, "Time, Clocks, and the Ordering of Events" (1978)** — eight pages, the most cited paper in the field.
- **Google SRE Workbook ch. 5** — multi-window multi-burn-rate alerting.

📈 **EXIT CRITERIA — Level 10**
- [ ] **≥6 famous outages reproduced**, each with before/after and a written analysis
- [ ] **🔴 The synthesis essay: "the seven mechanisms behind every major outage."** You will find them — config changes · circular dependencies in recovery · untested recovery paths · retry amplification · cold caches and thundering herds · silent backup or validation failure · unbounded resource growth. **Published**
- [ ] **≥20 incidents in AION**, each with alert, timeline, root cause, runbook entry
- [ ] **The clock-skew incident done properly**, with the quarantine invariant
- [ ] **Full-cluster cold start from S3 checkpoints, for real, and timed.** An untested recovery path is not a recovery path
- [ ] Every alert reviewed: actionable? runbook? worth 03:00? **An alert without a runbook is deleted, not documented**
- [ ] One deliberate **error-budget burn** with the written decision that follows
- [ ] `docs/REPORT.md` — the technical report, 15–25 pages: problem, architecture, benchmarks, the exactly-once curve, the Flink comparison, **and an honest limitations section** (cluster size, simulator fidelity, no SQL layer, single-author review). **The limitations section is what makes the rest credible**
- [ ] **CV v4 written; 48 applications sent**

## 🎤 INTERVIEW PARAGRAPH — Week 43 (and CV v4)

> Two things this month. The first is the benchmark against Flink — same hardware, same GitHub firehose, same job, and critically the same semantics, because comparing my at-least-once to their exactly-once would be a rigged test. I lose, which is the expected result after ten months against a decade, and the number isn't the point: I attributed every part of the gap to a named mechanism with the profile that shows it. Their network stack and serialisation account for most of it; my JNI boundary and checkpoint alignment account for the rest. I also found one place I genuinely win and said so, and one place I thought I'd win and didn't.
>
> The second is a deliberate failure programme — twenty-odd logged incidents where I killed workers mid-checkpoint, partitioned the cluster asymmetrically, filled disks, took S3 away during a checkpoint, and expired certificates, each with the alert that fired, a timeline, a root cause and a runbook. The one that taught me most is clock skew. I skewed one worker by four seconds and **nothing failed loudly** — its watermarks were wrong so windows closed at the wrong time, its lease expiry disagreed with the coordinator, and event-time results were quietly incorrect while every dashboard stayed green. It's also the incident that justified the fencing tokens I'd built five months earlier for reasons that were theoretical at the time. And I found a circular dependency in my own recovery by reproducing Meta's 2021 outage locally — the one where a BGP change took out their DNS and also the tools they needed to fix it.

## 🎓 LEVEL 10 EXIT EXAM
1. You are 3× slower than Flink. Where does the gap come from, in order of size?
2. What makes a benchmark against a mature system fair? Name four requirements.
3. Your clocks skew by 4 seconds. What breaks, and why does nothing alert?
4. Pick one reproduced outage. Trigger, amplifier, containment failure, recovery obstacle.
5. Why must observability not depend on the system it observes? Which AION component violates this?
6. Full-cluster cold start from S3. Walk through the first ten minutes and what fails.
7. Design an SLO for end-to-end processing latency. SLI, budget, burn-rate alert thresholds.

**Pass = 6/7.**

**🔗 Track I companion (W40–43):** topic learning is over. **Volume under time pressure and loop simulation** — company-tagged sets timed at 25 minutes, spoken aloud. **System design: full 45-minute designs, one per week, recorded.** Loops #2 and #3.

---
---

# ⚡ LEVEL 11 — Platform Completion

> **Goal:** the surfaces that make this a platform rather than a daemon. Interview volume ramps hard.
> **⏱ Weeks 44–48 · Jul 5 – Aug 8 2027 · 60h depth** · **Milestone A9** · **W48 = REST WEEK**
>
> ⚠️ **If you are behind, this is the level to cut.** Droppable in order: the dashboard's polish, `pgshift`, the tenant portal. **The API work is not droppable** — REST/API design is 34.4% of your target postings and this is where you earn it.

---

## 11.1 — The public API and the metadata store

📈 **EXIT CRITERIA**
- [ ] **OpenAPI 3.1 spec generated from code** (or code from spec — pick one, say why), with **drift detection failing CI** *(REST/API design 34.4%)*
- [ ] API versioning · **keyset pagination** over job and checkpoint history, with a benchmark of offset pagination at page 1 vs page 10,000 **and the `EXPLAIN` that says why** · **idempotency keys on job submission** (the same problem as Level 6's sink — say so in the doc) · rate limiting with correct `429`, `Retry-After`, `RateLimit-*` · **RFC 9457 Problem Details** error bodies with stable machine-readable codes
- [ ] **A pinned old-client binary in CI** whose requests must still pass against the new server
- [ ] Job definitions, tenant config and checkpoint metadata on **PostgreSQL**: schema migrations in git, applied automatically, reversible, tested against real Postgres in CI (**Testcontainers — never mock the database**) *(PostgreSQL 19.4%)*
- [ ] **`docs/design/isolation-level.md`** — which isolation level for the metadata store and why, **including the anomaly it does not prevent**
- [ ] `40001` serialization-failure retry loop, with **the retry rate measured under contention**

## 11.2 — `pgshift`: changing a hot table under live load

> ### 🔥 THE WALL
> Run `ALTER TABLE checkpoints ALTER COLUMN id TYPE BIGINT` on a 50M-row table while the cluster is checkpointing. **Everything queues behind the `ACCESS EXCLUSIVE` lock and checkpointing stops, which means recovery time is silently growing the whole time.** Capture the graph. That graph is half the project.

📈 **EXIT CRITERIA**
- [ ] **Expand/contract migration on a 50M-row table under live load: zero errors, p99 degradation <20%**, proven by a Grafana screenshot across the window
- [ ] **Backfill chunked, throttled and resumable** — kill it at 40%, restart, it completes correctly
- [ ] A verification pass proving all 50,000,000 rows match
- [ ] **The naive version's outage graph beside the correct one in the README**
- [ ] A written runbook: *"how to change a column type on a hot table,"* with rollback at every step

## 11.3 — The dashboard and admin surface

📈 **EXIT CRITERIA**
- [ ] `dashboard`: **WebSocket live cluster view** — workers, shards, job DAGs, lag, checkpoint status. **≥2,000 concurrent viewers sustained on the 4-core ARM box**, with **memory per connection reported and a bounded outbound queue with a stated drop policy** proven under a deliberately slow client
- [ ] **Reconnect storm test:** kill the dashboard holding 2,000 connections; show reconnect latency **with and without jitter.** Without jitter your redeploy is a self-inflicted DDoS
- [ ] `admin`: cluster health, shard state, manual drain, job kill, incident timeline. **Authenticated, audit-logged, every action reversible or confirmed**
- [ ] 🔴 **`docs/RUNBOOK.md` tested by a peer** resolving an injected incident using only the documentation. **Record every point where they got stuck and fix it.** Until now you have been the single point of failure for your own system — which is exactly what `incident-lab` #4 was about
- [ ] Pinned dependencies, SBOM, **CI fails on a known-critical CVE** *(Security 10.9%)*
- [ ] ≥8 full timed mock loops this level

## 🎤 INTERVIEW PARAGRAPH — Week 48

> This level was the surfaces. The one I'd point at is the schema migration: I changed a column type on a fifty-million-row table while the cluster was checkpointing. I did it the naive way first and captured the outage — everything queued behind an ACCESS EXCLUSIVE lock and checkpointing stopped, which is worse than it sounds because recovery time was silently growing the entire time the migration ran. Then I did it properly with expand/contract, dual writes and a chunked backfill that throttles when replication lag rises. Zero errors, p99 degradation under twenty percent, and both graphs are in the README because the failure is half the story.
>
> The other thing worth mentioning is that I had a colleague take my runbook and resolve an incident I injected, without me in the room. They got stuck in four places, and those four places were the actual gap between "I can operate this" and "this is operable." Until that test I was a single point of failure for my own system — the same failure mode as the Meta outage I'd reproduced two months earlier.

## 🎓 LEVEL 11 EXIT EXAM
1. Which isolation level for job metadata, and why? What anomaly does it not prevent?
2. Offset pagination at page 10,000. Explain with the query plan. What is the fix?
3. `ALTER TABLE` on a hot 50M-row table. Full plan, including rollback at every step.
4. 2,000 WebSocket viewers, one slow client. State your memory bound and how you enforce it.
5. You redeploy the dashboard. What happens to clients, and why do you need jitter?
6. Idempotency keys appear in three places in AION. Name them and explain why it is the same problem.
7. Your peer got stuck using your runbook. What was missing, and what class of gap is that?

**Pass = 6/7.**

---
---

# ⚡ LEVEL 12 — Synthesis & Conversion

> **Goal:** convert. **No new features.** The system was finished in Week 47.
> **⏱ Weeks 49–52 · Aug 9 – Sep 5 2027 · 40h depth** · **Milestone A10**
> Split: 10h legibility / 14h interview / 8h career.

> ### 📅 READ FIRST
> **The strongest big-tech hiring window is September–October 2027**, just past the end of this plan. Northern-hemisphere hiring slows through July–August — the months you are applying hardest — and picks up sharply in September when managers return and Q4 headcount is confirmed. That is a consequence of your Week-40 start, not a flaw: **your applications land as the window opens.** But **Week 52 is not the end of the process**, and `docs/NEXT.md` is the most important deliverable of the final week.

## 12.1 — Legibility (W49)

> ### 🔥 THE WALL
> Hand the repo to someone who has never seen it. **Ten minutes on a timer.** Ask: what is it, what is real, what is the most interesting technical decision in it?
>
> They will fail. Write down exactly where they got lost. **Interviewers do not explore repositories; they read what you point at.**

📈 **EXIT CRITERIA**
- [ ] **README final** for a ten-minute reader: what it is · **the prior-art statement and the scale statement, verbatim** · the three most interesting decisions, one sentence each · the headline numbers · one architecture diagram · what does not exist. **Tested on a human; their confusion points fixed**
- [ ] Architecture diagram, final. **Nothing aspirational**
- [ ] `bench/RESULTS.md` final — every benchmark, x86 and ARM, regenerable with one command
- [ ] **`docs/TOUR.md`** — *"ten minutes: read these three files. An hour: these eight."*

## 12.2 — The ten ADRs (W50)

Each: **context · options considered · decision · consequences · what you would do differently.**

| ADR | The contested decision |
|---|---|
| 0001 | **JNI/FFM for trusted kernels, separate process for untrusted tenant code** — the asymmetry |
| 0002 | **Java for the runtime, C++ for the kernels, Go for the control plane** — and where each boundary sits |
| 0003 | Consistency model per component; **what is and is not linearizable** |
| 0004 | **LSM state backend** — and that it was really a checkpointing decision |
| 0005 | **Aligned vs unaligned checkpoints**, and the interval you chose from the curve |
| 0006 | Raft for shard assignment rather than gossip or a fixed master |
| 0007 | **Exactly-once via replayable sources + snapshots + idempotent sinks** — and what you still cannot guarantee |
| 0008 | Simulator-first testing, and how you validated the simulator |
| 0009 | No SQL layer — a declarative job spec instead, and why |
| 0010 | S3 for checkpoint storage; the durability and cost argument |

📈 **ALSO**
- [ ] **`docs/LIMITATIONS.md`, linked from the README's first screen:** cluster size (12–20 real workers) · simulator fidelity and its measured divergence · no SQL layer · slower than Flink and by how much · single-author code review · no production users. **Volunteering limitations before you are asked is the single highest-leverage interview behaviour available to you**
- [ ] **`docs/COMPARISON.md`** — honest comparison against **Flink** (the reference implementation of everything here), **Spark Structured Streaming** (micro-batch instead of true streaming), **Kafka Streams** (library instead of cluster), **Materialize/RisingWave** (SQL-first, incremental view maintenance) and **Arroyo/Bytewax** (the modern lightweight attempts). Where you converge, where you diverge, why
- [ ] `docs/BUGS-INDEX.md` and `docs/incidents/README.md` — navigable. The simulator's bugs and the 20 incidents are among the most interview-useful things you own and they are currently buried

## 12.3 — The retrospective (W51)

> ### 🔥 THE WALL
> Open `LOG.md`. Compute, per level: **hours estimated vs actual, and the ratio.** You were consistently wrong in one direction by a consistent factor. **That factor is a measured fact about you over twelve months, and almost no candidate has one.**

📈 **EXIT CRITERIA**
- [ ] **`docs/RETROSPECTIVE.md`** — per level: estimated, actual, ratio. **Every target you set before measuring, with both numbers**
- [ ] The three things you would rebuild differently. Specific and technical, not "start earlier"
- [ ] One outward artifact — a talk outline or long-form post. **Strongest candidates: the exactly-once cost curve, the checkpoint death spiral, and the three bugs the simulator found**

## 12.4 — Close (W52)

📈 **EXIT CRITERIA**
- [ ] `make bootstrap` from clean. All tests pass. Cluster deployed and reachable. **Billing $0.00**
- [ ] **Record the 45-minute talk again and watch it against the Week-13 recording. The delta is the year**
- [ ] **`docs/NEXT.md`** — the September–October 2027 plan: application volume, target-list refresh, live loops, and **how you sustain 8h/week of DSA with no roadmap telling you to.** The habit has to survive the plan that built it

## 🎤 THE FULL ANSWER — Week 52

> I spent a year building a distributed stream-processing platform. Users submit jobs against an SDK; I compile them into operator graphs, shard them across a cluster, run them continuously over a real firehose — about six billion GitHub events — and guarantee exactly-once processing while machines die underneath. **Stream processing is solved: Flink has done exactly this in production since 2015 and I implement the same barrier-snapshot algorithm from Carbone's 2015 paper.** What I built is a version small enough to instrument completely, and what I measured is what nobody publishes.
>
> The layers: C++ kernels for decode, vectorized operators and an LSM state backend; a Java 21 runtime with a virtual-thread scheduler where user code lives; a Go control plane running Raft for shard assignment; and a Python lab for fault injection and benchmarks. The JNI boundary is batched so it is under two percent of operator time, and untrusted tenant code runs in a separate process because it must not share a crash domain with the data plane.
>
> The correctness core is asynchronous barrier snapshotting. Three things bit me and they are the three I would want to be asked about. Alignment deadlocks under backpressure, which is why unaligned checkpoints exist. Snapshot time grows with state until you make it incremental on immutable SSTs — my storage choice turned out to have really been a checkpointing choice. And my state was perfectly correct while my output was still wrong, because exactly-once is three mechanisms, not one: replayable sources, coordinated snapshots, **and an idempotent sink.** Most people name the middle one.
>
> I test it with deterministic simulation — every source of nondeterminism behind an injectable port, so a run is a pure function of one integer — killing a worker at each of five distinct phases of the barrier protocol, ten thousand seeds a night. It found three real bugs, two at the phase between snapshot completion and acknowledgement.
>
> Then the operational half: the goodput collapse curve, and the finding that overload in a stateful streaming system is checkpoint-mediated — skew makes alignment slower, slower alignment times out checkpoints, failed checkpoints make recovery more expensive exactly when you can least afford it. Multi-tenancy where one tenant's non-yielding operator silently stalls another tenant's checkpointing. Twenty incidents I caused on purpose. And a head-to-head against Flink where I lose by about 3×, with every part of the gap attributed to a named mechanism.
>
> The things I say without being asked: **my cluster is twelve to twenty workers I own, not a production deployment**, and I validated my simulator against it and published where they diverge. I have no SQL layer. I am slower than Flink and I can tell you precisely why. All of that is in a limitations document linked from the first screen of the README.

## 🎓 LEVEL 12 EXIT EXAM
1. Explain AION to a smart non-specialist in two sentences.
2. Name the five prior systems and where your design diverges from each.
3. Your three most interesting technical decisions, with the alternative you rejected.
4. What does your simulator prove, and what does it not?
5. The sharpest question an interviewer can ask about this project — what is it, and what is your answer? *(It is: "why would I use this instead of Flink?" The answer is: you would not, and here is what I learned by building it anyway, and here are two numbers Flink's team has never published.)*
6. Estimated vs actual hours. What is your ratio, and what will you do differently next time?

**Pass = 5/6.**

---
---

# 📚 TRACK F — The Gap-Filling Curriculum

> You are self-taught, which means your knowledge has holes you cannot see — not through carelessness, but because a curriculum's real function is to tell you what exists. **This is that function.**
>
> **The rule: no fundamental is taught in the abstract.** Each block lands the week the project first depends on it, uses **named chapters** rather than whole books, and ends in an exercise that proves it stuck.
>
> **Budget:** 3h/week most weeks, 2h during Ramadan, **0 from Week 40.** **Total ≈ 130h.**
>
> **An exercise you skipped is a block you did not do.**

| # | Fundamental | Weeks | Why exactly then |
|---|---|---|---|
| F1 | CPU memory hierarchy | 1–2 | You choose the batch and state layouts with these numbers in front of you |
| F2 | OS: processes, scheduling, isolation | 3–4 | The worker model, and Level 8's sandbox |
| F3 | OS: virtual memory & TLB | 5–6 | 20 workers on one box; memory is the binding resource |
| F4 | TCP, UDP & network behaviour | 7–9 | The wire protocol, gRPC, and everything from L7 |
| F5 | Cache-conscious data layout | 10–12 | The LSM index and the operator batch format |
| F6 | Transactions & isolation | 13–15 | The state backend's guarantees, and L11's metadata store |
| **F7** | **JVM: memory model, GC, virtual threads** | **14–16** | **The Java level. 52.7% of your postings.** |
| F8 | Probability & distributed randomness | 17–18 | Shard load distribution, election timeouts, sketches |
| F9 | Consensus, CAP & consistency models | 19–21 | Raft; and to place AION on the map |
| F10 | Performance measurement & optimisation | 21–22 | Everything you benchmark from here |
| F11 | Formal methods, lite | 23–25 | TLA+ on the barrier protocol |
| F12 | **Latency measurement done correctly** | 28 | **Your harness may have been lying since Week 2** |
| F13 | Cryptography for TLS & identity | 29–30 | `gatekeep`; mTLS between components |
| F14 | Partitioning & distributed data | 27, 30 | The vocabulary for your sharding design doc |
| F15 | AWS core services | 33–34 | **AWS is 48.4% of the skills backend postings name** |
| F16 | Event time, watermarks & the Dataflow model | 36–37 | Level 9. The most misunderstood topic in streaming |

---

**F1 · CPU memory hierarchy · W1–2 · 6h**
📖 **Bryant & O'Hallaron, *CS:APP* 3rd ed. — §6.2–6.4 only.** Skip §6.1.
🛠 **E1:** traverse a 256MB array with strides 1…4096, time each, plot. **Derive your L1/L2/L3 sizes from your own plot**, then check `lscpu`. If the plot has no steps your timing is wrong — fix it, because every number this year rests on measuring correctly.

**F2 · OS: processes, scheduling & isolation · W3–4 · 6h**
📖 **OSTEP ch. 4–7** (free). Plus **Linux cgroups v2 kernel docs — `memory` and `cpu` controllers** (`memory.max` vs `memory.high` precisely), and **NCC Group, "Understanding and Hardening Linux Containers"** — the namespace-escape sections.
🛠 **E2:** measure context-switch cost, two threads pinned to one core over a pipe, then to different cores. Explain the difference. Then **set a 100MB `memory.max`, run a memory bomb inside, and show the OOM kill happening *inside* the cgroup while the host is fine** — with the `dmesg` line.

**F3 · OS: virtual memory & TLB · W5–6 · 6h**
📖 **OSTEP ch. 13–16, 18–19.** Ch. 19 is the one that matters.
🛠 **E3:** demonstrate TLB thrashing — a program whose only change is page-touching order, with a large runtime gap at constant work. Report `dTLB-load-misses` for both. Then compute: **at your measured per-worker RSS, how many workers fit before you are paging?**

**F4 · TCP, UDP & network behaviour · W7–9 · 9h**
📖 **Kurose & Ross, *Computer Networking* 8th ed. — ch. 3 in full.** The most valuable chapter in the book. · **Fall & Stevens, *TCP/IP Illustrated Vol. 1* — ch. 13, 14, 15.** · **Grigorik, *High Performance Browser Networking* — ch. 1–4** (free at hpbn.co).
🛠 **E4:** capture a real gRPC connection with `tcpdump`, annotate **by hand** in Wireshark — handshake, initial cwnd, slow-start, exit, one provoked retransmission (`tc netem loss`). Then explain, in writing, what happens to your shard-handoff protocol on a link with 200ms RTT and 1% loss.

**F5 · Cache-conscious data layout · W10–12 · 9h**
📖 **Drepper, "What Every Programmer Should Know About Memory" — §3 in full, §6.2–6.4.** Skip §4–5.
🛠 **E5:** AoS→SoA on your operator batch format. Measure wall time, `L1-dcache-load-misses`, `LLC-load-misses`. **Then predict in writing, before running it, what `__builtin_prefetch` in the aggregation loop will do.** Commit the prediction, then test. Being wrong is normal; not recording the prediction wastes the lesson.

**F6 · Transactions & isolation · W13–15 · 6h**
📖 **Kleppmann, *DDIA* — ch. 7 in full.** Write skew and phantoms especially. · **Berenson, Bernstein, Gray et al., "A Critique of ANSI SQL Isolation Levels" (1995).** · **Kleppmann's "Hermitage" repo — run it against Postgres yourself.**
🛠 **E6:** from memory, the four anomalies with a concrete two-transaction interleaving each, and which isolation levels prevent which. One page. **You use this directly in Level 11.**

**F7 · JVM: memory model, GC & virtual threads · W14–16 · 9h** ☕
📖 **Goetz et al., *Java Concurrency in Practice* — ch. 3, 5, 10, 11.** · **Shipilëv's "JVM Anatomy Quarks"** — the allocation and GC entries. The best JVM performance writing that exists. · **JEP 444 (Virtual Threads)** and **JEP 442 (FFM API).**
🛠 **E7:** take your Level-4 operator loop and reduce its allocation rate to zero in the steady state, proven with `async-profiler -e alloc`. **Then write one page: why your first version allocated, what the JIT did and did not do for you, and where escape analysis failed.** *(This is the exercise that turns "I know Java" into "I know the JVM," which is the difference in a 52.7% skill.)*

**F8 · Probability & distributed randomness · W17–18 · 5h**
📖 **Mitzenmacher & Upfal, *Probability and Computing* — ch. 5 (balls into bins), §14.1 (power of two choices).** Ch. 5 is exactly your shard-distribution problem.
🛠 **E8:** simulate 10,000 shards into 12 workers with 1 / 10 / 100 / 500 virtual nodes each. **Plot the max-load-to-mean ratio.** Compare your empirical curves to the theoretical `log n / log log n` result and explain any gap.

**F9 · Consensus, CAP & consistency models · W19–21 · 7h**
📖 **Ongaro & Ousterhout, Raft — the EXTENDED version, §5 in full, §6 carefully.** · **DDIA ch. 8 and ch. 9 in full.** · **Jepsen's consistency model map** — one page, memorise the hierarchy. · **Kleppmann, "How to do distributed locking"** and antirez's reply. Both.
🛠 **E9:** place AION on the consistency map in writing, component by component — what is linearizable (shard assignment), what is eventual (job status, metrics), and **what a job is actually promised.** **This becomes ADR-0003.**

**F10 · Performance measurement & optimisation · W21–22 · 5h**
📖 **CS:APP ch. 5 in full** (what the compiler will and will not do for you), **§6.4–6.6.** · **Gregg, *Systems Performance* 2nd ed. — ch. 6 §6.6, ch. 13.** Reference.
🛠 **E10:** optimise one `aion-kernels` function through five stages. Each: `perf record` top-5 symbols, wall time, cache-miss rate, **and one sentence naming the mechanism.** Unattributable stages marked "unattributed" rather than explained away.

**F11 · Formal methods, lite · W23–25 · 5h** *(Ramadan-reduced — reading, not grinding)*
📖 **Hillel Wayne, `learntla.com`** — free, the best on-ramp. · **Newcombe et al., "How AWS Uses Formal Methods" (CACM 2015)** — read first, to understand why the hours are worth it.
🛠 **E11:** the Level 6.2 deliverable — spec the barrier protocol, model-check the exactly-once safety invariant, find one real design bug.

**F12 · Latency measurement done correctly · W28 · 3h**
📖 **Gil Tene, "How NOT to Measure Latency"** — in full. · **Dean & Barroso, "The Tail at Scale" (CACM 2013)** — eight pages, in full.
🛠 **E12: 🔴 audit your own harness.** If it sends the next event only after the previous is acknowledged, it has coordinated omission and **every latency number in this repository is optimistic.** Fix it, **re-run every benchmark**, put the before/after in `bench/RESULTS.md`. *"I found coordinated omission in my own harness and re-measured six months of results"* is one of the strongest sentences you can say in an interview.

**F13 · Cryptography for TLS & identity · W29–30 · 4h**
📖 **Aumasson, *Serious Cryptography* 2nd ed. — ch. 1, 3, 9, 10, 11.** · **RFC 8446 §2 only** (TLS 1.3 overview, six pages).
🛠 **E13:** capture a TLS 1.3 handshake, annotate every message against RFC 8446 §2. Then in writing: what mTLS adds, what is verified on each side, and **what happens when a worker's certificate expires at 03:00 on a Saturday.**

**F14 · Partitioning & distributed data · W27, 30 · 5h**
📖 **DDIA ch. 6 in full** (partitioning, rebalancing, request routing), then **ch. 8** — unreliable clocks and process pauses, which is exactly what you inject in Week 41.
🛠 **E14:** write your sharding design doc in ch. 6's vocabulary. Then the hard question: **what is your equivalent of a secondary index, given that a job's state is partitioned by a key the query may not use?**

**F15 · AWS core services · W33–34 · 6h**
📖 **Skip courses.** Free AWS Skill Builder for gaps only; learn the rest by building Week 34's infrastructure. Cover exactly: **IAM** (roles vs users, assume-role, least privilege, **OIDC federation**) · **VPC** (subnets, SGs vs NACLs) · **S3** (consistency, storage classes, lifecycle, prefix scaling) · **EC2** (t4g free tier) · **CloudWatch** (metrics, alarms, the $1 billing alarm). Nothing else. **Do not study for a certification.**
🛠 **E15:** write the checkpoint-store S3 IAM policy **by hand from the docs**, least privilege, and verify with the IAM policy simulator that it permits exactly what you intend and nothing more.

**F16 · Event time, watermarks & the Dataflow model · W36–37 · 6h**
📖 **Akidau et al., "The Dataflow Model" (VLDB 2015)** — the definitive treatment. · **Akidau, "Streaming 101 and 102"** — read first, it is the accessible version. · **DDIA ch. 11's time-reasoning section.**
🛠 **E16:** measure the **real** lateness distribution in GH Archive — how far out of order do genuine GitHub events arrive? Plot it. Then choose your allowed-lateness window **from that plot** and write down what fraction of events your choice discards.

## Deliberately NOT here
**Compilers and language theory** (interesting, and it is what a SQL layer would become — see the cut list) · **full Byzantine fault tolerance** (AION's failure model is crash-recovery, and knowing why is worth more than a half-finished PBFT) · **machine learning** (there is none in this project, deliberately) · **a fifth language** · **certifications** (AWS SAA is 40h to close a gap Week 34 closes better, with a running system as evidence instead of a badge).

---
---

# 🎯 TRACK I — The Interview Machine

> **Daily from Week 1.** 8h/week to Week 39 (**5.5h DSA + 2.5h system design**), **12h/week from Week 40.** Never batched. Never skipped.
>
> You can build every level of AION and still be rejected in a 45-minute phone screen. **This is the track that cannot be crammed.**

## What this is for, and the ratio that governs it

| Round | Named in backend postings |
|---|---|
| **System design** | **76.3%** |
| Algorithms / DSA | 18.3% |

**System design is therefore a first-class thread from Week 1, not a Level-7 afterthought.** That is the single biggest structural change from the plan this replaces.

**But DSA is a gate, and you are right that the bar has risen.** Frequency is irrelevant when 100% of the loops behind those postings contain two coding rounds, and Google and Meta now routinely ask problems that would have been "hard" three years ago. So DSA gets ~300h aimed at **hard-problem fluency**, not pattern coverage.

**It is not competitive programming.** Your Codeforces rating is a calibration instrument, not a goal. **The target: solve a medium-hard problem you have not seen, correctly, in 25 minutes, while talking.** The last three words are the part most people skip and the part that fails loops.

## Volume

| Period | Weeks | DSA | Design | Total |
|---|---|---|---|---|
| Levels 0–5 | 1–22 | 5.5 | 2.5 | 176 |
| Level 6 (Ramadan) | 23–26 | 3.5 | 1.5 | 20 |
| Levels 7–9 | 27–39 | 5.5 | 2.5 | 100 |
| Levels 10–12 | 40–52 | 7 | 5 | 156 |

**≈ 450 hours: ~300 DSA, ~150 system design. Target: 600 problems, 20 system designs, 12+ full timed loops.**

**Do not chase the count.** A problem you solved by opening the editorial after eight minutes did not happen. A problem you failed and rebuilt from scratch two days later counts double.

## Sources

| Source | For | How |
|---|---|---|
| **NeetCode 150 / 250** | The pattern spine, W1–17 | In order, grouped by pattern. Do not skip the easy ones. |
| **LeetCode, company-tagged** | W18–52 | Filter by your seven targets, last 6 months. Premium is worth $35 for two months before a loop. |
| **Codeforces Div 2 A–D** | Weekly, all year | Rated when it fits, virtual when it does not. Band 1400 → 1900. |
| **Codeforces EDU (ITMO)** | Segment trees W31–32, suffix structures W35 | The best free structured material for these. |
| **Laaksonen, *Competitive Programmer's Handbook*** (free) | Reference | **Ch. 7** (DP), **ch. 9** (range queries), **ch. 13–15** (graphs), **ch. 26** (probability). |
| **Skiena, *Algorithm Design Manual* 3rd ed.** | The *why* | **Ch. 8** (DP), **ch. 9** (intractability and reductions — supports W18). |
| **Alex Xu, *System Design Interview* Vol. 1 & 2** | System design | You own both. The weekly design curriculum below is built on them. |
| **`interviewing.io` / Pramp** | Mocks | Free peer mocks. **One paid mock with a real FAANG engineer around W30 if affordable.** |

## 🔗 The AION ↔ Track I map — where the tracks compound

| Weeks | Level | Systems work | DSA patterns | System design |
|---|---|---|---|---|
| 1–2 | L0 | Cache layout, working-set sweeps | Arrays, hashing, prefix sums, two pointers | Estimation module; the numbers to memorise |
| 3–4 | L1 | Batch-size tuning, windowing | **Binary search on the answer** — batch tuning literally is this. Monotonic stack | URL shortener · rate limiter |
| 5–9 | L2 | Partitioned log, consumer groups | Graph BFS/DFS, linked lists, trees, heaps, LRU design | **Distributed message queue** · notification system |
| 10–13 | L3 | LSM, Bloom filters, compaction | **Trees and BSTs, heaps and top-K, tries** — you built these under production constraints | **Key-value store** · distributed cache |
| 14–17 | L4 | Operator DAG, scheduling | **DP** (1-D, 2-D, knapsack), greedy | **Job scheduler** · metrics pipeline |
| 18–22 | L5 | Raft, consistent hashing, rebalancing | **Union-find**, reductions and NP-hardness (W18 = three written reductions), bit manipulation | **Distributed lock service** · sharded database |
| 23–26 | L6 | Barrier protocol, model checking | **Backtracking, state-space search** *(Ramadan: review only)* | Review only |
| 27–30 | L7 | Scheduling under load, shedding | **Heaps and priority queues, sliding window** (rate limiting *is* one), advanced graphs | **Rate limiter** · analytics pipeline |
| 31–35 | L8 | Quotas, fair sharing, isolation | DP and greedy, segment trees, Fenwick, binary lifting, strings | **Multi-tenant SaaS** · quota and fair-share system |
| 36–39 | L9 | Watermarks, sketches, serving | **Probability and expectation**, reservoir sampling, HyperLogLog | **Real-time leaderboard** · **time-series database** |
| 40–52 | L10–12 | — | Volume under time pressure, company-tagged sets | Full 45-min designs, one per week, recorded |

⚠️ **Where the tracks do NOT meet:** string algorithms (KMP, Z-function, suffix automata), combinatorics, number theory and geometry get **zero** reinforcement from AION. **These are where you will be weakest** — weeks 34–35 and the W43 weak-area blitz exist for them, and the disconnection is a reason to do them more carefully, not less.

## 🔴 The failure log — the part that actually produces improvement

Solving problems does not make you better. **Reviewing failures does.** `dsa/FAILURES.md`, an entry every time you miss the time box or solve with the wrong approach.

```
## <date> · <link> · <topic>
**Time box:** 25 min. **Outcome:** failed / solved at 41 min / wrong approach
**What I tried:** one sentence
**Why it failed:** be specific — "didn't see it was a graph problem" is a different bug
  from "saw it was a graph problem and implemented BFS wrong"
**The insight I was missing:** one sentence
**Category:** recognition / approach / implementation / speed / edge cases
**Re-solve due:** <date + 3 days>
```

**The category field is the whole point.** After thirty entries, **count them:**

| Mostly… | Means | Do |
|---|---|---|
| **recognition** | Need breadth | More problems, more varied |
| **approach** | Need depth | Slow down; work the reasoning, not the code |
| **implementation** | Need reps | Re-solve; do not move on |
| **speed** | Knowledge is fine | Timed sets, virtual contests |
| **edge cases** | Process problem | Write test cases *before* code, every time |

**Do the count in the rest weeks — W13, W26, W39, W48.** Twenty minutes, and it redirects the next quarter. Most people never do it and spend a year fixing the wrong thing.

**Re-solve discipline:** every failed problem re-solved from scratch three days later, without looking at your previous solution. **The highest-return habit in the track and the easiest to skip.**

## Time boxes

| Difficulty | Box | On expiry |
|---|---|---|
| Easy | 15 min | Read the solution, log as failure, re-solve from scratch same day |
| Medium | 25 min | Read the *approach only*, retry 15 min, then full solution. Log |
| Hard | 45 min | Same protocol |

**Never exceed the box.** An hour spent stuck teaches less than reading the solution and re-solving twice.

## The system design curriculum — 2.5h/week from Week 1

**Twenty designs.** One every two to three weeks to Week 39, then one per week timed at 45 minutes.

**Each produces a full design doc:** Summary · Context · Goals · **Non-Goals** · Proposal · **Alternatives Considered (minimum three)** · Risks · Rollout · Operational Impact.

**The 45-minute structure:** 0–5 requirements, functional **and** non-functional, written on the board · 5–10 estimation (**round aggressively, show the arithmetic**) · 10–15 API and data model · 15–25 high-level design (**state your choices as choices**) · 25–40 deep dive (where the grade is decided) · 40–45 failure modes and 10×.

> **The single highest-leverage habit: say the words "I'm optimising for X, which costs me Y." Every time.**

**Numbers to memorise:**
```
1 machine:  ~10-50k QPS simple requests · 64-256GB RAM · 10-40 cores
Postgres:   ~5-50k simple QPS · ~1-5k writes/s with fsync
Redis:      ~100k-1M ops/s single instance (single-threaded!)
Kafka:      ~100k-1M msg/s per broker (small, batched)
NVMe:       ~500k-1M IOPS · 3-7 GB/s        Network: 10 Gbps = 1.25 GB/s
RTT:        same-AZ ~0.3-0.5ms · cross-region 30-150ms
Time:       1 day ≈ 10^5 s · 1M req/day ≈ 12 QPS · 1B req/day ≈ 12k QPS
```

> **🔴 Your unusual advantage.** Most candidates answer system design from books. **You can answer from a system you built, operated, and broke twenty times on purpose.** Asked to design a metrics pipeline or a job scheduler or a message queue, do not recite — say *"I did this; here is what I chose and here is the number I measured."* **Practise that move deliberately in the W44 mock**, because it does not happen naturally under pressure.

## Mock schedule

| When | What |
|---|---|
| **W21** | First human mock + **the Raft Figure 8 whiteboard test** (a checkable gate, not a formality) |
| W26, W30, W34 | Monthly mock, one round |
| **W30** | **One paid mock with a real FAANG engineer**, if affordable |
| **W38** | **Full timed loop #1 — 4 rounds in one day** |
| W40–52 | Weekly, escalating to two/week from W49 |

**A "full timed loop" means** two 45-minute coding rounds with a human, one 45-minute system design, one 30-minute behavioural, **in a single day** with realistic breaks. **Not four sessions across a week.** The exhaustion is what you are training for.

**Speak while you solve, always, including alone.** The most common cause of a failed coding round in a candidate who *can* solve the problem is silence.

## 📈 TRACK I EXIT CRITERIA
- [ ] 600+ problems, **≥70% solved unaided within 25 minutes**
- [ ] A random unseen Medium, **narrated**, in ≤25 min, ≥80% of the time
- [ ] Complexity stated before code, every time
- [ ] 25+ Hard problems · **failure-log review queue empty** · Codeforces ≥1750
- [ ] **20 system designs as written docs** and 20 more practised verbally
- [ ] **12+ full timed loops** · 14 behavioural stories on video

---
---

# 🧭 TRACK J — Craft, Career & Visibility

> What separates an L4 from an L5 is not knowing more systems facts. It is **judgement, communication and impact beyond your own keyboard.**
> **5h/week, 8h from Week 40. One artifact every two weeks.**

## J.1 — Design docs and ADRs

**The design doc is the unit of senior technical work.** Promotion at every large company is decided by written artifacts.

```markdown
# [Title]                    **Author** · **Status** · **Date**
## 1. Summary            3 sentences. A reader should be able to stop here.
## 2. Context & Problem  What exists, what's broken — WITH DATA. Graphs, numbers, incident links.
## 3. Goals              Bulleted, measurable.
## 4. Non-Goals          Explicit. Where scope creep dies. The most under-used section.
## 5. Proposal           Design. Diagrams. Data model. Sequence for the critical paths.
## 6. Alternatives Considered   ← THE SECTION THAT DISTINGUISHES SENIOR WRITING
                         Minimum three. "Do nothing" is always one of them.
## 7. Risks & Failure Modes     Blast radius. Detection. Mitigation.
## 8. Rollout Plan       Phases. Flags. ROLLBACK AT EVERY STEP.
## 9. Operational Impact Monitoring, alerts, runbook, on-call burden, cost.
## 10. Open Questions
```

**The two sections that separate senior from mid: *Alternatives Considered* and *Non-Goals*.** A doc without a serious alternatives section reads as advocacy, not engineering.

**Already scheduled:** `event-model.md` (W4) · `delivery-semantics.md` (W9) · `durability-contract.md` (W12) · `job-model.md` (W17) · `consistency.md` (W22) · `time-model.md` (W38) · `threat-model.md` (W32) · `gcp-window.md` (W34) · `slo.md` (W35) · `isolation-level.md` (W44). **Ten, plus ten ADRs in W50.**

## J.2 — Writing and visibility — the multiplier

**Post the results, not the progress.** Not "day 47 of my coding journey" — the findings. You will have unusually good ones:

| Week | The post | Why it travels |
|---|---|---|
| 13 | **"I killed my state backend a thousand times and injected fsync failures at the syscall level"** | The torture harness, and the fsyncgate lesson |
| 17 | **"My Java stream processor was 15× slower than my C++ one. It wasn't Java's fault."** | Allocation rate, escape analysis, off-heap. A very common misconception, corrected with data |
| 22 | **"Consistent hashing told me who owned the shard. It didn't stop two workers believing it."** | Why hashing is not agreement — a distinction many engineers have never made explicit |
| 26 | 🔴 **"Three bugs in my stream processor that no test suite would have caught"** | DST + the barrier-phase kills. **Front-page candidate** |
| 28 | 🔴 **"I found coordinated omission in my own benchmark harness and re-measured six months of results"** | **Engineers at exactly your target companies will read this** |
| 30 | 🔴 **"Overload in a stateful stream processor is checkpoint-mediated. Here's the death spiral."** | **A genuinely novel finding with a graph. Front-page candidate** |
| 35 | **"One tenant's infinite loop stalled another tenant's exactly-once guarantee"** | A failure mode you can only find by building both halves |
| 43 | 🔴 **"What exactly-once actually costs: the curve nobody publishes"** | **The artifact. Flink has done this for a decade and never published the tradeoff.** The single most valuable thing you write this year |

Own the domain; cross-post to Hacker News, Lobsters, `r/dataengineering`, `r/programming`. **One post reaching the HN front page generates more inbound recruiting than 200 applications.**

**Give one talk.** A Cairo meetup counts. Explaining the barrier protocol out loud will expose every gap in your understanding, which is why it is valuable.

## J.3 — Open source

**A merged PR into a project people have heard of beats three personal projects**, because someone with commit rights judged your code good enough to ship.

**The ladder:** use it seriously → fix the docs where they confused you (gets you through the CLA/CI process once) → a `good first issue` → **a bug you personally hit** → **a bug found by fuzzing** (maintainers love a minimal reproducer) → a feature, after discussing design in an issue first.

**Highest-leverage targets given AION:** **Apache Flink** (you will read its source all year and you *will* find documentation gaps and edge cases — and a Flink contribution is a perfect CV line for this project) · **Apache Arrow** (columnar formats, and it is C++ and Java, both of yours) · **Redpanda** or **franz-go** (Kafka ecosystem, Go) · **Debezium** · **RocksDB.** **One meaningful PR to Flink is worth twenty to a random repo**, because it is *exactly* the domain you are claiming. **Budget: Levels 7–9. Target: 3+ merged, one non-trivial.**

## J.4 — 🔴 The referral problem, and how to solve it from Egypt

**Harder than the degree question.** A cold application from Cairo to a Dublin req competes with hundreds of in-region applicants needing no sponsorship. **A referred application is read by a human. A cold one frequently is not.**

**The mistake:** waiting until Week 40 and messaging strangers. A referral is someone putting their reputation on your application. **Nobody does that for someone who appeared in their inbox last Tuesday.**

### ⏰ The pipeline opens Week 18.

**Channel 1 — the Egyptian engineering diaspora. Highest return.** Substantial numbers at Google Dublin and Zurich, Meta London, Amazon Dublin, Microsoft. Find them via LinkedIn alumni search on your university, then other Egyptian universities, filtered by company. **They were where you are. They are disproportionately willing to help and disproportionately under-asked.**

Not "can you refer me":

> I'm a backend engineer in Cairo building a distributed stream-processing platform — Raft for shard assignment, barrier-based checkpointing for exactly-once, running over the GitHub Archive firehose. I'm implementing the checkpoint protocol now and I'd value fifteen minutes of your view on [one specific technical question you genuinely have]. No obligation and no ask beyond that.

Then have the conversation, be interesting, follow up two months later with what you built. **The referral, if it comes, comes on its own.** **Target: 3 conversations/month from Week 18. By Week 40 that is 15–18 people who know what you are building.**

**Channel 2 — build in public** (§J.2). **Channel 3 — OSS, especially Flink** (§J.3). **Channel 4 — the technical report** (W43); most candidates have a GitHub link, **a 20-page report with benchmarks and an honest limitations section is a different object and it gets forwarded.** **Channel 5 — meetups and CFPs**; submit the exactly-once-cost talk for 2028. The CFP is networking even when rejected.

**The direct ask, Week 40, to people you have known for months:**

> I'm applying to [specific role, specific office] this week. Here's the project [link] and my CV. If you're comfortable referring me I'd be grateful; if not, no problem at all — and I'd still value knowing whether the CV reads clearly to someone inside.

**The second half matters.** It gives them an out that is not a rejection, and it frequently produces useful feedback from people who will not refer you.

## J.5 — 🔴 The Logic Leap track: sourcing what a solo project cannot

**Mentoring is 36.6% of backend postings. Communication 34.4%. Collaboration 31.2%. Leadership 17.2%.** AION demonstrates **none** of them, and you chose — correctly — to source them from your job. **But that only works if it is deliberate.** Left to chance you will arrive at Week 44 with fourteen stories, twelve of them about a solo project, and interviewers notice.

**One hour a week of Track J is reserved for this. Seek these out at work, in this order:**

| Quarter | What to deliberately do at Logic Leap | The story it becomes |
|---|---|---|
| **W1–13** | **Ask to review other people's PRs**, seriously, weekly. Leave the kind of comment you would want. | *"Improving code quality without authority"* · Code review 16.1% |
| **W14–26** | **Write one design doc for real work** and circulate it before implementing. Use the §J.1 template. | *"Aligning people on a technical decision"* · the Alternatives section is the artifact |
| **W14–26** | **Onboard or unblock someone** — a new joiner, an intern, a colleague on unfamiliar code. Track what they were stuck on. | *"Mentoring"* — the single largest soft gap at 36.6% |
| **W27–39** | **Take one cross-team dependency end to end** — something needing another team's input, where you drive the conversation. | *"Cross-functional work"* 16.1% · *"Working across teams"* 59.1% of duties |
| **W27–39** | **Disagree with a senior person, in writing, with data**, and handle the outcome either way. | *"Disagreeing with a senior person"* — a required behavioural story you cannot fabricate |
| **W40–52** | **Lead one thing end to end**: scope, plan, delegate a piece, ship, own the outcome. | *"Leading a project"* 30.1% of duties · *"Leadership"* 17.2% |

**Log each in `career/LOGICLEAP.md` as it happens, with dates and specifics.** You will not remember the details in month eleven, and vague behavioural answers are the most common way strong technical candidates fail loops.

> **And the warning:** 🔴 **do not let AION eclipse your paid work.** At least four of your fourteen behavioural stories must come from Logic Leap, and an interviewer who hears twelve stories about a side project and two about the job you were paid to do draws a conclusion you do not want.

## J.6 — Target companies

Applications go to **specific offices**, not "Google."

| Company | Offices | Note |
|---|---|---|
| **Google** | Dublin, Zurich, London, Munich, **Warsaw** | Zurich strongest and hardest. **Warsaw more accessible.** |
| **Meta** | London, Dublin | London is the main EMEA engineering site |
| **Amazon / AWS** | Dublin, London, Berlin, Luxembourg | Most reqs, **most accessible tier-1 entry.** Kinesis/MSK/EMR map onto AION directly |
| **Microsoft** | Dublin, London, Cambridge, Munich, **Cairo** | 🔴 **The only tier-1 with engineering in Cairo. Apply there in Week 40 regardless** — a local tier-1 role is a legitimate route to an internal transfer |
| **Stripe** | Dublin, London | Backend-heavy, **values written communication — your report and ADRs are unusually well-matched** |
| **Datadog** | Paris, Dublin | **Ingest and query at enormous scale — your Level 7 and 9 work is their product domain** |
| **Cloudflare** | London, Lisbon | Systems-heavy; their data pipeline work is directly adjacent |

**Second tier, same practice, easier entry — and several of these are *literally* your project's domain:** 🔴 **Confluent** (Kafka; London — you will have implemented their problem) · **Databricks** (Amsterdam; Spark Structured Streaming) · **ClickHouse** (Amsterdam/remote) · **Redpanda** (remote) · **Materialize**, **RisingWave**, **StarTree**, **Imply** (streaming/OLAP, mostly remote) · **Snowflake** (Berlin/Dublin) · **Elastic** (Amsterdam, distributed, remote-first) · **Grafana Labs** (remote-first; observability) · **MongoDB** (Dublin) · **Bloomberg** (London, large C++ and Java) · **Booking.com**, **Adyen**, **Klarna** infra (Amsterdam/Stockholm) · **Canonical** (fully remote, hires globally, heavy systems interviews).

> **The streaming-and-data-infrastructure tier is your single best-fit market and it is unusually remote-friendly.** Confluent, Redpanda, Materialize, ClickHouse and StarTree are all small enough that a candidate who built a stream processor and published an exactly-once cost curve gets read by an engineer rather than a keyword filter.

**Calibration tier** (W30–39, no cooldown risk): Instabug, Swvl, Halan, Paymob, MaxAB (Cairo); Careem, Talabat, Tabby (Gulf); any European startup with a real systems interview.

## J.7 — CV versions

**One page. Every line traceable to something in the repo the day you write it.**

**Structure:** 1. Name, GitHub, **"Cairo, Egypt · open to relocation · requires EU/UK sponsorship"** · 2. Two-line summary · 3. 🔴 **SELECTED PROJECT — AION, 5–7 bullets. The largest section, ABOVE employment** · 4. Experience — Logic Leap, 3–4 bullets, quantified · 5. Skills, keyword-matched to the corpus · 6. **Education — one line, last.**

> **The degree line:** *"BSc Management Information Systems, [University], [year]."* **No parenthetical. No "(self-taught in CS)". No apologetic adjective.** The project section made the argument; restating it next to the degree draws attention to the anxiety rather than the evidence.

**Every bullet is X-Y-Z:** *"Accomplished [X] as measured by [Y], by doing [Z]."*

**CV v1 — W13** *(not for applying; it exists so an unexpected opportunity does not find you writing a CV in a panic)*
> **AION — distributed stream-processing platform** · C++, Java, Go, Python · [repo]
> · Built a SIMD-based ingest path processing **500k real events/sec/core** from the GitHub Archive firehose, verified against a DuckDB ground truth over 100M events.
> · Implemented a partitioned-log ingest layer surviving **500 forced consumer rebalances with zero event loss**, with measured partition skew on real production-shaped data.
> · Built a C++ LSM state backend with a torture harness performing **1,000 kill cycles and syscall-level `fsync`/torn-write fault injection, zero invariant violations**, supporting consistent snapshots under concurrent writes.

**CV v2 — W26**
> · Implemented **Raft** for shard assignment across a 12-worker cluster; a coordinator killed mid-rebalance leaves **zero shards unassigned or double-assigned**, with fencing tokens preventing expired-lease writes.
> · Implemented **distributed exactly-once processing** via asynchronous barrier snapshotting (Chandy–Lamport / Flink algorithm); verified by killing workers at **each of five distinct barrier-protocol phases across 500 seeds per phase**.
> · Built a deterministic simulation harness running **10,000 seeded fault schedules nightly**; found 3 correctness bugs no conventional test caught, each reproducible from a seed integer. Model-checked the barrier protocol in TLA+.

**CV v3 — W34** *(the first version that survives a tier-1 screen — send to your three strongest contacts for feedback, not for referral)*
> · **Measured and published the exactly-once cost curve** — throughput and p99 with and without exactly-once across checkpoint intervals and state sizes, with recovery time overlaid. No equivalent public measurement exists.
> · Held cluster goodput at **Y% of capacity under 5× offered load** via credit-based backpressure and priority shedding, against X% for the naive scheduler; identified and broke a checkpoint-mediated overload death spiral.
> · Built multi-tenant isolation where **one tenant at 100× load degrades others' p99 by <10%**; sandboxed untrusted job code in separate processes with cgroup and seccomp backstops.
> · Deployed across Oracle Cloud (ARM) and AWS at **$0/month**; ported the C++ kernels to aarch64 and published the per-component delta. Full stack in Terraform; CI authenticates via OIDC with zero long-lived credentials.

**CV v4 — W40** *(the one you apply with)*
> · Benchmarked head-to-head against **Apache Flink** on identical hardware, data and semantics; attributed every component of the performance gap to a named mechanism with supporting profiles.
> · Ran a chaos programme: **20+ injected incidents** (worker kill mid-checkpoint, asymmetric partition, clock skew, S3 loss during checkpoint) each with alerting, root cause and a runbook; separately reproduced 6 famous public outages locally with verified fixes.

## J.8 — Applications

| Weeks | Volume | Targets |
|---|---|---|
| 30–39 | 2–3/month | **Calibration tier only** |
| 40–43 | 12/week (48) | **Tier-1 EMEA first**, plus **Confluent, Databricks, ClickHouse, Redpanda, Materialize** — your best-fit tier |
| 44–47 | 12/week (48) | Remaining tier-1 and second tier |
| 49–52 | 8/week | Fill gaps; the pipeline is mostly conversion now |

**≈150 applications.** Fewer than 100 under-samples a noisy process; more than 250 is applying without targeting.

**Every application logged** in `career/APPLICATIONS.md` — date, company, office, role, referral (y/n, by whom), response, stage, outcome. **You cannot reconstruct this later and you need it to compute response rate and stage conversion.**

**Sequence your loops:** 3–4 companies you care less about *first*. Your fifth loop is dramatically better than your first. **Then overlap the real ones so offers arrive within ~2 weeks** — competing offers are the only real leverage.

### 🚨 If the response rate is low (checked W43, ~48 out)
**Below 10%, stop and diagnose before sending more with the same CV.** In order:
1. **Targeting** — reqs wanting 5+ years will not respond regardless. Check the level distribution.
2. **Sponsorship filter** — some reqs auto-reject sponsorship needs. **Invisible, and not about you.**
3. **The top third of the CV** — recruiters read the top third. If it does not contain **Java (52.7%), distributed systems (48.4%), AWS (48.4%), Python (43%), Go (37.6%), Kubernetes (30.1%), Kafka (20.4%)**, it is miscalibrated. **The barrier protocol and Raft are interview content; the top of the CV is screening surface.**
4. **Referral ratio** — under a third referred? The fix is §J.4, not more applications.

**Fix in Week 44. Do not respond to a low response rate by increasing volume** — that converts a fixable problem into a burned target list.

## J.9 — Negotiation

Weeks 50–52. **The highest hourly-rate work you will ever do.**
1. **Never give a number first**, including on the recruiter's first call. *"I'd like to focus on whether this is the right fit; I'm confident we can align on compensation"* is a complete answer and it is expected.
2. **Competing offers are the only real leverage.** Hence overlapping loops.
3. **Negotiate the whole package:** base · equity **and its vesting schedule** · sign-on (most flexible) · **level — worth more than any of the above over three years** · start date.
4. 🔴 **Applying from Egypt to a European role creates an anchoring risk.** Recruiters may benchmark against Egyptian salaries. **Do not accept that framing** — compensation is for the role in that location. Know your target level's `levels.fyi` number for that company and office **before the first call.**
5. **Read: Haseeb Qureshi, "Ten Rules for Negotiating a Job Offer."** Plausibly a five-figure return for two hours.
6. Be gracious. You will work with these people.

## J.10 — What the loops look like (verify with your recruiter)

| Company | Loop |
|---|---|
| **Google** | Phone screen → 2–3 coding, 1 system design, 1 Googleyness & Leadership. Then **hiring committee and team matching** — a strong loop can stall at team match. **Normal, not a rejection.** |
| **Meta** | Phone screen (**2 problems in 45 min — speed matters more here than anywhere**) → 2 coding, 1 system design, 1 behavioural |
| **Amazon** | OA → 4–5 rounds, **every round includes Leadership Principle questions.** The **Bar Raiser** is external with veto power |
| **Microsoft** | Coding + design + an "as appropriate" round with a senior leader |
| **Confluent / Databricks / ClickHouse / Redpanda** | **Practical over puzzle:** debugging unfamiliar code, extending real code, deep systems discussion, plus design. **AION prepares you for these better than any other project could** |
| **Stripe / Datadog / Cloudflare** | Practical: an integration exercise, extending real code, system design. **This roadmap prepares you unusually well** |

**Leveling:** L3/E3 (new grad) → **L4/E4 (2–5 yrs)** → **L5/E5 (5+ yrs, owns ambiguous projects end to end — where system design decides it).** **Interview for the level your evidence supports.** Being under-levelled costs years of compensation; push back with evidence if the loop went well.

---
---

# 📅 The 52-Week Calendar

**Standard week: 32h = 19 Depth / 8 Interview / 3 Fundamentals / 2 Craft.**
**From W40: 32h = 12 Depth / 12 Interview / 8 Career.**
Your shape: **4h weekdays + 6h each weekend day.** Weekdays are DSA, system design, fundamentals and reading. **The weekend blocks are where AION is built** — nothing hard is built in 45-minute slices.

**Budget:** 52 × 32 = 1,664 nominal. −88 (four rest weeks at 10h) −36 (Ramadan W23–25 at 20h) −12 (two Eid weeks at 26h) = **1,528 hours.** The table below sums to **1,536**, because four weeks are scheduled at 34h; applying their cut lines brings it back to 1,528. **Those 8 hours are the only slack in the calendar that is not a buffer week — do not spend them twice.**

⚠️ **Four weeks exceed budget: W4, W17, W31, W40.** Each has a stated cut line below the table. **Do not compress estimates — drop the task.**

| Wk | Starts | Lvl | Depth focus | Milestone / Flagship | I | F | J | Tot |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-07 | 0 | Repo, CI, toolchains (C++/Java/Go/Py), `latency-lab` | — | 8 | F1 3 | 2 | 32 |
| 2 | 09-14 | 0 | **🔴 SCALE RISK: real decode rate? worker ceiling?** `bench/`, `sickbay` | `SCALE-RISK.md` **go/no-go** | 8 | F1 3 | 2 | 32 |
| 3 | 09-21 | 1 | **Naive pipeline fails 4 ways on real GH Archive.** SIMD decode, arenas | — | 8 | F2 3 | 2 | 32 |
| 4 | 09-28 | 1 | Windowing, bounded state, **DuckDB ground-truth check**, 10× replay | **A0** | 8 | F2 3 | 2 | **34** ⚠ |
| 5 | 10-05 | 2 | `c10k-arena` — seven concurrency models incl. virtual threads | — | 8 | F3 3 | 2 | 32 |
| 6 | 10-12 | 2 | Kafka internals; partitioning, keying, **the real skew in GH data** | — | 8 | F3 3 | 2 | 32 |
| 7 | 10-19 | 2 | **Consumer groups; kill mid-batch → duplicates, then gaps** | — | 8 | F4 3 | 2 | 32 |
| 8 | 10-26 | 2 | `aiond/gateway`: submit API, OpenAPI, gRPC, protobuf versioning | — | 8 | F4 3 | 2 | 32 |
| 9 | 11-02 | 2 | 500 forced rebalances, zero loss; lag chart; delivery-semantics doc | **A1** | 8 | F4 3 | 2 | 32 |
| 10 | 11-09 | 3 | **`statestore`** — WAL, CRC framing, SSTs, compaction, Bloom | — | 8 | F5 3 | 2 | 32 |
| 11 | 11-16 | 3 | **Torture harness** + `LD_PRELOAD` injection · **injectable-port refactor** | **#1** | 8 | F5 3 | 2 | 32 |
| 12 | 11-23 | 3 | **Consistent snapshot under concurrent writes**; snapshot-cost curve | **A2** | 8 | F5 3 | **CV v1** 2 | 32 |
| 13 | 11-30 | — | 🛌 **REST** — exit check, checkpoint, **failure-category count** | — | 6 | — | 2 | 10 |
| 14 | 12-07 | 4 | ☕ **Java ramp: naive port is 15× slower — find out why.** AWS signup | — | 8 | F6/F7 3 | 2 | 32 |
| 15 | 12-14 | 4 | Off-heap, zero-allocation hot loop, `async-profiler` · **the SDK** | — | 8 | F7 3 | 2 | 32 |
| 16 | 12-21 | 4 | Operator DAG, chaining, virtual-thread scheduler, JNI/FFM boundary | — | 8 | F7 3 | 2 | 32 |
| 17 | 12-28 | 4 | SDK usability test on a human; failure isolation; **ADR-0001** | **A3** | 8 | F8 3 | 2 | **34** ⚠ |
| 18 | 2027-01-04 | 5 | Consistent hashing vs mod-N **with state**; vnodes | **🤝 REFERRALS OPEN** | 8 | F8 3 | 2 | 32 |
| 19 | 01-11 | 5 | Raft: elections, log replication, 1,000-run no-split-brain test | — | 8 | F9 3 | 2 | 32 |
| 20 | 01-18 | 5 | Raft: **Figure 8**, commit rules, membership, ReadIndex | **#2** | 8 | F9 3 | 2 | 32 |
| 21 | 01-25 | 5 | `aiond/coord`; fencing tokens · **🎯 Figure 8 whiteboard + first mock** | — | 8 | F9/F10 3 | 2 | 32 |
| 22 | 02-01 | 5 | 🔧 **BUFFER + pre-Ramadan pull-forward:** rebalance-under-load, Will Wilson talk, Chandy–Lamport + Carbone papers, learntla setup | **A4** | 8 | F10 3 | 2 | 32 |
| 23 | 02-08 | 6 | 🌙 Barrier snapshotting; alignment; the deadlock | — | 5 | F11 2 | 2 | **20** |
| 24 | 02-15 | 6 | 🌙 `aionsim`: sim clock/network/disk/scheduler + **5-phase kill** | — | 5 | F11 2 | 2 | **20** |
| 25 | 02-22 | 6 | 🌙 10k seeds, **find ≥3 bugs**; TLA+ on the barrier protocol | **#3** | 5 | F11 2 | **CV v2** 2 | **20** |
| 26 | 03-01 | — | 🛌 **REST** — **🚩 HALF-YEAR GATE**, retrospective, category count | **A5** | 5 | — | 3 | 10 |
| 27 | 03-08 | 7 | 🌙 Eid. Backpressure, credit-based flow control | — | 6 | F14 2 | 1 | **26** |
| 28 | 03-15 | 7 | **`overload`** — goodput curves, the **checkpoint death spiral** · **🔴 F12 audit** | **#4** | 8 | F12 3 | 2 | 32 |
| 29 | 03-22 | 7 | Shedding by key/priority, adaptive checkpoint interval, metastable | — | 8 | F13 3 | 2 | 32 |
| 30 | 03-29 | 7 | **k8s: 12-worker cluster, rolling restart zero loss, 3am dashboard** · **first calibration applications** | **A6** | 8 | F13/F14 3 | 2 | 32 |
| 31 | 04-05 | 8 | **The four attacks all work.** Sandbox: process, cgroups, seccomp | — | 8 | F15 3 | 2 | **34** ⚠ |
| 32 | 04-12 | 8 | **Non-yielding operator stalls another tenant's barrier** → deadline metering | **#5** | 8 | F15 3 | 2 | 32 |
| 33 | 04-19 | 8 | Multi-tenancy: quotas, fair queuing, shuffle sharding · **Oracle, aarch64** | — | 8 | F15 3 | 2 | 32 |
| 34 | 04-26 | 8 | `costwatch`, `gatekeep`, GCP window, **🔴 `sim-fidelity.md`** | — | 8 | F16 3 | **CV v3** 3 | 32 |
| 35 | 05-03 | 8 | 🔧 **BUFFER** + SLOs + S3 checkpoints + cost/recovery two-axis curve · **🚩 TWO-THIRDS GATE** | **A7** | 8 | — | 3 | 32 |
| 36 | 05-10 | 9 | Serving path; MVCC reads; read/write isolation | — | 8 | F16 3 | 2 | 32 |
| 37 | 05-17 | 9 | 🌙 Eid al-Adha. **Watermarks; the "current total" problem** | — | 6 | F16 2 | 1 | **26** |
| 38 | 05-24 | 9 | Event time, real lateness distribution, side outputs · **LOOP #1** | **A8** | 8 | — | 2 | 32 |
| 39 | 05-31 | — | 🛌 **REST** — **application-readiness gate**, **Final Gauntlet**, category count | — | 6 | — | 2 | 10 |
| 40 | 06-07 | 10 | **🎯 CV v4 · FIRST 12 APPLICATIONS · referral activation** · chaos framework | — | 12 | 0 | 8 | **34** ⚠ |
| 41 | 06-14 | 10 | **`flinkbench`** — the head-to-head, attributed · **LOOP #2** | **#7** | 12 | 0 | 8 | 32 |
| 42 | 06-21 | 10 | **`incident-lab`**: 20 incidents + **clock skew** + cold start from S3 | **#8** | 12 | 0 | 8 | 32 |
| 43 | 06-28 | 10 | 🔧 **BUFFER** + **#6 the exactly-once cost curve, final** + report + **🚨 response-rate gate** | **#6** | 12 | 0 | 8 | 32 |
| 44 | 07-05 | 11 | Public API, OpenAPI, pagination, idempotency, Postgres metadata · **LOOP #3** | — | 12 | 0 | 8 | 32 |
| 45 | 07-12 | 11 | **`pgshift`** — 50M-row migration under live checkpointing · **LOOP #4** | — | 12 | 0 | 8 | 32 |
| 46 | 07-19 | 11 | Dashboard: 2,000 WebSockets, backpressure, jitter · **LOOP #5** | — | 12 | 0 | 8 | 32 |
| 47 | 07-26 | 11 | `admin` + **runbook tested by a peer** + supply chain · **LOOP #6** | **A9** | 12 | 0 | 8 | 32 |
| 48 | 08-02 | — | 🛌 **REST** — interview prep only, pipeline review, category count | — | 6 | — | 4 | 10 |
| 49 | 08-09 | 12 | **README final, TOUR.md, benchmarks final** · **LOOPS #7–8** | — | 14 | 0 | 8 | 32 |
| 50 | 08-16 | 12 | **10 ADRs · LIMITATIONS.md · COMPARISON.md** · **LOOPS #9–10** | — | 14 | 0 | 8 | 32 |
| 51 | 08-23 | 12 | **RETROSPECTIVE.md** + the talk/post · **LOOP #11** | — | 14 | 0 | 8 | 32 |
| 52 | 08-30 | 12 | Final state, re-record the talk, **`docs/NEXT.md`** · **LOOP #12** | **A10** | 14 | 0 | 8 | 32 |

## Cut lines for the four over-budget weeks
- **W4 (34h):** drop the 10× replay test to a single 2× run (−2h). **Do not cut the DuckDB ground-truth check** — it is the only thing proving your engine is correct at all.
- **W17 (34h):** the SDK usability test moves to W18 (−2h). **Do not cut ADR-0001** — the JNI/process asymmetry is your first real architecture decision and it is interview material all year.
- **W31 (34h):** attack 4 (credential exfiltration) becomes a written analysis rather than a live reproduction (−2h). **Do not cut attack 3** — the barrier-stall attack is the one that is specific to your system.
- **W40 (34h):** the chaos framework slips to W41 (−2h). 🔴 **The application tasks CANNOT be cut.** If you cut them, the Week-40 decision never actually happens and you find yourself applying in Week 50 with no pipeline.

---
---

# ✂️ The Cut Order

**You chose full scope with a named cut order. This is it.** Cut in this sequence, top first. **Never cut out of order, and never cut silently — every cut gets a line in `docs/LIMITATIONS.md` saying what was dropped and why.**

| # | What gets cut | Costs you | Why it's first |
|---|---|---|---|
| 1 | **SQL-over-streams** (already a non-goal — this is a reminder not to re-add it) | Nothing. It is a compiler project wearing a streaming costume | It is the most seductive scope creep in this domain |
| 2 | **The dashboard's visual polish** (W46) | Nothing measurable. Keep the WebSocket backpressure work, which is the actual engineering | Frontend is ~0% of your postings |
| 3 | **`pgshift`** (W45) | PostgreSQL evidence drops from strong to adequate | Postgres is 19.4%; you still have the metadata store and migrations from W44 |
| 4 | **Unaligned checkpoints** (keep aligned only, W23) | A paragraph in the write-up, and one curve loses a line | Aligned exactly-once is the milestone; unaligned is the refinement |
| 5 | **The GCP 200-node window** (W34) | Simulator validation at scale; `sim-fidelity.md` gets weaker and you must say so | Costs credibility, not correctness |
| 6 | **The second attack family in the sandbox** and shuffle sharding (W33) | Multi-tenancy evidence thins; keep quotas and fair queuing | Quotas alone still demonstrate the shell |
| 7 | **ARM port and the x86/ARM analysis** (W33) | A nice free result and one blog post | Genuinely optional |
| 8 | **Two of the six reproduced outages** (W42) | `incident-lab` weakens but survives at four | The 20 self-inflicted incidents matter more than the famous ones |
| 9 | **Level 9's materialized-view layer** — serve from the last checkpoint only | Freshness. The watermark-consistency lesson survives | The interesting insight is the "current total" problem, and you keep that |

## 🔴 What is NEVER cut

| Never cut | Because |
|---|---|
| **Exactly-once and the barrier protocol (L6)** | It is the project. Without it AION is a toy and the whole year's argument collapses |
| **The DuckDB ground-truth check (W4)** | It is the only proof your engine computes correct answers |
| **The operational shell — k8s, observability, on-call, Terraform (L7, L8, L10)** | **The shell alone is 15.1% coverage; the core alone is 6.5%.** The shell is what the screen reads |
| **Java (L4)** | +14.1 points. The single most valuable decision in the plan |
| **The Track I hours** | The only track that degrades irreversibly. A missed week is not recoverable by working harder later |
| **Applications from W40** | The plan's entire purpose. Everything else is instrumental |
| **The Logic Leap track (J.5)** | 36.6% + 34.4% + 31.2% + 17.2% of postings, and nothing else in the plan touches them |

**The decision is forced at three gates: Week 26 (half-year), Week 35 (two-thirds), Week 43.** At each, count how many weeks behind you are and cut that many items off the top of the list. **Cutting at a gate is a decision. Discovering in Week 47 that you cannot finish is a failure.**

---
---

# 📊 ASSESSMENT: The Three Proofs

You do not "finish" a level. You **prove** it, three ways.

| Proof | What | Why |
|---|---|---|
| **1. The Exam** | The written questions at the level's end, no notes, timed | Retrieval under pressure — the interview condition |
| **2. The Artifact** | The project, exit criteria met, **numbers published** | That you can actually build it |
| **3. The Teach-Back** | **Explain the level's hardest concept to a camera in 10 minutes, no notes, with a diagram** | **The strictest test there is. You cannot fake teaching.** |

**Fail any of the three and the level is not done.**

## The Final Gauntlet — one week, Week 39, before your first real loop

| Day | Challenge | Pass condition |
|---|---|---|
| 1 | 4 LeetCode Mediums + 1 Hard, timed, **narrated aloud, recorded** | 4/5 unaided within time |
| 2 | 2 system designs, 45 min each, on video | Both hit the rubric |
| 3 | **Debug a sabotaged AION** — have a peer break it without telling you what | Root cause in <45 min **with evidence** |
| 4 | All 14 behavioural stories on video, cold | Each ≤90s, quantified, first person, **≥4 from Logic Leap** |
| 5 | Write a full design doc for a **novel** problem in 3 hours | All 10 sections, **3+ real alternatives** |
| 6 | **Teach-back: the barrier protocol · the exactly-once cost curve · deterministic simulation.** 10 min each | No notes, correct, with diagrams |
| 7 | Watch every video from days 1–6 and **grade yourself against the rubrics** | Honest scoring |

**Pass = ready to interview. Fail any day → that is your next two weeks.**

## The spaced-repetition deck

**One card per non-obvious fact, written by you.** Downloaded decks do not work; cards you write do. Target ~600. Categories: latency numbers · isolation-level anomalies · Raft rules · the five barrier-protocol kill phases · JVM GC and allocation facts · algorithm complexities · Linux commands and what they *answer* · failure modes · estimation constants · **your own measured numbers.**

**15 min/day, non-negotiable.** The difference between knowing something in month 3 and knowing it in month 12 when the interview happens.

---
---

# 📈 TRACKING & RE-PLANNING

Three artifacts, four rituals, ~45 min/week. **If it costs more, cut it down rather than abandoning it** — a degraded log you keep beats a perfect log you stop.

| File | Contains | Written |
|---|---|---|
| `LOG.md` | Hours by track, task outcomes, weekly review, monthly checkpoint | Daily + Sunday |
| `dsa/FAILURES.md` | Every failed problem, in the Track I format | As it happens |
| `career/APPLICATIONS.md` | Every application, with response and stage | As it happens |
| `career/LOGICLEAP.md` | The mentoring/leadership situations from J.5, dated | As they happen |

## Daily — 2 minutes
```
2026-09-23 · D:4.0 I:1.5 F:0 J:0 · SIMD decode at 380k ev/s, target 500k;
             arena allocator done. (nlohmann→simdjson port cost ~1h more than planned)
```
**Log the hours you actually worked, not the hours you sat at the desk.** The Week-51 retrospective is only useful if this is honest, and its value is telling you your real estimation ratio — which you cannot learn from inflated data.

## Weekly review — Sunday, 30 minutes

1. **Hours by track vs budget.** A deficit up to 3h is noise. **Three consecutive deficit weeks is a signal.**
2. **Which tasks met their acceptance criterion?** Met / not met. **"Partially" is not a category — force it.** A benchmark that runs but has no hardware counter **did not meet its criterion.**
3. **Which targets did you set before measuring, and what did you get?** **Both numbers, always.**
4. **What did not finish, and does it block next week?** Blocks → top of next week, something drops. Does not → the buffer list for W22/W35/W43. **Never silently carry unfinished work forward** — that is how a two-week slip becomes invisible until month eight.
5. **Interview track:** attempted / solved / failed / re-solved, **and system design docs written.** 15 attempted with 0 failure entries means the problems were too easy or you are not logging.
6. **Logic Leap:** did anything happen this week worth a J.5 entry? **If four weeks pass with nothing, go and create the situation.**
7. **One sentence: the biggest risk to the next four weeks.** A specific thing, not a feeling.

## Monthly checkpoint — at each level boundary

1. **Level exit criteria, one at a time. Met, or waived in writing with a reason. No third option.**
2. **Hours: month actual vs budget, and cumulative.** The cumulative number is the one that matters.
3. 🔴 **Is the repository interview-ready RIGHT NOW?** Three checks, *performed*:
   - Does `make bootstrap` work on a clean clone? **Actually run it.**
   - Does the README describe what exists rather than what is planned?
   - **Can you speak for 45 minutes about it, today, without preparation?**

   If any is no, fixing it is next week's top priority. **The plan is built so you can stop at any week and still be a coherent candidate, and this check is the only thing enforcing it.**
4. **The corpus gaps** — Java 52.7%, AWS 48.4%, distributed systems 48.4%, Kubernetes 30.1%, Kafka 20.4%, observability 22.6%, on-call 17.2%, PostgreSQL 19.4%. One line each: closed / in progress / not started, **and what the evidence is. Not what you read. What is running.**
5. 🔴 **Failure-category count** from `dsa/FAILURES.md`. **The most valuable twenty minutes in the checkpoint, and the one most likely to be skipped.**
6. **From Week 18:** referral pipeline — conversations this month, people who now know what you are building.
7. **From Week 40:** applications sent, responses, response rate, stage conversion, what is stalled.
8. **One paragraph: is the plan still right?** Not "am I on schedule" — whether it still describes the correct work.

### The mid-year review — Week 26
Three extra questions:
1. **Given six months of real data on your pace, does the second half fit?** If not, **go to §XV and cut now.** Cutting in month 6 is a decision; discovering it in month 11 is a failure. And **reconsider the Extended Track** — 18 months is legitimate; a rushed Level 7–10 is not.
2. **Is AION still the right project?** You are permitted to conclude it is not. What transfers — the Raft work, the state backend, the simulator, the operational shell — is most of it.
3. **Has anything about your situation changed?** Job, hours, health, finances. The plan assumes 32h/week for 52 weeks. If that assumption broke, re-cut rather than failing against a fiction.

## 🚨 Re-plan triggers

**Re-planning is not failure; it is the plan working.**

| Trigger | Response |
|---|---|
| **Cumulative deficit > 40h** | **Cut scope in the §XV order. Do not compress estimates.** |
| **All buffer weeks gone before W35** | Estimates are systematically wrong. **Recompute Levels 9–12 with your measured ratio from `LOG.md`**, and **seriously consider the Extended Track.** |
| **Two consecutive checkpoints where the repo is not interview-ready** | **Stop feature work entirely for one week.** README, build, demo. Overrides everything. |
| **Three consecutive weeks of Interview track under 5h** | The project is eating the track you explicitly protected. **Invert the week: interview first, project with what is left, for two weeks.** |
| **The Week-2 scale spike fails** — decode too slow, or you cannot run enough workers | **Decide in Week 2.** Substitute: fewer workers (6–8) with the simulator carrying scale from month one, stated in the README as the primary limitation. **Do not carry the uncertainty forward.** |
| **Java ramp overruns Week 15** | You are 15h down and Level 4 is the wrong place to be behind. Cut the SDK usability test and operator chaining to W18; **do not cut the zero-allocation exercise**, which is the thing that makes Java evidence real. |
| **A level runs 2+ weeks over** | Do not compress the next. Take it from the next buffer week and cut the top item in §XV. |
| **Response rate <10% at W43** | Diagnose per §J.8 **before** sending more. |
| 🔴 **You have not opened the repo in 7 days** | **The most important trigger and the easiest to ignore.** Do not restart at 32 hours. One 2-hour session, then one 4-hour session, then resume. **Restarting at full intensity after a break is how a one-week gap becomes a one-month one.** |

## What does NOT trigger a re-plan

- **A bad week.** Noise.
- **A target you missed.** Targets set before measurement are estimates. **Record both numbers and move on.**
- **A negative result.** Being 3× slower than Flink, or a sim-fidelity divergence larger than you hoped, **are results.** They get written up and become interview material.
- **Feeling behind.** Check `LOG.md`.
- 🔴 **A better project idea.** It will happen, probably around Level 4 and again around Level 8. **The answer is no.** Write it in `docs/IDEAS.md` and continue. **You have already changed spine twice, at week zero, when it was free. Changing again in month four costs you the accumulated depth that is the entire point of a single system.**

---
---

# 💼 RÉSUMÉ & GITHUB TRANSLATION

## Six pinned repos, chosen for legibility

```
📌 aion              Distributed stream-processing platform · C++/Java/Go/Python
                     Exactly-once over 6B real GitHub events, Raft shard assignment,
                     LSM state backend, multi-tenant sandboxed jobs
                     ★ architecture diagram + headline numbers + the prior-art and
                       scale statements, all in the first screen

📌 exactly-once-cost What does exactly-once actually cost you?
                     ★ THE curve. Throughput/p99/recovery vs checkpoint interval and
                       state size. Flink has never published this.

📌 aionsim           Deterministic simulation · worker death at 5 barrier phases
                     ★ "three bugs no test suite would have caught," with the seeds

📌 statestore        C++ LSM state backend + the torture harness
                     ★ 1,000 kill cycles, syscall-level fsync injection, zero violations

📌 flinkbench        AION vs Apache Flink, same data, same semantics, same hardware
                     ★ "3.2× slower, and here are the four reasons in order of size"

📌 incident-lab      Six famous outages reproduced locally, with verified fixes
                     ★ the table of outages is the hook
```

**Every README, first screen:** one sentence saying what it is · an architecture diagram · **the headline number or chart** · `make demo`.
**Profile README:** three sentences about what you work on, then the six with their numbers. **No badge walls. No language-percentage charts.**

## The interview answer this buys you

> *"Tell me about the most technically challenging thing you've built."*

A 45-minute answer with: an architecture diagram you can draw from memory · **three specific bugs and how a simulator you wrote found them** · measured numbers and where the bottleneck is · a defensible reason for every technology choice · **the alternatives you rejected, written as ADRs** · **an honest comparison to Flink, which solved this a decade ago** · and **a retrospective with measured estimate-versus-actual**, which tells an interviewer more about how you would estimate *their* project than anything else in the repo.

---
---

# 📚 THE LIBRARY

## The spine — with the chapters that matter

| # | Book | When | Chapters |
|---|---|---|---|
| 1 | **Kleppmann, *DDIA*** *(you own it)* | Throughout | **Ch. 3** (storage, L3) · **6** (partitioning, L5) · **7** (transactions, F6) · **8** (partial failure — **the theoretical spine**, L5) · **9** (consensus, L5) · **11** (streams — **the most important chapter for this project**, L2/L6/L9) |
| 2 | **Alex Xu, *System Design Interview* Vol. 1 & 2** *(you own them)* | Track I, weekly | **Vol 1 ch. 1** (estimation) · **4** (rate limiting) · **5** (consistent hashing) · **6, 8** (cache, CDN) · **11** (queues) · **Vol 2** for applied designs |
| 3 | **Bryant & O'Hallaron, *CS:APP* 3rd ed.** | L0, L3, F10 | **§6.2–6.4** (memory hierarchy) · **ch. 5** (optimising performance) |
| 4 | **Arpaci-Dusseau, *OSTEP*** *(free)* | L1, L2 | **Ch. 4–7** (processes) · **13–16, 18–19** (VM, TLB) · **25–33** (concurrency) |
| 5 | **Goetz et al., *Java Concurrency in Practice*** | L4, F7 | **Ch. 3, 5, 10, 11.** Skip the dated executor material |
| 6 | **Petrov, *Database Internals*** | L3 | **Ch. 2–5.** Part I is the best storage-engine treatment in print. Skip Part II |
| 7 | **Kurose & Ross, *Computer Networking* 8th ed.** | L2 | **Ch. 3 in full.** The most valuable chapter in the book |
| 8 | **Fall & Stevens, *TCP/IP Illustrated Vol. 1*** | L2 | **Ch. 13, 14, 15** |
| 9 | **Nygard, *Release It!* 2nd ed.** | L7, L10 | **The origin of circuit breaker and bulkhead. The most relevant book to Levels 7 and 10** |
| 10 | **Google, *SRE* + *SRE Workbook*** *(free)* | L7–L10 | **SRE ch. 3, 4, 6, 21, 22** (ch. 22 is the most valuable) + **Workbook ch. 5** |
| 11 | **Majors, Fong-Jones, Miranda, *Observability Engineering*** | L7 | **Ch. 1–6** |
| 12 | **Lukša, *Kubernetes in Action* 2nd ed.** | L7 | **Ch. 1–7, 12, 17** |
| 13 | **Aumasson, *Serious Cryptography* 2nd ed.** | L8 | **Ch. 1, 3, 9, 10, 11** |
| 14 | **Gregg, *Systems Performance* 2nd ed.** | L0, F10 | **Ch. 6 §6.6, ch. 13.** Reference |
| 15 | **Mitzenmacher & Upfal, *Probability and Computing*** | F8 | **Ch. 5** (balls into bins — literally your shard-distribution problem), **§14.1** |
| 16 | **Ousterhout, *A Philosophy of Software Design*** | L3 | Short, sharp, and more right than *Clean Code* where they disagree |
| 17 | **Skiena, *Algorithm Design Manual* 3rd ed.** | L5, Track I | **Ch. 8** (DP), **ch. 9** (intractability and reductions) |
| 18 | **Laaksonen, *Competitive Programmer's Handbook*** *(free)* | Track I | **Ch. 7, 9, 13–15, 26** |
| 19 | **Winters, Manshreck, Wright, *Software Engineering at Google*** *(free)* | Track J | **Ch. 9** (code review), **11–14** (testing at scale) |
| 20 | **Akidau, Chernyak, Lax, *Streaming Systems*** | L1, L6, L9 | 🔴 **The book for this project.** Ch. 1–4 (streaming, windows, watermarks) and ch. 5 (exactly-once). Read ch. 1–2 in Week 3 |

## The papers — cited at first assignment, one page of notes each

| Paper | Week | Why |
|---|---|---|
| **Langdale & Lemire, "Parsing Gigabytes of JSON per Second"** | W3 | It will change how you think about parsing |
| **Jay Kreps, "The Log"** | W6 | The unifying abstraction. Read fully |
| **"Bitcask: A Log-Structured Hash Table"** | W10 | 6 pages, your v1 target |
| **Rebello et al., "Can Applications Recover from fsync Failures?"** + the PostgreSQL fsyncgate thread | W10 | Why you cannot retry fsync |
| **Athanassoulis et al., "The RUM Conjecture"** | W10 | Read/Update/Memory — pick two |
| **O'Neil et al., "The Log-Structured Merge-Tree" (1996)** | W11 | The original LSM paper |
| **JEP 444 (Virtual Threads)** and Shipilëv's "JVM Anatomy Quarks" | W14 | The Java level's foundation |
| **Karger et al., "Consistent Hashing and Random Trees" (STOC 1997)** | W18 | The original |
| **Ongaro & Ousterhout, Raft — EXTENDED version** | W19 | §5 in full, §6 carefully |
| **Ongaro's PhD thesis** | W20 | Log compaction, membership changes |
| **Kleppmann, "How to do distributed locking"** + antirez's reply | W21 | Fencing tokens. Read both |
| **Chandy & Lamport, "Distributed Snapshots" (1985)** | W22 | 🔴 Eleven pages. One of the clearest papers in the field |
| **Carbone et al., "Lightweight Asynchronous Snapshots for Distributed Dataflows" (2015)** | W22 | 🔴 **The paper you implement** |
| **Carbone et al., "State Management in Apache Flink" (VLDB 2017)** | W23 | How Flink actually does it |
| **Zhou et al., "FoundationDB" (SIGMOD 2021) §4** | W24 | Simulation |
| **Newcombe et al., "How AWS Uses Formal Methods" (CACM 2015)** | W25 | Why TLA+ is worth your hours |
| **Dean & Barroso, "The Tail at Scale" (CACM 2013)** | W28 | Eight pages. The basis of Level 7 |
| **Bronson et al., "Metastable Failures" (HotOS 2021)** | W29 | The failure class nobody names |
| **Mitzenmacher, "The Power of Two Choices: A Survey"** | W29 | Placement |
| **Douceur, "The Sybil Attack"** *(optional)* | W32 | If you extend the tenant model |
| **Akidau et al., "The Dataflow Model" (VLDB 2015)** | W36 | 🔴 The definitive treatment of event time and watermarks |
| **Lamport, "Time, Clocks, and the Ordering of Events" (1978)** | W42 | Eight pages, most cited in the field |
| **Berenson, Bernstein, Gray et al., "A Critique of ANSI SQL Isolation Levels" (1995)** | F6 | Named the anomalies the standard forgot |

**For each: a one-page summary** — what problem, what was the key insight, what did they give up, what would you do differently in 2027, what system today embodies it. **Twenty-three one-pagers is a genuinely impressive public artifact.**

## Free reference
`aws.amazon.com/builders-library` **(read all ~20 across Levels 7–10)** · `k8s.af` **(read 10)** · `jepsen.io/analyses` · `sre.google/books` · `learntla.com` · `github.com/danluu/post-mortems` · `nightlies.apache.org/flink/flink-docs-stable/` (the Flink docs are genuinely excellent and you will read them all year) · `use-the-index-luke.com` · `hpbn.co` · `neetcode.io` · `levels.fyi` · `brooker.co.za`

## People
Martin Kleppmann · **Marc Brooker** (`brooker.co.za` — the best working systems writer today) · **Aleksey Shipilëv** (JVM) · Brendan Gregg · Julia Evans · Dan Luu · Kyle Kingsbury (aphyr) · Hillel Wayne · Charity Majors · Alex Petrov · **Tyler Akidau** (streaming) · **the TigerBeetle team** (simulation) · Gergely Orosz

---
---

# ✅ THE COMPLETE PROJECT CATALOG

**🚩 flagship · ⭐ core · ○ optional**

## Level 0 — Machine, Memory & Measurement
- [ ] ⭐ `latency-lab` — your machine's latency ladder, cache sizes derived from your own plot
- [ ] ⭐ `aionlab/bench` — the **open-loop** harness with `perf` integration, used all year
- [ ] ⭐ `sickbay` — 8 injectable pathologies including a JVM GC pause, median diagnosis <10 min
- [ ] ⭐ **`docs/SCALE-RISK.md`** — real decode rate, worker ceiling, disk rate, **the signed go/no-go**

### Level 1 — The Firehose
- [ ] ⭐ **A0** — SIMD selective decode, arena allocation, batching, tumbling windows
- [ ] ⭐ **≥500k events/sec/core**, with the gap from naive attributed to named mechanisms
- [ ] ⭐ **🔴 Correctness against a DuckDB ground truth over 100M real events, matching exactly**
- [ ] ⭐ Malformed and schema-drifted events counted and categorised, never silently dropped
- [ ] ⭐ Keeps up with a 10× replay, lag flat

### Level 2 — The Log & Concurrency
- [ ] ⭐ `c10k-arena` — seven models to 50k connections, **goroutines vs virtual threads**, and under cgroup throttling
- [ ] ⭐ **A1** — partitioned ingest, **500 forced rebalances with zero loss**, duplicate rate counted
- [ ] ⭐ Real partition skew in GH Archive measured and reported
- [ ] ⭐ `aiond/gateway` — submit API, OpenAPI, gRPC with versioned protobuf, old-client compatibility test
- [ ] ⭐ `docs/design/delivery-semantics.md` — what you guarantee today and what L6 changes

### Level 3 — State
- [ ] 🚩 **#1 `statestore`** + torture harness — **1,000 kill cycles, `LD_PRELOAD` injection, zero violations**
- [ ] ⭐ **A2** — LSM with WAL, CRC framing, SSTs, compaction, Bloom filters
- [ ] ⭐ **🔴 Consistent snapshot under concurrent writes, property-tested.** L6 is impossible without it
- [ ] ⭐ Snapshot cost vs state size — the first half of the recovery curve
- [ ] ⭐ Injectable-port refactor: **core suite in <2s with no real time, disk or network**
- [ ] ⭐ `docs/design/durability-contract.md`

### Level 4 — The Runtime & SDK ☕
- [ ] ⭐ **A3** — Java 21 runtime, operator DAG, virtual-thread scheduler, the SDK
- [ ] ⭐ **Bit-identical results to the L1 hand-written pipeline** on 100M real events
- [ ] ⭐ **Zero allocation in the steady-state hot loop**, proven by `async-profiler`
- [ ] ⭐ Within 2× of C++ end-to-end, or a written explanation of why not
- [ ] ⭐ **ADR-0001** — JNI/FFM for trusted kernels, process isolation for untrusted code
- [ ] ⭐ Unserialisable lambda capture fails at **submit** time with a readable message
- [ ] ⭐ SDK usability test on a real human, sticking points recorded and fixed

### Level 5 — Distribution & Consensus
- [ ] 🚩 **#2 `raft`** — 1,000 elections no split-brain; 500 partition schedules, minority cannot commit
- [ ] ⭐ **The Figure 8 scenario as a deliberate test** — and drawable from memory in 5 minutes
- [ ] ⭐ ReadIndex / lease reads, with the latency difference measured
- [ ] ⭐ **A4** — coordinator killed mid-rebalance: **zero shards unassigned, zero double-assigned**
- [ ] ⭐ **Fencing tokens: the violation without, the fix with, same seed**
- [ ] ⭐ **Rebalance under load with state handoff: zero events lost, degraded window vs state size**
- [ ] ⭐ Consistent hashing vs mod-N; load variance at 1/10/100/500 vnodes
- [ ] ○ Gossip Glomers 1–4 (W22 buffer)

### Level 6 — Exactly-Once
- [ ] ⭐ **A5** — asynchronous barrier snapshotting; **worker killed at each of 5 phases, 500 seeds each**
- [ ] ⭐ **Idempotent sink** — with the non-idempotent failure demonstrated first
- [ ] ⭐ Incremental checkpoints on immutable SSTs; snapshot time vs state size, incremental vs full
- [ ] ⭐ **The alignment-under-backpressure deadlock reproduced, then fixed or bounded**
- [ ] 🚩 **#3 `aionsim`** — 7 simulated components, **10,000 seeds nightly**
- [ ] ⭐ **🔴 ≥3 real bugs found, each with its seed and trace, in the README**
- [ ] ⭐ TLA+ spec of the barrier protocol, **≥1 design bug found by TLC**; `tla-vs-dst.md`
- [ ] 🚩 **#6 part 1 — the exactly-once cost curve** (throughput/p99/recovery vs interval and state size)

### Level 7 — Overload, Backpressure & Kubernetes
- [ ] 🚩 **#4 `overload`** — **the goodput collapse curves, six strategies, one chart**
- [ ] ⭐ **🔴 The checkpoint death spiral demonstrated, then broken**
- [ ] ⭐ **A metastable failure reproduced then made impossible.** Two graphs
- [ ] ⭐ Stateful autoscaling: the scale-up cost curve showing where adding a worker hurts first
- [ ] ⭐ **A6** — 12-worker cluster on k3s; **rolling restart with zero events lost or duplicated**
- [ ] ⭐ Prometheus + Grafana with **the five streaming signals**; 3am dashboard; RCA in <5 min on video
- [ ] ⭐ **F12: the harness audit, and every benchmark re-run if it fails**

### Level 8 — Multi-Tenancy, Sandbox & Cloud
- [ ] 🚩 **#5 `sandbox`** — **all four attacks fail**, especially **the barrier-stalling non-yielding operator**
- [ ] ⭐ **A7** — one tenant at 100×, **others degrade <10%**; shuffle-sharding blast-radius chart
- [ ] ⭐ Per-tenant accounting reconciling to cluster CPU within 5%
- [ ] ⭐ **aarch64 port + per-component x86-vs-ARM delta**
- [ ] ⭐ `costwatch` — Terraform, hand-written IAM, **a tested billing alarm**, free-tier drift detection
- [ ] ⭐ `gatekeep` — mTLS, credential rotation, `gitleaks` in CI, expiry alert fast-forward test
- [ ] ⭐ **S3 checkpoint storage** + **the checkpoint interval plotted against BOTH recovery time and monthly cost**
- [ ] ⭐ 🔴 **`docs/analysis/sim-fidelity.md`** — real cluster vs simulation, and the GCP-window validation
- [ ] ⭐ **$0.00 verified and screenshotted, every month**
- [ ] ⭐ `docs/design/threat-model.md` — **including what you do NOT defend against**

### Level 9 — Serving & Query
- [ ] ⭐ **A8** — **p99 <50ms serving while ingest runs full rate; ingest degrades <5%**
- [ ] ⭐ **Watermark-consistent reads** — asserted by a test that fails under naive per-shard reads
- [ ] ⭐ Freshness vs consistency measured and plotted
- [ ] ⭐ **Real lateness distribution in GH Archive measured**, and the allowed-lateness window chosen from it
- [ ] ⭐ Side output for late events; **nothing silently dropped**
- [ ] ⭐ `docs/design/time-model.md` — what a query result actually means

### Level 10 — Operations, Chaos & On-Call
- [ ] 🚩 **#7 `flinkbench`** — head-to-head, **same semantics**, every gap component attributed
- [ ] 🚩 **#6 final** — the exactly-once cost curve and recovery-vs-state-size, on the real cluster
- [ ] 🚩 **#8 `incident-lab`** — **6+ famous outages reproduced with verified fixes**
- [ ] ⭐ **The seven-mechanisms synthesis essay.** Published
- [ ] ⭐ **20+ AION incidents**, each with alert, timeline, root cause, runbook
- [ ] ⭐ **The clock-skew incident** + the quarantine invariant
- [ ] ⭐ **Full-cluster cold start from S3 checkpoints, for real, timed**
- [ ] ⭐ `docs/REPORT.md` — 15–25 pages **with the limitations section**
- [ ] ⭐ **CV v4; 48 applications sent**

### Level 11 — Platform Completion
- [ ] ⭐ OpenAPI 3.1 with **CI drift detection** · versioning · keyset pagination + the offset benchmark · idempotency keys · RFC 9457 errors · **pinned old-client compatibility suite**
- [ ] ⭐ Postgres metadata store: migrations in git, reversible, Testcontainers in CI, `isolation-level.md`
- [ ] ⭐ `pgshift` — **50M rows under live checkpointing, zero errors, both graphs in the README**
- [ ] ⭐ Dashboard — **2,000 WebSockets, memory bound demonstrated, the jitter test**
- [ ] ⭐ `admin` + **the runbook tested by a peer**, sticking points recorded and fixed
- [ ] ⭐ SBOM, pinned deps, **CI fails on a critical CVE**

### Level 12 — Synthesis
- [ ] ⭐ README final, **tested on a human with a ten-minute timer** · `TOUR.md` · final diagram
- [ ] ⭐ **The 10 ADRs** · `LIMITATIONS.md` on the first screen · **`COMPARISON.md` vs Flink, Spark, Kafka Streams, Materialize, Arroyo**
- [ ] ⭐ **`RETROSPECTIVE.md`** — estimate vs actual per level, every pre-measurement target with both numbers
- [ ] ⭐ The talk or long-form post · **`docs/NEXT.md`**

### Cross-cutting
- [ ] ⭐ **600+ problems** with the failure log and category counts at W13/26/39/48
- [ ] ⭐ **20 system design docs** + 20 practised verbally · **12+ full timed loops**
- [ ] ⭐ **14 behavioural stories on video, ≥4 from Logic Leap**
- [ ] ⭐ **10 design docs · 23 paper one-pagers · 8 published posts · 3+ merged OSS PRs (ideally Flink) · 1 talk**
- [ ] ⭐ **4 CV versions in git history** · **~150 applications logged with response rate and stage conversion**
- [ ] ⭐ **`career/LOGICLEAP.md`** — the six deliberate mentoring/leadership situations, dated

---
---

# 🏁 THE FINAL READINESS CHECKLIST

## Can you build it?
- [ ] A decode path doing 500k real events/sec/core, verified correct against an independent engine
- [ ] A state backend that survives 1,000 kills and injected `fsync` failures
- [ ] A Java runtime with zero steady-state allocation, within 2× of C++
- [ ] Raft, with Figure 8 as a deliberate test and no split-brain in 1,000 runs
- [ ] **Exactly-once through worker death at every phase of the barrier protocol**
- [ ] A simulator that found three bugs your tests did not, each reproducible from an integer
- [ ] Goodput held at 5× offered load by shedding, not collapsing
- [ ] Multi-tenant isolation a hostile job cannot break
- [ ] A benchmark against Flink where you can explain every part of the gap

## Can you explain it?
- [ ] Why exactly-once *delivery* is impossible but exactly-once *processing* is not
- [ ] The three mechanisms exactly-once requires — and why naming only snapshots is the common error
- [ ] What alignment is, why it deadlocks under backpressure, and what unaligned checkpoints cost
- [ ] Why a consistent snapshot under concurrent writes made your storage choice a checkpointing choice
- [ ] Raft's Figure 8, at a whiteboard, in five minutes
- [ ] Why consistent hashing is not agreement, with AION's concrete failure
- [ ] Why your Java was 15× slower and why it was not Java's fault
- [ ] **The checkpoint-mediated overload death spiral**
- [ ] Coordinated omission, and why you re-measured six months of results
- [ ] Why p99 goes vertical at 90% utilisation
- [ ] What a watermark is and why "the current total" was meaningless without one
- [ ] **Why you would not use AION instead of Flink** — and what you learned by building it anyway

## Can you diagnose it?
- [ ] Root-cause a sabotaged cluster in under 45 minutes, with evidence
- [ ] Read a flame graph in 10 seconds and say what you would fix
- [ ] Given "p99 is 3s, CPU is 8%", name three causes and the command that distinguishes them
- [ ] Given green dashboards and wrong answers, **find the clock**
- [ ] Given an OOMKill at a 4GB limit with a 3GB heap, name four consumers of the difference

## Can you interview?
- [ ] 600+ problems, ≥70% unaided in 25 minutes
- [ ] A random Medium, **narrated**, in 25 minutes, on video, repeatedly
- [ ] **20 system designs**, 45 min each, hitting the rubric
- [ ] 14 behavioural stories, ≤90s, quantified, first person, **≥4 from Logic Leap**
- [ ] **12+ full timed loops** · **the Final Gauntlet passed**

## Do they know you exist?
- [ ] 6 pinned repos, each with a diagram and a headline number in the first screen
- [ ] 8+ technical posts published — **at least one about a result, not a tutorial**
- [ ] 3+ merged OSS PRs, one non-trivial, **ideally in Apache Flink**
- [ ] One talk given
- [ ] **15–18 people at target companies who know what you are building, from conversations that started in January**
- [ ] A CV where **every bullet has a number**

---

# 🎯 What success means on 2027-09-05

**Not an offer.** Offer timing is not under your control, the strongest window falls just past the end of this plan, and treating an offer as the criterion makes you optimise for the wrong things in Levels 9–11.

> **The criterion: you are a candidate who cannot be screened out on credentials, and cannot be caught out in a system design round.**

If that is true and you have no offer yet, **the plan worked and the timing has not resolved.** Execute `docs/NEXT.md` through October.

If it is not true, **`docs/RETROSPECTIVE.md` tells you which level to return to — with numbers rather than a feeling.**

---

# Closing

Three things decide whether this works.

**1. You must actually reproduce the failures.** The Walls are not flavour text. Reading "exactly-once is hard" produces a fact you will forget. Watching your own output gain duplicates when you kill a consumer, then lose events when you move the commit, produces an instinct you will have for twenty years. **The three you will remember longest:** the naive pipeline falling permanently behind the live firehose in Week 3 · killing a consumer mid-batch in Week 7 and deriving the entire delivery-semantics problem by hand · and the seed in Week 25 where a worker died between "snapshot complete" and "acknowledgement received" and your exactly-once guarantee quietly stopped being true.

**2. You must run all three tracks at once.** Depth without the interview track means nobody sees the depth. The interview track without depth gets you an L4 offer and a six-year stall. Craft without either is empty. **It is genuinely harder to run three tracks than one, and it is the reason most people who "study systems for a year" do not convert it into an offer.**

**3. You must ship publicly, and honestly.** The gap between *"I understand distributed systems"* and *"here is a stream processor running six billion real events, here is the exactly-once guarantee verified by killing workers at five distinct phases of the barrier protocol across ten thousand seeds, here are the three bugs my simulator found that my tests could not, here is what exactly-once actually costs measured as a curve that Flink's team has never published, here are the twenty incidents I caused on purpose, and here is the document listing everything this does not do"* — **that gap is the entire difference between a candidate and a hire.**

This is roughly **1,528 hours across twelve months.** The output is not "a person who finished a roadmap." The output is an engineer who has processed billions of real events through a system they wrote, made correctness survive machines dying at the worst possible moment, implemented Raft from the paper, built a simulator that kills workers inside a distributed protocol, measured what a guarantee costs, kept the whole thing standing at five times its capacity on hardware that costs nothing — **and can explain any of it at a whiteboard from memory, including the parts that do not work.**

There are not many of those.

**And the numbers say the two things that decide your outcome are the operational shell and the Java service — not which clever core you picked. Build the clever core anyway; it is what you will talk about for forty-five minutes. But never let it eat the shell.**

**Now go download one day of GitHub Archive, write the obvious pipeline, and watch it fall behind.**
