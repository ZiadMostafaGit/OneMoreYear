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
| **IV** | **The Faculty** — every course, lecture-by-lecture, with what is and is not public | Before each level starts |
| **V** | **The Departments** — books, papers, specs, articles and tools, by subject, all linked | The library. Part VI tells you which week |
| **VI** | 🔴 **The Term** — **52 weeks, each with lectures, reading, the build, exit criteria, DSA and questions** | **This is the part you open every morning** |
| **VII** | **Track I** — 540 problems and 20 designs, mapped week-by-week to the build | Daily |
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

# PART IV — THE FACULTY

> **Verified 14 September 2026.** Course materials move, get renumbered, and go behind logins. Everything below was checked on that date, and where something has changed since the last generation of these roadmaps, **the correction is stated loudly** — because a curriculum that sends you to a 404 in Week 27 is worse than no curriculum.

## 🚨 IV.0 — Read these five corrections before you plan anything

| # | The correction | What it means for you |
|---|---|---|
| **1** | 🔴 **Stanford CS144's site and starter repo are OFFLINE right now.** `cs144.github.io` → 404, `github.com/CS144/minnow` → 404, the GitHub org has zero public repos. Wayback snapshots were healthy through **6 May 2026** and failing by **25 Aug 2026** | The repo "clears annually" and **Fall 2026 starts in late September** — expect it back within weeks. **Week 1 task: check `cs144.github.io` weekly and mirror the repo to a private fork the day it returns.** Level 5 is Week 27; you have time, but do not discover this in Week 26. Fallback: the Wayback snapshot and the live third-party mirrors below |
| **2** | 🔴 **MIT 6.5840's labs have been renumbered.** What older roadmaps call "Lab 2 Raft / Lab 3 KV / Lab 4 Sharded" is now **Lab 3 / Lab 4 / Lab 5**, with a brand-new **Lab 2 (single-machine KV server + lock)** inserted | **"Labs 1–3" in this document means MapReduce → KV server → Raft**, which is the correct current numbering. If you read an older guide, translate |
| **3** | 🔴 **MIT 6.1810's `thread` lab no longer exists, and `util` has entirely different exercises.** Current `util`: **sleep (via a `pause` syscall), sixfive, memdump, find, exec** — not the classic sleep/pingpong/primes/find/xargs | Old solution repos will not match the current grader. Not on the critical path this year, but do not budget for a lab that was deleted |
| **4** | 🔴 **CMU 15-445: use Fall 2025, not Fall 2026.** The F26 FAQ says verbatim that F26 recordings are CMU-only and *"Non-CMU students should watch the Fall 2025 lectures on YouTube"* | Use the F25 site and playlist. Also: **Project 1 is now Adaptive Replacement Cache, not LRU-K**, and **Project 0 is a Count-Min Sketch** |
| **5** | 🔴 **Boneh's Cryptography II was never released and never will be on the current plan.** `coursera.org/learn/crypto2` → 404, verified | Do not build a curriculum around it. The successor material lives in Parts II–III of the free Boneh–Shoup book |

**And one thing that is better than expected:** **CMU 15-445 has a public Gradescope for non-CMU students** — entry code **`5R4XPZ`**, school "Carnegie Mellon University". Auto-graders are released after each CMU deadline. That is a genuine, external, self-checkable grade.

---

## IV.1 📺 THE FOUR CORE COURSES

> **The pricing insight that makes 320 course-hours affordable inside a 52-week plan: two of these courses' labs ARE the product.** The TCP you write in CS144 becomes Adyton's transport reference. The Raft you write in 6.5840 becomes Adyton's directory. Those hours are counted once, not twice.

### 📺 COURSE 1 — **Stanford CS144: Introduction to Computer Networking** · Level 5 · W27–32 · ~90h

**You build a working TCP implementation in C++, across eight checkpoints.** The most relevant course to this project and the most unfakeable claim you will own: *"I implemented TCP and it passes Stanford's test suite."*

| | |
|---|---|
| **Site** | `https://cs144.github.io/` 🚨 **404 as of 14 Sep 2026 — see §IV.0** |
| **Archive (works now)** | `https://web.archive.org/web/20260506063931/https://cs144.github.io/` |
| **Repo** | `https://github.com/CS144/minnow` 🚨 404. Live mirrors: `https://github.com/ht4w5/minnow-winter-2025` (clean starter, Checkpoint-0 slice) · `https://github.com/MuhammadWaleed-Animations/minnow-Stanford` |
| **Most recent public offering** | **Fall 2025**, instructor Keith Winstein |
| **Videos** | ⚠️ **Not officially public.** Fall 2025 goes to Stanford Canvas. The watchable corpus is the older self-paced MOOC: `https://www.youtube.com/playlist?list=PL6RdenZrxrw9inR-IJv-erlOKRHjymxMN` (**145 videos**, third-party re-upload — *mirror what you need, it could vanish*). Semi-official, Routing only: `https://www.youtube.com/playlist?list=PLTQzEwN6b5LUL85DCttO9z_-BOQTApyvZ` (Nick McKeown's own channel) |
| **Textbook** | **None required.** The logistics handout says *"We will not be assigning readings."* Optional and free: **Peterson & Davie, *Computer Networks: A Systems Approach*** — `https://book.systemsapproach.org/` |
| **Environment** | Ubuntu 25.04, g++ 14.2.0, CMake. *"You need to be very comfortable with C++"* |
| **Official time** | *"About 70 hours total on the lab."* Self-study community estimate: ~100h |

**The eight checkpoints — exact current titles:**

| # | Title | `ctest` target | What you build |
|---|---|---|---|
| **0** | networking warmup | `check0` | Telnet and SMTP by hand · `webget` · an in-memory `ByteStream`. *Stated: 2–6 hours* |
| **1** | stitching substrings into a byte stream | `check1` | 🔴 **The `Reassembler` — and this is an interval-merge problem.** Do LC 56/57/435/253 this same week |
| **2** | the TCP receiver | `check2` | `Wrap32` 64↔32-bit seqno translation + `TCPReceiver` |
| **3** | the TCP sender | `check3` | 🔴 **`TCPSender` + the retransmission timer.** This is RFC 6298 implemented. Talk to real Linux TCP; the "one megabyte challenge" |
| **4** | measuring the real world | *(report)* | ≥3 Internet paths, `ping`/`mtr`/`traceroute`, **≥1 hour of `ping -D -n -i 0.2` data.** 🔴 **Feed this straight into Adyton's `lab/bench` network profiles** |
| **5** | down the stack (the network interface) | `check5` | `NetworkInterface` + ARP with 30-second expiry |
| **6** | building an IP router | `check6` | `Router`, longest-prefix match |
| **7** | making an Internet + something creative | *(capstone)* | Needs classmates — **not self-servable.** ✂️ Cut it; do checkpoints 0–6 |

**Self-checkable? ✅ Fully.** ~50 test binaries ship in `tests/`.
```bash
cmake -S . -B build && cmake --build build
cmake --build build --target check0     # then check1, check2, check3, check5, check6
cmake --build build --target test       # everything
cmake --build build --target speed      # throughput benchmarks
export TEST_ONLY="write, close, read"   # a single named test
```
**Past exams with answers were public:** `21fa-midterm`, `21fa-final`, `sp23_midterm`, `sp23_final` — grab them from the Wayback snapshot while you are there.

---

### 📺 COURSE 2 — **MIT 6.5840: Distributed Systems** · Level 7 · W38–44 · ~90h

**The most respected distributed-systems course in the world.** You run **Labs 1, 2 and 3** — MapReduce, a linearizable KV server, and Raft in full. Lab 4 is a W44 stretch goal; Lab 5 moves to `NEXT.md`.

| | |
|---|---|
| **Site** | `https://pdos.csail.mit.edu/6.824/` — live, serving **Spring 2026**, fully public, no login |
| **Instructors** | Frans Kaashoek and Robert Morris |
| **Videos** | ⚠️ **Spring 2020 only** — `https://www.youtube.com/playlist?list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB` (20 lectures). **No 2021–2026 video exists anywhere.** The `.txt` lecture notes on the course site are unusually complete and are your substitute |
| **Labs repo** | `git clone git://g.csail.mit.edu/6.5840-golabs-2026 6.5840` 🔴 **`git://` protocol only — the `https://` variant fails on a certificate-name mismatch, and some networks block port 9418.** Test this in Week 1, not Week 38 |
| **Textbook** | None. The reading *is* the paper list |

**The labs you run:**

| Lab | Title | Parts (with MIT's own difficulty tags) |
|---|---|---|
| **1** | **MapReduce** | One part — *moderate/hard*. Coordinator + worker, crash-recoverable, 10s timeout |
| **2** | **Key/Value Server** | KV server on a reliable network (*easy*) · **implementing a lock with the clerk** (*moderate*) · KV with **dropped messages** (*moderate*). Versioned `Put(key,value,version)`, at-most-once, linearizable. 🔴 **New since the old numbering — and it is directly the semantics your directory needs** |
| **3** | **Raft** | **3A** leader election (*moderate*) · **3B** log (*hard*) · **3C** persistence (*hard*) · **3D** snapshots (*hard*) |
| *4* | *Fault-tolerant KV service* | W44 buffer stretch goal only |
| *5* | *Sharded KV service* | ✂️ `NEXT.md` |

```bash
cd src
make mr                        # Lab 1
make kvsrv1 ; make lock1       # Lab 2
make RUN="-run 3A" raft1       # Lab 3 — then 3B, 3C, 3D
```
Underneath: plain `go test -v -race -run <pattern>`. **Only Gradescope submission is gated; everything else runs locally.**

> ⚠️ **The honest warning.** Older roadmaps budget "2–3 weeks" for all the labs. That is wrong by roughly 4×. **Lab 3 alone defeats most people on the first attempt.** Budget seven weeks, expect to rewrite your Raft at least once, and expect `TestFigure8Unreliable` to humble you. **Finishing Labs 1–3 puts you ahead of the large majority of working senior engineers.**

**The papers, assigned by lecture** — all PDFs on the course site: MapReduce (2004) · GFS (2003) · Paxos Made Simple · **Raft extended (2014)** · Herlihy & Wing, Linearizability · ZooKeeper (2010) · 6.033 Chapter 9 (distributed transactions) · Spanner (2012) · Chain Replication (OSDI 2004) · FaRM (2015) · IronFleet (2015) · Memcached at Facebook (2013) · **On-demand Container Loading (ATC 2023 — guest lecture by Marc Brooker)** · Ray (2021) · 🔴 **SUNDR (2004) — fork consistency, and this one matters unusually much to you** · Bitcoin (2008) · Practical BFT (1999).

🔴 **Watch the BFT lecture specifically**, so you can defend Adyton's crash-recovery failure model rather than hand-wave past it.

**Video-to-syllabus mapping:** 2020 lectures 1–8, 12–14, 16, 18, 19 map cleanly onto the 2026 syllabus. **2026 lectures on Chain Replication, IronFleet, AWS Lambda, Ray and BFT have no video** — read the paper plus the `.txt` notes. Conversely the 2020 set gives you bonus video on VMware FT, CRAQ, Aurora, Frangipani, Spark and COPS.

---

### 📺 COURSE 3 — **Dan Boneh, Cryptography I** · Level 3 · W13–18 · ~35h

**You are not becoming a cryptographer. You are becoming an engineer who can read the Sphinx paper and implement it without inventing anything** — and who knows precisely why "we encrypt it" is not a security claim.

| | |
|---|---|
| 🔴 **Use this, not Coursera** | **`https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/`** — **all lecture videos and all slides, free, no account.** Boneh's own page. Its own wording: *"This page contains all the lectures in the free cryptography course"* |
| **Coursera** | `https://www.coursera.org/learn/crypto` — homeworks, programming projects and the final exam are gated here. The current page does **not** clearly advertise a plain audit option |
| **Free textbook** | **Boneh & Shoup, *A Graduate Course in Applied Cryptography*** — `https://crypto.stanford.edu/~dabo/cryptobook/` · PDF v0.5 `https://crypto.stanford.edu/~dabo/cryptobook/BonehShoup_0_5.pdf` |
| **Self-check** | Reference solutions for all six programming assignments: `https://github.com/AxlLind/coursera-cryptography-I` |
| 🚨 | **Cryptography II does not exist.** Never released; both Coursera URLs 404 |

**What you take — weeks 1–5, plus week 6 if time allows:**

| Week | Topic | Book ch. | Why you need it |
|---|---|---|---|
| **1** | Stream ciphers, PRGs, semantic security, the one-time pad | 2–3 | The definitions everything else rests on |
| **2** | Block ciphers, AES, PRPs/PRFs, modes of operation, CTR | 4–5 | 🔴 **Your onion layers are CTR-mode-shaped** |
| **3** | Message integrity: MACs, CBC-MAC, HMAC, collision resistance, **timing attacks on MAC verification** | 6–8 | The timing-attack lecture is not optional for you |
| **4** | 🔴 **Authenticated encryption**, chosen-ciphertext attacks, **CBC padding attacks**, key derivation, **case study: TLS 1.2** | 9 | **The single most important week.** AEAD is what libsodium hands you and this is why |
| **5** | Key exchange, Merkle puzzles, **Diffie–Hellman**, number theory, intractable problems | 10 | X25519 is here |
| *6* | Public-key encryption, RSA, ElGamal | 11–12 | Useful, not load-bearing for Adyton |
| *7* | Digital signatures | 13–14 | ⚠️ **Slides only, no videos.** On Coursera this slot is the final exam |

**Paired with, the same weeks:** the **Cryptopals** challenges, sets 1–2 (`https://cryptopals.com/`) — 🔴 **you break padding oracles, CBC bit-flipping and nonce reuse by hand, and nothing teaches implementation pitfalls faster.**

---

### 📺 COURSE 4 — **UC Berkeley CS 161: Computer Security** · Levels 1 & 4 · threaded · ~40h

🔴 **A change from earlier versions of this plan.** MIT 6.858 was the assigned security course; its recent lectures are behind an MIT login. **CS161 has full public video, a free textbook, and public projects** — and its final unit is *anonymity and Tor*. For self-study it is simply the better instrument.

| | |
|---|---|
| **Site** | **Fall 2025 (complete):** `https://fa25.cs161.org/` · Fall 2026 running: `https://fa26.cs161.org/` |
| **Instructor** | David Wagner |
| **Videos** | ✅ **Fully public** — `https://www.youtube.com/@berkeley-cs161` |
| **Free textbook** | ✅ **`https://textbook.cs161.org`** — *Computer Security* (Wagner, Weaver, Kao, Shakir, Law, Ngai), CC BY-SA. **39 chapters** |
| **Projects** | Public: memory safety · cryptography implementation · exploitation and access control. Plus HW1–7 |

**The chapters you are assigned, and when:**
- **Level 1 (W4–8):** *Security Principles* · *x86 Assembly and the Call Stack* · **Memory Safety Vulnerabilities** · **Mitigating Memory-Safety Vulnerabilities**. 🔴 **Read these the same week you wire up the sanitizers, and Project 1 (memory safety) is your Level 1 warm-up**
- **Level 3 (W13–18):** *Introduction to Cryptography* · *Symmetric-Key Cryptography* · *Cryptographic Hashes* · *MACs* · *PRNGs* · *Diffie–Hellman* — as the gentler companion to Boneh
- **Level 4 (W19–26):** *Introduction to the Web* · **Same-Origin Policy** · **Cookies and Session Management** · *CSRF* · *XSS*. 🔴 **These four are exactly the browser-side model your compartments are defending**
- **Level 9 (W49–52):** 🔴 **the final chapters — *Anonymity / Tor*** — read last, when you have built the thing

**Supplement, for the harder and more current treatment:** **Stanford CS155** (`https://cs155.stanford.edu/`) — slides public (videos are Canvas-gated), and 🔴 **Lecture 17 is "Privacy, Anonymity & Censorship."** Its three project handouts and starter code are public, with downloadable VMs archived at `https://crypto.stanford.edu/cs155old/cs155-spring17/`.

---

## IV.2 📺 REFERENCE COURSES — consulted, never completed

### **CMU 15-213 / CS:APP — Introduction to Computer Systems** · L0, L1
⚠️ **No public lecture video for any recent offering** — the Fall 2025 site says videos were delayed by *"legal issues."* Treat it as **slides + textbook + labs.**
- **Slides, all public:** `https://www.cs.cmu.edu/afs/cs/academic/class/15213-f25/www/lectures/` — e.g. `01-overview.pdf`. You want: *The Memory Hierarchy*, *Cache Memories*, *Code Optimization*, *Concurrent Programming*, *Synchronization: Basic/Advanced*
- **Textbook:** CS:APP 3e — **§6.2–6.4** (Week 1) and **ch. 5** (Level 8)
- 🔴 **THE ONE LAB YOU SHOULD ACTUALLY DO: Proxy Lab.** `http://csapp.cs.cmu.edu/3e/proxylab.pdf` · handout `http://csapp.cs.cmu.edu/3e/proxylab-handout.tar` (133 KB, downloads anonymously, **ships `driver.sh` so it is fully self-gradeable offline**)

> **Why Proxy Lab earns a slot in a privacy-relay curriculum:** you write a **concurrent caching HTTP proxy** — parse the request, open a connection to the origin, forward, cache the response. Part II is concurrency. Part III is an LRU-approximating cache where 🔴 **the writeup explicitly forbids one big lock: *"protecting accesses to the cache with one large exclusive lock is not an acceptable solution"*** — you must partition, or use readers-writers locks, or build it from semaphores. **That is a proxy, with concurrency, with a real synchronisation constraint, auto-graded, in a weekend.** Schedule it in **Level 1, Week 7**, as the warm-up for everything that follows.
- Also free and self-gradeable: **Bomb Lab** (`http://csapp.cs.cmu.edu/3e/bomb.tar`, grading-server notification disabled) and **Attack Lab** (`/3e/target1.tar`) — do them in Week 2 if you want the x86 fluency

### **MIT 6.858 / 6.566 — Computer Systems Security** · L4, L9
- **Spring 2026:** `https://css.csail.mit.edu/6.5660/2026/` ⚠️ *(the root URLs redirect to a stale 2023 — go to the year directory directly)*. **There is no 2025 offering**
- 🔴 **Lecture 20 is literally "Anonymous Communication"** — assigned reading: the **Tor (2004) paper** plus the Tor blog's *"Top changes since the 2004 design paper"* series. **Read this in Level 9**
- **Videos:** 2026 is Panopto/MIT-only. Use **Spring 2020's public YouTube set** (25 lectures, linked from `https://css.csail.mit.edu/6.858/2020/`) or **OCW Fall 2014** (`https://ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/`, 23 videos — includes *Anonymous Communication*, *Private Browsing*, *Data Tracking*, *Side-Channel Attacks*)
- **Labs are fully public and self-gradeable:** VM image `https://web.mit.edu/6.858/2026/6.566-standalone-v26.zip` (~2.55 GB, Ubuntu 24.04) · code `git clone https://github.com/mit-pdos/6.566-lab-2026 lab` · `make check-lab1` etc.

### **MIT 6.1810 — Operating System Engineering (xv6)** · L4
You are **not** doing the labs — that is a 150-hour course and it is not on the critical path. It is here so that when you build network namespaces you know what the kernel is doing.
- **Fall 2025 (complete):** `https://pdos.csail.mit.edu/6.1810/2025/` — plain-text lecture notes, freely downloadable
- **Read:** the **page tables**, **system call entry/exit**, **traps**, and **networking** lecture notes. 🔴 **And `2025/lec/l-shenango.txt`** — high-performance networking
- **xv6 book, free:** `https://mit-pdos.github.io/xv6-riscv-book/`
- **Videos:** Fall 2020 only — `https://pdos.csail.mit.edu/6.S081/2020/schedule.html`
- ⚠️ **`thread` and `lazy` labs no longer exist; `util`'s exercises changed in 2025**

### **CMU 15-445 — Database Systems** · optional, L7
Only if the directory's storage layer leaves you hungry. **Use Fall 2025.**
- Site `https://15445.courses.cs.cmu.edu/fall2025/` · ✅ **full public playlist, 25 videos, ~33h42m:** `https://www.youtube.com/playlist?list=PLSE8ODhjZXjYMAgsGH-GtY5rJYZ6zjsd5`
- 🔴 **Public Gradescope for non-CMU students: entry code `5R4XPZ`**, school "Carnegie Mellon University"
- Repo `https://github.com/cmu-db/bustub` · written homeworks **with solutions** at `.../fall2025/assignments.html`
- **Watch:** *Database Logging* and *Database Recovery* — your epoch store is a WAL and recovery is ARIES's problem

### **UIUC ECE/CS 598HPN — High-speed and Programmable Networks** · optional, L8
All lecture slides are public PDFs; no video. `https://courses.grainger.illinois.edu/ece598hpn/fa2023/`
🔴 **The three lectures worth your time: "High-performance stack I/II/III"** — *Host network stack overheads*, *TAS*, *XDP*. Read them the week you profile Adyton's data plane.

### **Stanford CS244 — Reproducing Network Research** · optional, anytime
🔴 **`https://reproducingnetworkresearch.wordpress.com/`** — a decade of student projects reproducing networking papers, runnable on Mininet. **A ready-made menu of self-contained weekend experiments**, including BBR, QUIC, and congestion-control reproductions. Use it when you want a small measured result and have a spare Saturday.

## IV.3 📋 The Atlas at a glance

| Course | Level | Weeks | Hours | What you complete | Video? |
|---|---|---|---|---|---|
| **CS:APP / 15-213** | L0, L1 | W1–2, W7 | 25 | §6.2–6.4, ch. 5, **Proxy Lab**, Bomb Lab | ❌ slides only |
| **Berkeley CS161** | L1, L3, L4, L9 | threaded | 40 | Memory-safety + web + anonymity chapters, Project 1 | ✅ **full public** |
| **Boneh Crypto I** | L3 | W13–18 | 35 | **Weeks 1–5**, + Cryptopals 1–2 | ✅ free on Stanford |
| 🔴 **Stanford CS144** | **L5** | **W27–32** | **90** | **Checkpoints 0–6** | ⚠️ unofficial mirror |
| 🔴 **MIT 6.5840** | **L7** | **W38–44** | **90** | **Labs 1, 2, 3** | ⚠️ 2020 only |
| MIT 6.858 | L4, L9 | W22, W50 | 15 | Selected lectures, esp. **L20 Anonymous Communication** | ✅ 2020 / 2014 |
| MIT 6.1810 | L4 | W20 | 10 | Notes on page tables, traps, namespaces, Shenango | ✅ 2020 only |
| *15-445* | *L7* | *optional* | *—* | *Logging and recovery lectures* | ✅ **F25 playlist** |
| *598HPN* | *L8* | *optional* | *—* | *High-performance stack I–III* | ❌ |
| | | | **~305** | | |

---
---

# PART V — THE DEPARTMENTS

> **The library, organised the way a college is: by department.** Every item carries a link that was verified on 14 September 2026 and a line saying why it earns your time. **Nothing here is "further reading."** If it is listed, it is assigned somewhere in Part VI, and Part VI tells you which week.
>
> **Three of these sections are marked ⛓ THE SPINE.** Those are not reading lists — they are arguments that ran for a decade, with a reversal in the middle, and you read them **in order**. Following an argument is a different and better education than reading twenty papers.

## V.A ⚙️ DEPARTMENT OF SYSTEMS, C++ & CORRECTNESS

> **The department that makes the C++ choice defensible.** Everything here is scheduled work from Week 4, not hygiene you get to later. A week where CI's sanitizer job is disabled is a week the language choice became indefensible — and an interviewer will find out in ten minutes.

### Sanitizers — wire all of these in Week 4, not later

| Resource | Link |
|---|---|
| **AddressSanitizer** — heap/stack/global overflow, use-after-free, ~2× slowdown | `https://clang.llvm.org/docs/AddressSanitizer.html` |
| **UndefinedBehaviorSanitizer** — signed overflow, misaligned loads, invalid shifts. **Exactly the bugs hostile input triggers in a parser** | `https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html` |
| **ThreadSanitizer** — data races; essential once the relay runs an async event loop | `https://clang.llvm.org/docs/ThreadSanitizer.html` |
| **MemorySanitizer** — uninitialised reads. 🔴 **Catches the info-leak class ASan cannot see, which for you is a deanonymisation class** | `https://clang.llvm.org/docs/MemorySanitizer.html` |
| **LeakSanitizer** — near-zero cost bundled with ASan | `https://clang.llvm.org/docs/LeakSanitizer.html` |
| **SanitizerCoverage** — the instrumentation that makes coverage-guided fuzzing work. **Read before writing fuzz targets** | `https://clang.llvm.org/docs/SanitizerCoverage.html` |
| **google/sanitizers wiki** — the practical companion: limitations, suppression files, CI recipes | `https://github.com/google/sanitizers/wiki` |
| **`ASAN_OPTIONS` reference** — `detect_stack_use_after_return`, `halt_on_error` | `https://github.com/google/sanitizers/wiki/AddressSanitizerFlags` |
| **Common sanitizer flags** — symbolization and log routing for CI | `https://github.com/google/sanitizers/wiki/SanitizerCommonFlags` |
| **Valgrind quick start** — slower than ASan, catches different bugs, needs no recompile. Worth one session | `https://valgrind.org/docs/manual/quick-start.html` |

### Fuzzing — the flagship apparatus

| Resource | Link |
|---|---|
| **libFuzzer** — the canonical reference for in-process coverage-guided fuzzing | `https://llvm.org/docs/LibFuzzer.html` |
| **libFuzzer tutorial** — the single best starting exercise | `https://github.com/google/fuzzing/blob/master/tutorial/libFuzzerTutorial.md` |
| 🔴 **Building a good fuzz target** — **the critical document for this project.** Determinism, speed, no global state, no `exit()`, input-size discipline | `https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md` |
| 🔴 **Structure-aware fuzzing** — how to fuzz *structured* protocol input instead of burning cycles on malformed headers. **Directly applicable to a Sphinx packet parser** | `https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md` |
| **libprotobuf-mutator** — the practical tool for the above | `https://github.com/google/libprotobuf-mutator` |
| **AFL++** — the maintained AFL successor. CmpLog, persistent mode, custom mutators. **Complements libFuzzer; run both for corpus diversity** | `https://aflplus.plus/docs/` · `https://github.com/AFLplusplus/AFLplusplus` |
| **FuzzTest** — property-based testing and fuzzing in one C++ API; arguably the modern default | `https://github.com/google/fuzztest` |
| **honggfuzz** — hardware-counter feedback; a useful third engine | `https://github.com/google/honggfuzz` |
| **OSS-Fuzz** + the new-project guide — free continuous fuzzing for open source. **A stretch goal for Adyton in Level 8** | `https://google.github.io/oss-fuzz/` · `https://google.github.io/oss-fuzz/getting-started/new-project-guide/` |

### The documented subset — `docs/cpp-subset.md`

| Resource | Link |
|---|---|
| **C++ Core Guidelines** — **the Resource Management, Bounds and Lifetime profiles are your curriculum** | `https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines` |
| The repo — issue discussions explain the *reasoning* behind contested rules | `https://github.com/isocpp/CppCoreGuidelines` |
| **Guidelines Support Library (GSL)** — `gsl::span`, `not_null`, `narrow` | `https://github.com/microsoft/GSL` |
| 🔴 **`std::span`** — the C++20 type that replaces pointer-plus-length. **The single highest-leverage change for parser safety, and it is ADR material** | `https://en.cppreference.com/w/cpp/container/span` |
| **clang-tidy** + the full check list — pick `cppcoreguidelines-*`, `bugprone-*`, `cert-*` deliberately | `https://clang.llvm.org/extra/clang-tidy/` · `https://clang.llvm.org/extra/clang-tidy/checks/list.html` |
| **libc++ hardening modes** — turns standard-library UB into deterministic traps in production. **Low cost, badly under-used** | `https://libcxx.llvm.org/Hardening.html` |
| **libstdc++ `_GLIBCXX_ASSERTIONS`** — the GCC-side equivalent | `https://gcc.gnu.org/onlinedocs/libstdc++/manual/using_macros.html` |
| **Guru of the Week** — Herb Sutter's ownership and lifetime problem sets | `https://herbsutter.com/gotw/` |
| 🔴 **Chromium memory safety** — **~70% of serious Chromium security bugs are memory-safety bugs.** Read it, quote the number, and understand that you are volunteering for that same position | `https://www.chromium.org/Home/chromium-security/memory-safety/` |

### Property-based testing
**RapidCheck** — C++ QuickCheck with shrinking and GoogleTest integration. 🔴 **This is what asserts Sphinx's size invariant.** `https://github.com/emil-e/rapidcheck`
**CppQuickCheck** — an alternative worth comparing, to understand what generators and shrinkers actually are. `https://github.com/grogers0/CppQuickCheck`

### Applied cryptography engineering — you implement nothing, you compose correctly

| Resource | Link |
|---|---|
| **libsodium docs** | `https://doc.libsodium.org/` |
| **Quickstart & FAQ** — answers "which primitive do I use." **Read first** | `https://doc.libsodium.org/quickstart` |
| **Key exchange (`crypto_kx`)** — separate rx/tx session keys. **The API that prevents the directional-key-reuse bug** | `https://doc.libsodium.org/key_exchange` |
| **AEAD constructions** — XChaCha20-Poly1305 vs AES-GCM, with nonce-size and nonce-reuse guidance | `https://doc.libsodium.org/secret-key_cryptography/aead` |
| **Encrypted streams (`secretstream`)** — chunking, ordering, rekeying, truncation detection, done for you | `https://doc.libsodium.org/secret-key_cryptography/secretstream` |
| **Encrypting a set of related messages** — nonce management across many messages on one key | `https://doc.libsodium.org/secret-key_cryptography/encrypted-messages` |
| **Key derivation (`crypto_kdf`)** — subkeys with domain separation. **Exactly what you need per-hop and per-direction** | `https://doc.libsodium.org/key_derivation` |
| 🔴 **Secure memory** — `sodium_memzero`, `sodium_mlock`, guarded heap. **And why a plain `memset` gets optimised away** | `https://doc.libsodium.org/memory_management` |
| **The source** — the test suite is a good model for testing crypto code | `https://github.com/jedisct1/libsodium` |
| 🔴 **Cryptographic Right Answers** (Latacora, 2018) — one page of what to use and what never to touch | `https://www.latacora.com/blog/2018/04/03/cryptographic-right-answers/` |
| 🔴 **Cryptopals** — you break padding oracles, CBC bit-flipping and nonce reuse **by hand.** Nothing teaches implementation pitfalls faster. **Sets 1–2 are scheduled in Level 3** | `https://cryptopals.com/` |
| **Constant-time crypto** (Pornin/BearSSL) — which operations are constant-time on real CPUs and which silently are not | `https://bearssl.org/constanttime.html` |
| **A beginner's guide to constant-time cryptography** — the gentler on-ramp, with concrete C rewrites | `https://www.chosenplaintext.ca/articles/beginners-guide-constant-time-cryptography.html` |
| **cryptocoding** (Aumasson) — a do/don't checklist. **Use it as the review checklist for every crypto-touching PR** | `https://github.com/veorq/cryptocoding` |
| **Matthew Green's blog** — the best ongoing accessible analysis of real-world crypto failures | `https://blog.cryptographyengineering.com/` |

### High-performance I/O

| Resource | Link |
|---|---|
| **Lord of the io_uring** — the best io_uring tutorial that exists | `https://unixism.net/loti/` |
| **liburing** — the official helper library; `test/` is the most complete usage corpus available | `https://github.com/axboe/liburing` |
| `io_uring(7)`, `io_uring_setup(2)` — the SQ/CQ ring memory model and every flag that determines your performance profile | `https://man7.org/linux/man-pages/man7/io_uring.7.html` · `https://man7.org/linux/man-pages/man2/io_uring_setup.2.html` |
| **The rapid growth of io_uring** (LWN, Corbet) — why it grew beyond storage I/O | `https://lwn.net/Articles/810414/` |
| **io_uring-echo-server** — the standard published epoll-vs-io_uring comparison | `https://github.com/frevib/io_uring-echo-server` |
| `epoll(7)` — the baseline you are measuring against; the level-vs-edge-triggered section is the classic source of bugs | `https://man7.org/linux/man-pages/man7/epoll.7.html` |
| **MSG_ZEROCOPY** + **Zero-copy networking** (LWN) — and the honest answer about *when* it actually wins | `https://www.kernel.org/doc/html/latest/networking/msg_zerocopy.html` · `https://lwn.net/Articles/726917/` |
| `splice(2)`, `sendfile(2)` — the pipe-buffer generalisation; foundation for proxying without copies | `https://man7.org/linux/man-pages/man2/splice.2.html` |
| **The C10K Problem** (Kegel) — read as an artifact of how the industry got here | `https://www.kegel.com/c10k.html` |
| **The Secret to 10 Million Concurrent Connections** — the C10M argument: the kernel is the bottleneck | `https://highscalability.com/the-secret-to-10-million-concurrent-connections-the-kernel-i/` |
| *Optional:* **DPDK Programmer's Guide**, **AF_XDP**, **eBPF/XDP tutorial** — read to know what exists; **you are not using kernel bypass this year** | `https://doc.dpdk.org/guides/prog_guide/` · `https://www.kernel.org/doc/html/latest/networking/af_xdp.html` · `https://github.com/xdp-project/xdp-tutorial` |

### Measurement — Law 2's toolkit

| Resource | Link |
|---|---|
| 🔴 **How NOT to Measure Latency** (Gil Tene) — **mandatory viewing before you publish a single benchmark, and you re-audit against it in Week 47** | `https://www.infoq.com/presentations/latency-response-time/` |
| **Coordinated omission, the original thread** — Tene's written explanation with expert pushback | `https://groups.google.com/g/mechanical-sympathy/c/icNZJejUHfE` |
| **The Tail at Scale** (Dean & Barroso, CACM 2013) — eight pages; hedged requests, tied requests, micro-partitioning | `https://research.google/pubs/the-tail-at-scale/` |
| **HdrHistogram** + the C port — constant-cost recording with accurate high percentiles. **The right data structure for latency** | `http://hdrhistogram.org/` · `https://github.com/HdrHistogram/HdrHistogram_c` |
| **wrk2** — a *constant-throughput* load generator that corrects for coordinated omission. The practical companion to the talk | `https://github.com/giltene/wrk2` |
| **The USE Method** + the Linux checklist — a complete, finite checklist for finding a bottleneck instead of guessing | `https://www.brendangregg.com/usemethod.html` · `https://www.brendangregg.com/USEmethod/use-linux.html` |
| **Flame Graphs** + the tooling — how to read them, and how to mis-read them | `https://www.brendangregg.com/flamegraphs.html` · `https://github.com/brendangregg/FlameGraph` |
| **Linux perf Examples** — the best `perf` tutorial anywhere; dozens of copy-pasteable one-liners | `https://www.brendangregg.com/perf.html` · `https://perfwiki.github.io/main/` |
| **benchstat** — applies actual statistics to benchmark output. **Stops you shipping noise as a speedup** | `https://pkg.go.dev/golang.org/x/perf/cmd/benchstat` |
| **Google Benchmark** + user guide — `DoNotOptimize`/`ClobberMemory` to defeat the optimiser | `https://github.com/google/benchmark` · `https://github.com/google/benchmark/blob/main/docs/user_guide.md` |
| **Systems Performance 2e** (Gregg) — the reference text. Ch. 6 §6.6, ch. 13 | `https://www.brendangregg.com/systems-performance-2nd-edition-book.html` |

---

## V.B DEPARTMENT OF NETWORKS & TRANSPORT

> **Levels 5 and 6.** This is the department where you stop *using* the network and start understanding it. The artifact — a TCP that passes Stanford's test suite — is unfakeable, and it becomes the argument for every transport decision you make afterwards.

### Congestion control and the byte stream

| Resource | Why | Link |
|---|---|---|
| 🔴 **TCP Congestion Control: A Systems Approach** (Peterson, Brakmo & Davie, free online book) | **A free book devoted entirely to congestion control.** The best single spine for this topic and better than any chapter | `https://tcpcc.systemsapproach.org/` |
| **RFC 5681 — TCP Congestion Control** | The baseline: slow start, congestion avoidance, fast retransmit/recovery | `https://www.rfc-editor.org/rfc/rfc5681.html` |
| 🔴 **RFC 6298 — Computing TCP's Retransmission Timer** | SRTT, RTTVAR, minimum RTO, exponential backoff. **You will reimplement this algorithm in CS144 Checkpoint 3** | `https://www.rfc-editor.org/rfc/rfc6298.html` |
| **RFC 9438 — CUBIC** | The *current* standard. **Teach this one, not 8312** | `https://www.rfc-editor.org/rfc/rfc9438.html` |
| **RFC 8312 — CUBIC (historical)** | Useful only to show how a spec matures under deployment | `https://www.rfc-editor.org/rfc/rfc8312.html` |
| **BBR: Congestion-Based Congestion Control** (Cardwell et al., Google) | Reframed congestion control around bottleneck bandwidth and RTT instead of loss | `https://research.google/pubs/bbr-congestion-based-congestion-control/` |
| **google/bbr** — v1/v2/v3 code, docs, talks, maintained by the authors | The canonical hub | `https://github.com/google/bbr` |
| **The BBR internet-draft** | The state machine written out in full | `https://datatracker.ietf.org/doc/draft-cardwell-iccrg-bbr-congestion-control/` |
| 🔴 **Bufferbloat — Jim Gettys' own archive** | The primary-source narrative of discovering and diagnosing it. **And the reason a bigger buffer makes latency worse** | `https://gettys.wordpress.com/category/bufferbloat/` |
| **Bufferbloat.net** | fq_codel, CAKE, make-wifi-fast, and the measurement tooling | `https://www.bufferbloat.net/projects/` |
| **RFC 8289 (CoDel)** and **RFC 8290 (fq_codel)** | The no-knobs AQM based on sojourn time — the standardised fix, now the Linux default qdisc | `https://www.rfc-editor.org/rfc/rfc8289.html` · `https://www.rfc-editor.org/rfc/rfc8290.html` |

### QUIC — the transport you ship

| Resource | Why | Link |
|---|---|---|
| **RFC 9000 — QUIC** | Streams, flow control, connection IDs, migration, frame layout. **Read §2, §5, §12–13, §17** | `https://www.rfc-editor.org/rfc/rfc9000.html` |
| **RFC 9001 — Using TLS to Secure QUIC** | The handshake, key schedule and header protection. 🔴 **Header protection is why your handshakes can be made byte-identical except the random bits** | `https://www.rfc-editor.org/rfc/rfc9001.html` |
| **RFC 9002 — Loss Detection and Congestion Control** | ACK handling, packet number spaces, RTT estimation | `https://www.rfc-editor.org/rfc/rfc9002.html` |
| **RFC 8446 — TLS 1.3** | Prerequisite for 9001. The 0-RTT and key-schedule machinery lives here. **Read §2 (six pages) minimum** | `https://www.rfc-editor.org/rfc/rfc8446.html` |
| **RFC 9221 — Unreliable Datagram Extension** | Essential if you ever want QUIC carrying real-time traffic rather than reliable streams | `https://www.rfc-editor.org/rfc/rfc9221.html` |
| **RFC 9312 — Manageability of QUIC** | 🔴 **What network observers can and cannot see. Read this one specifically as a privacy engineer** — it is the operator's-eye view of your own threat model | `https://www.rfc-editor.org/rfc/rfc9312.html` |
| **RFC 9308 — Applicability of QUIC** | When QUIC is and is not the right choice, written by the working group itself | `https://www.rfc-editor.org/rfc/rfc9308.html` |
| **RFC 9369 — QUIC Version 2** | A deliberate version-negotiation exercise to fight ossification | `https://www.rfc-editor.org/rfc/rfc9369.html` |

### QUIC, explained by humans

| Resource | Why | Link |
|---|---|---|
| 🔴 **Head-of-Line Blocking in QUIC and HTTP/3: The Details** (Robin Marx) | **The definitive HOL-blocking explainer**, traced across HTTP/1.1 → /2 → /3 — and it argues the fix is *oversold*, which is exactly the scepticism you want before you build the chart yourself | `https://calendar.perfplanet.com/2020/head-of-line-blocking-in-quic-and-http-3-the-details/` |
| The source repo, with the full diagram set | | `https://github.com/rmarx/holblocking-blogpost` |
| **HTTP/3 From A to Z: Core Concepts** (Marx, Smashing) | The clearest ground-up explanation of why QUIC exists, by a QUIC WG contributor rather than a vendor | `https://www.smashingmagazine.com/2021/08/http3-core-concepts-part1/` |
| **HTTP/3: Performance Improvements** (Marx) | 🔴 **Healthily sceptical on 0-RTT, migration and HOL removal. Separates real gains from marketing** | `https://www.smashingmagazine.com/2021/08/http3-performance-improvements-part2/` |
| **HTTP/3: Practical Deployment** (Marx) | What actually changes operationally | `https://www.smashingmagazine.com/2021/09/http3-practical-deployment-options-part3/` |
| 🔴 **qvis — QUIC and HTTP/3 visualisation** | Load a qlog trace and **see** congestion window, multiplexing and HOL blocking. **The best teaching aid for QUIC internals that exists — point it at your own implementation's traces** | `https://qvis.quictools.info/` · `https://github.com/quiclog/qvis` |
| **HTTP/3 explained** (Daniel Stenberg, free book) | Continuously updated book-length introduction from curl's author | `https://http3-explained.haxx.se/en` |
| **The Road to QUIC** (Cloudflare) | The classic "why not TCP" argument, with ossification framed concretely | `https://blog.cloudflare.com/the-road-to-quic/` |
| **Introducing 0-RTT** (Cloudflare) | The best 0-RTT explainer, unusually honest about the replay-attack tradeoff | `https://blog.cloudflare.com/introducing-0-rtt/` |
| **Does the QUIC handshake require compression to be fast?** (Fastly) | Real measurement of handshake cost. **A good model for how to interrogate a protocol claim** | `https://www.fastly.com/blog/quic-handshake-tls-compression-certificates-extension-study` |
| **QUIC Interop Runner** | Live interop matrix — shows which features are *actually* deployed, not just specified | `https://interop.seemann.io/` |

### The two QUIC papers you must read together

| Resource | Why | Link |
|---|---|---|
| **The QUIC Transport Protocol: Design and Internet-Scale Deployment** (Langley et al., SIGCOMM '17) | The foundational deployment paper: 15–18% YouTube rebuffer reduction, 3.5–8% search latency reduction, at 35% of Google egress | `https://research.google/pubs/the-quic-transport-protocol-design-and-internet-scale-deployment/` |
| 🔴 **QUIC is not Quick Enough over Fast Internet** (Zhang et al., WWW '24) | **The essential counterweight: up to 45.2% *lower* throughput than TCP+TLS+HTTP/2 on fast links**, root-caused to receiver-side processing and userspace ACKs. **Read it the same week as the paper above and hold both** | `https://arxiv.org/abs/2310.09423` |

### Implementations to read and to use

| Resource | Why | Link |
|---|---|---|
| 🔴 **ngtcp2** — pure C, pluggable TLS backend. **This is what Adyton links against** | The reference for embedding QUIC in C/C++ | `https://github.com/ngtcp2/ngtcp2` |
| ngtcp2 docs and examples | A complete client/server pair — the fastest way to see the API driven end to end | `https://nghttp2.org/ngtcp2/` · `https://github.com/ngtcp2/ngtcp2/tree/main/examples` |
| **picoquic** | 🔴 **Deliberately minimal C — the most *readable* QUIC codebase for learning.** Read this one, link the other | `https://github.com/private-octopus/picoquic` |
| **quiche** (Cloudflare, Rust) | I/O-free API; powers Cloudflare's edge | `https://github.com/cloudflare/quiche` |
| **MsQuic** (Microsoft) + its perf dashboard | RSS, UDP GSO/GRO coalescing, XDP bypass. **The best case study in QUIC performance engineering**, with continuously published numbers | `https://github.com/microsoft/msquic` · `https://microsoft.github.io/msquic/` |

### NAT traversal — Level 6

| Resource | Why | Link |
|---|---|---|
| 🔴 **How NAT traversal works** (Tailscale, David Anderson) | **The best practical write-up in existence.** Every NAT class, birthday-paradox port prediction for symmetric NAT, and honest failure statistics. **Read this before any RFC** | `https://tailscale.com/blog/how-nat-traversal-works` |
| **How Tailscale works** | DERP as a production answer to "what do you do when traversal fails" | `https://tailscale.com/blog/how-tailscale-works` |
| 🔴 **Peer-to-Peer Communication Across NATs** (Ford, Srisuresh & Kegel, USENIX ATC '05) | **The original hole-punching paper**, including a measurement study of real success rates across hundreds of NATs | `https://bford.info/pub/net/p2pnat/` |
| **RFC 4787 — NAT Behavioral Requirements** | Defines endpoint-independent / address-dependent / **symmetric**. **The vocabulary for every NAT conversation. §4 is the core** | `https://www.rfc-editor.org/rfc/rfc4787.html` |
| **RFC 5128 — State of P2P Communication across NATs** | Survey of every technique with its failure modes. The best single overview | `https://www.rfc-editor.org/rfc/rfc5128.html` |
| **RFC 8445 — ICE** | The candidate-gathering and connectivity-check state machine everyone reimplements. **§2 is enough** | `https://www.rfc-editor.org/rfc/rfc8445.html` |
| **RFC 8489 — STUN** (current) and **RFC 5389** (historical) | **Read both and diff them** — most deployed code still implements 5389 | `https://www.rfc-editor.org/rfc/rfc8489.html` · `https://www.rfc-editor.org/rfc/rfc5389.html` |
| **RFC 8656 — TURN** | The relay fallback for when punching fails | `https://www.rfc-editor.org/rfc/rfc8656.html` |
| 🔴 **pion/ice** — **this is what Adyton uses** | A clean, readable Go ICE implementation you can actually finish reading | `https://github.com/pion/ice` · `https://pkg.go.dev/github.com/pion/ice/v4` |
| **pion/webrtc** + examples | Pure Go, no cgo. The reference for learning the whole stack | `https://github.com/pion/webrtc` · `https://github.com/pion/webrtc/tree/main/examples` |
| **WebRTC for the Curious** (free book) | Vendor-neutral, explains *why* WebRTC works the way it does. The best conceptual companion to the RFCs | `https://webrtcforthecurious.com/` |
| **DCUtR spec** (libp2p) | Coordinated hole punching — a compact, complete spec worth reading end to end | `https://github.com/libp2p/specs/blob/master/relay/DCUtR.md` |
| **Hole punching in libp2p** (Protocol Labs) | The narrative explainer of AutoNAT + Circuit Relay v2 + DCUtR working together | `https://blog.ipfs.tech/2022-01-20-libp2p-hole-punching/` |
| 🔴 **Hole punching in the wild** (FOSDEM 2023) | **6.25M hole-punch results from 154 clients against 47,000 peers; ~70% success for both TCP and QUIC** — overturning the folk belief that UDP is easier. **This is the number your own `natlab` measurement is compared against** | `https://archive.fosdem.org/2023/schedule/event/network_hole_punching_in_the_wild/` |
| **punchr** — the instrumentation behind those numbers | **A model for how to measure your own system honestly** | `https://github.com/libp2p/punchr` |
| **Large-Scale Measurement of NAT Traversal for the Decentralized Web** (arXiv, 2026) | The most recent success-rate study | `https://arxiv.org/abs/2604.12484` |
## V.C ⭐ DEPARTMENT OF ANONYMOUS COMMUNICATION

> **This is the department nobody else's roadmap has, and it is where your forty-five-minute answer comes from.**
>
> Three of these sections are not reading lists — they are **arguments that ran for a decade or more**, and following an argument is a different and better education than reading twenty papers. They are marked ⛓ **THE SPINE** and you read them **in order**.

### F.1 · Foundations — Week 7, before you write a line of Adyton

| Resource | Why | Link |
|---|---|---|
| 🔴 **Chaum, "Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms"** (CACM, 1981) | **The origin of the entire field, and it is seven pages.** Mixes, layered public-key encryption, return addresses. Read it first, before anything modern | `https://chaum.com/wp-content/uploads/2022/09/UNTRACEABLE-ELECTRONIC-MAIL-RETURN-ADDRESSES-AND-DIGITAL-PSEUDONYMS-tech-report.pdf` |
| 🔴 **Dingledine, Mathewson, Syverson, "Tor: The Second-Generation Onion Router"** (USENIX Security 2004) | **The design you are a cousin of.** Every later paper in this department is a reaction to a decision made here | `https://svn-archive.torproject.org/svn/projects/design-paper/tor-design.pdf` |
| **Reed, Syverson, Goldschlag, "Anonymous Connections and Onion Routing"** (IEEE JSAC, 1998) | The pre-Tor Naval Research Lab design — shows what Tor inherited and what it deliberately discarded | `https://www.cs.umd.edu/class/fall2023/cmsc614/papers/onion-routing.pdf` |
| 🔴 **The Tor Specifications** | **The normative protocol. This is what you implement against.** Start at `tor-spec`, then branch | `https://spec.torproject.org/` |
| — `tor-spec` | Cells, circuits, CREATE/EXTEND handshakes, relay cell format | `https://spec.torproject.org/tor-spec/index.html` |
| — `path-spec` | 🔴 **How clients actually choose circuits today — the baseline every AS-aware proposal in §F.4 modifies** | `https://spec.torproject.org/path-spec/index.html` |
| — `guard-spec` | The sampling-attack defence. **Prerequisite for the guard-placement attacks** | `https://spec.torproject.org/guard-spec/index.html` |
| — `dir-spec` | Consensus, directory authorities, relay descriptors — **the trust root, and the thing your Level 7 rebuilds** | `https://spec.torproject.org/dir-spec/index.html` |
| — `padding-spec` | The normative document for Tor cover traffic, connection- and circuit-level | `https://spec.torproject.org/padding-spec/index.html` |
| 🔴 **All Tor design proposals** | **Where Tor's design debates actually happen. The single richest primary source in this entire curriculum** | `https://spec.torproject.org/proposals/BY_STATUS.html` |
| **Tor Research Portal** and 🔴 **the Research Safety Board** | **Nine concrete safety principles for measuring a live anonymity network. Read the Safety Board page before you collect any data at all — including in Level 2** | `https://research.torproject.org/` · `https://research.torproject.org/safetyboard/` |
| **Free Haven's Selected Papers in Anonymity (anonbib)** | The field's canonical curated bibliography ⚠️ *host was unreachable during research; use the mirror if it stays down* | `https://www.freehaven.net/anonbib/` · mirror `https://github.com/glamrock/anonbib` |
| **Arti — the Rust Tor implementation** | The code to read next to the spec. Start at `crates/tor-proto` | `https://gitlab.torproject.org/tpo/core/arti` · docs `https://tpo.pages.torproject.net/core/doc/rust/arti_client/index.html` |
| 🔴 **Counter Galois Onion** (Tor blog Nov 2025; EUROCRYPT 2026) | **NEWER — Tor is replacing its relay-cell encryption** with a non-malleable forward-secret scheme. This is the current cryptographic frontier and it postdates every other roadmap you have | `https://blog.torproject.org/introducing-cgo/` |

### F.2 · The packet format — Level 3, and read the correction

| Resource | Why | Link |
|---|---|---|
| 🔴 **Danezis & Goldberg, "Sphinx: A Compact and Provably Secure Mix Format"** (IEEE S&P 2009) | **The format you implement.** Essentially every modern mixnet and the Lightning onion derive from it | `https://cypherpunks.ca/~iang/pubs/Sphinx_Oakland09.pdf` · ePrint `https://eprint.iacr.org/2008/475` |
| 🔴🔴 **Scherer, Weis, Strufe, "Provable Security for the Onion Routing and Mix Network Packet Format Sphinx"** (PoPETs 2024) | **NEWER, and you must read it with the paper above.** It **repairs Sphinx's broken proof**, shows **DDH is insufficient (you need Gap-DH)**, and documents a **payload malleability issue.** 🔴 **No other roadmap mentions this. Implementing Sphinx in 2027 without it is implementing a 2009 understanding of it** | `https://arxiv.org/abs/2312.08028` |
| **Kuhn, Beck, Strufe, "Breaking and (Partially) Fixing Provably Secure Onion Routing"** (IEEE S&P 2020) | Invalidates the Camenisch–Lysyanskaya onion-security framework that Sphinx and HORNET relied on. **Read for the humility** | `https://arxiv.org/abs/1910.13772` |
| 🔴 **Lightning BOLT #4: Onion Routing Protocol** | **The most widely deployed Sphinx derivative on Earth**, with its deltas from the academic format written down explicitly | `https://github.com/lightning/bolts/blob/master/04-onion-routing.md` |
| **lightning-onion** (Go reference implementation) | The concrete engineering deltas: MAC over the whole header, ChaCha20 instead of LIONESS, no end-to-end payload | `https://github.com/lightningnetwork/lightning-onion` |
| **nymtech/sphinx** (Rust) | The reference modern implementation. **Read it next to the 2009 paper** | `https://github.com/nymtech/sphinx` |
| **Nym, "Outfox: a Packet Format for a Layered Mixnet"** (arXiv, Dec 2024) | **NEWER** — the Sphinx successor: fewer per-hop public-key operations, smaller headers, KEMs instead of DH for post-quantum readiness | `https://arxiv.org/abs/2412.19937` |
| **Piotrowska et al., "The Loopix Anonymity System"** (USENIX Security 2017) | Poisson mixing and loop cover traffic — **the corner of the trilemma you are deliberately not taking**, and you should be able to say why | `https://www.usenix.org/system/files/conference/usenixsecurity17/sec17-piotrowska.pdf` |
| **Katzenpost mix network specifications** | An implementable, engineer-grade spec of a Loopix-style mixnet — **the missing link between papers and code** | `https://katzenpost.network/docs/specs/` |
| *Optional depth:* **HORNET** (CCS 2015) · **Vuvuzela** (SOSP 2015) · **Karaoke** (OSDI 2018) | Sphinx at line rate; and the DP-based metadata-hiding branch you are not taking | `https://arxiv.org/abs/1507.05724` · `https://pdos.csail.mit.edu/papers/vuvuzela:sosp15.pdf` · `https://www.usenix.org/system/files/osdi18-lazar.pdf` |

### F.3 · The trilemma — Week 7, and every design decision descends from it

| Resource | Why | Link |
|---|---|---|
| 🔴 **Das, Meiser, Mohammadi, Kate, "Anonymity Trilemma: Strong Anonymity, Low Bandwidth Overhead, Low Latency — Choose Two"** (IEEE S&P 2018) | **The impossibility result that sets your entire design envelope.** Adyton takes low latency and low overhead and gives up strong anonymity against a global passive adversary — **and this is the paper that makes that a principled choice rather than a shortcut** | `https://eprint.iacr.org/2017/954` |
| **"Comprehensive Anonymity Trilemma: User Coordination is not enough"** (PoPETs 2020) | Closes the loophole for protocols with proactive user coordination | `https://petsymposium.org/popets/2020/popets-2020-0056.pdf` |
| **Serjantov & Danezis; Díaz et al.** (both PET 2002) | 🔴 **Entropy-based anonymity-set size and the normalised degree of anonymity — read side by side; together they are the field's standard metric** | `https://link.springer.com/chapter/10.1007/3-540-36467-6_4` · `https://link.springer.com/chapter/10.1007/3-540-36467-6_5` |
| 🔴 **Kuhn et al., "On Privacy Notions in Anonymous Communication"** (PoPETs 2019, Best Paper) | **A complete hierarchy of ~20 privacy notions with strictness proofs. This is the reference for stating precisely what your system claims** — and precision is the whole discipline of your honesty statement | `https://petsymposium.org/popets/2019/popets-2019-0022.pdf` |

### F.4 ⛓ THE SPINE — AS-aware path selection, read in this order

> **This is the research contribution, and it is a nine-year argument with a negative result in the middle.** Read the five in order. The fourth is the one that should shape your design, and it is the reason your Level 9 exists.

| # | Read | Why | Link |
|---|---|---|---|
| **1** | 🔴 **Johnson, Wacek, Jansen, Sherr, Syverson, "Users Get Routed: Traffic Correlation on Tor by Realistic Adversaries"** (CCS 2013) | **Prerequisite for everything else.** Establishes the security-over-time framing and the AS/IXP adversary model the whole literature uses, and introduces **TorPS** | `https://dl.acm.org/doi/10.1145/2508859.2516651` |
| **2** | **Nithyanand et al., "Measuring and Mitigating AS-level Adversaries Against Tor" (Astoria)** (NDSS 2016) | The canonical AS-aware client: path prediction plus LP relay selection cuts vulnerable circuits from ~40% to 2% | `https://arxiv.org/abs/1505.05173` |
| **3a** | **Sun et al., "Counter-RAPTOR"** (IEEE S&P 2017) | Guard resilience against BGP hijack, plus location-aware guard selection with *bounded* location leakage | `https://arxiv.org/abs/1704.00843` |
| **3b** | **Barton & Wright, "DeNASA: Destination-Naive AS-Awareness"** (PoPETs 2016) | AS-awareness *without* knowing the destination — compatible with pre-built circuits, which matters for latency | `https://petsymposium.org/popets/2016/popets-2016-0044.php` |
| **4** | 🔴🔴 **Wan, Johnson, Wails, Wagh, Mittal, "Guard Placement Attacks on Path Selection Algorithms for Tor"** (PoPETs 2019) | **THE PAPER THIS LEVEL EXISTS TO ANSWER.** 0.216% of Tor's bandwidth bought **18% of guard-selection probability** against Counter-RAPTOR, DeNASA and LASTor. **A better defence made the targeted case worse, and a defender measuring only the average would never have noticed** | `https://www.princeton.edu/~pmittal/publications/guard-placement-pets19.pdf` |
| **5** | **Rochet, Wails, Johnson, Mittal, Pereira, "CLAPS: Client-Location-Aware Path Selection in Tor"** (CCS 2020) | The state of the art: fixes the security and load-balancing failures of Counter-RAPTOR and DeNASA by **formally bounding** location leakage. Read last | `https://www.freehaven.net/anonbib/cache/claps-ccs2020.pdf` |

**The attack literature underneath it:**
**RAPTOR** (USENIX Security 2015) — BGP hijack/interception plus asymmetric-traffic correlation, validated on live Tor · `https://arxiv.org/pdf/1503.03940`
**Murdoch & Zieliński, "Sampled Traffic Analysis by Internet-Exchange-Level Adversaries"** (PET 2007) — 🔴 Bayesian traffic analysis succeeds on **1-in-N sampled NetFlow.** Why **IXP** diversity matters and not just AS diversity · `https://link.springer.com/content/pdf/10.1007/978-3-540-75551-7_11.pdf`
**Wails et al., "Tempest: Temporal Dynamics in Anonymity Systems"** (PoPETs 2018) — 🔴 client mobility, usage patterns and BGP churn degrade anonymity over time, **and location-aware selection makes mobility *worse*** · `https://petsymposium.org/popets/2018/popets-2018-0019.php`

**🔴 The reality check you must read before trusting any of it:**
**Juen, Johnson, Das, Borisov, Caesar, "Defending Tor from Network Adversaries: A Case Study of Network Path Prediction"** (PoPETs 2015) — **17.2 million traceroutes showing BGP-simulated paths disagree badly with measured paths.** Every AS-aware design in this section rests on inference that is *substantially wrong*, and saying so in your write-up is what separates a research contribution from a demo · `https://petsymposium.org/popets/2015/popets-2015-0021.php`
**Nithyanand, Singh, Cho, Gill, "Holding all the ASes"** (arXiv 2016) — the essential self-critique: measurement error, inference error and performance pitfalls that break real AS-aware clients, **including Astoria** · `https://arxiv.org/abs/1605.03596`

**The newest work — none of which appears in any earlier roadmap:**
**"RPKI-Based Location-Unaware Tor Guard Relay Selection"** (PoPETs 2025) — **NEWER** — sidesteps client-location leakage *entirely* by using RPKI/ROV deployment status instead of client location. 🔴 **A genuinely different answer to the guard-placement problem, and a candidate for your own selector** · `https://arxiv.org/abs/2501.06010`
**"Who Carries Tor? Measuring Bandwidth-Weighted Transit Concentration"** (FOCI 2026) — **NEWER** — a 2015–2025 longitudinal study showing transit concentration persists despite network growth · `https://www.petsymposium.org/foci/2026/foci-2026-0014.pdf`
**"An Extended View on Measuring Tor AS-level Adversaries"** (Computers & Security 2023) — RIPE Atlas re-measurement, IPv4 vs IPv6 exposure, per-country risk · `https://arxiv.org/pdf/2403.08517`
**"PredicTor" / CLASI** (ACM TOPS 2025) — **NEWER** — a metric for how *inferable* a client's AS is from its path-selection behaviour. **Directly the quantity your trade-off curve is measuring** · `https://dl.acm.org/doi/10.1145/3723356`

**The AS-graph foundations — Level 9, Week 49:**
🔴 **Gao, "On Inferring Autonomous System Relationships in the Internet"** (IEEE/ACM ToN 2001) — **the origin of valley-free routing** and the customer/provider/peer heuristic every AS-aware path predictor rests on. **Start here** · `https://dl.acm.org/doi/10.1109/90.974527`
**Luckie et al., "AS Relationships, Customer Cones, and Validation"** (IMC 2013) — the algorithm behind the CAIDA dataset, **and it deliberately does not maximise valley-free paths**, which is directly relevant to valley-free's limits · `https://conferences.sigcomm.org/imc/2013/papers/imc039-luckieAemb.pdf`
🔴 **CAIDA AS Relationships dataset** — **the actual monthly p2c/p2p files that Astoria, DeNASA, Counter-RAPTOR and CLAPS all consume. Download these in Week 49 and get your hands dirty early** · `https://www.caida.org/catalog/datasets/as-relationships/`

**The tools you will actually run:**
🔴 **TorPS — the Tor Path Simulator** — Monte Carlo simulation of path selection over months of **real consensus archives.** The standard tool for evaluating a new algorithm's security *over time* · `https://github.com/torps/torps`
**Shadow** — runs unmodified Tor binaries deterministically; the tool for the *performance* side · `https://shadow.github.io/` · `https://github.com/shadow/tornettools`

### F.5 ⛓ THE SPINE — website fingerprinting, and a twelve-year argument about realism

> **Read these four in order and you will have watched a field correct itself.** Then you will know why Adyton's traffic-shaping work is scoped to `NEXT.md` rather than promised.

| # | Read | Why | Link |
|---|---|---|---|
| **1** | **Juarez, Afroz, Acar, Diaz, Greenstadt, "A Critical Evaluation of Website Fingerprinting Attacks"** (CCS 2014) | The realism critique: browsing habits, multi-tab, location and browser version **wreck published accuracies.** Read this immediately after any attack paper | `https://dl.acm.org/doi/10.1145/2660267.2660368` |
| **2** | 🔴 **Cherubin, Jansen, Troncoso, "Online Website Fingerprinting: Evaluating WF Attacks on Tor in the Real World"** (USENIX Security 2022, **Distinguished Paper**) | **The single most important reality check in this department.** The first evaluation on genuine Tor exit traffic in a true open world — **precision collapses versus lab numbers** | `https://www.usenix.org/conference/usenixsecurity22/presentation/cherubin` |
| **3** | **Jansen, Wails, Johnson, "A Measurement of Genuine Tor Traces for Realistic Website Fingerprinting"** (arXiv 2024) | Safely measured real traces showing **how synthetic datasets bias WF results** | `https://arxiv.org/abs/2404.07892` |
| **4** | **"Reality Check for Tor Website Fingerprinting in the Open World"** (arXiv Mar 2026) | **NEWER** — Tao Wang's group revisiting open-world viability. The most recent word | `https://arxiv.org/abs/2603.07412` |

**The attacks, for context:** Panchenko et al. (WPES 2011, put WF on the map) · Wang & Goldberg (WPES 2013, establishes the **Tor cell** as the right unit of analysis) · **Hayes & Danezis, k-fingerprinting** (USENIX Security 2016 — still the strongest non-DL baseline) · 🔴 **Sirinam et al., "Deep Fingerprinting"** (CCS 2018 — **the CNN that broke WTF-PAD at >90% and reset the arms race**) · Triplet Fingerprinting (CCS 2019 — portable fingerprints from ~5 examples).
🔴 **The survey to use as this section's spine: Cui et al., "A Comprehensive Survey of Website Fingerprinting Attacks and Defenses in Tor"** (arXiv Oct 2025, 46pp) — **NEWER** · `https://arxiv.org/abs/2510.11804`

**The defences, for when you get to `NEXT.md`:** Shmatikov & Wang's **original adaptive padding** (ESORICS 2006) · **WTF-PAD** (ESORICS 2016) · **Walkie-Talkie** (USENIX Security 2017 — **the one Deep Fingerprinting could not break**, held to 49.7%) · **FRONT and GLUE** (USENIX Security 2020 — cheap, and the standard modern baseline) · **RegulaTor** (PoPETs 2022 — the "simplicity wins" counterpoint) · **Surakav** (IEEE S&P 2022 — GAN-generated traces).
🔴 **The bridge from papers to deployable code: Pulls, "Towards Effective and Efficient Padding Machines for Tor"** (`https://arxiv.org/abs/2011.13471`) and **Maybenot** (`https://arxiv.org/abs/2304.09510`) — **and Maybenot is what Mullvad's DAITA actually ships**, so you can read the paper and then use the product.

**Flow correlation — the end-to-end attack that two hops cannot prevent:**
🔴 **Murdoch & Danezis, "Low-Cost Traffic Analysis of Tor"** (IEEE S&P 2005) — the founding result. **Start here** · `https://murdoch.is/papers/oakland05torta.pdf`
🔴 **Nasr, Bahramali, Houmansadr, "DeepCorr"** (CCS 2018) — **96% accuracy versus 4% for statistical methods.** Deep learning collapsed the noise tolerance that protected Tor flows, and **this is the attack your threat model explicitly does not defend against** · `https://arxiv.org/abs/1808.07285`
**DeepCoFFEA** (IEEE S&P 2022) — fixes DeepCorr's quadratic cost, making flow correlation scale to Tor-sized flow sets · `https://doi.org/10.1109/SP46214.2022.9833801`

### F.6 · Accountable anonymity — the thing Tor structurally cannot do

> Scoped to `NEXT.md` this year, but **you must be able to talk about it**, because "Tor cannot ban anyone" is a claim in your own problem statement and an interviewer will ask what you would do instead.

| Resource | Why | Link |
|---|---|---|
| 🔴 **Davidson, Goldberg, Sullivan, Tankersley, Valsorda, "Privacy Pass"** (PoPETs 2018) | The origin paper: 1-RTT VOPRF tokens letting Tor and VPN users stop re-solving CAPTCHAs | `https://www.petsymposium.org/2018/files/papers/issue3/popets-2018-0026.pdf` |
| **RFC 9576** (architecture) · **RFC 9577** (HTTP scheme) · **RFC 9578** (issuance) | The deployed standard. Client/Origin/Issuer/Attester roles, the wire format, and both issuance variants | `https://www.rfc-editor.org/info/rfc9576/` · `https://www.rfc-editor.org/rfc/rfc9577.html` · `https://datatracker.ietf.org/doc/rfc9578/` |
| **Cloudflare, "Privacy Pass — The Math"** | The most approachable explanation of the blinding and unblinding. **On-ramp before the RFCs** | `https://blog.cloudflare.com/privacy-pass-the-math/` |
| **Chaum, "Blind Signatures for Untraceable Payments"** (CRYPTO '82) | **Four pages**, and the origin of every unlinkable token in this section | `https://doi.org/10.1007/978-1-4757-0602-4_18` |
| 🔴 **Tsang, Kapadia, Cornelius, Smith, "Nymble: Blocking Misbehaving Users in Anonymizing Networks"** (IEEE TDSC 2011) | **The canonical "block abusers without deanonymising them" design** — and the trusted-third-party cost that makes it hard | `https://homes.luddy.indiana.edu/kapadia/papers/nymble-tdsc.pdf` |
| **BLAC** (CCS 2007) | Removes Nymble's TTP at the cost of proofs linear in the blacklist. **Defines the subfield's core tradeoff** | `https://www.cs.indiana.edu/~kapadia/papers/blac.pdf` |
| **Tor Abuse FAQ** | 🔴 **The operational counterpart to all of the above: what exit-relay abuse actually looks like, and why IP blocking fails.** Read it to understand the problem before the cryptography | `https://support.torproject.org/abuse/` |
| **ARC — Anonymous Rate-Limited Credentials** (IETF draft) | **NEWER** — extends Privacy Pass from one-shot tokens to rate-limited credentials. The standardisation frontier | `https://datatracker.ietf.org/doc/draft-ietf-privacypass-arc-protocol/` |

### F.7 · Measuring your own network without betraying its users — Level 7

| Resource | Why | Link |
|---|---|---|
| 🔴 **Jansen & Johnson, "Safely Measuring Tor" (PrivCount)** (CCS 2016) | **The foundational system for differentially-private, secret-shared aggregation across relays.** This is what your telemetry plane is modelled on | `https://www.robgjansen.com/publications/privcount-ccs2016.html` |
| **Elahi, Danezis, Goldberg, "PrivEx"** (CCS 2014) | PrivCount's predecessor — distributed DP plus secure aggregation for exit statistics | `https://cypherpunks.ca/~iang/pubs/privex-ccs14.pdf` |
| **Mani, Wilson-Brown, Jansen, Johnson, Sherr, "Understanding Tor Usage with Privacy-Preserving Measurement"** (IMC 2018) | **The worked example** — the largest safe measurement study of what Tor is actually used for | `https://www.robgjansen.com/publications/torusage-imc2018.html` |
| 🔴 **Corrigan-Gibbs & Boneh, "Prio"** (NSDI 2017) | SNIPs make client-input validation cheap enough for real telemetry at scale | `https://www.usenix.org/system/files/conference/nsdi17/nsdi17-corrigan-gibbs.pdf` |
| **DAP** and **VDAF** (IETF drafts) | The protocol and crypto layers standardising Prio-style two-aggregator telemetry. ⚠️ **Both are still Internet-Drafts, not RFCs — anyone citing "the PPM RFC" is wrong** | `https://datatracker.ietf.org/doc/draft-ietf-ppm-dap/` · `https://datatracker.ietf.org/doc/draft-irtf-cfrg-vdaf/` |
| **Divvi Up** (ISRG) | The production DAP deployment from the Let's Encrypt people — **privacy-preserving telemetry actually running** | `https://divviup.org/` |
| **Dwork, McSherry, Nissim, Smith, "Calibrating Noise to Sensitivity"** (TCC 2006) | The original: sensitivity, the Laplace mechanism, the ε your budget is denominated in | `https://journalprivacyconfidentiality.org/index.php/jpc/article/download/405/388` |
| **Dwork & Roth, *The Algorithmic Foundations of Differential Privacy*** | Chapters 1–3 are the grounding. ⚠️ *The widely circulated `cis.upenn.edu` PDF link now 404s* | `https://doi.org/10.1561/0400000042` |

### F.8 ⛓ THE SPINE — why Tor is slow, and what fixed it

> **Read in order, against *Once is Never Enough* as a methodological check.** This is the argument your `tor-bench` comparison is joining, and you cannot make an honest performance claim without it.

| # | Read | Why | Link |
|---|---|---|---|
| **1** | 🔴 **Dingledine & Murdoch, "Performance Improvements on Tor, or, Why Tor is Slow"** (2009) | **The agenda-setting document**, enumerating six root causes. Nearly all later work responds to one of its sections | `https://research.torproject.org/techreports/performance-2009-11-09.pdf` |
| **2** | **Jansen et al., "Never Been KIST"** (USENIX Security 2014) | Congestion lives in **egress kernel socket buffers**; real-time TCP-state-informed scheduling fixes it. **KIST shipped in Tor** | `https://www.usenix.org/system/files/conference/usenixsecurity14/sec14-paper-jansen.pdf` |
| **3** | 🔴 **Proposal 324: RTT-based Congestion Control** + the deployment post | **The single biggest reason Tor was slow, and its fix** — this removed the ~500 KB/s per-circuit ceiling. **Essential context before you benchmark against Tor: if you compare against a pre-0.4.7 Tor you are comparing against a system that no longer exists** | `https://spec.torproject.org/proposals/324-rtt-congestion-control.html` · `https://blog.torproject.org/congestion-contrl-047/` |
| **4** | **Proposal 329: Conflux (traffic splitting)** | Tor's deployed multipath design — two circuits to a common exit, lower-RTT leg preferred. **The biggest recent latency win.** ⚠️ *There is no Tor blog post on Conflux; the proposal is the canonical source* | `https://spec.torproject.org/proposals/329-traffic-splitting.html` |
| **✅** | 🔴 **Jansen, Tracey, Goldberg, "Once is Never Enough: Foundations for Sound Statistical Inference in Tor Network Experimentation"** (USENIX Security 2021) | **A methodological indictment of single-simulation Tor performance claims. Read it before trusting any speedup number in this section — including your own** | `https://www.usenix.org/system/files/sec21-jansen.pdf` |

**Also:** **Tor Metrics** (`https://metrics.torproject.org/onionperf-latencies.html`) — the canonical longitudinal measurement of how slow Tor actually is, **and your baseline for every claim you make** · **PeerFlow** (PoPETs 2017) — 🔴 bandwidth measurement is a *security* problem, not just an accuracy one · **sbws** — the deployed bandwidth scanner and why Torflow was replaced · **"Point Break"** (USENIX Security 2019) — **$2.8K/month against Tor's scanners cut median client download rate by 80%**.

### F.9 · The deployed comparables — what "it actually shipped" looks like

**Apple iCloud Private Relay** (whitepaper, platform security guide, WWDC talks) and **Cloudflare's account of running its second hop** — see §IV.E.1, the whole of which belongs to this department too.

| Resource | Why | Link |
|---|---|---|
| **Singanamalla et al., "Oblivious DNS over HTTPS"** (PoPETs 2021) | The peer-reviewed design and performance evaluation — 🔴 **it measures the real latency cost of an extra proxy hop**, which is the number your own architecture lives or dies on | `https://petsymposium.org/popets/2021/popets-2021-0085.pdf` |
| **RFC 9230 (ODoH)** · **RFC 9458 (OHTTP)** · **RFC 9298 (CONNECT-UDP)** | The normative specs for the family your design sits in | `https://www.rfc-editor.org/rfc/rfc9230.html` · `https://www.rfc-editor.org/rfc/rfc9458.html` · `https://www.rfc-editor.org/rfc/rfc9298.html` |
| **Donenfeld, "WireGuard: Next Generation Kernel Network Tunnel"** (NDSS 2017) | The data-plane primitive nearly every modern relay mesh builds on. **NoiseIK, cryptokey routing, under 4,000 lines of code** — read it as a lesson in how small a correct thing can be | `https://www.wireguard.com/papers/wireguard.pdf` |
| **Tailscale DERP servers** | The relay design: HTTPS/443 packet forwarding keyed by destination public key, **never seeing plaintext** | `https://tailscale.com/kb/1232/derp-servers` |
| 🔴 **Mullvad DAITA** | **A commercially deployed website-fingerprinting defence** — constant packet sizes and bidirectional cover traffic. Rare real-world deployment of padding research, built on Maybenot. **Read the product page and the paper together and judge whether the claims hold** | `https://mullvad.net/en/vpn/daita` |
| **Mullvad Browser** | 🔴 *"Tor Browser without the Tor network."* **The instructive separation of the fingerprinting-resistance layer from the relay layer — and the exact reason you do not touch the browser** | `https://mullvad.net/en/browser` · `https://blog.torproject.org/releasing-mullvad-browser/` |
| **Google IP Protection** (Privacy Sandbox) | Two-hop design plus RSA blind signatures to unlink traffic from accounts — **the closest browser-integrated analogue to Private Relay, and a live competitor to your premise** | `https://privacysandbox.google.com/protections/ip-protection` · `https://github.com/GoogleChrome/ip-protection` |
| **INVISV Relay / Pretty Good Phone Privacy** | A multi-party relay that also addressed IMSI-based mobile tracking. 🔴 **Instructive as a cautionary case — the service wound down in June 2024.** Read it when you are tempted to plan a public launch | `https://invisv.com/` |
## V.D 🔴 DEPARTMENT OF PRIVACY RELAY ENGINEERING

> **The core discovery of this curriculum's research: almost the entire production reference architecture for Adyton has been published, in public, by the companies that operate it.** Cloudflare runs the egress hop of iCloud Private Relay and has written about nearly every layer of it. Apple published the design document. Tor publishes its proposals. Signal publishes its censorship-circumvention post-mortems.
>
> **You are not working without a reference implementation. You are working without an excuse.**

### E.1 · The deployed two-hop relay — read this before you design anything

| Resource | Why it matters | Link |
|---|---|---|
| 🔴 **iCloud Private Relay Overview** (Apple, Dec 2021, PDF) | **The canonical design document for the system Adyton is a cousin of.** Ingress vs egress proxy, RSA blind-signature auth tokens, and the property that no single party sees both IP and destination. **Week 7 reading, and you will return to it all year** | `https://www.apple.com/icloud/docs/iCloud_Private_Relay_Overview_Dec2021.pdf` |
| **iCloud Private Relay security** (Apple Platform Security) | Token issuance, key separation, DNS handling — the security-engineering framing | `https://support.apple.com/guide/security/icloud-private-relay-security-secad8ce3233/web` |
| 🔴 **iCloud Private Relay: What Cloudflare Customers Need to Know** | **Cloudflare's own account of operating the egress hop of somebody else's two-hop relay.** The other half of the design document above | `https://blog.cloudflare.com/icloud-private-relay/` |
| 🔴 **Ready, set, relay: Protect app traffic with network relays** (WWDC23) | **The closest thing to an official "build a relay client" tutorial that exists**, including chaining multiple relay hops in application code | `https://developer.apple.com/videos/play/wwdc2023/10002/` |
| **`ProxyConfiguration.RelayHop`** (Apple API reference) | A real, shipping, multi-hop relay API. **Read it as a design study for your own `adyton identity` interface** | `https://developer.apple.com/documentation/network/proxyconfiguration/relayhop` |
| **Prepare your network for iCloud Private Relay** | The operational contract: port 443 QUIC/TLS 1.3, `mask.icloud.com`, and a public egress geo-feed | `https://developer.apple.com/icloud/prepare-your-network-for-icloud-private-relay/` |
| 🔴 **Measuring Apple's iCloud Private Relay** (AsiaCCS '23) | **Peer-reviewed independent measurement: did the design actually work?** The model for how your own system should eventually be evaluated by someone who is not you | `https://people.cs.umass.edu/~amir/papers/AsiaCCS23-Private-Relay.pdf` |
| **An investigation into Apple's new Relay network** (APNIC, 2023) | Independent measurement of the deployed topology and routing | `https://blog.apnic.net/2023/01/25/an-investigation-into-apples-new-relay-network/` |

### E.2 · MASQUE — the tunnelling primitive you should probably be using

> 🔴 **This is the single most important thing the research turned up, and it changes a design decision.** Adyton's original plan tunnels over raw per-hop QUIC. **MASQUE — CONNECT-UDP and CONNECT-IP over HTTP/3 — is the standardised way to do exactly that**, it is what Cloudflare replaced WireGuard with in WARP, it is what Apple's relays speak, and traffic shaped like HTTP/3 survives middleboxes that eat custom UDP. **Read these in Week 28 and write an ADR either adopting it or justifying why not.**

| Resource | Why | Link |
|---|---|---|
| 🔴 **Unlocking QUIC's proxying potential with MASQUE** (Cloudflare, 2022) | The clearest explanation of CONNECT-UDP and CONNECT-IP anywhere | `https://blog.cloudflare.com/unlocking-quic-proxying-potential/` |
| **Donning a MASQUE: building a new protocol into Cloudflare WARP** (2023) | **Replacing WireGuard with MASQUE in a shipping consumer client.** The migration story | `https://blog.cloudflare.com/masque-building-a-new-protocol-into-cloudflare-warp/` |
| **Zero Trust WARP: tunneling with a MASQUE** (2024) | Why HTTP/3-shaped tunnels survive middleboxes better than custom UDP — **a censorship-resistance argument as much as a compatibility one** | `https://blog.cloudflare.com/zero-trust-warp-with-a-masque/` |
| **RFC 9298 — Proxying UDP in HTTP (CONNECT-UDP)** | The normative spec | `https://datatracker.ietf.org/doc/rfc9298/` |
| **draft-ietf-masque-connect-ip** | Full IP tunnelling over HTTP/3 — the VPN-grade sibling | `https://datatracker.ietf.org/doc/draft-ietf-masque-connect-ip/13/` |
| **A Primer on Proxies** (Cloudflare, 2022) | Forward / reverse / transparent taxonomy and the trust model of each. **Required vocabulary before you write a design doc** | `https://blog.cloudflare.com/a-primer-on-proxies/` |

### E.3 · Oblivious protocols — the "separate who from what" principle

| Resource | Why | Link |
|---|---|---|
| 🔴 **Helping build the next generation of privacy-preserving protocols** (Cloudflare, 2020) | **Frames the single principle underneath every system in this department:** separate *who you are* from *what you are asking for*, and make sure no one party holds both | `https://blog.cloudflare.com/next-generation-privacy-protocols/` |
| **Improving DNS Privacy with Oblivious DoH** (2020) | Layered encryption plus a non-colluding proxy so the resolver never sees client IPs. **Adyton's DNS story should be argued against this one** | `https://blog.cloudflare.com/oblivious-dns/` |
| **Privacy Gateway: a privacy-preserving proxy built on Internet standards** (2022) | A production OHTTP relay: HPKE, the relay/gateway split, and the operational realities | `https://blog.cloudflare.com/building-privacy-into-internet-standards-and-how-to-make-your-app-more-private-today/` |
| 🔴 **Stronger than a promise: proving Oblivious HTTP privacy properties** (2022) | **What OHTTP actually guarantees versus what operators merely promise.** The distinction your own honesty statement lives or dies on | `https://blog.cloudflare.com/stronger-than-a-promise-proving-oblivious-http-privacy-properties/` |
| **RFC 9458 — Oblivious HTTP** | Unlinkability via a relay that cannot read and a gateway that cannot identify | `https://datatracker.ietf.org/doc/rfc9458/` |
| **Privacy Pass: upgrading to the latest protocol version** (2024) | Current IETF Privacy Pass — VOPRF and Private Access Tokens — as actually deployed. **This is the answer to the thing Tor structurally cannot do, and it is `NEXT.md`'s first item** | `https://blog.cloudflare.com/privacy-pass-standard/` |
| **Introducing the Cloudflare Onion Service** (2018) | Real Tor onion services at CDN scale, including key handling and load balancing | `https://blog.cloudflare.com/cloudflare-onion-service/` |
| 🔴 **Partnering to deploy Oblivious HTTP and Prio in Firefox** (Mozilla, 2023) | **A real OHTTP deployment with Fastly as the relay, plus DAP/Prio for telemetry — directly analogous to your Level 7 telemetry plane** | `https://blog.mozilla.org/en/products/firefox/partnership-ohttp-prio/` |
| **Testing Privacy-Preserving Telemetry with Prio** (Mozilla, 2018) | Secret-shared telemetry across two non-colluding servers | `https://hacks.mozilla.org/2018/10/testing-privacy-preserving-telemetry-with-prio/` |
| **STAR: privacy-preserving data collection** (Brave, 2022) | k-anonymity via threshold secret sharing **without Prio's non-collusion assumption.** Read both and pick | `https://brave.com/privacy-updates/19-star/` |

### E.4 · Running a relay fleet — the operational half

| Resource | Why | Link |
|---|---|---|
| 🔴 **Cloudflare servers don't own IPs anymore — so how do they connect?** (2022) | **Egress IP assignment, port allocation, soft-unicast. This is the hard part of relay egress and almost nobody writes about it** | `https://blog.cloudflare.com/cloudflare-servers-dont-own-ips-anymore/` |
| **Oxy: Cloudflare's Rust-based next-generation proxy framework** (2023) | 🔴 **The framework behind the iCloud Private Relay second hop** | `https://blog.cloudflare.com/introducing-oxy/` |
| **From IP packets to HTTP: the many faces of Oxy** (2023) | Every OSI layer it proxies and the socket/tunnel modes required | `https://blog.cloudflare.com/from-ip-packets-to-http-the-many-faces-of-our-oxy-framework/` |
| **How we built Pingora** (2022) and **open-sourcing it** (2024) | Why NGINX's worker model failed at scale; a multithreaded Rust proxy with connection reuse and zero-downtime upgrade. **Read for the architecture, not the language** | `https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/` · `https://blog.cloudflare.com/pingora-open-source/` |
| **How to build your own VPN, or: the history of WARP** (2025) | **Seven years of protocol and topology decisions — the arc this curriculum is walking** | `https://blog.cloudflare.com/how-to-build-your-own-vpn-or-the-history-of-warp/` |
| **Introducing WARP** (2019) | BoringTun userspace WireGuard, anycast ingress, mobile roaming constraints | `https://blog.cloudflare.com/1111-warp-better-vpn/` |
| **Accelerating UDP packet transmission for QUIC** (2020) | GSO and `sendmmsg` batching. 🔴 **The difference between a toy QUIC relay and one that saturates a NIC** | `https://blog.cloudflare.com/accelerating-udp-packet-transmission-for-quic/` |
| **Enhance UDP Throughput for QUIC and HTTP/3 on Linux** (Tailscale, 2023) | 🔴 **Directly applicable GSO/GRO tuning for a QUIC datapath** | `https://tailscale.com/blog/quic-udp-throughput` |
| **Enhancing Userspace with Kernel Interfaces** (Tailscale, 2022) | TSO/GRO + `sendmmsg` gave wireguard-go **2.2×**. The best userspace-VPN datapath write-up anywhere | `https://tailscale.com/blog/throughput-improvements` |
| **Surpassing 10 Gb/s with Tailscale** (2023) | UDP segmentation offload pushing userspace WireGuard past the in-kernel implementation | `https://tailscale.com/blog/more-throughput` |
| 🔴 **Introducing Quicksilver: configuration distribution at Internet scale** (2020) + **v2** (2025) | **The "why we did NOT use Raft" counterpoint to your Level 7.** Globally replicated KV with a monotonic log and async replication instead of consensus. **Read it, then defend your Raft choice in ADR-0006 against it** | `https://blog.cloudflare.com/introducing-quicksilver-configuration-distribution-at-internet-scale/` · `https://blog.cloudflare.com/quicksilver-v2-evolution-of-a-globally-distributed-key-value-store-part-1/` |
| **Tailnet lock** (2022) + **GA** (2025) | An Ed25519 signing chain so a **compromised coordination server cannot inject nodes.** 🔴 **This is the attack on your own directory, and its published mitigation** | `https://tailscale.com/blog/tailnet-lock` · `https://tailscale.com/blog/tailnet-lock-ga` |
| **Key Management in the Tailscale Control Protocol** (2021) | Machine keys vs node keys; how the network map is signed and distributed | `https://tailscale.com/blog/tailscale-key-management` |
| **Now with more DERP** (2022) · **Peer Relays beta** (2025) / **GA** (2026) | Running and scaling a global relay fleet; then **moving to user-operated relays** — the exact transition Adyton's `NEXT.md` contemplates | `https://tailscale.com/blog/more-derp` · `https://tailscale.com/blog/peer-relays-ga` |
| **How Tailscale is improving NAT traversal, parts 1–3** (2025) | **Five years on: what actually broke, what changed, and the cloud-NAT case that is hardest** | `https://tailscale.com/blog/nat-traversal-improvements-pt-1` · `https://tailscale.com/blog/nat-traversal-improvements-pt-2-cloud-environments` |
| **Kubernetes networking problems due to conntrack** (loveholidays, 2020) | 🔴 **Conntrack table exhaustion under many concurrent connections — exactly the failure a relay fleet on k8s will hit.** Level 8 incident material | `https://deploy.live/blog/kubernetes-networking-problems-due-to-the-conntrack/` |

### E.5 · Tor — the system you are honest about

| Resource | Why | Link |
|---|---|---|
| 🔴 **All Tor proposals, by status** | **The single best reading index for this entire curriculum.** Every design decision in a production anonymity network, argued in public | `https://spec.torproject.org/proposals/BY_STATUS.html` |
| **Announcing Arti, a pure-Rust Tor implementation** (2021) | 🔴 **~half of Tor's tracked security bugs since 2016 were memory-safety issues impossible in safe Rust.** Read this *the same week* you commit to C++, and let it make you uncomfortable — that discomfort is what the sanitizer apparatus answers | `https://blog.torproject.org/announcing-arti/` |
| **Arti 1.0.0: ready for production** (2022) · **2.x relay and directory-authority work** (2026) | The C→Rust rewrite as staged project planning, and the current state of Arti as a relay | `https://blog.torproject.org/arti_100_released/` · `https://blog.torproject.org/arti_2_0_0_released/` |
| 🔴 **Congestion Control Arrives in Tor 0.4.7** (2022) + **Proposal 324** | RTT-based congestion control lifting the ~500 KB/s per-circuit ceiling. **This is the single biggest reason Tor was slow, and its fix. Essential context for your `tor-bench` comparison** | `https://blog.torproject.org/congestion-contrl-047/` · `https://spec.torproject.org/proposals/324-rtt-congestion-control.html` |
| **Proposal 329: Conflux (traffic splitting)** | Splitting a stream across two pre-built circuits — multipath over an overlay | `https://spec.torproject.org/proposals/329-traffic-splitting.html` |
| 🔴 **Announcing the Vanguards Add-On** (2018) + **Vanguards in Arti** (2024) | The layered "2-3-8" guard topology and **guard-discovery attacks.** Direct prior art for your Level 9 | `https://blog.torproject.org/announcing-vanguards-add-onion-services/` · `https://blog.torproject.org/announcing-vanguards-for-arti/` |
| **Introducing Proof-of-Work Defense for Onion Services** (2023) + **How to stop the onion denial** (2020) | 🔴 **Read them together: the design discussion three years before the thing shipped, then the thing.** Tokens vs PoW, attacker asymmetry — and it is the same abuse-handling problem Privacy Pass answers differently |  `https://blog.torproject.org/introducing-proof-of-work-defense-for-onion-services/` · `https://blog.torproject.org/stop-the-onion-denial/` |
| **Sustaining Snowflake operations** (2023) | 5k → 75k users during censorship events, and what it cost in hardware and bandwidth. **The operational reality of running this for real** | `https://blog.torproject.org/snowflake-daily-operations/` |
| **Is Tor still safe to use?** (2024) | A case study in **communicating threat honestly to users** — which is a skill this project needs as much as any technical one | `https://blog.torproject.org/tor-is-still-safe/` |
| **Tor VPN Beta for Android** (2026) | Packaging an onion-routing client as a full-tunnel VPN — the productisation problem you are also solving | `https://blog.torproject.org/tor-vpn-beta/` |

### E.6 · Signal — crypto engineering, and the censorship arc

| Resource | Why | Link |
|---|---|---|
| **Forward Secrecy for Asynchronous Messages** (2013) | The prekey concept that became X3DH — authenticated DH when the peer is offline | `https://signal.org/blog/asynchronous-security/` |
| **Advanced cryptographic ratcheting** (2013) | The original Double Ratchet announcement | `https://signal.org/blog/advanced-ratcheting/` |
| **Sealed sender** (2018) | Sender certificates and delivery tokens — **the canonical metadata-minimisation design, and the thing Adyton explicitly does not attempt** | `https://signal.org/blog/sealed-sender/` |
| **PQXDH** (2023) and **SPQR** (2025) | Hybrid post-quantum key agreement, and extending PQ protection from the handshake into the ongoing ratchet | `https://signal.org/blog/pqxdh/` · `https://signal.org/blog/spqr/` |
| 🔴 **The three-part censorship arc — read in order** | **Doodles, stickers and censorship circumvention** (2016, domain fronting deployed) → **A letter from Amazon** (2018, domain fronting dies) → **Help users in Iran reconnect** (2021, TLS proxies resisting fingerprinting). **The best real-world narrative in this curriculum about a defence being built, working, and then being taken away** | `https://signal.org/blog/doodles-stickers-censorship/` · `https://signal.org/blog/looking-back-on-the-front/` · `https://signal.org/blog/help-iran-reconnect/` |
| **Run a proxy** (2022) · **Proxy Please** (2024) | Volunteer-operated proxy distribution — running a fleet you do not control | `https://signal.org/blog/run-a-proxy/` |
| 🔴 **Privacy is Priceless, but Signal is Expensive** (2023) | **Real infrastructure cost breakdown for a global privacy service.** Read it when you are tempted to imagine running Adyton publicly | `https://signal.org/blog/signal-is-expensive/` |

### E.7 · The browser half — what Mullvad Browser is doing while you do the network

> **You do not modify the browser.** But you must understand precisely what it is doing, because your job is the half it explicitly does not do.

| Resource | Why | Link |
|---|---|---|
| 🔴 **Introducing State Partitioning** (Mozilla Hacks, 2021) | **The engineering-depth companion to Total Cookie Protection:** exactly what state exists in a browser, how it is keyed, and the compatibility escape hatches. **This is the list of things two of your compartments must not share** | `https://hacks.mozilla.org/2021/02/introducing-state-partitioning/` |
| **Firefox 85 cracks down on supercookies** (2021) | Network-state partitioning: HTTP cache, **connection pools**, DNS cache, HSTS — per top-level site. 🔴 **Connection pools and TLS session tickets are the two your Level 4 leak suite must test** | `https://blog.mozilla.org/security/2021/01/26/supercookie-protections/` |
| **Total Cookie Protection** (2021) and **by default worldwide** (2022) | The cookie-jar-per-site model, and what it takes to ship a breaking privacy default globally | `https://blog.mozilla.org/security/2021/02/23/total-cookie-protection/` |
| **Firefox 79: redirect tracking** (2020) and **Brave: Debouncing** (2021) | Bounce tracking, and two different countermeasures. **Your compartments must survive a bounce chain** | `https://blog.mozilla.org/security/2020/08/04/firefox-79-includes-protections-against-redirect-tracking/` · `https://brave.com/privacy-updates/11-debouncing/` |
| 🔴 **Brave: Fingerprint randomization ("farbling")** (2020) and **Fingerprinting defenses 2.0** | **The opposing philosophy to Mullvad/Tor Browser's uniformity approach.** Randomise per-session per-site, versus make everyone identical. **You must be able to argue both sides — it is a great interview question and Level 4's ADR** | `https://brave.com/privacy-updates/3-fingerprint-randomization/` · `https://brave.com/privacy-updates/4-fingerprinting-defenses-2.0/` |
| 🔴 **Brave simplifies its fingerprinting protections** (2024) | **A published negative result: why their "strict" mode made users *more* identifiable.** The most valuable single article in this section, and exactly the intellectual honesty your own write-ups should imitate | `https://brave.com/privacy-updates/28-sunsetting-strict-fingerprinting-mode/` |
| **Brave: Preventing pool-party attacks** (2021) | 🔴 **Exhaustible socket and connection pools as covert cross-site channels.** A side channel that defeats naive compartmentalisation — **add it to your leak suite** | `https://brave.com/privacy-updates/13-pool-party-side-channels/` |
| **Brave: Fighting CNAME trickery** (2020) | DNS-level CNAME cloaking detection — why domain blocklists fail | `https://brave.com/privacy-updates/6-cname-trickery/` |
| **Brave: Unlinkable bouncing** (2022) · **Ephemeral third-party storage** (2021) | Giving a persistent tracker a fresh unlinkable identity each visit | `https://brave.com/privacy-updates/16-unlinkable-bouncing/` |
| **Brave: GPU fingerprinting protections** (2026) | Current-generation WebGL/WebGPU defences | `https://brave.com/privacy-updates/38-webgl-webgpu-fingerprinting-protections/` |
| **Firefox expands fingerprint protections** (2025) | Current RFP state, and **how they measured a ~50% reduction in trackable users** — a methodology you can borrow | `https://blog.mozilla.org/en/firefox/fingerprinting-protections/` |
| **DuckDuckGo: Most default browser tracking protection doesn't actually stop tracking** (2021) | 🔴 **A comparative measurement methodology for evaluating defences — including your own** | `https://spreadprivacy.com/browser-privacy-protection/` |
| **DuckDuckGo: Is private browsing really private?** (2022) | Clear threat-model framing of what incognito does and does not protect. **Good writing to imitate** | `https://spreadprivacy.com/is-private-browsing-really-private/` |

---

## V.E DEPARTMENT OF CONSENSUS & FORMAL METHODS

> Level 7. **Distributed systems is 48.9% of your backend postings and 57.0% of backend+infra — the highest-frequency technical skill in your corpus.**

| Resource | Link |
|---|---|
| 🔴 **Raft — the EXTENDED paper.** §5 in full, §6 carefully. **The conference version omits crucial detail; assign this one** | `https://raft.github.io/raft.pdf` |
| MIT's mirror of the same | `https://pdos.csail.mit.edu/6.824/papers/raft-extended.pdf` |
| **The Raft site** — the interactive visualization, talks, 100+ implementations | `https://raft.github.io/` |
| 🔴 **Ongaro's PhD thesis** — everything the paper omits: membership changes, log compaction, client semantics, the correctness proof. **Read before implementing** | `https://web.stanford.edu/~ouster/cgi-bin/papers/OngaroPhD.pdf` |
| **The Secret Lives of Data** — the animated walkthrough. **The best first exposure, W38 day one** | `https://thesecretlivesofdata.com/raft/` |
| 🔴 **Students' Guide to Raft** (Gjengset) — catalogues the exact mistakes implementers make. **Read *while* implementing, not before** | `https://thesquareplanet.com/blog/students-guide-to-raft/` |
| 🔴 **The membership-change bug thread** — **the author announcing a safety bug in his own thesis's protocol, with the fix.** The single best document on Raft's subtle failure modes, and a lesson in intellectual honesty | `https://groups.google.com/g/raft-dev/c/t4xj6dJTP6E` |
| **etcd-io/raft** — the most battle-tested library; its separation of protocol logic from I/O is a masterclass in testable design | `https://github.com/etcd-io/raft` · `https://pkg.go.dev/go.etcd.io/raft/v3` |
| **hashicorp/raft** — a contrasting design that owns its own I/O. **Read both and form an opinion** | `https://github.com/hashicorp/raft` |
| **tikv/raft-rs** — how Raft scales to many groups | `https://github.com/tikv/raft-rs` |
| 🔴 **raft.tla** — Ongaro's own TLA+ spec. **The bridge between this department and the next** | `https://github.com/ongardie/raft.tla` |
| **Jepsen: etcd 3.4.3** — what real consistency testing of a Raft system finds, and what "linearizable" does and does not buy you | `https://jepsen.io/analyses/etcd-3.4.3` |
| **Jepsen analyses index** — the best available catalogue of distributed-system failure case studies | `https://jepsen.io/analyses` |

### Formal methods, lite

| Resource | Link |
|---|---|
| 🔴 **Learn TLA+** (Hillel Wayne) — PlusCal-first, practical, no mathematical prerequisites. **The core curriculum** | `https://learntla.com/core/index.html` |
| Advanced topics — refinement, liveness, model-size control | `https://learntla.com/topics/` |
| 🔴 **How AWS Uses Formal Methods** (Newcombe et al., CACM 2015) — **read first**, to understand why the hours are worth it. Real bugs in DynamoDB and S3 that testing could never have caught | `https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf` |
| **Lamport's TLA+ video course** — the "why it is built this way" track | `https://lamport.azurewebsites.net/video/videos.html` |
| **Specifying Systems** (Lamport, free) — the reference for when the tools surprise you | `https://lamport.azurewebsites.net/tla/book.html` |
| **TLC and the Toolbox** · **the Examples corpus** — the fastest way to learn idiomatic TLA+ | `https://github.com/tlaplus/tlaplus` · `https://github.com/tlaplus/Examples` |
| **The Business Case for Formal Methods** — the argument to make to a sceptical team | `https://www.hillelwayne.com/post/business-case-formal-methods/` |

---

## V.F DEPARTMENT OF OPERATIONS

> **The shell is what the screen reads.** AWS 48.9% · Kubernetes 30.4% · observability 22.0% · on-call 21.5%. This department runs in Level 8 and **it is never cut.**

| Resource | Link |
|---|---|
| 🔴 **Kubernetes The Hard Way** (Kelsey Hightower) — bootstrap a cluster component by component. **The only way to actually understand the control plane** | `https://github.com/kelseyhightower/kubernetes-the-hard-way` |
| **Kubernetes Concepts** — Architecture, Workloads, Services | `https://kubernetes.io/docs/concepts/` |
| 🔴 **Kubernetes API Conventions** — spec/status, the reconciliation model, and why the API is shaped as it is. **The single best document for understanding Kubernetes' philosophy** | `https://github.com/kubernetes/community/blob/main/contributors/devel/sig-architecture/api-conventions.md` |
| **Kubernetes API Concepts** — resource versions, watch semantics, pagination | `https://kubernetes.io/docs/reference/using-api/api-concepts/` |
| **KEPs** — every feature's design rationale **and its rejected alternatives.** The real architecture documentation | `https://github.com/kubernetes/enhancements` |
| **The Kubebuilder Book** — controllers, CRDs, the reconcile loop | `https://book.kubebuilder.io/` |
| **A few things I've learned about Kubernetes** (Julia Evans) — an honest engineer's account of what is actually confusing | `https://jvns.ca/blog/2017/06/04/learning-about-kubernetes/` |
| 🔴 **Kubernetes Failure Stories** — **read ten.** The highest learning-per-minute in the ecosystem | `https://k8s.af/` |
| **cgroups v2 kernel docs** — the unified hierarchy and the CPU/memory/IO controllers that define every container limit you will ever debug | `https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html` |

### The SRE books — free, and assigned by chapter

| Chapter | Why | Link |
|---|---|---|
| **SRE Ch. 4 — Service Level Objectives** | SLIs, SLOs, error budgets. **The chapter that changes how teams make decisions** | `https://sre.google/sre-book/service-level-objectives/` |
| **SRE Ch. 6 — Monitoring Distributed Systems** | The four golden signals; the antidote to alert fatigue | `https://sre.google/sre-book/monitoring-distributed-systems/` |
| 🔴 **SRE Ch. 21 — Handling Overload** | Graceful degradation, client throttling, criticality | `https://sre.google/sre-book/handling-overload/` |
| 🔴 **SRE Ch. 22 — Addressing Cascading Failures** | Retry storms, thundering herds, death spirals. **Possibly the most valuable chapter in the book** | `https://sre.google/sre-book/addressing-cascading-failures/` |
| **SRE Ch. 15 — Postmortem Culture** | The practice that turns incidents into engineering | `https://sre.google/sre-book/postmortem-culture/` |
| **Workbook Ch. 2 — Implementing SLOs** | The how-to Ch. 4 leaves out; worked examples and error-budget policies | `https://sre.google/workbook/implementing-slos/` |
| **Workbook Ch. 4 — Monitoring** | Concrete patterns and anti-patterns | `https://sre.google/workbook/monitoring/` |
| *Full table of contents* | | `https://sre.google/books/` |

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
| 🔴 **Englehardt & Narayanan, "Online Tracking: A 1-Million-Site Measurement and Analysis"** (CCS 2016) | **The paper whose methodology you are replicating at smaller scale and greater currency.** 15 measurement types, stateful and stateless tracking, cookie syncing — and it produced OpenWPM | slides `https://senglehardt.com/presentations/2016_10_ccs_online_tracking.pdf` |
| **Acar et al., "The Web Never Forgets"** (CCS 2014) | The first large-scale measurement of **canvas fingerprinting, evercookies and cookie respawning** | `https://www.esat.kuleuven.be/cosic/publications/article-2457.pdf` |
| 🔴 **Web Almanac 2024 — Privacy chapter** | **95% of desktop and 94% of mobile sites carry at least one tracker; 27% carry more than ten.** Every query and figure published and reproducible, Apache 2.0. **Your baseline statistics, free** | `https://almanac.httparchive.org/en/2024/privacy` |
| 🔴 **Böttger et al., "From Third-Party to First-Party"** (arXiv 2026) | **The single most on-point paper for your thesis** — and the reason finding #3 above exists | `https://arxiv.org/abs/2606.16720` |
| **Fouad, Santos, Laperdrix, "Server-Side Tracking"** (PETS 2024) | The blind spot every client-side crawler misses, and how to detect it | `https://hal.science/hal-04617727v1/document` |
| **Sivan-Sevilla & Poudel, "Web Privacy based on Contextual Integrity"** (2024) | 🔴 **Frames tracking as *context collapse* — which is exactly the harm per-identity compartments address.** Useful framing for your README's opening | `https://arxiv.org/abs/2412.16246` |
| **Singh et al., "Where in the World Are My Trackers?"** (IMC 2025) | Tracking varies by vantage point — **directly informs where you crawl from and where you place exits** | `https://doi.org/10.1145/3730567.3764427` |

### G.2 · Cross-site linkage — the mechanism your graph is measuring

| Resource | Why | Link |
|---|---|---|
| 🔴 **Papadopoulos, Kourtellis, Markatos, "Cookie Synchronization: Everything You Always Wanted to Know But Were Afraid to Ask"** (WWW 2019) | **The reference cookie-sync measurement, and your Level 2 centrepiece.** Quantifies anonymity loss per ad impression (**~3.4 syncs**) and how identifiers diffuse | `https://arxiv.org/abs/1805.10505` |
| 🔴 **Munir et al., "CookieGraph"** (CCS 2023) | **First-party cookies get synced to third parties on a large majority of sites — the mechanism that survives third-party cookie deprecation.** This is what finding #3 means in practice | `https://arxiv.org/abs/2208.12370` |
| **Dimova et al., "The CNAME of the Game"** (PoPETs 2021) | CNAME cloaking: first-party-disguised third-party tracking. 🔴 **Resolve CNAMEs in your crawler or you will undercount** | `https://www.esat.kuleuven.be/cosic/publications/article-3303.pdf` |
| **Brave Research, "Measuring UID Smuggling in the Wild"** (IMC 2022) | Identifiers smuggled through URL parameters — **the link-decoration channel that defeats cookie blocking** | `https://brave.com/research/measuring-uid-smuggling-in-the-wild/` |
| 🔴 **Su, Shukla, Goel, Narayanan, "De-anonymizing Web Browsing Data with Social Networks"** (WWW 2017) | **"De-identified" browsing histories re-linked to named people via public social activity.** The strongest single argument that clickstream anonymisation fails — **quote this one in your demo** | `https://doi.org/10.1145/3038912.3052714` |
| **Deuser, Passmann, Strufe, "Browsing Unicity"** (IEEE S&P 2020) | **How few observations are needed to single out one user** | `https://doi.org/10.1109/sp40000.2020.00018` |
| **Brookman et al., "Cross-Device Tracking"** (PoPETs 2017) | 861 third-party domains collecting linkage-capable data; cross-device specialists on 34% of sites | `https://crysp.petsymposium.org/popets/2017/popets-2017-0020.pdf` |
| **Senol et al., "Leaky Forms"** (USENIX Sec 2022) | **Email addresses — the strongest cross-site identifier — exfiltrated before you press submit.** Dataset public | `https://gunesacar.net/papers/leaky-forms-usenix-sec-22.pdf` |

### G.3 · Fingerprinting — and the honesty that must come with it

| Resource | Why | Link |
|---|---|---|
| **Eckersley, "How Unique Is Your Web Browser?"** (PETS 2010) | Panopticlick: ≥18.1 bits of entropy. The origin of the field | `https://pde.is/research/2010panopticlick/` |
| **Laperdrix et al., "Browser Fingerprinting: A Survey"** (ACM TWEB 2020) | The reference survey — mechanics, vectors, defence taxonomy | `https://arxiv.org/abs/1905.01051` |
| 🔴 **Gómez-Boix, Laperdrix, Baudry, "Hiding in the Crowd"** (WWW 2018) | **THE essential counterweight.** On 2M real fingerprints, **uniqueness is far lower than Panopticlick suggested**, especially on mobile. 🔴 **Cite this to stay honest — it argues partly against your own project's framing, and including it is what makes the rest credible** | `https://hal.inria.fr/hal-01718234/document` |
| 🔴 **Annamalai, Bilogrevic, De Cristofaro, "Beyond the Crawl"** (WWW 2025) | **Read before designing your crawler.** The 45% finding | `https://arxiv.org/abs/2502.01608` |
| **Bacis et al. (Google), "Assessing Web Fingerprinting Risk"** (WWW 2024) | Entropy measured across **tens of millions of real Chrome browsers** — the largest ground truth that exists | `https://arxiv.org/abs/2403.15607` |
| 🔴 **Berke et al., "How Unique is Whose Web Browser?"** (PoPETs 2025) | **Lower-income users are more fingerprintable, and demographics are predictable from browser attributes.** A genuine equity argument for your project, and a strong paragraph in the README | `https://arxiv.org/abs/2410.06954` |
| **Vastel et al., "FP-STALKER"** (IEEE S&P 2018) | Fingerprints change — this measures how long you can still **link** them across changes. *The linkability paper, not the uniqueness paper* | `https://hal.inria.fr/hal-01652021/document` |
| 🔴 **Amin Azad et al., "Taming The Shape Shifter"** (DIMVA 2020) | **Anti-fingerprinting browsers are themselves detectable, which can make you *more* identifiable.** The core "do defences actually work?" result, and the reason you do not fork the browser | `https://hal.archives-ouvertes.fr/hal-02612461/document` |
| **Laor et al., "DRAWNAPART"** (NDSS 2022) | **WebGL fingerprinting at the physical-GPU level — survives a browser reinstall.** The hardest vector, and one you cannot defend against at the network layer. *Say so* | `https://hal.inria.fr/hal-03526240/document` |

### G.4 · The tools — read the methodology papers before picking one

| Tool | What it is | Link |
|---|---|---|
| 🔴 **OpenWPM** | The de facto standard Firefox+Selenium privacy crawler, actively maintained (**v0.37.0 pins Firefox 155**). **Cite the exact version** | `https://github.com/openwpm/OpenWPM` |
| **Tracker Radar Collector** (DuckDuckGo) | The **Puppeteer/Chromium** crawler that generates Tracker Radar. The best-documented production-grade Chromium alternative | `https://github.com/duckduckgo/tracker-radar-collector` |
| 🔴 **Blacklight Query** (The Markup) | **Batch-scans a URL list from the terminal with zero code.** The fastest path to a credible first result — run it in Week 9 while you build the real thing | `https://github.com/the-markup/blacklight-query` |
| 🔴 **WebREC / `.web` bundles** (Brave, USENIX Sec 2025) | **Reproducible, archivable web measurements.** 48% of surveyed papers could have reused archives without re-crawling. **Solves the thing most crawl studies fail at** | `https://brave.com/research/files/webrec-usenix-2025.pdf` · `https://github.com/brave/pagegraph-crawl` |
| **Privacy Pioneer crawler** (PoPETs 2024) | Detects **what personal data** is collected, not just which trackers are present | `https://github.com/privacy-tech-lab/privacy-pioneer-web-crawler` |
| 🔴 **Gundelach et al., "Detecting Bot Detection"** (2026) | **The most important paper for your crawler design.** Finding #2 above | `https://arxiv.org/abs/2606.14525` |
| **Stafeev & Pellegrino, "SoK: State of the Krawlers"** (USENIX Sec 2024) | How crawl *strategy* — depth, navigation policy — changes what you see | `https://www.cispa.de/en/stafeev-webcrawlers` |
| **Jueckstock et al., "Towards Realistic and Reproducible Web Crawl Measurements"** (WWW 2021) | Vantage point and statefulness materially change measured tracking | `https://www.kapravelos.com/publications/vpc-www21.pdf` |

**Lists and samples:** 🔴 **Tranco** — `https://tranco-list.eu/`, **free, daily, and every list has a permanent citable ID** · **EasyList / EasyPrivacy** — `https://easylist.to/`, **dual GPLv3 / CC BY-SA, the permissive option** · **Disconnect** and **DuckDuckGo Tracker Radar** — richer (ownership, prevalence, categories) but ⚠️ **CC BY-NC-SA, non-commercial only** · **third-party-web** — origin→company mapping from monthly crawls of ~4M sites, free · 🔴 **WhoTracks.Me** — **real-user data from 5M+ users and 1.5B page loads, free via `aws s3 sync --no-sign-request s3://data.whotracks.me/`.** The natural complement to the "crawls miss 45%" finding ⚠️ *licence not stated — confirm before redistributing*

### G.5 🔴 · Why the IP is the thing — the core of your premise

| Resource | Why | Link |
|---|---|---|
| 🔴🔴 **Mishra et al., "Don't Count Me Out: On the Relevance of IP Addresses in the Tracking Ecosystem"** (WWW 2020) | **THE core paper for your project's premise.** Devices reuse previous IPs for long periods — **IP is a far better re-identifier than the "dynamic IPs churn constantly" folk model claims.** If you cite one paper in your README, cite this | `https://hal.inria.fr/hal-02435622/document` |
| **Richter et al., "A Multi-perspective Analysis of Carrier-Grade NAT Deployment"** (IMC 2016) | How many subscribers share an address — **the ceiling on how much any single IP can identify.** The honest counterweight | `https://arxiv.org/abs/1605.05606` |
| **Padmanabhan et al., "Reasons Dynamic Addresses Change"** (IMC 2016) | *When* and *why* ISPs reassign residential addresses — **many rotate on fixed multiples of 24 h.** Cite for "how long does an IP stay linkable to a household" | `https://doi.org/10.1145/2987443.2987461` |
| **RFC 6269 — Issues with IP Address Sharing** | The normative *"an IP is not a user"* citation | `https://www.rfc-editor.org/rfc/rfc6269.html` |
| 🔴 **Breyer v Bundesrepublik Deutschland (C-582/14)**, CJEU 2016 | **Dynamic IPs are personal data under EU law** where the operator has lawful means to identify. **One paragraph, and it is the legal spine of your problem statement** | `https://curia.europa.eu/juris/document/document.jsf?docid=184668&doclang=EN` |
| 🔴 **FTC, "A Look at What ISPs Know About You"** (6(b) study, 2021) | **Compulsory-process findings on six major ISPs**: they collect all Internet traffic and real-time location with little meaningful choice. **The strongest citable US evidence for ISP-side collection** | `https://www.ftc.gov/system/files/documents/reports/look-what-isps-know-about-you-examining-privacy-practices-six-major-internet-service-providers/p195402_isp_6b_staff_report.pdf` |

**Data brokers — the assembly step:** **FTC, "Data Brokers: A Call for Transparency and Accountability"** (2014), the foundational regulatory study · **Sherman (Duke), "Data Brokers and Sensitive Data on US Individuals"** (2021), sourced by **direct purchase** · **Kim (Duke), "The Sale of Americans' Mental Health Data"** (2023), the most-cited concrete harm study · 🔴 **Gueorguieva et al. (Stanford), "Privacy Without Remedy"** (2026) — an audit of **522 registered brokers** showing **opt-out does not work.** *Prevention over removal, evidenced*

### G.6 🔴 · Does the deployed answer actually work? — read before you claim latency

| Resource | Why | Link |
|---|---|---|
| 🔴🔴 **Trevisan et al., "Measuring the Performance of iCloud Private Relay"** (PAM 2023) | **Up to 10× lower speed-test performance, plus page-load penalties.** *This is the deployment-friction reality check for your entire premise. Adyton's claim is "at latency a normal person will accept" — **this paper is the evidence that the incumbent does not meet that bar**, and it is simultaneously the standard you must beat and the reason the project has a point* | `https://pschmitt.net/docs/pam23_pr.pdf` |
| **Ravalico et al., "Measuring iCloud Private Relay: Desktop and Mobile"** (2025) | **RECENT** — current numbers | `https://doi.org/10.2139/ssrn.5361064` |
| 🔴 **Zohaib, Sheffey, Houmansadr, "Investigating Traffic Analysis Attacks on Apple iCloud Private Relay"** (AsiaCCS 2023) | **IP hiding does not defeat correlation or website fingerprinting.** The necessary caveat on your own claim, and the bridge to §V.C.5 | `https://doi.org/10.1145/3579856.3595793` |
| **Google Chrome IP Protection** | Two-hop proxy with RSA blind signatures, Incognito-only, regional rollout. ⚠️ *The explainer repo was archived in Nov 2025 — check the Privacy Sandbox status page before asserting its state* | `https://privacysandbox.google.com/protections/ip-protection` |
| **"Lost in the Prefix: Revisiting IP Geolocation Accuracy"** (2026) | **RECENT** — **mobile median error 179–207 km vs 3–16 km fixed**, failure rates 53–72% in Asia/Africa vs 9–20% in Europe. 🔴 *Relevant to you specifically: geolocation of an Egyptian client is much worse than the marketing assumes, in both directions* | `https://arxiv.org/abs/2605.21937` |

### G.7 · AS-graph infrastructure — Level 9, and 🚨 request access in Week 45

> 🚨 **Two scheduling facts to act on early.** **(1)** CAIDA's **AS Relationships** data — the thing you actually need — is **free with no registration.** But the **recent-year ITDK and Ark traceroute data is restricted** to academics, US government and CAIDA members, via a request form with a **2–3 business-day turnaround.** If you want it, request it in Week 45, not Week 49. **(2)** RIPE Atlas traceroutes cost **30 credits per result** (doubled for one-offs), and you earn ~21,600/day per hosted probe. **Host a probe now** and let the **free built-in measurement corpus** carry your bootstrap.

| Resource | Access | Link |
|---|---|---|
| 🔴 **CAIDA AS Relationships (serial-1 / serial-2)** | **Free, no registration.** Monthly p2c/p2p files — **the core input, and what Astoria, DeNASA, Counter-RAPTOR and CLAPS all consume** | `https://publicdata.caida.org/datasets/as-relationships/serial-1/` |
| **CAIDA AS Rank + API** | **Free, no key.** Per-AS rank, customer cone, clique membership, historical snapshots. 🔴 *Use it to score candidate relay ASes by transit centrality* | `https://asrank.caida.org/` · `https://api.asrank.caida.org/v2/docs` |
| **CAIDA AS-to-Organization** | Free under AUA. 🔴 **Essential: collapse sibling ASes so two relays in one org are not counted as independent** | `https://www.caida.org/catalog/datasets/as-organizations/` |
| **Routeviews Prefix-to-AS** | Free, daily. **How you resolve a relay IP to an ASN** | `https://publicdata.caida.org/datasets/routing/routeviews-prefix2as/` |
| **CAIDA ITDK / Ark traceroutes** | ⚠️ **Restricted for the recent year; request form, 2–3 days** | `https://catalog.caida.org/datasets/request_user_info_forms/topology_request` |
| 🔴 **Internet Yellow Pages (IYP)** (IMC 2024) | **The highest-leverage single tool here.** A Neo4j knowledge graph unifying 27+ sources, **freely queryable via Cypher with no auth**, Docker image for local use | `https://iyp.iijlab.net/` · tutorial `https://tutorial.iyp.ihr.live/` |
| **BGPStream / PyBGPStream** | Free/open. Unified API over RouteViews + RIS, live and historical. 🔴 **Write code against this, not raw MRT** | `https://bgpstream.caida.org/` |
| **RIPE Atlas built-in measurements** | 🔴 **Results readable free via the REST API, zero credits.** Every probe auto-pings roots every 240 s and traceroutes every 1800 s. **The best free continuously-collected global RTT corpus** | `https://atlas.ripe.net/docs/built-in-measurements/` |
| **`ripe-atlas-cousteau`** and **`ripe.atlas.sagan`** | Free/open. 🔴 *Sagan absorbs dozens of traceroute-format edge cases — **do not hand-roll the parsing*** | `https://github.com/RIPE-NCC/ripe-atlas-cousteau` · `https://github.com/RIPE-NCC/ripe.atlas.sagan` |
| **PeeringDB API** | **Read is free and anonymous**; write needs a key | `https://www.peeringdb.com/apidocs/` |
| 🔴 **Sermpezis et al., "Bias in Internet Measurement Platforms"** (TMA 2023) | **How Atlas/RouteViews/RIS probe placement is skewed by geography, AS type and topology. Read before generalising any Atlas latency number** | `https://doi.org/10.23919/tma58422.2023.10198985` |
| **Chatzis et al., "There Is More to IXPs Than Meets the Eye"** (CCR 2013) | 🔴 **The argument for placing relays at or near IXPs** rather than reasoning purely from the inferred AS graph | `https://doi.org/10.1145/2541468.2541473` |
| **PredictRoute** (SIGMETRICS 2021) | **The most practical off-the-shelf path predictor**, with accuracy reported against measured paths | `https://escholarship.org/uc/item/4xn2f3s3` |
| **Sibyl** (NSDI 2016) | 🔴 *Query for routes matching high-level properties — "find a path avoiding AS X" — and issue the minimum traceroutes to answer. **Exactly the primitive a relay selector needs*** | `https://www.usenix.org/conference/nsdi16/technical-sessions/presentation/cunha` |

### G.8 · Differential privacy for engineers — Level 7's telemetry plane

🔴 **Near & Abuah, *Programming Differential Privacy*** — a living open book with **executable Python chapters and no measure theory.** The best engineer-facing DP primer that exists · `https://programming-dp.com/`
**Damien Desfontaines, "A friendly, non-technical introduction to differential privacy"** — the series index, branching into the how and the why, including **when *not* to use DP** · `https://desfontain.es/blog/friendly-intro-to-differential-privacy.html`
🔴 **NIST SP 800-226, "Guidelines for Evaluating Differential Privacy Guarantees"** (Final, 2025) — **the normative checklist for judging a DP claim. Use it to write up your own defensibly** · `https://csrc.nist.gov/pubs/sp/800/226/final`
**NIST IR 8588 — DP Deployment Registry** (2025) — **a rare source of grounded real-world epsilon precedent** · `https://csrc.nist.gov/pubs/ir/8588/ipd`
**Janus + libprio-rs** (ISRG) — production DAP aggregator and Rust Prio/VDAF library. 🔴 **The most practical starting point for your aggregator** · `https://github.com/divviup/janus`
**OpenDP / SmartNoise** · **Google's differential-privacy library** (with **DP Auditorium** for auditing your own guarantees) · `https://opendp.org/` · `https://github.com/google/differential-privacy`
**Apple, "Learning with Privacy at Scale"** and **RAPPOR** (CCS 2014) — the two deployed local-DP systems, with real bandwidth and accuracy numbers · `https://machinelearning.apple.com/research/learning-with-privacy-at-scale` · `https://arxiv.org/abs/1407.6981`
---
---

# PART VI — THE TERM

> **This is the part you open every morning.**
>
> Each week gives you: 📺 **lectures** · 📄 **papers and articles** · 📕 **book pages** · 🛠 **the build** · ✅ **what must be true by Sunday** · 🧩 **DSA** · 🏛 **system design** · ❓ **the questions I will not answer.**
>
> **Links to the full resource entries live in Part V.** Inline links here are the specific thing you need *today*.
>
> **The weekend blocks are where Adyton gets built. Weekdays are lectures, reading, DSA and design.** If a week runs long, the buffer weeks are W18, W32 and W44 — **take them from there, not from Track I.**

---
---

# ⚡ LEVEL 0 — FOUNDATIONS & THE MEASUREMENT
### W1–3 · 14 Sep – 4 Oct 2026 · 3 weeks · Fundamentals F1

> **Goal:** build the hardware mental model, make every number you produce this year trustworthy, and find out in Week 2 — not Week 30 — how big your mesh can actually be.

## ⬛ WEEK 1 · 14–20 Sep · *the first week*

> 🔥 **THE WALL.** Two functions summing the same 4096×4096 `int32` matrix, row-major and column-major. **Identical Big-O. Column-major will be 5–60× slower.** Then two `int64` counters in one struct, two threads incrementing one each; then padded onto separate 64-byte cache lines. **Same work, 3–10× throughput difference.** *You may not read on until both numbers are on your screen.*

**📺 LECTURES (3h)**
- [ ] **CS:APP / 15-213 — the memory hierarchy and cache memories slides.** ⚠️ No video exists; these are slide decks + the book. `https://www.cs.cmu.edu/afs/cs/academic/class/15213-f25/www/lectures/` → `09-memory.pdf`, `10-cachememories.pdf`

**📕 PAGES (3h)**
- [ ] **CS:APP §6.2–6.4 only** (~40 pages). Skip §6.1
- [ ] **Drepper, "What Every Programmer Should Know About Memory" §3 in full** — `https://lwn.net/Articles/250967/` (full PDF: `https://people.freebsd.org/~lstewart/articles/cpumemory.pdf`)

**📄 READ (1h)**
- [ ] **Igor Ostrovsky, "Gallery of Processor Cache Effects"** — ten experiments. **Run all of them, do not just read them**
- [ ] **Colin Scott's interactive latency numbers** — `https://colin-scott.github.io/personal_website/research/interactive_latency.html`. Scrub 1990→2020 and note what changed and what did not

**🛠 BUILD (14h)**
- [ ] Repo, CI skeleton, toolchains: C++20 + CMake + vcpkg, Java 21, Go, Python
- [ ] 🔴 **`docs/scope.md`** — the §I.4 decision, one page, written *this week* and never revisited
- [ ] **`lab/latency-lab`** — measure this machine's ladder and emit a card: L1/L2/L3/DRAM, uncontended vs contended atomic, mutex, branch mispredict, NVMe 4K read, syscall, context switch, **TCP loopback RTT, and RTT to a free-tier box in Frankfurt.** Derive your cache sizes from a working-set sweep, **without asking the OS**

**✅ BY SUNDAY**
- [ ] Derived cache sizes match `lscpu` within one power of two — or you can explain why not
- [ ] Row-major vs column-major gap **explained by measured LLC-miss counts**, not asserted
- [ ] False-sharing fix ≥3× throughput, `perf c2c` output committed
- [ ] A chart: working-set size (log x) vs ns/access, knees annotated
- [ ] **The network row measured, not looked up.** 🔴 *A cross-continent RTT of ~90 ms is the floor on every circuit you will ever build. Write that number on something you can see*

**🧩 DSA (5.5h) —** arrays, hashing, prefix sums, two pointers. NeetCode Arrays & Hashing (all 9). 🔴 *The cache intuition you built today is **why** these are fast in practice, not just in Big-O.*
**🏛 DESIGN (2.5h) —** the estimation module. Memorise the numbers in §VII.8. First written estimate: *how much storage does a relay network carrying 10k users need for one month of consensus documents?*

> ❓ **GO FIND OUT**
> 1. Your L1 is ~1 ns and a cross-continent RTT is ~90 ms. **How many L1 accesses fit inside one RTT?** Compute it; the number should disturb you.
> 2. What is `perf c2c` actually measuring, and which CPU counter does it read?
> 3. Why is an *uncontended* atomic still slower than a plain load?

## ⬛ WEEK 2 · 21–27 Sep · 🔴 *the scale spike — do not defer this*

> 🔥 **THE WALL.** Benchmark a trivial function five times. **The numbers differ by 15–40%.** Find out why, one cause at a time: frequency scaling, turbo, thermal throttling, ASLR changing alignment, thread migration, cold first iterations. Then build a **closed-loop** generator and an **open-loop** one, point both at a service that stalls 200 ms once a second, **and watch the closed-loop harness report a beautiful p99 that is a lie.**

**📄 READ (3h)**
- [ ] 🔴 **Gil Tene, "How NOT to Measure Latency"** — `https://www.infoq.com/presentations/latency-response-time/`. **Before you publish any benchmark this year.** You will audit your own harness against it in Week 47
- [ ] **Dean & Barroso, "The Tail at Scale"** (CACM 2013), eight pages — `https://research.google/pubs/the-tail-at-scale/`
- [ ] **Brendan Gregg, The USE Method** + the Linux checklist — `https://www.brendangregg.com/usemethod.html`

**🛠 BUILD (16h)**
- [ ] **`lab/bench`** — the harness you use all year: fixed workloads, warm-up, percentiles, `perf stat` integration, **open-loop by default**, CI regression gate, **HdrHistogram** for percentiles (`http://hdrhistogram.org/`), and **four `tc netem` profiles** (clean · 1% loss · 5% loss + jitter · mobile) applied from config so **every network number states its conditions**
- [ ] **`sickbay`** — 8 injectable pathologies in a container, each with a hidden `SOLUTION.md` showing the *evidence* that reveals it
- [ ] 🔴 **`docs/SCALE-RISK.md`** — start 40 relay-shaped processes at realistic memory. **What breaks first: RAM, file descriptors, ephemeral ports, or the scheduler?** Provision the **Oracle always-free ARM box** (4 cores / 24 GB, no expiry); verify you reach it and it reaches you from Cairo; confirm **$0.00**

**✅ BY SUNDAY**
- [ ] Two runs produce byte-identical result sets (fixed seeds, stable tie-breaking)
- [ ] Harness is **open-loop by default** and you can explain why in one paragraph
- [ ] A deliberate 5% regression is caught by `benchstat` in CI
- [ ] **`sickbay`: median diagnosis under 10 minutes across all 8, on a shuffled re-run**
- [ ] 🔴 **A signed, dated go/no-go on the local-mesh-plus-simulator strategy**, with the binding resource named
- [ ] **Check whether `cs144.github.io` is back** *(see §IV.0 — it was 404 on 14 Sep)*. Do this every week until it returns, then **mirror the repo privately the same day**

**🧩 DSA (5.5h) —** two pointers, sliding window. NeetCode Two Pointers (5) + Sliding Window (6). Capstone: **LC 76 Minimum Window Substring**, narrated, under 25 min.
**🏛 DESIGN (2.5h) —** design a URL shortener. Practise the sentence: *"I'm optimising for X, which costs me Y."*

> ❓ **GO FIND OUT**
> 1. What is coordinated omission, in one sentence you could say to a manager? **Sketch a harness where a 200 ms stall is invisible.**
> 2. Why can you not average percentiles? What do you do instead?
> 3. Find out what `tc netem`'s `distribution normal` option actually does to the delay. Why does it matter for a relay?

## ⬛ WEEK 3 · 28 Sep – 4 Oct

**📺 LECTURES (3h)**
- [ ] **Berkeley CS161 — *Security Principles* and *x86 Assembly and the Call Stack***. `https://www.youtube.com/@berkeley-cs161` · textbook `https://textbook.cs161.org`

**📄 READ (3h)**
- [ ] 🔴 **The Tor Research Safety Board's principles** — `https://research.torproject.org/safetyboard/`. **Read this before Level 2 collects a single byte.** It is the ethics layer of every measurement in this curriculum
- [ ] **Marc Brooker, "Telling Stories About Little's Law"** — `https://brooker.co.za/blog/2018/06/20/littles-law.html`

**🛠 BUILD (13h)**
- [ ] **`1brc` v1** — the One Billion Row Challenge, your naive first attempt. Time it, commit it, and **do not optimise it.** You come back in Week 51 and report the delta. 🔴 *This is the only number in your whole repo that a stranger can check against a public leaderboard*
- [ ] Repo hygiene: `make bootstrap` works on a clean clone, README skeleton with the honesty and scale statements already in place

**✅ BY SUNDAY**
- [ ] `1brc` v1 runs and its time is recorded in `bench/RESULTS.md` with the machine spec
- [ ] **`make bootstrap` works on a clean clone.** You will re-verify this at every level boundary
- [ ] 📝 **Track J:** ask to review someone's PR at Logic Leap. Start the habit this week

**🧩 DSA (5.5h) —** finish NeetCode Arrays/Hashing/Two Pointers/Sliding Window. **~28 problems cumulative.**
**🏛 DESIGN (2.5h) —** design a rate limiter. You build one for real in Level 8.

> ❓ **GO FIND OUT**
> 1. Read the 1BRC leaderboard's top entries. **Name three techniques you do not currently understand.** Write them down; you will use at least two in Week 51.
> 2. What does the Tor Safety Board say about measuring a live network? Which of its principles applies to crawling the public web?

---
---

# ⚡ LEVEL 1 — ⚙️ C++, SANITIZERS & THE THREAT
### W4–8 · 5 Oct – 8 Nov 2026 · 5 weeks · **Milestone D0** · 🚩 **Flagship #1 `hardened`** · Fundamentals F2, F3

> **Goal:** a relay daemon that forwards, and that **hostile input cannot crash.** And the safety apparatus that is the argument for having chosen C++ at all.
>
> 🔴 **This level is where the C++ decision is either earned or exposed.** Sanitizers and fuzzing are scheduled work from Week 4, not hygiene you get to later.

## ⬛ WEEK 4 · 5–11 Oct

> 🔥 **THE WALL — four failures, in order.** Write the obvious framing: `send(json.dumps(msg).encode())`, `json.loads(sock.recv(4096))`. Then: **(1)** send two messages quickly — they arrive glued together, or half of one does. **TCP is a byte stream, not a message stream.** **(2)** Send 10 MB — `recv(4096)` gets 4096 bytes. **(3)** 🔴 **Send a length prefix of `0xFFFFFFFF`. Your receiver allocates 4 GB and dies. A hostile peer just killed your relay with four bytes.** **(4)** Add a field and deploy one side. The other breaks.

**📺 LECTURES (3h)**
- [ ] **CS161 — *Memory Safety Vulnerabilities* and *Mitigating Memory-Safety Vulnerabilities***

**📄 READ (3h)**
- [ ] 🔴 **Chromium: Memory safety** — `https://www.chromium.org/Home/chromium-security/memory-safety/`. **~70% of serious Chromium security bugs are memory-safety bugs.** Read the number, then read the next item
- [ ] 🔴 **Tor: "Announcing Arti, a pure-Rust Tor implementation"** — `https://blog.torproject.org/announcing-arti/`. **~half of Tor's tracked security bugs since 2016 were memory-safety issues impossible in safe Rust.** *Read these two on the same day you commit to C++, and let it make you uncomfortable. That discomfort is exactly what the rest of this level answers*
- [ ] **Google, "Building a good fuzz target"** — `https://github.com/google/fuzzing/blob/master/docs/good-fuzz-target.md`

**🛠 BUILD (16h)**
- [ ] **`adyton-node` skeleton** (C++20) + **`adyton-wire/codec`**: length-prefixed frames with a **hard maximum validated before allocation**, CRC, varints, zero-copy `std::span` views, arena allocation
- [ ] 🔴 **The apparatus, wired into CI this week:** ASan + UBSan + TSan on every run · `-Wall -Wextra -Werror -fno-omit-frame-pointer` · `clang-tidy` with `cppcoreguidelines-*` and `bugprone-*` · **libFuzzer on the frame parser**

**✅ BY SUNDAY**
- [ ] All four wall failures reproduced and **screenshotted**
- [ ] ASan/UBSan/TSan green in CI, **with a screenshot of a deliberately-introduced violation being caught**
- [ ] The fuzzer runs. **It does not need to be clean yet**

**🧩 DSA (5.5h) —** 🔴 **binary search, including on the answer** — LC 704, 74, 153, 33, **875 Koko**, **1011 Capacity to Ship**, 410. *875 and 1011 are literally how you will pick a frame-size parameter.*
**🏛 DESIGN (2.5h) —** design a distributed job queue.

> ❓ **GO FIND OUT**
> 1. Your parser validates the length before allocating. **Name three other places in a network daemon where "validate before you act" applies**, and find one real CVE for each.
> 2. What does `-fno-omit-frame-pointer` cost you, and why is it worth it?
> 3. Read Arti's announcement again. **Write one paragraph you would say to an interviewer who asks "why didn't you use Rust?"** Keep it; you will refine it all year.

## ⬛ WEEK 5 · 12–18 Oct

**📕 PAGES (3h)** — **OSTEP ch. 4–7** (processes, the API, direct execution, scheduling), free at `https://pages.cs.wisc.edu/~remzi/OSTEP/`
**📄 READ (2h)** — **C++ Core Guidelines**: the **Resource Management**, **Bounds** and **Lifetime** profiles · **`std::span`** on cppreference

**🛠 BUILD (17h)**
- [ ] Varint encode/decode · capability-negotiating handshake · explicit version field · **authenticated framing** (a frame failing its MAC is dropped *before* further parsing, and the failure is **counted and rate-limited**, not logged per occurrence — or a peer fills your disk)
- [ ] 🔴 **`docs/cpp-subset.md`** — what you do not use, and why. *This document is the C++ decision in written form*

**✅ BY SUNDAY** — an old pinned client binary interoperates with the new server, **asserted by a test** · `docs/cpp-subset.md` exists and is honest

**🧩 DSA (5.5h) —** 🔴 **bit manipulation** — LC 136, 191, 338, 190, 371, 268, 78. *Your varint encoder is bit manipulation; do this set the week you write it.*
**🏛 DESIGN (2.5h) —** design a key-value store.

> ❓ **GO FIND OUT** — 1. Why does Protobuf use varints, and what exactly does zigzag encoding solve? 2. What is the largest value a 5-byte varint can hold, and what should your parser do with a 6-byte one? 3. Find one real protocol that got version negotiation wrong. What broke?

## ⬛ WEEK 6 · 19–25 Oct

**📄 READ (3h)** — **Cloudflare, "A Primer on Proxies"** — `https://blog.cloudflare.com/a-primer-on-proxies/`. 🔴 *Forward, reverse, transparent, and the trust model of each. Required vocabulary before you write a design doc* · **Google, "Structure-aware fuzzing"** — `https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md`

**🛠 BUILD (17h)**
- [ ] 🚩 **`hardened`** — the flagship as a deliverable. Committed fuzzing corpus, the full sanitizer matrix, the documented subset
- [ ] 🔴 **Write up the memory bugs the fuzzer found in your own parser.** *This is the deliverable, not the clean run*
- [ ] **`docs/design/wire-protocol.md`** — the frame layout, the versioning scheme, the security properties of the handshake, and **what an unauthenticated peer can make you do**

**✅ BY SUNDAY — 🎯 MILESTONE D0**
- [ ] 🔴 **libFuzzer runs 1 hour clean on the frame parser, with the corpus committed**
- [ ] **Four attacks fail**, each with a test asserting the failure mode **and the counter it increments**
- [ ] **`kill -9` at random points, 500 cycles: no message lost, none duplicated, none torn**
- [ ] **The bug write-up is published** as part of the repo

**🧩 DSA (5.5h) —** stacks & monotonic stacks — LC 20, 155, 150, 22, 739, 853, 84.
**🏛 DESIGN (2.5h) —** design a notification system.

> ❓ **GO FIND OUT** — 1. Your fuzzer is clean for an hour. **What does that prove, and what does it not?** 2. What is a fuzzing *dictionary* and would one help your parser? 3. How does OSS-Fuzz decide a bug is a security bug?

## ⬛ WEEK 7 · 26 Oct – 1 Nov · 🔴 *Proxy Lab week*

> **The one CMU lab that belongs in a privacy-relay curriculum.** You write a **concurrent caching HTTP proxy**: parse the request, open a connection to the origin, forward, cache the response. 🔴 **Part III's writeup explicitly forbids one big lock — *"protecting accesses to the cache with one large exclusive lock is not an acceptable solution"*** — so you partition, or use readers-writers locks, or build it from semaphores. **A proxy, with concurrency, with a real synchronisation constraint, auto-graded, in a week.**

**🛠 BUILD (19h)**
- [ ] **CS:APP Proxy Lab**, all three parts — handout `http://csapp.cs.cmu.edu/3e/proxylab-handout.tar` · writeup `http://csapp.cs.cmu.edu/3e/proxylab.pdf`
- [ ] Run `./driver.sh`. **It is fully self-gradeable offline: BasicCorrectness 40, Concurrency 15, Cache 15**

**✅ BY SUNDAY** — **all 70 points**, no segfaults, no memory or fd leaks · a written paragraph: **which synchronisation strategy you chose for the cache and why**

**🧩 DSA (5.5h) —** linked lists — LC 206, 21, 143, 19, 138, 2, 141, 287, **146 LRU Cache**. 🔴 *You implemented a cache with an eviction policy this week. Do 146 and notice.*
**🏛 DESIGN (2.5h) —** design a distributed cache.

> ❓ **GO FIND OUT** — 1. Why must the proxy downgrade HTTP/1.1 to HTTP/1.0 when forwarding? What breaks if it doesn't? 2. Your cache approximates LRU. **What exactly does "approximates" buy you?** 3. What is the worst-case memory of your proxy, in terms of `MAX_CACHE_SIZE`, `MAX_OBJECT_SIZE` and thread count? Derive it.

## ⬛ WEEK 8 · 2–8 Nov

**📕 PAGES (3h)** — **OSTEP ch. 13–16, 18–19** (virtual memory, TLB). Ch. 19 is the one that matters
**📄 READ (2h)** — **Linux cgroups v2 kernel docs**, the `memory` and `cpu` controllers — `https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html`

**🛠 BUILD (17h)**
- [ ] The relay forwards. Two processes, framed authenticated messages, over a socket
- [ ] 🔴 **`docs/design/threat-model.md` v1** — the layers, what each assumes has already failed, and **an explicit section on what you do NOT defend against.** You will revise it in Weeks 25 and 50, and *the revisions are the interesting part*

**✅ BY SUNDAY** — **D0 fully signed off** · CV v0 skeleton exists (not for applying — so an unexpected opportunity does not find you writing one in a panic) · 📝 **Level checkpoint:** `make bootstrap` on a clean clone — **actually run it**

**🧩 DSA (5.5h) —** consolidation + the first **failure-category count** if you have 30 entries. **~72 problems cumulative.**
**🏛 DESIGN (2.5h) —** design a web crawler. 🔴 *You build one next week.*

> ❓ **GO FIND OUT** — 1. Your relay runs in a cgroup with `memory.max=512M`. **Name four things counting against that limit besides your heap.** 2. What is the difference between `memory.max` and `memory.high`, and which do you want? 3. Read one entry from `k8s.af` about conntrack. **How many concurrent connections before a default Linux box exhausts its conntrack table?**

---
---

# ⚡ LEVEL 2 — 🔴 THE PROBLEM, MEASURED
### W9–12 · 9 Nov – 6 Dec 2026 · 4 weeks · **Milestone D1** · 🚩 **Flagship #2 `linkage`** · **⚑ CV v1** · **W12 = REST WEEK**

> **Goal: make the premise of your own project into something you checked rather than something you read.**
>
> 🔴 **Why this level exists, and why it is never cut.** A privacy project built by someone who never measured the problem reads as *ideological*. A privacy project that opens with *"I crawled five thousand sites; here is the distribution"* reads as *engineering*. **That distinction is the whole difference in how a hiring manager receives this work** — and it lands in month three, not month seven.

> 🔥 **THE WALL — four measurements, each worse than the last.** **(1)** Open your own browser, go to a news site, count the third-party requests **by hand in devtools**. Write down how many distinct organisations received a request you did not ask for. **(2)** Do it across five sites you actually use and **intersect the sets.** The intersection is not empty. **(3)** Measure your own fingerprint entropy — canvas, WebGL, fonts, audio, screen, timezone, hardware concurrency. **How many bits are you carrying?** **(4)** 🔴 **Now your IP. Your fingerprint might be shared with a thousand people. Your IP is shared with your household. Combine them and the set size is one.** *That is the argument for the entire network layer, and it is why browser hardening alone is not an answer.*

## ⬛ WEEK 9 · 9–15 Nov · *the crawler*

**📄 READ (4h)**
- [ ] 🔴 **Englehardt & Narayanan, "Online Tracking: A 1-million-site Measurement and Analysis"** (CCS 2016) — the study you are doing a smaller, more current version of
- [ ] **The Tranco paper's motivation section** — `https://tranco-list.eu/`. 🔴 *Why it exists and what was wrong with Alexa top-1M for research. **Cite the list version and date; reproducibility is the point***
- [ ] **DuckDuckGo, "Tracker Radar"** — `https://spreadprivacy.com/duckduckgo-tracker-radar/`. The open dataset and crawler methodology behind the largest public tracker corpus
- [ ] **Brave, "Fighting CNAME trickery"** — `https://brave.com/privacy-updates/6-cname-trickery/`. 🔴 *Why domain-based blocklists fail, and a thing your own classifier must handle*

**🛠 BUILD (18h)**
- [ ] **`lab/linkage`** — decide **Playwright** (Chromium, fresh isolated profile per site) or **OpenWPM** (research-grade, citable provenance) and **write down why**
- [ ] Per site record: every **HTTP request** (URL, type, initiator) · every **cookie** (name, domain, expiry, `SameSite`) · every **localStorage/IndexedDB** write · every **script** · the response headers that matter
- [ ] **Store it in PostgreSQL**, schema in git *(and that is your 19.6% Postgres evidence, earned honestly)*
- [ ] 🔴 **Pin the Tranco list ID and publish it.** Every list has a permanent citable ID — **that single choice makes your study reproducible in a way most are not**
- [ ] 🔴 **Rate-limit yourself.** One request at a time per domain, a real user-agent **with a contact address in it**, respect `robots.txt`. **You are a guest.** Re-read the Safety Board principles from Week 3
- [ ] 🔴 **Spoof your headers, and then measure your own block rate by provider.** Gundelach et al. (2026) found **Cloudflare blocks 37% and Akamai 26% of headless crawls**, that **header-level signals alone cause 75%** of headless-specific blocking, and that **83% of published measurement papers never mention blocking at all.** *Fixing it is cheap. **Publishing your block rate by provider is a methodological contribution almost nobody makes***
- [ ] **Quick win on day one:** run **Blacklight Query** over a few hundred URLs while you build the real thing — `https://github.com/the-markup/blacklight-query`. **Zero code, nine concrete tests, a credible first result inside an afternoon**

**✅ BY SUNDAY** — the crawler completes **500 sites** unattended and is **resumable after a kill**

**🧩 DSA (5.5h) —** 🔴 **graphs: BFS, DFS, connected components** — LC 200, 133, 695, 417, 130, 994, 286. *You are about to build and analyse a real graph.*
**🏛 DESIGN (2.5h) —** design a web crawler — **and then compare your design to what you actually built.**

> ❓ **GO FIND OUT** — 1. What is the difference between a first-party cookie set by a third-party script and a third-party cookie, **and why does that distinction matter more every year?** 2. What is the state of third-party cookie policy in Chrome in 2026, and **what replaced the capability?** 3. What does `robots.txt` actually oblige you to do, legally and ethically? Are they the same?

## ⬛ WEEK 10 · 16–22 Nov · *the identifiers*

**📄 READ (3h)**
- [ ] **Eckersley, "How Unique Is Your Web Browser?"** (Panopticlick, PETS 2010) — the founding fingerprinting measurement
- [ ] 🔴 **Mozilla, "Introducing State Partitioning"** — `https://hacks.mozilla.org/2021/02/introducing-state-partitioning/`. **This is the list of every kind of state two of your compartments must not share.** You will implement against it in Level 4
- [ ] **Brave, "Preventing pool-party attacks"** — `https://brave.com/privacy-updates/13-pool-party-side-channels/`. 🔴 *Exhaustible socket and connection pools as covert cross-site channels — a side channel that defeats naive compartmentalisation*

**🛠 BUILD (18h)**
- [ ] Classify third-party domains against **EasyPrivacy** and **Disconnect**, and 🔴 **map domains to *organisations*** — many domains, one company, and this mapping is what makes the numbers honest
- [ ] **Find the identifiers.** A cookie value that is high-entropy, long-lived and *stable across the session*. Heuristics: length, entropy, expiry, **and whether it appears in a URL query string sent to another party**
- [ ] 🔴 **Resolve CNAMEs, and analyse first-party cookies too.** Böttger et al. (2026): **>54% of sites now deploy first-party or server-side tracking and filter lists are "largely inadequate" against it.** A crawler that only counts third-party requests is measuring a **shrinking slice of the problem** — see CookieGraph (CCS 2023) for the technique
- [ ] 🔴 **Hunt for cookie syncing** — the request where one tracker hands another its identifier so they can agree they are looking at the same person. **Finding one instance in your own data is the best screenshot in the whole study**
- [ ] Measure your own fingerprint entropy **in bits**

**✅ BY SUNDAY** — the crawl reaches **5,000 sites** · **at least one confirmed cookie-sync instance, documented with the actual request**

**🧩 DSA (5.5h) —** 🔴 **union-find** — LC 684, 547, **721 Accounts Merge**, 990. **🔴 LC 721 *is* the linkage problem: merging accounts that share an email is structurally identical to merging sessions that share a tracker identifier. Do it this week, then use it for real next week.**
**🏛 DESIGN (2.5h) —** design a distributed job queue.

> ❓ **GO FIND OUT** — 1. Your fingerprint has N bits of entropy. **How many bits are needed to uniquely identify one person among the world's internet users?** Compute it. 2. What is CNAME cloaking and why does it defeat your domain classifier? 3. Find one documented case of a data broker combining online and offline data. **What was the mechanism?**

## ⬛ WEEK 11 · 23–29 Nov · 🔴 *the graph — this is the level*

**🛠 BUILD (19h)**
- [ ] **The bipartite graph:** sites on one side, tracker organisations on the other, an edge if that tracker loaded on that site. Then the **projection**: trackers linked to trackers when they co-occur, weighted by how often
- [ ] **Answer these with actual numbers:**
  - **Degree distribution.** How many sites does the median tracker see? The 99th percentile?
  - 🔴 **THE HEADLINE: given a browsing session of N sites, what is the expected fraction a *single* tracker organisation can observe?** Plot it for N = 5, 10, 25, 50, **with a confidence interval**
  - **Largest connected component** when you link sessions sharing an identifier — *union-find, exactly as in LC 721*
  - **How many organisations must collude to reconstruct 90% of a typical session? 50%?**
  - 🔴 **Run the whole crawl again with uBlock Origin's default lists on, and report the delta.** *Nobody publishes this properly*

**✅ BY SUNDAY** — the graph is built, rendered, and **one figure carries the whole argument**

**🧩 DSA (5.5h) —** graphs part 2 — LC 207, 210, 261, 323, 127, **785 Is Graph Bipartite**, 886. *You built a bipartite graph this week.*
**🏛 DESIGN (2.5h) —** design a metrics pipeline.

> ❓ **GO FIND OUT** — 1. Your largest connected component covers X% of sessions. **What is the right null hypothesis to compare that against?** 2. Is your degree distribution power-law? **How would you actually test that** rather than eyeballing the log-log plot? (Find Clauset, Shalizi & Newman.) 3. What is the difference between measuring *capability* and measuring *actual data sharing*, and which did you do?

## ⬛ WEEK 12 · 30 Nov – 6 Dec · 🛌 **REST WEEK (10h)** · **🎯 MILESTONE D1** · **⚑ CV v1**

**🛠 (6h)**
- [ ] 🔴 **`docs/analysis/linkability-2026.md`** — the methodology in enough detail that someone else can rerun it (list version, date, browser version, blocklist versions, machine) · the graph · the headline number with its interval
- [ ] 🔴 **The limitations section, and it is not optional:** 5,000 sites is not the web · 🔴 **your number is a LOWER BOUND — Annamalai et al. (WWW 2025) measured that automated crawls miss ~45% of the fingerprinting sites real users hit, because of login walls, bot detection and untriggered scripts. Say this in the abstract and cite them** · your measured block rate by provider, stated · one vantage point in one country sees one ad market · your identifier heuristics have a false-positive rate **you estimated rather than ignored** · **and you measured *capability*, not actual data sharing between companies.** *It justifies "many parties can observe overlapping slices of a session and some exchange identifiers." It does not prove any named company assembled any named profile. Say so in the first paragraph*
- [ ] **Export the graph** in a form `adyton-demo` can render in Week 26
- [ ] 🚀 **BLOG POST 1: *"I crawled 5,000 sites to find out how linkable the web actually is. Here's the graph."*** Cross-post to HN, Lobsters, `r/privacy`
- [ ] **⚑ CV v1 written**

**📝 (4h)** — 🔴 **failure-category count** from `dsa/FAILURES.md` — the first one that will actually redirect you · level checkpoint · **🤝 the referral pipeline opens next week: draft your three opening messages now, using the study as the hook**

> ❓ **THE QUESTION FOR THE REST WEEK**
> You now have a measured number for how linkable the web is. **Go and find what Apple, Google, Mozilla and Brave each claim their defences achieve — and check whether any of them publishes a comparable measurement.** Write one paragraph on what you found. *That paragraph is the opening of your project's README.*
---
---

# ⚡ LEVEL 3 — ONION ROUTING & SPHINX
### W13–18 · 7 Dec 2026 – 17 Jan 2027 · 6 weeks · **Milestone D2** · 🚩 **Flagship #3 `sphinx`** · 📺 **Boneh Crypto I** · **W18 = BUFFER** · **🤝 referrals open W13**

> **Goal:** constant-size onion packets whose serialised length is **byte-identical regardless of how many hops remain** — because a packet that shrinks as it travels tells every relay exactly where in the circuit it is.

## ⬛ WEEK 13 · 7–13 Dec · 🤝 *the referral pipeline opens*

> 🔥 **THE WALL.** Build the obvious onion: encrypt the payload for hop 3, wrap for hop 2, wrap for hop 1. Send it. **Now measure the packet at each hop.** It gets smaller. **The first relay knows it is first, the last knows it is last, and an observer counting bytes learns the position of every packet on the wire without breaking any crypto at all.**

**📺 LECTURES (4h)** — **Boneh Crypto I, Week 1** (stream ciphers, PRGs, semantic security, the one-time pad) — `https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/` 🔴 *use the Stanford page, not Coursera — free, no account*
**📄 READ (3h)**
- [ ] 🔴 **Chaum, "Untraceable Electronic Mail…"** (1981) — **seven pages, and the origin of the whole field.** One-page note
- [ ] 🔴 **Das, Meiser, Mohammadi, Kate, "Anonymity Trilemma"** (IEEE S&P 2018) — `https://eprint.iacr.org/2017/954`. **Every subsequent decision in this project descends from this paper.** Read it properly and write the note
- [ ] **Dingledine, Mathewson, Syverson, "Tor: The Second-Generation Onion Router"** (2004)

**🛠 BUILD (16h)** — `adyton-core/crypto`: X25519, ChaCha20-Poly1305 AEAD, HKDF via **libsodium**; **zeroizing secret types** (`sodium_memzero`, and find out why a plain `memset` gets optimised away)
**✅** — the wall reproduced and the shrinking measured · secret material never touches a log, **enforced by a CI grep**
**🧩 DSA —** trees & BSTs: LC 226, 104, 543, 110, 100, 572, 235, 102, 199, 98, 230. **🏛** design a distributed lock service.
**📝 Track J —** 🔴 **write to three people in the Egyptian engineering diaspora. The hook is your Week-12 study, not "I'm learning distributed systems."** Ask one specific technical question. No other ask.

> ❓ 1. The trilemma says pick two of three. **Which two does Tor pick, which two does Nym pick, and which two do you?** 2. Why is `sodium_memzero` necessary when `memset` exists? 3. What is the difference between semantic security and indistinguishability under chosen-plaintext attack?

## ⬛ WEEK 14 · 14–20 Dec
**📺** Boneh **Week 2** (block ciphers, AES, PRPs/PRFs, modes, CTR) — 🔴 *your onion layers are CTR-shaped*
**📄** 🔴 **Danezis & Goldberg, "Sphinx"** (IEEE S&P 2009) — `https://cypherpunks.ca/~iang/pubs/Sphinx_Oakland09.pdf`. **§3 and §4 carefully.** 🔴 **Before you write code, answer in one paragraph: why is the header size independent of hops remaining?**
**🛠 (16h)** — the Sphinx header: the group element, the routing information, the per-hop MAC. Start with the *structure*, not the crypto
**✅** — you can draw the packet layout from memory
**🧩 DSA —** heaps & top-K: LC 703, 1046, 973, 215, 621, **295 Find Median from Data Stream**. **🏛** design a sharded database.

> ❓ 1. Sphinx uses a **single** group element for the whole header regardless of hop count. **How?** 2. What is LIONESS and why does Lightning's BOLT #4 use ChaCha20 instead? 3. What stops a relay from replaying a Sphinx packet?

## ⬛ WEEK 15 · 21–27 Dec
**📺** Boneh **Week 3** (MACs, CBC-MAC, HMAC, collision resistance, 🔴 **timing attacks on MAC verification** — not optional for you)
**📄** 🔴🔴 **Scherer, Weis, Strufe, "Provable Security for … Sphinx"** (PoPETs 2024) — `https://arxiv.org/abs/2312.08028`. **This repairs Sphinx's broken proof, shows DDH is insufficient (you need Gap-DH), and documents a payload malleability issue.** *No other roadmap you have mentions this. Implementing Sphinx in 2027 without it is implementing a 2009 understanding of it*
**🛠 (16h)** — `adyton-core/sphinx`: single-pass construction, per-hop key derivation, the MAC chain
**✅** — a 2-hop packet is constructed and processed end to end
**🧩 DSA —** tries: LC 208, 211, 212. **🏛** design a system with end-to-end encryption.

> ❓ 1. What exactly was wrong with the original Sphinx proof, in two sentences? 2. **Does the payload malleability issue affect your design?** Justify either answer. 3. Compare Sphinx's header to BOLT #4's. Name three deltas and why Lightning made each.

## ⬛ WEEK 16 · 28 Dec – 3 Jan
**📺** Boneh **Week 4** 🔴 **the most important week** — authenticated encryption, chosen-ciphertext attacks, **CBC padding attacks**, key derivation, **case study: TLS 1.2**
**🛠 (16h)** — 🔴 **RapidCheck property test: serialised packet size is byte-identical for 1, 2, 3 and 4 hops remaining, across 10,000 generated packets** · libFuzzer on the Sphinx parser with its own corpus
**✅** — **the size invariant is asserted, not assumed** · the Sphinx parser fuzzes clean for an hour
**🧩 DSA —** hashing deep-dive + consolidation. **🏛** design an identity/auth system.
**📚 Cryptopals set 1** — `https://cryptopals.com/`

> ❓ 1. You have a size invariant. **Name two other invariants of your packet format that a property test could assert**, and write them. 2. What is a padding oracle and could your relay be one? 3. Why does the order of encrypt and MAC matter?

## ⬛ WEEK 17 · 4–10 Jan
**📺** Boneh **Week 5** (key exchange, Merkle puzzles, **Diffie–Hellman**, number theory)
**📄** **BOLT #4** — `https://github.com/lightning/bolts/blob/master/04-onion-routing.md`. 🔴 *The most widely deployed Sphinx derivative on Earth, with its deltas written down*
**🛠 (16h)** — `adyton-node` forwards a Sphinx packet across two hops, for real, over the wire from Level 1 · **`docs/design/packet-format.md`**
**✅** — a packet traverses two relays and the payload arrives intact
**🧩 DSA —** 🔴 **Cryptopals set 2** counts as this week's problem practice. **🏛** design a certificate/PKI system.

> ❓ 1. What does your relay learn about a packet it forwards? **Enumerate it exhaustively — that list is a section of your threat model.** 2. Why two hops and not three? What does the third buy, and what does it cost? 3. What is the *forward secrecy* property of your circuit, and what breaks it?

## ⬛ WEEK 18 · 11–17 Jan · 🔧 **BUFFER** · **🎯 MILESTONE D2**
**✅** — 🔴 **D2: Sphinx constant-size onion packets. 2-hop packet processed; serialised size byte-identical regardless of hops remaining, RapidCheck-asserted** · Boneh weeks 1–5 complete · Cryptopals sets 1–2 done
**Also:** **check `cs144.github.io`** — you need it in nine weeks. If it is still down, **plan the Wayback + mirror route now**
**🧩 DSA —** **failure-category count.** **🏛** ~175 problems cumulative.

> ❓ **THE BUFFER-WEEK QUESTION.** Read Tor's `tor-spec` on relay cells. **Write one page comparing Tor's cell format to your Sphinx packet: what does each optimise for, and what did Tor give up by not using Sphinx?** *(Tor predates Sphinx. That is part of the answer.)*

---
---

# ⚡ LEVEL 4 — ★ COMPARTMENTS
### W19–26 · 18 Jan – 14 Mar 2027 · 8 weeks · **Milestone D3 ★** · 🚩 **Flagship #4 `leakproof`** · ★ **THE DEMO** · 🌙 **Ramadan W22–26 at 20h** · **W26 = REST**

> ★ **Goal: the first thing that is real.** At the end of this level you can sit someone down and show them **two browsers on one laptop that the internet cannot connect to each other.** Everything before was necessary. This is the first thing a person can *see*.
>
> 🌙 **Ramadan 1448 ≈ 8 Feb – 9 Mar = weeks 22–26, at 20h.** **This collision is deliberate and it is good luck.** The heavy netns work lands in W19–21 at full load; **W22–26 is the leak suite, which is many small independent tests — exactly the right shape of work for a reduced month.**

## ⬛ WEEK 19 · 18–24 Jan
> 🔥 **THE WALL — five failures, and three of them are not the proxy's fault.** Point a normal browser at a SOCKS proxy on your relay. Congratulations, you have a VPN. Now watch it betray you: **(1) WebRTC** hands out your real local and public IP as ICE candidates, **around the proxy entirely.** **(2) IPv6** — host is dual-stack, tunnel is v4, browser prefers v6 and **goes direct.** `tcpdump` it. **(3) DNS** still goes to your ISP — **every destination logged by name before a single proxied byte moves.** **(4)** Kill the relay mid-download: the browser **retries without the proxy.** **(5)** 🔴 **The one that is the actual product: run two profiles through the same proxy and check whether a site can tell they are the same person. Cookies, `localStorage`, TLS session tickets, HTTP/2 connection coalescing, one shared exit IP. They can.**
> **Screenshot all five.** *Three of the first four are the application declining to use the proxy — which is the entire argument for enforcing the boundary in the kernel rather than asking the application nicely.*

**📺** **CS161 — *Introduction to the Web*, *Same-Origin Policy*, *Cookies and Session Management***
**📄** **Mozilla, "Firefox 85 cracks down on supercookies"** — 🔴 *network-state partitioning: HTTP cache, **connection pools**, DNS cache, HSTS. Connection pools and TLS session tickets are the two your suite must test* · **Mullvad Browser docs** — its own statement that **it does not hide your IP**
**🛠 (19h)** — reproduce all five failures. **This week is diagnosis, not construction**
**🧩 DSA —** 🔴 **dynamic programming part 1** — 1-D. LC 70, 198, 213, 91, 139, 322, 518, 300. 🔴 **The method, every time, no exceptions: state the subproblem in words → write the recurrence in a comment → base cases → *then* choose memo or table → optimise space last. Do not write code before the recurrence exists in a comment.** **🏛** design a multi-tenant API with quotas.

> ❓ 1. Which of the five failures would a *commercial VPN client* also have? **Go and test one.** 2. What is HTTP/2 connection coalescing and why does it link two profiles sharing an exit? 3. What is a TLS session ticket and how long does it live?

## ⬛ WEEK 20 · 25–31 Jan
**📺** **MIT 6.1810 lecture notes** on page tables, traps and namespaces — `https://pdos.csail.mit.edu/6.1810/2025/` *(notes only; you are not doing xv6's labs)*
**📕** **Kerrisk, *TLPI* ch. 28** (namespaces) or `namespaces(7)` · the **nftables** wiki, "Quick reference" and "Chains"
**🛠 (19h)** — `adytond` + `adyton-edge/launch`: **Linux network namespaces** as the boundary — own interfaces, own routing table, own resolver. **veth pair** to the tunnel. 🔴 **nftables default-drop, so the kill switch is structural: if the tunnel dies there is no rule permitting anything**
**✅** — a process inside the namespace **cannot route around it, because there is no other route**
**🧩 DSA —** DP 2-D: LC 1143, **72 Edit Distance**, 62, 64, 221, 5, 647. **🏛** design a VPN/tunnelling service.

> ❓ 1. 🔴 **A kill switch as "detect and react" is a race. As default-drop it is an invariant. Give the exact race in the first design.** 2. What happens to an **already-open socket** when its namespace's default route is removed? **Verify it, don't guess.** 3. How do Mullvad's and Tailscale's Linux kill switches actually work?

## ⬛ WEEK 21 · 1–7 Feb
**🛠 (19h)** — one unmodified **Mullvad Browser** profile per identity, each in its own netns on its own 2-hop circuit with its own pinned exit · `adyton identity launch shopping` as **one command** · ⚙️ 🔴 **make `Identity` a type whose constructor takes circuit + exit + profile-dir + namespace and has no setters — so a mismatched identity is not a bug you can write**
**✅** — ★ **an unmodified Mullvad Browser runs in a netns over a 2-hop circuit and you browse the real web through it**
**🧩 DSA —** DP knapsack: LC 416, 494, 474, 1049 + **AtCoder Educational DP A–F** — `https://atcoder.jp/contests/dp`. **🏛** design a browser-isolation product.

> ❓ 1. 🔴 **Why is a network namespace a stronger boundary than a browser container?** Be specific about what each isolates and what each shares. 2. Why must you **not** modify Mullvad Browser? What does each modification cost, and *to whom*? 3. What is in `docs/browser-delta.md`, and **can you justify every line?**

## ⬛ WEEK 22 · 8–14 Feb · 🌙 **RAMADAN BEGINS (20h from next week; this week still 32h)**
**📄** **MIT 6.858 lecture 4** (buffer overflow defences) and **lecture 12** (web security model) — cheap to pull forward, and useful here
**🛠 (19h)** — the leak suite skeleton in CI. **Get the harness working at full load this week, because the tests themselves are the reduced-hours work**
**🧩 DSA —** greedy + intervals: LC 53, 55, 45, 134, 846, 56, 57, 435, 253. **🏛** design a quota and fair-share system.

> ❓ 1. What is the **smallest** observable difference between two of your compartments that would let a tracker link them? **Rank your five leak vectors by how hard each is to exploit.**

## ⬛ WEEKS 23–26 · 15 Feb – 14 Mar · 🌙 **RAMADAN — 20h/week** *(11 Depth / 5 Interview / 2 Fundamentals / 2 Craft)*

> **The interview track drops to 5h. It does not stop.** 🔴 **No new DSA topics for four weeks. Re-solve every DP failure from the log, and work AtCoder DP A–L slowly.** *DP is the one topic that rewards slow careful weeks, so this collision is better luck than it looks.*

**🛠 THE LEAK SUITE — `leakproof`, one test family per week (11h/wk)**
- **W23 — WebRTC and IPv6.** Zero ICE candidates carrying a non-namespace address. No IPv6 packet attributable to the identity leaves the host
- **W24 — DNS and the kill switch.** Zero DNS queries on the host uplink during a browse session. 🔴 **Daemon killed mid-transfer: zero subsequent packets, 20 runs, 20 passes**
- **W25 — cross-compartment.** Two identities share **no exit IP, no cookie, no DNS query, no TLS session ticket** — and produce **identical CreepJS output.** 🔴 **Add the pool-party side channel from Brave's research to the suite**
- **W26 (Eid, rest) — `docs/design/threat-model.md` v2**, and the write-up

**📄 across the four weeks** — **Tor Browser design document**, *"Cross-Origin Identifier Unlinkability"* and *"Fingerprinting"* — 🔴 *the most thorough public treatment of browser linkability there is* · **Brave, "Fingerprint randomization"** and 🔴 **"Brave simplifies its fingerprinting protections"** — *a published **negative result**: their strict mode made users **more** identifiable. The best single article on intellectual honesty in this field, and the model for your own write-ups*

## ⬛ WEEK 26 · 8–14 Mar · 🛌 **REST + EID** · **🎯 MILESTONE D3 ★** · ★ **THE DEMO** · **⚑ CV v2**

**✅ D3 — the exit criteria**
- [ ] ★ Unmodified Mullvad Browser, netns, 2-hop circuit, browsing the real web
- [ ] 🔴 **`leakproof` green in CI across all five families — and a red build blocks merge.** *Its going red is the alarm*
- [ ] **Identical CreepJS output across two machines.** Any difference is a bug in your launcher
- [ ] Ephemeral identities wiped on close, verified · named identities with **exits pinned stably across restarts**
- [ ] 🔴 **`docs/browser-delta.md` — and if it is longer than "profile directory path and SOCKS endpoint," justify every entry or remove it**

**★ THE DEMO (built this week, finalised W52)**
- [ ] **Screen one — you are assembled.** IP, ISP, city, fingerprint, and the hash. Click through five demo sites; **a graph draws itself live, connecting every visit — using your own Week-11 co-occurrence data**
- [ ] **Screen two — you are not.** The same walk through two compartments. **The graph fails to connect.** Side by side, sixty seconds apart
- [ ] **Screen three — and it isn't slow.** Page-load and TTFB: direct vs Adyton vs Tor, measured live on their connection
- [ ] 🔴 **The scale statement printed on the page**, not buried in the README. Rate-limited, quota per IP, **and it says it is a demonstration, not a proxy**
- [ ] **Tested on a non-engineer.** If they do not understand it in ten seconds, it is not finished

**🚀 BLOG POST 2: *"Your proxy leaks four ways and three of them aren't the proxy's fault."*** · **⚑ CV v2** · **failure-category count**

> ❓ **THE REST-WEEK QUESTION.** Your demo shows two compartments that do not link. **Now try to break it yourself for one hour, as an attacker with JavaScript on both sites.** Write down everything you tried. *That list is the next version of the leak suite, and "I attacked my own product and here is what I found" is the best answer you can give in an interview.*
---
---

# ⚡ LEVEL 5 — TRANSPORT: QUIC & FINGERPRINTS
### W27–32 · 15 Mar – 25 Apr 2027 · 6 weeks · **Milestone D4** · 🚩 **Flagship #5 `minnow`** · 📺 **CS144, checkpoints 0–6** · **W32 = BUFFER**

> **Goal:** stop *using* the network and start understanding it — by implementing TCP, then using what you learn to justify every transport decision you make afterwards. **The artifact is unfakeable: a TCP that passes Stanford's test suite.**

> 🚨 **Before Week 27: confirm the CS144 repo is back.** If it is not, use the Wayback handouts and a live mirror (§IV.1) and **say so in your README** — *"built against the Fall 2025 handouts"* is a fine sentence.

| Wk | Dates | 📺 Course | 🛠 Build | 🧩 DSA | ❓ Go find out |
|---|---|---|---|---|---|
| **27** | 15–21 Mar | **CS144 ckpt 0** — telnet and SMTP by hand, `webget`, `ByteStream` | Set up the toolchain; the harness that will run your TCP and the kernel's side by side | 🔴 **Intervals — LC 56, 57, 435, 253, 763.** *Do these the week before you write the reassembler* | What does `webget` teach you that `curl` hides? |
| **28** | 22–28 Mar | 🔴 **CS144 ckpt 1 — the `Reassembler`** | The reassembler. **This IS an interval-merge problem and you did the set last week** | Queues & deques: LC 239, 622, 933 | Why is the capacity limit part of the reassembler's *interface* and not an implementation detail? |
| **29** | 29 Mar – 4 Apr | **CS144 ckpt 2** — `Wrap32`, `TCPReceiver` | Sequence-number wraparound, the window | DP part 2: LC 309, 494, 97, 329 | 32-bit seqnos wrap. **At 10 Gbps, how long until wraparound?** Compute it |
| **30** | 5–11 Apr | 🔴 **CS144 ckpt 3 — `TCPSender` + the retransmission timer.** This is **RFC 6298** implemented | Talk to real Linux TCP. The "one megabyte challenge" | Graphs: shortest paths — LC 743, 787, 1631, 778 | Your RTT estimator oscillates on a jittery link. **What does RFC 6298 do about it, and why those constants?** |
| **31** | 12–18 Apr | **CS144 ckpt 4** (the report — ≥3 Internet paths, ≥1 hour of `ping -D -n -i 0.2`) **+ ckpts 5–6** (ARP, the router) | 🔴 **Feed ckpt 4's real measurements straight into `lab/bench`'s `tc netem` profiles.** Your network conditions are now *yours*, not invented | MST & bridges: LC 1584, **1489 Critical Connections** | **LC 1489 is Tarjan's bridge-finding. Which relay's removal partitions your mesh?** You answer this for real in Level 6 |
| **32** | 19–25 Apr | 🔧 **BUFFER** | QUIC via **ngtcp2**; `adyton-core/transport`; **ADR-0002** | Consolidation; failure-category count | — |

**📄 THE READING, across the level**
- [ ] 🔴 **Robin Marx, "Head-of-Line Blocking in QUIC and HTTP/3: The Details"** — `https://calendar.perfplanet.com/2020/head-of-line-blocking-in-quic-and-http-3-the-details/`. **The definitive explainer — and it argues the fix is *oversold*, which is exactly the scepticism you want before building the chart yourself**
- [ ] **RFC 9000 §2, 5, 12–13, 17** · **RFC 9001** (🔴 *header protection is why your handshakes can be made byte-identical except the random bits*) · **RFC 9002**
- [ ] 🔴 **Read these two on the same day and hold both:** **Langley et al., "The QUIC Transport Protocol"** (SIGCOMM '17 — 15–18% YouTube rebuffer reduction at 35% of Google egress) and **"QUIC is not Quick Enough over Fast Internet"** (WWW '24 — **up to 45.2% *lower* throughput than TCP+TLS+H2 on fast links**, root-caused to receiver-side processing and userspace ACKs) — `https://arxiv.org/abs/2310.09423`
- [ ] 🔴 **Cloudflare, "Unlocking QUIC's proxying potential with MASQUE"** — `https://blog.cloudflare.com/unlocking-quic-proxying-potential/`. **Read in W28 and write an ADR: CONNECT-UDP is the standardised way to do exactly what you are doing, it is what Cloudflare replaced WireGuard with in WARP, and HTTP/3-shaped traffic survives middleboxes that eat custom UDP. Adopt it or justify why not**
- [ ] **Cloudflare, "Accelerating UDP packet transmission for QUIC"** and **Tailscale, "Enhance UDP Throughput for QUIC and HTTP/3 on Linux"** — 🔴 *GSO and `sendmmsg` batching: the difference between a toy QUIC relay and one that saturates a NIC*
- [ ] **`qvis`** — `https://qvis.quictools.info/`. 🔴 *Point it at your own qlog traces and **see** the congestion window and the multiplexing*

**✅ MILESTONE D4 — by Week 32**
- [ ] 🔴 **CS144 checkpoints 0–6 pass the provided test suite.** Screenshot in the README
- [ ] Your TCP **interoperates with the kernel's** — your client talks to a real `nc` server and back
- [ ] **The comparison:** yours vs the kernel's, six `tc netem` profiles, throughput + p99 + retransmission count, **with an honest analysis of every place yours is worse**
- [ ] 🔴 **THE HEAD-OF-LINE-BLOCKING CHART** — ten logical circuits over one TCP connection vs ten connections vs QUIC streams, under 5% loss. **This chart justifies ADR-0002 and you will show it in interviews**
- [ ] **Per-hop QUIC transport works**, and 🔴 **two peers' handshakes are byte-identical except the random bits** — *because a distinctive handshake is a fingerprint, and a fingerprint defeats the entire product*
- [ ] **ADR-0002** written, argued from your own graphs
- [ ] 🚀 **BLOG POST 3: *"I implemented TCP so I'd stop guessing about head-of-line blocking. Here's the graph."***

---
---

# ⚡ LEVEL 6 — THE MESH: NAT & GOSSIP
### W33–37 · 26 Apr – 30 May 2027 · 5 weeks · **Milestone D5** · 🚩 **Flagship #6 `meshsim`** · 🌙 **Eid al-Adha W36 (26h)** · **W37 = REST**

> **Goal:** twenty to forty relays that find each other, survive churn, and tell you the truth about how often two machines behind home routers can actually talk directly.

> 🔥 **THE WALL.** Run a relay on your workstation in Cairo and another on a different network. Give each the other's IP. **They cannot connect, in either direction.** Both are behind NAT; neither has a routable address. **This is the physical reason peer-to-peer software needs traversal infrastructure, and it is invisible until you hit it.** Then do it again with the Oracle box as a rendezvous and watch hole punching work — **then find the NAT type where it still does not**, and fall back to relaying.
> ```bash
> # ask TWO different rendezvous servers for your external ip:port.
> # If they disagree, you are behind symmetric NAT and punching will not work.
> ```

| Wk | 📄 Read | 🛠 Build | 🧩 DSA |
|---|---|---|---|
| **33** | 🔴 **Tailscale, "How NAT traversal works"** — `https://tailscale.com/blog/how-nat-traversal-works`. *The best practical write-up in existence: every NAT class, birthday-paradox port prediction, honest failure statistics. **Read this before any RFC.*** · **RFC 4787 §4** (the NAT taxonomy) | `adyton-edge/nat` with **`pion/ice`**. Hole punching, relay fallback | Backtracking: LC 78, 90, 39, 40, 46, 79, 131, 51 |
| **34** | **Ford, Srisuresh & Kegel** (USENIX ATC '05, the original) · **RFC 8445 §2** · 🔴 **"Hole punching in the wild"** (FOSDEM 2023) — **6.25M results, ~70% success, and equal for TCP and QUIC**, overturning the folk belief that UDP is easier. *This is the published number your own result gets compared against* | 🔴 **`natlab` — the reachability table: hole-punch success by NAT-type pair, across every network you can borrow** — home, mobile tether, café, cloud | Graphs: articulation points, SCC. 🔴 **Run Tarjan on your own 30-node gossip topology and report which relays are articulation points** |
| **35** | **Das, Gupta, Motivala, "SWIM"** (DSN 2002) — short and unusually clear · **Hayashibara et al., "φ Accrual Failure Detector"** (SRDS 2004) · **HashiCorp's Lifeguard docs** — *a production system's honest account of where the paper needed fixing* | `adyton-edge/gossip`: SWIM membership, phi-accrual detection | Probability & expectation: LC 837, 808, 688 |
| **36** 🌙 | *Eid al-Adha — 26h.* **Marc Brooker, "Simple Simulations for System Builders"** — `https://brooker.co.za/blog/2022/04/11/simulation.html` | 🚩 **`meshsim`** — deterministic simulation: seeded clock **that can run backwards**, network with **asymmetric partitions**, disk faults, 🔴 **and a relay that *lies*** | Reservoir sampling, Bloom filters, HyperLogLog |
| **37** 🛌 | **REST WEEK.** 🎯 **D5** | Write-up, blog post, failure-category count | — |

**✅ MILESTONE D5**
- [ ] **20–40 relays discover each other; discovery converges within a bounded number of gossip rounds, measured and plotted against mesh size, next to the naive O(N²) curve**
- [ ] 🔴 **p50 circuit recovery <800 ms, p99 <3 s, under 20% churn**
- [ ] 🔴 **THE REACHABILITY TABLE published** — hole-punch success rate by NAT-type pair, **with N stated honestly because it is small**, plus the relay-fallback fraction and what it costs in latency and bandwidth. *Nobody publishes this for a privacy relay*
- [ ] **Phi-accrual vs fixed timeout: false-positive rate and detection latency, both, as a chart**, under injected jitter
- [ ] 🔴 **The asymmetric-partition test:** A reaches B, B does not reach A. **The mesh converges to a consistent view, or you document exactly why it cannot**
- [ ] **`meshsim` runs 10,000 seeds nightly.** 🔴 **≥3 real bugs found, each reproducible from a seed integer.** *A harness that finds nothing means your fault injection is too gentle — go and make it worse*
- [ ] 🚀 **BLOG POST 4: *"What fraction of real NAT pairs can actually hole-punch?"***

> ❓ 1. **Which NAT type defeats hole punching, and what does the fallback cost you** — in latency, in bandwidth, and in what the relay operator can see? 2. Why is SWIM O(N) per node when naive membership is O(N²)? **What does indirect probing buy you specifically?** 3. 🔴 **A relay that lies is a different fault class from a relay that crashes. Name three things a lying relay can do that your simulator should model — and one thing it can do that you cannot detect at all.**

---
---

# ⚡ LEVEL 7 — ☕ THE DIRECTORY: RAFT & TELEMETRY
### W38–44 · 31 May – 18 Jul 2027 · 7 weeks · **Milestone D6** · 🚩 **Flagship #7 `raft-dir`** · 📺 **MIT 6.5840 Labs 1–3** · **W44 = BUFFER + Final Gauntlet**

> ☕ **The Java level, and Java is 53.3% of your target backend postings — the single most-demanded skill in your corpus and the largest measured gap in your profile.** It is not here as a keyword: the directory is stateful, consensus-backed, and genuinely the right place for a managed language.
>
> 🔴 **Why a directory needs consensus at all:** every client must see **the same** list of relays. If two clients see different lists, **their circuit choices differ in an observable way — and disagreement is a fingerprint.** That sentence is the whole justification, and it is a better one than "distributed systems are cool."

| Wk | 📺 Course | 🛠 Build | 🧩 DSA |
|---|---|---|---|
| **38** | 6.5840 **lectures 1–3** + **Lab 1 (MapReduce)**. 🔴 **Read the extended Raft paper and Gjengset's "Students' Guide" BEFORE you start, not when stuck** | Java 21 ramp: records, sealed interfaces, **virtual threads**, `async-profiler` | 🔴 **W38 is a *proving* week: three written reductions from Skiena ch. 9.** Not code — prose proofs |
| **39** | 6.5840 **Lab 2** — KV server, **the lock**, dropped messages. *Versioned put, at-most-once, linearizable — exactly the semantics your directory needs* | `adyton-directory` skeleton | Topological sort: LC 207, 210, 269, 310. 🔴 *The epoch hash chain is a DAG* |
| **40** | 6.5840 **Lab 3A/3B** — elections, log replication | Raft integrated | Segment trees — **Codeforces EDU, Segment Tree parts 1–2** |
| **41** | 6.5840 **Lab 3C** — persistence, 🔴 **Figure 8** | Epoch documents, hash chaining | Fenwick / range queries: LC 307, 315, 493 |
| **42** | 6.5840 **Lab 3D** — snapshots, `TestFigure8Unreliable` | 🔴 **`adyton-aggregate`: relays → Kafka → aggregator → Postgres, with DP noise applied before publication** | Strings — **Codeforces EDU, String Algorithms**. *The one area Adyton gives you nothing for* |
| **43** | — | Peer admission; **the DP budget that fails closed**; `docs/design/consensus.md` | Company-tagged sets, timed |
| **44** | 🔧 **BUFFER** + 🔴 **THE FINAL GAUNTLET** (§IX.2) + **Full timed loop #1** | D6 sign-off | Failure-category count |

**📄 THE READING**
- [ ] 🔴 **Raft, the EXTENDED paper** — `https://raft.github.io/raft.pdf`. §5 in full, §6 carefully
- [ ] 🔴 **Gjengset, "Students' Guide to Raft"** — `https://thesquareplanet.com/blog/students-guide-to-raft/`. **Read it *while* implementing**
- [ ] 🔴 **The membership-change bug thread** — `https://groups.google.com/g/raft-dev/c/t4xj6dJTP6E`. *Ongaro announcing a safety bug in his own thesis's protocol, with the fix. The best document on Raft's subtle failure modes, and a lesson in intellectual honesty*
- [ ] 🔴 **Antithesis, "Finding bugs in Raft implementations"** — `https://antithesis.com/blog/2026/finding-bugs-in-raft-implementations/`. **State-machine-safety violations found in HashiCorp Raft, Aeron Cluster, OpenRaft and MicroRaft — and it enumerates four assumptions the Raft paper leaves implicit.** *Read it before you trust your own*
- [ ] 🔴 **Cloudflare, "Introducing Quicksilver"** — `https://blog.cloudflare.com/introducing-quicksilver-configuration-distribution-at-internet-scale/`. **The "why we did NOT use Raft" counterpoint: globally replicated KV with async replication and a monotonic log. Read it, then defend your choice in ADR-0006 against it**
- [ ] **Tailscale, "Tailnet lock"** — 🔴 *an Ed25519 signing chain so a **compromised coordination server cannot inject nodes.** That is the attack on your own directory, with its published mitigation*
- [ ] **AWS Builders' Library, "Leader election in distributed systems"** — leases, fencing tokens, real production failure modes. **Read before implementing**
- [ ] **SUNDR** (OSDI 2004) — 🔴 **fork consistency.** *A directory that shows two clients different histories is exactly a fork attack, and this is the paper that names it*
- [ ] **Tor's `dir-spec`** — `https://spec.torproject.org/dir-spec/index.html`. *What you are rebuilding, and what a production consensus document actually contains*

**✅ MILESTONE D6**
- [ ] 🔴 **6.5840 Labs 1, 2 and 3 pass MIT's test suites, including `TestFigure8Unreliable`.** Screenshot
- [ ] Leader elected from 5 nodes; **no split-brain across 1,000 randomised runs** · **minority partition cannot commit, 500 randomised partition schedules**
- [ ] 🔴 **The Figure 8 scenario built as a deliberate test** — and **you can draw it at a whiteboard in under five minutes from memory, tested by a human in W40**
- [ ] 🔴 **D6: 100% of peers hold the same epoch-N consensus hash within 30 s of close, under 20% churn** — *because disagreement is a fingerprint*
- [ ] **Fencing tokens:** a relay whose lease expired **cannot** publish. *Demonstrate the violation without them and the fix with them, same seed*
- [ ] **Kafka → aggregator → Postgres telemetry**, with **DP noise before publication and a budget that fails closed**
- [ ] **ADR-0006** (Raft vs Quicksilver-style async replication) · **`docs/design/consensus.md`** — what is linearizable, what is eventual, what a client is actually promised
- [ ] 🚀 **BLOG POST 5: *"Where I put consensus in a relay network, and why not everywhere."***

---
---

# ⚡ LEVEL 8 — 🎯 OPERATIONS & THE SHELL
### W45–48 · 19 Jul – 15 Aug 2027 · 4 weeks · **Milestone D7** · 🚩 **Flagship #8 `incident-lab`** · **⚑ CV v4** · 🎯 **APPLICATIONS OPEN W45** · **W48 = REST**

> 🔴 **This level is what the screen reads.** AWS 48.9% · Kubernetes 30.4% · observability 22.0% · on-call 21.5%. **It is never cut and never deferred.** Everything before this is what you talk about for forty-five minutes; this is what gets you into the room.
>
> **The split changes from W45: 12h Depth / 12h Interview / 8h Career.** Applications are live; interview readiness is now the binding constraint.

| Wk | 🛠 Build | Career |
|---|---|---|
| **45** | k8s: the mesh on k3s. Multi-region relays on free tiers. **Terraform: `apply` from zero, `destroy` to nothing** | 🎯 **CV v4 · first 16 applications** — Cloudflare, Tailscale, Apple, Mullvad, Proton first. **Referral activation to the 24+ people you have known since December** |
| **46** | Prometheus + Grafana. 🔴 **`docs/design/trustless-observability.md` — you cannot log per user, so which metrics are *facts* and which are relay *claims*?** The 3am dashboard | 16 applications · **Loop #2** |
| **47** | 🚩 **`incident-lab`**: 20+ self-inflicted incidents + 6 famous outages reproduced · 🔴 **the F12 harness audit — if it had coordinated omission, re-run every benchmark and put the before/after in `bench/RESULTS.md`** | 16 applications · **Loop #3** |
| **48** 🛌 | **REST.** `gatekeep` (mTLS, tested cert-expiry alerting), `costwatch` (**a billing alarm tested by triggering it**) | Pipeline review · failure-category count |

**📄 THE READING** — **AWS Builders' Library**, all of: *Using load shedding to avoid overload* · *Timeouts, retries and backoff with jitter* · *Avoiding insurmountable queue backlogs* · **Static stability using Availability Zones** (🔴 *keep working on stale state when the control plane is unreachable — arguably the most important article for a relay network*) · *Implementing health checks* (🔴 *and how a deep check takes down a whole fleet at once*) · *Reliability, constant work, and a good cup of coffee* (🔴 *push full directory snapshots, not deltas — no failure-mode cliff*) · **Google SRE ch. 21 and 22** · **`k8s.af` — read ten**, including 🔴 **"Kubernetes networking problems due to conntrack"** *(conntrack exhaustion under many concurrent connections is exactly what a relay fleet will hit)* · **Netflix, "Performance Under Load: Adaptive Concurrency Limits"**

**🔥 THE INCIDENTS — inject all of these**
relay kill mid-circuit · Raft leader kill mid-commit · **asymmetric partition** · disk fill on a relay holding epoch history · certificate expiry · a poison packet that crashes one relay's parser · **all 20 relays restarting simultaneously** · a peer flooding you · **a lying relay in production** · reconnect storm · **conntrack exhaustion** · 🔴 **clock skew**

> 🔴 **THE CLOCK SKEW INCIDENT — do this one properly.** Skew one relay's clock by four seconds. **Nothing fails loudly.** Raft lease expiry is computed against a clock that disagrees with the leader's. Rate-limit windows are wrong. Epoch validity checks drift. **The relay does not crash — it quietly makes wrong decisions while every dashboard stays green.** Then write the invariant that catches it: **relays report clock offset relative to the leader, and a relay beyond threshold is quarantined from leadership.**

**✅ MILESTONE D7** — 20-relay mesh on k8s · 🔴 **rolling restart drops ZERO circuits under sustained load** · the 3am dashboard, and **time-to-root-cause under 5 minutes from dashboards alone, demonstrated on video** · **20+ incidents with runbooks** · **full cold start from epoch history, for real, and timed** · **$0.00 verified from both consoles and screenshotted** · 🔴 **the circular-dependency audit: does your admin surface, your monitoring, or your bootstrap relay depend on the mesh?** · 🚀 **BLOG POST 6 + 7**

---
---

# ⚡ LEVEL 9 — ⭐ THE ATTACK LAB & PATH SELECTION
### W49–52 · 16 Aug – 12 Sep 2027 · 4 weeks · **Milestones D8, D9** · 🚩 **Flagships #9 `ascorr` + #10 `guardplace`** · **W49 = REST**

> ⭐ **The research contribution, and the only part of this project where you will have a result nobody has published.**
>
> 🔥 **THE WALL.** Implement AS-aware selection: score candidates on AS-path disjointness between the two ends, prefer the best. Re-run the adversary. **Compromise probability drops meaningfully. Excellent.** Now put on the attacker's hat: 🔴 **your selector is deterministic and its scoring function is public — it is in your open-source repository. Where should I put my relays so your algorithm prefers them?** Place ten relays chosen to maximise their score under *your* function. **It will be dramatically more than their fair share.** *You have made the average case better and the targeted case worse — and a defender who only measured the average would never have noticed.*

| Wk | 📄 Read | 🛠 Build |
|---|---|---|
| **49** 🛌 | **REST + the AS-graph foundations.** 🔴 **Gao (2001), valley-free routing** — *start here* · **Luckie et al. (IMC 2013)** — the algorithm behind CAIDA's dataset | **Download CAIDA's AS Relationships data** — `https://www.caida.org/catalog/datasets/as-relationships/`. `lab/asgraph`: valley-free inference |
| **50** | ⛓ **THE SPINE, in order:** **Users Get Routed** (CCS 2013) → **Astoria** (NDSS 2016) → **Counter-RAPTOR** (S&P 2017) + **DeNASA** (PoPETs 2016). 🔴 **And the reality check: Juen et al. (PoPETs 2015) — 17.2M traceroutes showing BGP-simulated paths disagree badly with measured ones.** *Every design here rests on inference that is substantially wrong, and saying so is what makes it research rather than a demo* | 🚩 **`ascorr`** — circuit-compromise probability against a defined AS-level adversary, **for Adyton *and* for Tor**, on real CAIDA data. **TorPS** for security-over-time |
| **51** | 🔴🔴 **Wan et al., "Guard Placement Attacks on Path Selection Algorithms for Tor"** (PoPETs 2019) — **0.216% of bandwidth bought 18% of guard-selection probability.** *The paper this level exists to answer* → then **CLAPS** (CCS 2020) | 🚩 **`guardplace`** — **build the attack against your own selector.** Place relays optimised against your own public scoring function and measure their selection rate. Then **controlled randomness on a single tunable**, swept |
| **52** | **CS161 — the *Anonymity / Tor* chapters** · **6.858 lecture 20, Anonymous Communication** · 🔴 **"RPKI-Based Location-Unaware Tor Guard Relay Selection"** (PoPETs 2025) — *a genuinely different answer, and a candidate for your own selector* | 🔴 **THE CURVE.** Synthesis, ADRs, retrospective, `NEXT.md` |

**✅ MILESTONE D8 — the attack lab** — compromise probability against a defined AS adversary, **for Adyton and for Tor**, on real topology data, **with the inference-accuracy caveat stated in the first paragraph**

**✅ MILESTONE D9 — ⭐ the contribution**
- [ ] Candidate selectors implemented **in Python first**, scored over the same graph against the same adversary presets. **Winner chosen on data, with the reason recorded**
- [ ] 🔴 **The guard-placement adversary implemented and run against your own selector**, reporting the selection rate adversary-placed relays achieve
- [ ] 🔴 **THE CURVE, PUBLISHED:** for ≥5 randomness settings, **compromise probability against the AS adversary *and* adversary-placed-relay selection rate, on one plot.** `docs/results/tradeoff-curve.md`
- [ ] **The operating point chosen off the curve, with the reason written down.** Not by instinct
- [ ] 🔴 **The latency budget outranks the score.** *Adyton's whole trilemma choice was low latency; a selector that improves safety at 200 ms of build cost has violated the premise. If the winner exceeds budget, the budget wins and that is documented*
- [ ] 🚀 **BLOG POST 8: *"AS-aware path selection makes you predictable. Here is the curve."*** 🔴 **The plot is the post. It does not exist anywhere else, and it is the most novel thing you will write this year**

**✅ WEEK 52 — THE CLOSE**
- [ ] **README final**, tested on a human with a ten-minute timer · **the honesty and scale statements, verbatim, in the first screen**
- [ ] **The ten ADRs** (§IX.1) · 🔴 **`docs/LIMITATIONS.md`, linked from the first screen** — mesh size, simulator fidelity, **metadata**, no mobile client, single-author review, no users. *Volunteering limitations before you are asked is the single highest-leverage interview behaviour available to you*
- [ ] **`docs/COMPARISON.md`** — against **Tor**, **iCloud Private Relay**, **Nym/Loopix**, **Mullvad + Mullvad Browser**, **Google IP Protection**. Where you converge, where you diverge, why
- [ ] **`docs/RETROSPECTIVE.md`** — estimated vs actual hours per level, and the ratio. 🔴 *That ratio is a measured fact about you over twelve months, and almost no candidate has one*
- [ ] **★ The demo finalised.** `make bootstrap` from clean. **Billing $0.00**
- [ ] 🔴 **Re-record the 45-minute talk and watch it against the Week-26 recording. The delta is the year**
- [ ] **`docs/NEXT.md`** — Privacy Pass and accountable abuse handling · traffic shaping and the WF evaluation · the full Tor benchmark · 6.1810 and 15-445 in full · **and only then, if you have an offer and a jurisdiction, the public network**

> ❓ **THE LAST QUESTION.** *"Why would I use this instead of Tor?"*
> **The answer is: you would not** — and you should be able to say that without flinching, then explain what you learned by building it anyway, and then show two curves the Tor Project has never published. **If you can do that calmly, the year worked.**
---
---

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

## VII.3 Sources

| Source | Link | For |
|---|---|---|
| **NeetCode 150 → 250** | `neetcode.io/practice` | The pattern spine, W1–26. In order, grouped by pattern. **Do not skip the easy ones** |
| **LeetCode, company-tagged** | `leetcode.com` | W27–52. Filter by your seven targets, last 6 months. Premium is genuinely worth $35 for the two months before a loop |
| **AtCoder Educational DP Contest** | `atcoder.jp/contests/dp` | 🔴 **The best structured DP resource that exists, and it is free.** Problems A–L, Level 3 |
| **CSES Problem Set** | `cses.fi/problemset/` | Sorting & Searching, Dynamic Programming, Graph Algorithms, Mathematics — the curated sets |
| **Codeforces Div 2 A–D** | `codeforces.com` | Weekly, all year. Rated when it fits, virtual when it does not. Band **1450 → 1750** |
| **Codeforces EDU (ITMO)** | `codeforces.com/edu/courses` | Segment trees (W39–40), suffix structures (W41). The best free structured material for these |
| **Laaksonen, *Competitive Programmer's Handbook*** | `cses.fi/book/book.pdf` | Free. **Ch. 7** (DP), **ch. 9** (range queries), **ch. 13–15** (graphs), **ch. 26** (probability) |
| **Skiena, *The Algorithm Design Manual* 3e** | — | The *why*. **Ch. 8** (DP), **ch. 9** (intractability and reductions) |
| **Alex Xu, *System Design Interview* Vol. 1 & 2** | *(owned)* | The weekly design curriculum is built on these |
| **interviewing.io / Pramp** | `interviewing.io` · `pramp.com` | Free peer mocks. **One paid mock with a real FAANG engineer around W30 if affordable** |

## VII.4 🔗 The map — where Adyton and Track I compound

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

## VII.5 The problem sets, level by level

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

## VII.6 🔴 The failure log — the part that actually produces improvement

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

## VII.7 Time boxes

| Difficulty | Box | On expiry |
|---|---|---|
| Easy | 15 min | Read the solution, log as failure, re-solve from scratch the same day |
| Medium | 25 min | Read the **approach only**, retry 15 min, then the full solution. Log |
| Hard | 45 min | Same protocol |

**Never exceed the box.** An hour spent stuck teaches less than reading the solution and re-solving it twice.

## VII.8 System design — 2.5h/week from Week 1, 20 written designs

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

## VII.9 Mocks and loops

| When | What |
|---|---|
| **W30** | First human mock · **one paid mock with a real FAANG engineer, if affordable** |
| **W40** | 🔴 **The Raft Figure 8 whiteboard test** — a checkable gate, not a formality. A human watches you draw it from memory in under five minutes |
| W34, W38, W42 | Monthly mock, one round |
| **W44** | 🔴 **Full timed loop #1 — four rounds in one day**, and the **Final Gauntlet** week |
| W45–52 | Weekly, escalating to two per week from W50. **Loops #2 through #12** |

**A "full timed loop" means** two 45-minute coding rounds with a human, one 45-minute system design, one 30-minute behavioural, **in a single day** with realistic breaks. **Not four sessions across a week.** The exhaustion is what you are training for, and it is what surprises people at their first real onsite.

**Speak while you solve, always, including alone.** The most common cause of a failed coding round in a candidate who *can* solve the problem is silence.

## VII.10 📈 Track I exit criteria
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
