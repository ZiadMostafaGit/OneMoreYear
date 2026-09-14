# ἌΔΥΤΟΝ · THE ADYTON COLLEGE

## A one-year degree in systems, privacy and distributed engineering — built around one thing you are actually making

> **ἄδυτον** — *adyton*, "the not-to-be-entered." The inner chamber of a Greek temple that only the initiated could pass into. The room whose contents nobody outside gets to assemble.

**Matriculated:** Ziad Mostafa Elsaid · Cairo · 1 year at Logic Leap · BSc Management Information Systems · Codeforces 1450
**Term:** Monday **14 September 2026** → Sunday **12 September 2027** · 52 weeks · ~1,520 hours
**Degree awarded on:** a working system, nine published measurements, and a loop you can pass.

---

## 📖 HOW THIS DOCUMENT WORKS

**This is not a roadmap. It is a course catalogue and a term schedule.**

Open it in the morning. Go to this week. You will find: **the lectures you owe**, **the paper you are reading**, **the article that explains what a real company did about this**, **the book chapter that is not optional**, **the thing you are building**, **the assignment that proves you built it**, **the exam at the end of the level**, and **the questions I refuse to answer — which exist to make you go and find out.**

### 📑 CONTENTS

| Part | What it is | Use it |
|---|---|---|
| **I** | **The Project** — Adyton specified, the scope decision, the demo | Read once, return at every level boundary |
| **II** | **The Evidence Base** — your 569 postings, recomputed | When you doubt a priority |
| **III** | **The Term at a Glance** — 10 levels, 52 weeks, every date | The map |
| **IV** | **The Faculty** — the six you complete, the ones you consult, and **a full elective directory of every free systems course worth knowing** | Before each level starts |
| **V** | **The Departments** — books, papers, specs, articles and tools, by subject, all linked | The library. Part VI tells you which week |
| **VI** | 🔴 **The Term** — **52 week cards. Every one has lectures, reading, the build, exit criteria, DSA, design and questions — and every link is clickable** | **This is the part you open every morning** |
| **VII** | **Track I** — 540 problems, 20 designs, and **`DSA_Mastery.pdf` mapped chapter-by-chapter across all 52 weeks** | Daily |
| **VIII** | **Track J** — writing, OSS, referrals from Week 13, four CV versions, applications | Weekly |
| **IX** | **Assessment, the Cut Order, Tracking** — the three proofs, the Gauntlet, what gets cut first | At every gate |

### The five parts of every week

| Icon | What it is | Rule |
|---|---|---|
| 📺 | **Lectures** — a named course, a numbered lecture, a link | Watched at 1.25–1.5×, with the slides open, and *paused* to write things down |
| 📄 | **Reading** — a paper, a spec, an article, a chapter, a link | **Papers get a one-page note.** What problem, what insight, what did they give up, what would you do differently in 2027 |
| 🛠 | **The build** — this week's contribution to Adyton | Weekend blocks. **Nothing hard is ever built in 45-minute slices** |
| ✅ | **Assignments** — the labs and the exit criteria, with numbers | "Partially" is not a category. Met, or not met |
| ❓ | **The questions** — I ask, you go find out | **No answer is given anywhere in this document.** That is deliberate. The looking-up is the lesson |

### The four tracks, run simultaneously — never one after the other

```
TRACK D — DEPTH            19 h/wk   the courses + Adyton.  Weekend blocks.
TRACK I — INTERVIEW         8 h/wk   DSA 5.5 + system design 2.5.  DAILY. Never skipped.
TRACK F — FUNDAMENTALS      3 h/wk   named chapters, landing the week they are needed.
TRACK J — CRAFT & CAREER    2 h/wk   writing, ADRs, OSS, referrals.  One artifact per fortnight.
                                     → from Week 45:  12 D / 12 I / 8 J
```

**Your shape:** 4h on weekdays, 6h on each weekend day. Weekdays are lectures, reading, DSA and system design. **The weekend blocks are where Adyton gets built.**

> **Read this twice.** Depth without the interview track means nobody ever sees the depth — you fail the phone screen and never reach the design round. The interview track without depth gets you an L4 offer and a six-year stall. **If you only have one hour on a given day, spend it on Track I.** It is the only track that degrades irreversibly when skipped.

### The ten laws

1. **Failure first.** Every topic opens with **🔥 THE WALL** — a broken thing you reproduce. **You may not read the explanation, open the lecture, or run the prompt until the failure is on your screen.** Knowledge acquired to resolve a felt confusion is retained permanently; knowledge from a video you nodded at is gone in nine days, and interviewers hear the difference instantly.
2. **Measure everything.** A speedup you cannot attribute to a named mechanism is a coincidence. Wall time *and* the hardware counter *and* the mechanism — or it is marked "unattributed."
3. **Set the target before you measure. Record both numbers.** Every target in this document was written before any measurement existed and some are wrong. Both numbers, side by side, always. The pattern becomes `RETROSPECTIVE.md` in Week 52.
4. **Three sources, one topic.** Every topic has a *course*, a *page*, and an *AI prompt*. "I don't know where to learn this" is never a valid reason to stall.
5. **Never trust the AI on a fact you will build on.** The prompts are the fastest teacher you have and they will confidently invent APIs, misstate a paper's result, and hand you a plausible algorithm that is subtly wrong. Every AI-learned claim a design decision rests on gets verified against the course or the paper.
6. **⚙️ In C++, safety is earned every commit.** Sanitizers, fuzzers and the documented subset are not hygiene — **they are the argument for having chosen C++ at all.** A week where CI's sanitizer job is disabled is a week the language choice became indefensible.
7. **Real data, always.** The tracking study uses the real web. The AS graph is real CAIDA data. The benchmark runs against real Tor. When you must simulate, say so, and validate the simulator against the real thing.
8. **Ship publicly.** Own repo, README with an architecture diagram and a results chart in the first screen, `make demo` that works on a clean machine.
9. **Be honest about prior art and about scale.** You are never allowed to say "unsolved," "first," or "nobody has done this." **The honesty statement and the scale statement are said unprompted, every time.**
10. **The permitted headline never changes.** *No company can assemble one profile that contains all of you.* Never *"nobody can track you."* The first person who tests an overclaim dismantles it in one blog post, and then nothing else you say gets believed — including the true parts you spent a year measuring.

---
---

# PART I — THE PROJECT

## I.1 The problem, stated as a person would feel it

**Right now, a person browsing the web is assembled. Not watched — *assembled*.**

A tracker on a news site and a tracker on a shopping site share an identifier. A data broker joins those to a purchase record, a location history and a mobile advertising ID. An ISP in many jurisdictions sells the destination log legally. **No single party sees your whole life; together they construct one profile that contains all of it** — and that profile is sold, leaked, subpoenaed, and used to price things differently for you than for someone else.

The existing answers all fail differently:

| Answer | Why it fails for a normal person |
|---|---|
| **A VPN** | Moves the trust from your ISP to one company that sees everything. Single trust anchor, and an enormous commercial incentive to log |
| **Tor** | Correct, admirable, and **nearly unusable for daily life**: endless CAPTCHAs, blocked exits, banks locking accounts, logins breaking on circuit rotation, video that will not stream. The cause is structural — exit IPs are shared with abusers and **Tor cannot ban anyone**, because anonymity means no accountability |
| **iCloud Private Relay** | Architecturally right — two hops, split trust — and proof it works at consumer scale. But Safari and Apple devices only, Apple as the single trust anchor, and **no per-identity compartments**: all your browsing in one bucket |
| **Browser hardening alone** | A uniform fingerprint from a stable home IP is useless. **The IP identifies you** |

**Adyton is the missing one:** an open, cross-platform **privacy relay network with per-identity compartmentalisation**, at latency a normal person will accept.

### The product, stated exactly

**It is not "nobody knows who I am."** When you log into Amazon, Amazon knows it is you — you told them. **It is: nothing can link your identities to each other.**

Your shopping self, social self, work self and reading self get separate network paths, separate exit addresses, separate browser profiles, separate cookie jars — **bound at the operating-system level so a leak between them is structurally prevented rather than merely unlikely.** The tracker on the news site and the tracker on the shopping site see two unrelated strangers. Your ISP sees encrypted traffic to one relay and nothing else.

> ### 🔴 The one sentence you are permitted to claim
> **No company can assemble one profile that contains all of you.**

## I.2 🔴 The honesty statement — said FIRST, unprompted, every time

> Onion routing is not new and I did not invent it. **Tor has run it in production since 2003**, has millions of users, and is the right tool for anyone whose safety depends on it. **Arti**, the Tor Project's Rust implementation, is the modern rewrite. **Nym** and **Loopix** take the stronger-anonymity corner of the trade-off. **Apple's iCloud Private Relay** proves two-hop split trust works at consumer scale, and **Cloudflare** operates one of its hops. **Sphinx**, **Astoria**, **Counter-RAPTOR**, **DeNASA**, **CLAPS**, **WTF-PAD** and **Privacy Pass** are all published work that I implement rather than invent. **Mullvad Browser** — built jointly by Mullvad and the Tor Project — does the fingerprinting half, and I do not touch it.

**The gaps that are actually real, and every one is measurable:**

1. **No deployed QUIC transport for onion routing.** Papers only.
2. **No deployed AS-aware path selection.** Astoria, Counter-RAPTOR, DeNASA and CLAPS are published and **none runs anywhere.**
3. 🔴 **No open, measured guard-placement-resistant selection.** Wan et al. (PoPETs 2019) showed AS-aware selection becomes *predictable*, and **nobody has published the trade-off curve.**
4. **No open, cross-platform, low-latency relay client with per-identity compartments** bound at the OS level.
5. 🔴 **Nobody has published a current, reproducible measurement of how linkable the ordinary web actually is** — the thing the whole product exists to fix. *(This is new to this version of the plan and it is Level 2.)*

> **The sentence you are allowed to say:**
> *"Onion routing is solved and Tor does it better than I ever will. What isn't deployed anywhere is AS-aware path selection, and the reason is a 2019 result showing it makes your selector predictable. I implemented it, built the attack against my own selector, and published the trade-off curve. And before any of that I measured how linkable the web actually is, because I didn't want the premise of my own project to be something I'd read rather than something I'd checked."*

## I.3 🔴 The scale statement — the other thing you say unprompted

> **This mesh is 20–40 relays I run on one workstation, plus free-tier cloud nodes in three real regions, plus a deterministic simulator modelling up to 10,000 peers.** It has never had a stranger on it. Anything about scale beyond forty nodes is measured in simulation, and **the simulator is validated against the real mesh where both run** — `docs/analysis/sim-fidelity.md`. **A simulator you have not validated is a fantasy generator.**

## I.4 🔴 The scope decision — read this in Week 1 and never revisit it

There are two completely different projects here, and only one of them is this one.

| | What it is | Exposure |
|---|---|---|
| **(a) The research build** ← **this is what you are doing** | You build the system, run it **entirely on infrastructure you control or rent**, carry **only your own traffic and a load generator's**, and publish the implementation and the measurements | Ordinary. This is what security researchers publish at PETS and USENIX every year |
| (b) A public network | You invite strangers to run relays and route their traffic | Real legal and abuse-handling exposure, in any jurisdiction, and especially from Egypt |

> ### The decision, written in Week 1 and never re-opened:
> **Non-goal for the entire term: no public network, no invitation to strangers, no third-party traffic.** Every relay runs on infrastructure you control or rent. The only traffic on it is yours and the benchmark's. **What you publish is the implementation and the measurements.**

**This costs you nothing.** Every flagship still works: `guardplace` and `ascorr` are simulations over public topology data; `tor-bench` is you measuring your own client; `leakproof` is your own browser. **It removes the only genuinely serious risk in the plan, and it takes one paragraph in the README.**

**Week 1 task:** write `docs/scope.md` — one page, stating the above, with the sentence *"this is not legal advice"* and a note that if you ever want (b) it is a decision for after you have an offer and a jurisdiction. **Then never think about it again.**

## I.5 ⚙️ Four languages, each owning a real layer

| Language | Owns | Corpus share* | Why it, specifically |
|---|---|---|---|
| **C++20** | `adyton-core` — crypto envelope, Sphinx, per-hop QUIC, circuits, path selection, the relay daemon. **The entire data plane** | **26.0%** be+infra | Everything a hostile peer's bytes touch. A memory bug here is a remote compromise, not a crash |
| **Java 21** | `adyton-directory` (Raft, epoch documents) · `adyton-aggregate` (the telemetry plane) · `adyton-gateway`. **Everything stateful and consensus-backed** | **53.3%** — the #1 skill in your corpus | The largest measured gap in your profile, and this is where it honestly belongs |
| **Go** | `adyton-edge` — NAT traversal (`pion/ice`), SWIM gossip, the client supervisor, netns orchestration, the browser launcher, the demo server | **38.0%** | `pion` is the mature NAT stack and it is Go; supervision is what Go's runtime is for |
| **Python** | `lab/` — **the tracking study**, the AS-graph work, the attack lab, the WF classifier, benchmarks, every chart | **43.5%** | Analysis should be fast to iterate. Slow code here costs nothing |

\* Share of the 92 backend postings in your own dataset, recomputed 2026-09-14. **Rust is deliberately dropped** at 8.7% — your existing Rust HTTP server stays pinned on GitHub, so the language is still evidenced without buying a fifth.

**⚙️ The C++ dependency set — you implement none of these:** **libsodium** (X25519, ChaCha20-Poly1305, BLAKE2b, `sodium_memzero`) · **ngtcp2** + **BoringSSL** (QUIC) · **GoogleTest** · **RapidCheck** (property tests) · **libFuzzer** with a committed corpus · **CMake** + **vcpkg**.

> ### ⚙️ The C++ sentence. Memorise it, because it is the harder and better answer.
> *"This is a network daemon parsing hostile input from untrusted peers, where a memory bug is not a crash but a deanonymisation vulnerability. Rust gives you that safety by construction. I chose C++ and had to **earn** it: ASan, UBSan and TSan on every CI run, libFuzzer on every parser with a committed corpus, `std::span` instead of pointer-plus-length, no raw owning pointers in the parsing path, and a documented subset in `docs/cpp-subset.md`. Here are the three memory bugs my fuzzer found in my own code and how. That is the position almost every real systems codebase is actually in, and being the engineer who can hold that line is worth more than being the engineer who was handed it."*

🔴 **The condition, and it is not optional: the safety tooling is first-class scheduled work from Week 4.** Skip it and C++ was the wrong call, and an interviewer will find out in ten minutes.

## I.6 What is new in this version, and why

Six changes from the plan in `r2.md`. Each closes something measured or fixes something real.

| # | Change | Why |
|---|---|---|
| **1** | 🔴 **Level 2 is new: `lab/linkage`, a real measurement of how linkable the web is.** You crawl the Tranco top sites, record every third-party request and identifier, build the **tracker co-occurrence graph**, and compute what fraction of a browsing session a single tracker can reconstruct | **The project's premise becomes something you measured rather than something you read.** It lands in **Week 12** — you have a publishable artifact and a CV line three months in, instead of at month seven. It is Python (43.5%), real data, and **it is graph work**, early |
| **2** | 🔴 **The demo is a scheduled deliverable with a spec (§I.9), built at Week 26 and finalised at Week 52** | Your stated success condition is that a recruiter opens a link, sees it work, and calls. **r2 has no such page.** This one shows the *harm*, then shows it gone |
| **3** | **A telemetry plane: relays → Kafka → aggregator → Postgres, with DP noise before publication** | Closes **Kafka 20.7%** and **PostgreSQL 19.6%**, which r2 leaves open. And it is honest — the directory's relay-capacity estimates have to come from somewhere |
| **4** | 🔴 **The operational shell (Kubernetes, observability, on-call) is pulled into Year One at Level 8**, before applications open | **It is what the screen reads.** AWS 48.9%, Kubernetes 30.4%, observability 22.0%, on-call 21.5%. In r2 it sits at week 53–58, which is past the point where it can help you |
| **5** | ⭐ **The attack lab and AS-aware path selection are pulled into Year One at Level 9** | It is the research contribution **and** the graph-algorithm content, and in r2 it sits at weeks 59–76. It is the best thing in the project and it should not be in a year you might not run |
| **6** | **Every resource carries a link, and engineering-blog reading is a first-class part of every week** | r2 names resources; it does not link them, and it has almost no writing from Cloudflare, Netflix, Tailscale, AWS or Signal — which is where you learn what production actually looks like |

**And three corrections carried forward** from recomputing your dataset on 2026-09-14: the "system design is named in 76.3% of postings" figure **does not reproduce** (it is 23.9% as a skill, 32.6% as a duty — so system design stays a first-class track for loop-structure reasons, but **DSA does not drop below 300 hours**); "backend+infra n=128" is **n=200**; and the `1.0% → 58.8%` project-coverage table is **a model with no stated methodology and is not derivable from the dataset — never quote it in an interview.**

## I.7 ⚙️ The component map

| Component | Language | Appears | Purpose |
|---|---|---|---|
| `lab/bench` | Python | **W2** | The open-loop benchmark harness, with `tc netem` profiles. Used all year |
| `lab/linkage` | Python | **W9** | 🔴 **The tracking study.** Crawler, identifier extraction, the co-occurrence graph |
| `adyton-core/crypto` | **C++20** | W13 | X25519, AEAD, HKDF via libsodium; zeroizing secret types |
| `adyton-core/sphinx` | **C++20** | W15 | Constant-size onion packets, single-pass construction |
| `adyton-node` | **C++20** | W6 | The relay daemon. **Middle-only by construction** |
| `adytond` | **C++20** | W20 | Client daemon: identities, circuits, SOCKS, kill switch |
| `adyton-edge/launch` + `/cli` | Go | W21 | netns orchestration, browser launcher, `adyton identity …` |
| `adyton-demo` | Go + HTML | **W26** | 🔴 **The public linkability demonstration** |
| `adyton-core/transport` | **C++20** | W29 | Per-hop QUIC via ngtcp2 + BoringSSL; fingerprint normalisation |
| `adyton-core/circuit` | **C++20** | W31 | Circuit build, teardown, health, stream multiplexing |
| `adyton-edge/nat` | Go | W33 | NAT traversal (`pion/ice`), hole punching, relay fallback |
| `adyton-edge/gossip` | Go | W34 | SWIM membership, phi-accrual failure detection |
| `lab/meshsim` | Python + Go | W36 | Deterministic simulation of the mesh, **with a lying relay** |
| `adyton-directory` | **Java 21** | W38 | **Raft, epoch documents, hash chaining, peer admission** |
| `adyton-aggregate` | **Java 21** | **W42** | 🔴 **Kafka → aggregator → Postgres, with DP noise before publication** |
| `adyton-gateway` | **Java 21** | W45 | Public API, quotas, OpenAPI, live status |
| `lab/asgraph` | Python | **W49** | ⭐ CAIDA topology, valley-free inference, the AS adversary |
| `lab/attacks` | Python | **W50** | ⭐ Correlation, **guard placement**, sybil |

## I.8 The ten milestones

| # | Lvl | Week | What you build | The invariant you must prove |
|---|---|---|---|---|
| **D0** | 1 | **W8** | ⚙️ A relay that forwards and cannot be crashed by hostile input | Four attacks fail; **libFuzzer 1h clean with a committed corpus; ASan/UBSan/TSan green in CI** |
| **D1** | 2 | **W12** | 🔴 **The linkability study** | A reproducible crawl of ≥5,000 real sites; the co-occurrence graph; **the fraction of a session a single tracker reconstructs, with a number and a confidence interval** |
| **D2** | 3 | **W18** | Sphinx constant-size onion packets | 2-hop packet processed; **serialised size byte-identical regardless of hops remaining**, RapidCheck-asserted |
| **D3** | 4 | **W26** ★ | ★ **THE FIRST REAL THING** — one identity, end to end | Unmodified Mullvad Browser in a netns over a 2-hop circuit; **leak suite green**; two identities share no IP, DNS, cookie, TLS ticket or fingerprint difference. **And the demo page is live** |
| **D4** | 5 | **W32** | Per-hop QUIC transport | 🔴 **The head-of-line-blocking chart**; two peers' handshakes byte-identical except the random bits |
| **D5** | 6 | **W37** | The 20–40 node mesh | Discovery converges; **p50 circuit recovery <800ms, p99 <3s under 20% churn**; NAT direct-path rate measured and published |
| **D6** | 7 | **W44** | ☕ The directory + the telemetry plane | **100% of peers hold the same epoch-N consensus hash within 30s of close under 20% churn** — because disagreement is a fingerprint. Kafka→Postgres pipeline with DP noise, and the DP budget fails closed |
| **D7** | 8 | **W48** 🎯 | The operational shell | Mesh on k8s; rolling restart drops **zero** circuits; the 3am dashboard; **20+ incidents with runbooks; CV v4 and applications open** |
| **D8** | 9 | **W51** | ⭐ The attack lab | Circuit-compromise probability against a defined AS adversary, **for Adyton and for Tor**, on real CAIDA data |
| **D9** | 9 | **W52** | ⭐ **Path selection that survives its adversary** | 🔴 **The AS-diversity-versus-predictability trade-off curve, published** |

## I.9 🔴 THE DEMO — built W26, finalised W52, never cut

**Do not demo the product. Demo the harm.**

> **Screen one — you are assembled.** A visitor opens the link. Before they click anything the page shows them: their IP, their ISP, their city, their canvas/WebGL/font/audio fingerprint, and a hash of the lot. Then: **"You are `a4f9c2…`. Here is what that identifier saw."** They click through five demo sites. A graph draws itself, live, connecting every visit into one profile — **using the real tracker co-occurrence data you measured in Level 2**, so the numbers on screen are yours.
>
> **Screen two — you are not.** The same five sites, through two Adyton compartments. **The graph fails to connect.** Two unrelated strangers, side by side with the first graph, sixty seconds apart.
>
> **Screen three — and it isn't slow.** Page-load time and time-to-first-byte: direct, through Adyton, through Tor. Measured live, on their connection, in front of them. Because *"it works and it isn't slow"* is the entire claim.
>
> **Printed on the page, not buried in the README: the scale statement.**

**Why this shape:** it is ten seconds, it is emotionally legible to a recruiter's *parent*, and it demonstrates the thing rather than describing it. It needs no install and no signup. **And it is powered by your own measurement**, which means the demo and the research artifact are the same work done once.

**Guardrails:** rate-limited, quota per IP, no arbitrary destinations, and **it cannot be used as a real proxy** — it is a demonstration, and the page says so.

## I.10 Non-goals — if you are doing one of these, stop

- **Implementing QUIC, TLS or cryptographic primitives.** ngtcp2, BoringSSL, libsodium. You implement *protocols built on* primitives, never primitives.
- **Modifying Mullvad Browser.** A fork is actively harmful — every customisation makes your users distinguishable from the crowd they are hiding in. **`docs/browser-delta.md` must stay at "profile directory path and SOCKS endpoint."**
- **Open-web exits as a default.** Gateways only. Exits are opt-in, a separate build, separate operators, and not in this term.
- **A public network.** §I.4. Settled.
- **Metadata resistance against a global passive adversary.** The trilemma choice is low latency; you gave this up deliberately and you **say so** rather than hoping nobody asks.
- **Full Byzantine consensus.** You watch 6.5840's BFT lecture specifically so you can defend the lighter model.
- **A polished web frontend.** One demo page and a functional status view. No design system. Frontend is ~0% of your target postings.
- **A fifth language. A mobile app. Voice or video.**

---
---

# PART II — THE EVIDENCE BASE

Everything traces to the dataset **you** collected on 2026-08-28: **569 verified postings, 83 companies, 937 named skills.** Every figure below was **recomputed from `postings.json` on 2026-09-14**. Denominators: 554 postings carry skill data, of which **92 are backend** and **200 are backend-or-infra**.

## The degree question. Settled here. Never raised again.

| Question | Answer | Of |
|---|---|---|
| Postings requiring a PhD with no stated alternative | **6** (1.1%) | 554 |
| Postings demanding a CS degree, no alternative field, no experience route | **1** (0.18%) | 569 |
| — and that one is | **a student internship** | |
| **Backend postings stating no degree requirement at all** | **55 of 92 (59.8%)** | 92 |
| Tier-1 postings stating no degree gate | 28.1% | 146 |
| Tier-2/3 postings stating no degree gate | 56.9% | 408 |

**Three in five backend postings state no degree gate at all.** Of the rest, most carry an equivalent-experience clause. **That clause is the route, and something has to fill it.** Adyton plus CS144's eight checkpoints and 6.5840's labs is what fills it — *"I implemented TCP and it passes Stanford's test suite"* and *"my Raft passes MIT's"* are the closest things to a transcript that exist outside a university.

**Zero hours on credential anxiety. Zero hours on certifications that are not free and incidental.**

## What backend postings demand (n = 92)

| Skill | Share | | Skill | Share |
|---|---|---|---|---|
| **Java** | **53.3%** | | GCP | 21.7% |
| **AWS** | **48.9%** | | **Kafka** | **20.7%** |
| **Distributed systems** | **48.9%** | | **C++** | **19.6%** |
| Python | 43.5% | | CI/CD | 19.6% |
| Go | 38.0% | | **PostgreSQL** | **19.6%** |
| Mentoring | 37.0% | | Microservices | 19.6% |
| REST / API design | 34.8% | | Data structures | 17.4% |
| Communication | 34.8% | | **On-call** | **17.4%** |
| Scalability | 31.5% | | Docker | 17.4% |
| Collaboration | 31.2% | | Testing | 15.2% |
| **Kubernetes** | **30.4%** | | Algorithms | 14.1% |
| System design | 23.9% | | Observability | 13.0% |

**Backend + infrastructure (n = 200):** Distributed systems **57.0%** · Python 49.0% · Java 48.0% · AWS 40.5% · Go 40.0% · Kubernetes 35.5% · Scalability 34.5% · **C++ 26.0%** · CI/CD 25.0% · **Observability 22.0%** · **On-call 21.5%** · Networking 14.5% · Kafka 12.5% · Security fundamentals 3.5%

> **Distributed systems at 57.0% is the highest-frequency technical skill in your entire target corpus, and Adyton's centre of mass is exactly that skill.**

## 🔴 The split — read this twice

**The cryptographic and algorithmic core** — Sphinx, AS-aware path selection, guard-placement resistance, the linkability measurement — is the real intellectual content and it is **your forty-five-minute answer.** It is also nearly invisible to a recruiter screen. *Algorithms are named in 8.9% of the whole corpus.*

**The operational shell** — running the mesh, sharding it, observing it, deploying it, breaking it, keeping it up — is **what the screen reads.** Distributed systems 48.9%, AWS 48.9%, Kubernetes 30.4%, on-call 17.4%.

**Build the core** because it is the answer, because a degree *asserts* you can do this and you have no such assertion so a measured trade-off curve is a stronger claim *because it is checkable*, and because a year of YAML will not sustain you for twelve months.
**Build the shell** because it is what gets you read.

> **The rule: the shell is never optional and never deferred past Level 8.** If the year goes badly, cut core depth before you cut shell.

## The gaps no solo project can close

**Mentoring 37.0% · Communication 34.8% · Collaboration 31.2% · Leadership 17.2%.** Adyton demonstrates **none** of them. They come from Logic Leap, deliberately and on a schedule — Part VIII names the six situations to seek out and the stories they become. **At least four of your fourteen behavioural stories must come from the job you were paid to do.**

---
---

# PART III — THE TERM AT A GLANCE

| Lvl | Name | Weeks | Dates | Milestone | Course running | Flagship |
|---|---|---|---|---|---|---|
| **0** | Foundations & the Measurement | W1–3 | 14 Sep – 4 Oct 26 | — | 15-213 §6 | `latency-lab`, `sickbay` |
| **1** | ⚙️ C++, Sanitizers & the Threat | W4–8 | 5 Oct – 8 Nov 26 | **D0** | 15-213 ch.5 | 🚩 **#1 `hardened`** |
| **2** | 🔴 The Problem, Measured | W9–12 | 9 Nov – 6 Dec 26 | **D1** | — | 🚩 **#2 `linkage`** |
| **3** | Onion Routing & Sphinx | W13–18 | 7 Dec – 17 Jan 27 | **D2** | **Boneh Crypto I** | 🚩 **#3 `sphinx`** |
| **4** | ★ Compartments | W19–26 | 18 Jan – 14 Mar 27 | **D3** ★ | 6.858 (sel.) 🌙 | 🚩 **#4 `leakproof`** · ★ **the demo** |
| **5** | Transport: QUIC & Fingerprints | W27–32 | 15 Mar – 25 Apr 27 | **D4** | **CS144, all 8 checkpoints** | 🚩 **#5 `minnow`** |
| **6** | The Mesh: NAT & Gossip | W33–37 | 26 Apr – 30 May 27 | **D5** | — | 🚩 **#6 `meshsim`** |
| **7** | ☕ The Directory & Telemetry | W38–44 | 31 May – 18 Jul 27 | **D6** | **6.5840, Labs 1–3** | 🚩 **#7 `raft-dir`** |
| **8** | Operations & the Shell 🎯 | W45–48 | 19 Jul – 15 Aug 27 | **D7** | — | 🚩 **#8 `incident-lab`** · 🎯 **APPLY** |
| **9** | ⭐ The Attack Lab & Path Selection | W49–52 | 16 Aug – 12 Sep 27 | **D8, D9** | — | 🚩 **#9 `ascorr`**, 🚩 **#10 `guardplace`** |

**Rest weeks: 12, 26, 37, 48** (10h, no new scope). **Buffer weeks: 18, 32, 44.**
**🌙 Ramadan 1448 ≈ 8 Feb – 9 Mar 2027 = weeks 22–26, at 20h** — landing deliberately on the leak suite, which is many small independent tests and is the right shape of work for a reduced month. **Eid al-Adha ≈ 17 May = week 36, at 26h.**

**Budget:** 52 × 32 = 1,664 nominal. −88 (four rest weeks at 10h) −48 (Ramadan W23–26 at 20h) −6 (Eid W36 at 26h) = **≈1,522 effective hours.**

| Track | Hours | Share |
|---|---|---|
| Depth — courses + Adyton + flagships | ~870 | 57% |
| Interview — DSA ~300h + system design ~150h | ~450 | 30% |
| Fundamentals | ~130 | 9% |
| Craft & career | ~150 | 10% |
---
---

---
---

# PART IV — THE FACULTY

> **Verified 14 September 2026.** Course materials move, get renumbered and disappear behind logins. Everything below was checked on that date, and **where something changed since the last generation of these roadmaps, the correction is stated loudly** — a curriculum that sends you to a 404 in Week 27 is worse than no curriculum.
>
> **Three tiers.** **§IV.2 — the six you complete.** **§IV.3 — the ones you consult and never finish.** **§IV.4 — the full elective directory**, so you always know what exists, what it would cost, and whether it is worth your year.

## 🚨 IV.1 — Five corrections to read before you plan anything

| # | The correction | What to do about it |
|---|---|---|
| **1** | 🔴 **Stanford CS144's site and starter repo are OFFLINE right now.** [↗ cs144.github.io](https://cs144.github.io/) → 404, [↗ github.com/CS144/minnow](https://github.com/CS144/minnow) → 404, the GitHub org has zero public repos. Snapshots were healthy through **6 May 2026**, failing by **25 Aug 2026** | The repo "clears annually" and **Fall 2026 starts in late September** — expect it back within weeks. **Week 1 task: check weekly, and mirror it to a private fork the day it returns.** Level 5 is Week 27; you have time, but do not discover this in Week 26. Fallbacks in §IV.2 |
| **2** | 🔴 **MIT 6.5840's labs were renumbered.** What older guides call "Lab 2 Raft / Lab 3 KV / Lab 4 Sharded" is now **Lab 3 / 4 / 5**, with a new **Lab 2** (single-machine KV + lock) inserted | **"Labs 1–3" in this document means MapReduce → KV server → Raft**, the correct current numbering |
| **3** | 🔴 **MIT 6.1810's `thread` and `lazy` labs no longer exist, and `util` changed entirely.** Current `util`: **sleep (via a `pause` syscall), sixfive, memdump, find, exec** | Old solution repos will not match the grader. Not on your critical path, but do not budget for a deleted lab |
| **4** | 🔴 **CMU 15-445: use Fall 2025, not Fall 2026.** The F26 FAQ says verbatim that recordings are CMU-only and *"Non-CMU students should watch the Fall 2025 lectures on YouTube"* | Use the F25 site and playlist. Also: **Project 1 is now Adaptive Replacement Cache, not LRU-K**, and **Project 0 is a Count-Min Sketch** |
| **5** | 🔴 **Boneh's Cryptography II was never released and is not coming.** [↗ coursera.org/learn/crypto2](https://www.coursera.org/learn/crypto2) → 404, verified | Do not build a plan around it. The successor material is in Parts II–III of the free Boneh–Shoup book, and **CS255 is the real Stanford course** |

> ✅ **And one thing better than expected:** **CMU 15-445 runs a public Gradescope for non-CMU students** — entry code **`5R4XPZ`**, school "Carnegie Mellon University", auto-graders released after each CMU deadline. **A genuine external grade you can put on a CV.**

---

## 📚 IV.2 — THE SIX YOU COMPLETE

> **The pricing insight that makes ~340 course-hours fit inside a 52-week plan: two of these courses' labs *are* the product.** The TCP you write in CS144 becomes Adyton's transport reference. The Raft you write in 6.5840 becomes its directory. **Those hours are counted once, not twice.**

### 📺 1 · Stanford CS144 — *Introduction to Computer Networking*
**Level 5 · W27–32 · ~90h · the single most relevant course to this project**

> **What you build:** a **working TCP implementation in C++**, from the byte stream up — a reassembler, a receiver, a sender with retransmission, a full connection state machine, then ARP and an IP router underneath it.
> **What it buys you:** the most unfakeable claim you will own. *"I implemented TCP and it passes Stanford's test suite."*

| | |
|---|---|
| **Site** | [↗ cs144.github.io](https://cs144.github.io/) 🚨 **404 as of 14 Sep 2026 — see §IV.1** |
| **Archive that works today** | [↗ web.archive.org — CS144 May 2026](https://web.archive.org/web/20260506063931/https://cs144.github.io/) |
| **Live mirrors** | [↗ ht4w5/minnow-winter-2025](https://github.com/ht4w5/minnow-winter-2025) (clean starter, ckpt-0 slice) · [↗ MuhammadWaleed-Animations/minnow-Stanford](https://github.com/MuhammadWaleed-Animations/minnow-Stanford) |
| **Video** | ⚠️ Not officially public. The watchable corpus is the older MOOC: [↗ YouTube — CS144, 145 videos](https://www.youtube.com/playlist?list=PL6RdenZrxrw9inR-IJv-erlOKRHjymxMN) *(third-party re-upload — **mirror what you need**)* · semi-official, routing only: [↗ Nick McKeown's channel](https://www.youtube.com/playlist?list=PLTQzEwN6b5LUL85DCttO9z_-BOQTApyvZ) |
| **Textbook** | **None.** *"We will not be assigning readings."* Optional and free: [↗ book.systemsapproach.org](https://book.systemsapproach.org/) |
| **Time** | Official: *"about 70 hours total on the lab."* Self-study estimate ~100h |

| # | Checkpoint | Target | You build |
|---|---|---|---|
| **0** | networking warmup | `check0` | Telnet + SMTP by hand · `webget` · an in-memory `ByteStream`. *2–6 hours* |
| **1** | stitching substrings into a byte stream | `check1` | 🔴 **The `Reassembler` — an interval-merge problem.** Do LC 56/57/435/253 the same week |
| **2** | the TCP receiver | `check2` | `Wrap32` seqno translation + `TCPReceiver` |
| **3** | the TCP sender | `check3` | 🔴 **`TCPSender` + the retransmission timer — RFC 6298, implemented** |
| **4** | measuring the real world | *report* | ≥3 Internet paths, **≥1 hour of `ping -D -n -i 0.2`.** 🔴 *Feed it straight into `lab/bench`* |
| **5** | the network interface | `check5` | `NetworkInterface` + ARP with 30s expiry |
| **6** | building an IP router | `check6` | `Router`, longest-prefix match |
| **7** | making an Internet | — | ✂️ **Needs classmates. Cut it** |

```bash
cmake -S . -B build && cmake --build build
cmake --build build --target check0   # then check1 check2 check3 check5 check6
cmake --build build --target speed    # throughput benchmarks
export TEST_ONLY="write, close, read" # a single named test
```
**Past exams with answers were public** (`21fa-midterm`, `sp23_final`) — **grab them from the Wayback snapshot while you are in there.**

### 📺 2 · MIT 6.5840 — *Distributed Systems*
**Level 7 · W38–44 · ~90h · Labs 1, 2 and 3**

> **What you build:** MapReduce, a **linearizable key/value server with at-most-once RPC and a distributed lock**, and **Raft in full** — elections, log replication, persistence, snapshots. In Go.
> **What it buys you:** *"My Raft passes MIT's test suite, including `TestFigure8Unreliable`."* **Distributed systems is 48.9% of your backend postings — the highest-frequency technical skill in your corpus.**

| | |
|---|---|
| **Site** | [↗ pdos.csail.mit.edu/6.824](https://pdos.csail.mit.edu/6.824/) — live, Spring 2026, fully public |
| **Video** | ⚠️ **Spring 2020 only** — [↗ YouTube — 6.824 Spring 2020, 20 lectures](https://www.youtube.com/playlist?list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB). **No 2021–26 video exists anywhere.** The `.txt` notes are unusually complete and are your substitute |
| **Labs** | `git clone git://g.csail.mit.edu/6.5840-golabs-2026` 🔴 **`git://` only — the https variant fails on a cert-name mismatch and some networks block port 9418. Test this in Week 1, not Week 38** |

| Lab | Parts (MIT's own difficulty tags) |
|---|---|
| **1 · MapReduce** | one part — *moderate/hard*. Crash-recoverable, 10s timeout |
| **2 · Key/Value Server** | reliable net (*easy*) · **a lock via the clerk** (*moderate*) · **dropped messages** (*moderate*). 🔴 *Versioned put, at-most-once, linearizable — exactly your directory's semantics* |
| **3 · Raft** | **3A** elections (*moderate*) · **3B** log (*hard*) · **3C** persistence (*hard*) · **3D** snapshots (*hard*) |

```bash
cd src
make mr ; make kvsrv1 ; make lock1
make RUN="-run 3A" raft1     # then 3B 3C 3D
```
> ⚠️ **Older roadmaps budget "2–3 weeks" for all the labs. That is wrong by ~4×. Lab 3 alone defeats most people on the first attempt.** Budget seven weeks, expect to rewrite your Raft once, and expect `TestFigure8Unreliable` to humble you.

**The papers, by lecture** — all on the site: MapReduce · GFS · Paxos Made Simple · **Raft extended** · Herlihy & Wing *Linearizability* · ZooKeeper · Spanner · Chain Replication · FaRM · IronFleet · Memcached at Facebook · **On-demand Container Loading** *(guest lecture: Marc Brooker)* · Ray · 🔴 **SUNDR — fork consistency, which matters to you unusually much** · Bitcoin · **Practical BFT**.
🔴 **Watch the BFT lecture specifically**, so you can defend Adyton's crash-recovery failure model instead of hand-waving past it.

### 📺 3 · Dan Boneh — *Cryptography* · **two courses, use both**
**Level 3 · W13–18 · ~40h**

> **What you build:** correct compositions of AEAD, key exchange and MACs — and, via CS255's projects, **authenticated encryption, MACs, and key-exchange protocols implemented by hand.**
> **What it buys you:** the ability to read the Sphinx paper and implement it **without inventing anything.**

| | |
|---|---|
| 🔴 **The free lectures** | [↗ crypto.stanford.edu — OnlineCrypto](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/) — **all videos and slides, free, no account.** Use this, not Coursera |
| 🔴 **The real Stanford course** | [↗ crypto.stanford.edu/cs255](https://crypto.stanford.edu/cs255/) — **CS255 has the programming projects the online version gates.** Problem sets and project specs public |
| **Coursera** *(optional)* | [↗ coursera.org/learn/crypto](https://www.coursera.org/learn/crypto) — homeworks and the final exam live here |
| **Free textbook** | [↗ Boneh & Shoup, *A Graduate Course in Applied Cryptography*](https://crypto.stanford.edu/~dabo/cryptobook/) · [↗ PDF v0.5](https://crypto.stanford.edu/~dabo/cryptobook/BonehShoup_0_5.pdf) |
| **Self-check** | [↗ AxlLind/coursera-cryptography-I](https://github.com/AxlLind/coursera-cryptography-I) — reference solutions, all six programming assignments |

**Weeks 1–5, and week 4 is the one that matters:** stream ciphers and semantic security → block ciphers, AES, **CTR mode** *(your onion layers are CTR-shaped)* → MACs, HMAC, **timing attacks on MAC verification** → 🔴 **authenticated encryption, chosen-ciphertext attacks, CBC padding attacks, key derivation, TLS 1.2 as a case study** → Diffie–Hellman and X25519.

**Paired with:** [↗ cryptopals.com](https://cryptopals.com/) **sets 1–2** — 🔴 *you break padding oracles, CBC bit-flipping and nonce reuse **by hand**, and nothing teaches implementation pitfalls faster.*

### 📺 4 · 🔴 RPISEC — *Modern Binary Exploitation* · **NEW to this plan**
**Level 1 · W7–8 · ~25h**

> **What you build:** the other side of your own parser. **Stack smashing, shellcode, Return-Oriented Programming, format-string bugs, heap exploitation against glibc's allocator, and ASLR/DEP bypasses** — against pre-built target binaries in a supplied VM.
> 🔴 **Why it belongs in a privacy-relay curriculum, and why I added it:** you are writing a **C++ parser for bytes sent by people who want you dead.** Reading about memory safety produces a fact. **Spending two weeks *exploiting* a vulnerable parser produces an instinct** — and it turns your Level-1 fuzzing work from hygiene into something you understand from both ends. It is the **Adversary archetype applied to your own code**, and it is the cheapest credibility in this whole document.

| | |
|---|---|
| **Everything** | [↗ github.com/RPISEC/MBE](https://github.com/RPISEC/MBE) — slides, labs, **pre-built VM images**, and the target binaries |
| **Format** | Self-contained. Lecture slides + graduated challenge binaries, easy → hard |

**Pairs with:** CS:APP's **[↗ Attack Lab](http://csapp.cs.cmu.edu/3e/target1.tar)** and **[↗ Bomb Lab](http://csapp.cs.cmu.edu/3e/bomb.tar)** *(the self-study bomb has the grading-server notification disabled — explode it freely)*.

### 📺 5 · UC Berkeley CS 161 — *Computer Security*
**Levels 1, 3, 4, 9 · threaded through the year · ~40h**

> 🔴 **A deliberate substitution.** MIT 6.858 was the assigned security course in earlier drafts; its recent lectures are behind an MIT login. **CS161 has full public video, a free textbook, and public projects — and its final unit is anonymity and Tor.** For self-study it is simply the better instrument.

| | |
|---|---|
| **Site** | [↗ fa25.cs161.org](https://fa25.cs161.org/) *(complete)* · [↗ fa26.cs161.org](https://fa26.cs161.org/) *(running)* |
| **Video** | ✅ **Fully public** — [↗ youtube.com/@berkeley-cs161](https://www.youtube.com/@berkeley-cs161) |
| **Free textbook** | ✅ [↗ textbook.cs161.org](https://textbook.cs161.org) — 39 chapters, CC BY-SA |
| **Projects** | Memory safety · cryptography implementation · exploitation and access control. Plus HW1–7 |

**The chapters, and when:** **L1** *Security Principles* · *x86 Assembly and the Call Stack* · **Memory Safety Vulnerabilities** · **Mitigating Memory-Safety Vulnerabilities** — 🔴 *read the same week you wire the sanitizers, and Project 1 is your Level-1 warm-up alongside MBE* · **L3** *Symmetric-Key Crypto* · *Hashes* · *MACs* · *Diffie–Hellman* — the gentler companion to Boneh · **L4** 🔴 *Introduction to the Web* · **Same-Origin Policy** · **Cookies and Session Management** · *CSRF* · *XSS* — **exactly the browser-side model your compartments defend** · **L9** 🔴 **the *Anonymity / Tor* chapters — read last, when you have built the thing.**

### 📺 6 · CS:APP / CMU 15-213 — *Introduction to Computer Systems* · **Proxy Lab**
**Levels 0, 1, 8 · ~25h**

> ⚠️ **No public lecture video for any recent offering** — the Fall 2025 site says videos were delayed by *"legal issues."* Treat it as **slides + textbook + labs.**
> **Slides:** [↗ 15-213 Fall 2025 lecture PDFs](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f25/www/lectures/) — you want *The Memory Hierarchy*, *Cache Memories*, *Code Optimization*, *Concurrent Programming*, *Synchronization*.
> **Book:** CS:APP 3e — **§6.2–6.4** (Week 1) and **ch. 5** (Level 8).

> 🔴 **THE ONE LAB YOU ACTUALLY DO: Proxy Lab.** [↗ writeup](http://csapp.cs.cmu.edu/3e/proxylab.pdf) · [↗ handout (133 KB)](http://csapp.cs.cmu.edu/3e/proxylab-handout.tar)
>
> **What you build:** a **concurrent caching HTTP proxy** — parse the request, open a connection to the origin, forward, cache the response, evict by approximate LRU.
> **Why it belongs here:** it is a proxy, with concurrency, with a real synchronisation constraint — and **Part III's writeup explicitly forbids the easy answer: *"protecting accesses to the cache with one large exclusive lock is not an acceptable solution."*** You partition, or use readers–writers locks, or build it from semaphores. **Auto-graded offline via the bundled `driver.sh` (BasicCorrectness 40 / Concurrency 15 / Cache 15), in a single week.**

---

## 📖 IV.3 — CONSULTED, NEVER FINISHED

| Course | Use it for | Links |
|---|---|---|
| **MIT 6.858 — Computer Systems Security** | 🔴 **Lecture 20 is literally *Anonymous Communication***: the Tor 2004 paper plus the Tor blog's *"Top changes since the 2004 design paper."* **Read in Level 9.** Labs are public and self-gradeable | [↗ Spring 2026](https://css.csail.mit.edu/6.5660/2026/) ⚠️ *root URLs redirect to a stale 2023* · [↗ 2020 video set](https://css.csail.mit.edu/6.858/2020/) · [↗ OCW Fall 2014, 23 videos](https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/) · [↗ VM image 2.55GB](https://web.mit.edu/6.858/2026/6.566-standalone-v26.zip) |
| **MIT 6.1810 — OS Engineering (xv6)** | **Notes only, no labs** — page tables, traps, namespaces, and 🔴 `l-shenango.txt` on high-performance networking. So that when you build netns you know what the kernel is doing | [↗ Fall 2025](https://pdos.csail.mit.edu/6.1810/2025/) · [↗ xv6 book, free](https://mit-pdos.github.io/xv6-riscv-book/) · [↗ Fall 2020 video](https://pdos.csail.mit.edu/6.S081/2020/schedule.html) |
| **CMU 15-445 — Database Systems** | Optional. The **logging and recovery** lectures — your epoch store is a WAL and recovery is ARIES's problem | [↗ Fall 2025](https://15445.courses.cs.cmu.edu/fall2025/) · [↗ playlist, 25 videos](https://www.youtube.com/playlist?list=PLSE8ODhjZXjYMAgsGH-GtY5rJYZ6zjsd5) · [↗ bustub](https://github.com/cmu-db/bustub) · **public Gradescope `5R4XPZ`** |
| **MIT 6.172 — Performance Engineering** | 🔴 **Level 8.** The cache-efficiency, vectorisation and profiling lectures, for the data plane. Leiserson's course, full OCW video | [↗ OCW Fall 2018](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/) |
| **UIUC 598HPN — High-speed Networks** | 🔴 Three lectures: *Host network stack overheads*, *TAS*, *XDP*. Read the week you profile the data plane | [↗ Fall 2023, slides public](https://courses.grainger.illinois.edu/ece598hpn/fa2023/) |
| **Stanford CS244 — Reproducing Network Research** | 🔴 **A decade of student projects reproducing networking papers on Mininet — a ready-made menu of weekend experiments**, including BBR and QUIC | [↗ reproducingnetworkresearch](https://reproducingnetworkresearch.wordpress.com/) |
| **Stanford CS155 — Computer & Network Security** | 🔴 **Lecture 17 is *Privacy, Anonymity & Censorship*.** Slides and all three project handouts public | [↗ cs155.stanford.edu](https://cs155.stanford.edu/) · [↗ archive with VMs](https://crypto.stanford.edu/cs155old/cs155-spring17/) |

---

## 🗂 IV.4 — THE ELECTIVE DIRECTORY

> **Every serious, free, complete systems course worth knowing about — with what you build, and an honest verdict on whether it earns your year.**
>
> **You will not take these.** They are here so that when you hit a gap, you know exactly where to go — and so that in month nine, when you want a different problem for a weekend, you have a menu instead of a search engine.
>
> **Verdict key:** 🟢 **in this plan** · 🟡 **worth a weekend or a gap** · 🔵 **excellent, wrong year** · ⚪️ **great course, not your field**

### Performance engineering & parallelism
| Course | What you build | Verdict |
|---|---|---|
| **[↗ MIT 6.172 — Performance Engineering](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/)** (Leiserson) | Optimise matrix multiply, write custom allocators, AVX/SIMD vectorisation, a multi-threaded chess engine in Cilk. **24 video lectures + profiling labs** | 🟢 **Selected lectures, Level 8.** The best performance course that exists, and it is exactly "made it disappear" |
| **[↗ Stanford CS149 — Parallel Computing](https://gfxcourses.stanford.edu/cs149/)** | OpenMP schedulers, multi-threaded ray tracers, CUDA shaders, lock-free distributed shared memory | 🔵 Superb. **Wrong year** — Adyton is I/O-bound, not compute-bound |
| **[↗ CMU 15-418 — Parallel Architecture](https://www.cs.cmu.edu/~418/)** | Work-stealing runtimes, SIMD analysers, MPI cluster pipelines | 🔵 Overlaps CS149. Pick one, later |

### Operating systems & kernel
| Course | What you build | Verdict |
|---|---|---|
| **[↗ MIT 6.1810 — xv6](https://pdos.csail.mit.edu/6.828/)** | System calls, page tables, copy-on-write fork, crash-safe logging FS, a network driver. **Public autograders** | 🟡 **Notes in this plan; labs are 150h.** Do `pgtbl` and `net` in a gap if you want them |
| **[↗ CMU 15-410 — OS Design & Implementation](https://www.cs.cmu.edu/~410/)** | 🔴 **An entire multitasking kernel from scratch in C** — a thread library from assembly up, virtual memory, preemptive scheduling, IPC, device drivers | 🔵 **The hardest OS course in existence.** Genuinely transformative, and a whole semester. `NEXT.md` |
| **[↗ Berkeley CS162 — Operating Systems](https://cs162.org/)** | Pintos: user programs, synchronisation, **priority donation**, virtual memory, hierarchical filesystems | 🔵 Gentler than 15-410, still a full course |
| **[↗ UW CSE 333 — Systems Programming](https://courses.cs.washington.edu/courses/cse333/)** | An in-memory search engine and indexing file server in **modern C++ and POSIX sockets**, with Valgrind rubrics | 🟡 **The best "get fluent in C++ and sockets fast" course here.** If Level 1 exposes shaky C++, spend two weeks here |

### Distributed systems
| Course | What you build | Verdict |
|---|---|---|
| **[↗ MIT 6.5840](https://pdos.csail.mit.edu/6.824/)** | MapReduce, Raft, sharded fault-tolerant KV. Go | 🟢 **Level 7** |
| **[↗ UW CSE 452 — Distributed Systems](https://courses.cs.washington.edu/courses/cse452/)** | 🔴 **DSLabs in Java:** linearizable KV stores, primary-backup replication, **multi-Paxos**, atomic transactions — **with a network-partition simulator in the test harness** | 🟡 **The strongest elective on this whole page for you.** It is **Java** (53.3%, your largest gap) **and** distributed systems **and** it teaches Paxos, which 6.5840 does not implement. **If you take one elective, take this one** |
| **[↗ Princeton COS 418](https://www.cs.princeton.edu/courses/archive/fall20/cos418/)** | MapReduce, Raft, distributed transactional KV. Go | ⚪️ Cleanly built, but it is 6.5840's territory |

### Databases & storage
| Course | What you build | Verdict |
|---|---|---|
| **[↗ CMU 15-445](https://15445.courses.cs.cmu.edu/)** | BusTub in C++: buffer pool, B+Tree, Volcano execution, MVCC. **4K video, public Gradescope** | 🟡 **§IV.3.** Do the recovery lectures; do the projects only if storage grabs you |
| **[↗ Berkeley CS186](https://cs186berkeley.net/)** | RookieDB: B+Tree, buffer management, joins, query optimisation, **ARIES recovery** | 🟡 Java. **The ARIES project is the single best WAL-recovery exercise available** |
| **[↗ MIT 6.830 — SimpleDB](https://ocw.mit.edu/courses/6-830-database-systems-fall-2014/)** | A database bottom to top in Java: tuples, heap files, buffer pool, B+Trees, optimiser, lock manager, two-phase locking | 🔵 Older, but the skeleton is clean and complete |
| **[↗ CMU 15-721 — Advanced Databases](https://15721.courses.cs.cmu.edu/)** | Columnar storage, vectorised execution, **JIT query compilation with LLVM** | 🔵 `NEXT.md`. Spectacular, and not this year |

### Compilers & program analysis
| Course | What you build | Verdict |
|---|---|---|
| **[↗ Cornell CS 6120 — Advanced Compilers](https://www.cs.cornell.edu/courses/cs6120/)** | Dataflow analysis, **SSA construction**, global value numbering, loop-invariant code motion over the Bril IR. Video + open tests | ⚪️ Self-paced and excellent. Not your field this year |
| **[↗ Stanford CS143 — Compilers](https://web.stanford.edu/class/cs143/)** | A complete compiler for Cool: lexer, parser, type checker, MIPS/LLVM codegen | ⚪️ The classic |
| **[↗ CMU 15-411 — Compiler Design](https://www.cs.cmu.edu/~fp/courses/15411-f14/)** | An **optimising** compiler for C0 → x86-64, **register allocation by graph colouring**, garbage collection | ⚪️ Brutal and wonderful |
| **[↗ Cornell CS 3110 — Functional Programming](https://cs3110.github.io/textbook/)** | Lexers, AST evaluators, DSL interpreters in OCaml. **Free interactive textbook** | 🟡 The fastest route to thinking in types, if your Rust/C++ ownership intuition ever stalls |

### Architecture & hardware
| Course | What you build | Verdict |
|---|---|---|
| **[↗ Berkeley CS61C](https://cs61c.org/)** | RISC-V disassemblers, **a pipelined CPU in Logisim**, cache emulators, OpenMP acceleration | 🟡 If CS:APP's memory-hierarchy material ever feels like magic, this is the fix |
| **[↗ MIT 6.004 — Computation Structures](https://computationstructures.org/)** | A processor from CMOS gates up: ALU, register file, pipeline, interrupts. Browser-based simulator, autograded | ⚪️ Beautiful, and below your abstraction |
| **[↗ Stanford CS107](https://web.stanford.edu/class/cs107/)** | Generics in C, integer-representation exploits, **your own `malloc`/`free`**, x86-64 disassembly tools | 🟡 **The heap allocator project is the best single exercise for understanding what your arena allocator is avoiding** |

### Verification, testing & software design
| Course | What you build | Verdict |
|---|---|---|
| **[↗ CMU 15-414 — Bug Catching](https://www.cs.cmu.edu/~15414/)** | 🔴 **SAT/SMT solvers, dynamic symbolic execution engines, deductive verification with Why3** | 🟡 **The strongest alternative to the TLA+ block in Level 7.** If model checking grabs you, this is where to go deeper |
| **[↗ UPenn CIS 500 — Software Foundations](https://softwarefoundations.cis.upenn.edu/)** (Pierce) | Machine-checked proofs of program properties in **Coq**. Five complete free books with executable exercises | 🔵 A different way of thinking about correctness. `NEXT.md` |
| **[↗ Brown CSCI 0320 — Software Engineering](https://cs0320.github.io/)** | Multi-tier applications with **dependency injection, fuzz testing, mocks, API proxy layers, concurrency control** | ⚪️ Good course; you already do this at work |
| **[↗ UW CSE 331 — Software Design](https://courses.cs.washington.edu/courses/cse331/)** | Java with **formal invariants and Hoare logic**, graph pathfinding, modular GUIs | 🟡 The *invariants* material is genuinely useful for how you write exit criteria |

### Security & exploitation
| Course | What you build | Verdict |
|---|---|---|
| **[↗ RPISEC — Modern Binary Exploitation](https://github.com/RPISEC/MBE)** | Stack smashing, shellcode, **ROP**, format strings, heap exploitation, ASLR/DEP bypass. **VM + target binaries included** | 🟢 **Level 1, W7–8.** See §IV.2.4 |
| **[↗ Berkeley CS161](https://cs161.org/)** | Buffer overflows, control-flow hijack, **an end-to-end encrypted file-sharing system**, XSS, SQLi | 🟢 **Threaded through the year** |
| **[↗ MIT 6.858](https://css.csail.mit.edu/6.858/)** | Privilege separation, **seccomp/capabilities sandboxing**, side channels, secure authentication | 🟡 **§IV.3.** Lecture 20 is required reading in Level 9 |
| **[↗ Stanford CS255 — Cryptography](https://crypto.stanford.edu/cs255/)** | Authenticated encryption, MACs, PKI, **zero-knowledge primitives**, RSA/ECC key exchange. Projects + video | 🟢 **Level 3**, alongside the online lectures |

### Foundations, if a gap ever appears
**[↗ Berkeley CS61A](https://cs61a.org/)** — a **Scheme interpreter in Python**, superb autograders ⚪️ · **[↗ Berkeley CS61B](https://sp21.datastructur.es/)** — 🔴 **Gitlet: a working clone of Git in Java**, with trees, commits, branching, merging and SHA-1. 🟡 *The single best data-structures project in existence, and it is Java* · **[↗ MIT 6.046 — Algorithms](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)** — divide and conquer, DP, **network flows**, amortised analysis, NP-hardness reductions. 🟡 **The theory spine behind Track I's W38 reductions week**

---

## 🧭 IV.5 — SPECIALISATION TRACKS

**If you ever change direction**, these are the end-to-end sequences. The first is the one this document runs.

```
▸ PRIVACY & NETWORK INFRASTRUCTURE          ← THIS PLAN
  CS:APP §6 ─► RPISEC MBE ─► Boneh/CS255 ─► CS144 ─► 6.5840 ─► CS161 anonymity ─► 6.858 L20

▸ LOW-LEVEL INFRASTRUCTURE & CLOUD
  CS:APP ─► 6.1810 (xv6) ─► CS144 (TCP) ─► 6.5840 (Raft) ─► 15-445 (BusTub)

▸ HIGH-PERFORMANCE SYSTEMS & COMPILERS
  CS61C ─► 6.172 (Perf) ─► CS149 (Parallel/CUDA) ─► CS 6120 (Compilers)

▸ SECURITY & EXPLOIT ENGINEERING
  CS:APP ─► RPISEC MBE ─► CS161 ─► 6.858 ─► CS255

▸ HIGH-RELIABILITY & VERIFICATION
  CS61B ─► CS 3110 ─► CSE 331 ─► 15-414 (Bug Catching) ─► CIS 500 (Coq)
```

## 📋 IV.6 — The atlas at a glance

| Course | Level | Weeks | Hours | You complete | Video |
|---|---|---|---|---|---|
| **CS:APP / 15-213** | L0, L1, L8 | W1–2, W7, W40 | 25 | §6.2–6.4, ch. 5, **Proxy Lab**, Bomb Lab | ❌ slides only |
| 🔴 **RPISEC MBE** | **L1** | **W7–8** | **25** | **The exploitation ladder** | ❌ slides + VM |
| **Berkeley CS161** | L1, L3, L4, L9 | threaded | 40 | Memory-safety, web, **anonymity** chapters + Project 1 | ✅ **full public** |
| **Boneh + CS255** | L3 | W13–18 | 40 | **Weeks 1–5** + Cryptopals 1–2 + CS255 projects | ✅ free |
| 🔴 **Stanford CS144** | **L5** | **W27–32** | **90** | **Checkpoints 0–6** | ⚠️ mirror |
| 🔴 **MIT 6.5840** | **L7** | **W38–44** | **90** | **Labs 1, 2, 3** | ⚠️ 2020 only |
| MIT 6.858 | L4, L9 | W22, W50 | 15 | Selected, esp. **L20** | ✅ 2020 / 2014 |
| MIT 6.1810 | L4 | W20 | 10 | Notes only | ✅ 2020 only |
| MIT 6.172 | L8 | W40 | 10 | Selected lectures | ✅ OCW |
| | | | **~345** | | |
# PART V — THE DEPARTMENTS

> **The library, organised the way a college is: by department.** Every item carries a link that was verified on 14 September 2026 and a line saying why it earns your time. **Nothing here is "further reading."** If it is listed, it is assigned somewhere in Part VI, and Part VI tells you which week.
>
> **Three of these sections are marked ⛓ THE SPINE.** Those are not reading lists — they are arguments that ran for a decade, with a reversal in the middle, and you read them **in order**. Following an argument is a different and better education than reading twenty papers.

## V.A ⚙️ DEPARTMENT OF SYSTEMS, C++ & CORRECTNESS

> **The department that makes the C++ choice defensible.** Everything here is scheduled work from Week 4, not hygiene you get to later. A week where CI's sanitizer job is disabled is a week the language choice became indefensible — and an interviewer will find out in ten minutes.

### Sanitizers — wire all of these in Week 4, not later

| Resource | Link |
|---|---|
| **AddressSanitizer** — heap/stack/global overflow, use-after-free, ~2× slowdown | [↗ clang.llvm.org/docs](https://clang.llvm.org/docs/AddressSanitizer.html) |
| **UndefinedBehaviorSanitizer** — signed overflow, misaligned loads, invalid shifts. **Exactly the bugs hostile input triggers in a parser** | [↗ clang.llvm.org/docs](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html) |
| **ThreadSanitizer** — data races; essential once the relay runs an async event loop | [↗ clang.llvm.org/docs](https://clang.llvm.org/docs/ThreadSanitizer.html) |
| **MemorySanitizer** — uninitialised reads. 🔴 **Catches the info-leak class ASan cannot see, which for you is a deanonymisation class** | [↗ clang.llvm.org/docs](https://clang.llvm.org/docs/MemorySanitizer.html) |
| **LeakSanitizer** — near-zero cost bundled with ASan | [↗ clang.llvm.org/docs](https://clang.llvm.org/docs/LeakSanitizer.html) |
| **SanitizerCoverage** — the instrumentation that makes coverage-guided fuzzing work. **Read before writing fuzz targets** | [↗ clang.llvm.org/docs](https://clang.llvm.org/docs/SanitizerCoverage.html) |
| **google/sanitizers wiki** — the practical companion: limitations, suppression files, CI recipes | [↗ github.com/google](https://github.com/google/sanitizers/wiki) |
| **`ASAN_OPTIONS` reference** — `detect_stack_use_after_return`, `halt_on_error` | [↗ github.com/google](https://github.com/google/sanitizers/wiki/AddressSanitizerFlags) |
| **Common sanitizer flags** — symbolization and log routing for CI | [↗ github.com/google](https://github.com/google/sanitizers/wiki/SanitizerCommonFlags) |
| **Valgrind quick start** — slower than ASan, catches different bugs, needs no recompile. Worth one session | [↗ valgrind.org/docs](https://valgrind.org/docs/manual/quick-start.html) |

### Fuzzing — the flagship apparatus

| Resource | Link |
|---|---|
| **libFuzzer** — the canonical reference for in-process coverage-guided fuzzing | [↗ llvm.org/docs](https://llvm.org/docs/LibFuzzer.html) |
| **libFuzzer tutorial** — the single best starting exercise | [↗ github.com/google](https://github.com/google/fuzzing/blob/master/tutorial/libFuzzerTutorial.md) |
| 🔴 **Building a good fuzz target** — **the critical document for this project.** Determinism, speed, no global state, no `exit()`, input-size discipline | [↗ github.com/google](https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md) |
| 🔴 **Structure-aware fuzzing** — how to fuzz *structured* protocol input instead of burning cycles on malformed headers. **Directly applicable to a Sphinx packet parser** | [↗ github.com/google](https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md) |
| **libprotobuf-mutator** — the practical tool for the above | [↗ github.com/google](https://github.com/google/libprotobuf-mutator) |
| **AFL++** — the maintained AFL successor. CmpLog, persistent mode, custom mutators. **Complements libFuzzer; run both for corpus diversity** | [↗ aflplus.plus/docs](https://aflplus.plus/docs/) · [↗ github.com/AFLplusplus](https://github.com/AFLplusplus/AFLplusplus) |
| **FuzzTest** — property-based testing and fuzzing in one C++ API; arguably the modern default | [↗ github.com/google](https://github.com/google/fuzztest) |
| **honggfuzz** — hardware-counter feedback; a useful third engine | [↗ github.com/google](https://github.com/google/honggfuzz) |
| **OSS-Fuzz** + the new-project guide — free continuous fuzzing for open source. **A stretch goal for Adyton in Level 8** | [↗ google.github.io/oss-fuzz](https://google.github.io/oss-fuzz/) · [↗ google.github.io/oss-fuzz](https://google.github.io/oss-fuzz/getting-started/new-project-guide/) |

### The documented subset — `docs/cpp-subset.md`

| Resource | Link |
|---|---|
| **C++ Core Guidelines** — **the Resource Management, Bounds and Lifetime profiles are your curriculum** | [↗ isocpp.github.io/CppCoreGuidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) |
| The repo — issue discussions explain the *reasoning* behind contested rules | [↗ github.com/isocpp](https://github.com/isocpp/CppCoreGuidelines) |
| **Guidelines Support Library (GSL)** — `gsl::span`, `not_null`, `narrow` | [↗ github.com/microsoft](https://github.com/microsoft/GSL) |
| 🔴 **`std::span`** — the C++20 type that replaces pointer-plus-length. **The single highest-leverage change for parser safety, and it is ADR material** | [↗ en.cppreference.com/w](https://en.cppreference.com/w/cpp/container/span) |
| **clang-tidy** + the full check list — pick `cppcoreguidelines-*`, `bugprone-*`, `cert-*` deliberately | [↗ clang.llvm.org/extra](https://clang.llvm.org/extra/clang-tidy/) · [↗ clang.llvm.org/extra](https://clang.llvm.org/extra/clang-tidy/checks/list.html) |
| **libc++ hardening modes** — turns standard-library UB into deterministic traps in production. **Low cost, badly under-used** | [↗ libcxx.llvm.org/Hardening.html](https://libcxx.llvm.org/Hardening.html) |
| **libstdc++ `_GLIBCXX_ASSERTIONS`** — the GCC-side equivalent | [↗ gcc.gnu.org/onlinedocs](https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_macros.html) |
| **Guru of the Week** — Herb Sutter's ownership and lifetime problem sets | [↗ herbsutter.com/gotw](https://herbsutter.com/gotw/) |
| 🔴 **Chromium memory safety** — **~70% of serious Chromium security bugs are memory-safety bugs.** Read it, quote the number, and understand that you are volunteering for that same position | [↗ chromium.org/Home](https://www.chromium.org/Home/chromium-security/memory-safety/) |

### Property-based testing
**RapidCheck** — C++ QuickCheck with shrinking and GoogleTest integration. 🔴 **This is what asserts Sphinx's size invariant.** [↗ github.com/emil-e](https://github.com/emil-e/rapidcheck)
**CppQuickCheck** — an alternative worth comparing, to understand what generators and shrinkers actually are. [↗ github.com/grogers0](https://github.com/grogers0/CppQuickCheck)

### Applied cryptography engineering — you implement nothing, you compose correctly

| Resource | Link |
|---|---|
| **libsodium docs** | [↗ doc.libsodium.org](https://doc.libsodium.org/) |
| **Quickstart & FAQ** — answers "which primitive do I use." **Read first** | [↗ doc.libsodium.org/quickstart](https://doc.libsodium.org/quickstart) |
| **Key exchange (`crypto_kx`)** — separate rx/tx session keys. **The API that prevents the directional-key-reuse bug** | [↗ doc.libsodium.org/key_exchange](https://doc.libsodium.org/key_exchange) |
| **AEAD constructions** — XChaCha20-Poly1305 vs AES-GCM, with nonce-size and nonce-reuse guidance | [↗ doc.libsodium.org/secret-key_cryp…](https://doc.libsodium.org/secret-key_cryptography/aead) |
| **Encrypted streams (`secretstream`)** — chunking, ordering, rekeying, truncation detection, done for you | [↗ doc.libsodium.org/secret-key_cryp…](https://doc.libsodium.org/secret-key_cryptography/secretstream) |
| **Encrypting a set of related messages** — nonce management across many messages on one key | [↗ doc.libsodium.org/secret-key_cryp…](https://doc.libsodium.org/secret-key_cryptography/encrypted-messages) |
| **Key derivation (`crypto_kdf`)** — subkeys with domain separation. **Exactly what you need per-hop and per-direction** | [↗ doc.libsodium.org/key_derivation](https://doc.libsodium.org/key_derivation) |
| 🔴 **Secure memory** — `sodium_memzero`, `sodium_mlock`, guarded heap. **And why a plain `memset` gets optimised away** | [↗ doc.libsodium.org/memory_manageme…](https://doc.libsodium.org/memory_management) |
| **The source** — the test suite is a good model for testing crypto code | [↗ github.com/jedisct1](https://github.com/jedisct1/libsodium) |
| 🔴 **Cryptographic Right Answers** (Latacora, 2018) — one page of what to use and what never to touch | [↗ latacora.com/blog](https://www.latacora.com/blog/2018/04/03/cryptographic-right-answers/) |
| 🔴 **Cryptopals** — you break padding oracles, CBC bit-flipping and nonce reuse **by hand.** Nothing teaches implementation pitfalls faster. **Sets 1–2 are scheduled in Level 3** | [↗ cryptopals.com](https://cryptopals.com/) |
| **Constant-time crypto** (Pornin/BearSSL) — which operations are constant-time on real CPUs and which silently are not | [↗ bearssl.org/constanttime.html](https://bearssl.org/constanttime.html) |
| **A beginner's guide to constant-time cryptography** — the gentler on-ramp, with concrete C rewrites | [↗ chosenplaintext.ca/articles](https://www.chosenplaintext.ca/articles/beginners-guide-constant-time-cryptography.html) |
| **cryptocoding** (Aumasson) — a do/don't checklist. **Use it as the review checklist for every crypto-touching PR** | [↗ github.com/veorq](https://github.com/veorq/cryptocoding) |
| **Matthew Green's blog** — the best ongoing accessible analysis of real-world crypto failures | [↗ blog.cryptographyengineering.com](https://blog.cryptographyengineering.com/) |

### High-performance I/O

| Resource | Link |
|---|---|
| **Lord of the io_uring** — the best io_uring tutorial that exists | [↗ unixism.net/loti](https://unixism.net/loti/) |
| **liburing** — the official helper library; `test/` is the most complete usage corpus available | [↗ github.com/axboe](https://github.com/axboe/liburing) |
| `io_uring(7)`, `io_uring_setup(2)` — the SQ/CQ ring memory model and every flag that determines your performance profile | [↗ man7.org/linux](https://man7.org/linux/man-pages/man7/io_uring.7.html) · [↗ man7.org/linux](https://man7.org/linux/man-pages/man2/io_uring_setup.2.html) |
| **The rapid growth of io_uring** (LWN, Corbet) — why it grew beyond storage I/O | [↗ lwn.net/Articles](https://lwn.net/Articles/810414/) |
| **io_uring-echo-server** — the standard published epoll-vs-io_uring comparison | [↗ github.com/frevib](https://github.com/frevib/io_uring-echo-server) |
| `epoll(7)` — the baseline you are measuring against; the level-vs-edge-triggered section is the classic source of bugs | [↗ man7.org/linux](https://man7.org/linux/man-pages/man7/epoll.7.html) |
| **MSG_ZEROCOPY** + **Zero-copy networking** (LWN) — and the honest answer about *when* it actually wins | [↗ kernel.org/doc](https://www.kernel.org/doc/html/latest/networking/msg_zerocopy.html) · [↗ lwn.net/Articles](https://lwn.net/Articles/726917/) |
| `splice(2)`, `sendfile(2)` — the pipe-buffer generalisation; foundation for proxying without copies | [↗ man7.org/linux](https://man7.org/linux/man-pages/man2/splice.2.html) |
| **The C10K Problem** (Kegel) — read as an artifact of how the industry got here | [↗ kegel.com/c10k.html](https://www.kegel.com/c10k.html) |
| **The Secret to 10 Million Concurrent Connections** — the C10M argument: the kernel is the bottleneck | [↗ highscalability.com/the-secret-to…](https://highscalability.com/the-secret-to-10-million-concurrent-connections-the-kernel-i/) |
| *Optional:* **DPDK Programmer's Guide**, **AF_XDP**, **eBPF/XDP tutorial** — read to know what exists; **you are not using kernel bypass this year** | [↗ doc.dpdk.org/guides](https://doc.dpdk.org/guides/prog_guide/) · [↗ kernel.org/doc](https://www.kernel.org/doc/html/latest/networking/af_xdp.html) · [↗ github.com/xdp-project](https://github.com/xdp-project/xdp-tutorial) |

### Measurement — Law 2's toolkit

| Resource | Link |
|---|---|
| 🔴 **How NOT to Measure Latency** (Gil Tene) — **mandatory viewing before you publish a single benchmark, and you re-audit against it in Week 47** | [↗ infoq.com/presentations](https://www.infoq.com/presentations/latency-response-time/) |
| **Coordinated omission, the original thread** — Tene's written explanation with expert pushback | [↗ groups.google.com/g](https://groups.google.com/g/mechanical-sympathy/c/icNZJejUHfE) |
| **The Tail at Scale** (Dean & Barroso, CACM 2013) — eight pages; hedged requests, tied requests, micro-partitioning | [↗ research.google/pubs](https://research.google/pubs/the-tail-at-scale/) |
| **HdrHistogram** + the C port — constant-cost recording with accurate high percentiles. **The right data structure for latency** | [↗ hdrhistogram.org](http://hdrhistogram.org/) · [↗ github.com/HdrHistogram](https://github.com/HdrHistogram/HdrHistogram_c) |
| **wrk2** — a *constant-throughput* load generator that corrects for coordinated omission. The practical companion to the talk | [↗ github.com/giltene](https://github.com/giltene/wrk2) |
| **The USE Method** + the Linux checklist — a complete, finite checklist for finding a bottleneck instead of guessing | [↗ brendangregg.com/usemethod.html](https://www.brendangregg.com/usemethod.html) · [↗ brendangregg.com/USEmethod](https://www.brendangregg.com/USEmethod/use-linux.html) |
| **Flame Graphs** + the tooling — how to read them, and how to mis-read them | [↗ brendangregg.com/flamegraphs.html](https://www.brendangregg.com/flamegraphs.html) · [↗ github.com/brendangregg](https://github.com/brendangregg/FlameGraph) |
| **Linux perf Examples** — the best `perf` tutorial anywhere; dozens of copy-pasteable one-liners | [↗ brendangregg.com/perf.html](https://www.brendangregg.com/perf.html) · [↗ perfwiki.github.io/main](https://perfwiki.github.io/main/) |
| **benchstat** — applies actual statistics to benchmark output. **Stops you shipping noise as a speedup** | [↗ pkg.go.dev/golang.org](https://pkg.go.dev/golang.org/x/perf/cmd/benchstat) |
| **Google Benchmark** + user guide — `DoNotOptimize`/`ClobberMemory` to defeat the optimiser | [↗ github.com/google](https://github.com/google/benchmark) · [↗ github.com/google](https://github.com/google/benchmark/blob/main/docs/user_guide.md) |
| **Systems Performance 2e** (Gregg) — the reference text. Ch. 6 §6.6, ch. 13 | [↗ brendangregg.com/systems-performa…](https://www.brendangregg.com/systems-performance-2nd-edition-book.html) |

---

## V.B DEPARTMENT OF NETWORKS & TRANSPORT

> **Levels 5 and 6.** This is the department where you stop *using* the network and start understanding it. The artifact — a TCP that passes Stanford's test suite — is unfakeable, and it becomes the argument for every transport decision you make afterwards.

### Congestion control and the byte stream

| Resource | Why | Link |
|---|---|---|
| 🔴 **TCP Congestion Control: A Systems Approach** (Peterson, Brakmo & Davie, free online book) | **A free book devoted entirely to congestion control.** The best single spine for this topic and better than any chapter | [↗ tcpcc.systemsapproach.org](https://tcpcc.systemsapproach.org/) |
| **RFC 5681 — TCP Congestion Control** | The baseline: slow start, congestion avoidance, fast retransmit/recovery | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc5681.html) |
| 🔴 **RFC 6298 — Computing TCP's Retransmission Timer** | SRTT, RTTVAR, minimum RTO, exponential backoff. **You will reimplement this algorithm in CS144 Checkpoint 3** | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc6298.html) |
| **RFC 9438 — CUBIC** | The *current* standard. **Teach this one, not 8312** | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9438.html) |
| **RFC 8312 — CUBIC (historical)** | Useful only to show how a spec matures under deployment | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc8312.html) |
| **BBR: Congestion-Based Congestion Control** (Cardwell et al., Google) | Reframed congestion control around bottleneck bandwidth and RTT instead of loss | [↗ research.google/pubs](https://research.google/pubs/bbr-congestion-based-congestion-control/) |
| **google/bbr** — v1/v2/v3 code, docs, talks, maintained by the authors | The canonical hub | [↗ github.com/google](https://github.com/google/bbr) |
| **The BBR internet-draft** | The state machine written out in full | [↗ datatracker.ietf.org/doc](https://datatracker.ietf.org/doc/draft-cardwell-iccrg-bbr-congestion-control/) |
| 🔴 **Bufferbloat — Jim Gettys' own archive** | The primary-source narrative of discovering and diagnosing it. **And the reason a bigger buffer makes latency worse** | [↗ gettys.wordpress.com/category](https://gettys.wordpress.com/category/bufferbloat/) |
| **Bufferbloat.net** | fq_codel, CAKE, make-wifi-fast, and the measurement tooling | [↗ bufferbloat.net/projects](https://www.bufferbloat.net/projects/) |
| **RFC 8289 (CoDel)** and **RFC 8290 (fq_codel)** | The no-knobs AQM based on sojourn time — the standardised fix, now the Linux default qdisc | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc8289.html) · [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc8290.html) |

### QUIC — the transport you ship

| Resource | Why | Link |
|---|---|---|
| **RFC 9000 — QUIC** | Streams, flow control, connection IDs, migration, frame layout. **Read §2, §5, §12–13, §17** | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9000.html) |
| **RFC 9001 — Using TLS to Secure QUIC** | The handshake, key schedule and header protection. 🔴 **Header protection is why your handshakes can be made byte-identical except the random bits** | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9001.html) |
| **RFC 9002 — Loss Detection and Congestion Control** | ACK handling, packet number spaces, RTT estimation | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9002.html) |
| **RFC 8446 — TLS 1.3** | Prerequisite for 9001. The 0-RTT and key-schedule machinery lives here. **Read §2 (six pages) minimum** | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc8446.html) |
| **RFC 9221 — Unreliable Datagram Extension** | Essential if you ever want QUIC carrying real-time traffic rather than reliable streams | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9221.html) |
| **RFC 9312 — Manageability of QUIC** | 🔴 **What network observers can and cannot see. Read this one specifically as a privacy engineer** — it is the operator's-eye view of your own threat model | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9312.html) |
| **RFC 9308 — Applicability of QUIC** | When QUIC is and is not the right choice, written by the working group itself | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9308.html) |
| **RFC 9369 — QUIC Version 2** | A deliberate version-negotiation exercise to fight ossification | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9369.html) |

### QUIC, explained by humans

| Resource | Why | Link |
|---|---|---|
| 🔴 **Head-of-Line Blocking in QUIC and HTTP/3: The Details** (Robin Marx) | **The definitive HOL-blocking explainer**, traced across HTTP/1.1 → /2 → /3 — and it argues the fix is *oversold*, which is exactly the scepticism you want before you build the chart yourself | [↗ calendar.perfplanet.com/2020](https://calendar.perfplanet.com/2020/head-of-line-blocking-in-quic-and-http-3-the-details/) |
| The source repo, with the full diagram set | | [↗ github.com/rmarx](https://github.com/rmarx/holblocking-blogpost) |
| **HTTP/3 From A to Z: Core Concepts** (Marx, Smashing) | The clearest ground-up explanation of why QUIC exists, by a QUIC WG contributor rather than a vendor | [↗ smashingmagazine.com/2021](https://www.smashingmagazine.com/2021/08/http3-core-concepts-part1/) |
| **HTTP/3: Performance Improvements** (Marx) | 🔴 **Healthily sceptical on 0-RTT, migration and HOL removal. Separates real gains from marketing** | [↗ smashingmagazine.com/2021](https://www.smashingmagazine.com/2021/08/http3-performance-improvements-part2/) |
| **HTTP/3: Practical Deployment** (Marx) | What actually changes operationally | [↗ smashingmagazine.com/2021](https://www.smashingmagazine.com/2021/09/http3-practical-deployment-options-part3/) |
| 🔴 **qvis — QUIC and HTTP/3 visualisation** | Load a qlog trace and **see** congestion window, multiplexing and HOL blocking. **The best teaching aid for QUIC internals that exists — point it at your own implementation's traces** | [↗ qvis.quictools.info](https://qvis.quictools.info/) · [↗ github.com/quiclog](https://github.com/quiclog/qvis) |
| **HTTP/3 explained** (Daniel Stenberg, free book) | Continuously updated book-length introduction from curl's author | [↗ http3-explained.haxx.se/en](https://http3-explained.haxx.se/en) |
| **The Road to QUIC** (Cloudflare) | The classic "why not TCP" argument, with ossification framed concretely | [↗ blog.cloudflare.com/the-road-to-q…](https://blog.cloudflare.com/the-road-to-quic/) |
| **Introducing 0-RTT** (Cloudflare) | The best 0-RTT explainer, unusually honest about the replay-attack tradeoff | [↗ blog.cloudflare.com/introducing-0…](https://blog.cloudflare.com/introducing-0-rtt/) |
| **Does the QUIC handshake require compression to be fast?** (Fastly) | Real measurement of handshake cost. **A good model for how to interrogate a protocol claim** | [↗ fastly.com/blog](https://www.fastly.com/blog/quic-handshake-tls-compression-certificates-extension-study) |
| **QUIC Interop Runner** | Live interop matrix — shows which features are *actually* deployed, not just specified | [↗ interop.seemann.io](https://interop.seemann.io/) |

### The two QUIC papers you must read together

| Resource | Why | Link |
|---|---|---|
| **The QUIC Transport Protocol: Design and Internet-Scale Deployment** (Langley et al., SIGCOMM '17) | The foundational deployment paper: 15–18% YouTube rebuffer reduction, 3.5–8% search latency reduction, at 35% of Google egress | [↗ research.google/pubs](https://research.google/pubs/the-quic-transport-protocol-design-and-internet-scale-deployment/) |
| 🔴 **QUIC is not Quick Enough over Fast Internet** (Zhang et al., WWW '24) | **The essential counterweight: up to 45.2% *lower* throughput than TCP+TLS+HTTP/2 on fast links**, root-caused to receiver-side processing and userspace ACKs. **Read it the same week as the paper above and hold both** | [↗ arxiv.org/abs](https://arxiv.org/abs/2310.09423) |

### Implementations to read and to use

| Resource | Why | Link |
|---|---|---|
| 🔴 **ngtcp2** — pure C, pluggable TLS backend. **This is what Adyton links against** | The reference for embedding QUIC in C/C++ | [↗ github.com/ngtcp2](https://github.com/ngtcp2/ngtcp2) |
| ngtcp2 docs and examples | A complete client/server pair — the fastest way to see the API driven end to end | [↗ nghttp2.org/ngtcp2](https://nghttp2.org/ngtcp2/) · [↗ github.com/ngtcp2](https://github.com/ngtcp2/ngtcp2/tree/main/examples) |
| **picoquic** | 🔴 **Deliberately minimal C — the most *readable* QUIC codebase for learning.** Read this one, link the other | [↗ github.com/private-octopus](https://github.com/private-octopus/picoquic) |
| **quiche** (Cloudflare, Rust) | I/O-free API; powers Cloudflare's edge | [↗ github.com/cloudflare](https://github.com/cloudflare/quiche) |
| **MsQuic** (Microsoft) + its perf dashboard | RSS, UDP GSO/GRO coalescing, XDP bypass. **The best case study in QUIC performance engineering**, with continuously published numbers | [↗ github.com/microsoft](https://github.com/microsoft/msquic) · [↗ microsoft.github.io/msquic](https://microsoft.github.io/msquic/) |

### NAT traversal — Level 6

| Resource | Why | Link |
|---|---|---|
| 🔴 **How NAT traversal works** (Tailscale, David Anderson) | **The best practical write-up in existence.** Every NAT class, birthday-paradox port prediction for symmetric NAT, and honest failure statistics. **Read this before any RFC** | [↗ tailscale.com/blog](https://tailscale.com/blog/how-nat-traversal-works) |
| **How Tailscale works** | DERP as a production answer to "what do you do when traversal fails" | [↗ tailscale.com/blog](https://tailscale.com/blog/how-tailscale-works) |
| 🔴 **Peer-to-Peer Communication Across NATs** (Ford, Srisuresh & Kegel, USENIX ATC '05) | **The original hole-punching paper**, including a measurement study of real success rates across hundreds of NATs | [↗ bford.info/pub](https://bford.info/pub/net/p2pnat/) |
| **RFC 4787 — NAT Behavioral Requirements** | Defines endpoint-independent / address-dependent / **symmetric**. **The vocabulary for every NAT conversation. §4 is the core** | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc4787.html) |
| **RFC 5128 — State of P2P Communication across NATs** | Survey of every technique with its failure modes. The best single overview | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc5128.html) |
| **RFC 8445 — ICE** | The candidate-gathering and connectivity-check state machine everyone reimplements. **§2 is enough** | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc8445.html) |
| **RFC 8489 — STUN** (current) and **RFC 5389** (historical) | **Read both and diff them** — most deployed code still implements 5389 | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc8489.html) · [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc5389.html) |
| **RFC 8656 — TURN** | The relay fallback for when punching fails | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc8656.html) |
| 🔴 **pion/ice** — **this is what Adyton uses** | A clean, readable Go ICE implementation you can actually finish reading | [↗ github.com/pion](https://github.com/pion/ice) · [↗ pkg.go.dev/github.com](https://pkg.go.dev/github.com/pion/ice/v4) |
| **pion/webrtc** + examples | Pure Go, no cgo. The reference for learning the whole stack | [↗ github.com/pion](https://github.com/pion/webrtc) · [↗ github.com/pion](https://github.com/pion/webrtc/tree/main/examples) |
| **WebRTC for the Curious** (free book) | Vendor-neutral, explains *why* WebRTC works the way it does. The best conceptual companion to the RFCs | [↗ webrtcforthecurious.com](https://webrtcforthecurious.com/) |
| **DCUtR spec** (libp2p) | Coordinated hole punching — a compact, complete spec worth reading end to end | [↗ github.com/libp2p](https://github.com/libp2p/specs/blob/master/relay/DCUtR.md) |
| **Hole punching in libp2p** (Protocol Labs) | The narrative explainer of AutoNAT + Circuit Relay v2 + DCUtR working together | [↗ blog.ipfs.tech/2022-01-20-libp2p-…](https://blog.ipfs.tech/2022-01-20-libp2p-hole-punching/) |
| 🔴 **Hole punching in the wild** (FOSDEM 2023) | **6.25M hole-punch results from 154 clients against 47,000 peers; ~70% success for both TCP and QUIC** — overturning the folk belief that UDP is easier. **This is the number your own `natlab` measurement is compared against** | [↗ archive.fosdem.org/2023](https://archive.fosdem.org/2023/schedule/event/network_hole_punching_in_the_wild/) |
| **punchr** — the instrumentation behind those numbers | **A model for how to measure your own system honestly** | [↗ github.com/libp2p](https://github.com/libp2p/punchr) |
| **Large-Scale Measurement of NAT Traversal for the Decentralized Web** (arXiv, 2026) | The most recent success-rate study | [↗ arxiv.org/abs](https://arxiv.org/abs/2604.12484) |
## V.C ⭐ DEPARTMENT OF ANONYMOUS COMMUNICATION

> **This is the department nobody else's roadmap has, and it is where your forty-five-minute answer comes from.**
>
> Three of these sections are not reading lists — they are **arguments that ran for a decade or more**, and following an argument is a different and better education than reading twenty papers. They are marked ⛓ **THE SPINE** and you read them **in order**.

### F.1 · Foundations — Week 7, before you write a line of Adyton

| Resource | Why | Link |
|---|---|---|
| 🔴 **Chaum, "Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms"** (CACM, 1981) | **The origin of the entire field, and it is seven pages.** Mixes, layered public-key encryption, return addresses. Read it first, before anything modern | [↗ chaum.com/wp-content](https://chaum.com/wp-content/uploads/2022/09/UNTRACEABLE-ELECTRONIC-MAIL-RETURN-ADDRESSES-AND-DIGITAL-PSEUDONYMS-tech-report.pdf) |
| 🔴 **Dingledine, Mathewson, Syverson, "Tor: The Second-Generation Onion Router"** (USENIX Security 2004) | **The design you are a cousin of.** Every later paper in this department is a reaction to a decision made here | [↗ svn-archive.torproject.org/svn](https://svn-archive.torproject.org/svn/projects/design-paper/tor-design.pdf) |
| **Reed, Syverson, Goldschlag, "Anonymous Connections and Onion Routing"** (IEEE JSAC, 1998) | The pre-Tor Naval Research Lab design — shows what Tor inherited and what it deliberately discarded | [↗ cs.umd.edu/class](https://www.cs.umd.edu/class/fall2023/cmsc614/papers/onion-routing.pdf) |
| 🔴 **The Tor Specifications** | **The normative protocol. This is what you implement against.** Start at `tor-spec`, then branch | [↗ spec.torproject.org](https://spec.torproject.org/) |
| — `tor-spec` | Cells, circuits, CREATE/EXTEND handshakes, relay cell format | [↗ spec.torproject.org/tor-spec](https://spec.torproject.org/tor-spec/index.html) |
| — `path-spec` | 🔴 **How clients actually choose circuits today — the baseline every AS-aware proposal in §F.4 modifies** | [↗ spec.torproject.org/path-spec](https://spec.torproject.org/path-spec/index.html) |
| — `guard-spec` | The sampling-attack defence. **Prerequisite for the guard-placement attacks** | [↗ spec.torproject.org/guard-spec](https://spec.torproject.org/guard-spec/index.html) |
| — `dir-spec` | Consensus, directory authorities, relay descriptors — **the trust root, and the thing your Level 7 rebuilds** | [↗ spec.torproject.org/dir-spec](https://spec.torproject.org/dir-spec/index.html) |
| — `padding-spec` | The normative document for Tor cover traffic, connection- and circuit-level | [↗ spec.torproject.org/padding-spec](https://spec.torproject.org/padding-spec/index.html) |
| 🔴 **All Tor design proposals** | **Where Tor's design debates actually happen. The single richest primary source in this entire curriculum** | [↗ spec.torproject.org/proposals](https://spec.torproject.org/proposals/BY_STATUS.html) |
| **Tor Research Portal** and 🔴 **the Research Safety Board** | **Nine concrete safety principles for measuring a live anonymity network. Read the Safety Board page before you collect any data at all — including in Level 2** | [↗ research.torproject.org](https://research.torproject.org/) · [↗ research.torproject.org/safetyboa…](https://research.torproject.org/safetyboard/) |
| **Free Haven's Selected Papers in Anonymity (anonbib)** | The field's canonical curated bibliography ⚠️ *host was unreachable during research; use the mirror if it stays down* | [↗ freehaven.net/anonbib](https://www.freehaven.net/anonbib/) · mirror [↗ github.com/glamrock](https://github.com/glamrock/anonbib) |
| **Arti — the Rust Tor implementation** | The code to read next to the spec. Start at `crates/tor-proto` | [↗ gitlab.torproject.org/tpo](https://gitlab.torproject.org/tpo/core/arti) · docs [↗ tpo.pages.torproject.net/core](https://tpo.pages.torproject.net/core/doc/rust/arti_client/index.html) |
| 🔴 **Counter Galois Onion** (Tor blog Nov 2025; EUROCRYPT 2026) | **NEWER — Tor is replacing its relay-cell encryption** with a non-malleable forward-secret scheme. This is the current cryptographic frontier and it postdates every other roadmap you have | [↗ blog.torproject.org/introducing-c…](https://blog.torproject.org/introducing-cgo/) |

### F.2 · The packet format — Level 3, and read the correction

| Resource | Why | Link |
|---|---|---|
| 🔴 **Danezis & Goldberg, "Sphinx: A Compact and Provably Secure Mix Format"** (IEEE S&P 2009) | **The format you implement.** Essentially every modern mixnet and the Lightning onion derive from it | [↗ cypherpunks.ca/~iang](https://cypherpunks.ca/~iang/pubs/Sphinx_Oakland09.pdf) · ePrint [↗ eprint.iacr.org/2008](https://eprint.iacr.org/2008/475) |
| 🔴🔴 **Scherer, Weis, Strufe, "Provable Security for the Onion Routing and Mix Network Packet Format Sphinx"** (PoPETs 2024) | **NEWER, and you must read it with the paper above.** It **repairs Sphinx's broken proof**, shows **DDH is insufficient (you need Gap-DH)**, and documents a **payload malleability issue.** 🔴 **No other roadmap mentions this. Implementing Sphinx in 2027 without it is implementing a 2009 understanding of it** | [↗ arxiv.org/abs](https://arxiv.org/abs/2312.08028) |
| **Kuhn, Beck, Strufe, "Breaking and (Partially) Fixing Provably Secure Onion Routing"** (IEEE S&P 2020) | Invalidates the Camenisch–Lysyanskaya onion-security framework that Sphinx and HORNET relied on. **Read for the humility** | [↗ arxiv.org/abs](https://arxiv.org/abs/1910.13772) |
| 🔴 **Lightning BOLT #4: Onion Routing Protocol** | **The most widely deployed Sphinx derivative on Earth**, with its deltas from the academic format written down explicitly | [↗ github.com/lightning](https://github.com/lightning/bolts/blob/master/04-onion-routing.md) |
| **lightning-onion** (Go reference implementation) | The concrete engineering deltas: MAC over the whole header, ChaCha20 instead of LIONESS, no end-to-end payload | [↗ github.com/lightningnetwork](https://github.com/lightningnetwork/lightning-onion) |
| **nymtech/sphinx** (Rust) | The reference modern implementation. **Read it next to the 2009 paper** | [↗ github.com/nymtech](https://github.com/nymtech/sphinx) |
| **Nym, "Outfox: a Packet Format for a Layered Mixnet"** (arXiv, Dec 2024) | **NEWER** — the Sphinx successor: fewer per-hop public-key operations, smaller headers, KEMs instead of DH for post-quantum readiness | [↗ arxiv.org/abs](https://arxiv.org/abs/2412.19937) |
| **Piotrowska et al., "The Loopix Anonymity System"** (USENIX Security 2017) | Poisson mixing and loop cover traffic — **the corner of the trilemma you are deliberately not taking**, and you should be able to say why | [↗ usenix.org/system](https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-piotrowska.pdf) |
| **Katzenpost mix network specifications** | An implementable, engineer-grade spec of a Loopix-style mixnet — **the missing link between papers and code** | [↗ katzenpost.network/docs](https://katzenpost.network/docs/specs/) |
| *Optional depth:* **HORNET** (CCS 2015) · **Vuvuzela** (SOSP 2015) · **Karaoke** (OSDI 2018) | Sphinx at line rate; and the DP-based metadata-hiding branch you are not taking | [↗ arxiv.org/abs](https://arxiv.org/abs/1507.05724) · [↗ pdos.csail.mit.edu/papers](https://pdos.csail.mit.edu/papers/vuvuzela:sosp15.pdf) · [↗ usenix.org/system](https://www.usenix.org/system/files/osdi18-lazar.pdf) |

### F.3 · The trilemma — Week 7, and every design decision descends from it

| Resource | Why | Link |
|---|---|---|
| 🔴 **Das, Meiser, Mohammadi, Kate, "Anonymity Trilemma: Strong Anonymity, Low Bandwidth Overhead, Low Latency — Choose Two"** (IEEE S&P 2018) | **The impossibility result that sets your entire design envelope.** Adyton takes low latency and low overhead and gives up strong anonymity against a global passive adversary — **and this is the paper that makes that a principled choice rather than a shortcut** | [↗ eprint.iacr.org/2017](https://eprint.iacr.org/2017/954) |
| **"Comprehensive Anonymity Trilemma: User Coordination is not enough"** (PoPETs 2020) | Closes the loophole for protocols with proactive user coordination | [↗ petsymposium.org/popets](https://petsymposium.org/popets/2020/popets-2020-0056.pdf) |
| **Serjantov & Danezis; Díaz et al.** (both PET 2002) | 🔴 **Entropy-based anonymity-set size and the normalised degree of anonymity — read side by side; together they are the field's standard metric** | [↗ link.springer.com/chapter](https://link.springer.com/chapter/10.1007/3-540-36467-6_4) · [↗ link.springer.com/chapter](https://link.springer.com/chapter/10.1007/3-540-36467-6_5) |
| 🔴 **Kuhn et al., "On Privacy Notions in Anonymous Communication"** (PoPETs 2019, Best Paper) | **A complete hierarchy of ~20 privacy notions with strictness proofs. This is the reference for stating precisely what your system claims** — and precision is the whole discipline of your honesty statement | [↗ petsymposium.org/popets](https://petsymposium.org/popets/2019/popets-2019-0022.pdf) |

### F.4 ⛓ THE SPINE — AS-aware path selection, read in this order

> **This is the research contribution, and it is a nine-year argument with a negative result in the middle.** Read the five in order. The fourth is the one that should shape your design, and it is the reason your Level 9 exists.

| # | Read | Why | Link |
|---|---|---|---|
| **1** | 🔴 **Johnson, Wacek, Jansen, Sherr, Syverson, "Users Get Routed: Traffic Correlation on Tor by Realistic Adversaries"** (CCS 2013) | **Prerequisite for everything else.** Establishes the security-over-time framing and the AS/IXP adversary model the whole literature uses, and introduces **TorPS** | [↗ dl.acm.org/doi](https://dl.acm.org/doi/10.1145/2508859.2516651) |
| **2** | **Nithyanand et al., "Measuring and Mitigating AS-level Adversaries Against Tor" (Astoria)** (NDSS 2016) | The canonical AS-aware client: path prediction plus LP relay selection cuts vulnerable circuits from ~40% to 2% | [↗ arxiv.org/abs](https://arxiv.org/abs/1505.05173) |
| **3a** | **Sun et al., "Counter-RAPTOR"** (IEEE S&P 2017) | Guard resilience against BGP hijack, plus location-aware guard selection with *bounded* location leakage | [↗ arxiv.org/abs](https://arxiv.org/abs/1704.00843) |
| **3b** | **Barton & Wright, "DeNASA: Destination-Naive AS-Awareness"** (PoPETs 2016) | AS-awareness *without* knowing the destination — compatible with pre-built circuits, which matters for latency | [↗ petsymposium.org/popets](https://petsymposium.org/popets/2016/popets-2016-0044.php) |
| **4** | 🔴🔴 **Wan, Johnson, Wails, Wagh, Mittal, "Guard Placement Attacks on Path Selection Algorithms for Tor"** (PoPETs 2019) | **THE PAPER THIS LEVEL EXISTS TO ANSWER.** 0.216% of Tor's bandwidth bought **18% of guard-selection probability** against Counter-RAPTOR, DeNASA and LASTor. **A better defence made the targeted case worse, and a defender measuring only the average would never have noticed** | [↗ princeton.edu/~pmittal](https://www.princeton.edu/~pmittal/publications/guard-placement-pets19.pdf) |
| **5** | **Rochet, Wails, Johnson, Mittal, Pereira, "CLAPS: Client-Location-Aware Path Selection in Tor"** (CCS 2020) | The state of the art: fixes the security and load-balancing failures of Counter-RAPTOR and DeNASA by **formally bounding** location leakage. Read last | [↗ freehaven.net/anonbib](https://www.freehaven.net/anonbib/cache/claps-ccs2020.pdf) |

**The attack literature underneath it:**
**RAPTOR** (USENIX Security 2015) — BGP hijack/interception plus asymmetric-traffic correlation, validated on live Tor · [↗ arxiv.org/pdf](https://arxiv.org/pdf/1503.03940)
**Murdoch & Zieliński, "Sampled Traffic Analysis by Internet-Exchange-Level Adversaries"** (PET 2007) — 🔴 Bayesian traffic analysis succeeds on **1-in-N sampled NetFlow.** Why **IXP** diversity matters and not just AS diversity · [↗ link.springer.com/content](https://link.springer.com/content/pdf/10.1007/978-3-540-75551-7_11.pdf)
**Wails et al., "Tempest: Temporal Dynamics in Anonymity Systems"** (PoPETs 2018) — 🔴 client mobility, usage patterns and BGP churn degrade anonymity over time, **and location-aware selection makes mobility *worse*** · [↗ petsymposium.org/popets](https://petsymposium.org/popets/2018/popets-2018-0019.php)

**🔴 The reality check you must read before trusting any of it:**
**Juen, Johnson, Das, Borisov, Caesar, "Defending Tor from Network Adversaries: A Case Study of Network Path Prediction"** (PoPETs 2015) — **17.2 million traceroutes showing BGP-simulated paths disagree badly with measured paths.** Every AS-aware design in this section rests on inference that is *substantially wrong*, and saying so in your write-up is what separates a research contribution from a demo · [↗ petsymposium.org/popets](https://petsymposium.org/popets/2015/popets-2015-0021.php)
**Nithyanand, Singh, Cho, Gill, "Holding all the ASes"** (arXiv 2016) — the essential self-critique: measurement error, inference error and performance pitfalls that break real AS-aware clients, **including Astoria** · [↗ arxiv.org/abs](https://arxiv.org/abs/1605.03596)

**The newest work — none of which appears in any earlier roadmap:**
**"RPKI-Based Location-Unaware Tor Guard Relay Selection"** (PoPETs 2025) — **NEWER** — sidesteps client-location leakage *entirely* by using RPKI/ROV deployment status instead of client location. 🔴 **A genuinely different answer to the guard-placement problem, and a candidate for your own selector** · [↗ arxiv.org/abs](https://arxiv.org/abs/2501.06010)
**"Who Carries Tor? Measuring Bandwidth-Weighted Transit Concentration"** (FOCI 2026) — **NEWER** — a 2015–2025 longitudinal study showing transit concentration persists despite network growth · [↗ petsymposium.org/foci](https://www.petsymposium.org/foci/2026/foci-2026-0014.pdf)
**"An Extended View on Measuring Tor AS-level Adversaries"** (Computers & Security 2023) — RIPE Atlas re-measurement, IPv4 vs IPv6 exposure, per-country risk · [↗ arxiv.org/pdf](https://arxiv.org/pdf/2403.08517)
**"PredicTor" / CLASI** (ACM TOPS 2025) — **NEWER** — a metric for how *inferable* a client's AS is from its path-selection behaviour. **Directly the quantity your trade-off curve is measuring** · [↗ dl.acm.org/doi](https://dl.acm.org/doi/10.1145/3723356)

**The AS-graph foundations — Level 9, Week 49:**
🔴 **Gao, "On Inferring Autonomous System Relationships in the Internet"** (IEEE/ACM ToN 2001) — **the origin of valley-free routing** and the customer/provider/peer heuristic every AS-aware path predictor rests on. **Start here** · [↗ dl.acm.org/doi](https://dl.acm.org/doi/10.1109/90.974527)
**Luckie et al., "AS Relationships, Customer Cones, and Validation"** (IMC 2013) — the algorithm behind the CAIDA dataset, **and it deliberately does not maximise valley-free paths**, which is directly relevant to valley-free's limits · [↗ conferences.sigcomm.org/imc](https://conferences.sigcomm.org/imc/2013/papers/imc039-luckieAemb.pdf)
🔴 **CAIDA AS Relationships dataset** — **the actual monthly p2c/p2p files that Astoria, DeNASA, Counter-RAPTOR and CLAPS all consume. Download these in Week 49 and get your hands dirty early** · [↗ caida.org/catalog](https://www.caida.org/catalog/datasets/as-relationships/)

**The tools you will actually run:**
🔴 **TorPS — the Tor Path Simulator** — Monte Carlo simulation of path selection over months of **real consensus archives.** The standard tool for evaluating a new algorithm's security *over time* · [↗ github.com/torps](https://github.com/torps/torps)
**Shadow** — runs unmodified Tor binaries deterministically; the tool for the *performance* side · [↗ shadow.github.io](https://shadow.github.io/) · [↗ github.com/shadow](https://github.com/shadow/tornettools)

### F.5 ⛓ THE SPINE — website fingerprinting, and a twelve-year argument about realism

> **Read these four in order and you will have watched a field correct itself.** Then you will know why Adyton's traffic-shaping work is scoped to `NEXT.md` rather than promised.

| # | Read | Why | Link |
|---|---|---|---|
| **1** | **Juarez, Afroz, Acar, Diaz, Greenstadt, "A Critical Evaluation of Website Fingerprinting Attacks"** (CCS 2014) | The realism critique: browsing habits, multi-tab, location and browser version **wreck published accuracies.** Read this immediately after any attack paper | [↗ dl.acm.org/doi](https://dl.acm.org/doi/10.1145/2660267.2660368) |
| **2** | 🔴 **Cherubin, Jansen, Troncoso, "Online Website Fingerprinting: Evaluating WF Attacks on Tor in the Real World"** (USENIX Security 2022, **Distinguished Paper**) | **The single most important reality check in this department.** The first evaluation on genuine Tor exit traffic in a true open world — **precision collapses versus lab numbers** | [↗ usenix.org/conference](https://www.usenix.org/conference/usenixsecurity22/presentation/cherubin) |
| **3** | **Jansen, Wails, Johnson, "A Measurement of Genuine Tor Traces for Realistic Website Fingerprinting"** (arXiv 2024) | Safely measured real traces showing **how synthetic datasets bias WF results** | [↗ arxiv.org/abs](https://arxiv.org/abs/2404.07892) |
| **4** | **"Reality Check for Tor Website Fingerprinting in the Open World"** (arXiv Mar 2026) | **NEWER** — Tao Wang's group revisiting open-world viability. The most recent word | [↗ arxiv.org/abs](https://arxiv.org/abs/2603.07412) |

**The attacks, for context:** Panchenko et al. (WPES 2011, put WF on the map) · Wang & Goldberg (WPES 2013, establishes the **Tor cell** as the right unit of analysis) · **Hayes & Danezis, k-fingerprinting** (USENIX Security 2016 — still the strongest non-DL baseline) · 🔴 **Sirinam et al., "Deep Fingerprinting"** (CCS 2018 — **the CNN that broke WTF-PAD at >90% and reset the arms race**) · Triplet Fingerprinting (CCS 2019 — portable fingerprints from ~5 examples).
🔴 **The survey to use as this section's spine: Cui et al., "A Comprehensive Survey of Website Fingerprinting Attacks and Defenses in Tor"** (arXiv Oct 2025, 46pp) — **NEWER** · [↗ arxiv.org/abs](https://arxiv.org/abs/2510.11804)

**The defences, for when you get to `NEXT.md`:** Shmatikov & Wang's **original adaptive padding** (ESORICS 2006) · **WTF-PAD** (ESORICS 2016) · **Walkie-Talkie** (USENIX Security 2017 — **the one Deep Fingerprinting could not break**, held to 49.7%) · **FRONT and GLUE** (USENIX Security 2020 — cheap, and the standard modern baseline) · **RegulaTor** (PoPETs 2022 — the "simplicity wins" counterpoint) · **Surakav** (IEEE S&P 2022 — GAN-generated traces).
🔴 **The bridge from papers to deployable code: Pulls, "Towards Effective and Efficient Padding Machines for Tor"** ([↗ arxiv.org/abs](https://arxiv.org/abs/2011.13471)) and **Maybenot** ([↗ arxiv.org/abs](https://arxiv.org/abs/2304.09510)) — **and Maybenot is what Mullvad's DAITA actually ships**, so you can read the paper and then use the product.

**Flow correlation — the end-to-end attack that two hops cannot prevent:**
🔴 **Murdoch & Danezis, "Low-Cost Traffic Analysis of Tor"** (IEEE S&P 2005) — the founding result. **Start here** · [↗ murdoch.is/papers](https://murdoch.is/papers/oakland05torta.pdf)
🔴 **Nasr, Bahramali, Houmansadr, "DeepCorr"** (CCS 2018) — **96% accuracy versus 4% for statistical methods.** Deep learning collapsed the noise tolerance that protected Tor flows, and **this is the attack your threat model explicitly does not defend against** · [↗ arxiv.org/abs](https://arxiv.org/abs/1808.07285)
**DeepCoFFEA** (IEEE S&P 2022) — fixes DeepCorr's quadratic cost, making flow correlation scale to Tor-sized flow sets · [↗ doi.org/10.1109](https://doi.org/10.1109/SP46214.2022.9833801)

### F.6 · Accountable anonymity — the thing Tor structurally cannot do

> Scoped to `NEXT.md` this year, but **you must be able to talk about it**, because "Tor cannot ban anyone" is a claim in your own problem statement and an interviewer will ask what you would do instead.

| Resource | Why | Link |
|---|---|---|
| 🔴 **Davidson, Goldberg, Sullivan, Tankersley, Valsorda, "Privacy Pass"** (PoPETs 2018) | The origin paper: 1-RTT VOPRF tokens letting Tor and VPN users stop re-solving CAPTCHAs | [↗ petsymposium.org/2018](https://www.petsymposium.org/2018/files/papers/issue3/popets-2018-0026.pdf) |
| **RFC 9576** (architecture) · **RFC 9577** (HTTP scheme) · **RFC 9578** (issuance) | The deployed standard. Client/Origin/Issuer/Attester roles, the wire format, and both issuance variants | [↗ rfc-editor.org/info](https://www.rfc-editor.org/info/rfc9576/) · [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9577.html) · [↗ datatracker.ietf.org/doc](https://datatracker.ietf.org/doc/rfc9578/) |
| **Cloudflare, "Privacy Pass — The Math"** | The most approachable explanation of the blinding and unblinding. **On-ramp before the RFCs** | [↗ blog.cloudflare.com/privacy-pass-…](https://blog.cloudflare.com/privacy-pass-the-math/) |
| **Chaum, "Blind Signatures for Untraceable Payments"** (CRYPTO '82) | **Four pages**, and the origin of every unlinkable token in this section | [↗ doi.org/10.1007](https://doi.org/10.1007/978-1-4757-0602-4_18) |
| 🔴 **Tsang, Kapadia, Cornelius, Smith, "Nymble: Blocking Misbehaving Users in Anonymizing Networks"** (IEEE TDSC 2011) | **The canonical "block abusers without deanonymising them" design** — and the trusted-third-party cost that makes it hard | [↗ homes.luddy.indiana.edu/kapadia](https://homes.luddy.indiana.edu/kapadia/papers/nymble-tdsc.pdf) |
| **BLAC** (CCS 2007) | Removes Nymble's TTP at the cost of proofs linear in the blacklist. **Defines the subfield's core tradeoff** | [↗ cs.indiana.edu/~kapadia](https://www.cs.indiana.edu/~kapadia/papers/blac.pdf) |
| **Tor Abuse FAQ** | 🔴 **The operational counterpart to all of the above: what exit-relay abuse actually looks like, and why IP blocking fails.** Read it to understand the problem before the cryptography | [↗ support.torproject.org/abuse](https://support.torproject.org/abuse/) |
| **ARC — Anonymous Rate-Limited Credentials** (IETF draft) | **NEWER** — extends Privacy Pass from one-shot tokens to rate-limited credentials. The standardisation frontier | [↗ datatracker.ietf.org/doc](https://datatracker.ietf.org/doc/draft-ietf-privacypass-arc-protocol/) |

### F.7 · Measuring your own network without betraying its users — Level 7

| Resource | Why | Link |
|---|---|---|
| 🔴 **Jansen & Johnson, "Safely Measuring Tor" (PrivCount)** (CCS 2016) | **The foundational system for differentially-private, secret-shared aggregation across relays.** This is what your telemetry plane is modelled on | [↗ robgjansen.com/publications](https://www.robgjansen.com/publications/privcount-ccs2016.html) |
| **Elahi, Danezis, Goldberg, "PrivEx"** (CCS 2014) | PrivCount's predecessor — distributed DP plus secure aggregation for exit statistics | [↗ cypherpunks.ca/~iang](https://cypherpunks.ca/~iang/pubs/privex-ccs14.pdf) |
| **Mani, Wilson-Brown, Jansen, Johnson, Sherr, "Understanding Tor Usage with Privacy-Preserving Measurement"** (IMC 2018) | **The worked example** — the largest safe measurement study of what Tor is actually used for | [↗ robgjansen.com/publications](https://www.robgjansen.com/publications/torusage-imc2018.html) |
| 🔴 **Corrigan-Gibbs & Boneh, "Prio"** (NSDI 2017) | SNIPs make client-input validation cheap enough for real telemetry at scale | [↗ usenix.org/system](https://www.usenix.org/system/files/conference/nsdi17/nsdi17-corrigan-gibbs.pdf) |
| **DAP** and **VDAF** (IETF drafts) | The protocol and crypto layers standardising Prio-style two-aggregator telemetry. ⚠️ **Both are still Internet-Drafts, not RFCs — anyone citing "the PPM RFC" is wrong** | [↗ datatracker.ietf.org/doc](https://datatracker.ietf.org/doc/draft-ietf-ppm-dap/) · [↗ datatracker.ietf.org/doc](https://datatracker.ietf.org/doc/draft-irtf-cfrg-vdaf/) |
| **Divvi Up** (ISRG) | The production DAP deployment from the Let's Encrypt people — **privacy-preserving telemetry actually running** | [↗ divviup.org](https://divviup.org/) |
| **Dwork, McSherry, Nissim, Smith, "Calibrating Noise to Sensitivity"** (TCC 2006) | The original: sensitivity, the Laplace mechanism, the ε your budget is denominated in | [↗ journalprivacyconfidentiality.org…](https://journalprivacyconfidentiality.org/index.php/jpc/article/download/405/388) |
| **Dwork & Roth, *The Algorithmic Foundations of Differential Privacy*** | Chapters 1–3 are the grounding. ⚠️ *The widely circulated `cis.upenn.edu` PDF link now 404s* | [↗ doi.org/10.1561](https://doi.org/10.1561/0400000042) |

### F.8 ⛓ THE SPINE — why Tor is slow, and what fixed it

> **Read in order, against *Once is Never Enough* as a methodological check.** This is the argument your `tor-bench` comparison is joining, and you cannot make an honest performance claim without it.

| # | Read | Why | Link |
|---|---|---|---|
| **1** | 🔴 **Dingledine & Murdoch, "Performance Improvements on Tor, or, Why Tor is Slow"** (2009) | **The agenda-setting document**, enumerating six root causes. Nearly all later work responds to one of its sections | [↗ research.torproject.org/techrepor…](https://research.torproject.org/techreports/performance-2009-11-09.pdf) |
| **2** | **Jansen et al., "Never Been KIST"** (USENIX Security 2014) | Congestion lives in **egress kernel socket buffers**; real-time TCP-state-informed scheduling fixes it. **KIST shipped in Tor** | [↗ usenix.org/system](https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-jansen.pdf) |
| **3** | 🔴 **Proposal 324: RTT-based Congestion Control** + the deployment post | **The single biggest reason Tor was slow, and its fix** — this removed the ~500 KB/s per-circuit ceiling. **Essential context before you benchmark against Tor: if you compare against a pre-0.4.7 Tor you are comparing against a system that no longer exists** | [↗ spec.torproject.org/proposals](https://spec.torproject.org/proposals/324-rtt-congestion-control.html) · [↗ blog.torproject.org/congestion-co…](https://blog.torproject.org/congestion-contrl-047/) |
| **4** | **Proposal 329: Conflux (traffic splitting)** | Tor's deployed multipath design — two circuits to a common exit, lower-RTT leg preferred. **The biggest recent latency win.** ⚠️ *There is no Tor blog post on Conflux; the proposal is the canonical source* | [↗ spec.torproject.org/proposals](https://spec.torproject.org/proposals/329-traffic-splitting.html) |
| **✅** | 🔴 **Jansen, Tracey, Goldberg, "Once is Never Enough: Foundations for Sound Statistical Inference in Tor Network Experimentation"** (USENIX Security 2021) | **A methodological indictment of single-simulation Tor performance claims. Read it before trusting any speedup number in this section — including your own** | [↗ usenix.org/system](https://www.usenix.org/system/files/sec21-jansen.pdf) |

**Also:** **Tor Metrics** ([↗ metrics.torproject.org/onionperf-…](https://metrics.torproject.org/onionperf-latencies.html)) — the canonical longitudinal measurement of how slow Tor actually is, **and your baseline for every claim you make** · **PeerFlow** (PoPETs 2017) — 🔴 bandwidth measurement is a *security* problem, not just an accuracy one · **sbws** — the deployed bandwidth scanner and why Torflow was replaced · **"Point Break"** (USENIX Security 2019) — **$2.8K/month against Tor's scanners cut median client download rate by 80%**.

### F.9 · The deployed comparables — what "it actually shipped" looks like

**Apple iCloud Private Relay** (whitepaper, platform security guide, WWDC talks) and **Cloudflare's account of running its second hop** — see §IV.E.1, the whole of which belongs to this department too.

| Resource | Why | Link |
|---|---|---|
| **Singanamalla et al., "Oblivious DNS over HTTPS"** (PoPETs 2021) | The peer-reviewed design and performance evaluation — 🔴 **it measures the real latency cost of an extra proxy hop**, which is the number your own architecture lives or dies on | [↗ petsymposium.org/popets](https://petsymposium.org/popets/2021/popets-2021-0085.pdf) |
| **RFC 9230 (ODoH)** · **RFC 9458 (OHTTP)** · **RFC 9298 (CONNECT-UDP)** | The normative specs for the family your design sits in | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9230.html) · [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9458.html) · [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc9298.html) |
| **Donenfeld, "WireGuard: Next Generation Kernel Network Tunnel"** (NDSS 2017) | The data-plane primitive nearly every modern relay mesh builds on. **NoiseIK, cryptokey routing, under 4,000 lines of code** — read it as a lesson in how small a correct thing can be | [↗ wireguard.com/papers](https://www.wireguard.com/papers/wireguard.pdf) |
| **Tailscale DERP servers** | The relay design: HTTPS/443 packet forwarding keyed by destination public key, **never seeing plaintext** | [↗ tailscale.com/kb](https://tailscale.com/kb/1232/derp-servers) |
| 🔴 **Mullvad DAITA** | **A commercially deployed website-fingerprinting defence** — constant packet sizes and bidirectional cover traffic. Rare real-world deployment of padding research, built on Maybenot. **Read the product page and the paper together and judge whether the claims hold** | [↗ mullvad.net/en](https://mullvad.net/en/vpn/daita) |
| **Mullvad Browser** | 🔴 *"Tor Browser without the Tor network."* **The instructive separation of the fingerprinting-resistance layer from the relay layer — and the exact reason you do not touch the browser** | [↗ mullvad.net/en](https://mullvad.net/en/browser) · [↗ blog.torproject.org/releasing-mul…](https://blog.torproject.org/releasing-mullvad-browser/) |
| **Google IP Protection** (Privacy Sandbox) | Two-hop design plus RSA blind signatures to unlink traffic from accounts — **the closest browser-integrated analogue to Private Relay, and a live competitor to your premise** | [↗ privacysandbox.google.com/protect…](https://privacysandbox.google.com/protections/ip-protection) · [↗ github.com/GoogleChrome](https://github.com/GoogleChrome/ip-protection) |
| **INVISV Relay / Pretty Good Phone Privacy** | A multi-party relay that also addressed IMSI-based mobile tracking. 🔴 **Instructive as a cautionary case — the service wound down in June 2024.** Read it when you are tempted to plan a public launch | [↗ invisv.com](https://invisv.com/) |
## V.D 🔴 DEPARTMENT OF PRIVACY RELAY ENGINEERING

> **The core discovery of this curriculum's research: almost the entire production reference architecture for Adyton has been published, in public, by the companies that operate it.** Cloudflare runs the egress hop of iCloud Private Relay and has written about nearly every layer of it. Apple published the design document. Tor publishes its proposals. Signal publishes its censorship-circumvention post-mortems.
>
> **You are not working without a reference implementation. You are working without an excuse.**

### E.1 · The deployed two-hop relay — read this before you design anything

| Resource | Why it matters | Link |
|---|---|---|
| 🔴 **iCloud Private Relay Overview** (Apple, Dec 2021, PDF) | **The canonical design document for the system Adyton is a cousin of.** Ingress vs egress proxy, RSA blind-signature auth tokens, and the property that no single party sees both IP and destination. **Week 7 reading, and you will return to it all year** | [↗ apple.com/icloud](https://www.apple.com/icloud/docs/iCloud_Private_Relay_Overview_Dec2021.pdf) |
| **iCloud Private Relay security** (Apple Platform Security) | Token issuance, key separation, DNS handling — the security-engineering framing | [↗ support.apple.com/guide](https://support.apple.com/guide/security/icloud-private-relay-security-secad8ce3233/web) |
| 🔴 **iCloud Private Relay: What Cloudflare Customers Need to Know** | **Cloudflare's own account of operating the egress hop of somebody else's two-hop relay.** The other half of the design document above | [↗ blog.cloudflare.com/icloud-privat…](https://blog.cloudflare.com/icloud-private-relay/) |
| 🔴 **Ready, set, relay: Protect app traffic with network relays** (WWDC23) | **The closest thing to an official "build a relay client" tutorial that exists**, including chaining multiple relay hops in application code | [↗ developer.apple.com/videos](https://developer.apple.com/videos/play/wwdc2023/10002/) |
| **`ProxyConfiguration.RelayHop`** (Apple API reference) | A real, shipping, multi-hop relay API. **Read it as a design study for your own `adyton identity` interface** | [↗ developer.apple.com/documentation](https://developer.apple.com/documentation/network/proxyconfiguration/relayhop) |
| **Prepare your network for iCloud Private Relay** | The operational contract: port 443 QUIC/TLS 1.3, `mask.icloud.com`, and a public egress geo-feed | [↗ developer.apple.com/icloud](https://developer.apple.com/icloud/prepare-your-network-for-icloud-private-relay/) |
| 🔴 **Measuring Apple's iCloud Private Relay** (AsiaCCS '23) | **Peer-reviewed independent measurement: did the design actually work?** The model for how your own system should eventually be evaluated by someone who is not you | [↗ people.cs.umass.edu/~amir](https://people.cs.umass.edu/~amir/papers/AsiaCCS23-Private-Relay.pdf) |
| **An investigation into Apple's new Relay network** (APNIC, 2023) | Independent measurement of the deployed topology and routing | [↗ blog.apnic.net/2023](https://blog.apnic.net/2023/01/25/an-investigation-into-apples-new-relay-network/) |

### E.2 · MASQUE — the tunnelling primitive you should probably be using

> 🔴 **This is the single most important thing the research turned up, and it changes a design decision.** Adyton's original plan tunnels over raw per-hop QUIC. **MASQUE — CONNECT-UDP and CONNECT-IP over HTTP/3 — is the standardised way to do exactly that**, it is what Cloudflare replaced WireGuard with in WARP, it is what Apple's relays speak, and traffic shaped like HTTP/3 survives middleboxes that eat custom UDP. **Read these in Week 28 and write an ADR either adopting it or justifying why not.**

| Resource | Why | Link |
|---|---|---|
| 🔴 **Unlocking QUIC's proxying potential with MASQUE** (Cloudflare, 2022) | The clearest explanation of CONNECT-UDP and CONNECT-IP anywhere | [↗ blog.cloudflare.com/unlocking-qui…](https://blog.cloudflare.com/unlocking-quic-proxying-potential/) |
| **Donning a MASQUE: building a new protocol into Cloudflare WARP** (2023) | **Replacing WireGuard with MASQUE in a shipping consumer client.** The migration story | [↗ blog.cloudflare.com/masque-buildi…](https://blog.cloudflare.com/masque-building-a-new-protocol-into-cloudflare-warp/) |
| **Zero Trust WARP: tunneling with a MASQUE** (2024) | Why HTTP/3-shaped tunnels survive middleboxes better than custom UDP — **a censorship-resistance argument as much as a compatibility one** | [↗ blog.cloudflare.com/zero-trust-wa…](https://blog.cloudflare.com/zero-trust-warp-with-a-masque/) |
| **RFC 9298 — Proxying UDP in HTTP (CONNECT-UDP)** | The normative spec | [↗ datatracker.ietf.org/doc](https://datatracker.ietf.org/doc/rfc9298/) |
| **draft-ietf-masque-connect-ip** | Full IP tunnelling over HTTP/3 — the VPN-grade sibling | [↗ datatracker.ietf.org/doc](https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ip/13/) |
| **A Primer on Proxies** (Cloudflare, 2022) | Forward / reverse / transparent taxonomy and the trust model of each. **Required vocabulary before you write a design doc** | [↗ blog.cloudflare.com/a-primer-on-p…](https://blog.cloudflare.com/a-primer-on-proxies/) |

### E.3 · Oblivious protocols — the "separate who from what" principle

| Resource | Why | Link |
|---|---|---|
| 🔴 **Helping build the next generation of privacy-preserving protocols** (Cloudflare, 2020) | **Frames the single principle underneath every system in this department:** separate *who you are* from *what you are asking for*, and make sure no one party holds both | [↗ blog.cloudflare.com/next-generati…](https://blog.cloudflare.com/next-generation-privacy-protocols/) |
| **Improving DNS Privacy with Oblivious DoH** (2020) | Layered encryption plus a non-colluding proxy so the resolver never sees client IPs. **Adyton's DNS story should be argued against this one** | [↗ blog.cloudflare.com/oblivious-dns](https://blog.cloudflare.com/oblivious-dns/) |
| **Privacy Gateway: a privacy-preserving proxy built on Internet standards** (2022) | A production OHTTP relay: HPKE, the relay/gateway split, and the operational realities | [↗ blog.cloudflare.com/building-priv…](https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/) |
| 🔴 **Stronger than a promise: proving Oblivious HTTP privacy properties** (2022) | **What OHTTP actually guarantees versus what operators merely promise.** The distinction your own honesty statement lives or dies on | [↗ blog.cloudflare.com/stronger-than…](https://blog.cloudflare.com/stronger-than-a-promise-proving-oblivious-http-privacy-properties/) |
| **RFC 9458 — Oblivious HTTP** | Unlinkability via a relay that cannot read and a gateway that cannot identify | [↗ datatracker.ietf.org/doc](https://datatracker.ietf.org/doc/rfc9458/) |
| **Privacy Pass: upgrading to the latest protocol version** (2024) | Current IETF Privacy Pass — VOPRF and Private Access Tokens — as actually deployed. **This is the answer to the thing Tor structurally cannot do, and it is `NEXT.md`'s first item** | [↗ blog.cloudflare.com/privacy-pass-…](https://blog.cloudflare.com/privacy-pass-standard/) |
| **Introducing the Cloudflare Onion Service** (2018) | Real Tor onion services at CDN scale, including key handling and load balancing | [↗ blog.cloudflare.com/cloudflare-on…](https://blog.cloudflare.com/cloudflare-onion-service/) |
| 🔴 **Partnering to deploy Oblivious HTTP and Prio in Firefox** (Mozilla, 2023) | **A real OHTTP deployment with Fastly as the relay, plus DAP/Prio for telemetry — directly analogous to your Level 7 telemetry plane** | [↗ blog.mozilla.org/en](https://blog.mozilla.org/en/products/firefox/partnership-ohttp-prio/) |
| **Testing Privacy-Preserving Telemetry with Prio** (Mozilla, 2018) | Secret-shared telemetry across two non-colluding servers | [↗ hacks.mozilla.org/2018](https://hacks.mozilla.org/2018/10/testing-privacy-preserving-telemetry-with-prio/) |
| **STAR: privacy-preserving data collection** (Brave, 2022) | k-anonymity via threshold secret sharing **without Prio's non-collusion assumption.** Read both and pick | [↗ brave.com/privacy-updates](https://brave.com/privacy-updates/19-star/) |

### E.4 · Running a relay fleet — the operational half

| Resource | Why | Link |
|---|---|---|
| 🔴 **Cloudflare servers don't own IPs anymore — so how do they connect?** (2022) | **Egress IP assignment, port allocation, soft-unicast. This is the hard part of relay egress and almost nobody writes about it** | [↗ blog.cloudflare.com/cloudflare-se…](https://blog.cloudflare.com/cloudflare-servers-dont-own-ips-anymore/) |
| **Oxy: Cloudflare's Rust-based next-generation proxy framework** (2023) | 🔴 **The framework behind the iCloud Private Relay second hop** | [↗ blog.cloudflare.com/introducing-o…](https://blog.cloudflare.com/introducing-oxy/) |
| **From IP packets to HTTP: the many faces of Oxy** (2023) | Every OSI layer it proxies and the socket/tunnel modes required | [↗ blog.cloudflare.com/from-ip-packe…](https://blog.cloudflare.com/from-ip-packets-to-http-the-many-faces-of-our-oxy-framework/) |
| **How we built Pingora** (2022) and **open-sourcing it** (2024) | Why NGINX's worker model failed at scale; a multithreaded Rust proxy with connection reuse and zero-downtime upgrade. **Read for the architecture, not the language** | [↗ blog.cloudflare.com/how-we-built-…](https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/) · [↗ blog.cloudflare.com/pingora-open-…](https://blog.cloudflare.com/pingora-open-source/) |
| **How to build your own VPN, or: the history of WARP** (2025) | **Seven years of protocol and topology decisions — the arc this curriculum is walking** | [↗ blog.cloudflare.com/how-to-build-…](https://blog.cloudflare.com/how-to-build-your-own-vpn-or-the-history-of-warp/) |
| **Introducing WARP** (2019) | BoringTun userspace WireGuard, anycast ingress, mobile roaming constraints | [↗ blog.cloudflare.com/1111-warp-bet…](https://blog.cloudflare.com/1111-warp-better-vpn/) |
| **Accelerating UDP packet transmission for QUIC** (2020) | GSO and `sendmmsg` batching. 🔴 **The difference between a toy QUIC relay and one that saturates a NIC** | [↗ blog.cloudflare.com/accelerating-…](https://blog.cloudflare.com/accelerating-udp-packet-transmission-for-quic/) |
| **Enhance UDP Throughput for QUIC and HTTP/3 on Linux** (Tailscale, 2023) | 🔴 **Directly applicable GSO/GRO tuning for a QUIC datapath** | [↗ tailscale.com/blog](https://tailscale.com/blog/quic-udp-throughput) |
| **Enhancing Userspace with Kernel Interfaces** (Tailscale, 2022) | TSO/GRO + `sendmmsg` gave wireguard-go **2.2×**. The best userspace-VPN datapath write-up anywhere | [↗ tailscale.com/blog](https://tailscale.com/blog/throughput-improvements) |
| **Surpassing 10 Gb/s with Tailscale** (2023) | UDP segmentation offload pushing userspace WireGuard past the in-kernel implementation | [↗ tailscale.com/blog](https://tailscale.com/blog/more-throughput) |
| 🔴 **Introducing Quicksilver: configuration distribution at Internet scale** (2020) + **v2** (2025) | **The "why we did NOT use Raft" counterpoint to your Level 7.** Globally replicated KV with a monotonic log and async replication instead of consensus. **Read it, then defend your Raft choice in ADR-0006 against it** | [↗ blog.cloudflare.com/introducing-q…](https://blog.cloudflare.com/introducing-quicksilver-configuration-distribution-at-internet-scale/) · [↗ blog.cloudflare.com/quicksilver-v…](https://blog.cloudflare.com/quicksilver-v2-evolution-of-a-globally-distributed-key-value-store-part-1/) |
| **Tailnet lock** (2022) + **GA** (2025) | An Ed25519 signing chain so a **compromised coordination server cannot inject nodes.** 🔴 **This is the attack on your own directory, and its published mitigation** | [↗ tailscale.com/blog](https://tailscale.com/blog/tailnet-lock) · [↗ tailscale.com/blog](https://tailscale.com/blog/tailnet-lock-ga) |
| **Key Management in the Tailscale Control Protocol** (2021) | Machine keys vs node keys; how the network map is signed and distributed | [↗ tailscale.com/blog](https://tailscale.com/blog/tailscale-key-management) |
| **Now with more DERP** (2022) · **Peer Relays beta** (2025) / **GA** (2026) | Running and scaling a global relay fleet; then **moving to user-operated relays** — the exact transition Adyton's `NEXT.md` contemplates | [↗ tailscale.com/blog](https://tailscale.com/blog/more-derp) · [↗ tailscale.com/blog](https://tailscale.com/blog/peer-relays-ga) |
| **How Tailscale is improving NAT traversal, parts 1–3** (2025) | **Five years on: what actually broke, what changed, and the cloud-NAT case that is hardest** | [↗ tailscale.com/blog](https://tailscale.com/blog/nat-traversal-improvements-pt-1) · [↗ tailscale.com/blog](https://tailscale.com/blog/nat-traversal-improvements-pt-2-cloud-environments) |
| **Kubernetes networking problems due to conntrack** (loveholidays, 2020) | 🔴 **Conntrack table exhaustion under many concurrent connections — exactly the failure a relay fleet on k8s will hit.** Level 8 incident material | [↗ deploy.live/blog](https://deploy.live/blog/kubernetes-networking-problems-due-to-the-conntrack/) |

### E.5 · Tor — the system you are honest about

| Resource | Why | Link |
|---|---|---|
| 🔴 **All Tor proposals, by status** | **The single best reading index for this entire curriculum.** Every design decision in a production anonymity network, argued in public | [↗ spec.torproject.org/proposals](https://spec.torproject.org/proposals/BY_STATUS.html) |
| **Announcing Arti, a pure-Rust Tor implementation** (2021) | 🔴 **~half of Tor's tracked security bugs since 2016 were memory-safety issues impossible in safe Rust.** Read this *the same week* you commit to C++, and let it make you uncomfortable — that discomfort is what the sanitizer apparatus answers | [↗ blog.torproject.org/announcing-ar…](https://blog.torproject.org/announcing-arti/) |
| **Arti 1.0.0: ready for production** (2022) · **2.x relay and directory-authority work** (2026) | The C→Rust rewrite as staged project planning, and the current state of Arti as a relay | [↗ blog.torproject.org/arti_100_rele…](https://blog.torproject.org/arti_100_released/) · [↗ blog.torproject.org/arti_2_0_0_re…](https://blog.torproject.org/arti_2_0_0_released/) |
| 🔴 **Congestion Control Arrives in Tor 0.4.7** (2022) + **Proposal 324** | RTT-based congestion control lifting the ~500 KB/s per-circuit ceiling. **This is the single biggest reason Tor was slow, and its fix. Essential context for your `tor-bench` comparison** | [↗ blog.torproject.org/congestion-co…](https://blog.torproject.org/congestion-contrl-047/) · [↗ spec.torproject.org/proposals](https://spec.torproject.org/proposals/324-rtt-congestion-control.html) |
| **Proposal 329: Conflux (traffic splitting)** | Splitting a stream across two pre-built circuits — multipath over an overlay | [↗ spec.torproject.org/proposals](https://spec.torproject.org/proposals/329-traffic-splitting.html) |
| 🔴 **Announcing the Vanguards Add-On** (2018) + **Vanguards in Arti** (2024) | The layered "2-3-8" guard topology and **guard-discovery attacks.** Direct prior art for your Level 9 | [↗ blog.torproject.org/announcing-va…](https://blog.torproject.org/announcing-vanguards-add-onion-services/) · [↗ blog.torproject.org/announcing-va…](https://blog.torproject.org/announcing-vanguards-for-arti/) |
| **Introducing Proof-of-Work Defense for Onion Services** (2023) + **How to stop the onion denial** (2020) | 🔴 **Read them together: the design discussion three years before the thing shipped, then the thing.** Tokens vs PoW, attacker asymmetry — and it is the same abuse-handling problem Privacy Pass answers differently |  [↗ blog.torproject.org/introducing-p…](https://blog.torproject.org/introducing-proof-of-work-defense-for-onion-services/) · [↗ blog.torproject.org/stop-the-onio…](https://blog.torproject.org/stop-the-onion-denial/) |
| **Sustaining Snowflake operations** (2023) | 5k → 75k users during censorship events, and what it cost in hardware and bandwidth. **The operational reality of running this for real** | [↗ blog.torproject.org/snowflake-dai…](https://blog.torproject.org/snowflake-daily-operations/) |
| **Is Tor still safe to use?** (2024) | A case study in **communicating threat honestly to users** — which is a skill this project needs as much as any technical one | [↗ blog.torproject.org/tor-is-still-…](https://blog.torproject.org/tor-is-still-safe/) |
| **Tor VPN Beta for Android** (2026) | Packaging an onion-routing client as a full-tunnel VPN — the productisation problem you are also solving | [↗ blog.torproject.org/tor-vpn-beta](https://blog.torproject.org/tor-vpn-beta/) |

### E.6 · Signal — crypto engineering, and the censorship arc

| Resource | Why | Link |
|---|---|---|
| **Forward Secrecy for Asynchronous Messages** (2013) | The prekey concept that became X3DH — authenticated DH when the peer is offline | [↗ signal.org/blog](https://signal.org/blog/asynchronous-security/) |
| **Advanced cryptographic ratcheting** (2013) | The original Double Ratchet announcement | [↗ signal.org/blog](https://signal.org/blog/advanced-ratcheting/) |
| **Sealed sender** (2018) | Sender certificates and delivery tokens — **the canonical metadata-minimisation design, and the thing Adyton explicitly does not attempt** | [↗ signal.org/blog](https://signal.org/blog/sealed-sender/) |
| **PQXDH** (2023) and **SPQR** (2025) | Hybrid post-quantum key agreement, and extending PQ protection from the handshake into the ongoing ratchet | [↗ signal.org/blog](https://signal.org/blog/pqxdh/) · [↗ signal.org/blog](https://signal.org/blog/spqr/) |
| 🔴 **The three-part censorship arc — read in order** | **Doodles, stickers and censorship circumvention** (2016, domain fronting deployed) → **A letter from Amazon** (2018, domain fronting dies) → **Help users in Iran reconnect** (2021, TLS proxies resisting fingerprinting). **The best real-world narrative in this curriculum about a defence being built, working, and then being taken away** | [↗ signal.org/blog](https://signal.org/blog/doodles-stickers-censorship/) · [↗ signal.org/blog](https://signal.org/blog/looking-back-on-the-front/) · [↗ signal.org/blog](https://signal.org/blog/help-iran-reconnect/) |
| **Run a proxy** (2022) · **Proxy Please** (2024) | Volunteer-operated proxy distribution — running a fleet you do not control | [↗ signal.org/blog](https://signal.org/blog/run-a-proxy/) |
| 🔴 **Privacy is Priceless, but Signal is Expensive** (2023) | **Real infrastructure cost breakdown for a global privacy service.** Read it when you are tempted to imagine running Adyton publicly | [↗ signal.org/blog](https://signal.org/blog/signal-is-expensive/) |

### E.7 · The browser half — what Mullvad Browser is doing while you do the network

> **You do not modify the browser.** But you must understand precisely what it is doing, because your job is the half it explicitly does not do.

| Resource | Why | Link |
|---|---|---|
| 🔴 **Introducing State Partitioning** (Mozilla Hacks, 2021) | **The engineering-depth companion to Total Cookie Protection:** exactly what state exists in a browser, how it is keyed, and the compatibility escape hatches. **This is the list of things two of your compartments must not share** | [↗ hacks.mozilla.org/2021](https://hacks.mozilla.org/2021/02/introducing-state-partitioning/) |
| **Firefox 85 cracks down on supercookies** (2021) | Network-state partitioning: HTTP cache, **connection pools**, DNS cache, HSTS — per top-level site. 🔴 **Connection pools and TLS session tickets are the two your Level 4 leak suite must test** | [↗ blog.mozilla.org/security](https://blog.mozilla.org/security/2021/01/26/supercookie-protections/) |
| **Total Cookie Protection** (2021) and **by default worldwide** (2022) | The cookie-jar-per-site model, and what it takes to ship a breaking privacy default globally | [↗ blog.mozilla.org/security](https://blog.mozilla.org/security/2021/02/23/total-cookie-protection/) |
| **Firefox 79: redirect tracking** (2020) and **Brave: Debouncing** (2021) | Bounce tracking, and two different countermeasures. **Your compartments must survive a bounce chain** | [↗ blog.mozilla.org/security](https://blog.mozilla.org/security/2020/08/04/firefox-79-includes-protections-against-redirect-tracking/) · [↗ brave.com/privacy-updates](https://brave.com/privacy-updates/11-debouncing/) |
| 🔴 **Brave: Fingerprint randomization ("farbling")** (2020) and **Fingerprinting defenses 2.0** | **The opposing philosophy to Mullvad/Tor Browser's uniformity approach.** Randomise per-session per-site, versus make everyone identical. **You must be able to argue both sides — it is a great interview question and Level 4's ADR** | [↗ brave.com/privacy-updates](https://brave.com/privacy-updates/3-fingerprint-randomization/) · [↗ brave.com/privacy-updates](https://brave.com/privacy-updates/4-fingerprinting-defenses-2.0/) |
| 🔴 **Brave simplifies its fingerprinting protections** (2024) | **A published negative result: why their "strict" mode made users *more* identifiable.** The most valuable single article in this section, and exactly the intellectual honesty your own write-ups should imitate | [↗ brave.com/privacy-updates](https://brave.com/privacy-updates/28-sunsetting-strict-fingerprinting-mode/) |
| **Brave: Preventing pool-party attacks** (2021) | 🔴 **Exhaustible socket and connection pools as covert cross-site channels.** A side channel that defeats naive compartmentalisation — **add it to your leak suite** | [↗ brave.com/privacy-updates](https://brave.com/privacy-updates/13-pool-party-side-channels/) |
| **Brave: Fighting CNAME trickery** (2020) | DNS-level CNAME cloaking detection — why domain blocklists fail | [↗ brave.com/privacy-updates](https://brave.com/privacy-updates/6-cname-trickery/) |
| **Brave: Unlinkable bouncing** (2022) · **Ephemeral third-party storage** (2021) | Giving a persistent tracker a fresh unlinkable identity each visit | [↗ brave.com/privacy-updates](https://brave.com/privacy-updates/16-unlinkable-bouncing/) |
| **Brave: GPU fingerprinting protections** (2026) | Current-generation WebGL/WebGPU defences | [↗ brave.com/privacy-updates](https://brave.com/privacy-updates/38-webgl-webgpu-fingerprinting-protections/) |
| **Firefox expands fingerprint protections** (2025) | Current RFP state, and **how they measured a ~50% reduction in trackable users** — a methodology you can borrow | [↗ blog.mozilla.org/en](https://blog.mozilla.org/en/firefox/fingerprinting-protections/) |
| **DuckDuckGo: Most default browser tracking protection doesn't actually stop tracking** (2021) | 🔴 **A comparative measurement methodology for evaluating defences — including your own** | [↗ spreadprivacy.com/browser-privacy…](https://spreadprivacy.com/browser-privacy-protection/) |
| **DuckDuckGo: Is private browsing really private?** (2022) | Clear threat-model framing of what incognito does and does not protect. **Good writing to imitate** | [↗ spreadprivacy.com/is-private-brow…](https://spreadprivacy.com/is-private-browsing-really-private/) |

---

## V.E DEPARTMENT OF CONSENSUS & FORMAL METHODS

> Level 7. **Distributed systems is 48.9% of your backend postings and 57.0% of backend+infra — the highest-frequency technical skill in your corpus.**

| Resource | Link |
|---|---|
| 🔴 **Raft — the EXTENDED paper.** §5 in full, §6 carefully. **The conference version omits crucial detail; assign this one** | [↗ raft.github.io/raft.pdf](https://raft.github.io/raft.pdf) |
| MIT's mirror of the same | [↗ pdos.csail.mit.edu/6.824](https://pdos.csail.mit.edu/6.824/papers/raft-extended.pdf) |
| **The Raft site** — the interactive visualization, talks, 100+ implementations | [↗ raft.github.io](https://raft.github.io/) |
| 🔴 **Ongaro's PhD thesis** — everything the paper omits: membership changes, log compaction, client semantics, the correctness proof. **Read before implementing** | [↗ web.stanford.edu/~ouster](https://web.stanford.edu/~ouster/cgi-bin/papers/OngaroPhD.pdf) |
| **The Secret Lives of Data** — the animated walkthrough. **The best first exposure, W38 day one** | [↗ thesecretlivesofdata.com/raft](https://thesecretlivesofdata.com/raft/) |
| 🔴 **Students' Guide to Raft** (Gjengset) — catalogues the exact mistakes implementers make. **Read *while* implementing, not before** | [↗ thesquareplanet.com/blog](https://thesquareplanet.com/blog/students-guide-to-raft/) |
| 🔴 **The membership-change bug thread** — **the author announcing a safety bug in his own thesis's protocol, with the fix.** The single best document on Raft's subtle failure modes, and a lesson in intellectual honesty | [↗ groups.google.com/g](https://groups.google.com/g/raft-dev/c/t4xj6dJTP6E) |
| **etcd-io/raft** — the most battle-tested library; its separation of protocol logic from I/O is a masterclass in testable design | [↗ github.com/etcd-io](https://github.com/etcd-io/raft) · [↗ pkg.go.dev/go.etcd.io](https://pkg.go.dev/go.etcd.io/raft/v3) |
| **hashicorp/raft** — a contrasting design that owns its own I/O. **Read both and form an opinion** | [↗ github.com/hashicorp](https://github.com/hashicorp/raft) |
| **tikv/raft-rs** — how Raft scales to many groups | [↗ github.com/tikv](https://github.com/tikv/raft-rs) |
| 🔴 **raft.tla** — Ongaro's own TLA+ spec. **The bridge between this department and the next** | [↗ github.com/ongardie](https://github.com/ongardie/raft.tla) |
| **Jepsen: etcd 3.4.3** — what real consistency testing of a Raft system finds, and what "linearizable" does and does not buy you | [↗ jepsen.io/analyses](https://jepsen.io/analyses/etcd-3.4.3) |
| **Jepsen analyses index** — the best available catalogue of distributed-system failure case studies | [↗ jepsen.io/analyses](https://jepsen.io/analyses) |

### Formal methods, lite

| Resource | Link |
|---|---|
| 🔴 **Learn TLA+** (Hillel Wayne) — PlusCal-first, practical, no mathematical prerequisites. **The core curriculum** | [↗ learntla.com/core](https://learntla.com/core/index.html) |
| Advanced topics — refinement, liveness, model-size control | [↗ learntla.com/topics](https://learntla.com/topics/) |
| 🔴 **How AWS Uses Formal Methods** (Newcombe et al., CACM 2015) — **read first**, to understand why the hours are worth it. Real bugs in DynamoDB and S3 that testing could never have caught | [↗ lamport.azurewebsites.net/tla](https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf) |
| **Lamport's TLA+ video course** — the "why it is built this way" track | [↗ lamport.azurewebsites.net/video](https://lamport.azurewebsites.net/video/videos.html) |
| **Specifying Systems** (Lamport, free) — the reference for when the tools surprise you | [↗ lamport.azurewebsites.net/tla](https://lamport.azurewebsites.net/tla/book.html) |
| **TLC and the Toolbox** · **the Examples corpus** — the fastest way to learn idiomatic TLA+ | [↗ github.com/tlaplus](https://github.com/tlaplus/tlaplus) · [↗ github.com/tlaplus](https://github.com/tlaplus/Examples) |
| **The Business Case for Formal Methods** — the argument to make to a sceptical team | [↗ hillelwayne.com/post](https://www.hillelwayne.com/post/business-case-formal-methods/) |

---

## V.F DEPARTMENT OF OPERATIONS

> **The shell is what the screen reads.** AWS 48.9% · Kubernetes 30.4% · observability 22.0% · on-call 21.5%. This department runs in Level 8 and **it is never cut.**

| Resource | Link |
|---|---|
| 🔴 **Kubernetes The Hard Way** (Kelsey Hightower) — bootstrap a cluster component by component. **The only way to actually understand the control plane** | [↗ github.com/kelseyhightower](https://github.com/kelseyhightower/kubernetes-the-hard-way) |
| **Kubernetes Concepts** — Architecture, Workloads, Services | [↗ kubernetes.io/docs](https://kubernetes.io/docs/concepts/) |
| 🔴 **Kubernetes API Conventions** — spec/status, the reconciliation model, and why the API is shaped as it is. **The single best document for understanding Kubernetes' philosophy** | [↗ github.com/kubernetes](https://github.com/kubernetes/community/blob/main/contributors/devel/sig-architecture/api-conventions.md) |
| **Kubernetes API Concepts** — resource versions, watch semantics, pagination | [↗ kubernetes.io/docs](https://kubernetes.io/docs/reference/using-api/api-concepts/) |
| **KEPs** — every feature's design rationale **and its rejected alternatives.** The real architecture documentation | [↗ github.com/kubernetes](https://github.com/kubernetes/enhancements) |
| **The Kubebuilder Book** — controllers, CRDs, the reconcile loop | [↗ book.kubebuilder.io](https://book.kubebuilder.io/) |
| **A few things I've learned about Kubernetes** (Julia Evans) — an honest engineer's account of what is actually confusing | [↗ jvns.ca/blog](https://jvns.ca/blog/2017/06/04/learning-about-kubernetes/) |
| 🔴 **Kubernetes Failure Stories** — **read ten.** The highest learning-per-minute in the ecosystem | [↗ k8s.af](https://k8s.af/) |
| **cgroups v2 kernel docs** — the unified hierarchy and the CPU/memory/IO controllers that define every container limit you will ever debug | [↗ kernel.org/doc](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html) |

### The SRE books — free, and assigned by chapter

| Chapter | Why | Link |
|---|---|---|
| **SRE Ch. 4 — Service Level Objectives** | SLIs, SLOs, error budgets. **The chapter that changes how teams make decisions** | [↗ sre.google/sre-book](https://sre.google/sre-book/service-level-objectives/) |
| **SRE Ch. 6 — Monitoring Distributed Systems** | The four golden signals; the antidote to alert fatigue | [↗ sre.google/sre-book](https://sre.google/sre-book/monitoring-distributed-systems/) |
| 🔴 **SRE Ch. 21 — Handling Overload** | Graceful degradation, client throttling, criticality | [↗ sre.google/sre-book](https://sre.google/sre-book/handling-overload/) |
| 🔴 **SRE Ch. 22 — Addressing Cascading Failures** | Retry storms, thundering herds, death spirals. **Possibly the most valuable chapter in the book** | [↗ sre.google/sre-book](https://sre.google/sre-book/addressing-cascading-failures/) |
| **SRE Ch. 15 — Postmortem Culture** | The practice that turns incidents into engineering | [↗ sre.google/sre-book](https://sre.google/sre-book/postmortem-culture/) |
| **Workbook Ch. 2 — Implementing SLOs** | The how-to Ch. 4 leaves out; worked examples and error-budget policies | [↗ sre.google/workbook](https://sre.google/workbook/implementing-slos/) |
| **Workbook Ch. 4 — Monitoring** | Concrete patterns and anti-patterns | [↗ sre.google/workbook](https://sre.google/workbook/monitoring/) |
| *Full table of contents* | | [↗ sre.google/books](https://sre.google/books/) |

---

---

## V.G 🔴 DEPARTMENT OF MEASUREMENT & THE WEB

> **Level 2's department, and the one that makes your premise checkable.**
>
> 🔴 **Five findings from the current literature change how you build the crawler. Read this box before you write a line of it** — each one is a mistake most published studies make, and avoiding them is itself a contribution.

| # | The finding | What you do about it |
|---|---|---|
| **1** | 🔴 **Automated crawls miss ~45% of the fingerprinting sites real users encounter** — Annamalai et al. (WWW 2025) compared 30 users over 10 weeks against crawls of the same 3,000 sites. Login walls, bot detection and untriggered scripts hide the rest | **Report your headline as a lower bound, and say why in the abstract.** Cite this paper when you do |
| **2** | 🔴 **Bot detection biases your sample non-randomly.** Gundelach et al. (2026): headless Chromium hit a **15% soft-block rate vs 7%** otherwise; **Cloudflare blocked 37%, Akamai 26%**; and **header-level signals alone caused 75%** of headless-specific blocks. **83% of measurement papers never mention blocking at all** | **Spoof the headers** — it is cheap and it unblocks most of them. Then **measure and publish your own block rate by provider.** Almost nobody does this, and it is a publishable methodological note on its own |
| **3** | 🔴 **Tracking has moved first-party and server-side.** Böttger et al. (2026): **>54% of sites** now deploy first-party or server-side tracking and filter lists are *"largely inadequate"* against it | A crawler that counts third-party requests measures a **shrinking slice** of the problem. Add **CookieGraph-style first-party cookie analysis** and **CNAME resolution**, or your numbers describe 2016 |
| **4** | **Filter lists miss a large share of real trackers** — Fouad et al. (PETS 2020), invisible pixels | Your list-based labels **undercount**. Say so, and estimate by how much |
| **5** | 🔴 **Use Tranco and publish the pinned list ID.** Le Pochat et al. (NDSS 2019) showed a single HTTP request could move Alexa ranks | That one choice makes your study reproducible in a way most are not. **Every Tranco list gets a permanent citable ID** |

### G.1 · The measurement canon

| Resource | Why | Link |
|---|---|---|
| 🔴 **Englehardt & Narayanan, "Online Tracking: A 1-Million-Site Measurement and Analysis"** (CCS 2016) | **The paper whose methodology you are replicating at smaller scale and greater currency.** 15 measurement types, stateful and stateless tracking, cookie syncing — and it produced OpenWPM | slides [↗ senglehardt.com/presentations](https://senglehardt.com/presentations/2016_10_ccs_online_tracking.pdf) |
| **Acar et al., "The Web Never Forgets"** (CCS 2014) | The first large-scale measurement of **canvas fingerprinting, evercookies and cookie respawning** | [↗ esat.kuleuven.be/cosic](https://www.esat.kuleuven.be/cosic/publications/article-2457.pdf) |
| 🔴 **Web Almanac 2024 — Privacy chapter** | **95% of desktop and 94% of mobile sites carry at least one tracker; 27% carry more than ten.** Every query and figure published and reproducible, Apache 2.0. **Your baseline statistics, free** | [↗ almanac.httparchive.org/en](https://almanac.httparchive.org/en/2024/privacy) |
| 🔴 **Böttger et al., "From Third-Party to First-Party"** (arXiv 2026) | **The single most on-point paper for your thesis** — and the reason finding #3 above exists | [↗ arxiv.org/abs](https://arxiv.org/abs/2606.16720) |
| **Fouad, Santos, Laperdrix, "Server-Side Tracking"** (PETS 2024) | The blind spot every client-side crawler misses, and how to detect it | [↗ hal.science/hal-04617727v1](https://hal.science/hal-04617727v1/document) |
| **Sivan-Sevilla & Poudel, "Web Privacy based on Contextual Integrity"** (2024) | 🔴 **Frames tracking as *context collapse* — which is exactly the harm per-identity compartments address.** Useful framing for your README's opening | [↗ arxiv.org/abs](https://arxiv.org/abs/2412.16246) |
| **Singh et al., "Where in the World Are My Trackers?"** (IMC 2025) | Tracking varies by vantage point — **directly informs where you crawl from and where you place exits** | [↗ doi.org/10.1145](https://doi.org/10.1145/3730567.3764427) |

### G.2 · Cross-site linkage — the mechanism your graph is measuring

| Resource | Why | Link |
|---|---|---|
| 🔴 **Papadopoulos, Kourtellis, Markatos, "Cookie Synchronization: Everything You Always Wanted to Know But Were Afraid to Ask"** (WWW 2019) | **The reference cookie-sync measurement, and your Level 2 centrepiece.** Quantifies anonymity loss per ad impression (**~3.4 syncs**) and how identifiers diffuse | [↗ arxiv.org/abs](https://arxiv.org/abs/1805.10505) |
| 🔴 **Munir et al., "CookieGraph"** (CCS 2023) | **First-party cookies get synced to third parties on a large majority of sites — the mechanism that survives third-party cookie deprecation.** This is what finding #3 means in practice | [↗ arxiv.org/abs](https://arxiv.org/abs/2208.12370) |
| **Dimova et al., "The CNAME of the Game"** (PoPETs 2021) | CNAME cloaking: first-party-disguised third-party tracking. 🔴 **Resolve CNAMEs in your crawler or you will undercount** | [↗ esat.kuleuven.be/cosic](https://www.esat.kuleuven.be/cosic/publications/article-3303.pdf) |
| **Brave Research, "Measuring UID Smuggling in the Wild"** (IMC 2022) | Identifiers smuggled through URL parameters — **the link-decoration channel that defeats cookie blocking** | [↗ brave.com/research](https://brave.com/research/measuring-uid-smuggling-in-the-wild/) |
| 🔴 **Su, Shukla, Goel, Narayanan, "De-anonymizing Web Browsing Data with Social Networks"** (WWW 2017) | **"De-identified" browsing histories re-linked to named people via public social activity.** The strongest single argument that clickstream anonymisation fails — **quote this one in your demo** | [↗ doi.org/10.1145](https://doi.org/10.1145/3038912.3052714) |
| **Deuser, Passmann, Strufe, "Browsing Unicity"** (IEEE S&P 2020) | **How few observations are needed to single out one user** | [↗ doi.org/10.1109](https://doi.org/10.1109/sp40000.2020.00018) |
| **Brookman et al., "Cross-Device Tracking"** (PoPETs 2017) | 861 third-party domains collecting linkage-capable data; cross-device specialists on 34% of sites | [↗ crysp.petsymposium.org/popets](https://crysp.petsymposium.org/popets/2017/popets-2017-0020.pdf) |
| **Senol et al., "Leaky Forms"** (USENIX Sec 2022) | **Email addresses — the strongest cross-site identifier — exfiltrated before you press submit.** Dataset public | [↗ gunesacar.net/papers](https://gunesacar.net/papers/leaky-forms-usenix-sec-22.pdf) |

### G.3 · Fingerprinting — and the honesty that must come with it

| Resource | Why | Link |
|---|---|---|
| **Eckersley, "How Unique Is Your Web Browser?"** (PETS 2010) | Panopticlick: ≥18.1 bits of entropy. The origin of the field | [↗ pde.is/research](https://pde.is/research/2010panopticlick/) |
| **Laperdrix et al., "Browser Fingerprinting: A Survey"** (ACM TWEB 2020) | The reference survey — mechanics, vectors, defence taxonomy | [↗ arxiv.org/abs](https://arxiv.org/abs/1905.01051) |
| 🔴 **Gómez-Boix, Laperdrix, Baudry, "Hiding in the Crowd"** (WWW 2018) | **THE essential counterweight.** On 2M real fingerprints, **uniqueness is far lower than Panopticlick suggested**, especially on mobile. 🔴 **Cite this to stay honest — it argues partly against your own project's framing, and including it is what makes the rest credible** | [↗ hal.inria.fr/hal-01718234](https://hal.inria.fr/hal-01718234/document) |
| 🔴 **Annamalai, Bilogrevic, De Cristofaro, "Beyond the Crawl"** (WWW 2025) | **Read before designing your crawler.** The 45% finding | [↗ arxiv.org/abs](https://arxiv.org/abs/2502.01608) |
| **Bacis et al. (Google), "Assessing Web Fingerprinting Risk"** (WWW 2024) | Entropy measured across **tens of millions of real Chrome browsers** — the largest ground truth that exists | [↗ arxiv.org/abs](https://arxiv.org/abs/2403.15607) |
| 🔴 **Berke et al., "How Unique is Whose Web Browser?"** (PoPETs 2025) | **Lower-income users are more fingerprintable, and demographics are predictable from browser attributes.** A genuine equity argument for your project, and a strong paragraph in the README | [↗ arxiv.org/abs](https://arxiv.org/abs/2410.06954) |
| **Vastel et al., "FP-STALKER"** (IEEE S&P 2018) | Fingerprints change — this measures how long you can still **link** them across changes. *The linkability paper, not the uniqueness paper* | [↗ hal.inria.fr/hal-01652021](https://hal.inria.fr/hal-01652021/document) |
| 🔴 **Amin Azad et al., "Taming The Shape Shifter"** (DIMVA 2020) | **Anti-fingerprinting browsers are themselves detectable, which can make you *more* identifiable.** The core "do defences actually work?" result, and the reason you do not fork the browser | [↗ hal.archives-ouvertes.fr/hal-0261…](https://hal.archives-ouvertes.fr/hal-02612461/document) |
| **Laor et al., "DRAWNAPART"** (NDSS 2022) | **WebGL fingerprinting at the physical-GPU level — survives a browser reinstall.** The hardest vector, and one you cannot defend against at the network layer. *Say so* | [↗ hal.inria.fr/hal-03526240](https://hal.inria.fr/hal-03526240/document) |

### G.4 · The tools — read the methodology papers before picking one

| Tool | What it is | Link |
|---|---|---|
| 🔴 **OpenWPM** | The de facto standard Firefox+Selenium privacy crawler, actively maintained (**v0.37.0 pins Firefox 155**). **Cite the exact version** | [↗ github.com/openwpm](https://github.com/openwpm/OpenWPM) |
| **Tracker Radar Collector** (DuckDuckGo) | The **Puppeteer/Chromium** crawler that generates Tracker Radar. The best-documented production-grade Chromium alternative | [↗ github.com/duckduckgo](https://github.com/duckduckgo/tracker-radar-collector) |
| 🔴 **Blacklight Query** (The Markup) | **Batch-scans a URL list from the terminal with zero code.** The fastest path to a credible first result — run it in Week 9 while you build the real thing | [↗ github.com/the-markup](https://github.com/the-markup/blacklight-query) |
| 🔴 **WebREC / `.web` bundles** (Brave, USENIX Sec 2025) | **Reproducible, archivable web measurements.** 48% of surveyed papers could have reused archives without re-crawling. **Solves the thing most crawl studies fail at** | [↗ brave.com/research](https://brave.com/research/files/webrec-usenix-2025.pdf) · [↗ github.com/brave](https://github.com/brave/pagegraph-crawl) |
| **Privacy Pioneer crawler** (PoPETs 2024) | Detects **what personal data** is collected, not just which trackers are present | [↗ github.com/privacy-tech-lab](https://github.com/privacy-tech-lab/privacy-pioneer-web-crawler) |
| 🔴 **Gundelach et al., "Detecting Bot Detection"** (2026) | **The most important paper for your crawler design.** Finding #2 above | [↗ arxiv.org/abs](https://arxiv.org/abs/2606.14525) |
| **Stafeev & Pellegrino, "SoK: State of the Krawlers"** (USENIX Sec 2024) | How crawl *strategy* — depth, navigation policy — changes what you see | [↗ cispa.de/en](https://www.cispa.de/en/stafeev-webcrawlers) |
| **Jueckstock et al., "Towards Realistic and Reproducible Web Crawl Measurements"** (WWW 2021) | Vantage point and statefulness materially change measured tracking | [↗ kapravelos.com/publications](https://www.kapravelos.com/publications/vpc-www21.pdf) |

**Lists and samples:** 🔴 **Tranco** — [↗ tranco-list.eu](https://tranco-list.eu/), **free, daily, and every list has a permanent citable ID** · **EasyList / EasyPrivacy** — [↗ easylist.to](https://easylist.to/), **dual GPLv3 / CC BY-SA, the permissive option** · **Disconnect** and **DuckDuckGo Tracker Radar** — richer (ownership, prevalence, categories) but ⚠️ **CC BY-NC-SA, non-commercial only** · **third-party-web** — origin→company mapping from monthly crawls of ~4M sites, free · 🔴 **WhoTracks.Me** — **real-user data from 5M+ users and 1.5B page loads, free via `aws s3 sync --no-sign-request s3://data.whotracks.me/`.** The natural complement to the "crawls miss 45%" finding ⚠️ *licence not stated — confirm before redistributing*

### G.5 🔴 · Why the IP is the thing — the core of your premise

| Resource | Why | Link |
|---|---|---|
| 🔴🔴 **Mishra et al., "Don't Count Me Out: On the Relevance of IP Addresses in the Tracking Ecosystem"** (WWW 2020) | **THE core paper for your project's premise.** Devices reuse previous IPs for long periods — **IP is a far better re-identifier than the "dynamic IPs churn constantly" folk model claims.** If you cite one paper in your README, cite this | [↗ hal.inria.fr/hal-02435622](https://hal.inria.fr/hal-02435622/document) |
| **Richter et al., "A Multi-perspective Analysis of Carrier-Grade NAT Deployment"** (IMC 2016) | How many subscribers share an address — **the ceiling on how much any single IP can identify.** The honest counterweight | [↗ arxiv.org/abs](https://arxiv.org/abs/1605.05606) |
| **Padmanabhan et al., "Reasons Dynamic Addresses Change"** (IMC 2016) | *When* and *why* ISPs reassign residential addresses — **many rotate on fixed multiples of 24 h.** Cite for "how long does an IP stay linkable to a household" | [↗ doi.org/10.1145](https://doi.org/10.1145/2987443.2987461) |
| **RFC 6269 — Issues with IP Address Sharing** | The normative *"an IP is not a user"* citation | [↗ rfc-editor.org/rfc](https://www.rfc-editor.org/rfc/rfc6269.html) |
| 🔴 **Breyer v Bundesrepublik Deutschland (C-582/14)**, CJEU 2016 | **Dynamic IPs are personal data under EU law** where the operator has lawful means to identify. **One paragraph, and it is the legal spine of your problem statement** | [↗ curia.europa.eu/juris](https://curia.europa.eu/juris/document/document.jsf?docid=184668&doclang=EN) |
| 🔴 **FTC, "A Look at What ISPs Know About You"** (6(b) study, 2021) | **Compulsory-process findings on six major ISPs**: they collect all Internet traffic and real-time location with little meaningful choice. **The strongest citable US evidence for ISP-side collection** | [↗ ftc.gov/system](https://www.ftc.gov/system/files/documents/reports/look-what-isps-know-about-you-examining-privacy-practices-six-major-internet-service-providers/p195402_isp_6b_staff_report.pdf) |

**Data brokers — the assembly step:** **FTC, "Data Brokers: A Call for Transparency and Accountability"** (2014), the foundational regulatory study · **Sherman (Duke), "Data Brokers and Sensitive Data on US Individuals"** (2021), sourced by **direct purchase** · **Kim (Duke), "The Sale of Americans' Mental Health Data"** (2023), the most-cited concrete harm study · 🔴 **Gueorguieva et al. (Stanford), "Privacy Without Remedy"** (2026) — an audit of **522 registered brokers** showing **opt-out does not work.** *Prevention over removal, evidenced*

### G.6 🔴 · Does the deployed answer actually work? — read before you claim latency

| Resource | Why | Link |
|---|---|---|
| 🔴🔴 **Trevisan et al., "Measuring the Performance of iCloud Private Relay"** (PAM 2023) | **Up to 10× lower speed-test performance, plus page-load penalties.** *This is the deployment-friction reality check for your entire premise. Adyton's claim is "at latency a normal person will accept" — **this paper is the evidence that the incumbent does not meet that bar**, and it is simultaneously the standard you must beat and the reason the project has a point* | [↗ pschmitt.net/docs](https://pschmitt.net/docs/pam23_pr.pdf) |
| **Ravalico et al., "Measuring iCloud Private Relay: Desktop and Mobile"** (2025) | **RECENT** — current numbers | [↗ doi.org/10.2139](https://doi.org/10.2139/ssrn.5361064) |
| 🔴 **Zohaib, Sheffey, Houmansadr, "Investigating Traffic Analysis Attacks on Apple iCloud Private Relay"** (AsiaCCS 2023) | **IP hiding does not defeat correlation or website fingerprinting.** The necessary caveat on your own claim, and the bridge to §V.C.5 | [↗ doi.org/10.1145](https://doi.org/10.1145/3579856.3595793) |
| **Google Chrome IP Protection** | Two-hop proxy with RSA blind signatures, Incognito-only, regional rollout. ⚠️ *The explainer repo was archived in Nov 2025 — check the Privacy Sandbox status page before asserting its state* | [↗ privacysandbox.google.com/protect…](https://privacysandbox.google.com/protections/ip-protection) |
| **"Lost in the Prefix: Revisiting IP Geolocation Accuracy"** (2026) | **RECENT** — **mobile median error 179–207 km vs 3–16 km fixed**, failure rates 53–72% in Asia/Africa vs 9–20% in Europe. 🔴 *Relevant to you specifically: geolocation of an Egyptian client is much worse than the marketing assumes, in both directions* | [↗ arxiv.org/abs](https://arxiv.org/abs/2605.21937) |

### G.7 · AS-graph infrastructure — Level 9, and 🚨 request access in Week 45

> 🚨 **Two scheduling facts to act on early.** **(1)** CAIDA's **AS Relationships** data — the thing you actually need — is **free with no registration.** But the **recent-year ITDK and Ark traceroute data is restricted** to academics, US government and CAIDA members, via a request form with a **2–3 business-day turnaround.** If you want it, request it in Week 45, not Week 49. **(2)** RIPE Atlas traceroutes cost **30 credits per result** (doubled for one-offs), and you earn ~21,600/day per hosted probe. **Host a probe now** and let the **free built-in measurement corpus** carry your bootstrap.

| Resource | Access | Link |
|---|---|---|
| 🔴 **CAIDA AS Relationships (serial-1 / serial-2)** | **Free, no registration.** Monthly p2c/p2p files — **the core input, and what Astoria, DeNASA, Counter-RAPTOR and CLAPS all consume** | [↗ publicdata.caida.org/datasets](https://publicdata.caida.org/datasets/as-relationships/serial-1/) |
| **CAIDA AS Rank + API** | **Free, no key.** Per-AS rank, customer cone, clique membership, historical snapshots. 🔴 *Use it to score candidate relay ASes by transit centrality* | [↗ asrank.caida.org](https://asrank.caida.org/) · [↗ api.asrank.caida.org/v2](https://api.asrank.caida.org/v2/docs) |
| **CAIDA AS-to-Organization** | Free under AUA. 🔴 **Essential: collapse sibling ASes so two relays in one org are not counted as independent** | [↗ caida.org/catalog](https://www.caida.org/catalog/datasets/as-organizations/) |
| **Routeviews Prefix-to-AS** | Free, daily. **How you resolve a relay IP to an ASN** | [↗ publicdata.caida.org/datasets](https://publicdata.caida.org/datasets/routing/routeviews-prefix2as/) |
| **CAIDA ITDK / Ark traceroutes** | ⚠️ **Restricted for the recent year; request form, 2–3 days** | [↗ catalog.caida.org/datasets](https://catalog.caida.org/datasets/request_user_info_forms/topology_request) |
| 🔴 **Internet Yellow Pages (IYP)** (IMC 2024) | **The highest-leverage single tool here.** A Neo4j knowledge graph unifying 27+ sources, **freely queryable via Cypher with no auth**, Docker image for local use | [↗ iyp.iijlab.net](https://iyp.iijlab.net/) · tutorial [↗ tutorial.iyp.ihr.live](https://tutorial.iyp.ihr.live/) |
| **BGPStream / PyBGPStream** | Free/open. Unified API over RouteViews + RIS, live and historical. 🔴 **Write code against this, not raw MRT** | [↗ bgpstream.caida.org](https://bgpstream.caida.org/) |
| **RIPE Atlas built-in measurements** | 🔴 **Results readable free via the REST API, zero credits.** Every probe auto-pings roots every 240 s and traceroutes every 1800 s. **The best free continuously-collected global RTT corpus** | [↗ atlas.ripe.net/docs](https://atlas.ripe.net/docs/built-in-measurements/) |
| **`ripe-atlas-cousteau`** and **`ripe.atlas.sagan`** | Free/open. 🔴 *Sagan absorbs dozens of traceroute-format edge cases — **do not hand-roll the parsing*** | [↗ github.com/RIPE-NCC](https://github.com/RIPE-NCC/ripe-atlas-cousteau) · [↗ github.com/RIPE-NCC](https://github.com/RIPE-NCC/ripe.atlas.sagan) |
| **PeeringDB API** | **Read is free and anonymous**; write needs a key | [↗ peeringdb.com/apidocs](https://www.peeringdb.com/apidocs/) |
| 🔴 **Sermpezis et al., "Bias in Internet Measurement Platforms"** (TMA 2023) | **How Atlas/RouteViews/RIS probe placement is skewed by geography, AS type and topology. Read before generalising any Atlas latency number** | [↗ doi.org/10.23919](https://doi.org/10.23919/tma58422.2023.10198985) |
| **Chatzis et al., "There Is More to IXPs Than Meets the Eye"** (CCR 2013) | 🔴 **The argument for placing relays at or near IXPs** rather than reasoning purely from the inferred AS graph | [↗ doi.org/10.1145](https://doi.org/10.1145/2541468.2541473) |
| **PredictRoute** (SIGMETRICS 2021) | **The most practical off-the-shelf path predictor**, with accuracy reported against measured paths | [↗ escholarship.org/uc](https://escholarship.org/uc/item/4xn2f3s3) |
| **Sibyl** (NSDI 2016) | 🔴 *Query for routes matching high-level properties — "find a path avoiding AS X" — and issue the minimum traceroutes to answer. **Exactly the primitive a relay selector needs*** | [↗ usenix.org/conference](https://www.usenix.org/conference/nsdi16/technical-sessions/presentation/cunha) |

### G.8 · Differential privacy for engineers — Level 7's telemetry plane

🔴 **Near & Abuah, *Programming Differential Privacy*** — a living open book with **executable Python chapters and no measure theory.** The best engineer-facing DP primer that exists · [↗ programming-dp.com](https://programming-dp.com/)
**Damien Desfontaines, "A friendly, non-technical introduction to differential privacy"** — the series index, branching into the how and the why, including **when *not* to use DP** · [↗ desfontain.es/blog](https://desfontain.es/blog/friendly-intro-to-differential-privacy.html)
🔴 **NIST SP 800-226, "Guidelines for Evaluating Differential Privacy Guarantees"** (Final, 2025) — **the normative checklist for judging a DP claim. Use it to write up your own defensibly** · [↗ csrc.nist.gov/pubs](https://csrc.nist.gov/pubs/sp/800/226/final)
**NIST IR 8588 — DP Deployment Registry** (2025) — **a rare source of grounded real-world epsilon precedent** · [↗ csrc.nist.gov/pubs](https://csrc.nist.gov/pubs/ir/8588/ipd)
**Janus + libprio-rs** (ISRG) — production DAP aggregator and Rust Prio/VDAF library. 🔴 **The most practical starting point for your aggregator** · [↗ github.com/divviup](https://github.com/divviup/janus)
**OpenDP / SmartNoise** · **Google's differential-privacy library** (with **DP Auditorium** for auditing your own guarantees) · [↗ opendp.org](https://opendp.org/) · [↗ github.com/google](https://github.com/google/differential-privacy)
**Apple, "Learning with Privacy at Scale"** and **RAPPOR** (CCS 2014) — the two deployed local-DP systems, with real bandwidth and accuracy numbers · [↗ machinelearning.apple.com/research](https://machinelearning.apple.com/research/learning-with-privacy-at-scale) · [↗ arxiv.org/abs](https://arxiv.org/abs/1407.6981)
---
---

---
---

# PART VI — THE TERM

> ## 📅 This is the part you open every morning.
>
> **Find this week. Everything you owe is in one card, and every link is clickable.**

### How to read a week card

| Icon | Means | Rule |
|---|---|---|
| 📺 | **Watch** — a named course, a numbered lecture | 1.25–1.5×, slides open, **paused** to write things down |
| 📄 | **Read** — a paper, spec, article or chapter | 🔴 **Every paper gets a one-page note:** what problem · what insight · what did they give up · what would you do differently in 2027 |
| 🛠 | **Build** — this week's Adyton work | **Weekend blocks.** Nothing hard is built in 45-minute slices |
| 🧩 | **DSA** — the pattern, and the exact problems | Daily. Time-boxed. Log every failure |
| 📖 | **The book** — named chapters and page numbers from `DSA_Mastery.pdf` | 1h, **inside** the DSA budget. 🔴 *Type the code from memory, not from the page* |
| 🏛 | **Design** — one system-design problem, written up | 45 minutes, to the rubric in §VII.9 |
| ✅ | **Done when** — the acceptance criteria | Met or not met. **"Partially" is not a category** |
| ❓ | **Find out** — questions I refuse to answer | The looking-up *is* the lesson |

**🔥 THE WALL** opens each level. **You may not read the explanation, open the lecture or run the prompt until the failure is on your screen.**

> **Two card densities, on purpose.** **Levels 0–4** get a **full card per week**, because every week is a different shape. **Levels 5–9** get a **week-per-row table**, because those levels are "keep driving one course while the build advances" and a row is the honest density — same seven fields, less scrolling. **Every week from 1 to 52 is there either way.**

### The year on one line

```
L0 ▸▸▸        W1-3    foundations, and how big can this actually be
L1 ▸▸▸▸▸      W4-8    C++, sanitizers, fuzzing, exploitation        │ D0
L2 ▸▸▸▸       W9-12   🔴 measure the problem before solving it      │ D1  ⚑CV1
L3 ▸▸▸▸▸▸     W13-18  onion routing & Sphinx                        │ D2  🤝referrals
L4 ▸▸▸▸▸▸▸▸   W19-26  ★ compartments — the first real thing         │ D3  ★DEMO ⚑CV2
L5 ▸▸▸▸▸▸     W27-32  transport — you write TCP                     │ D4
L6 ▸▸▸▸▸      W33-37  the mesh — NAT, gossip, simulation            │ D5
L7 ▸▸▸▸▸▸▸    W38-44  ☕ the directory — Raft, Kafka, Postgres       │ D6
L8 ▸▸▸▸       W45-48  🎯 operations & the shell — APPLY             │ D7  ⚑CV4
L9 ▸▸▸▸       W49-52  ⭐ the attack lab & the curve                  │ D8 D9
```

**Rest weeks: 12 · 26 · 37 · 48** (10h) **· Buffer: 18 · 32 · 44 · 🌙 Ramadan W22–26 (20h) · Eid W36 (26h)**

---
---

# ⚡ LEVEL 0 — FOUNDATIONS & THE MEASUREMENT
**W1–3 · 14 Sep – 4 Oct 2026**

> 🔥 **THE WALL** — Two functions summing the same 4096×4096 `int32` matrix, row-major and column-major. **Identical Big-O. Column-major is 5–60× slower.** Then two `int64` counters in one struct, two threads incrementing one each; then padded onto separate 64-byte cache lines. **Same work, 3–10× throughput difference.**
> *Both numbers on your screen before you read anything.*

## ▸ W01 · 14–20 Sep · L0 · 32h
> **Set up the year, and measure the machine you will spend it on.**

| | h | What | Go |
|---|---|---|---|
| 📺 | 3 | **CS:APP** — *The Memory Hierarchy* + *Cache Memories* ⚠️ slides only, no video | [↗ slide decks](https://www.cs.cmu.edu/afs/cs/academic/class/15213-f25/www/lectures/) |
| 📕 | 3 | **CS:APP §6.2–6.4** (~40pp, skip §6.1) · **Drepper §3 in full** | [↗ Drepper, LWN](https://lwn.net/Articles/250967/) · [↗ full PDF](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf) |
| 📄 | 1 | Ostrovsky, *Gallery of Processor Cache Effects* — **run all ten, don't just read** · Colin Scott's latency numbers, scrubbed 1990→2020 | [↗ latency numbers](https://colin-scott.github.io/personal_website/research/interactive_latency.html) |
| 🛠 | 14 | Repo · CI · toolchains (C++20/CMake/vcpkg, Java 21, Go, Python) · 🔴 **`docs/scope.md`** (§I.4, one page, never revisited) · **`lab/latency-lab`** | — |
| 🧩 | 4.5 | Arrays, hashing, prefix sums, two pointers — **NeetCode Arrays & Hashing, all 9** | [↗ neetcode.io/practice](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Big-O: Time & Space* **p9** · *Arrays* **p41** · *Hash Maps & Sets* **p47** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | The estimation module. Memorise §VII.9's numbers. *How much storage does a relay network for 10k users need per month of consensus documents?* | — |

**✅ DONE WHEN** cache sizes derived from your own working-set sweep match `lscpu` within one power of two · row-major vs column-major gap **explained by measured LLC-misses, not asserted** · false-sharing fix ≥3× with `perf c2c` committed · 🔴 **the network row measured, not looked up — a ~90 ms cross-continent RTT is the floor under every circuit you will ever build**

**❓ FIND OUT** · L1 is ~1 ns and a cross-continent RTT is ~90 ms — **how many L1 accesses fit in one RTT?** Compute it; the number should disturb you · What is `perf c2c` measuring, and which counter does it read? · Why is an *uncontended* atomic still slower than a plain load?

## ▸ W02 · 21–27 Sep · L0 · 32h 🔴 *the scale spike — do not defer*
> **Find out what your hardware can carry, and learn that your benchmarks are lying.**

| | h | What | Go |
|---|---|---|---|
| 📄 | 3 | 🔴 **Gil Tene, *How NOT to Measure Latency*** — before you publish a single benchmark this year · Dean & Barroso, *The Tail at Scale* (8pp) · Gregg, *The USE Method* | [↗ Tene talk](https://www.infoq.com/presentations/latency-response-time/) · [↗ Tail at Scale](https://research.google/pubs/the-tail-at-scale/) · [↗ USE method](https://www.brendangregg.com/usemethod.html) |
| 🛠 | 16 | **`lab/bench`** — open-loop by default, `perf stat`, **HdrHistogram**, CI regression gate, and **four `tc netem` profiles** (clean / 1% loss / 5%+jitter / mobile) so every network number states its conditions · **`sickbay`** (8 injectable pathologies) · 🔴 **`docs/SCALE-RISK.md`** | [↗ HdrHistogram](http://hdrhistogram.org/) · [↗ wrk2](https://github.com/giltene/wrk2) |
| 🧩 | 4.5 | Two pointers, sliding window — NeetCode both sets | [↗ neetcode.io](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Two Pointers* **p78** · *Sliding Window* **p82** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | URL shortener. Practise the sentence: *"I'm optimising for X, which costs me Y."* | — |

**✅ DONE WHEN** two runs give byte-identical results · harness is **open-loop by default** and you can say why in a paragraph · a deliberate 5% regression is caught by `benchstat` in CI · **`sickbay` median diagnosis under 10 min across all 8, shuffled** · 🔴 **a signed, dated go/no-go on the local-mesh-plus-simulator strategy, with the binding resource named** · **Oracle always-free ARM box live, reachable from Cairo, $0.00 confirmed** · 🚨 **check whether [↗ cs144.github.io](https://cs144.github.io/) is back — and repeat every week until it is**

**❓ FIND OUT** · Coordinated omission, in one sentence you'd say to a manager — then **sketch a harness where a 200 ms stall is invisible** · Why can't you average percentiles? · What does `tc netem`'s `distribution normal` actually do, and why does it matter for a relay?

## ▸ W03 · 28 Sep – 4 Oct · L0 · 32h
> **A number a stranger can check, and the ethics of measuring anything.**

| | h | What | Go |
|---|---|---|---|
| 📺 | 3 | **CS161** — *Security Principles* · *x86 Assembly and the Call Stack* | [↗ CS161 video](https://www.youtube.com/@berkeley-cs161) · [↗ free textbook](https://textbook.cs161.org) |
| 📄 | 3 | 🔴 **The Tor Research Safety Board's principles — read before Level 2 collects a single byte** · Brooker, *Telling Stories About Little's Law* | [↗ Safety Board](https://research.torproject.org/safetyboard/) · [↗ Little's Law](https://brooker.co.za/blog/2018/06/20/littles-law.html) |
| 🛠 | 13 | **`1brc` v1** — the naive attempt. Time it, commit it, **do not optimise it.** You return in W51 · README skeleton with the honesty and scale statements already in place | [↗ 1BRC](https://github.com/gunnarmorling/1brc) |
| 🧩 | 4.5 | Finish the L0 set — **~28 problems cumulative** | — |
| 📖 | 1 | **DSA Mastery** — *Prefix Sums & Difference Arrays* **p98** · *Amortized Analysis* **p37** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Rate limiter *(you build one for real in L8)* | — |

**✅ DONE WHEN** `1brc` v1 time is in `bench/RESULTS.md` with the machine spec · 🔴 **`make bootstrap` works on a clean clone** — you re-verify this at every level boundary · 📝 **Track J: review someone's PR at Logic Leap. Start the habit this week**

**❓ FIND OUT** · Read the 1BRC leaderboard's top entries and **name three techniques you don't understand** — you'll use two of them in W51 · What does the Tor Safety Board say about measuring a live network, and which principle applies to crawling the public web?

---
---

# ⚡ LEVEL 1 — ⚙️ C++, SANITIZERS & THE THREAT
**W4–8 · 5 Oct – 8 Nov 2026 · 🎯 D0 · 🚩 `hardened`**

> 🔥 **THE WALL — four failures, in order.** Write the obvious framing. Then: **(1)** send two messages quickly — they arrive glued together. **TCP is a byte stream, not a message stream.** **(2)** Send 10 MB — `recv(4096)` gets 4096 bytes. **(3)** 🔴 **Send a length prefix of `0xFFFFFFFF`. Your receiver allocates 4 GB and dies. A hostile peer just killed your relay with four bytes.** **(4)** Add a field, deploy one side, watch the other break.

## ▸ W04 · 5–11 Oct · L1 · 32h
> **Wire the safety apparatus. It is the argument for having chosen C++ at all.**

| | h | What | Go |
|---|---|---|---|
| 📺 | 3 | **CS161** — *Memory Safety Vulnerabilities* · *Mitigating Memory-Safety Vulnerabilities* | [↗ CS161](https://www.youtube.com/@berkeley-cs161) |
| 📄 | 3 | 🔴 **Read these two on the same day:** Chromium — *~70% of serious security bugs are memory-safety bugs* · Tor — *~half of Tor's tracked bugs since 2016 were memory-safety issues impossible in safe Rust*. **Let it make you uncomfortable; the rest of this level is the answer** · Google, *Building a good fuzz target* | [↗ Chromium memory safety](https://www.chromium.org/Home/chromium-security/memory-safety/) · [↗ Announcing Arti](https://blog.torproject.org/announcing-arti/) · [↗ good fuzz target](https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md) |
| 🛠 | 16 | `adyton-node` skeleton + `adyton-wire/codec`: length-prefixed frames with a **hard max validated before allocation**, CRC, varints, `std::span` views, arena allocation · 🔴 **CI this week: ASan + UBSan + TSan, `-Werror`, clang-tidy `cppcoreguidelines-*`+`bugprone-*`, libFuzzer on the parser** | [↗ ASan](https://clang.llvm.org/docs/AddressSanitizer.html) · [↗ libFuzzer](https://llvm.org/docs/LibFuzzer.html) · [↗ std::span](https://en.cppreference.com/w/cpp/container/span) |
| 🧩 | 4.5 | 🔴 **Binary search, including on the answer** — LC 704 · 74 · 153 · 33 · **875 Koko** · **1011 Ship Packages** · 410. *875 and 1011 are literally how you pick a frame-size parameter* | [↗ LeetCode binary search](https://leetcode.com/tag/binary-search/) |
| 📖 | 1 | **DSA Mastery** — *Binary Search on Arrays* **p86** · 🔴 *Binary Search on the Answer* **p90** — *the exact tool you use to pick a frame-size parameter* | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Distributed job queue | — |

**✅ DONE WHEN** all four wall failures reproduced and **screenshotted** · ASan/UBSan/TSan green in CI **with a screenshot of a deliberately-introduced violation being caught** · the fuzzer runs *(it need not be clean yet)*

**❓ FIND OUT** · Your parser validates length before allocating — **name three other places in a network daemon where "validate before you act" applies, and find one real CVE for each** · What does `-fno-omit-frame-pointer` cost, and why is it worth it? · **Write the paragraph you'd say to an interviewer who asks "why didn't you use Rust?"** Keep it; you'll refine it all year

## ▸ W05 · 12–18 Oct · L1 · 32h
| | h | What | Go |
|---|---|---|---|
| 📕 | 3 | **OSTEP ch. 4–7** — processes, the API, direct execution, scheduling | [↗ OSTEP, free](https://pages.cs.wisc.edu/~remzi/OSTEP/) |
| 📄 | 2 | **C++ Core Guidelines** — the Resource Management, Bounds and Lifetime profiles | [↗ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines) |
| 🛠 | 17 | Varints · capability-negotiating handshake · explicit version field · **authenticated framing** (a frame failing its MAC is dropped *before* further parsing, and the failure is **counted and rate-limited**, not logged per occurrence — or a peer fills your disk) · 🔴 **`docs/cpp-subset.md`** | [↗ Protobuf encoding](https://protobuf.dev/programming-guides/encoding/) |
| 🧩 | 4.5 | 🔴 **Bit manipulation** — LC 136 · 191 · 338 · 190 · 371 · 268 · 78. *Your varint encoder is bit manipulation* | [↗ LeetCode bit manipulation](https://leetcode.com/tag/bit-manipulation/) |
| 📖 | 1 | **DSA Mastery** — 🔴 *Bit Manipulation* **p17** — *and your varint encoder is this chapter* | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Key-value store | — |

**✅ DONE WHEN** a **pinned old client binary interoperates with the new server, asserted by a test** · `docs/cpp-subset.md` exists and is honest

**❓ FIND OUT** · Why does Protobuf use varints, and what does zigzag encoding solve? · What's the largest value a 5-byte varint holds, and what should your parser do with a 6-byte one? · **Find one real protocol that got version negotiation wrong. What broke?**

## ▸ W06 · 19–25 Oct · L1 · 32h · **🎯 MILESTONE D0**
| | h | What | Go |
|---|---|---|---|
| 📄 | 3 | 🔴 **Cloudflare, *A Primer on Proxies*** — forward/reverse/transparent and the trust model of each. **Required vocabulary before you write a design doc** · Google, *Structure-aware fuzzing* | [↗ Primer on Proxies](https://blog.cloudflare.com/a-primer-on-proxies/) · [↗ structure-aware fuzzing](https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md) |
| 🛠 | 17 | 🚩 **`hardened`** — the apparatus as a deliverable: committed corpus, full sanitizer matrix, documented subset · 🔴 **write up the memory bugs the fuzzer found in your own parser — that is the deliverable, not the clean run** · `docs/design/wire-protocol.md` | — |
| 🧩 | 4.5 | Stacks & monotonic stacks — LC 20 · 155 · 150 · 22 · 739 · 853 · 84 | [↗ NeetCode Stack](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Stacks* **p53** · *Monotonic Stack & Queue* **p105** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Notification system | — |

**✅ DONE WHEN — D0** 🔴 **libFuzzer runs 1 hour clean on the frame parser, corpus committed** · **four attacks fail**, each with a test asserting the failure mode **and the counter it increments** · **`kill -9` at random points × 500: no message lost, duplicated or torn** · the bug write-up is in the repo

**❓ FIND OUT** · Your fuzzer is clean for an hour — **what does that prove, and what does it not?** · What is a fuzzing *dictionary* and would one help your parser? · How does OSS-Fuzz decide a bug is a *security* bug?

## ▸ W07 · 26 Oct – 1 Nov · L1 · 32h 🔴 *Proxy Lab + exploitation week*
> **Write a concurrent caching proxy — and you are forbidden the easy answer.**

| | h | What | Go |
|---|---|---|---|
| 🛠 | 13 | **CS:APP Proxy Lab**, all three parts. 🔴 *Part III's writeup forbids one big lock: "protecting accesses to the cache with one large exclusive lock is not an acceptable solution." Partition it, use readers–writers locks, or build it from semaphores* | [↗ writeup PDF](http://csapp.cs.cmu.edu/3e/proxylab.pdf) · [↗ handout .tar](http://csapp.cs.cmu.edu/3e/proxylab-handout.tar) |
| 🛠 | 6 | 🔴 **RPISEC MBE begins** — set up the VM, work the first challenge tier. **You have spent three weeks defending a parser; now spend two attacking one** | [↗ RPISEC/MBE](https://github.com/RPISEC/MBE) · [↗ CS:APP Bomb Lab](http://csapp.cs.cmu.edu/3e/bomb.tar) |
| 🧩 | 4.5 | Linked lists — LC 206 · 21 · 143 · 19 · 138 · 2 · 141 · 287 · **146 LRU Cache**. *You built a cache with an eviction policy this week* | [↗ NeetCode Linked List](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Linked Lists* **p50** · 🔴 *LRU/LFU Cache Design* **p285** — *you are building a proxy cache with an eviction policy this week. Read the chapter the same day* | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Distributed cache | — |

**✅ DONE WHEN** **70/70 from the bundled `./driver.sh`** · no segfaults, no memory or fd leaks · **a written paragraph on which synchronisation strategy you chose for the cache and why**

**❓ FIND OUT** · Why must the proxy downgrade HTTP/1.1→1.0 when forwarding, and what breaks if it doesn't? · **What exactly does "approximates LRU" buy you?** · Derive your worst-case memory in terms of `MAX_CACHE_SIZE`, `MAX_OBJECT_SIZE` and thread count

## ▸ W08 · 2–8 Nov · L1 · 32h
| | h | What | Go |
|---|---|---|---|
| 📕 | 3 | **OSTEP ch. 13–16, 18–19** (VM, TLB — ch. 19 is the one) · **cgroups v2 kernel docs**, `memory` and `cpu` controllers | [↗ OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) · [↗ cgroups v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html) |
| 🛠 | 11 | 🔴 **RPISEC MBE — ROP and format strings.** Finish the ladder as far as you get · the relay forwards, two processes, framed authenticated messages | [↗ RPISEC/MBE](https://github.com/RPISEC/MBE) |
| 🛠 | 6 | 🔴 **`docs/design/threat-model.md` v1** — the layers, what each assumes has already failed, and **an explicit section on what you do NOT defend against.** *You revise it in W25 and W50, and the revisions are the interesting part* | — |
| 🧩 | 4.5 | Consolidation + **the first failure-category count** if you have 30 entries. **~72 cumulative** | — |
| 📖 | 1 | **DSA Mastery** — *Recursion Mechanics* **p13** · *Strings* **p44** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | **Web crawler** *(you build one next week)* | — |

**✅ DONE WHEN** D0 signed off · CV v0 skeleton exists · 📝 **level checkpoint: `make bootstrap` on a clean clone — actually run it**

**❓ FIND OUT** · Your relay runs under `memory.max=512M` — **name four things counting against that limit besides your heap** · `memory.max` vs `memory.high`: which do you want? · Read one `k8s.af` entry about conntrack — **how many concurrent connections before a default Linux box exhausts its conntrack table?**

---
---

# ⚡ LEVEL 2 — 🔴 THE PROBLEM, MEASURED
**W9–12 · 9 Nov – 6 Dec 2026 · 🎯 D1 · 🚩 `linkage` · ⚑ CV v1 · W12 rest**

> **Make the premise of your own project into something you checked rather than something you read.**
> 🔴 *A privacy project built by someone who never measured the problem reads as ideological. One that opens with "I crawled five thousand sites; here is the distribution" reads as engineering. **That distinction is the whole difference in how a hiring manager receives this work** — and it lands in month three.*

> 🔥 **THE WALL — four measurements, each worse than the last.** **(1)** Count the third-party requests on one news site **by hand in devtools.** **(2)** Do five sites you actually use and **intersect the sets** — the intersection is not empty. **(3)** Measure your own fingerprint entropy **in bits.** **(4)** 🔴 **Now your IP. Your fingerprint may be shared with a thousand people. Your IP is shared with your household. Combine them and the set size is one.** *That is the argument for the entire network layer.*

## ▸ W09 · 9–15 Nov · L2 · 32h — *the crawler*
| | h | What | Go |
|---|---|---|---|
| 📄 | 4 | 🔴 **Englehardt & Narayanan, *Online Tracking: A 1-Million-Site Measurement*** — the methodology you're replicating · 🔴 **Gundelach et al., *Detecting Bot Detection*** — **Cloudflare blocks 37% and Akamai 26% of headless crawls; header signals alone cause 75% of it; and 83% of published papers never mention blocking.** Read before you write a line · Tranco's motivation section · DuckDuckGo, *Tracker Radar* | [↗ CCS'16 slides](https://senglehardt.com/presentations/2016_10_ccs_online_tracking.pdf) · [↗ Detecting Bot Detection](https://arxiv.org/abs/2606.14525) · [↗ tranco-list.eu](https://tranco-list.eu/) · [↗ Tracker Radar](https://spreadprivacy.com/duckduckgo-tracker-radar/) |
| 🛠 | 4 | **Quick win on day one:** run **Blacklight Query** over a few hundred URLs. Zero code, nine tests, **a credible first result inside an afternoon** | [↗ blacklight-query](https://github.com/the-markup/blacklight-query) |
| 🛠 | 14 | **`lab/linkage`** — choose **OpenWPM** (citable provenance) or **Playwright** and **write down why**. Record every third-party request, cookie, storage write and script. **Store in PostgreSQL**, schema in git · 🔴 **pin the Tranco list ID and publish it** · 🔴 **spoof your headers, then measure and publish your own block rate by provider** | [↗ OpenWPM](https://github.com/openwpm/OpenWPM) · [↗ tracker-radar-collector](https://github.com/duckduckgo/tracker-radar-collector) · [↗ Playwright](https://playwright.dev/) |
| 🧩 | 4.5 | 🔴 **Graphs: BFS, DFS, connected components** — LC 200 · 133 · 695 · 417 · 130 · 994 · 286. *You're about to build a real graph* | [↗ NeetCode Graphs](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Graph Fundamentals* **p139** · *Breadth-First Search* **p143** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Web crawler — **then compare your design to what you actually built** | — |

**✅ DONE WHEN** the crawler completes **500 sites unattended and is resumable after a kill** · rate-limited, real UA **with a contact address**, `robots.txt` respected — **you are a guest**

**❓ FIND OUT** · First-party cookie set by a third-party script vs a third-party cookie — **why does that distinction matter more every year?** · What is the state of third-party cookie policy in Chrome in 2026, and **what replaced the capability?** · What does `robots.txt` oblige you to do legally, and ethically — **are they the same?**

## ▸ W10 · 16–22 Nov · L2 · 32h — *the identifiers*
| | h | What | Go |
|---|---|---|---|
| 📄 | 3 | 🔴 **Mishra et al., *Don't Count Me Out: On the Relevance of IP Addresses***. **THE core paper for your premise** — devices reuse IPs far longer than the folk model claims · 🔴 **Mozilla, *Introducing State Partitioning*** — **the list of every kind of state two compartments must not share** · Brave, *Pool-party attacks* · Papadopoulos et al., *Cookie Synchronization* | [↗ Don't Count Me Out](https://hal.inria.fr/hal-02435622/document) · [↗ State Partitioning](https://hacks.mozilla.org/2021/02/introducing-state-partitioning/) · [↗ pool-party](https://brave.com/privacy-updates/13-pool-party-side-channels/) · [↗ Cookie Sync](https://arxiv.org/abs/1805.10505) |
| 🛠 | 18 | Classify domains against **EasyPrivacy** + **Disconnect**, and 🔴 **map domains to *organisations*** — that mapping is what makes the numbers honest · 🔴 **resolve CNAMEs and analyse first-party cookies too** — Böttger et al. (2026): **>54% of sites now track first-party or server-side and filter lists are "largely inadequate"** · 🔴 **hunt for cookie syncing — one instance in your own data is the best screenshot in the study** · measure your fingerprint entropy in bits | [↗ EasyPrivacy](https://easylist.to/easylist/easyprivacy.txt) · [↗ Disconnect list](https://github.com/disconnectme/disconnect-tracking-protection) · [↗ CookieGraph](https://arxiv.org/abs/2208.12370) |
| 🧩 | 4.5 | 🔴 **Union-find** — LC 684 · 547 · **721 Accounts Merge** · 990. **🔴 LC 721 *is* the linkage problem: merging accounts sharing an email is structurally identical to merging sessions sharing a tracker ID. Do it this week; use it for real next week** | [↗ LC 721](https://leetcode.com/problems/accounts-merge/) |
| 📖 | 1 | **DSA Mastery** — *Depth-First Search* **p147** · 🔴 *Union-Find (DSU)* **p156** — *then run it over your own crawl data* | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Distributed job queue | — |

**✅ DONE WHEN** the crawl reaches **5,000 sites** · **at least one confirmed cookie-sync instance, documented with the actual request that carried the identifier**

**❓ FIND OUT** · Your fingerprint has N bits — **how many bits uniquely identify one person among the world's internet users?** Compute it · What is CNAME cloaking and why does it defeat your domain classifier? · **Find one documented case of a data broker combining online and offline data. What was the mechanism?**

## ▸ W11 · 23–29 Nov · L2 · 32h 🔴 *the graph — this is the level*
| | h | What | Go |
|---|---|---|---|
| 📄 | 2 | 🔴 **Gómez-Boix et al., *Hiding in the Crowd*** — on 2M real fingerprints **uniqueness is far lower than Panopticlick suggested.** *It argues partly against your own framing, and including it is what makes the rest credible* · Su et al., *De-anonymizing Web Browsing Data with Social Networks* | [↗ Hiding in the Crowd](https://hal.inria.fr/hal-01718234/document) · [↗ De-anonymizing](https://doi.org/10.1145/3038912.3052714) |
| 🛠 | 19 | **The bipartite graph** — sites ↔ tracker organisations — then the tracker-to-tracker projection. Answer with numbers: **degree distribution** · 🔴 **THE HEADLINE: given an N-site session, what fraction can a *single* tracker observe? Plot N = 5, 10, 25, 50 with a confidence interval** · **largest connected component under identifier linkage** *(union-find, exactly as in LC 721)* · **how many orgs must collude for 90% of a session?** · 🔴 **re-run the whole crawl with uBlock Origin on and report the delta — nobody publishes this properly** | — |
| 🧩 | 4.5 | Graphs 2 — LC 207 · 210 · 261 · 323 · 127 · **785 Is Graph Bipartite** · 886 | [↗ NeetCode](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Cycle Detection* **p176** · *Bipartite Check* **p180** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Metrics pipeline | — |

**✅ DONE WHEN** the graph is built and rendered, and **one figure carries the whole argument**

**❓ FIND OUT** · Your largest connected component covers X% — **what is the right null hypothesis to compare that against?** · Is your degree distribution power-law? **How would you actually test that** rather than eyeballing a log-log plot? *(Find Clauset, Shalizi & Newman)* · **What is the difference between measuring *capability* and measuring *actual* data sharing — and which did you do?**

## ▸ W12 · 30 Nov – 6 Dec · 🛌 **REST (10h)** · **🎯 D1 · ⚑ CV v1**
| | h | What |
|---|---|---|
| 🛠 | 6 | 🔴 **`docs/analysis/linkability-2026.md`** — methodology in enough detail to rerun (list version, date, browser version, blocklist versions, machine) · the graph · the headline with its interval · 🔴 **the limitations section, and it is not optional: 5,000 sites is not the web · your number is a LOWER BOUND — [↗ Annamalai et al. (WWW 2025)](https://arxiv.org/abs/2502.01608) measured that crawls miss ~45% of the fingerprinting sites real users hit · your block rate by provider, stated · one vantage point sees one ad market · your identifier heuristics have a false-positive rate you estimated rather than ignored · and you measured *capability*, not actual data sharing.** *It justifies "many parties can observe overlapping slices and some exchange identifiers." It does not prove any named company assembled any named profile. Say so in the first paragraph* · **export the graph for the W26 demo** |
| 🚀 | | **BLOG POST 1 — *"I crawled 5,000 sites to find out how linkable the web actually is. Here's the graph."*** Cross-post to HN, Lobsters, r/privacy |
| 📝 | 4 | 🔴 **First failure-category count** — the one that will actually redirect you · level checkpoint · **⚑ CV v1** · 🤝 **referrals open next week: draft your three opening messages now, with the study as the hook** |
| 📖 | — | **DSA Mastery** — 🔴 *Interview & Study Strategy* **p7**. **Re-read it now that you have thirty failure-log entries. It reads completely differently with data behind it** | `DSA_Mastery.pdf` |

**❓ THE REST-WEEK QUESTION** · Find what Apple, Google, Mozilla and Brave each *claim* their defences achieve — **and check whether any of them publishes a comparable measurement.** Write one paragraph. *That paragraph is the opening of your README.*

---
---

# ⚡ LEVEL 3 — ONION ROUTING & SPHINX
**W13–18 · 7 Dec 2026 – 17 Jan 2027 · 🎯 D2 · 🚩 `sphinx` · 📺 Boneh + CS255 · W18 buffer · 🤝 referrals open**

> 🔥 **THE WALL** — Build the obvious onion: encrypt for hop 3, wrap for hop 2, wrap for hop 1. **Now measure the packet at each hop. It gets smaller.** The first relay knows it is first, the last knows it is last, and **an observer counting bytes learns every packet's position without breaking any crypto at all.**

## ▸ W13 · 7–13 Dec · L3 · 32h · 🤝 *referrals open*
| | h | What | Go |
|---|---|---|---|
| 📺 | 4 | **Boneh week 1** — stream ciphers, PRGs, semantic security, the one-time pad. 🔴 *Use the Stanford page, free, no account* | [↗ OnlineCrypto](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/) · [↗ CS255](https://crypto.stanford.edu/cs255/) |
| 📄 | 3 | 🔴 **Chaum 1981 — seven pages, the origin of the field** · 🔴 **Das et al., *Anonymity Trilemma*** — **every subsequent decision descends from this** · Dingledine et al., *Tor design paper* | [↗ Chaum 1981](https://chaum.com/wp-content/uploads/2022/09/UNTRACEABLE-ELECTRONIC-MAIL-RETURN-ADDRESSES-AND-DIGITAL-PSEUDONYMS-tech-report.pdf) · [↗ Trilemma](https://eprint.iacr.org/2017/954) · [↗ Tor design](https://svn-archive.torproject.org/svn/projects/design-paper/tor-design.pdf) |
| 🛠 | 16 | `adyton-core/crypto` — X25519, ChaCha20-Poly1305, HKDF via **libsodium**; **zeroizing secret types** | [↗ libsodium docs](https://doc.libsodium.org/) · [↗ secure memory](https://doc.libsodium.org/memory_management) |
| 🧩 | 4.5 | Trees & BSTs — LC 226 · 104 · 543 · 110 · 100 · 572 · 235 · 102 · 199 · 98 · 230 | [↗ NeetCode Trees](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Binary Trees & Traversals* **p61** · *Binary Search Trees* **p65** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Distributed lock service | — |

**✅ DONE WHEN** the shrinking-packet wall is reproduced and measured · **no secret material reaches a log, enforced by a CI grep**
**📝 TRACK J** 🔴 **Write to three people in the Egyptian engineering diaspora. The hook is your Week-12 study, not "I'm learning distributed systems."** One specific technical question. No other ask.

**❓ FIND OUT** · The trilemma says pick two of three — **which two does Tor pick, which two does Nym pick, and which two do you?** · Why is `sodium_memzero` necessary when `memset` exists? · Semantic security vs IND-CPA: what's the difference?

## ▸ W14 · 14–20 Dec · L3 · 32h
| | h | What | Go |
|---|---|---|---|
| 📺 | 4 | **Boneh week 2** — block ciphers, AES, PRPs/PRFs, modes, **CTR**. 🔴 *Your onion layers are CTR-shaped* | [↗ OnlineCrypto](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/) |
| 📄 | 3 | 🔴 **Danezis & Goldberg, *Sphinx*** — §3 and §4 carefully. **Before you write code, answer in one paragraph: why is the header size independent of hops remaining?** | [↗ Sphinx PDF](https://cypherpunks.ca/~iang/pubs/Sphinx_Oakland09.pdf) |
| 🛠 | 16 | The Sphinx header — the group element, routing information, per-hop MAC. **Structure first, crypto second** | [↗ nymtech/sphinx](https://github.com/nymtech/sphinx) |
| 🧩 | 4.5 | Heaps & top-K — LC 703 · 1046 · 973 · 215 · 621 · **295 Median from Data Stream** | [↗ NeetCode Heap](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Heaps & Priority Queues* **p69** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Sharded database | — |

**✅ DONE WHEN** you can **draw the packet layout from memory**
**❓ FIND OUT** · Sphinx uses a **single** group element for the whole header regardless of hop count — **how?** · What is LIONESS, and why does Lightning's BOLT #4 use ChaCha20 instead? · **What stops a relay replaying a Sphinx packet?**

## ▸ W15 · 21–27 Dec · L3 · 32h
| | h | What | Go |
|---|---|---|---|
| 📺 | 4 | **Boneh week 3** — MACs, CBC-MAC, HMAC, collision resistance, 🔴 **timing attacks on MAC verification** *(not optional for you)* | [↗ OnlineCrypto](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/) |
| 📄 | 3 | 🔴🔴 **Scherer, Weis, Strufe, *Provable Security for … Sphinx*** (PoPETs 2024). **It repairs Sphinx's broken proof, shows DDH is insufficient — you need Gap-DH — and documents a payload malleability issue.** *No other roadmap mentions this. Implementing Sphinx in 2027 without it is implementing a 2009 understanding of it* | [↗ arXiv 2312.08028](https://arxiv.org/abs/2312.08028) |
| 🛠 | 16 | `adyton-core/sphinx` — single-pass construction, per-hop key derivation, the MAC chain | — |
| 🧩 | 4.5 | Tries — LC 208 · 211 · 212 | [↗ NeetCode Tries](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Tries* **p73** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | A system with end-to-end encryption | — |

**✅ DONE WHEN** a 2-hop packet is constructed and processed end to end
**❓ FIND OUT** · What exactly was wrong with the original Sphinx proof, in two sentences? · **Does the payload malleability issue affect your design?** Justify either answer · Compare Sphinx's header to BOLT #4's — **name three deltas and why Lightning made each**

## ▸ W16 · 28 Dec – 3 Jan · L3 · 32h
| | h | What | Go |
|---|---|---|---|
| 📺 | 4 | 🔴 **Boneh week 4 — the most important week.** Authenticated encryption, chosen-ciphertext attacks, **CBC padding attacks**, key derivation, TLS 1.2 as a case study | [↗ OnlineCrypto](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/) |
| 🛠 | 16 | 🔴 **RapidCheck property test: serialised packet size byte-identical for 1, 2, 3, 4 hops remaining, across 10,000 generated packets** · libFuzzer on the Sphinx parser with its own corpus | [↗ RapidCheck](https://github.com/emil-e/rapidcheck) |
| 🧩 | 4.5 | 🔴 **Cryptopals sets 1–2 count as this week's practice** — you break padding oracles and nonce reuse **by hand** | [↗ cryptopals.com](https://cryptopals.com/) |
| 📖 | 1 | **DSA Mastery** — *Modular Arithmetic* **p20** · *Fast Exponentiation* **p25** — *the same week you are deriving keys* | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Identity & auth | — |

**✅ DONE WHEN** **the size invariant is asserted, not assumed** · the Sphinx parser fuzzes clean for an hour
**❓ FIND OUT** · **Name two other invariants of your packet format a property test could assert** — then write them · What is a padding oracle, and **could your relay be one?** · Why does the order of encrypt and MAC matter?

## ▸ W17 · 4–10 Jan · L3 · 32h
| | h | What | Go |
|---|---|---|---|
| 📺 | 4 | **Boneh week 5** — key exchange, Merkle puzzles, **Diffie–Hellman**, number theory | [↗ OnlineCrypto](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/) |
| 📄 | 2 | **Lightning BOLT #4** — 🔴 *the most widely deployed Sphinx derivative on Earth, with its deltas written down* | [↗ BOLT #4](https://github.com/lightning/bolts/blob/master/04-onion-routing.md) |
| 🛠 | 16 | `adyton-node` forwards a Sphinx packet across two hops, over the Level-1 wire · **`docs/design/packet-format.md`** | — |
| 🧩 | 4.5 | **CS255 programming project** counts as this week's practice | [↗ CS255](https://crypto.stanford.edu/cs255/) |
| 📖 | 1 | **DSA Mastery** — *GCD, LCM & the Euclidean Algorithm* **p23** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Certificate / PKI system | — |

**❓ FIND OUT** · **What does your relay learn about a packet it forwards? Enumerate it exhaustively — that list is a section of your threat model** · Why two hops and not three? What does the third buy, and cost? · What is your circuit's *forward secrecy* property, and what breaks it?

## ▸ W18 · 11–17 Jan · 🔧 **BUFFER** · **🎯 MILESTONE D2**
**✅ DONE WHEN — D2** 🔴 **Sphinx constant-size onion packets: a 2-hop packet processed, serialised size byte-identical regardless of hops remaining, RapidCheck-asserted** · Boneh weeks 1–5 complete · Cryptopals 1–2 done
**Also:** 🚨 **check CS144 again — you need it in nine weeks.** If still down, **plan the Wayback + mirror route now** · **failure-category count** · **~175 problems cumulative**
**📖 THE BOOK** — *Sorting* **p94** · *Divide and Conquer* **p129**

**❓ THE BUFFER-WEEK QUESTION** · Read Tor's `tor-spec` on relay cells. **Write one page comparing Tor's cell format to your Sphinx packet: what does each optimise for, and what did Tor give up by not using Sphinx?** *(Tor predates Sphinx. That is part of the answer.)* — [↗ tor-spec](https://spec.torproject.org/tor-spec/index.html)
---
---

# ⚡ LEVEL 4 — ★ COMPARTMENTS
**W19–26 · 18 Jan – 14 Mar 2027 · 🎯 D3 ★ · 🚩 `leakproof` · ★ THE DEMO · 🌙 Ramadan W22–26 · W26 rest · ⚑ CV v2**

> ★ **The first thing that is real.** At the end of this level you can sit someone down and show them **two browsers on one laptop that the internet cannot connect to each other.**
> 🌙 **Ramadan lands on W22–26 at 20h, and the collision is good luck.** The heavy netns work is W19–21 at full load; **W22–26 is the leak suite — many small independent tests, exactly the right shape for a reduced month.**

> 🔥 **THE WALL — five failures, and three are not the proxy's fault.** Point a browser at a SOCKS proxy on your relay. **(1) WebRTC** hands out your real IP as an ICE candidate, around the proxy entirely. **(2) IPv6** goes direct because the host is dual-stack. **(3) DNS** still goes to your ISP — every destination logged by name before a proxied byte moves. **(4)** Kill the relay mid-download: the browser **retries without it.** **(5)** 🔴 **Two profiles through one proxy are still linkable — shared exit IP, cookies, and the one you won't expect: TLS session tickets.**
> *Screenshot all five. Three of the first four are the application declining to use the proxy — **which is the entire argument for enforcing the boundary in the kernel rather than asking the application nicely.***

## ▸ W19 · 18–24 Jan · L4 · 32h
| | h | What | Go |
|---|---|---|---|
| 📺 | 3 | **CS161** — *Introduction to the Web* · **Same-Origin Policy** · **Cookies and Session Management** | [↗ CS161](https://www.youtube.com/@berkeley-cs161) · [↗ textbook](https://textbook.cs161.org) |
| 📄 | 3 | 🔴 **Mozilla, *Firefox 85 cracks down on supercookies*** — network-state partitioning: HTTP cache, **connection pools**, DNS cache, HSTS. *Connection pools and TLS tickets are the two your suite must test* · **Mullvad Browser docs** — its own statement that **it does not hide your IP** | [↗ supercookies](https://blog.mozilla.org/security/2021/01/26/supercookie-protections/) · [↗ Mullvad Browser](https://mullvad.net/en/browser) |
| 🛠 | 19 | **Reproduce all five failures. This week is diagnosis, not construction** | — |
| 🧩 | 4.5 | 🔴 **DP part 1, 1-D** — LC 70 · 198 · 213 · 91 · 139 · 322 · 518 · 300. 🔴 **The method, every time: subproblem in words → recurrence in a comment → base cases → *then* memo or table → space last. Do not write code before the recurrence exists in a comment** | [↗ NeetCode 1-D DP](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — 🔴 *Dynamic Programming — 1D Fundamentals* **p200** — *read it before you write a single recurrence* | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Multi-tenant API with quotas | — |

**❓ FIND OUT** · **Which of the five would a commercial VPN client also have? Go and test one** · What is HTTP/2 connection coalescing, and why does it link two profiles sharing an exit? · What is a TLS session ticket and how long does it live?

## ▸ W20 · 25–31 Jan · L4 · 32h
| | h | What | Go |
|---|---|---|---|
| 📺 | 2 | **6.1810 notes** — page tables, traps, namespaces *(notes only, no labs)* | [↗ 6.1810 Fall 2025](https://pdos.csail.mit.edu/6.1810/2025/) |
| 📕 | 2 | **Kerrisk TLPI ch. 28** or `namespaces(7)` · the **nftables** wiki | [↗ nftables wiki](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page) |
| 🛠 | 19 | `adytond` + `adyton-edge/launch`: **network namespaces** as the boundary — own interfaces, routing table, resolver. **veth** to the tunnel. 🔴 **nftables default-drop, so the kill switch is structural: if the tunnel dies there is no rule permitting anything** | — |
| 🧩 | 4.5 | DP 2-D — LC 1143 · **72 Edit Distance** · 62 · 64 · 221 · 5 · 647 | [↗ NeetCode 2-D DP](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *2D DP — Grid Paths & String Matching* **p203** · *LCS & Edit Distance* **p214** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | VPN / tunnelling service | — |

**✅ DONE WHEN** a process inside the namespace **cannot route around it, because there is no other route**
**❓ FIND OUT** · 🔴 **A kill switch as "detect and react" is a race; as default-drop it is an invariant. Give the exact race in the first design** · What happens to an **already-open socket** when its namespace's default route is removed? **Verify it, don't guess** · How do Mullvad's and Tailscale's Linux kill switches actually work?

## ▸ W21 · 1–7 Feb · L4 · 32h
| | h | What | Go |
|---|---|---|---|
| 📄 | 2 | 🔴 **Tor Browser design doc** — *Cross-Origin Identifier Unlinkability* and *Fingerprinting*. **The most thorough public treatment of browser linkability there is** | [↗ Tor Browser design](https://2019.www.torproject.org/projects/torbrowser/design/) |
| 🛠 | 19 | One **unmodified Mullvad Browser** profile per identity, each in its own netns on its own 2-hop circuit with its own pinned exit · `adyton identity launch shopping` as **one command** · ⚙️ 🔴 **make `Identity` a type whose constructor takes circuit + exit + profile-dir + namespace and has no setters — so a mismatched identity is not a bug you can write** | — |
| 🧩 | 4.5 | DP knapsack — LC 416 · 494 · 474 · 1049 + **AtCoder Educational DP, A–F** | [↗ AtCoder DP contest](https://atcoder.jp/contests/dp) |
| 📖 | 1 | **DSA Mastery** — *Knapsack — 0/1 and Unbounded* **p207** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Browser-isolation product | — |

**✅ DONE WHEN** ★ **an unmodified Mullvad Browser runs in a netns over a 2-hop circuit and you browse the real web through it**
**❓ FIND OUT** · 🔴 **Why is a network namespace a stronger boundary than a browser container?** Be specific about what each isolates *and shares* · Why must you **not** modify Mullvad Browser — what does each modification cost, **and to whom?** · What is in `docs/browser-delta.md`, and **can you justify every line?**

## ▸ W22 · 8–14 Feb · L4 · 32h *(last full week before Ramadan)*
| | h | What | Go |
|---|---|---|---|
| 📄 | 2 | **6.858 lecture 4** (buffer-overflow defences) and **lecture 12** (web security model) — cheap to pull forward | [↗ 6.858 2020](https://css.csail.mit.edu/6.858/2020/) |
| 🛠 | 19 | **The leak-suite harness, at full load.** *Get the scaffolding working now, because the tests themselves are the reduced-hours work* | — |
| 🧩 | 4.5 | Greedy + intervals — LC 53 · 55 · 45 · 134 · 846 · 56 · 57 · 435 · 253 | [↗ NeetCode](https://neetcode.io/practice) |
| 📖 | 1 | **DSA Mastery** — *Greedy Algorithms* **p116** · *Intervals* **p102** | `DSA_Mastery.pdf` |
| 🏛 | 2.5 | Quota & fair-share system | — |

**❓ FIND OUT** · **What is the *smallest* observable difference between two of your compartments that would let a tracker link them? Rank your five leak vectors by how hard each is to exploit**

## ▸ W23–W26 · 15 Feb – 14 Mar · 🌙 **RAMADAN — 20h/week**
**Split: 11 Depth / 5 Interview / 2 Fundamentals / 2 Craft. The interview track drops to 5h. It does not stop.**
🔴 **No new DSA topics for four weeks. Re-solve every DP failure from the log, and work [↗ AtCoder DP A–L](https://atcoder.jp/contests/dp) slowly.** *DP is the one topic that rewards slow careful weeks.*

| Week | 🛠 The leak suite — one family per week | 📖 **DSA Mastery** |
|---|---|---|
| **W23** · 15–21 Feb | **WebRTC and IPv6.** Zero ICE candidates with a non-namespace address. No IPv6 packet attributable to the identity leaves the host | *LIS & Patience Sorting* **p210** · read [↗ Brave: farbling](https://brave.com/privacy-updates/3-fingerprint-randomization/) |
| **W24** · 22–28 Feb | **DNS and the kill switch.** Zero DNS queries on the host uplink during a browse session. 🔴 **Daemon killed mid-transfer: zero subsequent packets, 20 runs, 20 passes** | *Kadane's Algorithm* **p120** · read [↗ Brave: defenses 2.0](https://brave.com/privacy-updates/4-fingerprinting-defenses-2.0/) |
| **W25** · 1–7 Mar | 🔴 **Cross-compartment.** Two identities share **no exit IP, no cookie, no DNS query, no TLS session ticket**, and produce **identical CreepJS output**. **Add the pool-party side channel to the suite** · `threat-model.md` v2 | *DP Optimizations* **p239** · read 🔴 [↗ Brave: why strict mode made users MORE identifiable](https://brave.com/privacy-updates/28-sunsetting-strict-fingerprinting-mode/) — *a published negative result, and the model for your own write-ups* |
| **W26** · 8–14 Mar | 🛌 **REST + EID** — ★ **the demo**, the write-up, CV v2 | 🔴 **Re-read, do not read new:** *DP 1D* **p200** · *2D DP* **p203** · *Knapsack* **p207** — *with a month of failures behind you* |

## ▸ W26 · 8–14 Mar · 🛌 REST · **🎯 D3 ★ · ★ THE DEMO · ⚑ CV v2**

**✅ DONE WHEN — D3** ★ unmodified Mullvad Browser, netns, 2-hop circuit, browsing the real web · 🔴 **`leakproof` green in CI across all five families, and a red build blocks merge — its going red is the alarm** · **identical CreepJS output across two machines** *(any difference is a bug in your launcher)* · ephemeral identities wiped on close · named identities with **exits pinned stably across restarts** · 🔴 **`docs/browser-delta.md` — if it is longer than "profile directory path and SOCKS endpoint," justify every entry or remove it**

**★ THE DEMO** — *don't demo the product, demo the harm*
**Screen 1 — you are assembled.** Their IP, ISP, city, fingerprint, and the hash. They click through five demo sites and **a graph draws itself live, connecting every visit — using your own Week-11 data.**
**Screen 2 — you are not.** The same walk through two compartments. **The graph fails to connect.** Side by side, sixty seconds apart.
**Screen 3 — and it isn't slow.** Page-load and TTFB: direct vs Adyton vs Tor, measured live on their connection.
🔴 **The scale statement printed on the page.** Rate-limited, quota per IP, **and it says it is a demonstration, not a proxy.** **Tested on a non-engineer — if they don't get it in ten seconds it isn't finished.**

**🚀 BLOG POST 2 — *"Your proxy leaks four ways and three of them aren't the proxy's fault."*** · **⚑ CV v2** · **failure-category count**

**❓ THE REST-WEEK QUESTION** · **Spend one hour attacking your own demo as a tracker with JavaScript on both sites. Write down everything you tried.** *That list is the next version of the leak suite — and "I attacked my own product, here's what I found" is the best answer you can give in an interview.*

---
---

# ⚡ LEVEL 5 — TRANSPORT: QUIC & FINGERPRINTS
**W27–32 · 15 Mar – 25 Apr 2027 · 🎯 D4 · 🚩 `minnow` · 📺 CS144 ckpts 0–6 · W32 buffer**

> 🚨 **Before W27: confirm the CS144 repo is back.** If not, use the [↗ Wayback handouts](https://web.archive.org/web/20260506063931/https://cs144.github.io/) and a [↗ live mirror](https://github.com/ht4w5/minnow-winter-2025), and **say so in your README** — *"built against the Fall 2025 handouts"* is a fine sentence.

| Week | 📺 CS144 | 🛠 Build | 🧩 DSA | ❓ Find out |
|---|---|---|---|---|
| **W27** 15–21 Mar | **ckpt 0** — telnet & SMTP by hand, `webget`, `ByteStream` | Toolchain; the harness that runs your TCP and the kernel's side by side | 🔴 **Intervals — LC 56 · 57 · 435 · 253 · 763.** *Do these the week **before** the reassembler* | What does `webget` teach you that `curl` hides? |
| **W28** 22–28 Mar | 🔴 **ckpt 1 — the `Reassembler`** | The reassembler. **It IS an interval-merge and you did the set last week** | Queues & deques — LC 239 · 622 · 933 | Why is the capacity limit part of the reassembler's *interface*, not an implementation detail? |
| **W29** 29 Mar–4 Apr | **ckpt 2** — `Wrap32`, `TCPReceiver` | Seqno wraparound, the window | DP 2 — LC 309 · 494 · 97 · 329 | 32-bit seqnos wrap. **At 10 Gbps, how long until wraparound?** Compute it |
| **W30** 5–11 Apr | 🔴 **ckpt 3 — `TCPSender` + the retransmission timer.** This is **RFC 6298** implemented | Talk to real Linux TCP. The "one megabyte challenge" | Shortest paths — LC 743 · 787 · 1631 · 778 | Your RTT estimator oscillates on a jittery link. **What does RFC 6298 do, and why those constants?** |
| **W31** 12–18 Apr | **ckpt 4** (the report) **+ ckpts 5–6** (ARP, the router) | 🔴 **Feed ckpt 4's real measurements straight into `lab/bench`'s netem profiles.** Your network conditions are now *yours* | MST & bridges — LC 1584 · **1489 Critical Connections** | **LC 1489 is Tarjan's bridge-finding — which relay's removal partitions your mesh?** *(You answer it for real in L6)* |
| **W32** 19–25 Apr | 🔧 **BUFFER** | QUIC via **ngtcp2**; `adyton-core/transport`; **ADR-0002** | Consolidation; failure-category count | — |


**📖 THE BOOK — 1h/week, inside the DSA budget**

| Week | **DSA Mastery** `DSA_Mastery.pdf` |
|---|---|
| **W27** | *Sweep Line* **p123** + re-read *Intervals* **p102** 🔴 *the reassembler is this chapter* |
| **W28** | *Queues* **p57** |
| **W29** | *Interval DP* **p218** |
| **W30** | *Dijkstra's Algorithm* **p160** · *Bellman-Ford* **p168** |
| **W31** | *Minimum Spanning Tree* **p164** · 🔴 *Articulation Points & Bridges* **p190** |
| **W32** | *Floyd-Warshall* **p171** · *Coordinate Compression* **p135** |

**📄 THE READING, across the level**
🔴 **Robin Marx, *Head-of-Line Blocking in QUIC and HTTP/3: The Details*** — the definitive explainer, **and it argues the fix is oversold**, which is the scepticism you want before building the chart yourself · [↗ perfplanet](https://calendar.perfplanet.com/2020/head-of-line-blocking-in-quic-and-http-3-the-details/)
**RFC 9000** §2, 5, 12–13, 17 · **RFC 9001** *(🔴 header protection is why your handshakes can be byte-identical except the random bits)* · **RFC 9002** · [↗ RFC 9000](https://www.rfc-editor.org/rfc/rfc9000.html) · [↗ RFC 9001](https://www.rfc-editor.org/rfc/rfc9001.html)
🔴 **Read these two on the same day and hold both:** [↗ Langley et al., QUIC at Google scale](https://research.google/pubs/the-quic-transport-protocol-design-and-internet-scale-deployment/) *(15–18% YouTube rebuffer reduction)* and [↗ QUIC is not Quick Enough over Fast Internet](https://arxiv.org/abs/2310.09423) *(**up to 45.2% LOWER throughput than TCP+TLS+H2 on fast links**)*
🔴 **Cloudflare, *Unlocking QUIC's proxying potential with MASQUE*** — read in W28 and **write an ADR: CONNECT-UDP is the standardised way to do exactly what you're doing, it's what Cloudflare replaced WireGuard with in WARP, and HTTP/3-shaped traffic survives middleboxes that eat custom UDP. Adopt it or justify why not** · [↗ MASQUE](https://blog.cloudflare.com/unlocking-quic-proxying-potential/)
**GSO and `sendmmsg` batching** — *the difference between a toy QUIC relay and one that saturates a NIC* · [↗ Cloudflare UDP](https://blog.cloudflare.com/accelerating-udp-packet-transmission-for-quic/) · [↗ Tailscale QUIC UDP](https://tailscale.com/blog/quic-udp-throughput)
🔴 **`qvis`** — point it at your own qlog traces and **see** the congestion window and multiplexing · [↗ qvis.quictools.info](https://qvis.quictools.info/)

**✅ DONE WHEN — D4** 🔴 **CS144 checkpoints 0–6 pass, screenshot in the README** · **your TCP interoperates with the kernel's** *(your client talks to a real `nc` server and back)* · **the comparison:** yours vs the kernel's over six netem profiles, throughput + p99 + retransmissions, **with an honest analysis of every place yours is worse** · 🔴 **THE HEAD-OF-LINE-BLOCKING CHART** — ten circuits over one TCP connection vs ten connections vs QUIC streams at 5% loss. *This justifies ADR-0002 and you will show it in interviews* · **per-hop QUIC works**, and 🔴 **two peers' handshakes are byte-identical except the random bits** *(a distinctive handshake is a fingerprint, and a fingerprint defeats the product)* · 🚀 **BLOG POST 3 — *"I implemented TCP so I'd stop guessing about head-of-line blocking. Here's the graph."***

---
---

# ⚡ LEVEL 6 — THE MESH: NAT & GOSSIP
**W33–37 · 26 Apr – 30 May 2027 · 🎯 D5 · 🚩 `meshsim` · 🌙 Eid W36 (26h) · W37 rest**

> 🔥 **THE WALL** — Run a relay in Cairo and another on a different network. Give each the other's IP. **They cannot connect, in either direction.** Both are behind NAT. **This is the physical reason peer-to-peer software needs traversal infrastructure, and it is invisible until you hit it.**
> ```bash
> # ask TWO different rendezvous servers for your external ip:port.
> # if they disagree, you are behind symmetric NAT and punching will not work.
> ```

| Week | 📄 Read | 🛠 Build | 🧩 DSA |
|---|---|---|---|
| **W33** 26 Apr–2 May | 🔴 **Tailscale, *How NAT traversal works*** — *the best practical write-up in existence: every NAT class, birthday-paradox port prediction, honest failure statistics. **Read it before any RFC.*** · **RFC 4787 §4** [↗ Tailscale NAT](https://tailscale.com/blog/how-nat-traversal-works) · [↗ RFC 4787](https://www.rfc-editor.org/rfc/rfc4787.html) | `adyton-edge/nat` with **`pion/ice`** — hole punching, relay fallback [↗ pion/ice](https://github.com/pion/ice) | Backtracking — LC 78 · 90 · 39 · 40 · 46 · 79 · 131 · 51 |
| **W34** 3–9 May | **Ford, Srisuresh & Kegel** (the original) · 🔴 **Hole punching in the wild (FOSDEM 2023)** — **6.25M results, ~70% success, and equal for TCP and QUIC**, overturning the folk belief that UDP is easier. *This is the published number yours is compared against* [↗ Ford et al.](https://bford.info/pub/net/p2pnat/) · [↗ FOSDEM](https://archive.fosdem.org/2023/schedule/event/network_hole_punching_in_the_wild/) | 🔴 **`natlab` — the reachability table:** hole-punch success by NAT-type pair, **across every network you can borrow** — home, mobile tether, café, cloud | Articulation points, SCC. 🔴 **Run Tarjan on your own 30-node gossip topology and report which relays are articulation points** |
| **W35** 10–16 May | **SWIM** (DSN 2002) · **φ Accrual** (SRDS 2004) · **HashiCorp's Lifeguard docs** — *a production system's honest account of where the paper needed fixing* [↗ SWIM](https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf) | `adyton-edge/gossip` — SWIM membership, phi-accrual detection | Probability & expectation — LC 837 · 808 · 688 |
| **W36** 17–23 May 🌙 | *Eid al-Adha, 26h.* **Brooker, *Simple Simulations for System Builders*** [↗ Brooker](https://brooker.co.za/blog/2022/04/11/simulation.html) | 🚩 **`meshsim`** — seeded clock **that can run backwards**, **asymmetric partitions**, disk faults, 🔴 **and a relay that *lies*** | Reservoir sampling, Bloom filters, HyperLogLog |
| **W37** 24–30 May | 🛌 **REST · 🎯 D5** | Write-up, blog post, failure-category count | — |


**📖 THE BOOK — 1h/week, inside the DSA budget**

| Week | **DSA Mastery** `DSA_Mastery.pdf` |
|---|---|
| **W33** | *Backtracking* **p112** |
| **W34** | *Strongly Connected Components* **p187** · *Euler Tour & Eulerian Paths* **p193** |
| **W35** | *Expected Value & Probability DP* **p233** |
| **W36** | *Randomized Algorithms — Quickselect & Reservoir Sampling* **p293** |
| **W37** | *Matrix / Grid Traversal* **p108** · *Largest Rectangle in Histogram* **p126** |

**✅ DONE WHEN — D5** **20–40 relays discover each other; convergence measured and plotted against mesh size, next to the naive O(N²) curve** · 🔴 **p50 circuit recovery <800 ms, p99 <3 s, under 20% churn** · 🔴 **THE REACHABILITY TABLE published** — success by NAT-type pair, **with N stated honestly because it is small**, plus the relay-fallback fraction and what it costs · **phi-accrual vs fixed timeout: false-positive rate and detection latency, both, charted** under injected jitter · 🔴 **the asymmetric-partition test: A reaches B, B doesn't reach A — the mesh converges, or you document exactly why it cannot** · **`meshsim` runs 10,000 seeds nightly; ≥3 real bugs found, each reproducible from a seed integer.** *A harness that finds nothing means your faults are too gentle — go and make them worse* · 🚀 **BLOG POST 4 — *"What fraction of real NAT pairs can actually hole-punch?"***

**❓ FIND OUT** · **Which NAT type defeats hole punching, and what does the fallback cost** — in latency, bandwidth, and **what the relay operator can see?** · Why is SWIM O(N) per node when naive membership is O(N²)? **What does indirect probing buy specifically?** · 🔴 **A relay that lies is a different fault class from one that crashes. Name three things a lying relay can do that your simulator should model — and one thing it can do that you cannot detect at all**

---
---

# ⚡ LEVEL 7 — ☕ THE DIRECTORY: RAFT & TELEMETRY
**W38–44 · 31 May – 18 Jul 2027 · 🎯 D6 · 🚩 `raft-dir` · 📺 6.5840 Labs 1–3 · W44 buffer + Final Gauntlet**

> ☕ **The Java level. Java is 53.3% of your target backend postings — the most-demanded skill in your corpus and the largest measured gap in your profile.**
> 🔴 **Why a directory needs consensus:** every client must see **the same** relay list. If two clients see different lists, their circuit choices differ observably — **and disagreement is a fingerprint.** *That sentence is the whole justification, and it is better than "distributed systems are cool."*

| Week | 📺 6.5840 | 🛠 Build | 🧩 DSA |
|---|---|---|---|
| **W38** 31 May–6 Jun | **Lectures 1–3 + Lab 1 (MapReduce).** 🔴 **Read the extended Raft paper and Gjengset's guide BEFORE you start, not when stuck** [↗ raft.pdf](https://raft.github.io/raft.pdf) · [↗ Students' Guide](https://thesquareplanet.com/blog/students-guide-to-raft/) | Java 21 ramp — records, sealed interfaces, **virtual threads**, `async-profiler` | 🔴 **A *proving* week: three written reductions from Skiena ch. 9.** Not code — prose proofs |
| **W39** 7–13 Jun | **Lab 2** — KV server, **the lock**, dropped messages. *Versioned put, at-most-once, linearizable — exactly your directory's semantics* | `adyton-directory` skeleton | Topological sort — LC 207 · 210 · 269 · 310. 🔴 *The epoch hash chain is a DAG* |
| **W40** 14–20 Jun | **Lab 3A/3B** — elections, log replication | Raft integrated · 🎯 **the Figure 8 whiteboard test, with a human watching** | **Segment trees** — [↗ Codeforces EDU](https://codeforces.com/edu/course/2/lesson/4) |
| **W41** 21–27 Jun | **Lab 3C** — persistence, 🔴 **Figure 8** | Epoch documents, hash chaining | Fenwick / range queries — LC 307 · 315 · 493 |
| **W42** 28 Jun–4 Jul | **Lab 3D** — snapshots, `TestFigure8Unreliable` | 🔴 **`adyton-aggregate`: relays → Kafka → aggregator → Postgres, with DP noise applied before publication** | **Strings** — [↗ CF EDU string algorithms](https://codeforces.com/edu/course/2/lesson/3). *The one area Adyton gives you nothing for* |
| **W43** 5–11 Jul | — | Peer admission · **the DP budget that fails closed** · `docs/design/consensus.md` | Company-tagged sets, timed at 25 min |
| **W44** 12–18 Jul | 🔧 **BUFFER** | D6 sign-off | 🔴 **THE FINAL GAUNTLET (§IX.2) + full timed loop #1** |


**📖 THE BOOK — 1h/week, inside the DSA budget**

| Week | **DSA Mastery** `DSA_Mastery.pdf` |
|---|---|
| **W38** | 🔴 *Network Flow: Max Flow & Min Cut* **p196** — *the same week you write three NP-hardness reductions* |
| **W39** | 🔴 *Topological Sort* **p152** — *your epoch hash chain is a DAG* |
| **W40** | *Segment Trees: Range Query & Update* **p248** |
| **W41** | *Fenwick Tree* **p253** · *Sparse Tables* **p257** · *LCA via Binary Lifting* **p183** |
| **W42** | *String Matching: KMP & Rabin-Karp* **p273** |
| **W43** | *Z-Function & Palindromic Substrings* **p277** · *Advanced Trie Problems* **p269** |
| **W44** | 🔴 **Part VII revision sheets before the Gauntlet:** *Graph Algorithms* **p318** · *Advanced Data Structures* **p308** |

**📄 THE READING**
🔴 [↗ Raft, the EXTENDED paper](https://raft.github.io/raft.pdf) — §5 in full, §6 carefully · 🔴 [↗ Students' Guide to Raft](https://thesquareplanet.com/blog/students-guide-to-raft/) — **read it *while* implementing**
🔴 [↗ The membership-change bug thread](https://groups.google.com/g/raft-dev/c/t4xj6dJTP6E) — *Ongaro announcing a safety bug in his own thesis's protocol, with the fix. The best document on Raft's subtle failure modes, and a lesson in intellectual honesty*
🔴 [↗ Antithesis, *Finding bugs in Raft implementations*](https://antithesis.com/blog/2026/finding-bugs-in-raft-implementations/) — **safety violations found in HashiCorp Raft, Aeron Cluster, OpenRaft and MicroRaft, and it enumerates four assumptions the Raft paper leaves implicit.** *Read before you trust your own*
🔴 [↗ Cloudflare, *Introducing Quicksilver*](https://blog.cloudflare.com/introducing-quicksilver-configuration-distribution-at-internet-scale/) — **the "why we did NOT use Raft" counterpoint. Read it, then defend your choice in ADR-0006 against it**
[↗ Tailscale, *Tailnet lock*](https://tailscale.com/blog/tailnet-lock) — 🔴 *an Ed25519 signing chain so a **compromised coordination server cannot inject nodes.** That is the attack on your own directory, with its published mitigation*
[↗ AWS, *Leader election in distributed systems*](https://builder.aws.com/content/3Ev0vH0hfkcUizISUWYTvHibtcp/leader-election-in-distributed-systems) — leases, fencing tokens, real failure modes. **Read before implementing** · **SUNDR** — 🔴 *fork consistency: a directory showing two clients different histories is exactly a fork attack* · [↗ Tor's dir-spec](https://spec.torproject.org/dir-spec/index.html) — *what a production consensus document actually contains*

**✅ DONE WHEN — D6** 🔴 **6.5840 Labs 1, 2 and 3 pass MIT's suites, including `TestFigure8Unreliable`. Screenshot** · leader elected from 5 nodes, **no split-brain across 1,000 randomised runs** · **minority partition cannot commit, 500 randomised schedules** · 🔴 **the Figure 8 scenario built as a deliberate test — and you draw it at a whiteboard in under five minutes from memory, tested by a human in W40** · 🔴 **100% of peers hold the same epoch-N consensus hash within 30 s of close, under 20% churn** *(because disagreement is a fingerprint)* · **fencing tokens: a relay whose lease expired cannot publish — demonstrate the violation without them and the fix with them, same seed** · **Kafka → Postgres telemetry with DP noise and a budget that fails closed** · **ADR-0006** · 🚀 **BLOG POST 5 — *"Where I put consensus in a relay network, and why not everywhere."***

---
---

# ⚡ LEVEL 8 — 🎯 OPERATIONS & THE SHELL
**W45–48 · 19 Jul – 15 Aug 2027 · 🎯 D7 · 🚩 `incident-lab` · ⚑ CV v4 · 🎯 APPLICATIONS OPEN · W48 rest**

> 🔴 **This level is what the screen reads.** AWS 48.9% · Kubernetes 30.4% · observability 22.0% · on-call 21.5%. **Never cut, never deferred.** Everything before this is what you talk about for forty-five minutes; **this is what gets you into the room.**
> **From W45 the split changes: 12h Depth / 12h Interview / 8h Career.**

| Week | 🛠 Build | 🎯 Career |
|---|---|---|
| **W45** 19–25 Jul | The mesh on **k3s**. Multi-region relays on free tiers. **Terraform: `apply` from zero, `destroy` to nothing** · 🚨 **request CAIDA ITDK access now if you want it — 2–3 business days** | 🎯 **CV v4 · first 16 applications** — Cloudflare, Tailscale, Apple, Mullvad, Proton **first** · **referral activation to the 24+ people you've known since December** |
| **W46** 26 Jul–1 Aug | Prometheus + Grafana · 🔴 **`docs/design/trustless-observability.md` — you cannot log per user, so which metrics are *facts* and which are relay *claims*?** · the 3am dashboard | 16 applications · **Loop #2** · 🔴 *practise answering design questions from your own system, deliberately — it doesn't happen naturally under pressure* |
| **W47** 2–8 Aug | 🚩 **`incident-lab`** — 20+ self-inflicted incidents + 6 famous outages reproduced · 🔴 **the harness audit: if `lab/bench` had coordinated omission, re-run every benchmark and put the before/after in `bench/RESULTS.md`** | 16 applications · **Loop #3** |
| **W48** 9–15 Aug | 🛌 **REST.** `gatekeep` (mTLS, **a cert-expiry alert tested by fast-forwarding a clock**), `costwatch` (**a billing alarm tested by triggering it**) | Pipeline review · failure-category count |


**📖 THE BOOK — 1h/week, inside the DSA budget**

| Week | **DSA Mastery** `DSA_Mastery.pdf` |
|---|---|
| **W45** | 🔴 *Concurrency Primitives in Coding Rounds* **p289** — *the same level you carry a pager* |
| **W46** | *Meet in the Middle* **p132** · *Balanced BSTs: AVL & Red-Black* **p260** |
| **W47** | *Bitmask DP* **p222** · *DP on Trees* **p226** |
| **W48** | *Suffix Arrays & Suffix Automaton* **p281** · Part VII *String Algorithms* **p315** |

**📄 THE READING** — **AWS Builders' Library**, all of: [↗ load shedding](https://builder.aws.com/content/3Eun1EEyX6p2e3VYNyRLSJzLuMV/using-load-shedding-to-avoid-overload) · [↗ timeouts, retries, jitter](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter) · [↗ queue backlogs](https://builder.aws.com/content/3EuRcgkTP1MI0c7zM8W6HL3WIqA/avoiding-insurmountable-queue-backlogs) · 🔴 [↗ static stability](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) *(keep working on stale state when the control plane is unreachable — **arguably the most important article for a relay network**)* · 🔴 [↗ implementing health checks](https://builder.aws.com/content/3Ev53O39izHCtWLzp4XU6t8PC1O/implementing-health-checks) *(and how a deep check takes down a whole fleet at once)* · 🔴 [↗ constant work](https://builder.aws.com/content/3F05oqNtNUWxHJ5r6L6I2HrH4rI/reliability-constant-work-and-a-good-cup-of-coffee) *(push full directory snapshots, not deltas — no failure-mode cliff)*
**Google SRE** [↗ ch. 21 Handling Overload](https://sre.google/sre-book/handling-overload/) · [↗ ch. 22 Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/) · **[↗ k8s.af — read ten](https://k8s.af/)**, including 🔴 [↗ conntrack exhaustion](https://deploy.live/blog/kubernetes-networking-problems-due-to-the-conntrack/) *(exactly what a relay fleet on k8s will hit)* · [↗ Netflix adaptive concurrency limits](https://medium.com/@NetflixTechBlog/performance-under-load-3e6fa9a60581)

**🔥 THE INCIDENTS — inject all of these:** relay kill mid-circuit · Raft leader kill mid-commit · **asymmetric partition** · disk fill on a relay holding epoch history · certificate expiry · a poison packet that crashes one parser · **all 20 relays restarting at once** · a peer flooding you · **a lying relay in production** · reconnect storm · **conntrack exhaustion** · 🔴 **clock skew**

> 🔴 **THE CLOCK-SKEW INCIDENT — do this one properly.** Skew one relay's clock by four seconds. **Nothing fails loudly.** Raft lease expiry is computed against a clock that disagrees with the leader's. Rate-limit windows are wrong. Epoch validity drifts. **The relay does not crash — it quietly makes wrong decisions while every dashboard stays green.** Then write the invariant: **relays report clock offset relative to the leader, and one beyond threshold is quarantined from leadership.**

**✅ DONE WHEN — D7** 20-relay mesh on k8s · 🔴 **rolling restart drops ZERO circuits under sustained load** · the 3am dashboard, and **time-to-root-cause under 5 minutes from dashboards alone, demonstrated on video** · **20+ incidents with runbooks** · **full cold start from epoch history, for real, and timed** · **$0.00 verified from both consoles and screenshotted** · 🔴 **the circular-dependency audit: does your admin surface, your monitoring, or your bootstrap relay depend on the mesh it serves?** · 🚀 **BLOG POSTS 6 + 7**

---
---

# ⚡ LEVEL 9 — ⭐ THE ATTACK LAB & PATH SELECTION
**W49–52 · 16 Aug – 12 Sep 2027 · 🎯 D8, D9 · 🚩 `ascorr` + `guardplace` · W49 rest**

> ⭐ **The research contribution — the only part of this project where you will have a result nobody has published.**
> 🔥 **THE WALL** — Implement AS-aware selection. Re-run the adversary. **Compromise probability drops meaningfully. Excellent.** Now put on the attacker's hat: 🔴 **your selector is deterministic and its scoring function is public — it is in your open-source repo. Where should I put my relays so your algorithm prefers them?** Place ten relays optimised against *your own* function. **It will be dramatically more than their fair share.** *You made the average case better and the targeted case worse, and a defender measuring only the average would never have noticed.*

| Week | 📄 Read | 🛠 Build |
|---|---|---|
| **W49** 16–22 Aug 🛌 | **REST + the AS-graph foundations.** 🔴 **Gao (2001), valley-free routing — start here** · **Luckie et al. (IMC 2013)**, the algorithm behind CAIDA's dataset [↗ Gao 2001](https://dl.acm.org/doi/10.1109/90.974527) · [↗ Luckie IMC'13](https://conferences.sigcomm.org/imc/2013/papers/imc039-luckieAemb.pdf) | **Download [↗ CAIDA AS Relationships](https://publicdata.caida.org/datasets/as-relationships/serial-1/)** *(free, no registration)* · `lab/asgraph` — valley-free inference · explore [↗ Internet Yellow Pages](https://iyp.iijlab.net/) *(free Cypher, no auth)* |
| **W50** 23–29 Aug | ⛓ **THE SPINE, in order:** [↗ Users Get Routed](https://dl.acm.org/doi/10.1145/2508859.2516651) → [↗ Astoria](https://arxiv.org/abs/1505.05173) → [↗ Counter-RAPTOR](https://arxiv.org/abs/1704.00843) + [↗ DeNASA](https://petsymposium.org/popets/2016/popets-2016-0044.php) · 🔴 **and the reality check: [↗ Juen et al.](https://petsymposium.org/popets/2015/popets-2015-0021.php) — 17.2M traceroutes showing BGP-simulated paths disagree badly with measured ones.** *Every design here rests on inference that is substantially wrong, and saying so is what makes it research rather than a demo* · **CS161 — the *Anonymity/Tor* chapters** · **6.858 L20** | 🚩 **`ascorr`** — circuit-compromise probability against a defined AS adversary, **for Adyton *and* for Tor**, on real CAIDA data. **[↗ TorPS](https://github.com/torps/torps)** for security-over-time |
| **W51** 30 Aug–5 Sep | 🔴🔴 **[↗ Wan et al., *Guard Placement Attacks*](https://www.princeton.edu/~pmittal/publications/guard-placement-pets19.pdf)** — **0.216% of bandwidth bought 18% of guard-selection probability.** *The paper this level exists to answer* → then **[↗ CLAPS](https://www.freehaven.net/anonbib/cache/claps-ccs2020.pdf)** · 🔴 **[↗ RPKI-Based Location-Unaware Guard Selection](https://arxiv.org/abs/2501.06010)** (PoPETs 2025) — *a genuinely different answer, and a candidate for your own selector* | 🚩 **`guardplace`** — **build the attack against your own selector.** Place relays optimised against your own public scoring function and measure their selection rate. Then **controlled randomness on a single tunable**, swept · **`1brc` v2 — the real assault, one year on. Report the delta** |
| **W52** 6–12 Sep | — | 🔴 **THE CURVE.** Synthesis, the ten ADRs, `LIMITATIONS.md`, `COMPARISON.md`, `RETROSPECTIVE.md`, `NEXT.md`, **the demo finalised** |


**📖 THE BOOK — 1h/week, inside the DSA budget**

| Week | **DSA Mastery** `DSA_Mastery.pdf` |
|---|---|
| **W49** | *Combinatorics Basics* **p28** · *Catalan Numbers* **p34** |
| **W50** | *Counting DP* **p236** · Part VII *Math & Number Theory* **p303** |
| **W51** | *Sieve of Eratosthenes* **p31** · *Matrix Exponentiation* **p243** · *Digit DP* **p230** |
| **W52** | 🔴 **All five Part VII Quick Reference sheets, end to end (p303–325)** — your final revision pass · and *Skip Lists* **p263** · *Branch and Bound* **p296** · *Gaussian Elimination* **p299** as **recognise, don't implement** |

**✅ DONE WHEN — D8** compromise probability against a defined AS adversary, **for Adyton and for Tor**, on real topology data, **with the inference-accuracy caveat stated in the first paragraph**

**✅ DONE WHEN — D9 ⭐** candidate selectors implemented **in Python first**, scored over the same graph against the same adversary presets, **winner chosen on data with the reason recorded** · 🔴 **the guard-placement adversary implemented and run against your own selector**, reporting the selection rate adversary-placed relays achieve · 🔴 **THE CURVE, PUBLISHED: for ≥5 randomness settings, compromise probability against the AS adversary *and* adversary-placed-relay selection rate, on one plot** · **the operating point chosen off the curve, with the reason written down — not by instinct** · 🔴 **the latency budget outranks the score.** *Adyton's whole trilemma choice was low latency; a selector that improves safety at 200 ms of build cost has violated the premise. If the winner exceeds budget, the budget wins and that is documented* · 🚀 **BLOG POST 8 — *"AS-aware path selection makes you predictable. Here is the curve."*** 🔴 **The plot is the post. It does not exist anywhere else.**

**✅ WEEK 52 — THE CLOSE** **README final**, tested on a human with a ten-minute timer, **the honesty and scale statements verbatim in the first screen** · **the ten ADRs** · 🔴 **`docs/LIMITATIONS.md` linked from the first screen** — mesh size, simulator fidelity, **metadata**, no mobile client, single-author review, no users. *Volunteering limitations before you are asked is the single highest-leverage interview behaviour available to you* · **`docs/COMPARISON.md`** vs **Tor**, **iCloud Private Relay**, **Nym/Loopix**, **Mullvad**, **Google IP Protection** · **`docs/RETROSPECTIVE.md`** — estimated vs actual hours per level and the ratio. *That ratio is a measured fact about you over twelve months, and almost no candidate has one* · `make bootstrap` from clean · **billing $0.00** · 🔴 **re-record the 45-minute talk and watch it against the W26 recording. The delta is the year** · **`docs/NEXT.md`**

> ❓ **THE LAST QUESTION** · *"Why would I use this instead of Tor?"*
> **The answer is: you would not** — and you should be able to say that without flinching, then explain what you learned building it anyway, then show two curves the Tor Project has never published. **If you can do that calmly, the year worked.**
# PART VII — TRACK I: THE INTERVIEW MACHINE

> **Daily from Week 1.** 8h/week to Week 44 (**5.5h DSA + 2.5h system design**), **12h/week from Week 45.**
> **Never batched. Never skipped.** You can build every level of Adyton and still be rejected in a 45-minute phone screen.

## VII.1 The ratio that governs it, and the correction

| Round | The evidence from your own corpus |
|---|---|
| **System design** | **23.9%** named as a skill in backend postings · **32.6%** as a stated design/architecture *duty* · and present in **essentially 100% of the loops** behind those postings |
| **Algorithms / DSA** | **14.1%** algorithms + **17.4%** data structures in backend postings — roughly double the whole-corpus figure |

> 🔴 **The correction.** An earlier version of this plan cited *"system design is named in 76.3% of backend postings"* as "the number that reorganised the plan," and moved forty hours away from DSA on its authority. **It does not reproduce.** The same document's own skills table says 23.9% four paragraphs earlier.
>
> **What survives:** system design is still a first-class daily track, because every loop contains a design round and **it decides the level you are hired at**, and level is worth more than base salary over three years.
> **What changes:** the justification is the duty data and the loop structure, not a phantom percentage — **and DSA does not drop below 300 hours.** DSA is a *gate*. Frequency is the wrong lens for a gate.

**It is not competitive programming.** Your Codeforces 1450 is a calibration instrument, not a goal.
**The target: solve a medium-hard problem you have not seen, correctly, in 25 minutes, while talking.** The last three words are the part most people skip and the part that fails loops.

## VII.2 Volume

| Period | Weeks | DSA | Design | Problems | Hours |
|---|---|---|---|---|---|
| Levels 0–3 | 1–18 | 5.5 | 2.5 | ~175 | 144 |
| Level 4 (🌙 Ramadan) | 19–26 | 5.5 → 3.5 | 2.5 → 1.5 | ~60 | 52 |
| Levels 5–7 | 27–44 | 5.5 | 2.5 | ~185 | 144 |
| Levels 8–9 | 45–52 | 7 | 5 | ~120 | 96 |
| | | | | **≈540** | **≈436** |

**Target on 12 September 2027: 540+ problems · 25+ Hard · ≥70% solved unaided inside 25 minutes · 20 written system designs · 12+ full timed loops · Codeforces ≥1750.**

> **Do not chase the count.** A problem you solved by opening the editorial after eight minutes **did not happen.** A problem you failed and rebuilt from scratch two days later **counts double.**

## VII.3 📖 THE TEXTBOOK — `DSA_Mastery.pdf`

> **325 pages · 7 parts · ~150 topics · in the project root.** This is the spine of the DSA track, and **every one of the 52 weeks in Part VI now names the exact chapters and page numbers you owe.**

### Why it works as a curriculum rather than a reference

The book tiers all 150 topics **by how often they actually appear in a loop** — Tier 1 *foundational, in almost every loop* through Tier 5 *recognise-only*. **Parts I–VI teach Tier 1–3 deeply, one topic per chapter. Part VII is a quick-reference for Tier 4–5.** That tiering is what lets 52 weeks cover the whole thing without padding: **you go deep where the frequency justifies it and shallow where it does not.**

Every deep chapter gives you nine things, and the order matters: **the idea** (explained two or three different ways — *read until one framing clicks*) → **a hand-traced worked example** → **clean Python you can reproduce from memory** → **complexity, including the naive baseline for contrast** → **tradeoffs** → 🔴 **"when to reach for it" — the exact problem-statement signals** → **common mistakes and edge cases, the failure modes interviewers hunt for** → 🔴 **interview mindset: what to name, what to ask, what to say first** → **5–8 practice problems, easy to hard.**

### 🔴 The loop the book tells you to run — and you should actually run it

| | Step | Time |
|---|---|---|
| **1** | Learn the mental model from the chapter | 10 min |
| **2** | **Trace the worked example with your hand covering the answer** | 5 min |
| **3** | 🔴 **Type the code from memory, not from the page** | 10 min |
| **4** | Drill the practice problems — 20–40 min each, hard ones up to 90 before peeking | *your Track I hours* |
| **5** | 🔴 **Revisit the chapter after you have struggled** — the triggers and tradeoffs mean ten times more once you have hit the failure mode yourself | 5 min |

> **Steps 1–3 are the 1 hour the weekly cards budget. Step 4 IS your 4.5h of problems — it is not extra.** The book's own line, and it is correct: *"Interview skill is a function of number of problems solved from memory with the timer running, not hours of reading. The book's job is to make every one of those problems a learning event instead of a guessing session."*

### 🔴 The three rules that decide whether this works

1. **Type the code from memory.** Reading code produces recognition; typing it from memory produces recall, **and recall is what a whiteboard tests.** If you cannot reproduce the chapter's implementation without looking, you have not done the chapter.
2. **Read the "when to reach for it" section twice.** Your failure log will tell you that most of your misses are **recognition** failures, not implementation ones — and that section is the direct cure for exactly that category.
3. **Come back after you fail.** Step 5 is the one everyone skips and the one that compounds. **Re-read the chapter the same week a problem from it beat you.**

### How the map was built

Every chapter is placed in the week where it is **most immediately useful** — sometimes because it matches that week's problem set, and **eleven times because it matches what you are building that week:**

| Week | The chapter | Why that week |
|---|---|---|
| **W4** | *Binary Search on the Answer* **p90** | You are tuning a frame-size parameter. **The chapter is the technique** |
| **W5** | *Bit Manipulation* **p17** | Your varint encoder *is* this chapter |
| **W7** | *LRU/LFU Cache Design* **p285** | 🔴 **You are building a caching proxy with an eviction policy the same week** |
| **W10** | *Union-Find* **p156** | Then you run it over your own crawl data to find the largest linked component |
| **W16** | *Modular Arithmetic* · *Fast Exponentiation* | The same week you derive keys |
| **W27** | *Sweep Line* + *Intervals* | 🔴 **CS144's reassembler is an interval-merge problem** |
| **W31** | *Articulation Points & Bridges* **p190** | Then you run Tarjan on your own mesh: **whose removal partitions it?** |
| **W38** | *Network Flow* **p196** | The same week you write three NP-hardness reductions |
| **W39** | *Topological Sort* **p152** | Your epoch hash chain is a DAG |
| **W45** | *Concurrency Primitives in Coding Rounds* **p289** | The same level you carry a pager |
| **W12** | *Interview & Study Strategy* **p7** | 🔴 **Re-read, not first-read.** Thirty failure-log entries later it is a different document |

**Coverage:** all 12 Part I chapters · all 10 Part II · all 17 Part III · all 16 Part IV · all 13 Part V · all 14 Part VI · and **all five Part VII quick-reference sheets, read end to end in Week 52 as the final revision pass.** Nothing is left out; the Tier 4–5 material lands late and is explicitly marked **recognise, don't implement.**

### Where it collides with the other sources — and who wins

**The book is the spine; NeetCode is the drill; Codeforces is the pressure.** When they overlap, the order is:
**1. Read the chapter** (the mental model and the trigger signals) → **2. do the chapter's own 5–8 practice problems** → **3. then the NeetCode/LeetCode set named in the week card.** If time runs out, **cut the LeetCode set, never the chapter** — the set without the model is pattern-matching, and pattern-matching is what fails you on an unseen problem.
🌙 **During Ramadan (W23–26) the book is the *only* new input** — one chapter a week, plus re-solving from the failure log. Everything else pauses.

## VII.4 Sources

| Source | Link | For |
|---|---|---|
| 🔴 **DSA Mastery** | `DSA_Mastery.pdf` — in the project root | **The spine.** 150 topics tiered by interview frequency; every week in Part VI names your exact chapters and pages. See **§VII.3** |
| **NeetCode 150 → 250** | [↗ neetcode.io/practice](https://neetcode.io/practice) | The pattern spine, W1–26. In order, grouped by pattern. **Do not skip the easy ones** |
| **LeetCode, company-tagged** | `leetcode.com` | W27–52. Filter by your seven targets, last 6 months. Premium is genuinely worth $35 for the two months before a loop |
| **AtCoder Educational DP Contest** | `atcoder.jp/contests/dp` | 🔴 **The best structured DP resource that exists, and it is free.** Problems A–L, Level 3 |
| **CSES Problem Set** | `cses.fi/problemset/` | Sorting & Searching, Dynamic Programming, Graph Algorithms, Mathematics — the curated sets |
| **Codeforces Div 2 A–D** | `codeforces.com` | Weekly, all year. Rated when it fits, virtual when it does not. Band **1450 → 1750** |
| **Codeforces EDU (ITMO)** | `codeforces.com/edu/courses` | Segment trees (W39–40), suffix structures (W41). The best free structured material for these |
| **Laaksonen, *Competitive Programmer's Handbook*** | `cses.fi/book/book.pdf` | Free. **Ch. 7** (DP), **ch. 9** (range queries), **ch. 13–15** (graphs), **ch. 26** (probability) |
| **Skiena, *The Algorithm Design Manual* 3e** | — | The *why*. **Ch. 8** (DP), **ch. 9** (intractability and reductions) |
| **Alex Xu, *System Design Interview* Vol. 1 & 2** | *(owned)* | The weekly design curriculum is built on these |
| **interviewing.io / Pramp** | `interviewing.io` · `pramp.com` | Free peer mocks. **One paid mock with a real FAANG engineer around W30 if affordable** |

## VII.5 🔗 The map — where Adyton and Track I compound

**This is the point of running them together.** Each level's build makes specific patterns *concrete*. Do those patterns that week, while the intuition is live.

| Weeks | Level | What you are building | The patterns it makes real | System design |
|---|---|---|---|---|
| **1–3** | L0 | Cache layout, working-set sweeps, latency ladder | Arrays · hashing · prefix sums · two pointers · sliding window. **The cache intuition is *why* these are fast in practice, not just in Big-O** | Estimation module; the numbers to memorise |
| **4–8** | L1 | Frame parsing, length caps, varints, fuzzing | **Binary search incl. on the answer** (frame/batch tuning literally is this) · **bit manipulation** (your varint encoder) · stacks & monotonic stacks · linked lists | URL shortener · **rate limiter** |
| **9–12** | L2 | 🔴 **The tracker co-occurrence graph** | 🔴 **Graphs: BFS/DFS, connected components, bipartite checking.** You are building and analysing a real bipartite graph of trackers and sites — **this is the cleanest DSA↔project tie in the year** · union-find · sorting | **Web crawler** · distributed job queue |
| **13–18** | L3 | Sphinx, key derivation, constant-size headers | Trees & BSTs · heaps & top-K · tries · **hashing deep-dive** | **Key-value store** · distributed cache |
| **19–26** | L4 🌙 | netns, the leak suite, the demo | 🔴 **Dynamic programming, part 1** — 1-D, 2-D, knapsack · greedy · intervals. **🌙 W23–26: no new topics. Re-solve from the log and work AtCoder DP A–L slowly** — DP is the one topic that rewards slow careful weeks, so this collision is better luck than it looks | Multi-tenant API with quotas · identity & auth |
| **27–32** | L5 | CS144: reassembler, sender, connection | 🔴 **Intervals and merging — the CS144 reassembler IS an interval-merge problem.** Do LC 56/57/435/253 the week you write it · queues & deques · DP part 2 | **Distributed message queue** · notification system |
| **33–37** | L6 | NAT traversal, SWIM gossip | 🔴 **Graph BFS again — gossip propagation IS breadth-first traversal**, and you now have a second, different instance of the same structure · shortest paths · **articulation points** — *whose removal partitions your mesh?* | **Distributed lock service** · service discovery |
| **38–44** | L7 | Raft, epoch documents, Kafka→Postgres | **Union-find** (membership) · **topological sort** (the epoch hash chain is a DAG) · reductions & NP-hardness (three written reductions in W38) · segment trees & Fenwick | **Sharded database** · **metrics pipeline** (you are building it) |
| **45–48** | L8 | k8s, observability, chaos | **Heaps & priority queues** (shedding is one) · **sliding window** (rate limiting literally is one) · volume under time pressure | Full 45-min designs, recorded, one per week |
| **49–52** | L9 | ⭐ AS graph, weighted selection, the curve | 🔴 **Probability, expectation and weighted sampling.** **LC 528 "Random Pick with Weight" *is* capacity-weighted relay selection** — the prefix-sum-plus-binary-search structure is exactly what your selector does on every circuit build · randomised algorithms · number theory | **Recommendation/ranking** · search |

⚠️ **Where the tracks do NOT meet:** string algorithms (KMP, Z-function, suffix automata), combinatorics, geometry, and advanced number theory get **zero** reinforcement from Adyton. **These are where you will be weakest.** Weeks 39–41 and the W48 weak-area blitz exist for them, and the disconnection is a reason to do them *more* carefully, not less.

## VII.6 The problem sets, level by level

### L0 · W1–3 · ~28 problems
**NeetCode 150:** Arrays & Hashing (all 9) · Two Pointers (all 5) · Sliding Window (all 6)
**LeetCode:** 1 Two Sum · 217 Contains Duplicate · 242 Valid Anagram · 49 Group Anagrams · 347 Top K Frequent · 238 Product of Array Except Self · 36 Valid Sudoku · 128 Longest Consecutive Sequence · 125 Valid Palindrome · 167 Two Sum II · 15 3Sum · 11 Container With Most Water · 42 Trapping Rain Water · 121 Best Time to Buy and Sell Stock · 3 Longest Substring Without Repeating · 424 Longest Repeating Character Replacement · 76 Minimum Window Substring · 239 Sliding Window Maximum
**CSES:** *Sorting and Searching* — the first eight
🏁 **Capstone:** **LC 76 Minimum Window Substring**, from scratch, narrated, under 25 minutes

### L1 · W4–8 · ~44 problems
**Patterns:** binary search including **on the answer** · bit manipulation · stack & monotonic stack · linked lists
**LeetCode — binary search:** 704 · 74 Search a 2D Matrix · 153/33 Rotated Sorted Array · 875 Koko Eating Bananas · 1011 Capacity To Ship Packages · 410 Split Array Largest Sum · 4 Median of Two Sorted Arrays
**LeetCode — bit:** 136 Single Number · 191 Number of 1 Bits · 338 Counting Bits · 190 Reverse Bits · 371 Sum of Two Integers · 268 Missing Number · 78 Subsets (bitmask form)
**LeetCode — stack:** 20 Valid Parentheses · 155 Min Stack · 150 Evaluate RPN · 22 Generate Parentheses · 739 Daily Temperatures · 853 Car Fleet · 84 Largest Rectangle in Histogram
**LeetCode — linked list:** 206 · 21 · 143 · 19 · 138 Copy List with Random Pointer · 2 Add Two Numbers · 141 Linked List Cycle · 287 Find the Duplicate Number · 146 LRU Cache
🔗 **The tie:** **875 and 1011 are binary search on the answer, which is exactly how you pick a frame-size or batch parameter.** You will do the real version in `lab/bench` this month.
🏁 **Capstone:** **LC 146 LRU Cache** from memory, then explain why your relay's circuit cache uses the same structure

### L2 · W9–12 · ~42 problems 🔴 *the graph level*
**Patterns:** graphs — BFS, DFS, connected components, bipartite · union-find · sorting
**LeetCode — graphs:** 200 Number of Islands · 133 Clone Graph · 695 Max Area of Island · 417 Pacific Atlantic · 130 Surrounded Regions · 994 Rotting Oranges · 286 Walls and Gates · 207/210 Course Schedule I & II · 261 Graph Valid Tree · 323 Connected Components · 127 Word Ladder · 785 **Is Graph Bipartite** · 886 Possible Bipartition
**LeetCode — union-find:** 684 Redundant Connection · 547 Number of Provinces · 721 Accounts Merge · 990 Satisfiability of Equality Equations
**CSES:** *Graph Algorithms* — the first ten
**Codeforces:** tag `graphs`, rating 1400–1600, 6 problems
🔗 **The tie, and it is exact:** 🔴 **LC 721 "Accounts Merge" is literally the linkage problem.** Merging accounts that share an email is structurally identical to merging browsing sessions that share a tracker identifier — **and you are implementing the real version in `lab/linkage` the same month.** Do 721 the week before you write the analysis, and notice.
🏁 **Capstone:** **LC 721 from scratch**, then run union-find over your own crawl data and report the size of the largest connected component of linked sessions

### L3 · W13–18 · ~40 problems
**Patterns:** trees & BSTs · heaps & top-K · tries · hashing
**LeetCode — trees:** 226 · 104 · 543 · 110 · 100 · 572 · 235 · 102 · 199 · 1448 · 98 Validate BST · 230 Kth Smallest · 105 Build from Preorder+Inorder · 124 Max Path Sum · 297 Serialize/Deserialize
**LeetCode — heaps:** 703 · 1046 · 973 K Closest Points · 215 Kth Largest · 621 Task Scheduler · 355 Design Twitter · 295 Find Median from Data Stream
**LeetCode — tries:** 208 Implement Trie · 211 Design Add and Search Words · 212 Word Search II
**CSES:** *Tree Algorithms* — the first six
🏁 **Capstone:** **LC 295 Find Median from Data Stream** — two heaps, from memory, and explain where the same structure appears in your latency harness

### L4 · W19–26 · ~60 problems 🌙 *reduced W23–26*
**Patterns:** 🔴 **dynamic programming part 1** — 1-D, 2-D, knapsack · greedy · intervals
🔴 **The method, every single time, no exceptions:** state the subproblem **in words** → write the recurrence **in a comment** → identify the base cases → *then* choose memoised recursion or a bottom-up table → optimise space last. **Do not write code before the recurrence exists in a comment.** That habit is the difference between solving DP and guessing at it, and interviewers can see which one you are doing.
**LeetCode — 1-D DP:** 70 · 198/213 House Robber I & II · 91 Decode Ways · 139 Word Break · 322 Coin Change · 518 Coin Change II · 300 LIS · 152 Maximum Product Subarray · 416 Partition Equal Subset
**LeetCode — 2-D DP:** 1143 LCS · 🔴 **72 Edit Distance** · 62 Unique Paths · 64 Minimum Path Sum · 221 Maximal Square · 5 Longest Palindromic Substring · 647 Palindromic Substrings · 10 Regular Expression Matching
**LeetCode — greedy & intervals:** 53 Maximum Subarray · 55/45 Jump Game I & II · 134 Gas Station · 846 Hand of Straights · 56 Merge Intervals · 57 Insert Interval · 435 Non-overlapping Intervals · 253 Meeting Rooms II
🔴 **AtCoder Educational DP Contest, problems A–L** — `atcoder.jp/contests/dp`
**CSES:** *Dynamic Programming* — the first ten
🌙 **W23–26 (Ramadan, 3.5h):** **no new topics.** Re-solve every DP failure from the log, and work AtCoder DP A–L slowly.
🏁 **Capstone:** **LC 72 Edit Distance from memory** — recurrence in a comment first, then the space-optimised version

### L5 · W27–32 · ~44 problems
**Patterns:** 🔴 **intervals and merging** · queues & deques · DP part 2 · design
🔗 **The tie, and it is exact:** 🔴 **CS144 Checkpoint 1 is the reassembler: you receive overlapping, out-of-order byte ranges and must merge them into a contiguous stream. That is LC 56/57/435/253 with a deadline.** Do the interval set the same week you write the reassembler, and you will write it faster and understand it better.
**LeetCode — intervals:** re-solve 56, 57, 435, 253 *after* Checkpoint 1 and notice how much easier they are · 763 Partition Labels · 1834 Single-Threaded CPU
**LeetCode — queues/deques:** 239 Sliding Window Maximum (re-solve) · 622 Design Circular Queue · 933 Number of Recent Calls
**LeetCode — DP part 2:** 309 Best Time to Buy and Sell with Cooldown · 494 Target Sum · 97 Interleaving String · 329 Longest Increasing Path in a Matrix · 115 Distinct Subsequences · 312 Burst Balloons
**LeetCode — design:** 155 · 380 Insert Delete GetRandom O(1) · 232/225
**CSES:** *Range Queries* — the first six
🏁 **Capstone:** implement the CS144 reassembler's interval logic as a standalone LeetCode-shaped problem, with your own tests, and post it

### L6 · W33–37 · ~40 problems
**Patterns:** 🔴 **graph part 2** — shortest paths, MST, **articulation points** · backtracking
**LeetCode — shortest path:** 743 Network Delay Time (Dijkstra) · 787 Cheapest Flights Within K Stops · 1631 Path With Minimum Effort · 778 Swim in Rising Water · 1976 Number of Ways to Arrive at Destination
**LeetCode — MST/union-find:** 1584 Min Cost to Connect All Points · 1489 Critical Connections **← this IS articulation points, and it IS the question "which relay's removal partitions my mesh"**
**LeetCode — backtracking:** 78 · 90 · 39 · 40 · 46 · 47 · 79 Word Search · 131 Palindrome Partitioning · 51 N-Queens
**CSES:** *Graph Algorithms* — Dijkstra, Floyd–Warshall, and the cycle-finding set
**Codeforces:** tag `shortest paths` + `dsu`, 1500–1700, 6 problems
🔗 **The tie:** 🔴 **LC 1489 Critical Connections is Tarjan's bridge-finding algorithm. Run the same algorithm over your own 30-node mesh's gossip topology and report which nodes are articulation points.** Same algorithm, interview and product.
🏁 **Capstone:** **LC 787 Cheapest Flights Within K Stops** — and explain why it is *not* plain Dijkstra, which is the thing interviewers are checking

### L7 · W38–44 · ~60 problems
**Patterns:** **topological sort** · union-find (again, harder) · **reductions & NP-hardness** · segment trees & Fenwick
**W38 is a proving week:** three written reductions from **Skiena ch. 9**. Not code. Prose proofs. This is the week you learn what "NP-hard" actually licenses you to say in a design interview.
**LeetCode — topological:** 207/210 (re-solve) · 269 Alien Dictionary · 310 Minimum Height Trees · 1136 Parallel Courses · 2115 Find All Possible Recipes
**LeetCode — advanced union-find:** 803 Bricks Falling When Hit · 924 Minimize Malware Spread · 1202 Smallest String With Swaps
**Codeforces EDU:** **Segment Tree, parts 1 and 2** — `codeforces.com/edu/course/2/lesson/4`
**LeetCode — range queries:** 307 Range Sum Query Mutable · 315 Count of Smaller Numbers After Self · 493 Reverse Pairs
**CSES:** *Range Queries* — the rest
🔗 **The tie:** 🔴 **the epoch hash chain is a DAG and validating it is a topological order.** Do the topo set the week you implement epoch validation.
🏁 **Capstone:** **LC 269 Alien Dictionary** — and it is the same shape as deriving a consistent relay ordering from pairwise constraints

### L8 · W45–48 · ~60 problems 🎯 *applications are live*
**Topic learning is over. Volume under time pressure and loop simulation.**
Company-tagged sets, timed at 25 minutes, **spoken aloud, recorded.** Heaps & priority queues, sliding window, and **the weak-area blitz**: strings (KMP, Z-function via Codeforces EDU), combinatorics, geometry — the four areas Adyton gave you nothing for.
**Codeforces EDU:** **String Algorithms** — `codeforces.com/edu/course/2/lesson/3`
🏁 **Capstone:** a full timed loop, four rounds, one day, recorded and graded

### L9 · W49–52 · ~60 problems
**Patterns:** 🔴 **probability, expectation, weighted sampling** · randomised algorithms · number theory
🔗 **The tie, and it is exact:** 🔴 **LC 528 "Random Pick with Weight" IS capacity-weighted relay selection.** Prefix sums plus binary search is precisely what `adyton-core/select` does on every circuit build. **And the entire level is about a randomness dial**, so the probability set is not adjacent to the work — it *is* the work.
**LeetCode — weighted sampling:** 🔴 **528** · 710 Random Pick with Blacklist · 382 Linked List Random Node · 398 Random Pick Index · 497 Random Point in Non-overlapping Rectangles
**LeetCode — randomised:** 384 Shuffle an Array · 470 Rand10 from Rand7 · 478 Random Point in a Circle · 519 Random Flip Matrix
**LeetCode — expectation:** 837 New 21 Game · 808 Soup Servings · 688 Knight Probability in Chessboard · 1230 Toss Strange Coins
**LeetCode — math:** 50 Pow(x,n) · 69 Sqrt(x) · 29 Divide Two Integers · 166 Fraction to Recurring Decimal · 372 Super Pow · 204 Count Primes
**CSES:** *Mathematics* — the first twelve
**Reading:** **Mitzenmacher & Upfal ch. 5** (balls into bins) — 🔴 **this is literally your relay-load-distribution problem**
🏁 **Capstone:** 🔴 **LC 528, then implement the same weighted-sampling structure inside `adyton-core/select` and verify the distribution over 10⁶ draws against the intended weights.** Same algorithm, interview and product, same week.

## VII.7 🔴 The failure log — the part that actually produces improvement

**Solving problems does not make you better. Reviewing failures does.** `dsa/FAILURES.md`, an entry every time you miss the time box or solve with the wrong approach.

```
## <date> · <link> · <topic>
**Time box:** 25 min.  **Outcome:** failed / solved at 41 min / wrong approach
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

**Do the count in the rest weeks — W12, W26, W37, W48.** Twenty minutes, and it redirects the next quarter. **Most people never do it and spend a year fixing the wrong thing.**

**Re-solve discipline:** every failed problem re-solved from scratch three days later, **without looking at your previous solution.** The highest-return habit in the track and the easiest to skip.

## VII.8 Time boxes

| Difficulty | Box | On expiry |
|---|---|---|
| Easy | 15 min | Read the solution, log as failure, re-solve from scratch the same day |
| Medium | 25 min | Read the **approach only**, retry 15 min, then the full solution. Log |
| Hard | 45 min | Same protocol |

**Never exceed the box.** An hour spent stuck teaches less than reading the solution and re-solving it twice.

## VII.9 System design — 2.5h/week from Week 1, 20 written designs

**Each produces a full design doc:** Summary · Context · Goals · **Non-Goals** · Proposal · **Alternatives Considered (minimum three)** · Risks · Rollout · Operational Impact.

**The 45-minute structure:** 0–5 requirements, functional **and** non-functional, written on the board · 5–10 estimation (**round aggressively, show the arithmetic**) · 10–15 API and data model · 15–25 high-level design (**state your choices as choices**) · 25–40 deep dive, where the grade is decided · 40–45 failure modes and 10×.

> **The single highest-leverage habit: say the words "I'm optimising for X, which costs me Y." Every time.**

**Numbers to memorise:**
```
1 machine:  ~10-50k QPS simple requests · 64-256GB RAM · 10-40 cores
Postgres:   ~5-50k simple QPS · ~1-5k writes/s with fsync
Redis:      ~100k-1M ops/s single instance (single-threaded!)
Kafka:      ~100k-1M msg/s per broker (small, batched)
Sockets:    ~10-50k concurrent connections per commodity node (memory-bound)
NVMe:       ~500k-1M IOPS · 3-7 GB/s          Network: 10 Gbps = 1.25 GB/s
RTT:        same-AZ ~0.3-0.5ms · cross-region 30-150ms · Cairo↔Frankfurt ~60-90ms
Crypto:     AES-GCM ~1-5 GB/s/core · X25519 ~20-50k ops/s/core
Time:       1 day ≈ 10^5 s · 1M req/day ≈ 12 QPS · 1B req/day ≈ 12k QPS
```

**The twenty designs, in order:** estimation warm-up · URL shortener · rate limiter · web crawler · distributed job queue · key-value store · distributed cache · multi-tenant API with quotas · identity and auth · distributed message queue · notification system · distributed lock service · service discovery · sharded database · metrics/monitoring pipeline · **a privacy relay network** *(you are building it — practise the move of answering from your own system)* · recommendation and ranking · search · a system with end-to-end encryption · **design Tor** *(the final one, W52)*

> 🔴 **Your unusual advantage.** Most candidates answer system design from books. **You can answer from a system you built, operated, and broke twenty times on purpose.** Asked to design a proxy tier, a metrics pipeline, a service-discovery system or anything with identity in it — **do not recite.** Say *"I did this; here is what I chose, here is the number I measured, and here is what it cost me."* **Practise that move deliberately in the W46 mock**, because it does not happen naturally under pressure.

## VII.10 Mocks and loops

| When | What |
|---|---|
| **W30** | First human mock · **one paid mock with a real FAANG engineer, if affordable** |
| **W40** | 🔴 **The Raft Figure 8 whiteboard test** — a checkable gate, not a formality. A human watches you draw it from memory in under five minutes |
| W34, W38, W42 | Monthly mock, one round |
| **W44** | 🔴 **Full timed loop #1 — four rounds in one day**, and the **Final Gauntlet** week |
| W45–52 | Weekly, escalating to two per week from W50. **Loops #2 through #12** |

**A "full timed loop" means** two 45-minute coding rounds with a human, one 45-minute system design, one 30-minute behavioural, **in a single day** with realistic breaks. **Not four sessions across a week.** The exhaustion is what you are training for, and it is what surprises people at their first real onsite.

**Speak while you solve, always, including alone.** The most common cause of a failed coding round in a candidate who *can* solve the problem is silence.

## VII.11 📈 Track I exit criteria
- [ ] **540+ problems, ≥70% solved unaided within 25 minutes**
- [ ] A random unseen Medium, **narrated**, in ≤25 min, ≥80% of the time, on video
- [ ] Complexity stated before code, every time
- [ ] **25+ Hard problems** · **failure-log review queue empty** · **Codeforces ≥1750**
- [ ] **20 system designs as written docs** and 20 more practised verbally
- [ ] **12+ full timed loops** · **14 behavioural stories on video, ≥4 from Logic Leap**
---
---

# PART VIII — TRACK J: CRAFT, CAREER & VISIBILITY

> What separates an L4 from an L5 is not knowing more systems facts. It is **judgement, communication, and impact beyond your own keyboard.**
> **2h/week, 8h from Week 45. One artifact every two weeks.**

## VIII.1 Design docs and ADRs — the unit of senior technical work

Promotion at every large company is decided by written artifacts.

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

**Scheduled this term:** `scope.md` (W1) · `threat-model.md` (W8) · `linkage-methodology.md` (W11) · `packet-format.md` (W17) · `browser-delta.md` (W25) · `transport.md` (W31) · `mesh.md` (W36) · `consensus.md` (W43) · `slo.md` (W47) · `path-selection.md` (W52). **Ten, plus ten ADRs in W52.**

**The ten ADRs:** 0001 the language boundary · 0002 QUIC over TCP, from your own chart · 0003 netns over browser containers · 0004 middle-only relays and the scope decision · 0005 Sphinx over a hand-rolled format · 0006 Raft for the directory rather than gossip or a fixed authority · 0007 what the DP budget protects and what it costs · 0008 simulator-first testing and how you validated the simulator · 0009 the randomness parameter's operating point · 0010 **everything you deliberately do not defend against.**

## VIII.2 Writing — post results, not progress

**Not "day 47 of my coding journey."** The findings. And you will have unusually good ones.

| Week | The post | Why it travels |
|---|---|---|
| **W12** | 🔴 **"I crawled 5,000 sites to find out how linkable the web actually is. Here's the graph."** | **Your first real artifact, and it lands in month three.** A current, reproducible measurement of the thing everyone asserts. **Front-page candidate** |
| **W16** | **"A four-byte length prefix killed my own server"** | The parser attack, and the three memory bugs your fuzzer found in your own code the same week |
| **W25** | 🔴 **"Your proxy leaks four ways and three of them aren't the proxy's fault"** | WebRTC, IPv6, DNS, the kill-switch race. **Universally useful and almost nobody writes it down. Front-page candidate** |
| **W32** | 🔴 **"I implemented TCP so I'd stop guessing about head-of-line blocking. Here's the graph."** | A real measurement behind folklore everyone repeats |
| **W37** | **"What fraction of real NAT pairs can actually hole-punch?"** | Measured, by NAT type, with the relay-fallback cost |
| **W44** | **"Where I put consensus in a relay network, and why not everywhere"** | The directory design, and why disagreement is a fingerprint |
| **W47** | 🔴 **"I found coordinated omission in my own benchmark harness and re-measured eight months of results"** | **Engineers at exactly your target companies will read this** |
| **W52** | 🔴 **"AS-aware path selection makes you predictable. Here is the curve."** | ⭐ **The plot is the post.** The most novel thing you will write this year, and it does not exist publicly |

**Cross-post to:** Hacker News · Lobsters · `r/netsec` · `r/privacy` · the **tor-dev** and **tor-relays** mailing lists · the Matrix/IRC channels of the projects you cite. **One post reaching the front page generates more inbound recruiting than 200 applications.**

**Give one talk.** A Cairo meetup counts. Explaining Sphinx's size invariant out loud will expose every gap in your understanding, which is why it is valuable.

## VIII.3 Open source — the Arti track

**A merged PR into a project people have heard of beats three personal projects**, because someone with commit rights judged your code good enough to ship.

**The ladder:** use it seriously → fix the docs where they confused you (this gets you through the CLA and CI process once, cheaply) → a `good first issue` → **a bug you personally hit** → **a bug found by fuzzing** (maintainers love a minimal reproducer) → a feature, after discussing design in an issue first.

**Highest-leverage targets, given Adyton:**
- 🔴 **Arti** (the Tor Project's Rust implementation) and **the Tor specifications.** You will read `spec.torproject.org` all year and you *will* find ambiguities. **A Tor Project contribution is the single most on-point CV line this project can generate**
- **`pion/ice` and `pion/webrtc`** — you use them hard in Level 6 and will hit edges
- **`ngtcp2`** — QUIC, Level 5
- **OpenWPM** — Level 2, and the most approachable of the list
- **`libsodium` bindings**, **`hashicorp/memberlist`** (SWIM in production), **`etcd/raft`**

**Budget: Levels 5–8. Target: 3+ merged, one non-trivial.**

## VIII.4 🔴 The referral problem, and how to solve it from Egypt

**Harder than the degree question — which your own data settles at one posting in 569.** A cold application from Cairo to a Dublin req competes with hundreds of in-region applicants needing no sponsorship. **A referred application is read by a human. A cold one frequently is not.**

**The mistake:** waiting until Week 45 and messaging strangers. A referral is someone putting their reputation on your application. **Nobody does that for a person who appeared in their inbox last Tuesday.**

### ⏰ The pipeline opens Week 13 — 7 December 2026.

Earlier than in any previous version of this plan, and for a specific reason: **you will have a publishable measurement at Week 12.** That is your opening line, and it is far better than "I'm learning distributed systems."

**Channel 1 — the Egyptian engineering diaspora. Highest return.** Substantial numbers at Google Dublin and Zurich, Meta London, Amazon Dublin, Microsoft. LinkedIn alumni search on your university, then other Egyptian universities, filtered by company. **They were where you are. They are disproportionately willing to help and disproportionately under-asked, because most people are too embarrassed to reach out.**

Never "can you refer me":

> I'm a backend engineer in Cairo. I just finished a crawl of 5,000 sites measuring how much cross-site linkage there actually is — [link to the write-up] — as the groundwork for a privacy relay client I'm building. I'd value fifteen minutes of your view on [one specific technical question you genuinely have]. No obligation and no ask beyond that.

Then have the conversation, be interesting, follow up two months later with what you built. **The referral, if it comes, comes on its own.** **Target: 3 conversations/month from W13. By W45 that is 24–28 people who know what you are building.**

**Channel 2 — build in public** (§VIII.2). **Channel 3 — OSS, especially Arti** (§VIII.3). **Channel 4 — the technical report** (W51): most candidates have a GitHub link; **a 20-page report with benchmarks and an honest limitations section is a different object and it gets forwarded.** **Channel 5 — the privacy research community**: the PETS and FOCI communities are small, welcoming, and read this kind of work. Submitting the guard-placement curve as a poster is networking even if rejected.

**The direct ask, Week 45, to people you have known for eight months:**

> I'm applying to [specific role, specific office] this week. Here's the project [link] and my CV. If you're comfortable referring me I'd be grateful; if not, no problem at all — and I'd still value knowing whether the CV reads clearly to someone inside.

**The second half matters.** It gives them an out that is not a rejection, and it frequently produces useful feedback from people who will not refer you.

## VIII.5 🔴 The Logic Leap track — sourcing what a solo project cannot

**Mentoring 37.0% · Communication 34.8% · Collaboration 31.2% · Leadership 17.2%.** Adyton demonstrates **none** of them. **Left to chance you arrive at Week 46 with fourteen stories, twelve of them about a side project, and interviewers notice.**

**One hour a week of Track J is reserved for this. Seek these out, in this order:**

| Weeks | What to deliberately do at Logic Leap | The story it becomes |
|---|---|---|
| **1–12** | **Ask to review other people's PRs**, seriously, weekly. Leave the kind of comment you would want | *"Improving code quality without authority"* |
| **13–26** | **Write one design doc for real work** and circulate it before implementing. Use the §VIII.1 template | *"Aligning people on a technical decision"* — the Alternatives section is the artifact |
| **13–26** | **Onboard or unblock someone** — a new joiner, an intern, a colleague on unfamiliar code. Track what they were stuck on | *"Mentoring"* — the largest soft gap at 37.0% |
| **27–44** | **Take one cross-team dependency end to end** — something needing another team's input, where you drive the conversation | *"Cross-functional work"* |
| **27–44** | **Disagree with a senior person, in writing, with data**, and handle the outcome either way | *"Disagreeing with a senior person"* — a required story you cannot fabricate |
| **45–52** | **Lead one thing end to end:** scope, plan, delegate a piece, ship, own the outcome | *"Leading a project"* |

**Log each in `career/LOGICLEAP.md` as it happens, with dates and specifics.** You will not remember the details in month eleven, and vague behavioural answers are the most common way strong technical candidates fail loops.

## VIII.6 The fourteen behavioural stories

STAR-L: Situation, Task, **Action — 60% of the words, "I" not "we"**, Result **with a number**, Learning. Written by W46, recorded on video, then five mock behavioural rounds with a human.

| # | Prompt | Your story |
|---|---|---|
| 1 | A technically hard problem | Sphinx's size invariant, or the guard-placement trade-off |
| 2 | 🔴 **Finding a serious problem in your own work** | **Coordinated omission in your own harness (W47). Your best story** — it shows the scepticism about your own results that senior engineers are selected for |
| 3 | Being wrong and changing course | The design your own simulator broke, or AS-aware selection turning out to have a cost you had not modelled |
| 4 | A failure | The level where your estimate was most wrong, **with the ratio from `RETROSPECTIVE.md`** |
| 5 | Shipping under a hard constraint | Zero budget forcing the ARM port and the 40-node memory ceiling |
| 6 | An incident | **Clock skew, or the epoch-disagreement incident — nothing fails loudly and every dashboard stays green** |
| 7 | A decision with incomplete information | QUIC over TCP, argued from your own head-of-line-blocking chart |
| 8 | Pushing back / saying no | 🔴 **Three real ones: no public network, no browser fork, no overclaim.** Each has a written reason |
| 9 | Learning something new fast | The Double Ratchet spec, or CAIDA's AS-relationship inference |
| 10 | Improving something unasked | The fuzzing corpus, or the leak suite in CI |
| 11 | Proudest achievement | ⭐ The trade-off curve |
| 12 | Mentoring / unblocking | The peer runbook test and the four gaps it exposed |
| 13 | Disagreeing with a senior person | **A real one from Logic Leap** |
| 14 | Something from Logic Leap | 🔴 **The 1,000-concurrent-call voice pipeline, or the permission-resolution rewrite that cut latency 62%.** Use them — they are real production systems at real scale |

**The rules that decide the score:** numbers always · **"I" not "we"** · the Learning is not optional · **90 seconds then stop** · Amazon maps each to a Leadership Principle and **drills with follow-ups that catch fabricated stories — use real ones.**

## VIII.7 CV versions

**One page. Every line traceable to something in the repo the day you write it.**

**Structure:** 1. Name, GitHub, **"Cairo, Egypt · open to relocation · requires EU/UK sponsorship"** · 2. Two-line summary · 3. 🔴 **SELECTED PROJECT — ADYTON, 5–7 bullets. The largest section, ABOVE employment** · 4. Experience — Logic Leap, 3–4 bullets, quantified · 5. Skills, keyword-matched to the corpus · 6. **Education — one line, last.**

> **The degree line:** *"BSc Management Information Systems, Alexandria University, 2025."* **No parenthetical. No "(self-taught in CS)". No apologetic adjective.** The project section made the argument; restating it next to the degree draws attention to the anxiety rather than the evidence.

> 🔴 **The top third is screening surface, not interview content.** Sphinx and the guard-placement curve are what you talk about for forty-five minutes. **The top third must contain Java, distributed systems, AWS, Python, Go, Kubernetes, Kafka** — in roughly that order, because those are the verified frequencies and a recruiter reads nothing else.

**Every bullet is X-Y-Z:** *"Accomplished [X] as measured by [Y], by doing [Z]."*

**CV v1 — W12** *(not for applying; it exists so an unexpected opportunity does not find you writing a CV in a panic)*
> **ADYTON — privacy relay client with per-identity compartments** · C++20, Java 21, Go, Python · [repo]
> · **Measured cross-site linkability across 5,000 real websites** with a purpose-built crawler, constructing the tracker co-occurrence graph and quantifying what fraction of a browsing session a single third party can reconstruct. Published with a reproducible methodology.
> · Built a C++20 relay daemon whose frame parser survives **one hour of libFuzzer clean with a committed corpus**, under ASan/UBSan/TSan on every CI run; reported the three memory bugs fuzzing found before it was clean.

**CV v2 — W26** ★
> · Implemented **Sphinx constant-size onion packets** (Danezis & Goldberg, IEEE S&P 2009); serialised packet size is **byte-identical regardless of hops remaining**, asserted by property test.
> · Built **OS-level identity compartments** — one browser profile per identity in its own Linux network namespace on its own circuit with its own pinned exit — with a **CI leak suite covering WebRTC, IPv6, DNS, kill-switch and cross-compartment linkage**; the suite going red blocks merge.

**CV v3 — W37**
> · Implemented **TCP from the byte stream up** (Stanford CS144, **all eight checkpoints passing**) and used it to measure head-of-line blocking across six loss profiles, producing the transport decision for the system.
> · Built **per-hop QUIC transport** (ngtcp2) with handshake fingerprint normalisation, and a **20–40 node mesh** with NAT traversal and SWIM gossip: **p50 circuit recovery <800ms under 20% churn**, with real hole-punch success rates measured by NAT type.

**CV v4 — W45** *(the one you apply with)*
> · Implemented **Raft** as the network's directory (**MIT 6.5840 Labs 1–3 passing**, including `TestFigure8Unreliable`): **100% of peers hold the identical epoch consensus hash within 30s under 20% churn.** Built the telemetry plane on **Kafka → Postgres** with differential-privacy noise applied before publication and a budget that fails closed.
> · Deployed the mesh on **Kubernetes across three regions at $0/month**; rolling restart of all relays drops **zero circuits**. Ran a chaos programme of **20+ injected incidents**, each with alerting, root cause and a runbook.
> · ⭐ **Published the AS-diversity-versus-predictability trade-off curve** for AS-aware path selection, including the guard-placement attack run against my own selector on real CAIDA topology data. **No equivalent public measurement exists.**

## VIII.8 Targets and applications

| Company | Offices | Note |
|---|---|---|
| 🔴 **Cloudflare** | London, Lisbon, Austin | **The single best fit in the industry for this project.** They operate a hop of iCloud Private Relay, shipped Privacy Pass, built ODoH and Oblivious HTTP, run a QUIC stack and a Rust proxy. **Everything you build this year is their day job** |
| **Apple** | London, Munich, Cambridge | iCloud Private Relay is the direct comparable |
| 🔴 **Tailscale** | Remote, global | **NAT traversal is their entire company.** Your Level 6 is their product |
| **Mullvad · Proton · Brave · Mozilla · DuckDuckGo** | Sweden / Switzerland / remote | Privacy-native. Small, technical, and they will *read the repo* |
| **Signal** | Remote | Crypto engineering; they hire few and read carefully |
| **Fastly · Akamai** | London, remote | Edge and proxy at scale |
| **Google** | Dublin, Zurich, London, Munich, **Warsaw** | Zurich strongest and hardest. **Warsaw more accessible** |
| **Meta** | London, Dublin | London is the main EMEA engineering site |
| **Amazon / AWS** | Dublin, London, Berlin, Luxembourg | Most reqs, **most accessible tier-1 entry**; their networking org is enormous |
| **Microsoft** | Dublin, London, Cambridge, Munich, **Cairo** | 🔴 **The only tier-1 with engineering in Egypt. Apply there in W45 regardless** — a local tier-1 role is a legitimate route to an internal transfer |
| **Stripe** | Dublin, London | **Values written communication — your report and ADRs are unusually well matched** |
| **Datadog · Grafana Labs · Canonical · Bloomberg** | Paris, Dublin, remote, London | Systems-heavy, and Canonical hires globally and remote |

**Calibration tier** (W33–44, no cooldown risk): Instabug, Swvl, Halan, Paymob, MaxAB (Cairo); Careem, Talabat, Tabby (Gulf); any European startup with a real systems interview.

| Weeks | Volume | Targets |
|---|---|---|
| 33–44 | 2–3/month | **Calibration tier only.** By W45 you will have sat 15–20 real rounds |
| 45–47 | 16/week (48) | **Cloudflare, Tailscale, Apple, Mullvad, Proton first** — your best-fit tier — then tier-1 EMEA |
| 48–50 | 12/week (36) | Remaining tier-1 and second tier |
| 51–52 | 8/week | Fill gaps; the pipeline is mostly conversion now |

**≈130 applications**, every one logged in `career/APPLICATIONS.md` — date, company, office, role, referral (y/n, by whom), response, stage, outcome. **You cannot reconstruct this later and you need it to compute response rate and stage conversion.**

**Sequence your loops:** 3–4 companies you care less about *first*. **Your fifth loop is dramatically better than your first.** Then overlap the real ones so offers arrive within ~2 weeks — **competing offers are the only real leverage.**

### 🚨 If the response rate is low (checked W50, ~84 out)
**Below 10%, stop and diagnose before sending more with the same CV.** In order: **targeting** (reqs wanting 5+ years will not respond regardless — check the level distribution) · **the sponsorship filter** (some reqs auto-reject; invisible, and not about you) · **the top third of the CV** (if it does not contain Java 53.3%, distributed systems 48.9%, AWS 48.9%, Python 43.5%, Go 38.0%, Kubernetes 30.4%, Kafka 20.7%, it is miscalibrated) · **the referral ratio** (under a third referred? the fix is §VIII.4, not more applications).

**Do not respond to a low response rate by increasing volume.** That converts a fixable problem into a burned target list.

## VIII.9 Negotiation — weeks 50–52, the highest hourly-rate work you will ever do

1. **Never give a number first**, including on the recruiter's first call. *"I'd like to focus on whether this is the right fit; I'm confident we can align on compensation"* is a complete answer and it is expected.
2. **Competing offers are the only real leverage.** Hence overlapping loops.
3. **Negotiate the whole package:** base · equity **and its vesting schedule** · sign-on (most flexible) · **level — worth more than any of the above over three years** · start date.
4. 🔴 **Applying from Egypt to a European role creates an anchoring risk.** Recruiters may benchmark against Egyptian salaries. **Do not accept that framing** — compensation is for the role in that location. Know your target level's `levels.fyi` number for that company and office **before the first call.**
5. **Read: Haseeb Qureshi, "Ten Rules for Negotiating a Job Offer."** Plausibly a five-figure return for two hours.
6. Be gracious. You will work with these people.

## VIII.10 What the loops look like (verify with your recruiter)

| Company | Loop |
|---|---|
| **Google** | Phone screen → 2–3 coding, 1 system design, 1 Googleyness & Leadership. Then **hiring committee and team matching** — a strong loop can stall at team match. **Normal, not a rejection** |
| **Meta** | Phone screen (**2 problems in 45 min — speed matters more here than anywhere**) → 2 coding, 1 system design, 1 behavioural |
| **Amazon** | OA → 4–5 rounds, **every round includes Leadership Principle questions.** The **Bar Raiser** is external with veto power |
| **Microsoft** | Coding + design + an "as appropriate" round with a senior leader |
| 🔴 **Cloudflare / Tailscale / Stripe / Datadog / Mullvad** | **Practical over puzzle:** debugging unfamiliar code, extending real code, a deep systems discussion, plus design. **Adyton prepares you for these better than any other project could, and these are your best-fit employers** |

**Leveling:** L3/E3 (new grad) → **L4/E4 (2–5 yrs)** → **L5/E5 (5+ yrs, owns ambiguous projects end to end — where system design decides it).** **Interview for the level your evidence supports.** Being under-levelled costs years of compensation; push back with evidence if the loop went well.

## VIII.11 The six pinned repos

```
📌 adyton            Privacy relay client with per-identity compartments
                     C++20 / Java 21 / Go / Python
                     ★ architecture diagram + headline numbers + the honesty and
                       scale statements, all in the first screen

📌 linkage           How linkable is the web? A 5,000-site measurement.
                     ★ THE GRAPH. And the methodology, so someone can redo it.

📌 leakproof         The suite that tries to break my own compartments
                     ★ WebRTC / IPv6 / DNS / kill-switch / cross-compartment. In CI.
                       Its going red is the alarm.

📌 guardplace        ⭐ AS-aware path selection makes you predictable. The curve.
                     ★ One plot. It does not exist anywhere else.

📌 minnow-plus       A TCP that passes CS144's suite, benchmarked against the kernel's
                     ★ six network profiles, three metrics, and the HOL-blocking chart

📌 incident-lab      Six famous outages reproduced locally, with verified fixes
                     ★ the table of outages is the hook
```

**Every README, first screen:** one sentence saying what it is · an architecture diagram · **the headline number or chart** · `make demo`.
**Profile README:** three sentences about what you work on, then the six with their numbers. **No badge walls. No language-percentage charts.**
---
---

# PART IX — ASSESSMENT, THE CUT ORDER, AND TRACKING

## IX.1 The three proofs

You do not "finish" a level. You **prove** it, three ways.

| Proof | What | Why |
|---|---|---|
| **1. The Exam** | The written questions at the level's end, no notes, timed | Retrieval under pressure — the interview condition |
| **2. The Artifact** | The build, exit criteria met, **numbers published** | That you can actually build it |
| **3. The Teach-Back** | **Explain the level's hardest concept to a camera in 10 minutes, no notes, with a diagram** | **The strictest test there is. You cannot fake teaching** |

**Fail any of the three and the level is not done.** This is the discipline that separates someone who "went through" a curriculum from someone who is dangerous.

## IX.2 The Final Gauntlet — Week 44, the week before applications open

| Day | Challenge | Pass condition |
|---|---|---|
| 1 | 4 LeetCode Mediums + 1 Hard, timed, **narrated aloud, recorded** | 4/5 unaided within time |
| 2 | 2 system designs, 45 min each, on video | Both hit the rubric |
| 3 | **Debug a sabotaged Adyton** — have a peer break it without telling you what | Root cause in <45 min **with evidence** |
| 4 | All 14 behavioural stories on video, cold | Each ≤90s, quantified, first person, **≥4 from Logic Leap** |
| 5 | Write a full design doc for a **novel** problem in 3 hours | All 10 sections, **3+ real alternatives** |
| 6 | **Teach-back: Sphinx's size invariant · Raft's Figure 8 · why three of four proxy leaks aren't the proxy's fault.** 10 min each | No notes, correct, with diagrams |
| 7 | Watch every video from days 1–6 and **grade yourself against the rubrics** | Honest scoring |

**Pass = ready to interview. Fail any day → that is your next two weeks**, and applications slip by exactly that much. **Do not apply having failed the Gauntlet** — Google and Meta cooldowns are 6–12 months and you get one attempt this cycle.

## IX.3 The spaced-repetition deck

**One card per non-obvious fact, written by you.** Downloaded decks do not work; cards you write do. Target ~500.

**Categories:** the latency ladder · **the four proxy-leak vectors** · **Raft's rules and the Figure 8 case** · **the NAT type matrix and what defeats punching** · TCP state transitions and the CS144 checkpoints · Sphinx's invariants · **the AS-path-selection scoring dimensions** · isolation-level anomalies · JVM GC and allocation facts · algorithm complexities · Linux commands and **what they *answer*** · failure modes · estimation constants · **your own measured numbers.**

**15 min/day, non-negotiable.** The difference between knowing something in month 3 and knowing it in month 12 when the interview happens.

## IX.4 ✂️ The cut order

**Full scope with a named cut order. Cut in this sequence, top first.** Never out of order, and **never silently** — every cut gets a line in `docs/LIMITATIONS.md` saying what was dropped and why.

| # | What gets cut | Costs you | Why it is first |
|---|---|---|---|
| 1 | **Exits and open-web browsing.** Gateways only (already a non-goal — this is a reminder not to re-add it) | Nothing. The compartment demo works through gateways | It is the most seductive scope creep here and it re-opens the scope decision |
| 2 | **The third and fourth candidate selectors** in Level 9 — take Counter-RAPTOR-style on the literature's evidence | The comparison thins; **the curve survives** | The curve is the artifact, not the bake-off |
| 3 | **The C++ port of the selector** — keep the Python implementation | A cross-language test-vector line on the CV | The result is the contribution; the language is not |
| 4 | **The DP noise on telemetry** — publish aggregates without it and say so | One design doc and a paragraph of honesty | Kafka→Postgres still evidences the pipeline |
| 5 | **The ARM port and the x86/ARM analysis** | A free result and one blog post | Genuinely optional |
| 6 | **Two of the six reproduced outages** | `incident-lab` weakens but survives at four | The 20 self-inflicted incidents matter more than the famous ones |
| 7 | **6.5840 Lab 1 (MapReduce)** — go straight to Labs 2–3 | A warm-up and one CV line | Raft is the artifact; MapReduce is not |
| 8 | **CS144 checkpoints 5–7** (ARP and the IP router) — keep 0–4, the TCP itself | "All 8 passing" becomes "checkpoints 0–4 passing" | The router is below your abstraction; the TCP is not |
| 9 | **The mesh simulator's fidelity study at scale** — keep the simulator, drop the validation sweep | `sim-fidelity.md` gets weaker and **you must say so** | Costs credibility, not correctness |
| 10 | **Level 9's sybil analysis** — keep correlation and guard placement | One section of the attack lab | The guard-placement result is the point |

### 🔴 What is NEVER cut

| Never cut | Because |
|---|---|
| **Level 2 — the linkability measurement** | It is the only thing that makes the project's premise *measured* rather than asserted, **and it is your first artifact.** Without it you are building a solution to a problem you read about |
| **Level 4 — the compartments and `leakproof`** | It is the product. Without it Adyton is a VPN with extra steps |
| **★ The demo (W26)** | Your stated success condition |
| **The operational shell — k8s, observability, on-call (Level 8)** | **It is what the screen reads.** AWS 48.9%, Kubernetes 30.4%, observability 22.0%, on-call 21.5% |
| **⭐ The guard-placement curve (W52)** | It is the research contribution and the single most novel thing you will produce |
| **The C++ safety apparatus** | It is the argument for having chosen C++ at all |
| **Java (Level 7)** | 53.3% — the most-demanded skill in your corpus and the largest measured gap in your profile |
| **The Track I hours** | The only track that degrades irreversibly. A missed week is not recoverable by working harder later |
| **Applications from W45** | The plan's entire purpose. Everything else is instrumental |
| **The Logic Leap track (§VIII.5)** | 37.0% + 34.8% + 31.2% + 17.2% of postings, and nothing else touches them |

**The decision is forced at three gates: Week 18, Week 32, Week 44.** At each, count how many weeks behind you are and **cut that many items off the top of the list.** **Cutting at a gate is a decision. Discovering in Week 48 that you cannot finish is a failure.**

## IX.5 🚨 Re-plan triggers

**Re-planning is not failure; it is the plan working.**

| Trigger | Response |
|---|---|
| **Cumulative deficit > 40h** | **Cut scope in the order above. Do not compress estimates** |
| **All three buffer weeks gone before W32** | Estimates are systematically wrong. **Recompute Levels 6–9 with your measured ratio from `LOG.md`**, and consider moving Level 9 into an explicit Year Two |
| **Two consecutive checkpoints where the repo is not interview-ready** | **Stop feature work entirely for one week.** README, build, demo. Overrides everything |
| **Three consecutive weeks of Track I under 5h** | The project is eating the track you explicitly protected. **Invert the week — interview first, project with what is left — for two weeks** |
| **The Week-2 scale spike fails** — too few relays fit, or the free-tier box is unreachable | **Decide in Week 2.** Substitute 8–12 relays with the simulator carrying scale from month one, **stated in the README as the primary limitation.** Do not carry the uncertainty forward |
| **The Level-2 crawl is blocked** — rate limits, bot detection, legal-ish grey zones | **Decide in W9.** Fall back to the published WhoTracks.me and OpenWPM datasets and do the *analysis* rather than the collection, and **say which you did.** The graph is the artifact either way |
| **CS144 overruns W32** | Take the W32 buffer, and cut checkpoints 5–7. **Do not cut checkpoints 0–4** — they are the artifact |
| **6.5840 Lab 3 overruns W43** | **Expected, and normal.** Take the W44 buffer. **Do not skip `TestFigure8Unreliable`** — passing it is the claim |
| **Response rate <10% at W50** | Diagnose per §VIII.8 **before** sending more |
| 🔴 **You have not opened the repo in 7 days** | **The most important trigger and the easiest to ignore.** Do not restart at 32 hours. One 2-hour session, then one 4-hour session, then resume. **Restarting at full intensity after a break is how a one-week gap becomes a one-month one** |

### What does NOT trigger a re-plan
**A bad week** — noise. **A target you missed** — targets set before measurement are estimates; record both numbers and move on. **A negative result** — an AS-aware selector that helps less than the papers suggested, or a sim-fidelity divergence larger than you hoped, **are results**; they get written up and become interview material. **Feeling behind** — check `LOG.md`. And 🔴 **a better project idea.** It will happen, probably around Level 4 and again around Level 7. **The answer is no.** Write it in `docs/IDEAS.md` and continue. **You spent weeks choosing this one deliberately; changing again in month four costs you the accumulated depth that is the entire point of a single system.**

## IX.6 Tracking — three artifacts, three rituals, ~45 min/week

| File | Contains | Written |
|---|---|---|
| `LOG.md` | Hours by track, task outcomes, weekly review, level checkpoint | Daily + Sunday |
| `dsa/FAILURES.md` | Every failed problem, in the §VII.6 format | As it happens |
| `career/APPLICATIONS.md` | Every application, with response and stage | As it happens |
| `career/LOGICLEAP.md` | The §VIII.5 situations, dated | As they happen |

**Daily — 2 minutes.**
```
2026-10-08 · D:4.0 I:1.5 F:0.5 J:0 · Frame parser: length cap + CRC done.
             libFuzzer found an OOB read at offset 12 after 4 min (fixed, corpus committed).
             Varints tomorrow. (nlohmann→hand-rolled cost ~1h more than planned)
```
**Log the hours you actually worked, not the hours you sat at the desk.** The Week-52 retrospective is only useful if this is honest, and its value is telling you your real estimation ratio — which you cannot learn from inflated data.

**Weekly review — Sunday, 30 minutes.**
1. **Hours by track vs budget.** A deficit up to 3h is noise. **Three consecutive deficit weeks is a signal**
2. **Which tasks met their acceptance criterion?** Met / not met. **"Partially" is not a category — force it.** A benchmark that runs but has no hardware counter **did not meet its criterion**
3. **Which targets did you set before measuring, and what did you get?** **Both numbers, always**
4. **What did not finish, and does it block next week?** Blocks → top of next week, something drops. Does not → the buffer list. **Never silently carry unfinished work forward** — that is how a two-week slip becomes invisible until month eight
5. **Track I:** attempted / solved / failed / re-solved, **and designs written.** 15 attempted with 0 failure entries means the problems were too easy or you are not logging
6. **Logic Leap:** did anything happen worth a §VIII.5 entry? **If four weeks pass with nothing, go and create the situation**
7. **One sentence: the biggest risk to the next four weeks.** A specific thing, not a feeling

**Level checkpoint — at each boundary.**
1. **Exit criteria, one at a time. Met, or waived in writing with a reason. No third option**
2. **Hours: level actual vs budget, and cumulative.** The cumulative number is the one that matters
3. 🔴 **Is the repository interview-ready RIGHT NOW?** Three checks, *performed*, not considered:
   - Does `make bootstrap` work on a clean clone? **Actually run it**
   - Does the README describe what exists rather than what is planned?
   - **Can you speak for 45 minutes about it, today, without preparation?**

   If any is no, fixing it is next week's top priority. **The plan is built so you can stop at any week and still be a coherent candidate, and this check is the only thing enforcing that**
4. **The corpus gaps** — Java 53.3%, AWS 48.9%, distributed systems 48.9%, Kubernetes 30.4%, Kafka 20.7%, PostgreSQL 19.6%, on-call 17.4%, observability 13.0%. One line each: closed / in progress / not started, **and what the evidence is. Not what you read. What is running**
5. 🔴 **Failure-category count** from `dsa/FAILURES.md`. **The most valuable twenty minutes in the checkpoint, and the one most likely to be skipped**
6. **From W13:** referral pipeline — conversations this month, people who now know what you are building
7. **From W45:** applications sent, responses, response rate, stage conversion, what is stalled
8. **One paragraph: is the plan still right?** Not "am I on schedule" — whether it still describes the correct work

## IX.7 ✅ The final readiness checklist

### Can you build it?
- [ ] A frame parser that survives an hour of libFuzzer clean, **with the bugs it found before it was clean, written up**
- [ ] 🔴 **A reproducible measurement of cross-site linkability across thousands of real sites**
- [ ] **Sphinx packets whose serialised size is byte-identical regardless of hops remaining**
- [ ] ★ **Two browsers on one laptop that the internet cannot connect to each other** — with a CI suite that tries and fails
- [ ] **A TCP that passes Stanford CS144's full test suite and interoperates with the kernel's**
- [ ] **Per-hop QUIC transport**, and the head-of-line-blocking chart that justified it
- [ ] **A 20–40 node mesh** with measured NAT hole-punch rates by type, and p50 circuit recovery under 800ms at 20% churn
- [ ] **Raft — MIT 6.5840 Labs 1–3 passing, including `TestFigure8Unreliable`** — and 100% epoch agreement within 30s under churn
- [ ] A **Kafka → Postgres** telemetry plane whose privacy budget **fails closed**
- [ ] The mesh on Kubernetes, **rolling restart dropping zero circuits**, at $0/month
- [ ] ⭐ **The AS-diversity-versus-predictability trade-off curve**

### Can you explain it?
- [ ] Why "no company can assemble one profile of you" is a different and smaller claim than "nobody can track you" — **and why you insist on the smaller one**
- [ ] Four ways a browser escapes a SOCKS proxy, **and which three are not the proxy's fault**
- [ ] Why a network namespace is a stronger boundary than a browser container
- [ ] Why default-drop is a better kill switch than detect-and-react — **give the race in the second design**
- [ ] Why Sphinx's header size must be independent of position in the circuit
- [ ] **Head-of-line blocking, with the number from your own chart, and why your transport is QUIC**
- [ ] Which NAT type defeats hole punching, and what the fallback costs
- [ ] **Raft's Figure 8, at a whiteboard, in five minutes, from memory**
- [ ] Why epoch disagreement is a **fingerprint**, not just an inconsistency
- [ ] ⭐ **The guard-placement attack in two sentences — and why a *better* defence enables it**
- [ ] Coordinated omission, and why you re-measured eight months of results
- [ ] 🔴 **Everything you do not defend against** — metadata, a global passive adversary, a compromised endpoint, traffic analysis — **and why you say it unprompted**
- [ ] **Why someone should use Tor instead of Adyton, and who** — answered without defensiveness

### Can you diagnose it?
- [ ] Root-cause a sabotaged mesh in under 45 minutes, with evidence
- [ ] Read a flame graph in 10 seconds and say what you would fix
- [ ] Given "p99 is 3s, CPU is 8%", name three causes and the command that distinguishes each
- [ ] Given green dashboards and diverging epochs, **find the clock**
- [ ] Given an OOMKill at a 4GB limit with a 3GB heap, name four consumers of the difference

### Can you interview?
- [ ] **540+ problems, ≥70% unaided in 25 minutes** · 25+ Hard · Codeforces ≥1750
- [ ] A random Medium, **narrated**, in 25 minutes, on video, repeatedly
- [ ] **20 system designs**, 45 min each, hitting the rubric
- [ ] 14 behavioural stories, ≤90s, quantified, first person, **≥4 from Logic Leap**
- [ ] **12+ full timed loops** · **the Final Gauntlet passed**

### Do they know you exist?
- [ ] **6 pinned repos**, each with a diagram and a headline number in the first screen
- [ ] **8 technical posts published** — at least three about a *result*, not a tutorial
- [ ] **3+ merged OSS PRs, one non-trivial, ideally in Arti or the Tor specs**
- [ ] One talk given
- [ ] **24–28 people at target companies who know what you are building**, from conversations that started in December
- [ ] **A CV where every bullet has a number**
- [ ] 🔴 **A live demo link that works right now**

---

# 🎯 What success means on 12 September 2027

**Not an offer.** Offer timing is not under your control, the strongest hiring window falls exactly where your loops land, and treating an offer as the criterion makes you optimise for the wrong things in Levels 7 through 9.

> **The criterion: you are a candidate who cannot be screened out on credentials, and cannot be caught out in a system design round.**

If that is true and you have no offer yet, **the plan worked and the timing has not resolved.** Execute `docs/NEXT.md` through October.
If it is not true, **`docs/RETROSPECTIVE.md` tells you which level to return to — with numbers rather than a feeling.**

### `docs/NEXT.md` — what Year Two would be, if you want it

Everything deliberately cut from this term, in priority order: **anonymous credentials and accountable abuse handling** (Privacy Pass — the answer to the thing Tor structurally cannot do) · **traffic shaping and the website-fingerprinting evaluation** (WTF-PAD-style padding, and what it costs in latency) · **the full Tor benchmark** (circuit build, TTFB, throughput, 1080p viability, one script) · **6.1810 and 15-445 in full** · **the C++ selector port** · **and only then, if you have an offer and a jurisdiction, the public network.**

---

# Closing

Three things decide whether this works.

**1. You must actually reproduce the failures.** The Walls are not flavour text. Reading "browsers leak around proxies" produces a fact you will forget. Watching your own real IP appear in a WebRTC ICE candidate while you are *certain* you are proxied produces an instinct you will have for twenty years. **The four you will remember longest:** the tracker graph in Week 12 connecting your own browsing into one profile · a four-byte length prefix killing your own relay in Week 6 · your real IP leaking four different ways in Week 19 · and the moment in Week 51 when you place ten relays against your own public scoring function and watch your own selector prefer them.

**2. You must run all four tracks at once.** Depth without the interview track means nobody ever sees the depth — you fail the phone screen and never reach the design round. The interview track without depth gets you an L4 offer and a six-year stall. Craft without either is empty. **It is genuinely harder to run four tracks than one, and it is the reason most people who "study systems for a year" do not convert it into an offer.**

**3. You must ship publicly, and honestly.** The gap between *"I care about privacy"* and *"here is a measurement of how linkable the web actually is, here is a relay client with OS-level identity compartments and a CI suite that tries to break them, here is a TCP I wrote that passes Stanford's tests, here is Raft that passes MIT's, here is the mesh on Kubernetes at zero dollars a month, here is the curve showing that AS-aware path selection makes you predictable and here is where I set the dial and why, and here is the document listing every single thing this does not protect you from"* — **that gap is the entire difference between a candidate and a hire.**

This is roughly **1,520 hours across twelve months.** The output is not a person who finished a curriculum. It is an engineer who has **measured a problem before solving it**, written a parser that hostile input cannot break, implemented a published cryptographic packet format correctly, bound an identity to a kernel namespace so tightly that the application cannot route around it, implemented TCP and knows why QUIC exists, made twenty machines agree on a document under churn, run the whole thing in production-shaped conditions and broken it twenty times on purpose, attacked their own defence and published the cost — **and can explain any of it at a whiteboard from memory, including the parts that do not work and the parts that never will.**

There are not many of those. **And exactly one posting in 569 cares what your degree says.**

**Now go to Week 1.**
