# ΚΗΡΥΞ · KERYX — The God-Level Roadmap

## From "backend engineer with one year of experience" → the engineer who gets handed the hardest distributed system in the company

**κῆρυξ** — *the herald.* The one who carries the message across, through hostile country, and is answerable for it arriving. The name is the thesis: this project is not about computing things. It is about **people reaching each other, and the message arriving — correctly, once, in order — when the machines and the companies in between are failing.**

**Built for one person:** Ziad Mostafa Elsaid · Cairo, Egypt · ~1 year at Logic Leap · BSc Management Information Systems · Codeforces 1450 (310+ problems) · Python, Go, Rust, C++, SQL · targeting backend and distributed-systems roles at Google, Meta, Amazon, Microsoft, Stripe, Cloudflare, Datadog, Confluent, Matrix/Element, Signal, Discord and their European offices.

**Week 1 begins Monday 2026-09-14. Week 52 ends Sunday 2027-09-12.**

> This is a **training program**, not a reading list. Every topic is entered through a **failure you reproduce before you are allowed the explanation.** Every project has **numeric exit criteria.** Every level ends with an **exam you pass or repeat.** Every level names its **DSA patterns** and its **system-design problem**, because the tracks compound. Every claim about the job market carries **its number, re-derived from your own dataset of 569 postings** — not quoted from an earlier draft.

---

## 📖 CONTENTS

| # | Section |
|---|---|
| **0** | [**The Spine Project — the idea, argued**](#part-0--the-spine-project-the-idea-argued) |
| I | [The Evidence Base — verified, with corrections](#part-i--the-evidence-base) |
| II | [KERYX — the full specification](#part-ii--keryx-the-specification) |
| III | [The Seven Decisions](#part-iii--the-seven-decisions) |
| IV | [The Eight Laws](#part-iv--the-eight-laws) |
| V | [The Learning System — three sources, five prompts](#part-v--the-learning-system) |
| VI | [The Course Atlas — every course, ranked by what it buys](#part-vi--the-course-atlas) |
| VII | [Every Topic From Every Roadmap, Ranked by the Data](#part-vii--every-topic-ranked-by-the-data) |
| VIII | [The Four Tracks](#part-viii--the-four-tracks) |
| IX | [The Level Map](#part-ix--the-level-map) |
| X | [**Levels 0–12 — the curriculum**](#-level-0--the-machine--the-measurement) |
| XI | [The Ten Flagships](#part-xi--the-ten-flagships) |
| XII | [Track I — The Interview Machine (DSA + System Design)](#part-xii--track-i--the-interview-machine) |
| XIII | [Track F — The Gap-Filling Curriculum](#part-xiii--track-f--the-gap-filling-curriculum) |
| XIV | [Track J — Craft, Career & Visibility](#part-xiv--track-j--craft-career--visibility) |
| XV | [The Library — books and papers, with the chapters that matter](#part-xv--the-library) |
| XVI | [The 52-Week Calendar](#part-xvi--the-52-week-calendar) |
| XVII | [The Cut Order & Re-Plan Triggers](#part-xvii--the-cut-order--re-plan-triggers) |
| XVIII | [Assessment — the three proofs](#part-xviii--assessment-the-three-proofs) |
| XIX | [The Final Readiness Checklist](#part-xix--the-final-readiness-checklist) |

---
---

# PART 0 — The Spine Project: the idea, argued

## The problem, stated as a person would feel it

You want to reach someone. Between you and them sits a company. That company decides whether the message is delivered, whether it is stored, whether it is read, whether it is searchable by an advertiser, whether it exists tomorrow, and whether the service works at all in your country this week.

**Every messaging system in wide use is a single point of failure with a logo on it.** WhatsApp is one company. Signal is one company, and an admirable one, but still one. Slack, Discord, Teams — one company each. When that company has an outage, everyone stops talking at once. When that company is blocked, an entire country stops talking at once. When that company changes its terms, you have no exit, because your conversations are not portable.

**The federated answer exists and is twenty-five years old.** XMPP federated in 1999. Email has federated since before that. **Matrix** has federated since 2014 and is the serious modern attempt — the French government, the German healthcare system and the Swedish military all run on it. Federation is the correct architecture: independent servers, run by different people, interoperating over a published protocol, so no single operator owns the conversation.

**And yet almost nobody chooses it, for one reason: it is slow, and nobody has published how slow, or why.** "Matrix is heavy" is folklore. The actual numbers — what a federation hop costs you in p99 delivery latency, how the ordering-violation rate scales with the number of participating servers, what happens to a conversation when one server partitions mid-sentence and how long convergence takes — are **not published anywhere as measured curves.** Ask three engineers why federated chat is slow and you will get three different stories and no data.

## What KERYX is

**A federated, partition-tolerant real-time messaging and presence backbone, with a direct peer-mesh fallback.**

Independent **relays** — run by different people on different machines — federate into one conversation space. A client connects to its home relay. Relays gossip, route, and replicate. Messages are end-to-end encrypted, so a relay forwards ciphertext it cannot read. When two relays cannot reach each other, clients fall back to **direct peer-to-peer paths** over NAT-traversed connections. When the internet is gone entirely, nearby devices form a **local mesh and store-and-forward** until a path opens.

> **The one sentence you are permitted to claim:**
> **No single operator can stop, read, or lose the conversation.**
>
> Never *"unbreakable"* or *"uncensorable."* The first person who tests an overclaim dismantles it in one blog post, and then nothing else you say gets believed — including the true parts you spent a year measuring.

## Why this is a great engineering problem and not just a virtuous one

**There is nowhere to hide from difficulty.** There is no central server to fall back on when you get lazy about consensus. There is no "the database" to lean on when you get lazy about ordering. There is an actual adversary — an operator who logs, a relay that lies, a network that partitions asymmetrically — and there is actual physics: NAT, packet loss, mobile radios that sleep, clocks that disagree.

**And the failure mode is not a 500.** It is a message that silently never arrives. Or arrives twice. Or arrives out of order so the conversation reads wrong. Or arrives on one of your three devices and not the others. Or arrives to the wrong person. Every one of those is invisible to a health check and catastrophic to a user, which means **correctness here is something you have to prove rather than assume** — and that is the single highest-value habit this roadmap is trying to build in you.

## Why it forces every topic you need — structurally, not by decoration

| KERYX needs… | …which forces you to master | Level | Verified corpus share* |
|---|---|---|---|
| Its own framed, versioned wire protocol | Binary encoding, framing, varints, forward/backward compatibility | L1 | REST/API design **34.8%** |
| Ten thousand live connections on one relay | epoll, io_uring, goroutines, virtual threads, C10K | L1 | Scalability **31.5%** |
| Bytes that actually arrive, in order, on a bad link | **TCP, congestion control, retransmission, QUIC** — built, not used | L2 | Networking 6.5% (but see §VII) |
| A message log that survives `kill -9` | **Storage engines: WAL, fsync, LSM/B+Tree, recovery, compaction** | L3 | PostgreSQL **19.6%** |
| "What order did this conversation happen in?" with no global clock | **Vector clocks, Lamport timestamps, causal delivery, CRDTs** | L3 | Distributed systems **48.9%** |
| Two relays owned by different people agreeing on a room | **Federation protocol design, conformance testing, versioning** | L4 | REST/API **34.8%** |
| A relay that forwards what it cannot read | **X25519, AEAD, the Double Ratchet, multi-device key management** | L5 | Security fundamentals 4.3% |
| A relay cluster that survives a machine dying mid-delivery | **Raft, leader election, replicated state machines, fencing tokens** | L6 | Distributed systems **48.9%** |
| Testing "partition + clock skew + a lying relay, simultaneously" | **Deterministic simulation testing, property testing, TLA+** | L7 | Testing **15.2%** |
| A presence storm in a 50,000-member room | **Fan-out, backpressure, admission control, load shedding, goodput** | L8 | Scalability **31.5%** · K8s **30.4%** |
| Keeping it up when you are the only one on call | **Observability, SLOs, chaos engineering, runbooks** | L9 | On-call **17.4%** · Obs **13.0%** |
| Two phones behind two home routers talking directly | **NAT traversal, STUN/ICE, hole punching, gossip, SWIM** | L10 | Networking · Distributed |
| Knowing what any of it actually costs | **Benchmark methodology, coordinated omission, the curves** | L11 | Perf optimisation **11.7%** |

\* Share of the **92 backend postings** in your dataset. Full ranking in §VII.

**Nothing on that list is decoration.** Remove any of it and either KERYX does not work, or you cannot explain why it does.

## The honesty statement — say this FIRST, unprompted, every time

> Federated messaging is not new and I did not invent it. **XMPP has federated since 1999. Matrix has federated since 2014**, is a published open standard, runs national healthcare and government deployments, and its reference server Synapse is a mature production system. **Signal** solved end-to-end encryption for real users with the **Double Ratchet**, which I implement rather than invent — it is Marlinspike and Perrin's design, and Signal's own specification is what I build from. **Briar** does Bluetooth and Tor mesh messaging today. **Delta Chat** uses email as its transport. **Meshtastic** does LoRa mesh. **Automerge and Yjs** solved CRDTs and did it better than I will. **libp2p and pion/ice** are the mature NAT-traversal stacks and I use them rather than writing my own.

**The gaps that are actually real, and each one is measurable:**

1. **Nobody publishes the federation cost curve.** "Matrix is slow" is universal folklore with no public numbers behind it. p99 delivery latency and ordering-violation rate as functions of *federation hop count*, *participating server count*, and *partition rate* — measured, on one testbed, with the configuration published — does not exist. **That is measurable, and I measure it.** (Flagship #8.)
2. **Nobody publishes the presence fan-out economics.** Presence — "who is online, who is typing" — is the O(N²) problem that has killed every chat system at scale, and everyone in the field knows it. The goodput curve under a presence storm, across admission strategies, is not published. (Flagship #6.)
3. **Nobody publishes what a partition costs a conversation.** Kill a relay mid-conversation: how many messages are delayed and by how long, how many arrive out of causal order, how long until every device converges, and does exactly-once delivery hold across a user's three devices? (Milestone K5, Flagship #5.)
4. **There is no conformance suite for a federation protocol** the way `h2spec` exists for HTTP/2. Matrix has a test suite; it is not a portable, adversarial conformance harness you can point at someone else's implementation. (Flagship #4.)
5. **Nobody publishes real NAT reachability for messaging.** What fraction of real-world peer pairs can hole-punch, from which network types, and what the relay fallback costs in latency and bandwidth. (Flagship #9.)
6. **There is no small, readable, benchmarked federated messaging implementation.** Synapse is ~150k lines of Python with a decade of accreted behaviour. A correct, measured, 30k-line relay that a person can read in a weekend does not exist.

**The sentence you are allowed to say:**

> *"Federated messaging is solved — Matrix has done it since 2014 and does it better than I will. What isn't published is what federation actually costs: the latency per hop, the ordering-violation rate as servers are added, and the recovery time after a partition. I built a relay small enough to instrument completely, killed servers in the middle of ten thousand seeded conversations, and I have all three curves."*

## The scale statement — the other thing you say unprompted

> **This federation is 20–40 relays I run on one workstation, plus free-tier cloud nodes in real regions, plus a deterministic simulator modelling up to 10,000 relays and a million clients.** It has never carried a real user's conversation. Anything I claim about scale beyond forty relays is measured in simulation, and **the simulator is validated against the real federation at the sizes where both run** — `docs/analysis/sim-fidelity.md`. **A simulator you have not validated is a fantasy generator.**

## Why this project and not the others you considered

| Candidate spine | Why it loses to KERYX |
|---|---|
| **Durable execution engine** (Chronos) | Legible and rare, but it is infrastructure with no human purpose — "generic executing code." Its topics are a strict subset of what KERYX forces, minus all networking, all crypto, and all federation. |
| **Privacy relay network** (Adyton) | Right instincts, wrong risk profile: two years, no clickable demo, and running relay infrastructure from Egypt opens a legal question the plan itself must budget a Week-1 memo for. KERYX keeps the onion-routing *lessons* (NAT, mesh, path selection, threat modelling) without the exposure — relays forward ciphertext for a **named, consenting** conversation, not anonymous traffic for strangers. |
| **Stream processor** (Aion) | The strongest *engineering* runner-up and the reason its best parts are transplanted below — real data, Java in the right place, a named opponent. But it is a data pipeline. Nobody is reached by it. |
| **P2P compute mesh** (Swarm) | Excellent trust content, transplanted below. But "rent out your computer" reads adjacent to crypto — the document concedes this itself — and it drops Java, the single most-demanded backend skill at 53.3%. |

**And the decisive argument: it is already your CV.** Read your own bullets back.

> *"Built a bidirectional real-time AI voice pipeline sustaining 1,000 concurrent calls… with low-latency audio handling and conversational state across multi-turn exchanges."*
> *"Designed and built an omnichannel messaging platform integrating the call-center system, WhatsApp Business APIs and a mail server."*
> *"Real-Time Chat Application — architected for horizontal scalability, distributing the WebSocket workload across ECS tasks behind an Application Load Balancer with sticky sessions."*

**You are already a real-time communications engineer with a year of production experience.** You have shipped concurrent WebSocket fan-out, multi-channel message routing, conversational state, and 1,000 simultaneous live sessions. KERYX is not a pivot — it is the sentence *"I built that on one company's infrastructure, hit the wall where that model stops, and went and built the federated version that doesn't have a single owner."*

That story is true, it is already half-evidenced by employment, and it makes one coherent engineer out of your résumé instead of a job plus an unrelated hobby.

## The demo — the thing that makes a recruiter call

Your stated success condition is: *a recruiter opens the link, sees it actually work, and calls.* So it is a scheduled deliverable, built in **Week 42** and finalised in **Week 52**, and it is on the never-cut list.

**One URL. No signup. No install.**

1. Two chat windows side by side, visibly connected to **two different relays** — `relay-a.keryx.dev` and `relay-b.keryx.dev` — with the federation path drawn between them.
2. Type in one. It appears in the other. The latency of each hop is displayed live.
3. **A big red `KILL RELAY B` button.** Relay B dies. Keep typing in window A. Messages queue visibly. Relay B comes back. **Everything arrives — exactly once, in causal order, on every device** — and the recovery time is shown as a number against the failure-free baseline.
4. **A `PARTITION` button.** The relays are severed. The direct peer path lights up and takes over, and the demo says which NAT type each side is behind and whether it hole-punched or relayed.
5. Beside it: the live goodput panel while you drive a presence storm past capacity — collapse against graceful shedding, on the same axes.
6. The **scale statement is printed on the page**, not buried in the README.

That is ten seconds, visceral, undeniable, and repeatable by a non-technical recruiter to a hiring manager: **"he built a chat system that keeps working when the servers running it die."**

---
---

# PART I — The Evidence Base

Everything here traces to a dataset **you** collected on 2026-08-28: **569 verified postings, 83 companies, 937 distinct named skills.** Every figure below was **re-derived from `postings.json` on 2026-09-14**, not quoted from an earlier roadmap — because the four earlier roadmaps disagree with each other and three of their headline numbers do not survive checking.

**Denominators.** 554 postings carry extracted skill data. Of those, **92 are backend** and **200 are backend-or-infra**. Percentages state which they use.

## The degree question. Settled here. Never raised again.

| Question | Answer | Of |
|---|---|---|
| Postings requiring a PhD with no stated alternative | **6** (1.1%) | 554 |
| Postings demanding a CS degree, no alternative field, no experience route | **1** (0.18%) | 569 |
| — and that one is | **a student internship** | |
| **Backend postings stating no degree requirement at all** | **55 of 92 (59.8%)** | 92 |
| Tier-1 postings stating no degree gate | 28.1% | 146 |
| Tier-2/3 postings stating no degree gate | 56.9% | 408 |

**Three in five backend postings state no degree gate at all.** Of the rest, most carry an equivalent-experience clause. **That clause is the route, and something has to fill it. KERYX plus four completed courses with their labs is what fills it** — *"I completed Stanford CS144 including all eight checkpoints, and MIT 6.5840 Labs 1 through 3"* is the closest thing to a transcript that exists outside a university.

**Zero hours on credential anxiety. Zero hours on certifications that are not free and incidental.**

## What backend postings actually demand (n = 92)

| Skill | Share | Skill | Share |
|---|---|---|---|
| **Java** | **53.3%** | GCP | 21.7% |
| **AWS** | **48.9%** | **Kafka** | **20.7%** |
| **Distributed systems** | **48.9%** | **C++** | **19.6%** |
| Python | 43.5% | CI/CD | 19.6% |
| Go | 38.0% | **PostgreSQL** | **19.6%** |
| Mentoring | 37.0% | Microservices | 19.6% |
| REST / API design | 34.8% | Data structures | 17.4% |
| Communication | 34.8% | **On-call** | **17.4%** |
| Scalability | 31.5% | Docker | 17.4% |
| Collaboration | 31.2% | Testing | 15.2% |
| **Kubernetes** | **30.4%** | Algorithms | 14.1% |
| System design | 23.9% | Observability | 13.0% |

## Backend + infrastructure (n = 200) — the wider target

**Distributed systems 57.0%** · Python 49.0% · Java 48.0% · AWS 40.5% · Go 40.0% · Kubernetes 35.5% · Scalability 34.5% · Mentoring 34.0% · Communication 31.0% · REST/API 28.5% · **C++ 26.0%** · CI/CD 25.0% · GCP 24.0% · System design 23.0% · **Observability 22.0%** · **On-call 21.5%** · Docker 18.5% · **Networking 14.5%** · Testing 14.0% · Kafka 12.5% · Data structures 12.0% · Algorithms 11.0% · PostgreSQL 11.0% · Rust 11.0% · Security fundamentals 3.5%

> **Distributed systems at 57.0% is the single highest-frequency technical skill in your entire target corpus.** KERYX's centre of mass is exactly that skill. That is not a coincidence of framing — it is why this spine wins on the evidence.

## 🔴 Three corrections to the earlier roadmaps — each changes a decision

**1. "System design is named in 76.3% of backend postings" is unsupported.** This is called *"the number that reorganised this plan"* in an earlier draft and is used to move 40 hours away from DSA. It does not reproduce, and that draft's own skills table says 23.9% four paragraphs earlier. **Measured: system design 23.9% as a named skill, 32.6% as a stated design/architecture duty. Against algorithms 14.1% + data structures 17.4% in backend postings.**

> **What survives:** system design becomes a first-class daily track anyway, because **100% of the loops behind these postings contain a design round and it decides the level you are hired at.**
> **What changes:** the justification is the duty data and the loop structure, not a phantom percentage — **and DSA does not drop below 300 hours.** DSA is a *gate*. Frequency is the wrong lens for a gate.

**2. "Algorithms are only 7.8%, so DSA can be deprioritised" is wrong for your target.** In **backend** postings specifically it is **14.1% algorithms and 17.4% data structures** — roughly double the whole-corpus figure. And it does not matter: every loop has two coding rounds.

**3. "128 backend or infra postings" is wrong — it is 200.** Every percentage computed on that denominator in an earlier draft is suspect. Likewise *"83.1% of non-tier-1 postings state no degree gate"* — the real figure is **56.9%**. And *"distributed systems 44.5% for backend+infra"* understates its own strongest argument; it is **57.0%**.

**4. The `1.0% → 58.8%` project-coverage table is a model, not a measurement.** Its methodology is stated nowhere and it is not derivable from the dataset. The *ordering* it produces — operational shell outranks clever core, Java is the single largest lever — is independently confirmed by the verified frequencies above, so the decisions it drives are sound. **But never quote 58.8% in an interview.** Quote Java 53.3% and distributed systems 48.9%. Those you can defend.

## 🔴 The split — read this twice

KERYX has two halves doing different jobs, and confusing them is how portfolios fail.

**The correctness and cryptographic core** — causal ordering, the Double Ratchet, Raft replication, deterministic simulation, the federation conformance suite — is the real intellectual content and it is **your forty-five-minute answer.** It is also nearly invisible to a recruiter screen. *Algorithms are named in 8.9% of the whole corpus.*

**The operational shell** — running the federation, sharding it, observing it, deploying it on Kubernetes, breaking it on purpose, carrying its pager, keeping it up — is **what the screen reads.** Distributed systems 48.9%, AWS 48.9%, Scalability 31.5%, Kubernetes 30.4%, On-call 17.4%, Observability 13.0%.

**Build the core** because it is the answer, because a CS degree *asserts* you can do this and you have no such assertion so a working causal-delivery proof is a stronger claim *because it is checkable*, and because a year of YAML will not sustain you for twelve months.

**Build the shell** because it is what gets you read.

> **The rule: the shell is never optional and never deferred past Level 8.** If the year goes badly, cut core depth before you cut shell. §XVII says exactly how.

## The gaps no solo project can close

**Mentoring 37.0% · Communication 34.8% · Collaboration 31.2% · Leadership 17.2%.** KERYX demonstrates **none** of them. They come from Logic Leap, deliberately and on a schedule — §XIV.5 names the six specific situations to seek out and the stories they become. Left to chance you arrive at Week 44 with fourteen stories, twelve of them about a side project, and interviewers notice.

---
---

# PART II — KERYX, the Specification

## Two layers, composed

```
FEDERATION LAYER   relays, owned by different people, exchanging ciphertext
                   ↓ reliability, history, offline delivery, multi-device
PEER LAYER         direct NAT-traversed paths between devices
                   ↓ low latency, and survival when federation is unreachable
```

Neither works alone. Federation alone dies when the operator dies. A pure peer mesh alone cannot deliver to a phone that is asleep, cannot hold history, and cannot reach a device that has been offline for a week. **Real systems need both, and almost no portfolio project builds both.**

## Identity and threat model

**Identity** is a long-term X25519 keypair held by the user, plus one per-device subkey. A relay knows a user's *routing address* and nothing else; it forwards ciphertext it cannot read. Devices are added by cross-signing, and a key change is surfaced to the other party rather than silently accepted — **the silent-key-change failure is the one that broke real deployments, and reproducing it is Level 5's wall.**

**In scope:** a curious or malicious relay operator · a relay that lies about delivery or ordering · network partitions, asymmetric ones included · replay and reorder attacks · a device that is lost or compromised · presence-storm abuse · Sybil relays joining the federation.

**Out of scope, stated rather than hidden:** a global passive adversary doing traffic analysis (you are not Tor; say so) · metadata resistance — **relays learn who talks to whom and when, and that is a real, stated limitation** · a compromised endpoint · a nation-state targeting one user (**use Signal**) · post-compromise forward secrecy beyond what the Double Ratchet gives you.

## ⚙️ The component map — four languages, each owning a real layer

| Component | Language | Appears | Purpose |
|---|---|---|---|
| `keryx-wire/codec` | **C++20** | W3 | Frame encode/decode, varints, zero-copy views, versioning |
| `keryx-wire/transport` | **C++20** | W9 | TCP-from-scratch (CS144), then QUIC via **ngtcp2** |
| `keryx-wire/crypto` | **C++20** | W24 | X25519, AEAD, HKDF via **libsodium**; zeroizing secret types |
| `keryx-store` | **C++20** | W13 | The message log: WAL, CRC framing, LSM, compaction, snapshots |
| `keryx-fanout` | **C++20** | W39 | The hot path: per-room fan-out, batching, backpressure |
| `keryx-relay` | **Java 21** | W15 | **The relay core** — room state, delivery engine, causal ordering |
| `keryx-federate` | **Java 21** | W19 | **Server-to-server protocol, transactions, backfill, versioning** |
| `keryx-ratchet` | **Java 21** | W25 | **Double Ratchet, prekeys, multi-device, key-change detection** |
| `keryx-raft` | **Java 21** | W29 | **Raft-replicated relay cluster; the state machine is delivery** |
| `keryx-sdk` | **Java 21** | W21 | The client library a third party writes against |
| `keryxd/gateway` | Go | W5 | WebSocket termination, auth, quotas, OpenAPI |
| `keryxd/presence` | Go | W7 | Presence, typing, read receipts — the O(N²) service |
| `keryxd/push` | Go | W22 | Offline delivery, mobile wakeup, retry with jitter |
| `keryxd/mesh` | Go | W46 | **NAT traversal (`pion/ice`), SWIM gossip, store-and-forward** |
| `keryxd/admin` | Go | W48 | Ops surface: federation health, room state, manual drain |
| `lab/sim` | Python + Java | W35 | **Deterministic simulation of the whole federation** |
| `lab/conform` | Python | W20 | **The federation conformance suite** |
| `lab/bench` | Python | W2 | The open-loop benchmark harness, used all year |
| `lab/analysis` | Python | W13 | Curves, plots, the Synapse comparison |
| `demo/` | Go + HTML | W42 | **The public kill-a-relay page** |

**⚙️ The C++ dependency set — you implement none of these:** **libsodium** (X25519, ChaCha20-Poly1305, BLAKE2b, `sodium_memzero`) · **ngtcp2** + **BoringSSL** (QUIC) · **GoogleTest** · **RapidCheck** (property tests) · **libFuzzer** with a committed corpus · **CMake** + **vcpkg**.

**ADR-0001 — the language boundary, and it is the first thing you explain in an interview.**
**C++ owns everything a hostile peer's bytes touch** — the codec, the transport, the crypto envelope, the storage engine, the fan-out hot path — because these are called at extreme frequency on untrusted input and a memory bug here is a remote compromise, not a crash. **Java owns everything stateful and consensus-backed** — the relay core, federation, the ratchet, Raft — because that is where the business logic lives, where a garbage collector is acceptable, and because it is how every large messaging backend is actually built. **Go owns the edge and the supervision** — connection termination, presence, orchestration, NAT signalling — because `pion/ice` is the mature stack and it is Go, and because connection handling is what Go's scheduler is for. **Python owns the lab**, because analysis should be fast to iterate and slow code there costs nothing.

> **The C++ sentence. Memorise it.**
> *"This is a network daemon parsing hostile input from untrusted peers, where a memory bug is a remote compromise. Rust gives you that safety by construction. I chose C++ and had to **earn** it: ASan, UBSan and TSan on every CI run, libFuzzer on every parser with a committed corpus, `std::span` instead of pointer-plus-length, no raw owning pointers in the parsing path, and a documented subset in `docs/cpp-subset.md`. Here are the three memory bugs my fuzzer found in my own code and how. That is the position almost every real systems codebase is actually in, and being the engineer who can hold that line is worth more than being the engineer who was handed it."*

🔴 **The condition, and it is not optional: the safety tooling is first-class scheduled work from Week 3, not an afterthought.** A week where CI's sanitizer job is disabled is a week the language choice became indefensible, and an interviewer will find out in ten minutes.

## The twelve milestones — one per level

| # | Level | Week | What you build | The invariant you must prove |
|---|---|---|---|---|
| **K0** | 1 | W6 | Two processes exchanging framed, authenticated messages over your own wire protocol | `kill -9` at any instruction: no message lost, none duplicated, none torn. 500 cycles. An old client and a new server interoperate. |
| **K1** | 2 | W12 | **Your own TCP** (CS144 checkpoints 0–7), then the relay speaking it | Passes CS144's full test suite. Sustains throughput on a link with 10% loss and 200ms RTT where a naive protocol collapses. |
| **K2** | 3 | W18 | The durable message log + **causal ordering** | 1,000 random-kill cycles, zero loss or corruption. **No message is ever delivered before its causal predecessor**, property-tested across 10k random interleavings. |
| **K3** | 4 | W23 | **Federation v1** — two independently-run relays share a room | A message sent on relay A appears on relay B, in causal order, exactly once. **The conformance suite passes against both.** Backfill of 10k historical messages converges. |
| **K4** | 5 | W27 | **End-to-end encryption** — Double Ratchet, multi-device | A relay operator with full database access cannot read a message. A device added mid-conversation receives subsequent messages and **provably not prior ones**. A silent key change is detected and surfaced. |
| **K5** | 6 | W34 | **Raft-replicated relay cluster** | Kill the leader mid-delivery under sustained load: **no message lost, none delivered twice, none reordered.** Verified across 500 randomised partition schedules. |
| **K6** | 7 | W38 | **Deterministic simulation of the federation** | Partition + clock skew + a lying relay + disk EIO, simultaneously, across 10,000 seeds. **≥3 real bugs found, each reproducible from a seed integer.** |
| **K7** | 8 | W42 | **Presence at scale, overload, Kubernetes — and the public demo** | Goodput held at 5× offered load by shedding, not collapse. A 50k-member room's presence storm does not degrade unrelated rooms. **A stranger can kill a relay from the demo page and every message still arrives.** |
| **K8** | 9 | W45 | The operational shell 🎯 | 20-relay federation on k8s; rolling restart delivers **zero** duplicate and zero lost messages; the 3am dashboard; 20+ incidents with runbooks. **Applications open.** |
| **K9** | 10 | W48 | **The peer mesh** — NAT traversal, gossip, store-and-forward | Two devices behind different NATs exchange a message with no relay reachable. **Real hole-punch success rate measured and published** by NAT type. |
| **K10** | 11 | W51 | **The federation benchmark** | The three curves, and a head-to-head against **Synapse** on identical hardware and semantics, reproducible by one script. |
| **K11** | 12 | W52 | Report, ADRs, retrospective | A stranger understands the architecture in 15 minutes. |

## Non-goals — if you are doing one of these, stop

- **Implementing crypto primitives, QUIC or TLS.** libsodium, ngtcp2, BoringSSL. You implement *protocols* built on primitives, never the primitives.
- **A mobile app.** A reference web client and a CLI. Mobile is a six-month project wearing a two-week costume.
- **Voice or video.** Tempting given your CV, and it is a whole second system (SFU, jitter buffers, codecs). It goes in `docs/NEXT.md` and it is the strongest thing on that list.
- **Matrix protocol compatibility.** Speaking Matrix's actual server-to-server API is an interoperability project, not a systems project, and it would consume the year. **You build your own federation protocol and you benchmark against Synapse.** Say why.
- **A blockchain, a token, or any identifying ledger.** It adds nothing you do not get from Raft and it makes some interviewers stop reading.
- **Metadata resistance / anonymity.** You are not Tor. Stated as a limitation, not attempted.
- **Full Byzantine consensus.** Crash-recovery is KERYX's failure model. Knowing precisely why you chose the lighter model is worth more than a half-finished PBFT.
- **A polished frontend.** One functional web client, one demo page. No design system. Frontend is ~0% of your target postings.
- **A fifth language.**

---
---

# PART III — The Seven Decisions

**1. Four languages, each owning a real layer.** C++20 (**26.0%** backend+infra) · Java 21 (**53.3%** backend, the #1 skill in the corpus) · Go (**40.0%**) · Python (**49.0%**). **Rust is dropped** at 11.0% — it does not appear in the top-20 backend skills, and a fifth language is bought at the price of the first. **Your existing Rust HTTP server stays pinned on GitHub**, so the language is still evidenced without costing the year.

**2. Four courses run to completion with their labs; four more as named reference.** §VI prices them. The key insight: **CS144's checkpoints and 6.5840's labs are not "study time" — they are build time.** The TCP you write in CS144 *is* KERYX's transport. The Raft you write in 6.5840 *is* KERYX's relay cluster. That is what makes a 270-hour course budget affordable in a 12-month plan.

**3. 32 h/week, 52 weeks, ≈1,522 effective hours.** Your stated shape: **4h weekdays + 6h each weekend day.** Weekday hours are DSA, system design, fundamentals and reading. **The weekend blocks are where KERYX is built** — nothing hard is ever built in 45-minute slices.

> ⚠️ **The honest risk, stated once.** 32 h/week on top of full-time work for 52 weeks is at the ceiling of sustainable. An earlier roadmap's own timeline calls 25 h/week "sustainable for about a year with genuine discipline" and names burnout around month five as the most common failure mode of programs like this. The plan is written at 32 because you chose it. **The trigger is not negotiable: three consecutive weeks of cumulative deficit, or all buffer weeks gone before W34, and you switch to the 18-month Extended Track at the Week-27 gate.** Eighteen months is a legitimate choice. A rushed Level 8 through 11 is not.

**4. Budget: zero.**
- **Oracle Cloud always-free** — 4 ARM Ampere cores / 24GB, **no expiry.** This is KERYX's publicly-reachable **bootstrap relay and STUN/relay server.** A federation needs one reachable machine; this is it, free forever.
- **AWS 12-month free tier — sign up Week 14**, not Week 1, so the twelve months cover the weeks you actually need it. Billing alarm at $1 **before any resource**.
- **GCP $300 / 90-day credit** — spent in **one planned 72-hour window** in Level 11, running a 200-relay federation at a scale your workstation cannot reach, purely to validate the simulator.
- **$0.00 verified from both consoles and screenshotted, every month.**

**5. Hardware: 64GB+ workstation.** What makes a 20–40 relay local federation feasible solo. **Measure the real ceiling in Week 2** — `docs/SCALE-RISK.md` — and sign a dated go/no-go before anything depends on it.

**6. 🎯 Applications open Week 43 (2027-07-05).** Google and Meta run 6–12 month cooldowns after a failed loop, so the date is real. **The strong northern hiring window is September–October 2027.** Applying 5 July puts first responses in late July and tier-1 loops in **August through October** — *inside* the window rather than just before it. **From Week 30, 2–3 applications/month to non-target regional companies purely for loop calibration**, so by W43 you will have sat 15–20 real interview rounds before the first application that matters.

**7. Fully mobile — read this in Week 1, not month ten.**
> **US H-1B cap registration happens once a year, in March.** A July 2027 application for a cap-subject US role means registering March 2028 → lottery → start October 2028. **Europe has no lottery** — Ireland's Critical Skills permit, the EU Blue Card, the Netherlands scheme and the UK Skilled Worker visa are continuous and reachable in 2027. **EMEA offices are the primary target, not the fallback.** The US is a two-to-three-year move via an EMEA office. *Verify current rules yourself in Week 1.*

### 🌙 The Egyptian calendar, budgeted in advance rather than discovered

**Ramadan 1448 ≈ 8 Feb – 9 Mar 2027 → weeks 22–26.** Budgeted at **20h, not 32**, with scope moved out in advance. This lands on Level 5 — **cryptography and threat modelling — deliberately, because it is the reading-and-specification level, not a heavy build level.** The Boneh lectures, the Signal specification and the 6.858 threat-model work are exactly what a reduced week can carry.
**Eid al-Fitr** ≈ 10–12 Mar (week 26, 20h). **Eid al-Adha** ≈ 17 May 2027 (week 36, 26h — a reduced week inside Level 7).

---
---

# PART IV — The Eight Laws

**1. Failure First.** Every topic opens with **🔥 THE WALL** — a broken system you reproduce. **You may not read the explanation, open the lecture, or run the prompt until the failure is on your screen.** Knowledge acquired to resolve a felt confusion is retained permanently; knowledge from a video you nodded at is gone in nine days. Interviewers hear the difference instantly.

**2. Measure Everything.** Every project ships **📈 EXIT CRITERIA** with numbers. **A speedup you cannot attribute to a named mechanism is a coincidence.** Every optimisation reports wall time *and* the relevant hardware counter *and* the mechanism — or is marked "unattributed."

**3. Set the target before you measure. Record both numbers.** Every target in this document was written before any measurement existed. Some are wrong. **Record the pre-measurement target and the actual, side by side**, and revise with a written reason. The pattern becomes `RETROSPECTIVE.md` in Week 52 — a document almost no candidate has.

**4. Real conditions, always.** KERYX is measured on **real network conditions** — `tc netem` with loss, jitter and reordering profiles taken from published mobile-network measurements — and against **real federation partners** (your own relays on three continents via free tiers). When you must simulate, say so, and validate the simulator against the real system.

**5. ⚙️ In C++, safety is earned every single commit.** Sanitizers, fuzzers and the documented subset are not hygiene — **they are the argument for having chosen C++ at all.**

**6. Three sources, one topic — and never trust the AI on a fact you will build on.** Every topic has a **course**, a **book location**, and an **AI prompt**. §V says how to choose. "I don't know where to learn this" is never a valid reason to stall. And the prompts **will** confidently invent APIs, misstate a paper's result, and hand you a plausible algorithm that is subtly wrong. Every AI-learned claim a design decision rests on gets verified against the course or the book.

**7. Ship publicly.** Own repo, README with an architecture diagram and a results chart **in the first screen**, `make demo` that works on a clean machine.

**8. Be honest about prior art and about what is simulated.** **You are never allowed to say "unsolved," "first," or "nobody has done this."** State the gap precisely instead — it is a stronger answer and the only one that survives an interviewer who has used Matrix. The **honesty statement** and the **scale statement** are said unprompted, every time.

---
---

# PART V — The Learning System

## The Three-Source Rule

Every topic carries three entries. They do different jobs, and using the wrong one for the job is how people waste months.

**📺 THE COURSE — for building a model from nothing.** When you have no scaffolding for a subject at all, a lecture sequence gives you the shape before the detail. Slow, and worth it exactly once per subject. §VI.

**📕 THE PAGES — for precision, and for coming back.** Named chapters, never whole books. This is what you cite in a design doc, and what you re-read *after* building — the second reading is the one that lands. §XV.

**🤖 THE PROMPT — for the gap, the block, and the check.** Five modes below. Fastest teacher you have, and the one Law 6 exists for.

**The choosing rule:** *new subject* → course. *Detail you half-remember* → pages. *Blocked right now, or checking your own work* → prompt. **A topic you have only ever met through a prompt is a topic you do not know.**

## The Five Prompts

**🤖 1 — TEACH · the workhorse**
> I am a backend engineer building a federated messaging system. I know [X and Y]. I do not understand [Z]. Teach me [Z] by starting from the failure it prevents — show me the broken version first, then the fix. Use a concrete example from a messaging or distributed-systems context. Then give me three questions I should be able to answer, and do not answer them.

**🤖 2 — INTERROGATE · the one you will avoid, and the one that works**
> I claim I understand [topic]. Ask me eight questions, one at a time, escalating in difficulty, of the kind an interviewer at a company that runs this in production would ask. Do not accept vague answers — push back on any hand-waving and ask me to be specific. After the eighth, tell me which of my answers were weak and what I should go re-read.

**🤖 3 — REVIEW · critique my implementation**
> Here is my implementation of [X]: [code]. Review it as a staff engineer who has operated this exact thing in production at scale. Name every correctness bug, every case I have not handled, and every place where this would fail under partition, clock skew, or hostile input. Rank them by severity. Do not compliment anything.

**🤖 4 — BRIDGE · when sources disagree**
> [Source A] says [X]. [Source B] says [Y]. They appear to contradict each other on [specific point]. Explain whether they actually disagree or are answering different questions, what assumptions each is making, and which applies to my case, which is [context]. If one is simply outdated, say so and say when it changed.

**🤖 5 — ADVERSARY · think like the attacker**
> Here is my design for [component]: [description]. You are a motivated attacker with [capability]. Describe, in order of practicality, every way you would break the security, the correctness, or the availability of this. For each, say what I would see in my logs and metrics — or, worse, that I would see nothing.

---
---

# PART VI — The Course Atlas

**The pricing insight that makes this affordable:** two of these courses' labs **are the product.** CS144's checkpoints produce a working TCP that becomes KERYX's transport. 6.5840's labs produce a Raft implementation that becomes KERYX's relay cluster. Their hours are build hours, counted once.

## Run to completion, with all labs — 270h

### 📺 **Stanford CS144 — Introduction to Computer Networking** · L2 · ~90h
**The single most relevant course to this project.** You build a working TCP implementation in C++, from the byte stream up, across eight checkpoints (the "Minnow"/"Sponge" framework): a reassembler, a receiver, a sender, a full TCP connection, an IP router, an ARP layer. Free, self-contained, with a public test suite that either passes or does not.

**Why it lands at Level 2:** KERYX's entire premise is bytes arriving reliably over a hostile network. You cannot reason about head-of-line blocking, congestion collapse, or why QUIC exists until you have written the retransmission timer yourself. **And "I implemented TCP and it passes Stanford's test suite" is an unfakeable, checkable claim.**
**Corpus:** networking 14.5% backend+infra — but this course's real payoff is distributed systems at 57.0%.

### 📺 **MIT 6.5840 (formerly 6.824) — Distributed Systems** · L6 · ~90h for Labs 1–3
**The most respected distributed-systems course in the world.** Lectures with an assigned paper each; five labs in Go. You run **Lab 1 (MapReduce), Lab 2 (Key/Value server with at-most-once RPC), and Lab 3 (Raft, in full)**. Lab 4 (fault-tolerant KV on Raft) is a stretch goal in the W34 buffer; Lab 5 (sharded KV) moves to `NEXT.md`.

> ⚠️ **The honest warning.** An earlier roadmap budgeted "2–3 weeks" for all five labs. That is wrong by roughly 4×. **Lab 3 alone defeats most people on the first attempt.** Budget 7 weeks at 12–15 h/week, expect to rewrite your Raft at least once, and expect `TestFigure8Unreliable` to humble you. Finishing Labs 1–3 puts you ahead of the large majority of working senior engineers.

**Read before you start:** the **extended** Raft paper (§5 in full, §6 carefully — the conference version omits crucial detail), and **Jon Gjengset's "Students' Guide to Raft."** Not when you are stuck. Before.

### 📺 **CMU 15-445/645 — Database Systems** (Andy Pavlo) · L3 · ~60h
**You asked about this one specifically, and it earns its place.** Pavlo's course is the best public treatment of storage engines in existence, and the recorded lectures plus the BusTub projects are entirely free.

**What you take:** **Lectures 1–10** (storage, buffer pools, hash tables, B+Trees, index concurrency) and **Project 1 (Buffer Pool Manager) and Project 2 (B+Tree Index)** in C++. Lectures 11–25 (query execution, optimisation, concurrency control, recovery, distributed databases) are watched but not projected — except **the logging and recovery lectures (ARIES), which you watch twice**, because KERYX's message log is a WAL and its recovery path is the same problem.

**Why it lands at Level 3:** KERYX's message log must survive `kill -9`, must never lose an acknowledged message, must never serve a torn record, and must support a consistent snapshot while writes continue. That is a storage engine, and Pavlo teaches it better than any book.
**Corpus:** PostgreSQL 19.6% backend. **The deeper payoff is that this is the level where "I know databases" becomes "I built one."**

### 📺 **Dan Boneh — Cryptography I** (Stanford) · L5 · ~30h
**Weeks 1–4 plus the Signal specification.** Stream and block ciphers, message integrity, authenticated encryption, key exchange, Diffie-Hellman. You are not becoming a cryptographer; you are becoming an engineer who can read the Double Ratchet specification and implement it **without inventing anything**, and who knows precisely why "we encrypt it" is not a security claim.

**Paired with:** the **Signal Double Ratchet specification** and the **X3DH specification**, both public and both short. And **Matthew Green's blog** for the parts the spec assumes you already know.

## Reference — consulted, not completed

### 📺 **CMU 15-213 / CS:APP — Introduction to Computer Systems** · L0–L1 · ~15h
**§6.2–6.4 only** (the memory hierarchy) plus **Chapter 5** (optimising program performance) when you profile the fan-out path in L8. The cache-line and false-sharing material is Week 1 and everything you build sits on it.

### 📺 **MIT 6.858 — Computer Systems Security** · L5, L9 · ~15h
**Selected lectures: the threat-model lecture, the network security lectures, the key-management lecture, and the side-channel lecture.** Its function here is to make `docs/design/threat-model.md` a real document rather than a list of good intentions.

### 📺 **MIT 6.1810 — Operating System Engineering** · L1, L10 · ~10h
**Lectures on virtual memory, traps, and network namespaces.** You are not doing xv6's labs — that is a 150-hour course and it is not on the critical path. It is here so that when you configure cgroups and network namespaces for the test federation you know what the kernel is actually doing.

### 📺 **Harvard CS165 — Data Systems** (Stratos Idreos) · optional, L3 · ~10h
Read the **course notes on column stores and adaptive indexing** if Level 3 leaves you hungry. It is the research-flavoured complement to Pavlo's engineering-flavoured course. **Genuinely excellent and genuinely optional.**

### 📺 **CMU 15-721 — Advanced Database Systems** · `NEXT.md`
Vectorised execution, code generation, modern OLAP. Not on the critical path for a messaging system. It is the best thing to do in month 13.

> **What about Harvard CS50?** It is an outstanding introductory course and you are five years past needing it. Skip it. If you ever want the Harvard equivalent at your level, it is **CS165** above, or **CS262 (Introduction to Distributed Computing)**, which overlaps 6.5840 and loses.

## 📋 The Atlas at a glance

| Course | Level | Weeks | Hours | Completion | What it buys |
|---|---|---|---|---|---|
| **CMU 15-213** §6 + ch.5 | L0, L8 | W1–2, W40 | 15 | Reference | The hardware model everything sits on |
| **Stanford CS144** | **L2** | **W7–12** | **90** | **All 8 checkpoints** | **KERYX's transport. TCP you wrote.** |
| **CMU 15-445** | **L3** | **W13–18** | **60** | **Lec 1–10, Proj 1–2** | **KERYX's message log. A storage engine you built.** |
| **Boneh Crypto I** | **L5** | **W24–27** | **30** | **Weeks 1–4** | **KERYX's E2E layer. Read a spec, implement it, invent nothing.** |
| **MIT 6.858** | L5, L9 | W26, W47 | 15 | Selected | A threat model that survives contact |
| **MIT 6.5840** | **L6** | **W28–34** | **90** | **Labs 1–3** | **KERYX's relay cluster. Raft that passes MIT's tests.** |
| **MIT 6.1810** | L1, L10 | W4, W46 | 10 | Selected | What the kernel does when you make a namespace |
| **Harvard CS165** | L3 | W18 | 10 | Optional | Depth on data systems if L3 leaves you hungry |
| | | | **~320** | | |

---
---

# PART VII — Every Topic Ranked by the Data

Every technical topic named across CHRONOS, ADYTON, AION and SWARM, sorted by its **verified share of backend postings**, with the level that covers it. **This is the answer to "what should I actually learn first."**

| Rank | Topic | Backend | BE+Infra | Level | How KERYX forces it |
|---:|---|---:|---:|---|---|
| 1 | **Java** | **53.3%** | 48.0% | **L4–L6** | The relay core, federation, ratchet and Raft are all Java 21 |
| 2 | **Distributed systems** | **48.9%** | **57.0%** | **L3–L7** | Federation, causal order, consensus, partition tolerance — the whole spine |
| 3 | **AWS** | **48.9%** | 40.5% | L9 | Relays on EC2/t4g, S3 media store, IAM, CloudWatch, the tested billing alarm |
| 4 | **Python** | 43.5% | 49.0% | L0, L7 | The simulator, the conformance suite, every benchmark and every chart |
| 5 | **Go** | 38.0% | 40.0% | L1, L8, L10 | Gateway, presence, push, NAT traversal, gossip, admin |
| 6 | **Mentoring** | 37.0% | 34.0% | Track J | 🔴 Not from KERYX. From Logic Leap, deliberately — §XIV.5 |
| 7 | **REST / API design** | 34.8% | 28.5% | L4, L9 | The client API, the federation S2S protocol, OpenAPI, versioning, the conformance suite |
| 8 | **Communication** | 34.8% | 31.0% | Track J | Design docs, ADRs, eight published posts, one talk |
| 9 | **Scalability** | 31.5% | 34.5% | **L8** | Presence fan-out, the goodput curve, admission control |
| 10 | **Collaboration** | 31.2% | — | Track J | Logic Leap, OSS PRs, the peer runbook test |
| 11 | **Kubernetes** | 30.4% | 35.5% | **L8** | The 20-relay federation on k3s; rolling restart with zero message loss |
| 12 | **System design** | 23.9% | 23.0% | Track I | 2.5h/week from Week 1, 20 written designs |
| 13 | **GCP** | 21.7% | 24.0% | L11 | The one planned 72-hour 200-relay window |
| 14 | **Kafka** | 20.7% | 12.5% | L9 | The audit and telemetry plane; offline delivery queue; outbox from committed Raft entries |
| 15 | **C++** | 19.6% | **26.0%** | **L1–L3** | Codec, transport, crypto envelope, storage engine, fan-out |
| 16 | **CI/CD** | 19.6% | 25.0% | L1→ | Sanitizers, fuzzers, the conformance suite and 10k sim seeds, all nightly |
| 17 | **PostgreSQL** | 19.6% | 11.0% | L3, L11 | Relay metadata, room state, migrations; `pgshift` under live load |
| 18 | **Microservices** | 19.6% | 12.0% | L8 | Gateway / presence / push / relay / federate as separately deployable services |
| 19 | **Data structures** | 17.4% | 12.0% | Track I | 🔴 Higher in backend than the whole corpus. 300h, do not cut |
| 20 | **On-call** | **17.4%** | 21.5% | **L9** | 20+ self-inflicted incidents with runbooks; the least substitutable gap in the list |
| 21 | **Docker** | 17.4% | 18.5% | L8 | Relay images, the test-federation orchestration |
| 22 | **Testing** | 15.2% | 14.0% | **L7** | DST, property tests, fuzzing, the conformance suite |
| 23 | **Networking** | 14.5%† | 14.5% | **L2, L10** | You implement TCP. Then NAT traversal. Then you measure both |
| 24 | **Algorithms** | 14.1% | 11.0% | Track I | See §XII |
| 25 | **Observability** | 13.0% | 22.0% | **L9** | RED per service + the five messaging signals; the 3am dashboard |
| 26 | **Perf optimisation** | 11.7%‡ | — | L8, L11 | Fan-out profiling, the curves, `flamegraph` |
| 27 | **Security fundamentals** | 4.3% | 3.5% | **L5** | E2E, threat model, sandboxing, key management |
| — | Rust | 8.7% | 11.0% | ✂️ **Dropped** | Keep the existing HTTP server pinned; do not add a fifth language |
| — | TypeScript / React | 13.0% | 11.5% | ✂️ Minimal | One functional web client, no design system |

† backend-only figure is 6.5%; the 14.5% backend+infra figure is the honest one to quote for this project.
‡ from the earlier roadmaps' extraction; treat as approximate.

**Deliberately NOT in this plan, and why:** compilers and language theory (0% corpus support) · full Byzantine consensus (you build the practical subset and explain the difference, which is worth more) · machine learning (there is none in this project, deliberately) · a fifth language · **certifications** (AWS SAA is 40 hours to close a gap that Level 9 closes better, with a running system as evidence instead of a badge).

---
---

# PART VIII — The Four Tracks

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ TRACK D — DEPTH  (59% · 19h/week → 12h from W43)                              │
│ Levels 0–12 + the Course Atlas. Builds the engineer. Builds KERYX.            │
│ Long weekend blocks. Nothing hard is ever built in 45-minute slices.          │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK I — INTERVIEW  (25% · 8h/week → 12h from W43)                           │
│ DSA 5.5h + SYSTEM DESIGN 2.5h. DAILY from week 1. Never batched, never        │
│ skipped. 600 problems · 20 written designs · 12+ full timed loops.            │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK F — FUNDAMENTALS  (9% · 3h/week → 0 from W43)                           │
│ 16 blocks, each landing the week the project first depends on it.             │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK J — CRAFT, CAREER & VISIBILITY  (7% · 2h/week → 8h from W43)            │
│ Design docs, ADRs, writing, OSS, referrals, CV, applications, and the         │
│ Logic Leap mentoring/leadership evidence. REFERRALS OPEN WEEK 18.             │
└───────────────────────────────────────────────────────────────────────────────┘
```

**Standard week: 32h = 19 Depth / 8 Interview / 3 Fundamentals / 2 Craft.**
**From Week 43: 32h = 12 Depth / 12 Interview / 8 Career.**

**Budget:** 52 × 32 = 1,664 nominal. −88 (four rest weeks at 10h: W12, W27, W38, W49) −48 (Ramadan W23–26 at 20h) −6 (Eid al-Adha W36 at 26h) = **≈ 1,522 effective hours.**

| Track | Hours | Share |
|---|---|---|
| Depth — KERYX + courses + flagships | ~870 | 57% |
| Interview — DSA ~300h + system design ~150h | ~450 | 30% |
| Fundamentals | ~130 | 9% |
| Craft & Career | ~200 | 13% |

*(Shares exceed 100% because Fundamentals hours sit inside the Depth block in the weekly split. §XVI is authoritative.)*

> **Read twice.** Depth without the interview track means nobody ever sees the depth — you fail the phone screen and never reach the design round. The interview track without depth gets you an L4 offer and a six-year stall. Craft without either is empty. **If you have only one hour on a given day, spend it on Track I** — it is the only track that degrades irreversibly when skipped.

---
---

# PART IX — The Level Map

```
  L0  The Machine & the Measurement      W1–2     Sep 2026          —
  L1  Bytes on the Wire                  W3–6     Sep–Oct 26        K0   ⚙️ C++ & sanitizers
  L2  The Network: TCP From Scratch      W7–12    Oct–Nov 26        K1   📺 CS144
  L3  Storage, Logs & Causal Order       W13–18   Nov 26–Jan 27     K2   📺 15-445   ⚑ CV v1
  L4  Federation                         W19–23   Jan–Feb 27        K3
  L5  Cryptography & the Threat Model    W24–27   Feb–Mar 27        K4   📺 Boneh  🌙 Ramadan
  L6  Consensus & Replication            W28–34   Mar–May 27        K5   📺 6.5840  ⚑ CV v2
  L7  Correctness: Simulation & DST      W35–38   May–Jun 27        K6
  L8  Presence, Overload & Kubernetes    W39–42   Jun–Jul 27        K7   ★ the demo  ⚑ CV v3
  L9  Operations, Chaos & On-Call        W43–45   Jul–Aug 27        K8   🎯 APPLY  ⚑ CV v4
  L10 The Peer Mesh: NAT & Gossip        W46–48   Aug 27            K9
  L11 The Federation Benchmark           W49–51   Aug–Sep 27        K10
  L12 Synthesis & Conversion             W52      Sep 27            K11
```

| Lvl | Name | Weeks | Dates | Milestone | Flagship | Course | Depth h |
|---|---|---|---|---|---|---|---|
| **0** | The Machine & the Measurement | 1–2 | Sep 14 – Sep 27 | — | `latency-lab`, `sickbay`, `1brc` v1 | 15-213 §6 | 32 |
| **1** | Bytes on the Wire | 3–6 | Sep 28 – Oct 25 | **K0** | **#1 `hardened`** | 6.1810 (sel.) | 76 |
| **2** | The Network: TCP From Scratch | 7–12 | Oct 26 – Dec 6 | **K1** | **#2 `minnow`**, `c10k-arena` | **CS144** | 105 |
| **3** | Storage, Logs & Causal Order | 13–18 | Dec 7 – Jan 17 | **K2** | **#3 `logstore`** | **15-445** | 114 |
| **4** | Federation | 19–23 | Jan 18 – Feb 21 | **K3** | **#4 `conform`** | — | 95 |
| **5** | 🌙 Cryptography & the Threat Model | 24–27 | Feb 22 – Mar 21 | **K4** | `ratchet` | **Boneh**, 6.858 | 44 |
| **6** | Consensus & Replication | 28–34 | Mar 22 – May 9 | **K5** | **#5 `raft`** | **6.5840** | 133 |
| **7** | Correctness: Simulation & DST | 35–38 | May 10 – Jun 6 | **K6** | **#6 `keryxsim`** | — | 66 |
| **8** | Presence, Overload & Kubernetes | 39–42 | Jun 7 – Jul 4 | **K7** | **#7 `presence-storm`** · ★ **the demo** | 15-213 ch.5 | 76 |
| **9** | Operations, Chaos & On-Call 🎯 | 43–45 | Jul 5 – Jul 25 | **K8** | **#8 `incident-lab`**, `costwatch`, `gatekeep` | 6.858 | 36 |
| **10** | The Peer Mesh: NAT & Gossip | 46–48 | Jul 26 – Aug 15 | **K9** | **#9 `natlab`** | 6.1810 (sel.) | 36 |
| **11** | The Federation Benchmark | 49–51 | Aug 16 – Sep 5 | **K10** | **#10 `fedbench`**, `1brc` v2, `pgshift` | — | 24 |
| **12** | Synthesis & Conversion | 52 | Sep 6 – Sep 12 | **K11** | — | — | 12 |

**Rest weeks: 12, 27, 38, 49** (10h, no new scope). **Buffer weeks: 22, 34, 45** (catch-up only; rest if on schedule). **🌙 Reduced (20h): 23–26. Eid (26h): 36.**

**The three gates.** **W27 — half-year:** is there a working federation? If not, decide the Extended Track *here*. **W34 — two-thirds:** the correctness half is built; count weeks behind and cut that many items off §XVII. **W45 — response rate:** ≈48 applications out; below 10%, diagnose before sending more.

---
---

# ⚡ LEVEL 0 — The Machine & the Measurement

> **Goal:** build the hardware mental model, and make every number you produce this year trustworthy.
> **⏱ Weeks 1–2 · Sep 14 – Sep 27 2026 · 32h depth** · **Prereq:** none · **Fundamentals F1** · 📺 CS:APP §6.2–6.4

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
The latency ladder with numbers you measured · cache lines (64B: touching one byte costs 64) · spatial and temporal locality · **AoS vs SoA** · **false sharing and MESI** · why an uncontended atomic costs ~20ns and a contended one ~100ns+ · prefetching rescues sequential access and cannot rescue pointer chasing · TLB and huge pages · NUMA.

**Why this is Week 1 and not Week 30:** in Week 3 you design a wire frame layout, in Week 13 a message log's page layout, in Week 39 a fan-out loop that touches ten thousand subscriber records per message. **Every one of those is a memory-layout decision, and you make them all with these numbers in front of you.**

### 📄 SOURCES
- 📺 **CMU 15-213 lectures on the memory hierarchy** (cache lecture + the cache lab's writeup).
- 📕 **Bryant & O'Hallaron, *CS:APP* 3rd ed. — §6.2–6.4 only** (~40 pages). Skip §6.1.
- 📕 **Drepper, "What Every Programmer Should Know About Memory" — §3 in full**, §6.2–6.4. Skip §4–5.
- 📄 **Igor Ostrovsky, "Gallery of Processor Cache Effects"** — ten experiments, run all of them.
- 📄 **Colin Scott's interactive latency numbers** — note what changed over 20 years and what did not.

### 🛠 CORE PROJECT — `latency-lab` *(Instrument, 8/10)* · 6h
A tool that measures the latency ladder of the machine it runs on and emits a personalised card: L1/L2/L3/DRAM, uncontended vs contended atomic, mutex, branch mispredict, NVMe 4K read, syscall, context switch, **TCP loopback RTT, and TCP RTT to your Oracle box in Frankfurt.** **Derive your cache sizes from a working-set sweep, without asking the OS.**

📈 **EXIT CRITERIA**
- [ ] Derived cache sizes match `lscpu` within one power of two — or you can explain why not
- [ ] Row-major vs column-major gap **explained by measured LLC-miss counts**, not asserted
- [ ] False-sharing fix ≥3× throughput, with `perf c2c` output committed
- [ ] A chart: working-set size (log x) vs ns/access, with the knees annotated
- [ ] **The network row: loopback RTT, same-city RTT, cross-continent RTT — measured, not looked up**
- [ ] You can recite the ladder in orders of magnitude in under 20 seconds

⛓ **PROBLEM CHAIN**
```
"Column-major is 40× slower"      → cache lines → the wire frame's field order              (→ L1)
"Contended atomic is 5×"          → MESI → why the room's subscriber table is read-mostly   (→ L8)
"Pointer chasing can't prefetch"  → why the message log's index is flat, not a node graph    (→ L3)
"Cross-continent RTT is 90ms"     → a federation hop costs at least that → the whole curve   (→ L11)
"Syscall is 400ns"                → why fan-out batches writes instead of one per subscriber (→ L8)
```

## 0.2 — Benchmark methodology: your numbers are lying to you

> ### 🔥 THE WALL
> Benchmark a trivial function five times. **The numbers differ by 15–40%.** Find out why, one cause at a time: frequency scaling, turbo, thermal throttling, ASLR changing alignment, thread migration, cold first iterations.
>
> Then build a **closed-loop** load generator (send the next message after the previous is acknowledged) and an **open-loop** one (fixed arrival rate regardless). Point both at a service that stalls 200ms once a second. **The closed-loop harness reports a beautiful p99. It is a lie.**

### 📖 THEORY
**Coordinated omission** — a closed-loop generator cannot measure the latency of messages it failed to send. When the relay stalls, the generator stalls with it, and every message that *should* have arrived does not exist in the data. **This matters more in a messaging system than almost anywhere**, because senders do not wait politely for your relay to recover.
**You cannot average percentiles.** The p99 of a message crossing three relays is not the p99 of one hop. **Tail latency compounds through a federation path** — this is the whole of Level 11.
Warm-up, steady state, `benchstat`, ≥5 runs, report distributions.

**Reporting discipline for this repo:** every benchmark reports p50/p90/p99, peak RSS, **and the relevant hardware counter.** A latency number without one is not a result.

### 📄 SOURCES
- 📄 **Gil Tene, "How NOT to Measure Latency"** — in full, before you publish any benchmark this year.
- 📄 **Dean & Barroso, "The Tail at Scale", CACM 56(2), 2013** — eight pages.
- 📕 **Gregg, *Systems Performance* 2nd ed. — ch. 6 §6.6, ch. 13.** Reference.

### 🛠 CORE PROJECT — `lab/bench` + `sickbay` · 14h
The harness you use all year: fixed workloads, warm-up, percentiles, `perf stat` integration, **open-loop by default**, CI regression gate, and **`tc netem` profiles** (clean / 1% loss / 5% loss+jitter / mobile) applied from the harness so every network number states its conditions.
**`sickbay`:** 8 injectable pathologies in a container — memory leak, FD leak, lock contention, runaway syscall loop, disk saturation, CPU throttling under cgroup, DNS stall, **JVM GC pause** — each with a hidden `SOLUTION.md` showing the *evidence* that reveals it.

📈 **EXIT CRITERIA**
- [ ] Two runs produce byte-identical result sets (fixed seeds, stable tie-breaking)
- [ ] Harness is **open-loop by default**; you can explain why in one paragraph
- [ ] CPU pinning and governor applied inside the harness
- [ ] A deliberate 5% regression is caught by `benchstat` in CI
- [ ] **Four `tc netem` profiles applied from config; every benchmark records which one it ran under**
- [ ] **`sickbay`: median diagnosis under 10 minutes across all 8, on a shuffled re-run**

> ⚠️ **You revisit this in Week 40 (F12).** If your harness turns out to have coordinated omission, you **re-run every benchmark** and put the before/after in `bench/RESULTS.md`. *"I found coordinated omission in my own harness and re-measured eight months of results"* is one of the strongest sentences you can say in an interview.

## 0.3 — The scale spike: how big can your federation actually be?

> ### 🔥 THE WALL
> Before any protocol work: **start 40 JVM processes**, each with a 400MB heap and 250 open sockets, all gossiping. Watch what breaks first — RAM, file descriptors, ephemeral ports, or the scheduler.
>
> Then provision the **Oracle always-free ARM box** and verify you can reach it, and it can reach you, from your Cairo connection.
>
> **Those numbers are the ceiling on your entire year**, and you need them in Week 2, not Week 30.

📈 **EXIT CRITERIA — `docs/SCALE-RISK.md`**
- [ ] Measured max concurrent relay-shaped JVM processes at realistic heap, **with the binding resource named**
- [ ] `ulimit -n`, `net.ipv4.ip_local_port_range`, cgroup limits documented and tuned
- [ ] Disk sustained write rate measured — the message log cannot exceed it
- [ ] **Oracle always-free instance provisioned; a process runs there; you reach it and it reaches you; `$0.00` confirmed**
- [ ] **Signed, dated go/no-go on the local-federation-plus-simulator strategy**

## 🎓 LEVEL 0 EXIT EXAM
1. Recite the latency ladder in orders of magnitude. How many L1 hits fit in one DRAM access? One cross-continent RTT?
2. You store a room's subscriber list as array-of-structs vs struct-of-arrays. Fanning out to 1,000 subscribers touching one field each — how many cache lines for each layout?
3. Explain false sharing in four sentences, then the fix.
4. What is coordinated omission? Sketch a harness where a 200ms stall is invisible.
5. Why can't you average p99s across a three-hop federation path? What do you do instead?
6. Your box runs 38 relays and dies at 39. Name three possible binding resources and the command that identifies each.

**Pass = 5/6.**

### 🧩 TRACK I — L0 · W1–2 · 8h/wk
**DSA:** arrays, hashing, prefix sums, two pointers, sliding window. **The cache intuition you just built is *why* these are fast in practice, not just in Big-O** — do them now while that is fresh. NeetCode 150, sections 1–3. **~24 problems.**
**System design:** the **estimation module** — back-of-envelope arithmetic and the numbers to memorise (§XII). First written estimate: *"how much storage does a messaging service with 10M daily users need per year?"*

---
---

# ⚡ LEVEL 1 — Bytes on the Wire

> **Goal:** two processes exchange framed, authenticated, versioned messages over a socket — and neither a crash nor a hostile peer can make them lose, duplicate, or misparse one.
> **⏱ Weeks 3–6 · Sep 28 – Oct 25 2026 · 76h** · **Milestone K0** · **🚩 Flagship #1 `hardened`** · **Fundamentals F2, F3**
>
> ⚙️ **This is where the C++ safety apparatus is built, and it is scheduled work from Week 3.** Every later level assumes it is green.

## 1.1 — The protocol nobody designs carefully, and then regrets

> ### 🔥 THE WALL — four failures, in order
> Write the obvious protocol: `send(json.dumps(msg).encode())` on one side, `json.loads(sock.recv(4096))` on the other. Then:
> 1. **Send two messages quickly.** The receiver gets them glued together, or gets half of one. **TCP is a byte stream, not a message stream** — and every engineer discovers this exactly once.
> 2. **Send a 10MB message.** `recv(4096)` gets 4096 bytes. You need framing and you need a length prefix.
> 3. **Send a length prefix of `0xFFFFFFFF`.** Your receiver allocates 4GB and dies. **A hostile peer just killed your relay with 4 bytes.**
> 4. **Add a field to the message and deploy one side.** The other side breaks. You now have a versioning problem and no versioning scheme.
>
> **Screenshot all four.** Failure 3 is the one that defines this level: **every byte you parse came from someone who may want you dead.**

### 🔎 DIAGNOSE
```bash
tcpdump -i lo -X 'tcp port 9000'        # look at your own frames on the wire
strace -c -f ./relay                     # syscalls per message: the batching argument
valgrind --tool=memcheck ./parse_fuzz    # before you have sanitizers wired up
```

### 📖 THEORY
- **Framing.** Length-prefixed vs delimited vs self-describing. **Length-prefix with a hard maximum, validated before allocation**, always.
- **Varints, zigzag, and why Protobuf encodes the way it does.** You are not using Protobuf — you are writing a codec — but you should understand the design you are deliberately not adopting, and be able to say why. *(The reason: you want byte-level control of a security-sensitive parser and a conformance suite you own.)*
- **Zero-copy parsing.** `std::span` and string views into the receive buffer; arena allocation so you never `free` per message. Never a raw pointer-plus-length in the parsing path.
- **Wire versioning done properly.** Required vs optional fields, unknown-field preservation, capability negotiation at handshake, and **the test that pins an old binary and asserts it still interoperates.**
- **Authenticated framing.** Every frame carries a MAC; a frame that fails authentication is dropped *before* it is parsed further, and the failure is counted and rate-limited rather than logged per occurrence (or a peer can fill your disk).
- **Concurrency models and the C10K problem.** Process-per-connection vs thread-per-connection vs bounded pool vs `epoll` vs `io_uring` vs goroutines vs **JVM virtual threads**. Cost in bytes and microseconds. Context-switch anatomy — **the cache cost dwarfs the switch cost.** `EMFILE` vs `ENFILE`.

### 📄 SOURCES
- 📕 **Arpaci-Dusseau, *OSTEP* — ch. 4–7** (processes, the API, direct execution, scheduling). Free.
- 📄 **Dan Kegel, "The C10K Problem"** — read as an artifact of how the industry got here.
- 📄 **Evan Klitzke, "Blocking I/O, Nonblocking I/O, And Epoll"** — precise and short.
- 📄 **Jens Axboe, "Efficient IO with io_uring"** — the primary source.
- 📄 **William Kennedy (Ardan Labs), "Scheduling In Go"** — all three parts.
- 📄 **JEP 444 (Virtual Threads)** — because L4's relay runs on these.
- 📕 **Protocol Buffers encoding documentation** — read the varint and wire-format pages, then close them and design your own.
- 📄 **The libFuzzer tutorial** and **Google's fuzzing best practices** — you are wiring this up this week, not later.
- 📺 **MIT 6.1810 — the traps and virtual-memory lectures** (selected), for what the kernel is doing underneath.

### 🛠 🚩 FLAGSHIP #1 — `hardened` *(Adversary, 9/10)* + MILESTONE K0 · 60h

**The codec** (`keryx-wire/codec`, C++20): length-prefixed frames with a hard cap, CRC, varint fields, zero-copy views, capability-negotiating handshake, explicit version field.
**The safety apparatus, as a deliverable:** ASan + UBSan + TSan on every CI run · **libFuzzer on the frame parser with a committed corpus** · `-Wall -Wextra -Werror -fno-omit-frame-pointer` · `clang-tidy` with `cppcoreguidelines` and `bugprone` · and **`docs/cpp-subset.md`** stating what you do not use and why.
**The Go side** (`keryxd/gateway`): WebSocket termination speaking the same wire format, so a browser and a relay are the same protocol.

📈 **EXIT CRITERIA**
- [ ] **Four attacks fail:** oversized length prefix, truncated frame, frame claiming a version from the future, frame with a valid header and corrupt MAC. Each has a test asserting the failure mode **and** the counter it increments
- [ ] **libFuzzer runs 1 hour clean on the parser**, with the corpus committed. 🔴 **Report the bugs it found before it was clean** — that is the deliverable, not the clean run
- [ ] **ASan / UBSan / TSan green in CI**, screenshot of a deliberately-introduced violation being caught
- [ ] **K0: `kill -9` at random points across 500 cycles — no message lost, none duplicated, none torn.** The receiver's log and the sender's log reconcile exactly
- [ ] **An old client binary, pinned in CI, interoperates with the new server.** Asserted, not assumed
- [ ] `c10k-arena` (below) informs a **written** decision: which concurrency model each KERYX component uses, with the numbers
- [ ] `docs/design/wire-protocol.md` — the frame layout, the versioning scheme, the security properties of the handshake, and **what an unauthenticated peer can make you do**

### 🛠 CORE PROJECT — `c10k-arena` *(Instrument, 9/10)* · 16h
The same echo server **seven ways** — process-per-connection, thread-per-connection, bounded thread pool, single-threaded `epoll`, `io_uring`, **goroutines**, **JVM virtual threads** — plus the harness benchmarking all seven at 100 / 1k / 10k / 50k connections.

📈 **EXIT CRITERIA**
- [ ] All seven pass an identical correctness test (echo integrity under concurrent load, no interleaving)
- [ ] Seven-line chart: connections (log) vs p99 latency; second chart for RSS
- [ ] **You can state exactly where each model's knee is and name the resource that caused it**
- [ ] `io_uring` shows **measurably fewer syscalls per message** than `epoll` — the number from `strace -c`
- [ ] **Goroutines vs JVM virtual threads compared directly** — a genuinely current comparison almost nobody has published numbers for
- [ ] **Run again under a cgroup CPU limit and show how the ranking changes under throttling** — the Kubernetes reality, and almost nobody benchmarks it

⛓ **PROBLEM CHAIN**
```
"Two messages arrived glued"   → TCP is a byte stream → framing → length prefix
"4-byte length killed my relay"→ validate before allocate → every byte is hostile        (→ L5)
"Adding a field broke the peer"→ wire versioning → capability negotiation → pinned tests (→ L4)
"10k threads killed the server"→ epoll → goroutines vs virtual threads → measure both
"The fuzzer found a heap overflow"→ THIS is why the sanitizers are scheduled work
"My frames arrive out of order"→ ...and TCP is supposed to prevent that. Does it? How?    (→ L2)
```

## 🎤 INTERVIEW PARAGRAPH — Week 6

> I'm building a federated messaging backbone — independent relays run by different people, interoperating over a protocol I designed, so no single operator owns the conversation. Federated messaging isn't new; Matrix has done it since 2014 and XMPP since 1999. What isn't published is what federation actually *costs* — latency per hop, ordering violations as servers are added, recovery time after a partition — and that's what I'm measuring. Right now I'm at the wire. The first thing I did was write the naive version and attack it: two messages arrived glued together because TCP is a byte stream and not a message stream, a ten-megabyte message arrived in 4KB pieces, and then I sent a length prefix of 0xFFFFFFFF and my own relay allocated four gigabytes and died. A hostile peer killed my server with four bytes. So the parser validates before it allocates, every frame is authenticated before it's parsed further, and the C++ safety apparatus is scheduled work rather than hygiene — sanitizers on every CI run and libFuzzer on the parser with a committed corpus. It found three real memory bugs in my own code in the first week, which is exactly the argument for having them. I also benchmarked seven concurrency models to fifty thousand connections including goroutines against JVM virtual threads, and ran them again under a cgroup CPU limit, because that's the Kubernetes reality and it changes the ranking.

## 🎓 LEVEL 1 EXIT EXAM
1. TCP delivers a byte stream. Name three framing strategies and the failure mode of each.
2. A peer sends a length prefix of 4 billion. Walk through every place that should have stopped it.
3. Why is `std::span` preferable to pointer-plus-length in a parsing path? Give the bug class it eliminates.
4. Your fuzzer has run clean for 24 hours. What do you conclude, and what do you do next?
5. Goroutines vs JVM virtual threads vs epoll — when does each win? Answer from your own chart. What is thread pinning?
6. You add a field to the wire format. Describe every deployment order and what breaks in each.
7. A peer floods you with frames that fail authentication. What must happen, and what must *not* happen?

**Pass = 6/7.**

### 🧩 TRACK I — L1 · W3–6 · 8h/wk
**DSA:** **binary search including binary search on the answer** (frame-size and batch tuning are literally this) · stacks and monotonic stacks · linked lists · **bit manipulation** (your varint encoder is bit manipulation, do the set this week). NeetCode 150 sections 4–7. **~44 problems.**
**System design:** design a **URL shortener** and a **rate limiter**. Both are estimation-and-storage warm-ups, and the rate limiter is the thing you build for real in Level 8.

---
---

# ⚡ LEVEL 2 — The Network: TCP From Scratch

> **Goal:** stop *using* the network and start *understanding* it — by implementing TCP, then measuring what it does to your messages on a bad link.
> **⏱ Weeks 7–12 · Oct 26 – Dec 6 2026 · 105h** · **Milestone K1** · **🚩 Flagship #2 `minnow`** · **📺 Stanford CS144, all 8 checkpoints** · **W12 = REST WEEK** · **Fundamentals F4, F5**
>
> **This is the level that makes you a networking engineer rather than someone who has read about networking.** It is six weeks and it is worth every one of them, because the artifact — a TCP that passes Stanford's test suite — is unfakeable and becomes KERYX's transport.

## 2.1 — What TCP is actually doing for you, and what it costs

> ### 🔥 THE WALL
> Run your Level-1 relay over a link with `tc netem delay 200ms 50ms loss 5% reorder 10%`. Send a thousand messages.
> 1. **Throughput collapses far more than 5%.** Find out why — one loss event triggers a congestion-window collapse, and with 200ms RTT it takes seconds to recover.
> 2. **Now open ten conversations over that one TCP connection.** A single lost packet stalls *all ten*, because TCP must deliver bytes in order and one gap blocks the whole stream. **That is head-of-line blocking, it is the reason QUIC exists, and you should see it on a graph before you read a word about it.**
> 3. **Now open ten separate TCP connections instead.** Better for HOL, dramatically worse for handshake cost and congestion fairness. There is no free option.
>
> **Capture all three graphs.** They justify every transport decision you make for the rest of the year.

### 📖 THEORY — this is CS144, and you do the labs
- **The byte-stream abstraction** and how it is manufactured from unreliable datagrams.
- **The reassembler** — out-of-order arrival, overlapping segments, capacity limits. *(CS144 checkpoint 1, and the first time most people realise how much bookkeeping is hidden.)*
- **The receiver** — sequence numbers, wraparound, the window. *(Checkpoint 2.)*
- **The sender** — retransmission timers, exponential backoff, RTT estimation and why it is a moving average with variance, the retransmission ambiguity problem. *(Checkpoint 3.)*
- **The connection** — three-way handshake, teardown, TIME_WAIT and why it exists, simultaneous close. *(Checkpoint 4.)*
- **The network below** — ARP, the IP router, longest-prefix match. *(Checkpoints 5–7.)*
- **Congestion control** — slow start, congestion avoidance, fast retransmit, and the modern divergence: **Reno vs CUBIC vs BBR.** Bufferbloat, and why a bigger buffer makes latency worse.
- **Head-of-line blocking and QUIC** — independent streams over one connection, 0-RTT resumption, connection migration across network changes (**which matters enormously for a phone**), and why QUIC lives in userspace.
- 🔴 **The decision this level produces:** KERYX's transport is **QUIC via ngtcp2**, and you can now argue it from your own measurements rather than from fashion. Write **ADR-0002**.

### 📄 SOURCES
- 📺 **Stanford CS144 — all lectures, and all eight checkpoints.** The labs are the level.
- 📕 **Kurose & Ross, *Computer Networking* 8th ed. — ch. 3 in full.** The most valuable chapter in the book.
- 📕 **Fall & Stevens, *TCP/IP Illustrated Vol. 1* — ch. 13, 14, 15.** The definitive reference when CS144's framework leaves a gap.
- 📕 **Grigorik, *High Performance Browser Networking*** — ch. 1–4, free at `hpbn.co`. Read the UDP chapter too.
- 📄 **RFC 9000 §2 (QUIC overview)** — twelve pages. Then the ngtcp2 examples.
- 📄 **Cardwell et al., "BBR: Congestion-Based Congestion Control" (ACM Queue 2016).**
- 📄 **Gettys & Nichols, "Bufferbloat: Dark Buffers in the Internet."**

### 🛠 🚩 FLAGSHIP #2 — `minnow` *(Reimplementation, 9/10)* + MILESTONE K1 · 85h

CS144's eight checkpoints, completed, **plus the thing that makes it a flagship rather than a homework submission**: a harness that runs *your* TCP and *the kernel's* TCP over the same six `tc netem` profiles and plots throughput, p99 latency, and retransmission count side by side — **and a written analysis of every place yours is worse and why.**

📈 **EXIT CRITERIA**
- [ ] **All 8 CS144 checkpoints pass the provided test suite.** Screenshot in the README
- [ ] Your TCP interoperates with the kernel's — **your client talks to a real `nc` server and back**
- [ ] **The comparison chart:** yours vs the kernel's, six network profiles, three metrics. With the honest analysis
- [ ] **The head-of-line-blocking chart** — ten logical conversations over one TCP connection vs ten connections vs QUIC streams, under 5% loss. 🔴 **This chart justifies ADR-0002 and you will show it in interviews**
- [ ] RTT estimation implemented per RFC 6298; **plot your estimator against measured RTT** on a jittery link
- [ ] **K1:** the relay speaks QUIC (ngtcp2) and sustains throughput on 200ms RTT / 10% loss where the Level-1 TCP relay collapses. Both numbers
- [ ] **ADR-0002 written** — TCP vs QUIC vs a hand-rolled reliable-UDP layer, argued from your own graphs
- [ ] `docs/design/transport.md` — what the transport guarantees, what it does not, and what the application layer must therefore handle itself

⛓ **PROBLEM CHAIN**
```
"5% loss cost me 60% throughput"→ congestion control → cwnd collapse → RTT recovery
"One lost packet stalled 10 chats"→ head-of-line blocking → QUIC streams → ADR-0002
"Ten connections fixed HOL"     → ...and broke handshake cost and fairness → no free option
"My RTT estimator oscillated"   → RFC 6298 → smoothed RTT + variance → why the constants
"The phone changed WiFi→LTE"    → connection migration → QUIC connection IDs               (→ L10)
"Bytes arrive in order..."      → ...but MESSAGES across relays don't → causal order        (→ L3)
```

## 🎤 INTERVIEW PARAGRAPH — Week 12

> I spent six weeks implementing TCP, because my whole project is messages arriving over networks that are trying not to deliver them, and I didn't want to reason about that from a diagram. It's Stanford's CS144 framework — reassembler, receiver, sender, full connection, then an IP router underneath — and it passes their test suite and interoperates with the kernel's stack. But the part I'd actually show you is the comparison: I ran my TCP and the kernel's over six network profiles with loss, jitter and reordering, and plotted throughput and p99 side by side, with a written analysis of every place mine is worse and why. And one graph came out of it that decided my architecture. I ran ten logical conversations over a single TCP connection at five percent loss, and one lost packet stalled all ten — head-of-line blocking, because TCP has to deliver bytes in order and a gap blocks everything behind it. Ten separate connections fixes that and wrecks your handshake cost and congestion fairness instead. QUIC's independent streams fix it properly, which is why my transport is QUIC — and I can argue that from my own measurements rather than because it's fashionable. Connection migration matters to me too, because a phone switching from WiFi to LTE shouldn't drop a conversation.

## 🎓 LEVEL 2 EXIT EXAM
1. Walk through what happens to the congestion window on a single loss at 200ms RTT. How long to recover, and why?
2. Explain head-of-line blocking to someone who knows TCP delivers reliably. Give the number from your own chart.
3. Why does TIME_WAIT exist? What breaks if you disable it?
4. Your RTT estimator oscillates on a jittery link. What is wrong and what does RFC 6298 do about it?
5. Reno vs CUBIC vs BBR — what is each optimising for, and where does each lose?
6. What is bufferbloat, and why does adding buffer memory make latency worse?
7. Your TCP is 20% slower than the kernel's. Name three plausible causes and how you would distinguish them.
8. A phone moves from WiFi to LTE mid-conversation. What happens under TCP, and what does QUIC do differently?

**Pass = 7/8.**

### 🧩 TRACK I — L2 · W7–12 · 8h/wk (W12 reduced)
**DSA:** **graphs — BFS and DFS** (routing and the reassembler's interval merging are both graph-shaped) · intervals and merging (**the reassembler *is* an interval-merge problem — do LeetCode's interval set this week specifically**) · queues and deques · sorting. NeetCode 150 sections 8–10. **~50 problems. Running total ≈118.**
**System design:** design a **distributed message queue**, and design a **notification system**. You are about to build the first one for real.
**W12 rest week:** the first **failure-category count** from `dsa/FAILURES.md`. Twenty minutes, and it redirects the next quarter.

---
---

# ⚡ LEVEL 3 — Storage, Logs & Causal Order

> **Goal:** a message log that survives being killed, and an ordering guarantee that survives having no global clock. **The two hardest correctness problems in messaging, back to back.**
> **⏱ Weeks 13–18 · Dec 7 2026 – Jan 17 2027 · 114h** · **Milestone K2** · **🚩 Flagship #3 `logstore`** · **📺 CMU 15-445** · **⚑ CV v1** · **Fundamentals F6, F7**

## 3.1 — 🚩 FLAGSHIP #3: `logstore` — the engine and the adversary

> ### 🔥 THE WALL — the torn write
> Build the simplest durable message log: append `msg_id,room,sender,ciphertext` to a file, keep an in-memory index of id → offset. **Now `kill -9` it mid-write. Restart. Is the log correct?** Do it 500 times with random kill timing.
>
> You will find: truncated records · records that parse but are garbage · an index pointing past EOF · and the nastiest — **records that look valid but are half-old, half-new.**
>
> Then discover, in order:
> - **`write()` returning success means nothing was persisted.** It is in the page cache. You acknowledged a message that does not exist.
> - **`fsync()` is what persists**, and costs ~100µs on NVMe — which caps your acknowledged-message rate unless you group-commit.
> - **On some filesystems a failed `fsync` marks the pages clean anyway** — so retrying `fsync` after an error can silently lose your data. That is "fsyncgate," and it hit PostgreSQL. **You cannot retry an fsync failure; you must treat it as fatal.**

### 📖 THEORY — this is 15-445 lectures 1–10, plus the recovery lectures
- **B-Trees vs LSM-Trees and the RUM conjecture** — optimise two of Read amplification, Update amplification and Memory; never all three. **A message log is append-heavy with point lookups by id and range scans by room+time**, which is an LSM shape. State which two you chose and why.
- **The buffer pool** *(15-445 Project 1)* — page replacement, pinning, and why the OS page cache is not enough when you need to control eviction.
- **B+Tree indexes** *(15-445 Project 2)* — and the concurrency protocol (latch crabbing) that makes them usable from many threads.
- **WAL and ARIES** — redo logging, group commit, checkpointing, and the durability/latency dial (`fsync` per write vs group commit vs none). **Measure all three.** 🔴 **Watch 15-445's logging and recovery lectures twice** — KERYX's message log *is* a WAL and its recovery path is ARIES's problem.
- **Checksums and framing** — every record carries a CRC and a length; a torn tail is detected, not parsed.
- **Bloom filters** — skip an SST without reading it. Report the configured false-positive rate and the measured disk-read reduction.
- **Compaction** — and why it causes latency spikes you must budget background I/O for. **In a messaging system a compaction stall becomes delivery lag becomes a client timeout**, so this is not academic.
- **🔴 Consistent snapshots while writes continue.** Required absolutely by Level 6: you must be able to say "the log as of exactly here" without stopping the world, because that is what a new relay joining a room backfills from and what Raft snapshots. LSM makes this natural — immutable SSTs plus a manifest — **and that is not a coincidence.**
- **MVCC and isolation** *(F6, 15-445's concurrency-control lectures)* — the vocabulary for the relay metadata store, and for understanding what your engine does *not* provide.

### 📄 SOURCES
- 📺 **CMU 15-445 — lectures 1–10 and Projects 1–2 (Buffer Pool, B+Tree), in C++.** Then lectures on logging and recovery, twice.
- 📕 **Kleppmann, *DDIA* — ch. 3 in full.** Read it twice; the second time after the project.
- 📕 **Petrov, *Database Internals* — ch. 2–4** (B-trees), **ch. 5** (transaction processing, recovery, WAL/ARIES). Part I is the best storage-engine treatment in print. Skip Part II.
- 📄 **"Bitcask: A Log-Structured Hash Table for Fast Key/Value Data"** — 6 pages, your v1 target.
- 📄 **Rebello et al., "Can Applications Recover from fsync Failures?"** + the PostgreSQL fsyncgate mailing-list thread.
- 📄 **Athanassoulis et al., "The RUM Conjecture."**
- 📄 **O'Neil et al., "The Log-Structured Merge-Tree" (1996)** — the original.
- 📺 *Optional:* **Harvard CS165 notes on adaptive indexing**, if you finish early and want the research-flavoured view.

### 🛠 THE BUILD · 60h — `keryx-store` (C++20)

**The engine (v1→v5):** append log + in-memory index → CRC framing and partial-tail recovery → SST files and compaction → Bloom filter per SST → **consistent snapshot via immutable SSTs + manifest.**

**`logstore-torture` — the adversary, and the reason this scores 9/10:**
- Random append/read workload while `kill -9`ing at random intervals
- **After every restart, verify four invariants:** every acknowledged message is present · no unacknowledged message is present · no record is torn or garbage · the index never points outside a file
- **Syscall-level fault injection via `LD_PRELOAD`:** `write()` succeeds but writes only half · `fsync()` returns `EIO` · a file is truncated at a random offset
- 1,000 cycles in CI

📈 **EXIT CRITERIA**
- [ ] **1,000 random-kill cycles, zero invariant violations**
- [ ] **Torn-write injection caught by checksums 100% of the time** — keep the pre-CRC branch to demonstrate a failing case
- [ ] Throughput: `fsync`-per-append vs group commit vs no-fsync, all three measured, **with a written argument for which KERYX ships and the acknowledged-message rate each implies**
- [ ] 15-445 **Projects 1 and 2 pass their test suites** — the buffer pool and the B+Tree
- [ ] Bloom filter measurably reduces reads for missing ids, configured **and measured** false-positive rate
- [ ] **Compaction's effect on p99 measured during a compaction**, and the write-stall behaviour under sustained append
- [ ] **🔴 A consistent snapshot is taken while appends continue, and reading it returns exactly the log as of the snapshot point.** Property-tested. **Levels 4 and 6 cannot exist without this**
- [ ] `docs/design/durability-contract.md` — what this engine guarantees and what it does not, in DDIA ch. 3's language

> **Why this is a flagship and "build a KV store" is not:** thousands of people have written Bitcask. **Almost nobody writes the torture harness.** The harness is the senior artifact — it demonstrates that correctness is something you *prove*, not assume.

## 3.2 — 🔴 Causal order: the hardest idea in this document

> ### 🔥 THE WALL
> Three clients, one room. Alice sends "Is the server down?". Bob replies "Yes, I just checked". Carol sends "No it's fine" *at the same moment as Bob*, without having seen his message.
>
> Order them by wall-clock timestamp. **The clocks disagree by 40ms.** Carol's reply appears before Alice's question. **The conversation now reads as nonsense, and nothing crashed, and no metric moved.**
>
> Then "fix" it by having the relay assign sequence numbers. **Now add a second relay**, and discover that two relays cannot assign a single sequence without agreeing — which they cannot do cheaply, across continents, per message.
>
> **This is the failure that makes federated chat hard, and every wrong answer to it is invisible.**

### 📖 THEORY
- **Wall clocks lie.** NTP skew, leap seconds, VM clock jumps, and the fact that **a clock going backwards is a normal event you must handle.** `CLOCK_MONOTONIC` vs `CLOCK_REALTIME` and when each is correct.
- **Lamport timestamps** — a total order consistent with causality, and what it cannot tell you (whether two events were actually concurrent).
- **Vector clocks** — the partial order that *does* capture concurrency. Size grows with participants; the compaction strategies that make them practical.
- **Causal delivery** — a message is delivered to the application only when all its causal predecessors have been. The buffer this requires, and what happens when a predecessor never arrives.
- **Happens-before, and what "concurrent" actually means.** This is Lamport's 1978 paper and it is eight pages and you read it now.
- **CRDTs** — the algebra that lets independent replicas merge without coordination: join-semilattices, LWW registers, OR-sets, and **why a messaging timeline is a *sequence* CRDT (RGA/Fugue-style), which is the hard case.** You implement a simple one and **you use a library for the hard one and say so.**
- 🔴 **The design decision KERYX makes, and you must be able to defend it:** messages carry a **vector clock over relays** (not over clients — there are too many), delivery is **causally ordered**, and ties are broken by a deterministic total order (hash of the message id) so **every relay independently produces the identical sequence.** That is `ADR-0003`.

### 📄 SOURCES
- 📄 **Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System" (1978).** Eight pages. The most cited paper in the field. Read it three times across the year.
- 📕 **Kleppmann, *DDIA* — ch. 8 in full** (unreliable clocks, process pauses — **the theoretical spine of this project**) and **ch. 5's replication-lag section.**
- 📄 **Kleppmann, "A Critique of the CAP Theorem"** — short, and it will stop you saying CP/AP in an interview like it means something precise.
- 📄 **Shapiro et al., "Conflict-free Replicated Data Types" (2011)** — read §3–4.
- 📄 **Kleppmann's "CRDTs: The Hard Parts" talk** — the honest account of where sequence CRDTs get painful.
- 📄 **Jepsen's consistency model map** (`jepsen.io/consistency`) — one page. **Memorise the hierarchy.**

📈 **EXIT CRITERIA — MILESTONE K2**
- [ ] Vector clocks over relays implemented, with a documented compaction strategy and a measured size at 5 / 20 / 100 relays
- [ ] **🔴 No message is ever delivered before its causal predecessor.** Property-tested across **10,000 random interleavings** with random delays, drops and reorders
- [ ] **Every relay independently produces the identical delivered sequence** for the same message set — tested with three relays receiving messages in three different arrival orders
- [ ] A message whose predecessor never arrives: the **stated, tested policy** (buffer with a bound, then surface a gap to the client — never silently reorder and never block forever)
- [ ] The wall-clock version's failure reproduced and kept as a failing test, so the fix is *earned*
- [ ] **A clock jumping backwards 5 seconds mid-conversation changes nothing.** Asserted
- [ ] `docs/design/ordering.md` + **ADR-0003** — what order KERYX promises, what it does not, and where it sits on the Jepsen map

⛓ **PROBLEM CHAIN**
```
"kill -9 corrupted the log"      → fsync, CRC, WAL → and you cannot retry a failed fsync
"Timestamps ordered it wrong"    → clocks lie → Lamport → vector clocks → causal delivery
"Relay sequence numbers"         → ...need agreement between relays → too expensive per message
"Two relays produced different order"→ deterministic tie-break → identical sequence everywhere
"The vector clock got huge"      → per-relay not per-client → compaction → measure it
"A predecessor never arrived"    → bounded buffer + surface the gap → never silently reorder
"How do I snapshot while writing?"→ immutable SSTs + manifest → and L6 needs exactly this   (→ L6)
```

## 🎤 INTERVIEW PARAGRAPH — Week 18 (and CV v1)

> This level was storage and ordering, and the ordering half is the one I'd want to be asked about. Three people in a room, two of them reply at the same moment, and if you order by wall-clock timestamp the conversation reads as nonsense — a reply appears before the question, because the clocks disagreed by forty milliseconds. Nothing crashes and no metric moves. The fix people reach for is having the server assign sequence numbers, which works until there are two servers, and two servers can't agree on a single sequence cheaply across continents on every message. So messages carry a vector clock over *relays* rather than over clients — clients are too numerous — delivery is causally ordered, and ties break on a deterministic hash so every relay independently produces the identical sequence. I test that with three relays receiving the same messages in three different arrival orders and asserting they agree. Ten thousand random interleavings in CI.
>
> The storage half is a message log I wrote in C++ as an LSM tree, and the part I'd point at isn't the engine, it's the torture harness — a thousand kill cycles checking four invariants after every restart, with syscall-level fault injection through LD_PRELOAD: a `write` that succeeds but only writes half, an `fsync` that returns EIO. That last one taught me something I'd have got wrong: on some filesystems a failed fsync marks the pages clean anyway, so you can't retry it, you have to treat it as fatal. That's the bug that hit PostgreSQL. And the requirement that actually drove the design only matters later — I need a consistent snapshot of the log while appends continue, because that's what a relay joining a room backfills from and what Raft snapshots in month six. Realising my storage choice was really a replication choice is when the architecture clicked.

## 🎓 LEVEL 3 EXIT EXAM
1. Draw an LSM tree and a B+Tree. Give a workload where each wins decisively, and name the amplification factors.
2. `fsync` returns EIO. What do you do, and why can't you retry?
3. Your torture harness found zero bugs. What do you conclude, and what do you do next?
4. Explain the difference between Lamport timestamps and vector clocks. What can the second tell you that the first cannot?
5. Two relays receive the same five messages in different orders. Prove they deliver the same sequence.
6. A message arrives whose causal predecessor never does. Name four defensible policies and the domain each suits.
7. How do you take a consistent snapshot while appends continue? Why does Level 6 depend on it?
8. Place KERYX on the Jepsen consistency map, component by component.

**Pass = 7/8.**

### 🧩 TRACK I — L3 · W13–18 · 8h/wk
**DSA:** **trees and BSTs** (you just built a B+Tree under production constraints) · **heaps and top-K** (the causal delivery buffer is a priority queue) · **tries** · **topological sort — causal delivery *is* a topological order over a DAG of messages, and this is the single cleanest DSA-to-systems mapping in the whole roadmap.** NeetCode 150 sections 11–13 + LeetCode's topological-sort set. **~55 problems. Running total ≈173.**
**System design:** design a **key-value store**, and design a **distributed cache**. You have opinions now; use them.
**⚑ CV v1 written** — not for applying. It exists so an unexpected opportunity does not find you writing a CV in a panic.

---
---

# ⚡ LEVEL 4 — Federation

> **Goal:** two relays, owned by different people, running different builds, share a conversation correctly. **This is the level the project is named for.**
> **⏱ Weeks 19–23 · Jan 18 – Feb 21 2027 · 95h** · **Milestone K3** · **🚩 Flagship #4 `conform`** · **🤝 Referrals open W18** · **W23 = buffer + pre-Ramadan pull-forward** · **Fundamentals F8, F9**
>
> ☕ **This is the Java level, and Java is 53.3% of your target backend postings — the single most-demanded skill in your corpus.** It is not here as a keyword. The relay core, the federation state machine and the delivery engine are genuinely the right place for a managed language, and it is how every large messaging backend is actually built.

## 4.1 — Java 21, learned properly and fast

> ### 🔥 THE WALL
> Port your Level-3 delivery path to Java, naively — `ArrayList<Message>`, `HashMap<String, Room>`, streams API, objects everywhere. Fan out 100k messages to 10k subscribers beside the C++ version.
>
> It will be **5–20× slower and use 10× the memory.** Then look at where it actually went: not "Java is slow" but **allocation rate, pointer chasing through boxed objects, and GC pressure.** Turn on `-Xlog:gc*` and watch it.
>
> Then fix it the way real systems do — **off-heap `ByteBuffer`s for message bodies, primitive arrays for subscriber ids, object reuse, no allocation in the fan-out loop** — and get most of it back. **You have just learned the single most important thing about the JVM: it is fast when you stop making garbage.**

### 🔎 DIAGNOSE
```bash
java -Xlog:gc*:file=gc.log ...            # allocation rate and pause times
async-profiler -e alloc -d 30 <pid>       # WHERE the allocation happens — the killer tool
jcmd <pid> Thread.print                   # and jdk.tracePinnedThreads for virtual threads
```

### 📖 THEORY
- **Modern Java, not 2011 Java.** Records, sealed interfaces, pattern matching for `switch`, `var`, text blocks. Your federation event types are a sealed hierarchy of records — idiomatic Java 21, and it reads nothing like the Java people complain about.
- **The memory model** — `volatile`, `final`, happens-before. You are writing a concurrent delivery engine; this is not optional.
- **Virtual threads (JEP 444)** — a relay holds tens of thousands of in-flight deliveries. Virtual threads make a blocking-style delivery engine viable without a platform thread per delivery. **You benchmarked them against goroutines in Level 1**; now use them and report the real behaviour under load, including where they pin.
- **GC as an engineering parameter** — G1 vs ZGC, allocation rate as the thing you actually control, why `-Xmx` is not the interesting knob. **A GC pause in a relay becomes delivery lag becomes a client timeout becomes a reconnect storm** — the same chain as a compaction stall in Level 3.
- **Off-heap and the FFI boundary** — `ByteBuffer.allocateDirect`, and **JNI vs the Foreign Function & Memory API (JEP 442)** for calling `keryx-store` and `keryx-wire`. Choose one, measure the per-call overhead, batch across the boundary, and write **ADR-0004**.

### 📄 SOURCES
- 📕 **Goetz et al., *Java Concurrency in Practice* — ch. 3 (sharing objects), 5 (building blocks), 10 (liveness hazards), 11 (performance).** Still the reference; skip the dated executor material.
- 📄 **Aleksey Shipilëv's "JVM Anatomy Quarks"** — the allocation and GC entries. The best JVM performance writing that exists.
- 📄 **JEP 444 (Virtual Threads)**, **JEP 442 (FFM API)**, and Ron Pressler's "State of Loom."

## 4.2 — 🚩 FLAGSHIP #4: `conform` — the federation protocol and its adversary

> ### 🔥 THE WALL — five failures across the seam
> You have two relays. Make them share a room, and watch each of these bite:
> 1. **Relay B was offline for an hour.** It comes back. **What does it not know, and how does it find out?** Naive answer: ask for everything. At 10k messages that is fine; at 10M it is an outage.
> 2. **Relay B's clock is 4 seconds ahead.** Its messages sort into the future and pin to the top of everyone's timeline forever.
> 3. **Relay B is running last month's build** and sends a field yours does not know. Does yours drop it, crash, or preserve it? **If it drops it, and later re-signs the event, the signature is now wrong for everyone else.**
> 4. **Relay B claims a message from a user it does not host.** Nothing in a naive design stops it.
> 5. **Relay B sends the same message twice with different ids.** Your room now has a duplicate, and every other relay disagrees about it.
>
> **These five are why federation is hard, and none of them appears in a single-server design.**

### 📖 THEORY
- **The server-to-server protocol.** Transactions (a batch of events with a shared ack), retry with backoff, **idempotency by event id so a retried transaction is harmless** — the same problem as Level 3's dedup and it will appear a third time in Level 8's push. Say so.
- **Backfill.** How a joining or recovering relay catches up: request events *since* a known point, walk the causal DAG backwards, and bound the walk. **The depth limit and what you do when you hit it** is the interesting part.
- **Event signing and the authorisation DAG.** Each event is signed by its origin relay and names its causal parents. A relay may only originate events for users it hosts. **Membership is itself an event**, so "was Bob in the room when he said that?" is answerable from the DAG rather than from current state — which is how you resolve a partition where both sides changed membership.
- **Unknown-field preservation.** Canonical serialisation so a signature survives a round-trip through a relay that does not understand every field. **This is the subtlest bug in the level and it is a real one from Matrix's history.**
- **Capability negotiation and protocol versioning.** Two relays agree at handshake on a protocol version and a feature set. **A pinned old binary in CI must keep working.**
- **State resolution.** When two relays independently changed room state during a partition, the deterministic function that both run to reach the same answer. **Keep yours simple and say why** — Matrix's v2 algorithm is a well-known source of complexity and you are not obliged to repeat it.
- **Rate limiting a *peer*, not a user.** A federated relay is an untrusted client with a much bigger budget. Per-relay quotas, and what you do when a peer exceeds them (slow, then refuse, then defederate — and log it).

### 📄 SOURCES
- 📄 **The Matrix specification — the Server-Server API, in full.** This is the best-documented federated messaging protocol in existence. **Read it to learn the problems, then design your own and write down every place you diverge and why.** That comparison document is itself an interview artifact.
- 📄 **Matrix's "state resolution v2" explainer** and the blog posts about why v1 was replaced. A rare public record of a federation design failing and being fixed.
- 📄 **XMPP RFC 6120 §4–5** — read for the handshake and stream-negotiation model. Twenty-five years of federation experience compressed.
- 📄 **The `h2spec` conformance suite** — read its *structure*, not its content. It is the model for `conform`.
- 📕 **DDIA ch. 5** (replication) and **ch. 6** (partitioning) for the vocabulary your design doc is written in.
- 📄 **Kleppmann, "Making Sense of Stream Processing"** (free) ch. 1–3 — the log-as-truth framing that KERYX's event DAG is a cousin of.

### 🛠 THE BUILD · 80h — `keryx-relay` + `keryx-federate` (Java 21) + `lab/conform` (Python)

**`conform` is the flagship**: an adversarial conformance suite that runs against *any* implementation of your protocol over a socket. ~80 cases: malformed transactions, out-of-order events, events with unknown fields, events signed by the wrong relay, events claiming users the peer does not host, duplicate ids, backfill requests beyond the depth limit, version mismatches, and a **fuzzer** that mutates valid transactions.

📈 **EXIT CRITERIA — MILESTONE K3**
- [ ] **Two relays, separate processes, separate stores, exchange a room.** A message sent on A appears on B **in causal order, exactly once**
- [ ] **Backfill: relay B offline for 10,000 messages rejoins and converges**, with the walk bounded and the time measured against message count
- [ ] **All five wall failures have a test asserting the correct behaviour**, especially #3 — **an event round-trips through a relay that does not understand one of its fields and its signature still verifies**
- [ ] **`conform` passes 100% against your own relay**, and you run it against a deliberately-broken build to prove it catches things. **Report the count: "N/N cases passing" is an unfakeable claim**
- [ ] Per-relay rate limiting with a stated escalation policy; a misbehaving peer is slowed, then refused, then defederated — and each is logged and counted
- [ ] **Java fan-out within 2× of the C++ path**, with the gap attributed to named mechanisms — or a written explanation of why not
- [ ] **Zero allocation in the steady-state fan-out loop**, proven by `async-profiler -e alloc` showing a flat profile over a 10-minute run
- [ ] Virtual-thread delivery engine runs ≥10,000 concurrent deliveries; **pinning incidents detected and reported**
- [ ] **ADR-0004** (JNI vs FFM, with the measured per-call cost) and **ADR-0005** (why your state resolution is simpler than Matrix's)
- [ ] `docs/design/federation.md` — the protocol, the threat model at the seam, and **`docs/design/vs-matrix.md`**, every place you diverge and why

⛓ **PROBLEM CHAIN**
```
"Java fan-out was 15× slower"  → allocation rate → off-heap → reuse → not "Java is slow"
"GC pause became delivery lag" → same chain as compaction → latency budgets everywhere    (→ L3)
"B was offline for 10M messages"→ backfill → bounded DAG walk → the depth limit
"B's clock was 4s ahead"       → you already solved this → causal order, not wall clock   (→ L3)
"B dropped a field and re-signed"→ unknown-field preservation → canonical serialisation
"B claimed a user it doesn't host"→ event signing → origin authority → the auth DAG
"B sent the same message twice"→ idempotency by event id → third time you've seen this    (→ L8)
"Both sides changed membership"→ state resolution → deterministic, and keep it simple
"How do I know B is correct?"  → you don't → a conformance suite → and it must be hostile
"What if B just lies?"         → ...that's a different problem                            (→ L7)
```

## 🎤 INTERVIEW PARAGRAPH — Week 23

> This month the project became federated: two relays, separate processes, separate databases, sharing a conversation. Five things bit me and none of them exists in a single-server design. A relay that was offline for ten thousand messages has to catch up, and the naive answer — ask for everything — is fine at ten thousand and an outage at ten million, so backfill is a bounded walk backwards through the causal DAG with a depth limit and a stated policy for hitting it. A peer running last month's build sends a field I don't know, and if I drop it and later re-sign the event, the signature is now wrong for everyone else — so unknown fields are preserved through canonical serialisation, which is the subtlest bug at the seam and a real one from Matrix's history. And a peer can simply claim a message from a user it doesn't host, which nothing in a naive design stops, so every event is signed by its origin relay and membership is itself an event in the DAG — which means "was Bob in the room when he said that" is answerable from history rather than from current state, and that's how you resolve a partition where both sides changed membership.
>
> The artifact I'd point at is the conformance suite. It's an adversarial harness that runs against any implementation of my protocol over a socket — eighty-odd cases plus a fuzzer that mutates valid transactions — and I run it against a deliberately broken build to prove it actually catches things. `h2spec` exists for HTTP/2 and nothing like it exists for a federation protocol, and "eighty out of eighty cases passing" is a claim someone else can check.

## 🎓 LEVEL 4 EXIT EXAM
1. Your Java fan-out is 15× slower than C++. Name the three real causes in order, and how you'd confirm each.
2. A relay rejoins after 10M messages. Design the catch-up. What is bounded, and what happens at the bound?
3. A peer sends an event with a field you don't understand. What must happen and why?
4. A peer claims a message from a user it doesn't host. What stops it?
5. Two relays changed room membership during a partition. Describe the resolution and why it must be deterministic.
6. Why does a GC pause in a relay become a reconnect storm? Trace it.
7. What does your conformance suite prove, and what does it not?
8. Your protocol versus Matrix's: name three places you diverge and defend each.

**Pass = 7/8.**

### 🧩 TRACK I — L4 · W19–23 · 8h/wk
**DSA:** **dynamic programming** (1-D, 2-D, knapsack) and **greedy** · **graphs part 2 — DAGs, cycle detection, shortest path.** The causal DAG you are walking in backfill is exactly this, and cycle detection is a real safety check in your event graph. NeetCode 150 DP + advanced graphs. **~50 problems. Running total ≈223.**
**System design:** design a **chat system** (you will have opinions nobody else in the room has), and design a **news feed** — fan-out on write vs read, **the celebrity problem and the hybrid solution.** The celebrity problem is Level 8's presence problem wearing a different hat.
**🤝 Referrals open Week 18** — see §XIV.4. Three conversations a month from here.

---
---

# ⚡ LEVEL 5 — 🌙 Cryptography & the Threat Model

> **Goal:** the relay forwards what it cannot read — and you can say precisely what that does and does not protect.
> **⏱ Weeks 24–27 · Feb 22 – Mar 21 2027 · 44h** · **Milestone K4** · **📺 Boneh Crypto I, MIT 6.858** · **W27 = REST WEEK + half-year gate**

> ## 🌙 RAMADAN — READ BEFORE STARTING
> **Ramadan 1448 ≈ 8 Feb – 9 Mar 2027**, spanning weeks 22–26. **Weeks 23–26 are budgeted at 20 hours, not 32.** Week 27 is a rest week at 10h.
>
> **This level is here on purpose.** It is the reading-and-specification level: Boneh's lectures, the Signal specification, 6.858's threat-model material, and an implementation that is deliberately *small* because **you invent nothing**. That is what a reduced week can actually carry. The heavy build levels sit either side of it.
>
> **Mitigations already applied:** the Boneh weeks 1–2 lectures are watched in W22's buffer; the X3DH and Double Ratchet specs are read in W22; libsodium is already wired in from Level 1's crypto envelope.
>
> Reduced split: **11h Depth / 5h Interview / 2h Fundamentals / 2h Craft.** **The interview track drops to 5h. It does not stop.**

## 5.1 — "We encrypt it" is not a security claim

> ### 🔥 THE WALL — four attacks on the obvious design
> Encrypt each message with a shared AES key per room. Then:
> 1. **The relay operator dumps the database.** Nothing is readable. Good — this is the part that works.
> 2. **A key leaks today.** **Every message ever sent in that room, including three years of history the attacker captured earlier, is now readable.** There is no forward secrecy.
> 3. **Alice adds a new phone.** Either it can read the whole history — so a stolen phone is a full breach — or it can read nothing, which users will not accept. **You must choose, deliberately, and say so.**
> 4. **The relay silently swaps Bob's public key for its own**, forwards, re-encrypts, and reads everything. **Neither Alice nor Bob sees anything unusual.** This is the attack that matters and the one that naive designs lose to.
>
> **Attack 4 is the level.** Confidentiality without key-change detection is theatre.

### 📖 THEORY
- **The primitives, and the rule.** AEAD (ChaCha20-Poly1305), X25519 key agreement, HKDF, Ed25519 signatures. **You implement none of them — libsodium does.** Your job is to compose them correctly, and composition is where real systems fail.
- **Why forward secrecy needs ratcheting.** A static shared key means one compromise reads all history. A **symmetric ratchet** (derive the next message key, delete the last) gives forward secrecy. A **Diffie-Hellman ratchet** (new ephemeral keys as the conversation goes back and forth) additionally gives *post-compromise security* — recovery after a compromise. **The Double Ratchet is both, composed.**
- **X3DH** — how two parties agree a key when one of them is asleep. Prekeys, one-time prekeys, and the exhaustion problem when someone burns them all.
- **Out-of-order and lost messages.** The ratchet advances per message; a message that arrives late needs its key retained. **Skipped-key storage is a memory-exhaustion attack surface** and it needs a bound.
- **Multi-device.** Per-device subkeys, cross-signing, and the honest tradeoff on history: **KERYX's choice is that a new device receives nothing prior to its enrolment, and history is opt-in per room via an explicitly-shared history key.** State it, test it, defend it.
- **🔴 Key-change detection** — the answer to attack 4. Safety numbers, and a UI event the user cannot miss. **Test that a swapped key produces a visible, testable signal**, because a security property with no test is an intention.
- **The threat model as a document** *(6.858)* — what you defend against, what you do not, and **what each layer assumes has already failed.** Defence in depth stated as a principle.
- **Metadata.** Your relays learn who talks to whom and when. **That is a real limitation and you state it in the README rather than hoping nobody asks.**

### 📄 SOURCES
- 📺 **Boneh, Cryptography I — weeks 1–4** (stream ciphers, block ciphers, message integrity, authenticated encryption). Free on Coursera.
- 📄 **The Signal Double Ratchet specification** and **the X3DH specification.** Both public, both short, both the thing you implement.
- 📄 **Cohn-Gordon et al., "A Formal Security Analysis of the Signal Messaging Protocol" (EuroS&P 2017)** — read the security-properties section so you can state precisely what the ratchet gives you.
- 📕 **Aumasson, *Serious Cryptography* 2nd ed. — ch. 1, 3, 8, 9, 10, 11.**
- 📺 **MIT 6.858 — the threat-model lecture, the network-security lectures, and the side-channel lecture.**
- 📄 **The libsodium documentation** on `crypto_kx`, `crypto_aead`, `crypto_kdf`, and `sodium_memzero`. Read the "do not do this" sections twice.
- 📄 **Matthew Green's blog** on the Double Ratchet — the intuition the spec assumes you have.

### 🛠 THE BUILD · 36h — `keryx-ratchet` (Java 21) + `keryx-wire/crypto` (C++20)

📈 **EXIT CRITERIA — MILESTONE K4**
- [ ] X3DH implemented: two parties agree a key **when one is offline**. Prekey exhaustion has a tested, stated fallback
- [ ] Double Ratchet implemented: symmetric + DH ratchet, **skipped-message keys retained with a hard bound** and the bound tested by attack
- [ ] **🔴 A relay operator with full database and disk access cannot read a message.** Demonstrated: dump the store, show ciphertext, show the decryption failing
- [ ] **Forward secrecy demonstrated:** compromise a current key, show that captured prior ciphertext stays unreadable
- [ ] **Post-compromise security demonstrated:** compromise a key, let the conversation continue, show that later messages are unreadable to the same attacker
- [ ] **Multi-device:** a device added mid-conversation receives subsequent messages and **provably not prior ones**. Asserted by test
- [ ] **🔴 A silently swapped public key produces a detectable, tested signal** — safety-number mismatch surfaced, not logged
- [ ] Out-of-order and 24-hour-late messages decrypt correctly
- [ ] All secret material in zeroizing types; **no key ever written to a log, including at debug level** — enforced by a CI grep
- [ ] `docs/design/threat-model.md` — the layers, what each assumes has failed, and 🔴 **an explicit section on what you do NOT defend against**: metadata, a compromised endpoint, a global passive adversary, traffic analysis

⛓ **PROBLEM CHAIN**
```
"One key leak read everything"  → forward secrecy → symmetric ratchet
"Recovery after compromise?"    → DH ratchet → post-compromise security → both = Double Ratchet
"New phone reads all history"   → per-device keys → and you must CHOOSE, and say so
"The relay swapped Bob's key"   → key-change detection → safety numbers → a TESTED signal
"Skipped keys ate my memory"    → bound them → a crypto design is an availability surface too
"The operator sees who talks to whom"→ metadata → you do NOT solve this → say it in the README
```

## 🎤 INTERVIEW PARAGRAPH — Week 27 (and the half-year gate)

> This level was end-to-end encryption, and the useful thing is the attack that beats the obvious design. If you encrypt each room with a shared key, then a relay operator dumping the database gets nothing — which is the part people stop at. But a key leaking today reads three years of captured history, because there's no forward secrecy. So you ratchet: derive the next message key and delete the last, which protects the past; and run a Diffie-Hellman ratchet as the conversation goes back and forth, which lets you *recover* after a compromise. That's the Double Ratchet, and it's Marlinspike and Perrin's design — I implemented their published spec and invented nothing, which is the correct posture in cryptography.
>
> The attack that actually matters is the fourth one. The relay swaps Bob's public key for its own, forwards, re-encrypts, and reads everything, and neither party sees anything unusual. Confidentiality without key-change detection is theatre. So a swapped key produces a safety-number mismatch that's surfaced as a testable event, and I assert it in CI, because a security property with no test is an intention. And I say the limitation out loud rather than waiting to be asked: my relays learn who talks to whom and when. I don't defend against metadata analysis and I'm not going to pretend otherwise — that's Tor's problem and it's a different system.

## 🎓 LEVEL 5 EXIT EXAM
1. Forward secrecy and post-compromise security. Which ratchet gives which, and why do you need both?
2. Two parties agree a key while one is offline. Walk through X3DH. What happens when prekeys are exhausted?
3. A relay swaps a public key. What detects it, and what must the user see?
4. A new device joins mid-conversation. Name the three defensible history policies and who each suits.
5. Skipped-message keys are a memory-exhaustion surface. Explain the attack and your bound.
6. Your messages are E2E encrypted. Name four things the relay operator still learns.
7. Your threat model has four layers. For each, state what it assumes has already failed.

**Pass = 6/7.**

### 🧩 TRACK I — L5 · W24–27 · 5h/wk *(Ramadan-reduced)*
**Review and re-solve only. No new topics.** Work the queue in `dsa/FAILURES.md` — every failed problem re-solved from scratch without looking at your previous solution. **Keep the daily streak; that is the whole objective this month.** **~20 problems. Running total ≈243.**
**System design:** one design only — **design a system with end-to-end encryption** (you are doing it). Written, not timed.
**W27:** **failure-category count**, plus the 🚩 **half-year gate** below.

> ### 🚩 HALF-YEAR GATE — end of Week 27
> Six months. Check honestly: **is there a working federation — two independently-run relays sharing a causally-ordered, end-to-end-encrypted conversation over a transport you wrote, backed by a message log that survives being killed?**
>
> If yes, you are on plan and the second half is where the corpus gaps close.
> If no, read §XVII **now**, before Level 6, and **seriously reconsider the Extended Track.** Eighteen months is a legitimate choice; a rushed Level 6 through 9 is not.

---
---

# ⚡ LEVEL 6 — Consensus & Replication

> **Goal:** a relay is a *cluster*, not a machine — and a machine dying mid-delivery loses nothing and duplicates nothing.
> **⏱ Weeks 28–34 · Mar 22 – May 9 2027 · 133h** · **Milestone K5** · **🚩 Flagship #5 `raft`** · **📺 MIT 6.5840 Labs 1–3** · **⚑ CV v2** · **W34 = buffer** · **Fundamentals F10, F11**
>
> **This is the longest level in the plan and the one it was chosen for.** Distributed systems is named in **48.9% of backend postings and 57.0% of backend+infra** — the highest-frequency technical skill in your entire corpus — and this is where you earn it.

## 6.1 — Why one relay process is not a relay

> ### 🔥 THE WALL
> Your relay is one process holding room state. Kill it mid-fan-out — after it has accepted a message from Alice and acknowledged it, but before it has delivered to all 500 subscribers.
>
> Restart. **Some subscribers have the message and some do not, and the relay has no idea which.** Re-deliver to everyone and you duplicate. Re-deliver to nobody and you lose. **Both are visible to users and neither is detectable by a health check.**
>
> Now run two relay processes for redundancy, both accepting messages for the same room. **Now they disagree about the room's state, and each is confident.** You have made it worse.

### 📖 THEORY — this is 6.5840, and you do Labs 1–3
- **Why a single machine is not an availability story**, and why two machines without agreement is *worse* than one.
- **Raft in full** *(Lab 3)*: terms · randomised election timeouts and why randomisation is load-bearing rather than a detail · RequestVote and the up-to-date-log check · AppendEntries · the **log matching property** · commit index advancement · applying to the state machine · membership changes · log compaction and snapshots.
- **🔴 The Figure 8 case** — why a leader may not directly commit an entry from a *previous* term, and the no-op-on-election fix. **This is the subtle part of Raft, it is what interviewers probe, and you must be able to draw it at a whiteboard from memory in five minutes.**
- **The state machine is delivery.** KERYX's replicated log is the *room's ordered event sequence*; applying an entry means "this message is now durably accepted by the cluster." **Delivery to subscribers happens after commit, and is idempotent by event id** so a re-delivery after failover is harmless. That framing — *what exactly is the state machine?* — is the question that separates people who implemented Raft from people who read about it.
- **At-most-once RPC** *(Lab 2)* — request ids, duplicate detection, and why a client retrying is the normal case rather than the exception. **This is the fourth time you have met idempotency.**
- **Read-only optimisations** — ReadIndex and lease reads: how etcd serves linearizable reads without a log write. Measure the difference.
- **Leases and fencing tokens** — a relay whose lease expired **must not be able to deliver on behalf of the cluster.** A TTL-based lock is not a lock in an asynchronous system.
- **Why one Raft group per room shard, not one globally.** A global Raft group across every room is absurd; the keyspace is sharded and each shard has a small group. **The sharding decision is ADR-0006 and it is the central architecture of the relay cluster.**
- **What consensus does NOT give you.** It gives at-most-once *acceptance*. It does not prevent duplicate *delivery* to a subscriber who was mid-receive during failover. **Your exactly-once story is: consensus on acceptance + idempotent delivery keyed by event id + client-side dedup.** Say all three; candidates who name only the middle one have read about it rather than built it.

### 📄 SOURCES
- 📺 **MIT 6.5840 — all lectures with their assigned papers, and Labs 1, 2 and 3.** Lab 4 is a W34 stretch goal.
- 📄 **Ongaro & Ousterhout, "In Search of an Understandable Consensus Algorithm" — the EXTENDED version.** §5 in full, §6 (membership) carefully. The conference version omits crucial detail.
- 📄 **Ongaro's PhD thesis** — for log compaction and membership changes done properly.
- 📄 **Jon Gjengset, "Students' Guide to Raft."** **Read it before you start, not when you are stuck.**
- 📕 **DDIA ch. 9 in full** (consistency and consensus) and **ch. 8** re-read.
- 📄 **Kleppmann, "How to do distributed locking"** — then antirez's reply. **Read both.** Fencing tokens.
- 📄 **`thesecretlivesofdata.com/raft/`** — the visualisation, for intuition before the paper.
- 📄 *Optional in W34's buffer:* **Fly.io's Gossip Glomers 1–4** — Maelstrom checks your consistency for you.

### 🛠 🚩 FLAGSHIP #5 — `raft` + MILESTONE K5 · 115h

6.5840's Labs 1–3, then `keryx-raft` (Java 21) as KERYX's relay cluster on top of the same understanding — **and the second implementation, in a second language, is where the understanding shows.**

📈 **EXIT CRITERIA**
- [ ] **6.5840 Labs 1, 2 and 3 pass MIT's test suites**, including `TestFigure8Unreliable`. Screenshot in the README
- [ ] Leader elected from 5 nodes; **re-elected within the timeout after a leader kill; no split-brain across 1,000 randomised runs**
- [ ] **Partition test: a minority partition CANNOT commit, across 500 randomised partition schedules.** On heal, the minority's uncommitted entries are correctly overwritten
- [ ] **The Figure 8 scenario constructed deliberately as a test**, and the commit rule shown to prevent it. Then: **you draw it at a whiteboard in under five minutes from memory, tested by a human in W33**
- [ ] ReadIndex or lease reads implemented; **linearizable reads served without a log write**, latency difference measured
- [ ] Membership change (add and remove a relay) without losing availability; **log compaction and snapshot install** working
- [ ] **Every failure reproducible from a seed integer alone, on any machine.** The harness that makes this true is what makes Level 7 possible
- [ ] **K5: kill the leader mid-fan-out under sustained load — no message lost, none delivered twice, none reordered.** Verified by reconciling every subscriber's received log against the sender's
- [ ] **Fencing tokens: a relay whose lease expired cannot deliver on the cluster's behalf.** Demonstrate the violation without them and the fix with them, **same seed**
- [ ] **ADR-0006** — room sharding and one Raft group per shard, argued
- [ ] `docs/design/consistency.md` — what is linearizable (room acceptance), what is causal (cross-room), what is eventual (presence, read receipts), and **what a client is actually promised**

⛓ **PROBLEM CHAIN**
```
"Killed mid-fan-out: some got it"→ acceptance must be replicated before delivery
"Two relays, both confident"    → hashing isn't agreement → Raft
"Can't tell slow from dead"     → you never can → design for at-least-once + idempotence
"Split votes never resolved"    → randomised election timeouts → randomness is load-bearing
"A committed entry vanished"    → Figure 8 → the previous-term commit rule
"Expired lease-holder delivered"→ fencing tokens → a TTL is not a lock
"One global Raft group?"        → absurd → shard by room → ADR-0006
"Linearizable read cost a write"→ ReadIndex / lease reads
"How do I test all of this?"    → you can't by hand → deterministic simulation            (→ L7)
```

## 🎤 INTERVIEW PARAGRAPH — Week 34 (and CV v2)

> This is the level the project exists for. A relay that's one process holding room state is not an availability story — kill it after it's accepted a message from Alice and acknowledged her but before it's delivered to all five hundred subscribers, and some have it and some don't and the relay has no idea which. Re-deliver to everyone and you duplicate; re-deliver to nobody and you lose. Both are visible to users and invisible to a health check. So acceptance is replicated through Raft before anything is delivered, which I implemented from the extended paper — and I did MIT 6.5840's labs first, so the second implementation, in a different language, is where the understanding shows. Labs one through three pass, including TestFigure8Unreliable, which humbled me for about a week.
>
> Two things I'd flag. The first is the framing question that separates people who implemented Raft from people who read about it: *what is the state machine?* Mine is the room's ordered event sequence, so applying an entry means "the cluster has durably accepted this message," and delivery happens after commit and is idempotent by event id so a re-delivery after failover is harmless. And I'd say precisely what consensus gives me: at-most-once *acceptance*. It does not prevent duplicate *delivery* to a subscriber who was mid-receive during a failover. My exactly-once story is consensus on acceptance, plus idempotent delivery keyed by event id, plus client-side dedup — three mechanisms, and I'd rather say that than claim something I can't support. The second is fencing tokens: a relay whose lease expired must not be able to deliver on the cluster's behalf, and I can show you the same seed producing duplicate delivery without them and correctness with them.

## 🎓 LEVEL 6 EXIT EXAM
1. Draw Raft's Figure 2 from memory.
2. Explain the Figure 8 scenario and the rule that fixes it. Five minutes, whiteboard.
3. What is KERYX's replicated state machine? Why is that the right choice?
4. Why is randomising the election timeout load-bearing rather than a detail?
5. A minority partition. What can it do, what can't it, and how does it find out?
6. Explain fencing tokens. Give KERYX's concrete failure without them.
7. What does consensus NOT give you here? State the exactly-once story precisely, all three parts.
8. Why one Raft group per room shard rather than one globally? What does the sharding cost you?
9. Place KERYX on the consistency map, component by component.

**Pass = 8/9.** *This is the hardest exam in the document.*

### 🧩 TRACK I — L6 · W28–34 · 8h/wk
**DSA:** **union-find** (shard membership) · **reductions and NP-hardness** (W28 is a *proving* week — three written reductions from Skiena ch. 9) · **advanced graphs** — SCC, bridges, **articulation points** (*which relay's removal partitions your federation?* — a real question about your own system) · **math and modular arithmetic.** LeetCode company-tagged sets begin here. **~60 problems. Running total ≈303.**
**System design:** design a **distributed lock service**, and design a **sharded database**. **W33: first human mock + the Figure 8 whiteboard test** — a checkable gate, not a formality.
**⚑ CV v2 written.**

---
---

# ⚡ LEVEL 7 — Correctness: Simulation & Deterministic Testing

> **Goal:** test the combinations of failures you cannot construct by hand — including a relay that lies. **The rarest skill in this document.**
> **⏱ Weeks 35–38 · May 10 – Jun 6 2027 · 66h** · **Milestone K6** · **🚩 Flagship #6 `keryxsim`** · **W38 = REST WEEK** · **Fundamentals F12, F13**

## 7.1 — 🚩 FLAGSHIP #6: `keryxsim`

> ### 🔥 THE WALL
> KERYX passes every test you have. Now answer: **what happens if relay B partitions asymmetrically from relay C, while A's clock jumps backwards four seconds, while a Raft leader election is in progress, while a disk returns `EIO` mid-snapshot, while relay D claims a message from a user it does not host — all within the same three seconds?**
>
> You cannot construct that by hand. There are millions of orderings. **So make the entire universe deterministic and let a seeded PRNG explore it for you.**

### 📖 THEORY

```
Real                        Simulated
──────────────────────────────────────────────────────────────────
System.nanoTime()      →    sim.Clock      (advances only when you say; can go BACKWARDS)
sleep / timers         →    sim.Timer      (instant; advances virtual time)
network / RPC          →    sim.Network    (delay, drop, reorder, duplicate, ASYMMETRIC PARTITION)
disk / fsync           →    sim.Disk       (torn writes, EIO, tail truncation on crash)
task scheduling        →    sim.Scheduler  (deterministic single-threaded interleaving)
rand                   →    rng            (seeded)
a relay's behaviour    →    sim.Relay      (honest | crashed | slow | LYING)   ← the KERYX one
```

Then `for seed in 0..100_000 { run(seed) }`. **When one violates an invariant you have a seed integer that reproduces it exactly, forever, on any machine.**

**🔴 The KERYX-specific contribution: `LyingRelay` as a first-class fault.** FoundationDB's and TigerBeetle's simulators model crashes, partitions and disk faults — the *fail-stop* world. **A federation's peers are not fail-stop: they are other people's servers.** Variants worth injecting: a relay that drops events it should forward · one that reorders them · one that **claims a message from a user it does not host** · one that **omits an event from backfill** so history silently differs · one that **behaves correctly only when probed.** The last two are where the real bugs live, and neither is reachable by a conventional test.

**The invariants, checked continuously — not just at the end:**
1. **No message is delivered before its causal predecessor**, on any relay
2. **Every relay that has an event agrees on its position in the room's order**
3. No acknowledged message is ever lost
4. No message is delivered twice to the same device
5. A minority partition never commits a Raft entry
6. **A lying relay cannot cause an honest relay to deliver a forged message**
7. The message log's integrity holds: every acknowledged event is retrievable and its signature verifies

**And TLA+ on the one protocol that most needs it** *(F11)*: spec the **federation catch-up and state-resolution protocol**, model-check the safety invariant *"two honest relays that have seen the same event set deliver the same sequence,"* and find at least one real design bug TLC catches that your tests did not.

### 📄 SOURCES
- 📄 **Will Wilson, "Testing Distributed Systems w/ Deterministic Simulation" (Strange Loop 2014).** **Watch in Week 34. The most valuable 40 minutes in this roadmap.**
- 📄 **Zhou et al., "FoundationDB" (SIGMOD 2021) — §4 on simulation.**
- 📄 **TigerBeetle's VOPR and simulation posts** — open source, readable, modern. Study the code.
- 📄 **Hillel Wayne, `learntla.com`** — free, the best TLA+ on-ramp.
- 📄 **Newcombe et al., "How Amazon Web Services Uses Formal Methods" (CACM 2015)** — read first, to understand why the hours are worth it.
- 📄 **Kyle Kingsbury (aphyr), any three Jepsen analyses** — the register of a person finding real bugs in real systems. Read for the *method*.
- 📄 **Go's `testing/synctest`** and **`madsim`** (Rust) — real implementations of the technique to compare against.

### 🛠 THE BUILD · 56h — MILESTONE K6

📈 **EXIT CRITERIA**
- [ ] All seven simulated components, including **asymmetric partitions** and a **clock that runs backwards**
- [ ] **`LyingRelay` with all five behaviours**, injectable per-seed
- [ ] **10,000+ seeds nightly in CI**, each simulating hours of virtual time in milliseconds. Report the speedup factor
- [ ] **🔴 ≥3 real bugs found this way, each documented with its seed and a human-readable event trace, in the README.** *This is the deliverable.* **A harness that finds nothing means your fault injection is too gentle — go and make it worse**
- [ ] **Any failure reproducible from its seed alone, on any machine**
- [ ] **A lying-relay scenario that an honest relay correctly rejects**, with the seed — and a written statement of **what a lying relay can still do that you cannot prevent** (it can refuse to forward; it can reveal metadata; those are real and you say so)
- [ ] TLA+ spec of the catch-up protocol; model-checks the ordering safety invariant; **≥1 real design bug found by TLC**, with its counterexample trace
- [ ] `docs/analysis/tla-vs-dst.md` — **they catch different classes of bug**, and articulating that distinction is a genuinely senior insight
- [ ] **F12 audit done:** if your benchmark harness had coordinated omission, **every benchmark is re-run** and the before/after is in `bench/RESULTS.md`
- [ ] **Published post: "Three bugs in my federated messaging system that no test suite would have caught."** With the seeds

⛓ **PROBLEM CHAIN**
```
"Can't test 5 simultaneous faults"→ make the universe deterministic → seeded exploration
"Found a bug, can't reproduce it" → seeds → reproducibility is the whole point
"Simulator found nothing"         → faults too gentle → make them worse
"A peer is not fail-stop"         → LyingRelay → the fault class FDB doesn't model
"It only misbehaved when probed"  → the nastiest variant → and the one that finds real bugs
"TLC found what tests didn't"     → model checking explores; tests sample
"Is the simulator even right?"    → validate against the real federation → sim-fidelity     (→ L11)
```

## 🎤 INTERVIEW PARAGRAPH — Week 38

> This month was correctness, and the technique is deterministic simulation testing — the FoundationDB approach. Every source of nondeterminism is behind an injectable port: the clock, the network, the disk, the scheduler, the RNG. In simulation each is replaced by an implementation driven by one seeded PRNG, so a whole run — hours of virtual time, thousands of messages, a dozen injected failures — is a pure function of an integer. Ten thousand seeds a night, and when one violates an invariant I have a seed that reproduces it exactly, forever, on any machine. It found three real bugs no test suite of mine would have caught.
>
> The part that's specific to my system is the fault type nobody else models. FoundationDB and TigerBeetle simulate crashes, partitions and disk faults — the fail-stop world. But a federation's peers aren't fail-stop, they're *other people's servers*, so I model a relay that stays up, responds promptly, and lies: drops events it should forward, claims a message from a user it doesn't host, or omits an event from backfill so two relays' history silently differs. The last one is the nastiest, because nothing fails and nothing alerts and the two servers just quietly disagree about what was said. And I'm honest about the limit: a lying relay can always refuse to forward and can always see metadata. I detect forgery. I can't detect silence.

## 🎓 LEVEL 7 EXIT EXAM
1. Explain deterministic simulation testing to a sceptical manager in 90 seconds, including adoption cost.
2. Name three things that must be true of your architecture for DST to be possible at all.
3. Give an invariant in KERYX a unit test cannot check but a simulation can.
4. Why is `LyingRelay` a different fault class from `CrashedRelay`? What does it break that crashes don't?
5. A relay omits one event from backfill. What is the observable symptom, and how long until anyone notices?
6. TLA+ and DST catch different bugs. Give an example of each the other would miss.
7. Your simulator ran clean for 10,000 seeds. What does that prove, and what does it not?

**Pass = 6/7.**

### 🧩 TRACK I — L7 · W35–38 · 8h/wk
**DSA:** **backtracking and state-space search** — model checking and DST are structurally a systematic search over interleavings, and this is the week that connection is live · **probability and expectation** · randomised algorithms, reservoir sampling, **Bloom filters and HyperLogLog** (you will need the second one for presence in Level 8). **~48 problems. Running total ≈351.**
**System design:** design a **rate limiter** and design a **metrics/monitoring system.** You build both in the next two levels.
**W38 rest week:** **failure-category count** + the **Final Gauntlet** (§XVIII) + **Full Timed Loop #1.**

---
---

# ⚡ LEVEL 8 — Presence, Overload & Kubernetes

> **Goal:** stay useful when far more work arrives than the federation can do — and ship the page that makes a recruiter call. **This is where the corpus percentages start closing.**
> **⏱ Weeks 39–42 · Jun 7 – Jul 4 2027 · 76h** · **Milestone K7** · **🚩 Flagship #7 `presence-storm`** · **★ THE PUBLIC DEMO** · **⚑ CV v3** · **Fundamentals F14, F15**

## 8.1 — 🚩 FLAGSHIP #7: `presence-storm` — the O(N²) problem that kills every chat system

> ### 🔥 THE WALL
> A room with 5,000 members. Everyone's client sends a presence heartbeat every 30 seconds, and the relay broadcasts each to every member.
>
> **That is 5,000 × 5,000 / 30 = 833,000 messages per second, for a room where nobody said anything.** Your relay is now spending 100% of its CPU telling people who is online. Plot it against room size and watch the curve go vertical.
>
> Then the second wall: **a network blip disconnects all 5,000 at once.** They all reconnect immediately, all re-subscribe, all re-sync, and all re-broadcast presence. **Your own redeploy is a self-inflicted DDoS**, and it is the single most common way real chat systems fall over.
>
> Then the third: **drive the whole federation to 5× capacity with an open-loop generator and plot goodput** — messages successfully delivered *and acknowledged* per second. **It does not plateau. It collapses toward zero**, because the relay spends everything on deliveries that will time out before they land.

### 📖 THEORY
- **Little's Law: `L = λW`.** Concurrency = arrival rate × latency. A five-second calculation most engineers never make.
- **The queueing curve.** M/M/1: `W = S/(1−ρ)`. At ρ=0.5, 2× service time. At ρ=0.9, 10×. At ρ=0.99, 100×. **Memorise this shape** — it explains why you do not run at 90% utilisation.
- **Presence, done the way it actually has to be done:** debounce and batch · **aggregate per room rather than per member** · a **probabilistic member-count** (HyperLogLog) instead of an exact one for large rooms · lazy presence — send it only to members with the room *open* · and **stop broadcasting presence entirely above a room-size threshold**, which is what every large system does and almost nobody explains. Measure the threshold rather than guessing it.
- **Fan-out on write vs fan-out on read**, and the **celebrity problem**: a 50,000-member room is the chat equivalent, and the answer is the same hybrid. You met this in Level 4's system-design work; now you build it.
- **Backpressure through the delivery path.** Credit-based flow control, bounded queues everywhere with a **written** full-queue policy, and **why a messaging system's correct response to overload is to slow acceptance rather than to drop** — a dropped message is data loss, a delayed one is lag. Know when each is acceptable and say so.
- **Overload responses in order:** bounded queues → **drop deliveries whose deadline has passed** (cheapest large win: never work on something nobody is waiting for) → **shed by priority, never randomly** — a message beats a read receipt beats a typing indicator, and **random shedding corrupts the conversation** → adaptive concurrency limits (infer capacity from observed latency; Netflix's approach and the modern right answer) → autoscale.
- **Retry amplification and metastable failure** — the system stays broken *after* the trigger is removed because the reconnect backlog is self-sustaining. **Recovery requires shedding, not just fixing the trigger.** Extremely impressive in a design interview and almost nobody knows it by name.
- **Reconnect storms and jitter.** Exponential backoff with **full jitter**, and a `Retry-After` the client actually honours. **Without jitter your redeploy is the DDoS.**
- **Kubernetes** — the reconciliation loop (`while true { observe; diff; act }`); what happens between `kubectl apply` and a running pod (12+ steps, a top-5 interview question); **cgroups v2 and the JVM** (`memory.max` vs `memory.high`, why the container limit counts heap *plus* metaspace *plus* thread stacks *plus* your off-heap message buffers, `-XX:MaxRAMPercentage`); **CPU throttling** and finding `nr_throttled` in `cpu.stat`, invisible from inside the container; **graceful shutdown for a stateful relay** — SIGTERM → stop accepting → finish in-flight deliveries → hand off Raft leadership → exit inside `terminationGracePeriodSeconds`. **Getting that wrong loses messages on every deploy.**
- **RED per service, USE per resource.** Histograms, not summaries — **you cannot average percentiles.** Cardinality as the thing that blows up the bill. **And the five messaging-specific signals: delivery lag, federation transaction backlog, presence broadcast rate, reconnect rate, and per-room fan-out amplification.** Those five are the dashboard you would actually open at 3am.

### 📄 SOURCES
- 📄 **AWS Builders' Library** — *"Using load shedding to avoid overload"*, *"Timeouts, retries and backoff with jitter"*, *"Avoiding insurmountable queue backlogs"*, *"Workload isolation using shuffle-sharding"*, *"Caching challenges and strategies"*. **Read the whole library across Levels 8–9. The best free reliability writing that exists.**
- 📕 **Google SRE Book ch. 21 (Handling Overload) and ch. 22 (Cascading Failures).** **Ch. 22 may be the most valuable chapter in the book.**
- 📄 **Netflix, "Performance Under Load: Adaptive Concurrency Limits"** + the `Netflix/concurrency-limits` source.
- 📄 **Bronson et al., "Metastable Failures in Distributed Systems" (HotOS 2021).**
- 📄 **Dean & Barroso, "The Tail at Scale."** Re-read; you are living it.
- 📕 **Lukša, *Kubernetes in Action* 2nd ed. — ch. 1–7, 12, 17.**
- 📄 **"Kubernetes Failure Stories"** (`k8s.af`) — **read 10.** The highest learning-per-minute in the ecosystem.
- 📕 **Majors, Fong-Jones, Miranda, *Observability Engineering* — ch. 1–6.**
- 📕 **Google SRE Workbook ch. 5, "Alerting on SLOs"** — multi-window multi-burn-rate alerting.
- 📺 **CMU 15-213 ch. 5** — you are profiling the fan-out path this level; this is what the compiler will and will not do for you.

### 🛠 THE BUILD · 60h — MILESTONE K7

📈 **EXIT CRITERIA**
- [ ] **🔴 THE PRESENCE CURVE:** broadcast message rate vs room size, for five strategies (naive · debounced · batched · lazy/open-room-only · aggregate-above-threshold). **The naive curve going vertical is half the artifact**
- [ ] **The measured room-size threshold** at which you stop broadcasting individual presence, derived from your own curve rather than guessed
- [ ] **🔴 THE GOODPUT CHART:** offered load 0.5×→5× capacity vs successfully delivered-and-acknowledged messages/sec, for **six configurations** (naive · bounded queues · +deadline dropping · +priority shedding · +adaptive concurrency limit · +autoscale). **Collapse and graceful on the same axes**
- [ ] Quantified: *"at 3× overload the naive federation delivers X% of capacity; the adaptive one delivers Y%."*
- [ ] **Shedding is by priority, never random** — message > receipt > typing — and you can explain what random shedding does to a conversation
- [ ] **The reconnect storm reproduced, then survived:** kill a relay holding 5,000 connections; show reconnect latency **with and without full jitter.** Two graphs
- [ ] **A metastable failure reproduced, then made impossible.** Two graphs
- [ ] `kubectl apply -k deploy/` brings up a **20-relay federation on local k3s from nothing** *(Kubernetes 30.4%)*
- [ ] **Rolling restart of all 20 relays with ZERO lost and ZERO duplicated messages**, under sustained load. Harder than it sounds, and it is the real lesson
- [ ] Prometheus + Grafana; RED per component **plus the five messaging signals**; **a dashboard you would actually open at 3am** *(Observability 13.0% / 22.0%)*
- [ ] Given an injected fault, **time-to-root-cause under 5 minutes using only the dashboards.** Demonstrate on video
- [ ] **Multi-tenancy:** per-tenant quotas, weighted fair queuing, **shuffle sharding with the blast-radius combinatorics chart**. One tenant at 100× load degrades others' p99 by **<10%**

## 8.2 — ★ THE PUBLIC DEMO

> **This is your stated success condition — a recruiter opens a link, sees it work, and calls. It is a scheduled deliverable and it is on the never-cut list.** Built here in W42, finalised in W52.

📈 **EXIT CRITERIA**
- [ ] **One URL. No signup. No install.** Two chat windows, visibly on two different relays, with the federation path drawn and each hop's latency shown live
- [ ] **`KILL RELAY B`** — B dies visibly, messages queue visibly, B returns, **everything arrives exactly once in causal order**, and the recovery time is shown as a number against the failure-free baseline
- [ ] **`PARTITION`** — the relays are severed, the direct peer path lights up and takes over *(stubbed in W42, real in W48)*
- [ ] The **live goodput panel** while a visitor drives a presence storm past capacity — collapse against graceful shedding, same axes
- [ ] **The scale statement printed on the page**, not buried in the README
- [ ] Rate-limited, sandboxed, quota per IP, and it cannot be used as a real messaging service
- [ ] **A stranger with no context understands what they are looking at in ten seconds.** Tested on a non-engineer

## 8.3 — Cloud, and $0.00

📈 **EXIT CRITERIA**
- [ ] **AWS, exactly the subset you need — and no certification.** **IAM** (roles vs users, assume-role, least privilege, **OIDC federation from CI so there are zero long-lived credentials** — the modern correct answer and the AWS topic actually asked about in interviews) · **VPC** (subnets, SGs vs NACLs, **NAT gateway cost**, the classic surprise bill) · **S3** (consistency, storage classes, lifecycle — used here for media attachments and log archives) · **EC2 t4g** · **CloudWatch** (metrics, alarms, **the $1 billing alarm**) *(AWS 48.9%)*
- [ ] **`keryx-store` builds and passes all tests on aarch64** (the Oracle box is ARM); **per-component x86-vs-ARM delta published** and attributed to cache sizes, memory bandwidth, vector width
- [ ] **A real three-continent federation:** relays on Oracle (Frankfurt), AWS (Dublin) and your workstation (Cairo) exchange messages over the real internet. **Latency per hop measured — this is the first real data point for Level 11's curve**
- [ ] `costwatch`: **all infrastructure in Terraform** (`apply` from zero, `destroy` to nothing) · hand-written least-privilege IAM verified with the policy simulator · **a CloudWatch billing alarm at $1, tested by deliberately triggering it** (an untested alarm is not an alarm) · **free-tier drift detection that fails CI** if any non-free-tier resource is created
- [ ] **$0.00 verified from both consoles and screenshotted — every month from here**

⛓ **PROBLEM CHAIN**
```
"5k-member room = 833k msg/s"  → presence is O(N²) → debounce → batch → lazy → threshold
"A blip reconnected everyone"  → reconnect storm → full jitter → YOUR redeploy is the DDoS
"Goodput collapsed at 3×"      → shed, don't queue → by priority, never random
"Random shedding broke a chat" → a dropped message is data loss; a dropped receipt isn't
"Retries made it worse"        → amplification → budgets → metastable failure
"OOMKilled at a 'generous' limit"→ the container counts heap + off-heap + stacks
"Rolling restart lost messages"→ graceful drain → hand off Raft leadership → preStop
"The bill could become $400"   → NAT gateway → tested billing alarm → drift detection
```

## 🎤 INTERVIEW PARAGRAPH — Week 42 (and CV v3)

> This level was overload, and the finding I'd lead with is that presence — "who's online, who's typing" — is the thing that actually kills chat systems, and it's a pure O(N²) problem. A five-thousand-member room where everyone heartbeats every thirty seconds is eight hundred thousand broadcast messages a second for a room where nobody has said anything. I plotted the curve going vertical against room size, then plotted four mitigations on the same axes, and the real answer is the one nobody explains: above a measured room-size threshold you stop broadcasting individual presence entirely and aggregate it. I derived my threshold from my own curve rather than guessing it.
>
> Then goodput. I drove the federation to five times capacity with an open-loop generator and plotted successfully delivered-and-acknowledged messages per second. It doesn't plateau, it collapses, because the relay spends everything on deliveries that will time out before they land. The fixes are ordered — bounded queues, then drop deliveries whose deadline has already passed, then shed by priority — and shedding in a messaging system has a constraint a request/response service doesn't have, because dropping a random one percent of *messages* is data loss, while dropping typing indicators costs nothing. So shedding is message beats receipt beats typing, never random.
>
> The one that embarrassed me most was the reconnect storm. I killed a relay holding five thousand connections and they all came back at once, re-subscribed at once, and re-broadcast presence at once — my own redeploy was a self-inflicted DDoS until I added full jitter to the backoff. Two graphs, with and without.

## 🎓 LEVEL 8 EXIT EXAM
1. The federation runs at 70% utilisation with p99 of 800ms. Load rises 20%. Estimate the new p99 and name the model.
2. Derive the presence broadcast rate for an N-member room. At what N do you change strategy, and to what?
3. Why is random load shedding unacceptable in a messaging system but fine in a request/response one?
4. Explain coordinated omission and design a load test that avoids it.
5. Your JVM relay is OOMKilled at a 4GB limit with `-Xmx3g`. Name four things consuming the difference.
6. You redeploy 20 relays. What happens to 100,000 clients, and why do you need jitter?
7. What happens between `kubectl apply` and a running pod? 12+ steps.
8. What is a metastable failure? Give KERYX's and its mitigation.
9. Name the five messaging signals on your 3am dashboard and what each tells you.

**Pass = 8/9.** *This is the level that separates candidates.*

### 🧩 TRACK I — L8 · W39–42 · 8h/wk
**DSA:** **heaps and priority queues** (priority shedding *is* a priority queue) · **sliding window** (rate limiting literally is one) · **segment trees and Fenwick trees** (Codeforces EDU) · **binary lifting** · **strings.** Company-tagged sets, timed at 25 minutes. **~48 problems. Running total ≈399.**
**System design:** design a **multi-tenant SaaS with quotas and fair sharing**, and design **presence/online-status at scale** — and answer the second from your own curve, which almost no candidate can.
**⚑ CV v3 written** — the first version that survives a tier-1 screen. Send to your three strongest contacts **for feedback, not for a referral.**

---
---

# ⚡ LEVEL 9 — Operations, Chaos & On-Call 🎯

> **Goal:** close the gap with the least alternative route — **on-call, 17.4%** — and **start applying.**
> **⏱ Weeks 43–45 · Jul 5 – Jul 25 2027 · 36h depth** · **Milestone K8** · **🚩 Flagship #8 `incident-lab`** · **⚑ CV v4** · **🎯 APPLICATIONS OPEN W43** · **W45 = buffer + response-rate gate**
>
> **The split changes from Week 43: 12h Depth / 12h Interview / 8h Career.** Applications are live; interview readiness is now the binding constraint.

## 9.1 — 🚩 FLAGSHIP #8: `incident-lab`

### Part A — Six famous outages, reproduced locally

**For each:** read the postmortem → **build a minimal local reproduction** → observe it with instrumentation → implement the fix → write your own analysis. 4–6h each; **do six minimum.**

| # | Incident | The mechanism | What it teaches you about KERYX |
|---|---|---|---|
| 1 | **AWS S3, Feb 2017** | An operator command removed more capacity than intended; the restart path had never been tested at that scale | **Never-tested recovery paths — your full-federation cold start from the message log is one, and you have never run it at 20 relays** |
| 2 | **GitHub, Oct 2018** | A 43-second partition triggered failover; both sides accepted conflicting writes → 24h of reconciliation | **Split-brain.** You built Raft and fencing tokens for exactly this. Reproduce it *without* them, then show yours surviving |
| 3 | **Cloudflare, July 2019** | A regex with catastrophic backtracking deployed globally in one step | **Global deploys need staged rollout — and you deploy to relays other people run** |
| 4 | **Meta, Oct 2021** | A backbone change withdrew BGP routes for DNS; the company vanished, **including the tools needed to fix it** | 🔴 **Circular dependency in recovery. Does your admin surface depend on the federation it administers? Does your bootstrap relay? Check** |
| 5 | **Slack, Jan 2021** | Traffic ramp → slow autoscaling → cascading saturation with a retry feedback loop | **Metastable failure.** You reproduced one in Level 8; this is the production version |
| 6 | **Roblox, Oct 2021 (73 hours)** | Consul streaming under load → contention → could not recover; **and the observability system depended on the failed cluster** | 🔴 **Your monitoring must not depend on the federation it monitors** |
| 7 | **GitLab, 2017** | `rm -rf` on the wrong host — then **5 of 5 backup methods had silently been failing** | **Untested backups are not backups. Your S3 log archive is a backup you have restored from exactly once** |
| 8 | **Knight Capital, 2012** | Partial deploy + reused feature flag; $440M in 45 minutes | **You deploy to relays you do not watch during the deploy** |

**Deliverable per reproduction:** `docker compose up` for the minimal system · a trigger script · **instrumentation showing the failure as it happens** · the fix with the same trigger now harmless · and an analysis naming **the trigger, the amplifier, the containment failure, the recovery obstacle, and the three controls that would have prevented or bounded it.**

### Part B — Twenty incidents in your own federation

**≥20 logged incidents**, each with: the alert that fired (**or the alert that should have and did not**), a timestamped timeline, root cause, and a runbook entry.

**Injections:** relay kill mid-fan-out · Raft leader kill mid-commit · **asymmetric partition between two relays** · disk fill on a relay holding a room's log · S3 unavailable during archive · **certificate expiry** · a poison event that crashes one relay's parser · **all 20 relays restarting simultaneously** · a peer relay flooding you · **a lying relay in production** · reconnect storm from 5,000 clients · JVM GC pause storm · **clock skew.**

> ### 🔥 THE CLOCK SKEW INCIDENT — do this one properly
> Skew one relay's clock by four seconds. **Nothing fails loudly.**
>
> Raft lease expiry is computed against a clock that disagrees with the leader's. Rate-limit windows are wrong. Presence timeouts fire early. Message timestamps shown to users are wrong even though *ordering* is causal and therefore still correct — **so the conversation is right and the timeline display is wrong, which is the most confusing possible failure.** The relay does not crash. Every dashboard stays green.
>
> Then write the invariant check that catches it: **relays report clock offset relative to the Raft leader's, and a relay beyond a threshold is quarantined from leadership and from issuing timestamps.** And note the deeper lesson — **you built causal ordering in Level 3 precisely because you cannot trust a clock, and this is the incident that proves you were right.**

### 📄 SOURCES
- 📕 **Michael Nygard, *Release It!* 2nd ed.** — circuit breaker and bulkhead as named patterns. **The single most relevant book to this level.**
- 📕 **Google SRE Book ch. 21, 22** and **SRE Workbook ch. 5.**
- 📄 **`github.com/danluu/post-mortems`** — read one a week for the rest of the year.
- 📄 **Lamport, "Time, Clocks, and the Ordering of Events"** — read it a third time. It reads differently now.
- 📺 **MIT 6.858 — the key-management and side-channel lectures**, for `gatekeep`.

### 🛠 CORE PROJECTS · `gatekeep` (10h)
mTLS between all relays · **relay identity is a certificate, and federation trust attaches to it** · per-relay credentials, rotation, revocation · secrets out of git (`gitleaks` in CI) · **certificate expiry alerting tested by fast-forwarding a clock.**

📈 **EXIT CRITERIA — MILESTONE K8**
- [ ] **≥6 famous outages reproduced**, each with before/after and a written analysis
- [ ] **🔴 The synthesis essay: "the seven mechanisms behind every major outage."** You will find them — config changes · circular dependencies in recovery · untested recovery paths · retry amplification · cold caches and thundering herds · silent backup or validation failure · unbounded resource growth. **Published**
- [ ] **≥20 incidents in KERYX**, each with alert, timeline, root cause, runbook entry
- [ ] **The clock-skew incident done properly**, with the quarantine invariant
- [ ] **Full-federation cold start from the message log, for real, and timed.** An untested recovery path is not a recovery path
- [ ] **The circular-dependency audit:** does your admin surface, your monitoring, or your bootstrap relay depend on the federation? Write the honest answer and the mitigation
- [ ] Every alert reviewed: actionable? runbook? worth 03:00? **An alert without a runbook is deleted, not documented**
- [ ] One deliberate **error-budget burn** with the written decision that follows
- [ ] `docs/design/slo.md` — SLOs with error budgets, **derived from measured numbers, not aspirational**
- [ ] `gatekeep` complete; **no plaintext secret in git history**
- [ ] **CV v4 written; first 48 applications sent**

## 🎤 INTERVIEW PARAGRAPH — Week 45 (and CV v4)

> This month was a deliberate failure programme — twenty-odd logged incidents where I killed relays mid-fan-out, killed a Raft leader mid-commit, partitioned two relays asymmetrically, filled disks, expired certificates and put a lying relay into the running federation, each with the alert that fired, a timeline, a root cause and a runbook entry. The one that taught me most is clock skew. I skewed one relay by four seconds and **nothing failed loudly** — Raft lease expiry was computed against a clock that disagreed with the leader's, rate-limit windows were wrong, and message timestamps shown to users were wrong *even though the ordering was still correct*, because my ordering is causal and doesn't depend on clocks. So the conversation was right and the timeline display was wrong, which is the most confusing failure a user can be handed. Every dashboard stayed green. It's also the incident that justified the causal ordering I'd built six months earlier for reasons that were theoretical at the time.
>
> And I found a circular dependency in my own recovery by reproducing Meta's 2021 outage locally — the one where a BGP change took out their DNS and also the internal tools they needed to fix it. My admin surface was reachable only through the federation it administers. That's now written down honestly rather than discovered during an incident.

## 🎓 LEVEL 9 EXIT EXAM
1. Your clocks skew by 4 seconds. What breaks, what doesn't, and why does nothing alert?
2. Pick one reproduced outage. Name the trigger, the amplifier, the containment failure, the recovery obstacle.
3. Why must observability not depend on the system it observes? Which KERYX component violates this?
4. Full-federation cold start from the log. Walk through the first ten minutes and what fails.
5. Design an SLO for end-to-end message delivery. SLI, budget, burn-rate alert thresholds.
6. A relay's certificate expires at 03:00 Saturday. Walk through what happens and what should have happened.
7. A peer relay floods you. Name your escalation ladder and what each step costs.

**Pass = 6/7.**

### 🧩 TRACK I — L9 · W43–45 · 12h/wk
**Topic learning is over. Volume under time pressure and loop simulation.** Company-tagged sets timed at 25 minutes, **spoken aloud**. **System design: full 45-minute designs, one per week, recorded.** **~60 problems. Running total ≈459.** **Loops #2 and #3.**

---
---

# ⚡ LEVEL 10 — The Peer Mesh: NAT, Gossip & Store-and-Forward

> **Goal:** two devices reach each other when no relay can reach either of them. **The half of the purpose that federation alone cannot deliver.**
> **⏱ Weeks 46–48 · Jul 26 – Aug 15 2027 · 36h depth** · **Milestone K9** · **🚩 Flagship #9 `natlab`**

## 10.1 — Two phones behind two home routers

> ### 🔥 THE WALL
> Run a KERYX client on your workstation in Cairo. Run another on a different network. Give each the other's IP. **They cannot connect, in either direction.**
>
> Both are behind NAT. Neither has a publicly routable address. **This is the actual, physical reason peer-to-peer software needs discovery and traversal infrastructure**, and it is invisible until you hit it. Now do it again with the Oracle box as a rendezvous point and watch hole punching work — **and then find the NAT type where it still does not**, and fall back to relaying.

### 🔎 DIAGNOSE
```bash
tcpdump -i any -nn 'udp port 3478'   # watch the STUN exchange
# compare your observed external ip:port from TWO different rendezvous servers —
# if they differ, you are behind symmetric NAT and hole punching will not work
```

### 📖 THEORY
- **NAT types and why they matter:** full-cone, restricted-cone, port-restricted, **symmetric**. **Hole punching works for the first three and fails for symmetric NAT**, which is why every real P2P system has a relay fallback. Knowing this distinction separates someone who read about NAT from someone who fought it.
- **STUN-style discovery and ICE** — ask a public server what external `ip:port` your packet appeared to come from, then coordinate simultaneous outbound packets so both NATs open a mapping. You use **`pion/ice`**; you do not write this.
- **Relay fallback (TURN-shaped)** — when punching fails, proxy through the Oracle box. **Measure what fraction of your peer pairs need it**, because that fraction is a real cost in a real system.
- **SWIM gossip membership and phi-accrual failure detection** — a node pings one random peer per period and asks *k* others to probe indirectly if that fails; membership updates piggyback on the ping traffic. **Traffic is O(N) per node per period regardless of mesh size**, against the naive O(N²). Phi-accrual outputs a *suspicion level* from the distribution of recent inter-arrival times rather than a binary alive/dead on a fixed timeout — **compare them and measure the false-positive rate under injected jitter.**
- **Delay-tolerant store-and-forward.** A device holds a message for a peer it has seen before, with a TTL and a hop limit, and hands it over when they next meet. **This is the layer that works when the internet is gone**, and it is the one that makes the project's purpose real rather than rhetorical. Epidemic routing, its bandwidth cost, and why you bound it.
- **The honest limit:** store-and-forward through untrusted intermediaries is **fine because the payload is end-to-end encrypted** (Level 5 paid for this) — but the intermediary learns that two parties are in contact. **That is metadata, you do not solve it, and you say so.**

### 📄 SOURCES
- 📄 **RFC 8445 (ICE) §2** — the traversal model. And the `pion/ice` documentation.
- 📄 **Ford, Srisuresh & Kegel, "Peer-to-Peer Communication Across Network Address Translators" (USENIX ATC 2005)** — the paper that named the technique.
- 📄 **Tailscale's "How NAT traversal works"** — the best practical write-up in existence, and honest about where it fails.
- 📄 **Das, Gupta, Motivala, "SWIM" (DSN 2002).** Short and unusually clear.
- 📄 **Hayashibara et al., "The φ Accrual Failure Detector" (SRDS 2004).**
- 📄 **HashiCorp's Serf documentation on Lifeguard** — a production system's honest account of where the SWIM paper needed fixing.
- 📄 **The Briar protocol documentation** — the closest prior art to your mesh layer, and you cite it.
- 📺 **MIT 6.1810 — the network-namespace material**, for the test harness.

### 🛠 🚩 FLAGSHIP #9 — `natlab` *(Instrument, 9/10)* + MILESTONE K9 · 30h

📈 **EXIT CRITERIA**
- [ ] **Two devices behind different NATs exchange a message with no relay reachable.** If your own connection is symmetric-NAT, **demonstrate the relay fallback instead and document which it was** — that is a real finding, not a failure
- [ ] **🔴 THE REACHABILITY TABLE:** hole-punch success rate by NAT-type pair, measured across every network you can borrow — home, mobile tether, café, cloud. **Report N and be honest that it is small.** *Nobody publishes this for messaging*
- [ ] **Relay-fallback fraction measured**, and its latency and bandwidth cost against the direct path
- [ ] SWIM membership: a peer joining a 30-node mesh is known to all others **within a bounded number of rounds, measured and plotted against mesh size**, next to the naive O(N²) curve
- [ ] **Phi-accrual vs fixed timeout: false-positive rate and detection latency, both, as a chart**, under `tc netem` jitter
- [ ] **The asymmetric-partition test:** A reaches B, B does not reach A. The mesh converges to a consistent view **or you document exactly why it cannot and what you do about it**
- [ ] **Store-and-forward: a message from an offline sender reaches an offline recipient via a third device that met both.** TTL and hop limit enforced and tested
- [ ] `docs/design/mesh.md` — what the mesh layer guarantees, its bandwidth cost, **and the metadata it leaks**
- [ ] **The demo's `PARTITION` button now does the real thing**

⛓ **PROBLEM CHAIN**
```
"Peers can't connect"          → NAT types → hole punching → and symmetric NAT defeats it
"Punching failed 30% of pairs" → relay fallback → measure the fraction → it is a real cost
"O(N²) membership traffic"     → SWIM → indirect probing → flat per-node traffic
"Fixed timeout flaps on jitter"→ phi-accrual → suspicion levels → measure both
"A thinks B dead, B thinks A alive"→ asymmetric partition → the nastiest fault class      (→ L7)
"No internet at all"           → store-and-forward → TTL + hop limit → the purpose, realised
"The carrier device learns who"→ metadata → E2E protects content, not contact → SAY IT     (→ L5)
```

## 🎤 INTERVIEW PARAGRAPH — Week 48

> This is the half of the project that federation can't deliver. Two devices behind home routers cannot reach each other in either direction — that's the physical reality of NAT, and it's invisible until you hit it. So there's STUN-style hole punching through a rendezvous server, and a relay fallback for symmetric NAT where punching structurally cannot work. The artifact is the reachability table: hole-punch success rate by NAT-type pair, measured across every network I could borrow — home, mobile tether, café, cloud — with the relay-fallback fraction and what it costs in latency and bandwidth. Nobody publishes that for messaging, and I report my N honestly because it's small.
>
> On top of that is SWIM gossip for membership, which is O(N) per node instead of the naive all-pairs O(N²) — I have both curves — with phi-accrual failure detection rather than a fixed timeout, chosen after measuring false-positive rates under injected jitter. And the layer that makes the project's purpose real rather than rhetorical: store-and-forward, where a device carries a message for a peer it has met and hands it over when they next meet. It works with no internet at all. And I say the limit out loud: the carrier learns that two people are in contact. End-to-end encryption protects the content, not the fact of the conversation. I don't solve metadata and I don't pretend to.

## 🎓 LEVEL 10 EXIT EXAM
1. Four NAT types. Which defeats hole punching, and what do you do instead?
2. Why is SWIM O(N) per node when naive membership is O(N²)? What does indirect probing buy?
3. Fixed timeout vs phi-accrual. Give the failure mode of each and the metric that distinguishes them.
4. Asymmetric partition: A→B works, B→A does not. What does each side believe, and what can you actually do?
5. A message is store-and-forwarded through a stranger's phone. What do they learn, and what protects the rest?
6. Your hole-punch success rate is 68%. What does the other 32% cost you, in latency and in money?

**Pass = 5/6.**

### 🧩 TRACK I — L10 · W46–48 · 12h/wk
Volume and loops. **Loops #4, #5, #6.** **~48 problems. Running total ≈507.**
**System design:** design **WhatsApp** and design **a system that works offline and syncs later.** You have unusually good answers to both.

---
---

# ⚡ LEVEL 11 — The Federation Benchmark

> **Goal:** produce the numbers the field does not have. **This is the level that makes the year citable.**
> **⏱ Weeks 49–51 · Aug 16 – Sep 5 2027 · 24h depth** · **Milestone K10** · **🚩 Flagship #10 `fedbench`** · **W49 = REST WEEK**

## 11.1 — 🚩 FLAGSHIP #10: `fedbench` — the three curves, and the head-to-head

> ### 🔥 THE WALL
> Install **Synapse**, the Matrix reference server. Federate two instances. Run the same conversation workload through it that you run through KERYX, on the same hardware, over the same `tc netem` profiles.
>
> **You will lose on features by a mile and you may lose on latency too.** The number is not the point — **the explanation is.** Find out precisely where the difference is: the transport, the ordering algorithm, the state-resolution cost, the database schema, the language runtime. **Attribute every part of the gap to a named mechanism.**

### 📖 THEORY
Fair benchmarking: identical hardware, identical workload, **identical semantics** — *if Synapse is doing state resolution v2 and full auth-chain validation, either yours does too or you say loudly that it does not.* **Comparing your simpler protocol to their complete one and calling it a win is a rigged benchmark and a reviewer will catch it in one question.** Warm-up, steady state, multiple runs, distributions not means. **State versions. State configuration. Publish the configuration files.**

### 🛠 THE BUILD · 24h

📈 **EXIT CRITERIA**
- [ ] **🔴 CURVE 1 — the federation cost curve.** p99 end-to-end delivery latency vs **federation hop count** (1, 2, 3, 4 relays in the path), across four network profiles. *This does not exist publicly*
- [ ] **🔴 CURVE 2 — ordering violations vs federation size.** Rate of causally-inverted deliveries, and time-to-convergence, as the number of participating relays grows from 2 to 200. **The 200-relay point is the planned 72-hour GCP window**
- [ ] **🔴 CURVE 3 — partition cost.** Kill a relay mid-conversation: messages delayed, messages delivered out of causal order, and **time to full convergence**, plotted against partition duration and message rate
- [ ] **The Synapse head-to-head table:** delivery p50/p99, federation transaction throughput, CPU and memory per 1,000 messages, cold-start time. **Same hardware, same workload, and an explicit statement of every semantic difference**
- [ ] **One script reproduces every number.** A benchmark you cannot reproduce is a marketing claim
- [ ] **Every part of the gap attributed to a named mechanism**, with the profile that shows it
- [ ] At least one place where **KERYX wins**, honestly found and honestly explained — and **if there is none, say that**
- [ ] 🔴 **`docs/analysis/sim-fidelity.md`** — the same experiments on the real 20-relay federation and on a 20-relay simulation. **Where do they agree, where do they diverge, by how much, and does divergence grow at the GCP window's 200 relays?** *A simulator you have not validated is a fantasy generator, and this document is what stops yours being one*
- [ ] `docs/analysis/vs-synapse.md` — **written as an engineer, not a marketer.** *"I am 2.4× faster on delivery and I do four things Synapse does that matter, and here they are"* is a far stronger artifact than a bare win

### 🛠 CORE PROJECTS
**`1brc` v2** *(Instrument, 10/10)* — the One Billion Row Challenge, **the real assault, one year after your Week-2 naive attempt.** mmap, SIMD, a custom hash map, branchless parsing, thread partitioning. **Against a public leaderboard, so the number is checkable by a stranger rather than self-reported — the only artifact in this repo with that property.** Report the two-year delta.
**`pgshift`** — `ALTER TABLE` on a 50M-row relay metadata table under live federation load. Do it the naive way first and **capture the outage graph**; then expand/contract with a chunked, throttled, resumable backfill. **Both graphs in the README, because the failure is half the story.** *(PostgreSQL 19.6%)*

## 🎓 LEVEL 11 EXIT EXAM
1. What makes a benchmark against a mature system fair? Name four requirements.
2. You are slower than Synapse on X. Where does the gap come from, in order of size?
3. What does a federation hop actually cost? Answer from your own curve, and decompose it.
4. Your ordering-violation rate rises with relay count. Why, and what bounds it?
5. Your simulator says X and the real federation says Y. What do you do, and what does the gap tell you?
6. Someone says "federated chat is slow." Answer them with numbers, including the part where they are right.

**Pass = 5/6.**

### 🧩 TRACK I — L11 · W49–51 · 14h/wk
**Loops #7 through #11.** Two per week from W51. **~40 problems. Running total ≈547.**

---
---

# ⚡ LEVEL 12 — Synthesis & Conversion

> **Goal:** convert. **No new features.** The system was finished in Week 51.
> **⏱ Week 52 · Sep 6 – Sep 12 2027 · 12h depth** · **Milestone K11**
> Split: 12h legibility / 14h interview / 6h career.

> ### 📅 READ FIRST
> **The strongest big-tech hiring window is September–October 2027** — exactly where your Week-43 applications land their loops. Week 52 is **not** the end of the process, and `docs/NEXT.md` is the most important deliverable of the final week.

## 12.1 — Legibility

> ### 🔥 THE WALL
> Hand the repo to someone who has never seen it. **Ten minutes on a timer.** Ask: what is it, what is real, and what is the most interesting technical decision in it?
>
> They will fail. Write down exactly where they got lost. **Interviewers do not explore repositories; they read what you point at.**

📈 **EXIT CRITERIA**
- [ ] **README final** for a ten-minute reader: what it is · **the honesty statement and the scale statement, verbatim** · the three most interesting decisions, one sentence each · the headline numbers · one architecture diagram · what does not exist. **Tested on a human; their confusion points fixed**
- [ ] **`docs/TOUR.md`** — *"ten minutes: read these three files. An hour: these eight."*
- [ ] `bench/RESULTS.md` final — every benchmark, x86 and ARM, regenerable with one command
- [ ] **The demo finalised**, with the real partition path and the scale statement on the page

## 12.2 — The ten ADRs

Each: **context · options considered · decision · consequences · what you would do differently.**

| ADR | The contested decision |
|---|---|
| 0001 | **C++ for the wire and store, Java for the relay, Go for the edge** — and where each boundary sits |
| 0002 | **QUIC over TCP**, argued from your own head-of-line-blocking chart |
| 0003 | **Vector clocks over relays, causal delivery, deterministic tie-break** — and what a client is actually promised |
| 0004 | JNI vs FFM for the C++ boundary, with the measured per-call cost |
| 0005 | **Why your state resolution is simpler than Matrix's**, and what you gave up |
| 0006 | **One Raft group per room shard**, not one globally |
| 0007 | **The Double Ratchet as specified, inventing nothing** — and the multi-device history policy |
| 0008 | **Simulator-first testing, and how you validated the simulator** |
| 0009 | **No metadata resistance** — the deliberate non-goal, and who should use Signal or Tor instead |
| 0010 | **Your own federation protocol rather than Matrix compatibility** — and why |

📈 **ALSO**
- [ ] **`docs/LIMITATIONS.md`, linked from the README's first screen:** federation size (20–40 real relays) · simulator fidelity and its measured divergence · **metadata** · no mobile client · no voice or video · single-author code review · no production users. **Volunteering limitations before you are asked is the single highest-leverage interview behaviour available to you**
- [ ] **`docs/COMPARISON.md`** — honest comparison against **Matrix/Synapse** (the reference implementation of everything here), **XMPP** (twenty-five years of federation), **Signal** (centralised, and better at crypto than you), **Briar** (the mesh half, done for a harder threat model), **Delta Chat** (email as transport) and **Automerge/Yjs** (CRDTs, done properly). Where you converge, where you diverge, why
- [ ] `docs/BUGS-INDEX.md` and `docs/incidents/README.md` — navigable. The simulator's bugs and the 20 incidents are among the most interview-useful things you own and they are currently buried

## 12.3 — The retrospective

> ### 🔥 THE WALL
> Open `LOG.md`. Compute, per level: **hours estimated vs actual, and the ratio.** You were consistently wrong in one direction by a consistent factor. **That factor is a measured fact about you over twelve months, and almost no candidate has one.**

📈 **EXIT CRITERIA**
- [ ] **`docs/RETROSPECTIVE.md`** — per level: estimated, actual, ratio. **Every target you set before measuring, with both numbers**
- [ ] The three things you would rebuild differently. Specific and technical, not "start earlier"
- [ ] `make bootstrap` from clean. All tests pass. Federation deployed and reachable. **Billing $0.00**
- [ ] **Record the 45-minute talk again and watch it against the Week-18 recording. The delta is the year**
- [ ] **`docs/NEXT.md`** — the September–October 2027 plan: application volume, target-list refresh, live loops, **and how you sustain 8h/week of DSA with no roadmap telling you to.** The habit has to survive the plan that built it

## 🎤 THE FULL ANSWER — Week 52

> I spent a year building a federated messaging backbone. Independent relays, run by different people, interoperating over a protocol I designed, so no single operator can stop, read, or lose a conversation. **Federated messaging is solved — Matrix has done it since 2014 and XMPP since 1999, and Signal solved end-to-end encryption with the Double Ratchet, which I implement rather than invent.** What isn't published is what federation actually *costs*, and that's what I measured.
>
> The layers: a C++ wire protocol and transport — I implemented TCP first, through Stanford's CS144, so I could argue from measurements rather than diagrams, and the head-of-line-blocking chart that came out of it is why my transport is QUIC. A C++ message log built as an LSM tree, with a torture harness that kills it a thousand times and injects fsync failures at the syscall level. A Java 21 relay core doing causal delivery — vector clocks over relays, deterministic tie-break, so every relay independently produces the identical sequence — replicated by a Raft implementation I wrote after passing MIT 6.5840's labs. A Go edge for connections, presence and NAT traversal. And end-to-end encryption where the relay forwards ciphertext it cannot read, with key-change detection, because confidentiality without that is theatre.
>
> Three things bit me hardest and they're the three I'd want to be asked about. Ordering: three people reply at the same moment, and wall-clock timestamps make the conversation read as nonsense while nothing crashes. Presence: a five-thousand-member room is eight hundred thousand broadcast messages a second for a room where nobody said anything, and the real fix is a measured room-size threshold above which you stop broadcasting at all. And the seam: a peer running last month's build drops a field it doesn't understand and re-signs the event, and now the signature is wrong for everyone else.
>
> I test it with deterministic simulation — every source of nondeterminism behind an injectable port, so a run is a pure function of one integer, ten thousand seeds a night. It found three real bugs. And it models a fault type FoundationDB's simulator doesn't, because a federation's peers aren't fail-stop, they're other people's servers: a relay that stays up, responds promptly, and lies.
>
> Then the measurements nobody has published: p99 delivery latency against federation hop count, ordering-violation rate as relays are added from two to two hundred, and what a partition costs a conversation in delayed messages and time-to-convergence. Plus a head-to-head against Synapse on identical hardware with every semantic difference stated.
>
> The things I say without being asked: **my federation is twenty to forty relays I run, not a network with real users.** I validated my simulator against it and published where they diverge. **My relays learn who talks to whom and when — I don't defend against metadata analysis and I'm not going to pretend otherwise.** There's no mobile client and no voice. All of that is in a limitations document linked from the first screen of the README.

## 🎓 LEVEL 12 EXIT EXAM
1. Explain KERYX to a smart non-specialist in two sentences.
2. Name the six prior systems and where your design diverges from each.
3. Your three most interesting technical decisions, with the alternative you rejected.
4. What does your simulator prove, and what does it not?
5. The sharpest question an interviewer can ask about this project — what is it, and what is your answer? *(It is: "why would I use this instead of Matrix?" The answer is: you would not, and here is what I learned by building it anyway, and here are three curves the Matrix team has never published.)*
6. Estimated vs actual hours. What is your ratio, and what will you do differently next time?

**Pass = 5/6.**

---
---

# PART XI — The Ten Flagships

**The rubric — score before you start, build only if ≥7/10:** non-obvious premise (2) · produces an artifact that does not exist yet (2) · requires a hard idea to be **correct**, not just to run (2) · demoable in 60 seconds (1) · buildable solo in ≤3 weeks (1) · has a natural "and then it broke" story (1) · explainable to a non-specialist in two sentences (1).

**Four archetypes:** *Reimplementation with a twist* · *Instrument* (measures what people argue about with no data) · *Autopsy* (reproduce a real failure) · **Adversary** (builds the thing that proves a system wrong). **At least one must be an Adversary** — it is the single strongest signal of engineering maturity a portfolio can carry, because it demonstrates you think in invariants and failure modes rather than features. **KERYX has four.**

| # | Project | Lvl | Archetype | Score | Pitch | Corpus |
|---|---|---|---|---|---|---|
| 1 | ⚙️ **`hardened`** | 1 | **Adversary** | 9 | The C++ safety apparatus as a deliverable: sanitizers, libFuzzer with a committed corpus, the documented subset — **and the memory bugs the fuzzer found in my own frame parser, written up.** This is what makes the C++ choice defensible | C++ 26.0%, Testing 15.2% |
| 2 | **`minnow`** | 2 | Reimpl + **Instrument** | **10** | **A working TCP that passes Stanford CS144's full test suite and interoperates with the kernel's** — plus the head-to-head across six loss/jitter profiles, and **the head-of-line-blocking chart that decided my transport** | Networking 14.5% |
| 3 | **`logstore`** | 3 | **Adversary** | 9 | An LSM message log — and the torture harness that `kill -9`s it 1,000 times and injects `fsync` failures and torn writes at the syscall level via `LD_PRELOAD` | PostgreSQL 19.6%, Testing 15.2% |
| 4 | **`conform`** | 4 | **Adversary** | **10** | **A hostile conformance suite for a federation protocol.** ~80 adversarial cases plus a transaction fuzzer, runnable against any implementation over a socket. `h2spec` exists for HTTP/2; **nothing like it exists for federated messaging** | REST/API 34.8% |
| 5 | **`raft`** | 6 | Reimplementation | 9 | **MIT 6.5840 Labs 1–3 passing, including `TestFigure8Unreliable`** — then Raft again in Java as KERYX's relay cluster, **and the second implementation is where the understanding shows** | Distributed 48.9% |
| 6 | **`keryxsim`** | 7 | **Adversary** | **10** | Deterministic simulation of the whole federation — seeded clock that runs backwards, asymmetric partitions, disk faults — **and `LyingRelay` as a first-class fault, because a federation's peers are not fail-stop, they are other people's servers.** 10k seeds nightly, ≥3 real bugs with their seeds | Testing 15.2% |
| 7 | **`presence-storm`** | 8 | **Instrument** | 9 | **The O(N²) curve that kills every chat system**, with five mitigations on the same axes and the measured room-size threshold — plus the goodput collapse curve under 5× offered load | Scalability 31.5% |
| 8 | **`incident-lab`** | 9 | **Autopsy** | **10** | Six famous public outages reproduced locally with instrumentation and verified fixes, plus **20 self-inflicted incidents** with alerts, timelines, root causes and runbooks — including the clock-skew incident where nothing fails loudly | On-call 17.4%, Obs 22.0% |
| 9 | **`natlab`** | 10 | **Instrument** | 9 | **Hole-punch success rate by NAT-type pair**, measured across every network you can borrow, with the relay-fallback fraction and its cost. Nobody publishes this for messaging | Networking 14.5% |
| 10 | 🔴 **`fedbench`** | 11 | **Instrument** | **10** | 🔴 **The three curves nobody has:** delivery p99 vs federation hop count · ordering-violation rate vs relay count (2→200) · partition cost vs partition duration. **Plus the Synapse head-to-head, reproducible by one script** | Distributed 48.9%, Perf |

**Plus `1brc`** *(L0 + L11, Instrument, 10/10)* — the One Billion Row Challenge, twice, a year apart, **against a public leaderboard.** The only artifact here whose number a stranger can verify without trusting you.

**Core projects** (smaller, closing specific gaps): `latency-lab` (L0) · `sickbay` (L0, diagnosis under time pressure) · `c10k-arena` (L1, seven concurrency models including goroutines vs JVM virtual threads, **and again under a cgroup CPU limit** — the Kubernetes reality, and almost nobody benchmarks it) · `ratchet` (L5) · `gatekeep` (L9, mTLS + secrets + **a certificate-expiry alert tested by fast-forwarding a clock**) · `costwatch` (L8, Terraform + **a billing alarm tested by triggering it** — an untested alarm is not an alarm) · `pgshift` (L11, a 50M-row migration under live load, with the naive version's outage graph beside the correct one).

**Every flagship ships with:** its own repo · a README with an architecture diagram and a results chart **in the first screen** · a `make demo` that works on a clean machine · a written teardown · benchmarks someone else can reproduce.

---
---

# PART XII — Track I: The Interview Machine

> **Daily from Week 1.** 8h/week to Week 42 (**5.5h DSA + 2.5h system design**), **12h/week from Week 43.** Never batched. Never skipped.
>
> You can build every level of KERYX and still be rejected in a 45-minute phone screen. **This is the track that cannot be crammed, and it is the only one that degrades irreversibly when skipped.**

## What this is for, and the ratio that governs it

| Round | Evidence from your corpus |
|---|---|
| **System design** | Named as a skill in **23.9%** of backend postings; a design/architecture *duty* in **32.6%**; and present in **essentially 100% of the loops** behind these postings |
| **Algorithms / DSA** | **14.1%** algorithms + **17.4%** data structures in backend postings — roughly double the whole-corpus figure |

**System design is therefore a first-class daily thread from Week 1**, because it decides the *level* you are hired at, and level is worth more than base salary over three years.

**But DSA is a gate, and the bar has risen.** Frequency is irrelevant when 100% of these loops contain two coding rounds and Google and Meta now routinely ask problems that would have been "hard" three years ago. **~300h DSA aimed at hard-problem fluency, ~150h dedicated system design. Both to passing standard. Neither optional.**

> 🔴 **Do not let an earlier draft's 76.3% figure talk you into cutting DSA further.** It does not reproduce against the dataset. §I explains.

**It is not competitive programming.** Your Codeforces 1450 is a calibration instrument, not a goal. **The target: solve a medium-hard problem you have not seen, correctly, in 25 minutes, while talking.** The last three words are the part most people skip and the part that fails loops.

## Volume

| Period | Weeks | DSA h/wk | Design h/wk | Problems | Total h |
|---|---|---|---|---|---|
| Levels 0–4 | 1–23 | 5.5 | 2.5 | ~223 | 184 |
| Level 5 (Ramadan) | 24–27 | 3.5 | 1.5 | ~20 | 20 |
| Levels 6–8 | 28–42 | 5.5 | 2.5 | ~156 | 120 |
| Levels 9–12 | 43–52 | 7 | 5 | ~148 | 120 |
| | | | | **≈600** | **≈444** |

**Target: 600 problems · 25+ Hard · 20 system designs as written docs · 12+ full timed loops · Codeforces ≥1750.**

**Do not chase the count.** A problem you solved by opening the editorial after eight minutes did not happen. **A problem you failed and rebuilt from scratch two days later counts double.**

## 🔗 The KERYX ↔ DSA map — where the tracks compound

**This is the point of running them together.** Each level's systems work makes specific patterns *concrete*; do those patterns that week while the intuition is live.

| Weeks | Level | Systems work | DSA patterns it makes real | System design |
|---|---|---|---|---|
| 1–2 | L0 | Cache layout, working-set sweeps | Arrays, hashing, prefix sums, two pointers, sliding window — **the cache intuition is *why* these are fast in practice** | Estimation module; the numbers to memorise |
| 3–6 | L1 | Varint encoding, frame tuning, C10K | **Binary search incl. on the answer** (frame/batch tuning *is* this) · stacks & monotonic stacks · **bit manipulation** (your varint encoder) · linked lists | URL shortener · **rate limiter** |
| 7–12 | L2 | TCP reassembler, retransmission | 🔴 **Intervals and merging — the reassembler IS an interval-merge problem** · graphs BFS/DFS · queues & deques · sorting | **Distributed message queue** · notification system |
| 13–18 | L3 | B+Tree, LSM, causal delivery | 🔴 **Topological sort — causal delivery IS a topological order over a message DAG.** The cleanest mapping in the roadmap · trees & BSTs · heaps & top-K · tries | **Key-value store** · distributed cache |
| 19–23 | L4 | Backfill, DAG walks, state resolution | **DP** (1-D, 2-D, knapsack) · greedy · **DAGs, cycle detection, shortest path** (your backfill walk) | **Chat system** · **news feed** (the celebrity problem = L8's presence problem) |
| 24–27 | L5 | Ratchet, key derivation | 🌙 **Review and re-solve only. No new topics. Keep the streak** | E2E-encrypted system (written, untimed) |
| 28–34 | L6 | Raft, sharding, membership | **Union-find** (shard membership) · **reductions & NP-hardness** (W28 = three written reductions) · **articulation points** — *which relay's removal partitions your federation?* · modular arithmetic | **Distributed lock service** · **sharded database** |
| 35–38 | L7 | Model checking, DST | **Backtracking & state-space search** — DST and model checking are structurally a systematic search over interleavings · probability & expectation · **Bloom filters, HyperLogLog** (you need the second next level) | Rate limiter · **metrics/monitoring system** |
| 39–42 | L8 | Priority shedding, presence, fan-out | **Heaps & priority queues** (priority shedding *is* one) · **sliding window** (rate limiting literally is one) · segment trees & Fenwick · binary lifting · strings | **Multi-tenant SaaS with quotas** · **presence at scale** (answer from your own curve) |
| 43–45 | L9 | — | Volume under time pressure, company-tagged sets | Full 45-min designs, recorded |
| 46–48 | L10 | NAT, SWIM gossip | 🔴 **Graph BFS — gossip propagation IS breadth-first traversal.** Do the graph set again, timed | **WhatsApp** · **offline-first sync** |
| 49–52 | L11–12 | — | Loops, weak-area blitz | Two loops/week |

⚠️ **Where the tracks do NOT meet:** **string algorithms** (KMP, Z-function, suffix automata), **combinatorics**, **number theory**, and most of **geometry** get **zero** reinforcement from KERYX. **These are where you will be weakest.** Weeks 39–42 and the W45 weak-area blitz exist for them, and the disconnection is a reason to do them *more* carefully, not less.

## Sources

| Source | For | How |
|---|---|---|
| **NeetCode 150 → 250** | The pattern spine, W1–23 | In order, grouped by pattern. **Do not skip the easy ones** |
| **LeetCode, company-tagged** | W24–52 | Filter by your seven targets, last 6 months. Premium is genuinely worth $35 for two months before a loop |
| **Codeforces Div 2 A–D** | Weekly, all year | Rated when it fits, virtual when it does not. **Band 1450 → 1750** |
| **Codeforces EDU (ITMO)** | Segment trees W39–40, suffix structures W41 | The best free structured material for these, anywhere |
| **Laaksonen, *Competitive Programmer's Handbook*** (free) | Reference | **Ch. 7** (DP), **ch. 9** (range queries), **ch. 13–15** (graphs), **ch. 26** (probability) |
| **Skiena, *Algorithm Design Manual* 3rd ed.** | The *why* | **Ch. 8** (DP), **ch. 9** (intractability and reductions — supports W28) |
| **Sedgewick & Wayne, *Algorithms* (Princeton, free on Coursera)** | Foundations, if a topic feels shaky | Union-find and graphs specifically. **Optional — use it to repair, not to cover** |
| **Alex Xu, *System Design Interview* Vol. 1 & 2** | System design | **You own both.** The weekly design curriculum below is built on them |
| **`interviewing.io` / Pramp** | Mocks | Free peer mocks. **One paid mock with a real FAANG engineer around W33 if affordable** |

## 🔴 The failure log — the part that actually produces improvement

**Solving problems does not make you better. Reviewing failures does.** `dsa/FAILURES.md`, an entry every time you miss the time box or solve with the wrong approach.

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

**Do the count in the rest weeks — W12, W27, W38, W49.** Twenty minutes, and it redirects the next quarter. **Most people never do it and spend a year fixing the wrong thing.**

**Re-solve discipline:** every failed problem re-solved from scratch three days later, **without looking at your previous solution.** The highest-return habit in the track and the easiest to skip.

## Time boxes

| Difficulty | Box | On expiry |
|---|---|---|
| Easy | 15 min | Read the solution, log as failure, re-solve from scratch same day |
| Medium | 25 min | Read the *approach only*, retry 15 min, then the full solution. Log |
| Hard | 45 min | Same protocol |

**Never exceed the box.** An hour spent stuck teaches less than reading the solution and re-solving it twice.

## The system design curriculum — 2.5h/week from Week 1

**Twenty designs.** One every two to three weeks to Week 42, then one per week timed at 45 minutes.

**Each produces a full design doc:** Summary · Context · Goals · **Non-Goals** · Proposal · **Alternatives Considered (minimum three)** · Risks · Rollout · Operational Impact.

**The 45-minute structure:** 0–5 requirements, functional **and** non-functional, written on the board · 5–10 estimation (**round aggressively, show the arithmetic**) · 10–15 API and data model · 15–25 high-level design (**state your choices as choices**) · 25–40 deep dive (where the grade is decided) · 40–45 failure modes and 10×.

> **The single highest-leverage habit: say the words "I'm optimising for X, which costs me Y." Every time.**

**Numbers to memorise:**
```
1 machine:  ~10-50k QPS simple requests · 64-256GB RAM · 10-40 cores
Postgres:   ~5-50k simple QPS · ~1-5k writes/s with fsync
Redis:      ~100k-1M ops/s single instance (single-threaded!)
Kafka:      ~100k-1M msg/s per broker (small, batched)
WebSocket:  ~10-50k concurrent connections per commodity node (memory-bound)
NVMe:       ~500k-1M IOPS · 3-7 GB/s        Network: 10 Gbps = 1.25 GB/s
RTT:        same-AZ ~0.3-0.5ms · cross-region 30-150ms · Cairo↔Frankfurt ~60-90ms
Time:       1 day ≈ 10^5 s · 1M req/day ≈ 12 QPS · 1B req/day ≈ 12k QPS
```

> **🔴 Your unusual advantage.** Most candidates answer system design from books. **You can answer from a system you built, operated, and broke twenty times on purpose.** Asked to design a chat system, a message queue, a notification service or presence at scale, **do not recite** — say *"I did this; here is what I chose, here is the number I measured, and here is what it cost me."* **Practise that move deliberately in the W44 mock**, because it does not happen naturally under pressure.

## Mock schedule

| When | What |
|---|---|
| **W33** | First human mock + **the Raft Figure 8 whiteboard test** — a checkable gate, not a formality |
| **W33** | **One paid mock with a real FAANG engineer**, if affordable |
| W36, W40 | Monthly mock, one round |
| **W38** | **Full timed loop #1 — 4 rounds in one day** |
| W43–52 | Weekly, escalating to two/week from W51 |

**A "full timed loop" means** two 45-minute coding rounds with a human, one 45-minute system design, one 30-minute behavioural, **in a single day** with realistic breaks. **Not four sessions across a week.** The exhaustion is what you are training for, and it is what surprises people at their first real onsite.

**Speak while you solve, always, including alone.** The most common cause of a failed coding round in a candidate who *can* solve the problem is silence.

## 📈 TRACK I EXIT CRITERIA
- [ ] **600+ problems, ≥70% solved unaided within 25 minutes**
- [ ] A random unseen Medium, **narrated**, in ≤25 min, ≥80% of the time
- [ ] Complexity stated before code, every time
- [ ] **25+ Hard problems** · **failure-log review queue empty** · **Codeforces ≥1750**
- [ ] **20 system designs as written docs** and 20 more practised verbally
- [ ] **12+ full timed loops** · **14 behavioural stories on video, ≥4 from Logic Leap**

---
---

# PART XIII — Track F: The Gap-Filling Curriculum

> You are self-taught, which means your knowledge has holes you cannot see — not through carelessness, but because a curriculum's real function is to **tell you what exists.** This is that function.
>
> **The rule: no fundamental is taught in the abstract.** Each block lands the week the project first depends on it, uses **named chapters** rather than whole books, and ends in an exercise that proves it stuck.
>
> **Budget: 3h/week most weeks, 2h during Ramadan, 0 from Week 43. Total ≈130h.**
> **An exercise you skipped is a block you did not do.**

| # | Fundamental | Weeks | Hours | Why exactly then |
|---|---|---|---|---|
| F1 | CPU memory hierarchy | 1–2 | 6 | You choose the frame and log layouts with these numbers in front of you |
| F2 | OS: processes, scheduling, isolation | 3–4 | 6 | The relay process model, and L8's cgroups |
| F3 | OS: virtual memory & TLB | 5–6 | 6 | 40 relays on one box; memory is the binding resource |
| F4 | TCP & network behaviour | 7–9 | 9 | You are implementing it — this is the theory beside CS144 |
| F5 | Cache-conscious data layout | 10–12 | 9 | The LSM index and the subscriber table |
| F6 | Transactions & isolation | 13–15 | 6 | The message log's guarantees, and the relay metadata store |
| **F7** | **JVM: memory model, GC, virtual threads** | **16–18** | **9** | **The Java level. 53.3% of your postings** |
| F8 | Probability & distributed randomness | 19–20 | 5 | Shard distribution, election timeouts, HyperLogLog |
| F9 | Consensus, CAP & consistency models | 21–23 | 7 | Before Raft; and to place KERYX on the map |
| F10 | Performance measurement & optimisation | 28–29 | 5 | Everything you benchmark from here |
| F11 | Formal methods, lite (TLA+) | 30–32 | 5 | The catch-up protocol spec |
| F12 | **Latency measurement done correctly** | 35 | 3 | 🔴 **Your harness may have been lying since Week 2** |
| F13 | Cryptography for identity & TLS | 36–37 | 4 | `gatekeep`; relay identity is a certificate |
| F14 | Partitioning & distributed data | 39–40 | 5 | The vocabulary for your sharding design doc |
| F15 | AWS core services | 41–42 | 6 | **AWS is 48.9% of backend postings** |
| F16 | Queueing theory for engineers | 39 | 3 | Little's Law and the M/M/1 curve, which explain Level 8 |

**F1 · CPU memory hierarchy · 6h.** 📕 **CS:APP §6.2–6.4 only.** Skip §6.1.
🛠 **E1:** traverse a 256MB array with strides 1…4096, time each, plot. **Derive your L1/L2/L3 sizes from your own plot**, then check `lscpu`. If the plot has no steps your timing is wrong — fix it, because every number this year rests on measuring correctly.

**F2 · OS: processes, scheduling & isolation · 6h.** 📕 **OSTEP ch. 4–7** (free). Plus **Linux cgroups v2 kernel docs — the `memory` and `cpu` controllers** (`memory.max` vs `memory.high` precisely), and **NCC Group, "Understanding and Hardening Linux Containers"** — the namespace-escape sections.
🛠 **E2:** measure context-switch cost, two threads pinned to one core over a pipe, then to different cores. Explain the difference. Then **set a 100MB `memory.max`, run a memory bomb inside, and show the OOM kill happening *inside* the cgroup while the host is fine** — with the `dmesg` line.

**F3 · OS: virtual memory & TLB · 6h.** 📕 **OSTEP ch. 13–16, 18–19.** Ch. 19 is the one that matters.
🛠 **E3:** demonstrate TLB thrashing — a program whose only change is page-touching order, with a large runtime gap at constant work. Report `dTLB-load-misses` for both. Then compute: **at your measured per-relay RSS, how many relays fit before you are paging?**

**F4 · TCP & network behaviour · 9h.** 📕 **Kurose & Ross ch. 3 in full** · **Stevens *TCP/IP Illustrated Vol. 1* ch. 13–15** · **Grigorik, *HPBN* ch. 1–4** (free).
🛠 **E4:** capture a real connection with `tcpdump`, annotate **by hand** in Wireshark — handshake, initial cwnd, slow start, exit, one provoked retransmission (`tc netem loss`). Then explain in writing what happens to your federation transaction protocol on a link with 200ms RTT and 1% loss.

**F5 · Cache-conscious data layout · 9h.** 📕 **Drepper §3 in full, §6.2–6.4.** Skip §4–5.
🛠 **E5:** AoS→SoA on the room subscriber table. Measure wall time, `L1-dcache-load-misses`, `LLC-load-misses`. **Then predict in writing, before running it, what `__builtin_prefetch` in the fan-out loop will do.** Commit the prediction, then test. Being wrong is normal; not recording the prediction wastes the lesson.

**F6 · Transactions & isolation · 6h.** 📕 **DDIA ch. 7 in full** (write skew and phantoms especially) · 📄 **Berenson, Bernstein, Gray et al., "A Critique of ANSI SQL Isolation Levels" (1995)** · **Kleppmann's "Hermitage" repo — run it against Postgres yourself.**
🛠 **E6:** from memory, the four anomalies with a concrete two-transaction interleaving each, and which isolation levels prevent which. One page. **You use this directly in L11's `pgshift`.**

**F7 · JVM: memory model, GC & virtual threads · 9h ☕.** 📕 **Goetz, *JCiP* ch. 3, 5, 10, 11** · 📄 **Shipilëv's "JVM Anatomy Quarks"** — allocation and GC entries · **JEP 444, JEP 442.**
🛠 **E7:** take your Level-4 fan-out loop and reduce its allocation rate to zero in the steady state, proven with `async-profiler -e alloc`. **Then write one page: why your first version allocated, what the JIT did and did not do for you, and where escape analysis failed.** *This is the exercise that turns "I know Java" into "I know the JVM," which is the difference in a 53.3% skill.*

**F8 · Probability & distributed randomness · 5h.** 📕 **Mitzenmacher & Upfal ch. 5 (balls into bins), §14.1 (power of two choices).**
🛠 **E8:** simulate 10,000 rooms into 20 relays with 1 / 10 / 100 / 500 virtual nodes. **Plot max-load-to-mean.** Compare your empirical curve to the theoretical `log n / log log n` result and explain any gap.

**F9 · Consensus, CAP & consistency models · 7h.** 📄 **Raft extended, §5 in full, §6 carefully** · 📕 **DDIA ch. 8 and ch. 9 in full** · 📄 **Jepsen's consistency map** — memorise the hierarchy · 📄 **Kleppmann on distributed locking + antirez's reply. Both.**
🛠 **E9:** place KERYX on the consistency map in writing, component by component. **This becomes ADR-0003.**

**F10 · Performance measurement & optimisation · 5h.** 📕 **CS:APP ch. 5 in full**, §6.4–6.6 · 📕 **Gregg, *Systems Performance* ch. 6 §6.6, ch. 13.**
🛠 **E10:** optimise one `keryx-fanout` function through five stages. Each: `perf record` top-5 symbols, wall time, cache-miss rate, **and one sentence naming the mechanism.** Unattributable stages marked "unattributed" rather than explained away.

**F11 · Formal methods, lite · 5h.** 📄 **`learntla.com`** — free, the best on-ramp · 📄 **Newcombe et al., "How AWS Uses Formal Methods"** — read first, to know why the hours are worth it.
🛠 **E11:** the Level 7 deliverable — spec the catch-up protocol, model-check the ordering safety invariant, find one real design bug.

**F12 · Latency measurement done correctly · 3h.** 📄 **Gil Tene, "How NOT to Measure Latency"** in full · 📄 **Dean & Barroso, "The Tail at Scale."**
🛠 **E12: 🔴 audit your own harness.** If it sends the next message only after the previous is acknowledged, it has coordinated omission and **every latency number in this repository is optimistic.** Fix it, **re-run every benchmark**, put the before/after in `bench/RESULTS.md`.

**F13 · Cryptography for identity & TLS · 4h.** 📕 **Aumasson ch. 1, 3, 9, 10, 11** · 📄 **RFC 8446 §2 only** (TLS 1.3 overview, six pages).
🛠 **E13:** capture a TLS 1.3 handshake, annotate every message against RFC 8446 §2. Then in writing: what mTLS adds, what is verified on each side, and **what happens when a relay's certificate expires at 03:00 on a Saturday.**

**F14 · Partitioning & distributed data · 5h.** 📕 **DDIA ch. 6 in full**, then **ch. 8** again.
🛠 **E14:** write your room-sharding design doc in ch. 6's vocabulary. Then the hard question: **what is your equivalent of a secondary index, given that a user's rooms are spread across shards a query may not know?**

**F15 · AWS core services · 6h.** **Skip courses.** Free AWS Skill Builder for gaps only; learn the rest by building Week 42's infrastructure. Cover exactly: **IAM** (roles vs users, assume-role, least privilege, **OIDC federation**) · **VPC** (subnets, SGs vs NACLs) · **S3** (consistency, storage classes, lifecycle, prefix scaling) · **EC2 t4g** · **CloudWatch** (metrics, alarms, the $1 billing alarm). Nothing else. **Do not study for a certification.**
🛠 **E15:** write the media-store S3 IAM policy **by hand from the docs**, least privilege, and verify with the IAM policy simulator that it permits exactly what you intend and nothing more.

**F16 · Queueing theory for engineers · 3h.** 📕 **Google SRE ch. 21** · 📄 **Marc Brooker's queueing posts on `brooker.co.za`.**
🛠 **E16:** derive, from Little's Law alone, the concurrency your relay must support at your measured delivery rate and latency. Then plot the M/M/1 curve and mark your operating point on it. **One page, and you will use it in every system design round for the rest of your life.**

### Deliberately NOT here
**Compilers and language theory** (interesting, zero corpus support) · **full Byzantine consensus** (you build the practical subset and explain the difference — worth more than a half-finished PBFT) · **machine learning** (there is none in this project, deliberately) · **a fifth language** · **certifications** (AWS SAA is 40h to close a gap Week 42 closes better, with a running system as evidence instead of a badge).

---
---

# PART XIV — Track J: Craft, Career & Visibility

> What separates an L4 from an L5 is not knowing more systems facts. It is **judgement, communication, and impact beyond your own keyboard.**
> **2h/week, 8h from Week 43. One artifact every two weeks.**

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

**Already scheduled:** `wire-protocol.md` (W6) · `transport.md` (W12) · `durability-contract.md` (W16) · `ordering.md` (W18) · `federation.md` + `vs-matrix.md` (W23) · `threat-model.md` (W27) · `consistency.md` (W34) · `tla-vs-dst.md` (W38) · `slo.md` (W45) · `mesh.md` (W48). **Ten, plus ten ADRs in W52.**

## J.2 — Writing and visibility — the multiplier

**Post the results, not the progress.** Not "day 47 of my coding journey" — the findings. You will have unusually good ones.

| Week | The post | Why it travels |
|---|---|---|
| 6 | **"A four-byte message killed my server"** | The length-prefix attack, and the fuzzer finding real bugs in your own parser the same week |
| 12 | 🔴 **"I implemented TCP so I could stop guessing about head-of-line blocking. Here's the graph."** | **A real measurement behind folklore everyone repeats. Front-page candidate** |
| 18 | **"Your chat app's timestamps are lying and the conversation reads wrong"** | Causal order, explained through a failure anyone can feel |
| 23 | **"Five things that break the moment you add a second server"** | The federation seam. Nobody writes about this because almost nobody builds it |
| 27 | **"Encrypting the messages is the easy part"** | Key-change detection, and why confidentiality without it is theatre |
| 38 | 🔴 **"Three bugs in my federated messaging system that no test suite would have caught"** | DST + `LyingRelay`. **Front-page candidate** |
| 40 | 🔴 **"I found coordinated omission in my own benchmark harness and re-measured eight months of results"** | **Engineers at exactly your target companies will read this** |
| 42 | 🔴 **"Presence is O(N²) and it is why your chat system falls over"** | **A curve everyone needs and nobody has published. Front-page candidate** |
| 45 | **"The seven mechanisms behind every major outage"** | From six local reproductions. Broadly useful, highly shareable |
| 51 | 🔴 **"What federation actually costs: three curves nobody has published"** | **The artifact. Matrix has run this for a decade and never published the tradeoff.** The single most valuable thing you write this year |

Own the domain; cross-post to Hacker News, Lobsters, `r/programming`, and the Matrix community rooms — **where the people who will hire you for this actually are.** **One post reaching the HN front page generates more inbound recruiting than 200 applications.**

**Give one talk.** A Cairo meetup counts. Explaining causal delivery out loud will expose every gap in your understanding, which is exactly why it is valuable.

## J.3 — Open source

**A merged PR into a project people have heard of beats three personal projects**, because someone with commit rights judged your code good enough to ship.

**The ladder:** use it seriously → fix the docs where they confused you (gets you through the CLA/CI process once) → a `good first issue` → **a bug you personally hit** → **a bug found by fuzzing** (maintainers love a minimal reproducer) → a feature, after discussing design in an issue first.

**Highest-leverage targets given KERYX:** 🔴 **Matrix — Synapse, the Rust `ruma` crate, or the spec itself.** You will read the Server-Server API all year and you *will* find gaps and edge cases, and **a Matrix contribution is a perfect CV line for this project** · **`pion` / `pion-ice`** (you use it hard in L10 and will hit edges) · **HashiCorp `memberlist`** (SWIM in production) · **`ngtcp2`** · **`libsodium` bindings** · **etcd/raft.** **One meaningful PR to Matrix is worth twenty to a random repo**, because it is *exactly* the domain you are claiming. **Budget: Levels 8–10. Target: 3+ merged, one non-trivial.**

## J.4 — 🔴 The referral problem, and how to solve it from Egypt

**Harder than the degree question, which the data settles: one posting in 569.** A cold application from Cairo to a Dublin req competes with hundreds of in-region applicants needing no sponsorship. **A referred application is read by a human. A cold one frequently is not.**

**The mistake:** waiting until Week 43 and messaging strangers. A referral is someone putting their reputation on your application. **Nobody does that for someone who appeared in their inbox last Tuesday.**

### ⏰ The pipeline opens Week 18 — 11 January 2027.

**Channel 1 — the Egyptian engineering diaspora. Highest return.** Substantial numbers at Google Dublin and Zurich, Meta London, Amazon Dublin, Microsoft. Find them via LinkedIn alumni search on your university, then other Egyptian universities, filtered by company. **They were where you are. They are disproportionately willing to help and disproportionately under-asked, because most people are too embarrassed to reach out.**

Not "can you refer me":

> I'm a backend engineer in Cairo building a federated messaging backbone — my own wire protocol over QUIC, causal delivery with vector clocks over relays, Raft-replicated relay clusters. I'm working on the federation catch-up protocol now and I'd value fifteen minutes of your view on [one specific technical question you genuinely have]. No obligation and no ask beyond that.

Then have the conversation, be interesting, and follow up two months later with what you built. **The referral, if it comes, comes on its own.** **Target: 3 conversations/month from Week 18. By Week 43 that is 18–20 people who know what you are building.**

**Channel 2 — build in public** (§J.2). **Channel 3 — OSS, especially Matrix** (§J.3). **Channel 4 — the technical report** (W51); most candidates have a GitHub link, **a 20-page report with benchmarks and an honest limitations section is a different object and it gets forwarded.** **Channel 5 — meetups and CFPs**; submit the federation-cost talk for 2028. The CFP is networking even when rejected.

**The direct ask, Week 43, to people you have known for months:**

> I'm applying to [specific role, specific office] this week. Here's the project [link] and my CV. If you're comfortable referring me I'd be grateful; if not, no problem at all — and I'd still value knowing whether the CV reads clearly to someone inside.

**The second half matters.** It gives them an out that is not a rejection, and it frequently produces useful feedback from people who will not refer you.

## J.5 — 🔴 The Logic Leap track: sourcing what a solo project cannot

**Mentoring 37.0%. Communication 34.8%. Collaboration 31.2%. Leadership 17.2%.** KERYX demonstrates **none** of them. You source them from your job — **but that only works if it is deliberate.**

**One hour a week of Track J is reserved for this. Seek these out, in this order:**

| Weeks | What to deliberately do at Logic Leap | The story it becomes |
|---|---|---|
| **1–13** | **Ask to review other people's PRs**, seriously, weekly. Leave the kind of comment you would want. | *"Improving code quality without authority"* |
| **14–27** | **Write one design doc for real work** and circulate it before implementing. Use the §J.1 template. | *"Aligning people on a technical decision"* — the Alternatives section is the artifact |
| **14–27** | **Onboard or unblock someone** — a new joiner, an intern, a colleague on unfamiliar code. Track what they were stuck on. | *"Mentoring"* — the single largest soft gap at 37.0% |
| **28–42** | **Take one cross-team dependency end to end** — something needing another team's input, where you drive the conversation. | *"Cross-functional work"* |
| **28–42** | **Disagree with a senior person, in writing, with data**, and handle the outcome either way. | *"Disagreeing with a senior person"* — a required behavioural story you cannot fabricate |
| **43–52** | **Lead one thing end to end:** scope, plan, delegate a piece, ship, own the outcome. | *"Leading a project"* · Leadership 17.2% |

**Log each in `career/LOGICLEAP.md` as it happens, with dates and specifics.** You will not remember the details in month eleven, and vague behavioural answers are the most common way strong technical candidates fail loops.

> 🔴 **The warning: do not let KERYX eclipse your paid work.** At least four of your fourteen behavioural stories must come from Logic Leap. An interviewer who hears twelve stories about a side project and two about the job you were paid to do draws a conclusion you do not want.

## J.6 — The fourteen behavioural stories

STAR-L: Situation, Task, **Action — 60% of the words, "I" not "we"**, Result **with a number**, Learning. Written by Week 44, recorded on video, then five mock behavioural rounds with a human. **Your material this year is unusually good:**

| # | Prompt | Your story |
|---|---|---|
| 1 | A technically hard problem | Causal delivery, or the Raft Figure 8 case |
| 2 | 🔴 **Finding a serious problem in your own work** | **Coordinated omission in your own harness (W35). Your best story** — it shows the scepticism about your own results that senior engineers are selected for |
| 3 | Being wrong and changing course | The design your own simulator broke before you finished writing it |
| 4 | A failure | The level where your estimate was most wrong, **with the ratio from `RETROSPECTIVE.md`** |
| 5 | Shipping under a hard constraint | Zero budget forcing the ARM port and the 40-relay memory ceiling |
| 6 | An incident | **Clock skew — green dashboards, wrong timestamps, correct ordering, nothing alerting** |
| 7 | A decision with incomplete information | QUIC over TCP, argued from your own measurements |
| 8 | Pushing back / saying no | **No Matrix compatibility, no blockchain, no metadata claims.** Three real ones |
| 9 | Learning something new fast | TLA+, or the Double Ratchet spec |
| 10 | Improving something unasked | The `logstore` torture harness |
| 11 | Proudest achievement | The three federation curves |
| 12 | Mentoring / unblocking | The peer runbook test and the gaps it exposed |
| 13 | Disagreeing with a senior person | **A real one from Logic Leap** |
| 14 | Something from Logic Leap | 🔴 **The 1,000-concurrent-call voice pipeline, or the omnichannel messaging platform.** Use them — they are real production systems at real scale |

**The rules that decide the score:** numbers always · **"I" not "we"** · the Learning is not optional · **90 seconds then stop** · Amazon maps each to a Leadership Principle and **drills with follow-ups that catch fabricated stories — use real ones.**

## J.7 — CV versions

**One page. Every line traceable to something in the repo the day you write it.**

**Structure:** 1. Name, GitHub, **"Cairo, Egypt · open to relocation · requires EU/UK sponsorship"** · 2. Two-line summary · 3. 🔴 **SELECTED PROJECT — KERYX, 5–7 bullets. The largest section, ABOVE employment** · 4. Experience — Logic Leap, 3–4 bullets, quantified · 5. Skills, keyword-matched to the corpus · 6. **Education — one line, last.**

> **The degree line:** *"BSc Management Information Systems, Alexandria University, 2025."* **No parenthetical. No "(self-taught in CS)". No apologetic adjective.** The project section made the argument; restating it next to the degree draws attention to the anxiety rather than the evidence.

> **And the top third is screening surface, not interview content.** The Double Ratchet and causal delivery are what you talk about for forty-five minutes. **The top third of the CV must contain Java, distributed systems, AWS, Python, Go, Kubernetes, Kafka** — in roughly that order, because those are the verified frequencies and a recruiter reads nothing else.

**Every bullet is X-Y-Z:** *"Accomplished [X] as measured by [Y], by doing [Z]."*

**CV v1 — W18** *(not for applying; it exists so an unexpected opportunity does not find you writing a CV in a panic)*
> **KERYX — federated messaging backbone** · C++20, Java 21, Go, Python · [repo]
> · Implemented TCP from the byte stream up (**Stanford CS144, all 8 checkpoints passing**) and used it to measure head-of-line blocking across six loss profiles, producing the transport decision for the system.
> · Built a C++ LSM message log with a torture harness performing **1,000 kill cycles and syscall-level `fsync`/torn-write fault injection, zero invariant violations**, supporting consistent snapshots under concurrent appends.
> · Implemented causal message delivery with vector clocks over relays; **three relays receiving messages in three different arrival orders produce an identical delivered sequence**, property-tested across 10,000 random interleavings.

**CV v2 — W34**
> · Designed and implemented a **server-to-server federation protocol** with signed events, bounded DAG backfill and unknown-field preservation, plus **an adversarial conformance suite of 80+ cases** runnable against any implementation.
> · Implemented **end-to-end encryption** (X3DH + Double Ratchet, to Signal's published specification) with multi-device support and **tested key-change detection**; a relay operator with full database access cannot read a message.
> · Implemented **Raft** (**MIT 6.5840 Labs 1–3 passing, including `TestFigure8Unreliable`**) as the relay cluster's replication layer; killing the leader mid-fan-out loses zero messages and duplicates zero.

**CV v3 — W42** *(the first version that survives a tier-1 screen — send to your three strongest contacts for feedback, not for referral)*
> · Built a **deterministic simulation harness** running 10,000 seeded fault schedules nightly — including asymmetric partitions, backwards clocks and **relays that lie** — finding 3 correctness bugs no conventional test caught, each reproducible from a seed integer. Model-checked the catch-up protocol in TLA+.
> · **Measured and published the presence fan-out curve**, identifying the room-size threshold at which individual presence broadcast must stop; held goodput at Y% of capacity under 5× offered load via priority shedding against X% for the naive path.
> · Deployed a 20-relay federation across three continents on Kubernetes at **$0/month**; rolling restart of all relays under sustained load with **zero lost and zero duplicated messages**. Full stack in Terraform; CI authenticates via OIDC with zero long-lived credentials.

**CV v4 — W43** *(the one you apply with)*
> · **Published the three federation cost curves that do not exist publicly**: delivery p99 against federation hop count, ordering-violation rate against relay count from 2 to 200, and partition cost against partition duration — with a head-to-head against Matrix's Synapse on identical hardware, reproducible by one script.
> · Ran a chaos programme: **20+ injected incidents** (relay kill mid-fan-out, asymmetric partition, clock skew, certificate expiry, a lying relay in production) each with alerting, root cause and a runbook; separately reproduced 6 famous public outages locally with verified fixes.

## J.8 — Targets, timing and applications

**Applications go to specific offices, not "Google."**

| Company | Offices | Note |
|---|---|---|
| **Google** | Dublin, Zurich, London, Munich, **Warsaw** | Zurich strongest and hardest. **Warsaw more accessible** |
| **Meta** | London, Dublin | London is the main EMEA engineering site |
| **Amazon / AWS** | Dublin, London, Berlin, Luxembourg | Most reqs, **most accessible tier-1 entry** |
| **Microsoft** | Dublin, London, Cambridge, Munich, **Cairo** | 🔴 **The only tier-1 with engineering in Egypt. Apply there in W43 regardless** — a local tier-1 role is a legitimate route to an internal transfer |
| **Stripe** | Dublin, London | Backend-heavy, **values written communication — your report and ADRs are unusually well matched** |
| **Cloudflare** | London, Lisbon | 🔴 **Network and systems heavy. Your TCP implementation, QUIC work and NAT traversal are directly their domain** |
| **Datadog** | Paris, Dublin | Ingest and query at enormous scale; your L8 work is their product |

**🔴 The tier that is literally your project's domain — and it is not the fallback tier:**
**Element / Matrix.org** (London — *you will have implemented their problem, read their spec all year, and possibly contributed to it*) · **Signal** (remote) · **Discord** (remote/SF — real-time fan-out at enormous scale) · **Slack/Salesforce** (Dublin, London) · **Zoom, Twilio, Vonage, Agora** (real-time infrastructure, your CV's voice-pipeline work lands here) · **Confluent** (London, Kafka) · **Grafana Labs** (remote-first) · **Tailscale** (remote — NAT traversal is their entire company) · **Cloudflare** again · **Canonical** (fully remote, hires globally, heavy systems interviews) · **Bloomberg** (London, large C++ and Java).

**Calibration tier** (W30–42, no cooldown risk): Instabug, Swvl, Halan, Paymob, MaxAB (Cairo); Careem, Talabat, Tabby (Gulf); any European startup with a real systems interview.

| Weeks | Volume | Targets |
|---|---|---|
| 30–42 | 2–3/month | **Calibration tier only** |
| 43–45 | 16/week (48) | **Tier-1 EMEA first**, plus Element, Tailscale, Cloudflare, Discord — **your best-fit tier** |
| 46–49 | 12/week (48) | Remaining tier-1 and second tier |
| 50–52 | 8/week | Fill gaps; the pipeline is mostly conversion now |

**≈150 applications**, every one logged in `career/APPLICATIONS.md` — date, company, office, role, referral (y/n, by whom), response, stage, outcome. **You cannot reconstruct this later and you need it to compute response rate and stage conversion.**

**Sequence your loops:** 3–4 companies you care less about *first*. Your fifth loop is dramatically better than your first. **Then overlap the real ones so offers arrive within ~2 weeks** — competing offers are the only real leverage.

### 🚨 If the response rate is low (checked W45, ~48 out)
**Below 10%, stop and diagnose before sending more with the same CV.** In order: **targeting** (reqs wanting 5+ years will not respond regardless — check the level distribution) · **the sponsorship filter** (some reqs auto-reject; invisible, and not about you) · **the top third of the CV** (if it does not contain Java 53.3%, distributed systems 48.9%, AWS 48.9%, Python 43.5%, Go 38.0%, Kubernetes 30.4%, Kafka 20.7%, it is miscalibrated) · **the referral ratio** (under a third referred? the fix is §J.4, not more applications).

**Do not respond to a low response rate by increasing volume.** That converts a fixable problem into a burned target list.

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
| **Google** | Phone screen → 2–3 coding, 1 system design, 1 Googleyness & Leadership. Then **hiring committee and team matching** — a strong loop can stall at team match. **Normal, not a rejection** |
| **Meta** | Phone screen (**2 problems in 45 min — speed matters more here than anywhere**) → 2 coding, 1 system design, 1 behavioural |
| **Amazon** | OA → 4–5 rounds, **every round includes Leadership Principle questions.** The **Bar Raiser** is external with veto power |
| **Microsoft** | Coding + design + an "as appropriate" round with a senior leader |
| **Cloudflare / Stripe / Datadog / Element / Tailscale** | **Practical over puzzle:** debugging unfamiliar code, extending real code, deep systems discussion, plus design. **KERYX prepares you for these better than any other project could** |

**Leveling:** L3/E3 (new grad) → **L4/E4 (2–5 yrs)** → **L5/E5 (5+ yrs, owns ambiguous projects end to end — where system design decides it).** **Interview for the level your evidence supports.** Being under-levelled costs years of compensation; push back with evidence if the loop went well.

---
---

# PART XV — The Library

## The spine — with the chapters that matter

| # | Book | When | Chapters |
|---|---|---|---|
| 1 | **Kleppmann, *Designing Data-Intensive Applications*** *(you own it)* | Throughout | **Ch. 3** (storage, L3) · **5–6** (replication, partitioning, L4/L6) · **7** (transactions, F6) · **8** (partial failure, unreliable clocks — **the theoretical spine of KERYX**, L3/L6) · **9** (consistency and consensus, L6) · **11** (streams, L4) |
| 2 | **Alex Xu, *System Design Interview* Vol. 1 & 2** *(you own them)* | Track I, weekly | **Vol 1 ch. 1** (estimation) · **4** (rate limiting) · **5** (consistent hashing) · **6, 8** (cache, CDN) · **11** (queues) · **12** (chat system — read it, then do better) · **Vol 2** for applied designs |
| 3 | **Bryant & O'Hallaron, *CS:APP* 3rd ed.** | L0, L8 | **§6.2–6.4** (memory hierarchy) · **ch. 5** (optimising performance) |
| 4 | **Arpaci-Dusseau, *OSTEP*** *(free)* | L1 | **Ch. 4–7** (processes) · **13–16, 18–19** (VM, TLB) · **25–33** (concurrency) |
| 5 | **Kurose & Ross, *Computer Networking* 8th ed.** | **L2** | **Ch. 3 in full.** The most valuable chapter in the book, and the theory beside CS144 |
| 6 | **Fall & Stevens, *TCP/IP Illustrated Vol. 1*** | **L2** | **Ch. 13, 14, 15.** The reference when CS144's framework leaves a gap |
| 7 | **Grigorik, *High Performance Browser Networking*** *(free, hpbn.co)* | L2 | **Ch. 1–4**, and the UDP chapter specifically |
| 8 | **Petrov, *Database Internals*** | **L3** | **Ch. 2–5.** Part I is the best storage-engine treatment in print. Skip Part II |
| 9 | **Goetz et al., *Java Concurrency in Practice*** | **L4**, F7 | **Ch. 3, 5, 10, 11.** Skip the dated executor material |
| 10 | **Aumasson, *Serious Cryptography* 2nd ed.** | **L5** | **Ch. 1, 3, 8, 9, 10, 11** |
| 11 | **Nygard, *Release It!* 2nd ed.** | L8, L9 | **The origin of circuit breaker and bulkhead as named patterns. The most relevant book to Levels 8 and 9** |
| 12 | **Google, *SRE* + *SRE Workbook*** *(free)* | L8–L9 | **SRE ch. 3, 4, 6, 21, 22** (ch. 22 is the most valuable chapter) + **Workbook ch. 5** |
| 13 | **Majors, Fong-Jones, Miranda, *Observability Engineering*** | L8 | **Ch. 1–6** |
| 14 | **Lukša, *Kubernetes in Action* 2nd ed.** | L8 | **Ch. 1–7, 12, 17** |
| 15 | **Gregg, *Systems Performance* 2nd ed.** | L0, F10 | **Ch. 6 §6.6, ch. 13.** Reference |
| 16 | **Ousterhout, *A Philosophy of Software Design*** | L3 | Short, sharp, and more right than *Clean Code* where they disagree |
| 17 | **Mitzenmacher & Upfal, *Probability and Computing*** | F8 | **Ch. 5** (balls into bins — literally your shard-distribution problem), **§14.1** |
| 18 | **Skiena, *Algorithm Design Manual* 3rd ed.** | L6, Track I | **Ch. 8** (DP), **ch. 9** (intractability and reductions) |
| 19 | **Laaksonen, *Competitive Programmer's Handbook*** *(free)* | Track I | **Ch. 7, 9, 13–15, 26** |
| 20 | **Winters, Manshreck, Wright, *Software Engineering at Google*** *(free)* | Track J | **Ch. 9** (code review), **11–14** (testing at scale) |

## The papers — one page of notes each, at first assignment

| Paper | Week | Why |
|---|---|---|
| **Dan Kegel, "The C10K Problem"** | W5 | How the industry got here |
| **Jens Axboe, "Efficient IO with io_uring"** | W5 | The primary source |
| **RFC 9000 §2 (QUIC overview)** | W10 | Twelve pages. Then ngtcp2's examples |
| **Cardwell et al., "BBR" (ACM Queue 2016)** | W11 | What modern congestion control optimises for |
| **Gettys & Nichols, "Bufferbloat"** | W11 | Why a bigger buffer makes latency worse |
| **"Bitcask: A Log-Structured Hash Table"** | W13 | 6 pages, your v1 target |
| **Rebello et al., "Can Applications Recover from fsync Failures?"** + the PostgreSQL fsyncgate thread | W14 | Why you cannot retry `fsync` |
| **Athanassoulis et al., "The RUM Conjecture"** | W14 | Read/Update/Memory — pick two |
| **O'Neil et al., "The Log-Structured Merge-Tree" (1996)** | W15 | The original LSM paper |
| 🔴 **Lamport, "Time, Clocks, and the Ordering of Events" (1978)** | **W16** | **Eight pages. The most cited paper in the field. Read it in W16, W34 and W45 — it reads differently each time** |
| **Shapiro et al., "Conflict-free Replicated Data Types" (2011)** | W17 | §3–4. The algebra of merging without coordination |
| **Kleppmann, "A Critique of the CAP Theorem"** | W17 | It will stop you saying CP/AP like it means something precise |
| **The Matrix Server-Server API specification** | **W19** | 🔴 **The best-documented federated messaging protocol in existence. Read it to learn the problems, then design your own** |
| **XMPP RFC 6120 §4–5** | W20 | Twenty-five years of federation experience, compressed |
| 🔴 **The Signal Double Ratchet + X3DH specifications** | **W24** | **The thing you implement. Invent nothing** |
| **Cohn-Gordon et al., "A Formal Security Analysis of the Signal Protocol" (2017)** | W26 | So you can state precisely what the ratchet gives you |
| 🔴 **Ongaro & Ousterhout, Raft — EXTENDED version** | **W28** | **§5 in full, §6 carefully. The conference version omits crucial detail** |
| **Ongaro's PhD thesis** | W30 | Log compaction and membership changes, done properly |
| **Gjengset, "Students' Guide to Raft"** | W28 | **Read before you start, not when you are stuck** |
| **Kleppmann, "How to do distributed locking"** + antirez's reply | W31 | Fencing tokens. **Read both** |
| 🔴 **Will Wilson, "Testing Distributed Systems w/ Deterministic Simulation" (2014)** | **W34** | **The most valuable 40 minutes in this roadmap** |
| **Zhou et al., "FoundationDB" (SIGMOD 2021) §4** | W35 | Simulation, as a production system does it |
| **Newcombe et al., "How AWS Uses Formal Methods" (CACM 2015)** | W36 | Why TLA+ is worth your hours |
| **Dean & Barroso, "The Tail at Scale" (CACM 2013)** | W39 | Eight pages. The basis of Level 8 |
| **Bronson et al., "Metastable Failures" (HotOS 2021)** | W40 | The failure class nobody names |
| **Mitzenmacher, "The Power of Two Choices: A Survey"** | W40 | Placement |
| **Ford, Srisuresh & Kegel, "Peer-to-Peer Communication Across NATs" (2005)** | W46 | The paper that named hole punching |
| **Das, Gupta, Motivala, "SWIM" (DSN 2002)** | W47 | Membership. Short and unusually clear |
| **Hayashibara et al., "The φ Accrual Failure Detector" (2004)** | W47 | Failure detection that adapts |
| **Berenson, Bernstein, Gray et al., "A Critique of ANSI SQL Isolation Levels" (1995)** | F6 | Named the anomalies the standard forgot |

**For each: a one-page summary** — what problem, what was the key insight, what did they give up, what would you do differently in 2027, what system today embodies it. **Thirty one-pagers is a genuinely impressive public artifact and almost nobody has one.**

## Free reference
`aws.amazon.com/builders-library` **(read all ~20 across L8–L9)** · `k8s.af` **(read 10)** · `jepsen.io/analyses` · `sre.google/books` · `learntla.com` · `github.com/danluu/post-mortems` · `spec.matrix.org` · `hpbn.co` · `use-the-index-luke.com` · `neetcode.io` · `cs144.github.io` · `pdos.csail.mit.edu/6.824` · `15445.courses.cs.cmu.edu` · `levels.fyi` · `brooker.co.za`

## People to read
Martin Kleppmann · **Marc Brooker** (`brooker.co.za` — the best working systems writer today) · Brendan Gregg · Julia Evans · Dan Luu · **Kyle Kingsbury (aphyr)** · Hillel Wayne · Charity Majors · Alex Petrov · **Aleksey Shipilëv** (JVM) · **Matthew Green** (crypto) · **the TigerBeetle team** (simulation) · **Matthew Hodgson and the Matrix team** (federation, and they blog honestly about what is hard) · Gergely Orosz

---
---

# PART XVI — The 52-Week Calendar

**Standard week: 32h = 19 Depth / 8 Interview / 3 Fundamentals / 2 Craft. From W43: 12 Depth / 12 Interview / 8 Career.**
**Your shape: 4h weekdays + 6h each weekend day.** Weekdays are DSA, system design, fundamentals and reading. **The weekend blocks are where KERYX is built.**

| Wk | Starts | Lvl | Depth focus | Milestone / Flagship | I | F | J | Tot |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-14 | 0 | Repo, CI, toolchains (C++/Java/Go/Py), `latency-lab` | — | 8 | F1 3 | 2 | 32 |
| 2 | 09-21 | 0 | **🔴 SCALE SPIKE: relay ceiling? Oracle reachable?** `lab/bench`, `sickbay`, `1brc` v1 | `SCALE-RISK.md` **go/no-go** | 8 | F1 3 | 2 | 32 |
| 3 | 09-28 | 1 | **Four wire attacks all work.** Framing, length caps, the codec | ⚙️ sanitizers + libFuzzer in CI | 8 | F2 3 | 2 | 32 |
| 4 | 10-05 | 1 | Varints, zero-copy views, arena allocation, authenticated frames | — | 8 | F2 3 | 2 | 32 |
| 5 | 10-12 | 1 | `c10k-arena` — seven concurrency models incl. virtual threads | — | 8 | F3 3 | 2 | 32 |
| 6 | 10-19 | 1 | Handshake, capability negotiation, pinned-old-client test | **K0** · **#1 `hardened`** | 8 | F3 3 | 2 | 32 |
| 7 | 10-26 | 2 | 📺 CS144 ckpt 0–1: byte stream, reassembler | — | 8 | F4 3 | 2 | 32 |
| 8 | 11-02 | 2 | 📺 CS144 ckpt 2: the receiver, seq numbers, windows | — | 8 | F4 3 | 2 | 32 |
| 9 | 11-09 | 2 | 📺 CS144 ckpt 3: the sender, retransmission, RTT estimation | — | 8 | F4 3 | 2 | 32 |
| 10 | 11-16 | 2 | 📺 CS144 ckpt 4: the full connection. **The HOL-blocking chart** | ADR-0002 | 8 | F5 3 | 2 | 32 |
| 11 | 11-23 | 2 | 📺 CS144 ckpt 5–7: ARP, the IP router. Congestion control theory | **#2 `minnow`** | 8 | F5 3 | 2 | 32 |
| 12 | 11-30 | — | 🛌 **REST** — QUIC via ngtcp2, the kernel-vs-mine comparison, **category count** | **K1** | 6 | — | 2 | 10 |
| 13 | 12-07 | 3 | 📺 15-445 lec 1–5. `logstore` v1: append log, CRC framing | — | 8 | F6 3 | 2 | 32 |
| 14 | 12-14 | 3 | 📺 15-445 Project 1 (buffer pool). SSTs, compaction, Bloom | **AWS free tier signup** | 8 | F6 3 | 2 | 32 |
| 15 | 12-21 | 3 | 📺 15-445 Project 2 (B+Tree). **The torture harness + `LD_PRELOAD`** | **#3 `logstore`** | 8 | F6 3 | 2 | 32 |
| 16 | 12-28 | 3 | 📺 15-445 recovery lectures ×2. **Consistent snapshot under writes.** Lamport 1978 | — | 8 | F7 3 | 2 | 32 |
| 17 | 2027-01-04 | 3 | **Causal order: the wall.** Vector clocks, deterministic tie-break | — | 8 | F7 3 | 2 | 32 |
| 18 | 01-11 | 3 | Causal delivery, 10k interleavings, three-relay agreement test | **K2** · **⚑ CV v1** · **🤝 REFERRALS OPEN** | 8 | F7 3 | 2 | 32 |
| 19 | 01-18 | 4 | ☕ **Java ramp: naive port is 15× slower — find out why.** Read the Matrix S2S spec | — | 8 | F8 3 | 2 | 32 |
| 20 | 01-25 | 4 | Off-heap, zero-allocation fan-out, virtual-thread delivery engine | — | 8 | F8 3 | 2 | 32 |
| 21 | 02-01 | 4 | **Federation v1: two relays share a room.** Signed events, the auth DAG | — | 8 | F9 3 | 2 | 32 |
| 22 | 02-08 | 4 | 🌙 🔧 **BUFFER + pre-Ramadan pull-forward:** backfill, state resolution, **read Boneh wk 1–2 + the Signal specs** | — | 8 | F9 3 | 2 | 32 |
| 23 | 02-15 | 4 | 🌙 **`conform`** — the adversarial conformance suite | **K3** · **#4 `conform`** | 5 | F9 2 | 2 | **20** |
| 24 | 02-22 | 5 | 🌙 📺 Boneh wk 1–4. X3DH, prekeys | — | 5 | F9 2 | 2 | **20** |
| 25 | 03-01 | 5 | 🌙 **The Double Ratchet**, skipped-key bounds, multi-device | — | 5 | — 2 | 2 | **20** |
| 26 | 03-08 | 5 | 🌙 Eid. **Key-change detection.** 📺 6.858 threat-model lectures | **K4** | 5 | — 2 | 2 | **20** |
| 27 | 03-15 | — | 🛌 **REST** — **🚩 HALF-YEAR GATE**, `threat-model.md`, **category count** | — | 6 | — | 2 | 10 |
| 28 | 03-22 | 6 | 📺 6.5840 lectures + Lab 1 (MapReduce). Read Raft extended + Gjengset | — | 8 | F10 3 | 2 | 32 |
| 29 | 03-29 | 6 | 📺 6.5840 Lab 2 (KV, at-most-once RPC) | — | 8 | F10 3 | 2 | 32 |
| 30 | 04-05 | 6 | 📺 6.5840 Lab 3A/3B: elections, log replication | **first calibration applications** | 8 | F11 3 | 2 | 32 |
| 31 | 04-12 | 6 | 📺 6.5840 Lab 3C: persistence, **Figure 8** | — | 8 | F11 3 | 2 | 32 |
| 32 | 04-19 | 6 | 📺 6.5840 Lab 3D: snapshots. `TestFigure8Unreliable` | **#5 `raft`** | 8 | F11 3 | 2 | 32 |
| 33 | 04-26 | 6 | `keryx-raft` in Java. **🎯 Figure 8 whiteboard test + first human mock + paid mock** | — | 8 | — 3 | 2 | 32 |
| 34 | 05-03 | 6 | 🔧 **BUFFER** + fencing tokens + ADR-0006 + **watch Will Wilson** | **K5** · **⚑ CV v2** · **🚩 two-thirds gate** | 8 | — 3 | 2 | 32 |
| 35 | 05-10 | 7 | `keryxsim`: sim clock/network/disk/scheduler · **🔴 F12 harness audit** | — | 8 | F12 3 | 2 | 32 |
| 36 | 05-17 | 7 | 🌙 Eid al-Adha. **`LyingRelay`**, the invariant checker | — | 6 | F13 2 | 1 | **26** |
| 37 | 05-24 | 7 | 10,000 seeds nightly. **Find ≥3 bugs** | **#6 `keryxsim`** | 8 | F13 3 | 2 | 32 |
| 38 | 05-31 | — | 🛌 **REST** — TLA+ on catch-up, **Final Gauntlet**, **LOOP #1**, category count | **K6** | 6 | — | 2 | 10 |
| 39 | 06-07 | 8 | **Presence is O(N²).** The curve, five mitigations, the threshold | — | 8 | F14/F16 3 | 2 | 32 |
| 40 | 06-14 | 8 | **The goodput collapse curve.** Shedding, backpressure, metastable | **#7 `presence-storm`** | 8 | F14 3 | 2 | 32 |
| 41 | 06-21 | 8 | **k8s: 20-relay federation, rolling restart zero loss, the 3am dashboard** | — | 8 | F15 3 | 2 | 32 |
| 42 | 06-28 | 8 | **★ THE PUBLIC DEMO.** AWS, ARM port, three-continent federation, `costwatch` | **K7** · **⚑ CV v3** | 8 | F15 3 | 2 | 32 |
| 43 | 07-05 | 9 | **🎯 CV v4 · FIRST 48 APPLICATIONS · referral activation** · chaos framework | — | 12 | 0 | 8 | 32 |
| 44 | 07-12 | 9 | **`incident-lab`**: 20 incidents + **clock skew** + cold start · **LOOP #2** | — | 12 | 0 | 8 | 32 |
| 45 | 07-19 | 9 | 🔧 **BUFFER** + 6 famous outages + the seven-mechanisms essay + `gatekeep` · **🚨 response-rate gate** | **K8** · **#8 `incident-lab`** | 12 | 0 | 8 | 32 |
| 46 | 07-26 | 10 | **NAT traversal, hole punching, the reachability table** · **LOOP #3** | — | 12 | 0 | 8 | 32 |
| 47 | 08-02 | 10 | SWIM gossip, phi-accrual, asymmetric partition · **LOOP #4** | — | 12 | 0 | 8 | 32 |
| 48 | 08-09 | 10 | **Store-and-forward.** The demo's PARTITION button goes real · **LOOP #5** | **K9** · **#9 `natlab`** | 12 | 0 | 8 | 32 |
| 49 | 08-16 | — | 🛌 **REST** — pipeline review, **category count**, `pgshift` | — | 6 | — | 4 | 10 |
| 50 | 08-23 | 11 | **The three curves.** GCP 200-relay window · **LOOPS #6–7** | — | 14 | 0 | 6 | 32 |
| 51 | 08-30 | 11 | **Synapse head-to-head**, `sim-fidelity.md`, `1brc` v2, `docs/REPORT.md` · **LOOPS #8–9** | **K10** · **#10 `fedbench`** | 14 | 0 | 6 | 32 |
| 52 | 09-06 | 12 | **README, TOUR, 10 ADRs, LIMITATIONS, COMPARISON, RETROSPECTIVE, NEXT** · **LOOPS #10–12** | **K11** | 14 | 0 | 6 | 32 |

**Budget check:** 52 × 32 = 1,664 nominal. −88 (rest weeks 12, 27, 38, 49 at 10h) −48 (Ramadan weeks 23–26 at 20h) −6 (Eid al-Adha week 36 at 26h) = **1,522 effective hours.**

---
---

# PART XVII — The Cut Order & Re-Plan Triggers

**You chose full scope with a named cut order. This is it.** Cut in this sequence, top first. **Never out of order, and never silently — every cut gets a line in `docs/LIMITATIONS.md` saying what was dropped and why.**

| # | What gets cut | Costs you | Why it is first |
|---|---|---|---|
| 1 | **Matrix protocol compatibility** (already a non-goal — a reminder not to re-add it) | Nothing. It is an interoperability project, not a systems project | It is the most seductive scope creep in this domain |
| 2 | **The web client's polish** | Nothing measurable. Keep the demo and the WebSocket backpressure work | Frontend is ~0% of your target postings |
| 3 | **Store-and-forward** (L10) — keep NAT traversal and direct paths | The delay-tolerant story. The mesh still works when relays are up | The purpose survives on the direct-path half |
| 4 | **`pgshift`** | PostgreSQL evidence drops from strong to adequate | Postgres is 19.6%; the metadata store and migrations survive |
| 5 | **The GCP 200-relay window** | Curve 2 stops at 40 relays and `sim-fidelity.md` gets weaker — **and you must say so** | Costs credibility, not correctness |
| 6 | **CS144 checkpoints 5–7** (the IP router) — keep 0–4, the TCP itself | "All 8 passing" becomes "checkpoints 0–4 passing" | The router is below your abstraction; the TCP is not |
| 7 | **6.5840 Lab 1** (MapReduce) — go straight to Labs 2–3 | A warm-up, and one line on the CV | Raft is the artifact; MapReduce is not |
| 8 | **Two of the six reproduced outages** | `incident-lab` weakens but survives at four | The 20 self-inflicted incidents matter more than the famous ones |
| 9 | **The ARM port and the x86/ARM analysis** | A nice free result and one blog post | Genuinely optional |
| 10 | **15-445 Project 2** (B+Tree) — keep Project 1 and the recovery lectures | Index evidence thins; the log and the WAL survive | The message log is an LSM; the B+Tree is adjacent |

## 🔴 What is NEVER cut

| Never cut | Because |
|---|---|
| **Causal ordering (L3) and the federation protocol (L4)** | They are the project. Without them KERYX is a chat app and the year's argument collapses |
| **The `logstore` torture harness** | It is the proof that correctness is something you *prove*. The engine without it is a tutorial |
| **Java (L4)** | 53.3% — the single most-demanded skill in your corpus, and the largest measured gap in your profile |
| **The operational shell — k8s, observability, on-call (L8, L9)** | **It is what the screen reads.** The core is what you talk about; the shell is what gets you read |
| **★ The public demo (W42)** | Your stated success condition |
| **The Track I hours** | The only track that degrades irreversibly. A missed week is not recoverable by working harder later |
| **Applications from W43** | The plan's entire purpose. Everything else is instrumental |
| **The Logic Leap track (J.5)** | 37.0% + 34.8% + 31.2% + 17.2% of postings, and nothing else in the plan touches them |

**The decision is forced at three gates: Week 27, Week 34, Week 45.** At each, count how many weeks behind you are and **cut that many items off the top of the list.** **Cutting at a gate is a decision. Discovering in Week 48 that you cannot finish is a failure.**

## 🚨 Re-plan triggers

**Re-planning is not failure; it is the plan working.**

| Trigger | Response |
|---|---|
| **Cumulative deficit > 40h** | **Cut scope in the order above. Do not compress estimates** |
| **All buffer weeks gone before W34** | Estimates are systematically wrong. **Recompute Levels 8–12 with your measured ratio from `LOG.md`**, and **seriously consider the 18-month Extended Track** |
| **Two consecutive checkpoints where the repo is not interview-ready** | **Stop feature work entirely for one week.** README, build, demo. Overrides everything |
| **Three consecutive weeks of Track I under 5h** | The project is eating the track you explicitly protected. **Invert the week — interview first, project with what is left — for two weeks** |
| **The Week-2 scale spike fails** — too few relays fit, or you cannot reach Oracle | **Decide in Week 2.** Substitute 8–12 relays with the simulator carrying scale from month one, **stated in the README as the primary limitation.** Do not carry the uncertainty forward |
| **CS144 overruns Week 12** | Take it from W22's buffer, and cut checkpoints 5–7. **Do not cut checkpoints 0–4** — they are the artifact |
| **6.5840 Lab 3 overruns Week 33** | **Expected, and normal.** Take W34's buffer. **Do not skip `TestFigure8Unreliable`** — passing it is the claim |
| **The Java ramp overruns Week 20** | You are 15h down and Level 4 is the wrong place to be behind. Cut the conformance suite to 40 cases. **Do not cut the zero-allocation exercise** |
| **Response rate <10% at W45** | Diagnose per §J.8 **before** sending more |
| 🔴 **You have not opened the repo in 7 days** | **The most important trigger and the easiest to ignore.** Do not restart at 32 hours. One 2-hour session, then one 4-hour session, then resume. **Restarting at full intensity after a break is how a one-week gap becomes a one-month one** |

## What does NOT trigger a re-plan

- **A bad week.** Noise.
- **A target you missed.** Targets set before measurement are estimates. **Record both numbers and move on.**
- **A negative result.** Being slower than Synapse, or a sim-fidelity divergence larger than you hoped, **are results.** They get written up and become interview material.
- **Feeling behind.** Check `LOG.md`.
- 🔴 **A better project idea.** It will happen, probably around Level 4 and again around Level 8. **The answer is no.** Write it in `docs/IDEAS.md` and continue. **You have now changed spine five times at week zero, when it was free. Changing again in month four costs you the accumulated depth that is the entire point of a single system.**

## Tracking — three artifacts, three rituals, ~45 min/week

| File | Contains | Written |
|---|---|---|
| `LOG.md` | Hours by track, task outcomes, weekly review, monthly checkpoint | Daily + Sunday |
| `dsa/FAILURES.md` | Every failed problem, in the §XII format | As it happens |
| `career/APPLICATIONS.md` | Every application, with response and stage | As it happens |
| `career/LOGICLEAP.md` | The §J.5 situations, dated | As they happen |

**Daily — 2 minutes.** `2026-09-28 · D:4.0 I:1.5 F:0 J:0 · Frame codec: length cap + CRC done; fuzzer found an OOB read at offset 12 (fixed). Varints tomorrow.` **Log the hours you actually worked, not the hours you sat at the desk.** The Week-52 retrospective is only useful if this is honest.

**Weekly review — Sunday, 30 minutes.** Hours by track vs budget (a deficit up to 3h is noise; **three consecutive deficit weeks is a signal**) · **which tasks met their acceptance criterion — met or not met, "partially" is not a category** · which targets you set before measuring and what you got, **both numbers** · what did not finish and whether it blocks next week — **never silently carry unfinished work forward** · Track I: attempted / solved / failed / re-solved · Logic Leap: anything worth a J.5 entry? **If four weeks pass with nothing, go and create the situation** · one sentence: the biggest risk to the next four weeks, **a specific thing, not a feeling.**

**Monthly checkpoint — at each level boundary.** Exit criteria one at a time, **met or waived in writing with a reason, no third option** · hours actual vs budget, month and cumulative · 🔴 **is the repository interview-ready RIGHT NOW?** Three checks, *performed*: does `make bootstrap` work on a clean clone — **actually run it**; does the README describe what exists rather than what is planned; **can you speak for 45 minutes about it today, without preparation?** If any is no, fixing it is next week's top priority · **the corpus gaps**, one line each, closed / in progress / not started, **and what the evidence is — not what you read, what is running** · 🔴 **the failure-category count** · from W18, the referral pipeline · from W43, applications, responses, rate, stage conversion · one paragraph: **is the plan still right?** Not "am I on schedule" — whether it still describes the correct work.

---
---

# PART XVIII — Assessment: The Three Proofs

You do not "finish" a level. You **prove** it, three ways.

| Proof | What | Why |
|---|---|---|
| **1. The Exam** | The written questions at the level's end, no notes, timed | Retrieval under pressure — the interview condition |
| **2. The Artifact** | The project, exit criteria met, **numbers published** | That you can actually build it |
| **3. The Teach-Back** | **Explain the level's hardest concept to a camera in 10 minutes, no notes, with a diagram** | **The strictest test there is. You cannot fake teaching** |

**Fail any of the three and the level is not done.** This is the discipline that separates someone who "went through" a roadmap from someone who is dangerous.

## The Final Gauntlet — one week, Week 38, before your first real loop

| Day | Challenge | Pass condition |
|---|---|---|
| 1 | 4 LeetCode Mediums + 1 Hard, timed, **narrated aloud, recorded** | 4/5 unaided within time |
| 2 | 2 system designs, 45 min each, on video | Both hit the rubric |
| 3 | **Debug a sabotaged KERYX** — have a peer break it without telling you what | Root cause in <45 min **with evidence** |
| 4 | All 14 behavioural stories on video, cold | Each ≤90s, quantified, first person, **≥4 from Logic Leap** |
| 5 | Write a full design doc for a **novel** problem in 3 hours | All 10 sections, **3+ real alternatives** |
| 6 | **Teach-back: causal delivery · Raft's Figure 8 · the Double Ratchet.** 10 min each | No notes, correct, with diagrams |
| 7 | Watch every video from days 1–6 and **grade yourself against the rubrics** | Honest scoring |

**Pass = ready to interview. Fail any day → that is your next two weeks.**

## The spaced-repetition deck

**One card per non-obvious fact, written by you.** Downloaded decks do not work; cards you write do. Target ~600. Categories: latency numbers · isolation-level anomalies · **Raft rules** · **the NAT type matrix** · **TCP state transitions** · JVM GC and allocation facts · algorithm complexities · Linux commands and **what they *answer*** · failure modes · estimation constants · **your own measured numbers.**

**15 min/day, non-negotiable.** The difference between knowing something in month 3 and knowing it in month 12 when the interview happens.

---
---

# PART XIX — The Final Readiness Checklist

## Can you build it?
- [ ] A wire protocol a fuzzer cannot break, with the bugs it found before it was clean, written up
- [ ] **A TCP implementation that passes Stanford CS144's full test suite and interoperates with the kernel's**
- [ ] A message log that survives 1,000 kills and injected `fsync` failures
- [ ] **Causal delivery where three relays receiving different arrival orders produce an identical sequence**
- [ ] A federation protocol with a hostile conformance suite, and 80/80 passing
- [ ] **End-to-end encryption where the operator cannot read a message and a swapped key is detected**
- [ ] **Raft — MIT 6.5840 Labs 1–3 passing, including `TestFigure8Unreliable`**
- [ ] A simulator that found three bugs your tests did not, each reproducible from an integer
- [ ] Goodput held at 5× offered load by shedding, not collapsing
- [ ] **A page a stranger can open, kill a relay on, and watch every message still arrive**

## Can you explain it?
- [ ] Why wall-clock timestamps make a conversation read wrong, and what replaces them
- [ ] The difference between Lamport timestamps and vector clocks, and what each cannot tell you
- [ ] **Head-of-line blocking, with the number from your own chart, and why your transport is QUIC**
- [ ] Why you cannot retry a failed `fsync`
- [ ] Forward secrecy vs post-compromise security, and which ratchet gives which
- [ ] **Why confidentiality without key-change detection is theatre**
- [ ] **Raft's Figure 8, at a whiteboard, in five minutes, from memory**
- [ ] What consensus does NOT give you — all three parts of the exactly-once story
- [ ] **Why presence is O(N²) and what every large system actually does about it**
- [ ] Why random load shedding is unacceptable in a messaging system
- [ ] Coordinated omission, and why you re-measured eight months of results
- [ ] Why p99 goes vertical at 90% utilisation
- [ ] Which NAT type defeats hole punching, and what it costs you
- [ ] **Why you would not use KERYX instead of Matrix** — and what you learned building it anyway
- [ ] **What your relays still learn about your users, and why you say it unprompted**

## Can you diagnose it?
- [ ] Root-cause a sabotaged federation in under 45 minutes, with evidence
- [ ] Read a flame graph in 10 seconds and say what you would fix
- [ ] Given "p99 is 3s, CPU is 8%", name three causes and the command that distinguishes them
- [ ] **Given green dashboards and wrong timestamps but correct ordering, find the clock**
- [ ] Given an OOMKill at a 4GB limit with a 3GB heap, name four consumers of the difference

## Can you interview?
- [ ] **600+ problems, ≥70% unaided in 25 minutes** · 25+ Hard · Codeforces ≥1750
- [ ] A random Medium, **narrated**, in 25 minutes, on video, repeatedly
- [ ] **20 system designs**, 45 min each, hitting the rubric
- [ ] 14 behavioural stories, ≤90s, quantified, first person, **≥4 from Logic Leap**
- [ ] **12+ full timed loops** · **the Final Gauntlet passed**

## Do they know you exist?
- [ ] **6 pinned repos**, each with a diagram and a headline number in the first screen
- [ ] **10 technical posts published** — at least three about a *result*, not a tutorial
- [ ] **3+ merged OSS PRs, one non-trivial, ideally in Matrix or pion**
- [ ] One talk given
- [ ] **18–20 people at target companies who know what you are building, from conversations that started in January**
- [ ] **A CV where every bullet has a number**
- [ ] **A live demo link that works right now**

---

# 🎯 What success means on 2027-09-12

**Not an offer.** Offer timing is not under your control, the strongest window falls exactly where your loops land, and treating an offer as the criterion makes you optimise for the wrong things in Levels 9 through 11.

> **The criterion: you are a candidate who cannot be screened out on credentials, and cannot be caught out in a system design round.**

If that is true and you have no offer yet, **the plan worked and the timing has not resolved.** Execute `docs/NEXT.md` through October.
If it is not true, **`docs/RETROSPECTIVE.md` tells you which level to return to — with numbers rather than a feeling.**

---

# Closing

Three things decide whether this works.

**1. You must actually reproduce the failures.** The Walls are not flavour text. Reading "TCP is a byte stream" produces a fact you will forget. Watching two of your own messages arrive glued together produces an instinct you will have for twenty years. **The four you will remember longest:** a four-byte length prefix killing your own server in Week 3 · one lost packet stalling ten conversations in Week 10 · a conversation reading as nonsense in Week 17 because you trusted a clock · and a relay in Week 37 that stayed up, answered every probe, and quietly lied.

**2. You must run all four tracks at once.** Depth without the interview track means nobody ever sees the depth — you fail the phone screen and never reach the design round. The interview track without depth gets you an L4 offer and a six-year stall. Craft without either is empty. **It is genuinely harder to run four tracks than one, and it is the reason most people who "study systems for a year" do not convert it into an offer.**

**3. You must ship publicly, and honestly.** The gap between *"I understand distributed systems"* and *"here is a federated messaging backbone, here is a TCP I wrote that passes Stanford's tests, here is the storage engine that survives a thousand kills, here is causal delivery where three relays independently agree, here is Raft that passes MIT's suite, here is the simulator that found three bugs my tests could not, here are the three curves showing what federation actually costs that the Matrix team has never published, here are the twenty incidents I caused on purpose, and here is the document listing everything this does not do"* — **that gap is the entire difference between a candidate and a hire.**

This is roughly **1,522 hours across twelve months.** The output is not a person who finished a roadmap. It is an engineer who has implemented TCP and knows why QUIC exists, built a storage engine that survives being killed a thousand times, made three independent machines agree on the order of a conversation with no clock they trust, implemented consensus from the paper and passed MIT's tests with it, encrypted a conversation so the operator cannot read it and proved the operator cannot swap a key without being caught, written a simulator that models peers who lie, measured what nobody else has measured, kept it all standing at five times its capacity on hardware that costs nothing — **and can explain any of it at a whiteboard from memory, including the parts that do not work.**

There are not many of those. **And exactly one posting in 569 cares what your degree says.**

**Now go write a socket server, send it two messages quickly, and watch them arrive glued together.**
