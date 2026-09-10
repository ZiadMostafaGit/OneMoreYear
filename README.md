# ἌΔΥΤΟΝ · ADYTON — The Two-Year Roadmap to Supreme Backend & Systems Engineering

## Eight complete university courses. One real system that needs all of them. Every lecture, lab and page linked.

**ἄδυτον** — *the innermost chamber; not to be entered.* What a person's private life is supposed to be, and currently is not.

**Built for one person:** Ziad Mostafa Elsaid · Cairo, Egypt · Logic Leap · BSc Management Information Systems · Codeforces 1450 · targeting **backend engineering with a systems and infrastructure edge** at Cloudflare, Fastly, Tailscale, Datadog, Stripe, and the infrastructure organisations inside Google, Meta, Amazon and Microsoft.

**Week 1 begins Monday 2026-09-14. Week 104 ends Sunday 2028-09-10.**
🎯 **Applications open Week 56 — Monday 2027-10-04.** You do not wait for Year 2 to start interviewing.

> This is not a reading list and not a topic list. It is a **training program with a verified source for every single thing in it.** Eight complete courses — **lectures and all labs** — are run to completion, each sequenced to land before the part of the system that needs it. Every lecture and every lab is **individually linked in the Course Atlas (§VII).** Every topic also carries **exact book pages** and **an engineered AI prompt**. Every topic is entered through a **failure you reproduce before you are allowed the explanation.** Every project has **numeric exit criteria.** Every market claim carries **its number from your own dataset of 569 postings.** Every week has a date.

---

## 📖 Contents

| # | Section |
|---|---|
| I | [The Problem Adyton Solves](#i--the-problem-adyton-solves) |
| II | [The Seven Decisions](#ii--the-seven-decisions) |
| III | [The Evidence Base](#iii--the-evidence-base) |
| IV | [The Eight Laws](#iv--the-eight-laws) |
| V | [The Learning System — the Three-Source Rule](#v--the-learning-system--the-three-source-rule) |
| VI | [The AI Prompt System](#vi--the-ai-prompt-system) |
| VII | [🔴 **THE COURSE ATLAS** — every lecture, every lab, every link](#vii--the-course-atlas) |
| VIII | [The Four Tracks](#viii--the-four-tracks) |
| IX | [The Spine: ADYTON](#ix--the-spine-adyton) |
| X | [The Ten Flagships](#x--the-ten-flagships) |
| XI | [The Level Map](#xi--the-level-map) |
| XII | [Year One — Levels 0–6](#-level-0--the-machine) |
| XIII | [Year Two — Levels 7–13](#-level-7--operations-and-the-shell-) |
| XIV | [Track I — The Interview Machine](#-track-i--the-interview-machine) |
| XV | [Track J — Craft, Career & Visibility](#-track-j--craft-career--visibility) |
| XVI | [The 104-Week Calendar](#-the-104-week-calendar) |
| XVII | [The Cut Order](#-the-cut-order) |
| XVIII | [Assessment](#-assessment-the-three-proofs) |
| XIX | [Tracking & Re-planning](#-tracking--re-planning) |
| XX | [Résumé & GitHub Translation](#-résumé--github-translation) |
| XXI | [The Library](#-the-library) |
| XXII | [Project Catalog & Final Checklist](#-project-catalog--final-checklist) |

---

## I — The Problem Adyton Solves

**Right now, a person browsing the web is assembled.** Not watched — *assembled.* A tracker on a news site and a tracker on a shopping site share an identifier. A data broker joins those to a purchase record, a location history and a mobile advertising ID. An ISP in many jurisdictions sells the destination log legally. No single party sees your whole life; together they construct one profile that contains all of it, and that profile is sold, leaked, subpoenaed, and used to price things differently for you than for someone else.

The existing answers all fail differently:

| Answer | Why it fails for a normal person |
|---|---|
| **A VPN** | Moves the trust from your ISP to one company that sees everything. Single trust anchor, and an enormous incentive to log |
| **Tor** | Correct, admirable, and **nearly unusable for daily life**: endless CAPTCHAs, blocked exits, banks locking accounts, logins breaking on circuit rotation, video that will not stream. The cause is structural — exit IPs are shared with abusers and **Tor cannot ban anyone**, because anonymity means no accountability |
| **iCloud Private Relay** | Architecturally right — two hops, split trust — and proof it works at consumer scale. But Safari and Apple devices only, Apple as the single trust anchor, and **no per-identity compartments**: all your browsing in one bucket |
| **Browser hardening alone** | A uniform fingerprint from a stable home IP is useless. **The IP identifies you** |

**Adyton is the missing one:** an open, cross-platform **privacy relay network with per-identity compartmentalisation**, run by its users rather than a company, at latency a normal person will accept.

### The product, stated exactly

**It is not "nobody knows who I am."** When you log into Amazon, Amazon knows it is you — you told them. **It is: nothing can link your identities to each other.**

Your shopping self, social self, work self and reading self get separate network paths, separate exit addresses, separate browser profiles, separate cookie jars — bound at the operating-system level so a leak between them is structurally prevented rather than merely unlikely. The tracker on the news site and the tracker on the shopping site see two unrelated strangers. Your ISP sees encrypted traffic to one relay and nothing else.

> **The one sentence you are permitted to claim, for two years:**
> **No company can assemble one profile that contains all of you.**
>
> Never *"nobody can track you."* The first person who tests the overclaim dismantles it in one blog post, and nothing else you say gets believed — including the true parts you spent two years measuring.

### Why this is a *great* engineering problem and not just a virtuous one

**There is nowhere to hide from difficulty.** No central server to fall back on when you get lazy about consensus. No "the database" to lean on when you get lazy about distribution. There is an **actual adversary** — well-funded, technically strong, already deployed. And the failure mode is not a 500 error: **a bug in the packet parser is a deanonymisation vulnerability.**

**It also forces, structurally, every skill on the list — and it is the only project on my list that needs all eight courses:**

| Adyton needs | The course that teaches it | Corpus |
|---|---|---|
| Cache-aware packet layout, C at the metal, malloc, linking | **CMU 15-213** | 19.4% C++ |
| Why TCP head-of-line-blocks unrelated circuits, and what QUIC fixes | **Stanford CS144** *(labs in C++)* | 14.8% networking |
| Consensus, replication, linearizability, fork consistency | **MIT 6.5840** | **48.4%** distributed systems |
| AEAD, key agreement, what "secure" formally means | **Boneh Crypto I** | 10.9% security |
| Network namespaces, page tables, traps — the kernel mechanism | **MIT 6.1810** *(xv6, C)* | — |
| Storage engines, B+trees, MVCC, logging, recovery | **CMU 15-445** *(projects in C++)* | 19.4% PostgreSQL |
| Vectorized execution, code generation, cost models | **CMU 15-721** | database internals |
| Threat models, sandboxing, TLS, **anonymous communication** | **MIT 6.858** | 10.9% security |

**Nothing on that list is decoration.** Remove any of it and either Adyton does not work or you cannot explain why it does.

---

## II — The Seven Decisions

**1. Two years, priced honestly.** The full-course version costs **2,485 hours ≈ 104 weeks at 32h/week.**

| | Hours |
|---|---|
| Eight complete courses — lectures **and all labs** | **1,095** |
| Adyton build | 700 |
| Track I — DSA + system design | 490 |
| Career and craft | 200 |
| **Total** | **2,485** |

**What the second year buys:** eight completed courses with their labs, instead of eight courses' worth of named lectures. That is the difference between *"I watched the Raft lectures"* and *"I implemented Raft, then a sharded fault-tolerant key-value store on top of it, and MIT's test suite passes."* It is a real difference and interviewers can tell.

**What it costs:** twelve months. That is the honest price and you should keep seeing it.

**2. 🎯 Applications open Week 56 (2027-10-04), not in Year 2.** This is the decision that makes the two-year plan affordable. **Waiting for the full course stack before applying would cost a year of senior-role salary for near-zero hiring benefit.** Year 1 ends with circuits, compartments, per-hop QUIC transport, a 30-node mesh and Raft-backed consensus — already a strong CV — and **Week 56 lands in the strongest autumn hiring window.** Year 2 is depth *while interviewing*, and every completed course makes you better in the loops you are already sitting.

**3. ⚙️ C++ for the data plane, not Rust.** Reversed from the previous version, and the reasoning is better than the reasoning I had before.

**Your entire course stack is C and C++.** 15-213 is C. CS144's labs are C++. 6.1810's xv6 labs are C. 15-445's projects are C++. Choosing Rust would mean training in C/C++ for two years and writing the product in something else. And C++ is **19.4% of backend postings and 23.4% of infrastructure postings**, against Rust's ~10% — it does not even appear in the top 28 backend skills.

> **The C++ sentence. Memorise it, because it is the harder and better answer.**
>
> *"This is a network daemon parsing hostile input from untrusted peers, where a memory bug is not a crash but a deanonymisation vulnerability. Rust gives you that safety by construction. I chose C++ and had to **earn** it: sanitizers on every CI run, libFuzzer on every parser, `std::span` instead of pointer-plus-length, no raw owning pointers in the parsing path, and a documented subset. Here are the three memory bugs my fuzzer found and how. That is the position almost every real systems codebase is actually in, and being the engineer who can hold that line is worth more than being the engineer who was handed it."*

🔴 **The condition, and it is not optional: the safety tooling is first-class scheduled work from Week 7, not an afterthought.** ASan + UBSan + TSan in CI · libFuzzer on every parser with a committed corpus · `-Wall -Wextra -Werror -fno-omit-frame-pointer` · `clang-tidy` with the `cppcoreguidelines` and `bugprone` checks · **and `docs/cpp-subset.md` stating what you do not use and why.** If you skip this, C++ was the wrong call and an interviewer will find out in ten minutes.

**Four languages, each owning a real layer:**

| Language | Owns | Corpus | Courses that teach it |
|---|---|---|---|
| **C++20** | `adyton-core` — onion crypto, Sphinx, per-hop QUIC, circuits, path selection, the relay daemon, shaping. **The entire data plane** | **19.4%** | 15-213, CS144 labs, 15-445 projects |
| **Java 21** | `adyton-directory` — Raft, epoch documents; `adyton-credential` — Privacy Pass; the measurement aggregator and public gateway. **The stateful control plane** | **52.7%** | — (Track F block F12) |
| **Go** | `adyton-edge` — NAT traversal (`pion/ice`), gossip, the client supervisor and CLI, netns orchestration, the browser launcher | 37.6% | **6.5840's five labs are Go** |
| **Python** | `lab/` — the attack lab, AS-graph simulation, the WF classifier, benchmarks, DP analysis | 43.0% | 15-721 analysis work |

**4. Budget: zero.** **Oracle Cloud always-free** (4 ARM cores / 24GB, no expiry) is the seed node, STUN/relay server and always-on mesh member. **AWS 12-month free tier — sign up Week 36**, so it covers the weeks you actually need multi-region nodes; billing alarm at $5 before any resource. **GCP $300/90-day credit** spent in one planned 72-hour window in Level 8. All eight courses are free.

**5. Hardware: 64GB+ workstation.** What makes a 30–50 node local mesh feasible. **Measure the real ceiling in Week 2.**

**6. Fully mobile — read this in Week 1.** **US H-1B cap registration is once a year, in March.** An October 2027 application for a cap-subject US role means register March 2028 → lottery → start October 2028. **Europe has no lottery** — Ireland's Critical Skills permit, the EU Blue Card, the Netherlands scheme and the UK Skilled Worker visa are continuous. **EMEA offices are the primary target, not the fallback.** *Verify current rules yourself in Week 1.*

**7. 🌙 Two Ramadans, budgeted in advance.**
**Ramadan 1448 ≈ 8 Feb – 9 Mar 2027 → weeks 22–26.** **Ramadan 1449 ≈ 28 Jan – 26 Feb 2028 → weeks 72–76.** Both budgeted at **20h/week, not 32**, with scope moved out in advance rather than discovered. **Eid al-Fitr** in weeks 26 and 76; **Eid al-Adha** ≈ 17 May 2027 (week 36) and ≈ 6 May 2028 (week 86), both at 26h.

---

## III — The Evidence Base

Everything traces to a dataset you collected in **August 2026: 569 verified postings, 83 companies, 937 distinct named skills.** Where a number is not stated, no claim is being made. Percentages are against **backend (n=93)** or **backend+infra (n=205)**, stated each time.

### The degree question. Settled here. Never raised again.

| Question | Answer | Of |
|---|---|---|
| Postings requiring a PhD with no stated alternative | **5** (0.9%) | 569 |
| Postings demanding a CS degree, no alternative field, no experience route | **1** (0.18%) | 569 |
| — and that one is | **a student internship** | |
| **Backend postings stating no degree requirement at all** | **51 of 93 (54.8%)** | 93 |
| Backend postings that are CS-strict | 35 (37.6%) | 93 |
| — of which carry an equivalent-experience clause | 19 | |

**More than half of backend postings state no degree gate at all.** Of the third that do, most carry the equivalent-experience clause. **That clause is the route, and something has to fill it.** Adyton plus eight completed courses is what fills it — and the courses matter here specifically, because *"I completed MIT 6.5840 including all five labs"* is the closest thing to a transcript that exists outside a university.

### What backend postings demand (n=93)

| Skill | Share | Skill | Share |
|---|---|---|---|
| **Java** | **52.7%** | System design | 23.7% |
| AWS | 48.4% | GCP | 21.5% |
| **Distributed systems** | **48.4%** | Kafka | 20.4% |
| Python | 43.0% | **C++** | **19.4%** |
| Go | 37.6% | CI/CD | 19.4% |
| Mentoring | 36.6% | **PostgreSQL** | **19.4%** |
| REST/API design | 34.4% | Microservices | 18.3% |
| Communication | 34.4% | Data structures | 17.2% |
| Scalability | 31.2% | On-call | 17.2% |
| Collaboration | 31.2% | Docker | 17.2% |
| Kubernetes | 30.1% | Testing | 15.1% |

### 🔴 The three findings that shaped this plan

**1. The operational shell matters more than the clever core.** Eight candidate projects modelled against all 569 postings:

| What you add | Coverage, backend+infra |
|---|---|
| Nothing — you today | **1.0%** |
| A clever core with no operational shell | 6.5% |
| The operational shell alone | 15.1% |
| **Shell + a distributed-systems core** | **41.2%** |
| **… + Java** | **58.8%** |

**The shell is never optional.** Level 7 delivers it *before* applications open, and §XVII says what to cut instead.

**2. Java was worth more than any project choice: +14.1 points**, and 46.8% of your residual gap. Levels 6 and 10 are Java levels and they are not optional.

**3. The interview ratio is inverted from what people assume.**

| Round | Named in backend postings |
|---|---|
| **System design** | **76.3%** |
| Algorithms / DSA | 18.3% |

So **system design is a first-class daily track from Week 1.** But DSA is a *gate* — frequency is irrelevant when 100% of the loops contain two coding rounds, and the bar has risen. **~320h DSA aimed at hard-problem fluency, ~170h dedicated system design.**

### The gaps no solo project can close
**Mentoring 36.6% · Communication 34.4% · Collaboration 31.2% · Leadership 17.2%.** Adyton demonstrates none. **§XV.5 sources them deliberately from Logic Leap** — six specific situations, now spread across two years, which is easier than one.

### 🔴 The split — read this twice
Adyton has two halves doing different jobs. **The cryptographic and algorithmic core** — Sphinx, AS-aware path selection, guard-placement resistance, the shaping evaluation — is the real intellectual content and it is your forty-five-minute answer. **Graph algorithms are named in 0 of 569 postings.** **The operational shell** — running the mesh, sharding it, observing it, deploying it, breaking it, keeping it up — is what the screen reads.

**Build the core because it is the answer and because a year of YAML will not sustain you for two years. Build the shell because it is what gets you read. Never confuse which is doing which job.**

---

## IV — The Eight Laws

**1. Failure First.** Every topic opens with **🔥 THE WALL** — a broken system you reproduce. **You may not read the explanation, open the lecture, or run the prompt until the failure is on your screen.** Knowledge acquired to resolve a felt confusion is retained permanently; knowledge from a video you nodded at is gone in nine days. Interviewers hear the difference instantly.

**2. Courses are finished, not sampled.** Eight courses, **lectures and labs, to completion.** A course you watched half of is a topic you can name and not use. The Atlas (§VII) has a checkbox per lecture and per lab **because you are going to tick all of them.**

**3. Three sources, one topic.** Every topic has a **course**, a **book location**, and an **AI prompt**. §V says how to choose. **"I don't know where to learn this" is never a valid reason to stall.**

**4. ⚙️ In C++, safety is earned every single commit.** Sanitizers, fuzzers and the documented subset are not hygiene — **they are the argument for having chosen C++ at all.** A week where CI's sanitizer job is disabled is a week the language choice became indefensible.

**5. Measure everything.** Every project ships **📈 EXIT CRITERIA** with numbers. **A speedup you cannot attribute to a named mechanism is a coincidence.**

**6. Set the target before you measure. Record both numbers.** Every target here was written before any measurement existed. Some are wrong. **Record the pre-measurement target and the actual, side by side.** The pattern becomes `RETROSPECTIVE.md` in Week 103 — a document almost no candidate has.

**7. Never trust the AI on a fact you will build on.** The prompts in §VI are the fastest teacher you have and they will also **confidently invent APIs, misstate a paper's result, and hand you a plausible algorithm that is subtly wrong.** Every AI-learned claim a design decision rests on gets verified against the course or the book.

**8. Ship publicly, and honestly.** **You are never allowed to say "unsolved", "first", or "nobody has done this."** State the gap precisely instead — it is a stronger answer and the only one that survives an interviewer who knows Tor exists. And the permitted headline never changes: *no company can assemble one profile that contains all of you.*

---

## V — The Learning System — the Three-Source Rule

Every topic carries three entries. They do different jobs, and using the wrong one for the job is how people waste months.

### 📺 THE COURSE — for building a model from nothing
Use when the topic is **new to you as a whole area** and you need the model constructed in the right order by someone who has taught it twenty times and knows where students fall over. **Use it when** you could not currently draw the diagram, do not know the vocabulary, or cannot tell what the hard part is. **Do not use it when** you need one specific answer — a 25-lecture course to learn what a fencing token is is a catastrophic misuse of a week.

**In this plan the courses are also the spine of Track C, and they are run to completion.** §VII is the Atlas.

### 📕 THE PAGES — for precision and for coming back
**Named chapters and sections. Never a whole book.** Use when you need the statement to be *exact*, when you will return to it, or when a lecture was hand-wavy about the thing you actually have to implement. **Use it when** you are about to write the code. **Do not use it when** you are still deciding whether a topic is relevant — skim the lecture first.

### 🤖 THE PROMPT — for the gap, the block, and the check
Use in **three situations and mostly not otherwise**: you are **blocked on one specific thing** and neither source addresses it directly (most common, enormously effective) · **two sources appear to disagree** and you need the disagreement named rather than smoothed over · **you believe you understand something and want that belief attacked** (the highest-value use and the one people skip).

**The AI is not a substitute for the course. It is a substitute for the teaching assistant you do not have** — the person you could turn to and ask "wait, why does that not deadlock?"

### The choosing rule

| Your situation | Use |
|---|---|
| "I don't know what this area even contains" | 📺 Course, first 3 lectures |
| "I need to implement this tomorrow" | 📕 Pages, then 🤖 TEACH on the one part still foggy |
| "I'm stuck on one specific mechanism" | 🤖 TEACH. **Do not open a course** |
| "Two sources disagree" | 🤖 BRIDGE |
| "I think I understand it" | 🤖 INTERROGATE. **You will be wrong more often than you expect** |
| "My code works but I don't know if it's right" | 🤖 REVIEW, then 🤖 ADVERSARY |
| "A lab test fails and I can't see why" | 📕 the lab handout again, **line by line** — then 🤖 REVIEW. Course labs have precise specs and 90% of failures are a misread spec |
| "I need to remember this in a year" | 📕 Pages + a spaced-repetition card in your own words |

---

## VI — The AI Prompt System

Five archetypes. 🔴 **Save these as files in `docs/prompts/` in Week 1 and paste them — do not retype from memory**, because the value is entirely in the structure and you will erode it.

Each has **`[SLOTS]`** you fill. Every level and every Track F block supplies its own filled slots as a **prompt card**.

### 🤖 PROMPT 1 — TEACH · the workhorse
```
You are a senior systems engineer teaching one specific thing to one specific person.
You are not writing documentation and not writing a blog post. You are sitting next
to me while I am stuck.

WHO I AM
Backend engineer, ~2 years professional. Self-taught CS, no CS degree — so assume my
knowledge is deep in places and has holes in unpredictable places, and check rather
than assume. Strong Python and Go, competent C++, learning Java 21. Working through
CMU 15-213, Stanford CS144, MIT 6.5840, MIT 6.1810, CMU 15-445/721, MIT 6.858.
I already understand: [PREREQ]
I do NOT understand: [GAP]

WHAT I AM BUILDING
[CONTEXT — one sentence about the Adyton component]
I am blocked on this specific decision: [THE DECISION]

TEACH IT IN THIS ORDER. Do not reorder.
1. THE FAILURE. What breaks without this? Show me the broken version concretely — the
   actual mechanism, with a concrete sequence of events. No analogies.
2. THE MINIMAL FIX. The smallest correct thing that prevents that failure, as code or
   pseudocode I could actually run.
3. WHY MY INSTINCT IS WRONG. Name the solution I would most likely have reached for on
   my own, and show precisely where it breaks — the exact interleaving or input.
4. WHAT PRODUCTION SYSTEMS ACTUALLY DO. How does [NAMED REAL SYSTEM] do this, what does
   it do differently from the minimal version, and why?
5. THE THREE THINGS PEOPLE GET WRONG. For each: the mistake, the symptom you would
   observe, and how to tell it apart from the other two.

RULES
- Mechanism before analogy. If you use an analogy at all, use it after step 2.
- Every performance or behavioural claim gets a number, or the words "I don't know the
  number."
- If something is genuinely contested, unsettled or version-dependent, say so
  explicitly. Do not smooth it into false confidence.
- If any part of my question contains a wrong assumption, correct that FIRST.
- Assume I implement this tomorrow. Optimise for me being correct, not comfortable.

THEN, at the end:
- 5 questions whose answers would prove I understood, ordered easy to hard.
- 1 small exercise whose OUTPUT would be visibly different if I had misunderstood. Tell
  me what the right output looks like and what a misunderstanding would produce.
- The single most likely way I will get this wrong in my own implementation.
```

### 🤖 PROMPT 2 — INTERROGATE · the one you will avoid
**The highest-value prompt in the set and the one you will skip.** Run it at every level exit exam and after every completed course.
```
I am going to claim I understand [TOPIC]. Your job is to find out whether that is true,
and you should assume it is only partly true.

Interrogate me. Rules:
- Ask ONE question at a time and wait for my answer. Never give me the answer first.
- Start at "can you state it correctly," move to "can you apply it," then to "do you
  know its limits and failure modes."
- When I am vague, do not accept it. Ask me to be specific — a number, a sequence, an
  interleaving, a concrete case.
- When I am wrong, do not tell me the answer. Ask the question that makes the
  contradiction visible to me.
- Include at least one question about a case where the standard answer does NOT apply,
  and at least one about what this costs.
- After about 8 exchanges, stop and give me a verdict:
    SOLID: [what I clearly understand]
    SHAKY: [what I can state but not apply]
    ABSENT: [what I do not know that I do not know]
    GO READ: [the one specific source and section that fixes the biggest gap]

Context: I am building [CONTEXT] and I need this right because [CONSEQUENCE].
Begin with your first question. Nothing else.
```

### 🤖 PROMPT 3 — REVIEW · critique my implementation
⚙️ **Note the C++-specific section 4 — this is the prompt that substitutes for the code reviewer you do not have, and in C++ that matters more than it would in Rust.**
```
Review this implementation of [COMPONENT] as a hostile senior reviewer who has
maintained systems like this in production and has been paged at 3am because of code
like this.

CONTEXT
Language: [LANG]. Part of [SYSTEM], on the [data plane / control plane].
The invariant it must never violate: [INVARIANT]
The failure consequence if it does: [CONSEQUENCE]
Concurrency model: [e.g. one thread per circuit, shared state behind a shared_mutex]

REVIEW IN THIS ORDER, and be concrete — quote the line
1. CORRECTNESS. Any input, interleaving or failure timing that violates the invariant.
   For each: the exact sequence of events. No style issues here.
2. WHAT HAPPENS UNDER FAILURE. Process killed here / here / here. Network partition.
   Disk full. Peer sends malformed input. Clock jumps backwards.
3. RESOURCE BEHAVIOUR. What is unbounded? Every queue, buffer, map and retry — is there
   a bound, and what happens at the bound?
4. ⚙️ C++ MEMORY AND LIFETIME SAFETY. Specifically: any raw pointer or reference whose
   lifetime is not obviously tied to an owner; any span/string_view outliving its
   buffer; iterator invalidation; integer overflow or signed/unsigned confusion in
   length arithmetic; any place a hostile length field could drive an allocation or an
   index; anything ASan/UBSan/TSan would catch that my tests would not; and any use of
   a construct my documented subset forbids.
5. THE SECURITY READ. This parses hostile input from untrusted peers. What does an
   attacker who controls the input do? What does a timing difference leak?
6. WHAT I APPEAR TO HAVE MISUNDERSTOOD. Not bugs — evidence in the code that my mental
   model of the problem is wrong.
7. Only now: readability and idiom.

RULES
- Rank findings by consequence, worst first. Say "no finding" for a category rather than
  inventing one.
- If the code is fine in a category, say so plainly. Do not manufacture concerns.
- For every finding give the smallest fix, not a redesign — unless a redesign is
  genuinely the answer, in which case say why the small fix is a trap.

CODE:
[paste]
```

### 🤖 PROMPT 4 — BRIDGE · when sources disagree
```
I have two sources that appear to disagree, or a gap between them I cannot close.

SOURCE A says: [claim, and where it is from]
SOURCE B says: [claim, and where it is from]
What I am trying to decide: [DECISION]

1. Are they actually in conflict, or answering different questions? Be precise about
   the scope of each claim.
2. If it is a real disagreement: what changed between them — a different threat model,
   workload, decade of hardware, or definition of a shared term?
3. Which applies to MY case, and what specifically about my case decides it?
4. What is the third position neither takes, and is it better?
5. What would I have to measure to settle this myself, and is it cheap enough to be
   worth measuring rather than reasoning about?

Flag explicitly if you are uncertain which is right, or if the field has not settled
this. Do not pick a side for the sake of giving me an answer.
```

### 🤖 PROMPT 5 — ADVERSARY · think like the attacker
Adyton's whole subject is an adversary. Run this on every security-relevant component and on the threat model itself at every phase boundary.
```
You are an attacker. Your goal is to defeat the privacy property below, and you are
competent, well-resourced and patient.

THE SYSTEM: [component description]
THE PROPERTY IT CLAIMS: [e.g. "an observer cannot link identity A's traffic to B's"]
YOUR CAPABILITIES: [e.g. you run one relay; you observe one AS; you control 5% of
peers; you operate a website the user visits]
WHAT YOU DO NOT HAVE: [e.g. you cannot observe the whole network; you cannot break
X25519]

Produce:
1. The 5 most promising attacks, ordered by expected success and NOT by cleverness.
   Boring attacks that work beat elegant ones that do not.
2. For each: the concrete steps, what you observe, what you infer, and — critically —
   HOW MANY OBSERVATIONS you need before your confidence is meaningful.
3. Which of these the stated threat model already concedes, versus which are claimed to
   be defended and are not.
4. The cheapest defence for each, and what it costs in latency, bandwidth or usability.
5. The one attack the defender is most likely to have not thought about at all.

Be specific and quantitative. If an attack's feasibility depends on a number I have not
given you (mesh size, traffic volume, AS coverage), tell me which number decides it and
what the threshold is.
```

---

## VII — THE COURSE ATLAS

> **Eight courses, run to completion. Every lecture and every lab has a checkbox, because you are going to tick all of them.**
>
> **How to read this.** Each course has its lecture table and its lab table. The levels in §XII–XIII reference this Atlas by lecture number — *"Atlas → 6.5840 L6–L7"* — rather than repeating links, so the links live in exactly one place and stay maintainable.
>
> **On URLs.** Every link below returned HTTP 200 when this document was written. Course sites move and re-number by year; **if a link dies, the pattern is almost always `.../<year>/...` and the current year's page is one search away.** Where a per-lecture video URL does not stably exist, the Atlas gives **the playlist plus the exact lecture number and title** — a two-click lookup — rather than a fabricated video ID. **One course, CS144, wipes its handouts every academic year and is flagged accordingly.**
>
> ⏱ **Total: 1,095 hours.** Track C runs at **11h/week in Year 1, 8h/week in Year 2.**

### The sequence — why each course lands when it does

| Weeks | Course | h | Lands before |
|---|---|---|---|
| **1–16** | **CMU 15-213** — Computer Systems | 200 | Everything. It is the foundation and it is C |
| **17–21** | **Boneh — Cryptography I** | 50 | **Level 2**, the onion protocol |
| 22–26 | *🌙 Ramadan 1448 — reduced. 15-213/Boneh catch-up only* | 25 | — |
| **27–38** | **Stanford CS144** — Networking *(C++ labs)* | 130 | **Level 4**, the transport |
| **39–52** | **MIT 6.5840** — Distributed Systems *(Go labs)* | 190 | **Level 6**, the directory |
| **53–70** | **MIT 6.1810** — OS Engineering *(xv6, C)* | 180 | **Level 7's** deep isolation work, and everything about the kernel |
| 71 | *slack* | 10 | — |
| 72–76 | *🌙 Ramadan 1449 — reduced. Lectures only* | 20 | — |
| **77–90** | **CMU 15-445** — Database Systems *(C++ projects)* | 150 | **Level 10**, the credential store |
| **91–100** | **CMU 15-721** — Advanced Database Systems | 85 | **Level 12's** performance work |
| **95–104** | **MIT 6.858** — Systems Security | 110 | Runs alongside **Levels 12–13**, the release |

> 🔴 **Two exceptions, pulled forward out of sequence because Adyton needs them early:**
> **6.858 Lecture 1 (threat models)** in **Week 7**, and **6.858 Lecture 19 (anonymous communication, the Tor paper)** in **Week 12**. Watch those two standalone; the full course still runs late.

---

## 📺 COURSE 1 — CMU 15-213: Introduction to Computer Systems
**Weeks 1–16 · 200h · C** · Schedule and slides: **https://www.cs.cmu.edu/~213/schedule.html** · Book: *CS:APP* 3rd ed. · Self-study labs: **https://csapp.cs.cmu.edu/3e/labs.html**

> **Why it is first and why it is the longest.** This is the course that makes you not-a-tourist in systems. Every later course assumes it. And Adyton's data plane is C++ on packet buffers — `malloclab` and `cachelab` are not academic exercises for you, they are your product's hot path.

### Lectures — 25

| # | Lecture | CS:APP | ✓ |
|---|---|---|---|
| 1 | Overview | Ch. 1 | ☐ |
| 2 | Bits, Bytes & Integers | §2.1–2.3 | ☐ |
| 3 | Machine Programming I: Basics | §3.1–3.6 | ☐ |
| 4 | Machine Programming II: Control | §3.6–3.7 | ☐ |
| 5 | Machine Programming III: Procedures | §3.7–3.9 | ☐ |
| 6 | Machine Programming IV: Data | §3.10–3.11 | ☐ |
| 7 | Linking | Ch. 7 | ☐ |
| 8 | Design and Debugging | §9.10–9.12 | ☐ |
| 9 | 🔴 **The Memory Hierarchy** | §6.1–6.3 | ☐ |
| 10 | 🔴 **Cache Memories** | §6.4–6.7 | ☐ |
| 11 | Virtual Memory: Concepts | §9.1–9.6 | ☐ |
| 12 | Virtual Memory: Details | §9.7–9.8 | ☐ |
| 13 | Dynamic Memory Allocation: Basic | §9.9 | ☐ |
| 14 | Dynamic Memory Allocation: Advanced | §9.10–9.12 | ☐ |
| 15 | 🔴 **Code Optimization** | Ch. 5 | ☐ |
| 16 | Processes and Multitasking | §8.1–8.4 | ☐ |
| 17 | Exceptional Control Flow | §8.5–8.8 | ☐ |
| 18 | System Level I/O and File Systems | Ch. 10 | ☐ |
| 19 | File Systems / Network Programming I | §11.1–11.4 | ☐ |
| 20 | Network Programming II | §11.4–11.6 | ☐ |
| 21 | Concurrent Programming | §12.1–12.3 | ☐ |
| 22 | Synchronization: Basic | §12.4, 12.5.1–3 | ☐ |
| 23 | Synchronization: Advanced | §12.5.4–5, 12.7–8 | ☐ |
| 24 | Thread-Level Parallelism | §12.6 | ☐ |
| 25 | Frontiers of Computing | — | ☐ |

### Labs — 9, all self-contained for self-study

| Lab | Handout | Why it matters to Adyton | ✓ |
|---|---|---|---|
| L0 | C Programming Lab *(from the schedule page)* | Baseline C fluency | ☐ |
| L1 **Data Lab** | [datalab-handout.tar](https://csapp.cs.cmu.edu/3e/datalab-handout.tar) | Bit-level ops — the Sphinx header is bit-level | ☐ |
| L2 **Bomb Lab** | [bomb.tar](https://csapp.cs.cmu.edu/3e/bomb.tar) | Reading disassembly. **The single best debugging education there is** | ☐ |
| L3 **Attack Lab** | [target1.tar](https://csapp.cs.cmu.edu/3e/target1.tar) | 🔴 **You exploit a buffer overflow yourself.** This is why your parser is fuzzed | ☐ |
| L4 **Cache Lab** | [cachelab-handout.tar](https://csapp.cs.cmu.edu/3e/cachelab-handout.tar) | 🔴 Direct input to Level 0's layout decisions | ☐ |
| L5 **Malloc Lab** | [malloclab-handout.tar](https://csapp.cs.cmu.edu/3e/malloclab-handout.tar) | 🔴 You write an allocator. Adyton's packet pools are this | ☐ |
| L6 **Shell Lab** | [shlab-handout.tar](https://csapp.cs.cmu.edu/3e/shlab-handout.tar) | Signals, process groups, reaping — the node supervisor | ☐ |
| L7 **Proxy Lab** | [proxylab-handout.tar](https://csapp.cs.cmu.edu/3e/proxylab-handout.tar) | 🔴 **A concurrent caching web proxy. Adyton's relay is this, hardened** | ☐ |
| L8 | Performance Lab *(optional)* — [perflab-handout.tar](https://csapp.cs.cmu.edu/3e/perflab-handout.tar) | Kernel optimisation practice | ☐ |

🤖 **PROMPT 1** for the block you will get stuck on · `GAP:` why my malloclab throughput is fine and utilisation is terrible · `CONTEXT:` designing Adyton's per-circuit packet buffer pool · `THE DECISION:` segregated free lists vs a single coalescing list for fixed-size onion cells · `NAMED REAL SYSTEM:` jemalloc's size classes

---

## 📺 COURSE 2 — Boneh: Cryptography I
**Weeks 17–21 · 50h** · Slides and structure: **https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/** · Free textbook: **https://toc.cryptobook.us/** (*A Graduate Course in Applied Cryptography*, Boneh & Shoup) · Videos: the course's Coursera lectures, free to audit

> **Why weeks 17–21.** Level 2 is the onion protocol and it starts week 12 — so weeks 17–21 run *alongside* it, which is the right order: you hit the crypto wall in the build, then the course explains it properly. **Do weeks 1–4 and 6 before week 19.**

| Week | Module | Adyton needs it for | ✓ |
|---|---|---|---|
| 1 | Stream ciphers, one-time pad, PRGs, semantic security | What "secure" formally means | ☐ |
| 2 | Block ciphers: DES, AES, CBC/CTR modes, CPA security | Mode choice and why | ☐ |
| 3 | Message integrity: MACs, CBC-MAC, HMAC, collision resistance | 🔴 The per-hop MAC in the Sphinx header | ☐ |
| 4 | 🔴 **Authenticated encryption, TLS case study, padding attacks, key derivation** | 🔴 **AEAD and HKDF — the key schedule** | ☐ |
| 5 | Basic key exchange: Merkle puzzles, Diffie–Hellman, number theory | The groundwork | ☐ |
| 6 | 🔴 **Public-key encryption: RSA, ElGamal, trapdoor permutations** | X25519 and the handshake | ☐ |
| 7 | Digital signatures | 🔴 **Level 10's blind signatures** | ☐ |

🤖 **PROMPT 1** · `GAP:` why raw X25519 output must not be used as a key and what HKDF's `info` is for · `CONTEXT:` deriving per-hop keys for a Sphinx header from one ephemeral exchange · `THE DECISION:` whether one DH output can safely produce header key, payload key and next-hop blinding factor · `NAMED REAL SYSTEM:` the Noise protocol key schedule, and Lightning's BOLT #4

---

## 📺 COURSE 3 — Stanford CS144: Introduction to Computer Networking
**Weeks 27–38 · 130h · C++** · Course site: **https://web.stanford.edu/class/cs144/** · Video lectures: **[playlist PLvFG2xYBrYAQCyz4Wx3NPoYJOFjvU7g2Z](https://www.youtube.com/playlist?list=PLvFG2xYBrYAQCyz4Wx3NPoYJOFjvU7g2Z)** (Levis & McKeown)

> 🔴 **The single best networking education that exists, and its labs are in C++ — which is now your data-plane language.** Over eight checkpoints you build a working TCP: a byte stream, a reassembler, a receiver, a sender, a full connection, then an ARP-speaking network interface and an IP router. **Level 4 assumes you have done this.** After it you will never again be vague about retransmission, windows, or why loss hurts — and you will understand *why* QUIC made each of its choices instead of repeating that it is better.

⚠️ **HANDOUT WARNING — verified, act on it.** **CS144 clears its assignment repository every academic year and keeps no official archive.** The `cs144.github.io` paths that circulate online are dead. **In Week 26, before the course starts: go to the live course site, download every checkpoint PDF and the starter repo, and commit them to your own private mirror.** If you do not, you will lose access mid-course. This is the only course in the Atlas with this problem and it is the reason for the warning.

### Checkpoints — 8 (the "Minnow" framework, C++)

| # | Checkpoint | What you build | ✓ |
|---|---|---|---|
| 0 | **Networking warmup** | `webget` — a minimal HTTP client — plus an in-memory reliable **byte stream** | ☐ |
| 1 | **Stitching substrings** | The **reassembler**: turn out-of-order, overlapping segments into an ordered stream | ☐ |
| 2 | **The TCP receiver** | Sequence numbers, wrapping, the window | ☐ |
| 3 | **The TCP sender** | 🔴 Retransmission timers, backoff, the send window. **The hardest checkpoint** | ☐ |
| 4 | **Interoperating** | Your TCP talks to the real internet, **replacing the kernel's socket** | ☐ |
| 5 | **The network interface** | ARP, sending IP datagrams over Ethernet | ☐ |
| 6 | **The IP router** | Longest-prefix-match forwarding | ☐ |
| 7 | **Putting it together / end-to-end** | The whole stack, and the performance work | ☐ |

### Lecture topics — watch alongside the checkpoints
The four-layer model · packet switching and statistical multiplexing · **the byte-stream abstraction** · reliable delivery, stop-and-wait, sliding window · **TCP in detail: connection setup, teardown, flow control** · 🔴 **congestion control: AIMD, slow start, fast retransmit/recovery** · routing (link-state, distance-vector) · **inter-domain routing and BGP** · packet queueing and delay · NAT and middleboxes · security: attacks on TCP/IP.

🤖 **PROMPT 1** · `GAP:` mechanically why in-order delivery makes one circuit's loss stall another's, at the segment level · `CONTEXT:` deciding whether Adyton multiplexes circuits over one connection per relay pair, as Tor does · `THE DECISION:` per-hop QUIC versus one TCP per link · `NAMED REAL SYSTEM:` Tor's `or_connection` multiplexing, and QUIC's stream independence

---

## 📺 COURSE 4 — MIT 6.5840 (6.824): Distributed Systems
**Weeks 39–52 · 190h · Go** · Schedule with all papers: **https://pdos.csail.mit.edu/6.824/schedule.html** · Videos: **[playlist PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB](https://www.youtube.com/playlist?list=PLrw6a1wE39_tb2fErI4-WkMbsvGQk9_UB)** (Robert Morris)

> 🔴 **Distributed systems is 48.4% of your backend postings — tied for the highest single technical skill in your corpus. This course is how you earn it.** One paper per lecture. **Read the paper before the lecture, every time** — the lecture is a discussion of the paper, not a substitute for it.
> **The five labs are Go**, which is Adyton's edge language, so the labs and the product reinforce each other.

### Lectures — 22, with the assigned paper

| # | Lecture | Paper | Adyton | ✓ |
|---|---|---|---|---|
| 1 | Introduction | MapReduce (2004) | Grounding | ☐ |
| 2 | RPC and Threads | — | The Go edge layer | ☐ |
| 3 | GFS | GFS (2003) | The canonical "failure is normal" design | ☐ |
| 4 | 🔴 **Paxos** | Paxos | **ADR-0004: the alternative you rejected** | ☐ |
| 5 | Go patterns | "The Go Programming Language and Environment" | Lab technique | ☐ |
| 6 | 🔴 **Fault Tolerance: Raft (1)** | Raft extended (2014) | 🔴 **Level 6** | ☐ |
| 7 | 🔴 **Fault Tolerance: Raft (2)** | Raft extended (2014) | 🔴 **Level 6 — the half people skip** | ☐ |
| 8 | 🔴 **Consistency and Linearizability** | Linearizability | **ADR-0005: the consistency model** | ☐ |
| 9 | 🔴 **Zookeeper** | ZooKeeper (2010) | 🔴 **Adyton's exact shape: consensus in a small set, reads served widely** | ☐ |
| 10 | Q&A Lab 3A+B | — | Lab support | ☐ |
| 11 | Distributed Transactions | 6.033 ch. 9 | System design answers | ☐ |
| 12 | Spanner | Spanner (2012) | Clocks, and TrueTime's honesty about them | ☐ |
| 13 | Chain Replication | CR (2004) | **The second alternative considered** | ☐ |
| 14 | Optimistic Concurrency Control | FaRM (2015) | Ties to 15-445's CC lectures | ☐ |
| 15 | Verification of distributed systems | IronFleet (2015) | Why you TLA+ the barrier protocol | ☐ |
| 16 | Cache Consistency: Memcached at Facebook | Memcached at FB (2013) | A canonical design-round answer | ☐ |
| 17 | AWS Lambda | On-demand Container Loading (2023) | Modern infra | ☐ |
| 18 | Ray | Ray (2021) | Modern infra | ☐ |
| 19 | 🔴 **Fork Consistency, SUNDR** | SUNDR (2004) | 🔴🔴 **THE most important lecture in the Atlas for this project — see below** | ☐ |
| 20 | Peer-to-peer: Bitcoin | Bitcoin (2008) | Sybil framing, and why you have no chain | ☐ |
| 21 | 🔴 **Byzantine Fault Tolerance** | PBFT (1999) | 🔴 **Level 10: why you chose the lighter model** | ☐ |
| 22 | Project demos | — | — | ☐ |

### Labs — 5, all Go

| Lab | Handout | ✓ |
|---|---|---|
| 1 **MapReduce** | [lab-mr.html](https://pdos.csail.mit.edu/6.824/labs/lab-mr.html) | ☐ |
| 2 **Key/Value Server** | [lab-kvsrv1.html](https://pdos.csail.mit.edu/6.824/labs/lab-kvsrv1.html) | ☐ |
| 3 🔴 **Raft** | [lab-raft1.html](https://pdos.csail.mit.edu/6.824/labs/lab-raft1.html) | ☐ |
| 4 🔴 **Fault-tolerant KV service on Raft** | [lab-kvraft1.html](https://pdos.csail.mit.edu/6.824/labs/lab-kvraft1.html) | ☐ |
| 5 🔴 **Sharded KV service** | [lab-shard1.html](https://pdos.csail.mit.edu/6.824/labs/lab-shard1.html) | ☐ |

> ### 🔴 Why Lecture 19 matters more to Adyton than any other lecture in the Atlas
>
> Adyton's directory has a requirement that sounds like performance and is actually privacy: **every client must see the same epoch view of the mesh, because if two clients see different peer sets, that difference is itself a fingerprint that distinguishes them.**
>
> That is precisely a **fork attack**, and **fork consistency** is the property that constrains it: a malicious directory can split clients into divergent views, but **cannot do so indefinitely without the split becoming detectable.** SUNDR is where this is worked out; Certificate Transparency is the deployed system built on the same idea.
>
> **It reframes Level 6 from "run Raft" into "build a directory whose forks are detectable"** — a materially stronger design and a materially better interview answer. You would not have found it searching for "peer-to-peer consensus."

🤖 **PROMPT 4 (BRIDGE)**, week 50 · `SOURCE A:` Raft gives linearizable consensus among the authorities, so they agree on epoch N · `SOURCE B:` SUNDR shows a malicious server can still fork clients' views of a consistent log · `DECISION:` what Raft actually buys Adyton's *clients*, and what I must add — hash chaining, client-side gossip of epoch hashes, or both

---

## 📺 COURSE 5 — MIT 6.1810: Operating System Engineering
**Weeks 53–70 · 180h · C, RISC-V** · Schedule: **https://pdos.csail.mit.edu/6.1810/2024/schedule.html** · The xv6 book: **https://pdos.csail.mit.edu/6.1810/2024/xv6/book-riscv-rev4.pdf**

> **Why Year 2.** Adyton's compartments (Level 3) use network namespaces from *above* — you make them work by Week 27 without needing to know how the kernel implements them. This course is where you stop treating the kernel as a black box, and it lands before Level 7's deep isolation and Level 11's chaos work. **Nine labs where you modify a real, small, complete operating system.**

### Lectures — 22

| # | Lecture | Reading | ✓ |
|---|---|---|---|
| 1 | Introduction | xv6 book ch. 1 | ☐ |
| 2 | C in xv6 | K&R §2.9, 5.1–5.6, 6.4 | ☐ |
| 3 | OS design | xv6 book ch. 2 | ☐ |
| 4 | 🔴 **Page tables** | xv6 book ch. 3 | ☐ |
| 5 | System call entry/exit | xv6 book ch. 4 (except 4.6) | ☐ |
| 6 | GDB and calling conventions | RISC-V calling convention doc | ☐ |
| 7 | Page faults | xv6 book §4.6 | ☐ |
| 8 | Q&A labs | — | ☐ |
| 9 | Device drivers | xv6 book ch. 5 | ☐ |
| 10 | 🔴 **Locking** | xv6 book "Locking" | ☐ |
| 11 | Scheduling 1 | xv6 book "Scheduling" through §7.4 | ☐ |
| 12 | Coordination | remainder of "Scheduling" | ☐ |
| 13 | File systems | xv6 `bio.c`, `fs.c`, `sysfile.c`, `file.c` | ☐ |
| 14 | 🔴 **Crash recovery** | `kernel/log.c` + logging sections | ☐ |
| 15 | File system performance | Journaling ext2fs paper | ☐ |
| 16 | Virtual memory for applications | Virtual Memory Primitives paper | ☐ |
| 17 | OS Organization | Micro-Kernel-Based Systems paper | ☐ |
| 18 | Virtual Machines | Dune paper | ☐ |
| 19 | Kernels and high-level languages | RedLeaf paper | ☐ |
| 20 | 🔴 **Networking** | Receive Livelock paper | ☐ |
| 21 | 🔴 **Meltdown** | Meltdown paper | ☐ |
| 22 | Multi-core scalability and RCU | RCU paper | ☐ |

### Labs — 9

| Lab | Handout | Why it matters to Adyton | ✓ |
|---|---|---|---|
| **util** | [util.html](https://pdos.csail.mit.edu/6.1810/2024/labs/util.html) | Unix utilities; xv6 orientation | ☐ |
| **syscall** | [syscall.html](https://pdos.csail.mit.edu/6.1810/2024/labs/syscall.html) | You add a syscall. The boundary you cross per packet | ☐ |
| 🔴 **pgtbl** | [pgtbl.html](https://pdos.csail.mit.edu/6.1810/2024/labs/pgtbl.html) | Page tables by hand — the mechanism behind every isolation claim | ☐ |
| **traps** | [traps.html](https://pdos.csail.mit.edu/6.1810/2024/labs/traps.html) | Trap frames, backtraces, alarms | ☐ |
| **cow** | [cow.html](https://pdos.csail.mit.edu/6.1810/2024/labs/cow.html) | Copy-on-write fork — why process isolation is cheap | ☐ |
| 🔴 **net** | [net.html](https://pdos.csail.mit.edu/6.1810/2024/labs/net.html) | 🔴 **You write a network device driver.** The other end of CS144 | ☐ |
| **lock** | [lock.html](https://pdos.csail.mit.edu/6.1810/2024/labs/lock.html) | Removing lock contention — Level 12's problem, in miniature | ☐ |
| **fs** | [fs.html](https://pdos.csail.mit.edu/6.1810/2024/labs/fs.html) | Large files, symlinks, the on-disk format | ☐ |
| **mmap** | [mmap.html](https://pdos.csail.mit.edu/6.1810/2024/labs/mmap.html) | Demand paging — ties to 15-213's VM lectures | ☐ |

🤖 **PROMPT 1** · `GAP:` what a network namespace actually *is* in kernel data structures, now that I have written page tables and a driver · `CONTEXT:` I have been using netns for Adyton's compartments since Week 20 without knowing the mechanism · `THE DECISION:` whether anything inside a namespace can observe or reach the host's network stack · `NAMED REAL SYSTEM:` the Linux `net_namespace` struct and how veth pairs are wired

---

## 📺 COURSE 6 — CMU 15-445/645: Database Systems
**Weeks 77–90 · 150h · C++** · Schedule with slides, notes and videos: **https://15445.courses.cs.cmu.edu/fall2024/schedule.html** · Book: *Database System Concepts* (free chapters linked per lecture)

> **Why Adyton needs a database course.** Its Java control plane has two real stores: the **epoch store** — a versioned, immutable-once-published document set read concurrently while a new version is being written, which is MVCC — and the **credential store**, which needs durability, recovery and garbage collection of spent tokens. Levels 6 and 10 are much better with this course behind them. **And its five projects are C++**, which is your data-plane language.

### Lectures — 25

| # | Lecture | Adyton | ✓ |
|---|---|---|---|
| 0 | Course Overview & Logistics | — | ☐ |
| 1 | Relational Model & Algebra | Grounding | ☐ |
| 2 | Modern SQL | The metadata store | ☐ |
| 3 | Database Storage I | Page layout | ☐ |
| 4 | Database Storage II | — | ☐ |
| 5 | 🔴 **Storage Models & Compression** | The compact AS-graph encoding shipped in the epoch document | ☐ |
| 6 | 🔴 **Memory Management** (buffer pool) | Ties to 15-213 malloclab | ☐ |
| 7 | Hash Tables | The replay seen-set | ☐ |
| 8 | Indexes & Filters I | Bloom filters for the seen-set | ☐ |
| 9 | Indexes & Filters II | — | ☐ |
| 10 | Index Concurrency Control | Latch crabbing — the circuit table | ☐ |
| 11 | Sorting & Aggregations | — | ☐ |
| 12 | Joins | — | ☐ |
| 13 | Query Execution I | Ties to 15-721 | ☐ |
| 14 | Query Execution II | — | ☐ |
| 15 | Query Planning & Optimization | — | ☐ |
| 16 | 🔴 **Concurrency Control Theory** | Serialisability, the vocabulary | ☐ |
| 17 | Two-Phase Locking | — | ☐ |
| 18 | Timestamp Ordering | — | ☐ |
| 19 | 🔴 **Multi-Version Concurrency Control** | 🔴 **The epoch store is an MVCC store** | ☐ |
| 20 | 🔴 **Database Logging** | The credential store's durability | ☐ |
| 21 | 🔴 **Database Recovery** (ARIES) | Crash recovery, properly | ☐ |
| 22 | Introduction to Distributed Databases | — | ☐ |
| 23 | Distributed OLTP | Ties to 6.5840's transactions lecture | ☐ |
| 24 | Distributed OLAP | Ties to 15-721 | ☐ |
| 25 | Final Review + Systems Potpourri | — | ☐ |

### Projects — 5, C++ (BusTub)

| Project | What you build | ✓ |
|---|---|---|
| **P0** C++ Primer | Modern C++ warm-up — **and a good check on your subset discipline** | ☐ |
| 🔴 **P1** Buffer Pool Manager | LRU-K replacer, page guards, disk scheduler | ☐ |
| 🔴 **P2** Database Index | **A concurrent B+Tree.** The hardest project | ☐ |
| **P3** Query Execution | Volcano-model operators | ☐ |
| 🔴 **P4** Concurrency Control | MVCC with snapshot isolation | ☐ |

🤖 **PROMPT 4 (BRIDGE)** · `SOURCE A:` 15-445 lecture 19 — MVCC keeps multiple versions and garbage-collects the unreachable ones · `SOURCE B:` Adyton's epoch documents are immutable, signed and hash-chained, and clients only ever read the current one · `DECISION:` whether my epoch store genuinely needs MVCC, or whether immutability plus a validity window has already solved the problem a different way

---

## 📺 COURSE 7 — CMU 15-721: Advanced Database Systems
**Weeks 91–100 · 85h** · Schedule with all papers: **https://15721.courses.cs.cmu.edu/spring2024/schedule.html** · Videos: **[playlist PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ](https://www.youtube.com/playlist?list=PLSE8ODhjZXjYa_zX-KeMJui7pcN1rIaIJ)**

> **The honest placement.** Adyton is not a database. **~6 of these lectures serve it directly** — vectorized execution and code generation for Level 12's forwarding-path optimisation and the attack lab's AS-path computation over millions of candidate circuits; scheduling and NUMA for the relay's thread model; networking protocols for the wire format. **The rest is a parallel career investment**, and a good one: this material is *directly* what **Confluent, Databricks, ClickHouse, Snowflake and StarTree** interview on, and that tier is unusually remote-friendly and a strong fit for you.
> **Watch it also for the method** — paper, then what industry shipped, then the measurement. That posture is what this whole roadmap is trying to build in you.

| # | Lecture | Key paper(s) | Adyton | ✓ |
|---|---|---|---|---|
| 0 | Course Overview | — | — | ☐ |
| 1 | Modern Analytical Database Systems | Lakehouse (CIDR'21); Composable Data Management (VLDB'23) | — | ☐ |
| 2 | Data Formats & Encoding I | Columnar Storage Formats (VLDB'23) | Compact epoch encoding | ☐ |
| 3 | Data Formats & Encoding II | FastLanes (VLDB'23); BtrBlocks (SIGMOD'23); BitWeaving (SIGMOD'13) | 🔴 AS-graph compression | ☐ |
| 4 | Query Execution & Processing I | MonetDB/X100 (CIDR'05); Vertica (ICDE'13) | — | ☐ |
| 5 | Query Execution & Processing II | Velox (VLDB'22); Meta's Lakehouse (CIDR'23) | — | ☐ |
| 6 | 🔴 **Vectorized Query Execution** | SIMD Investments (VLDBJ'20); Rethinking SIMD (SIGMOD'15) | 🔴 **Batch packet processing; AS-path scoring** | ☐ |
| 7 | 🔴 **Code Generation & Compilation** | Neumann (VLDB'11); Krikellas (ICDE'10) | The selector's hot loop | ☐ |
| 8 | 🔴 **Scheduling & Coordination** | Morsel-Driven Parallelism (SIGMOD'14); NUMA-aware Scans (VLDB'15) | 🔴 **The relay's thread model** | ☐ |
| 9 | Hash Join Algorithms | Schuh (SIGMOD'16); Richter (VLDB'15) | — | ☐ |
| 10 | Multi-Way Join Algorithms | Worst-Case Optimal Joins (VLDB'20) | — | ☐ |
| 11 | Server-side Logic Execution | Froid (VLDB'17); UDF Batching (CIDR'24) | — | ☐ |
| 12 | 🔴 **Networking Protocols** | Client Protocol Redesign (VLDB'17); ConnectorX (VLDB'22) | 🔴 Wire-format design | ☐ |
| 13 | Optimizer Implementation I | Chaudhuri (PODS'98); Cascades (1995) | — | ☐ |
| 14 | Optimizer Implementation II | Unnesting Queries (BTW'15); Dynamic Programming (SIGMOD'08) | — | ☐ |
| 15 | Optimizer Implementation III | Plan Stitch (VLDB'18); Neo (VLDB'19) | — | ☐ |
| 16 | 🔴 **Cost Models** | Leis (VLDB'15); LEO (VLDB'01) | 🔴 **Adyton's path-selection scoring IS a cost model** | ☐ |
| 17 | System Analysis: Google Dremel/BigQuery | Dremel (VLDB'20, VLDB'10) | Design-round material | ☐ |
| 18 | System Analysis: Databricks/Spark | Photon (SIGMOD'22); Delta Lake (VLDB'20) | Design-round material | ☐ |
| 19 | System Analysis: Snowflake | Elastic Warehouse (SIGMOD'16); Disaggregated Storage (NSDI'22) | Design-round material | ☐ |
| 20 | System Analysis: DuckDB | DuckDB (SIGMOD'19); MotherDuck (CIDR'24) | Design-round material | ☐ |
| 21 | System Analysis: Yellowbrick | Yellowbrick on K8s (CIDR'24) | — | ☐ |
| 22 | System Analysis: Amazon Redshift | Redshift Re-Invented (SIGMOD'22) | Design-round material | ☐ |

> **Note on videos:** ~14 of the 22 lectures have recordings; the rest have slides and the assigned papers only. **For the eight without video, the papers are the lecture** — which is the more useful skill anyway.

---

## 📺 COURSE 8 — MIT 6.858: Computer Systems Security
**Weeks 95–104 · 110h** · Schedule with lecture notes and papers: **https://css.csail.mit.edu/6.858/2022/schedule.html** · Full video lectures (2014 edition): **MIT OpenCourseWare 6.858** — `ocw.mit.edu/courses/6-858-computer-systems-security-fall-2014/`

> **Why it is last, and the two lectures pulled forward.** Adyton is a security system, so this course *should* be first — except that its most valuable lectures are only meaningful once you have a system to apply them to, and Levels 12–13 are release and threat-model publication, which is exactly when you want it. **But two lectures cannot wait:**
>
> 🔴 **Lecture 1 (Introduction, threat models) → watch in Week 7**, before you write `docs/threat-model.md` v1.
> 🔴 **Lecture 19 (Anonymous communication, the Tor paper) → watch in Week 12**, at the start of the onion level. **This is the single lecture in the entire Atlas whose subject *is* Adyton.**

| # | Lecture | Reading | ✓ |
|---|---|---|---|
| 1 | 🔴 **Introduction, threat models** *(→ Week 7)* | — | ☐ |
| 2 | Security architecture | Google Infrastructure Security (2017) | ☐ |
| 3 | User authentication | "Your password doesn't matter" (2019); U2F (2016) | ☐ |
| 4 | 🔴 **Buffer overflow defenses** | Baggy bounds checking (2009) | ☐ |
| 5 | Privilege separation | OKWS (2004) | ☐ |
| 6 | OS and VM isolation | Firecracker (2020) | ☐ |
| 7 | Software fault isolation | WebAssembly (2017) | ☐ |
| 8 | Sandboxing libraries | RLBox (2020) | ☐ |
| 9 | Client device security | iOS Security (2019) | ☐ |
| 10 | Android security | Android Platform Security Model (2019) | ☐ |
| 11 | Symbolic execution | EXE (2006) | ☐ |
| 12 | Web security model | Web security overview (2022) | ☐ |
| 13 | 🔴 **Network security** | Security Problems in TCP/IP (2004) | ☐ |
| 14 | Secure channels | Analysis of SSL 3.0 (1996) | ☐ |
| 15 | 🔴 **Certificates** | SSL and HTTPS (2013) | ☐ |
| 16 | Information security in real life | *(guest)* | ☐ |
| 17 | Messaging security | Secure messaging (2015) | ☐ |
| 18 | IoT security: Azure Sphere | *(guest)* | ☐ |
| 19 | 🔴🔴 **Anonymous communication** *(→ Week 12)* | **Tor (2004)** | ☐ |
| 20 | 🔴 **CPU timing attacks** | On Spectre and Meltdown (2019) | ☐ |
| 21 | Hardware security | *(guest)* | ☐ |
| 22 | Zoom security | E2E Encryption for Zoom (2021) | ☐ |
| 23 | Project presentations | — | ☐ |

### Labs — 5

| Lab | Handout | Why it matters ⚙️ | ✓ |
|---|---|---|---|
| 🔴 **1 Buffer overflows** | [lab1.html](https://css.csail.mit.edu/6.858/2022/labs/lab1.html) | 🔴 **You exploit and then defend C memory bugs. This is the lab that justifies your C++ subset** | ☐ |
| **2 Privilege separation** | [lab2.html](https://css.csail.mit.edu/6.858/2022/labs/lab2.html) | The relay's process model | ☐ |
| **3 Symbolic execution** | [lab3.html](https://css.csail.mit.edu/6.858/2022/labs/lab3.html) | Complements fuzzing — a second bug-finding technique | ☐ |
| **4 Browser security** | [lab4.html](https://css.csail.mit.edu/6.858/2022/labs/lab4.html) | 🔴 Directly relevant to Level 3's compartments | ☐ |
| **5 Final project** | [lab5.html](https://css.csail.mit.edu/6.858/2022/labs/lab5.html) | 🔴 **Use Adyton. Submit your own threat model and attack lab as the project** | ☐ |

🤖 **PROMPT 5 (ADVERSARY)** after lecture 19 · `SYSTEM:` Adyton, whole · `PROPERTY:` *no company can assemble one profile that contains all of you* · `CAPABILITIES:` you are an ad-tech firm with trackers on 60% of the top 10,000 sites, you buy broker data, and you operate one Adyton relay · `WHAT YOU DO NOT HAVE:` you cannot observe the whole network and you cannot break the crypto. **Run this at Week 100 and put the result in `docs/threat-model.md`.**

---

### 📋 The Atlas at a glance

| Course | Lectures | Labs/Projects | Hours | Weeks |
|---|---|---|---|---|
| CMU 15-213 | 25 | 9 | 200 | 1–16 |
| Boneh Crypto I | 7 modules | psets | 50 | 17–21 |
| Stanford CS144 | ~20 | 8 checkpoints | 130 | 27–38 |
| MIT 6.5840 | 22 | 5 | 190 | 39–52 |
| MIT 6.1810 | 22 | 9 | 180 | 53–70 |
| CMU 15-445 | 25 | 5 | 150 | 77–90 |
| CMU 15-721 | 22 | — | 85 | 91–100 |
| MIT 6.858 | 23 | 5 | 110 | 95–104 |
| **TOTAL** | **~166 lectures** | **41 labs/projects** | **1,095** | |

🔴 **166 lecture checkboxes and 41 lab checkboxes. Tick every one.** That is the artifact — and *"eight courses completed including all forty-one labs"* is the closest thing to a transcript that exists outside a university, which is precisely what the equivalent-experience clause in 37.6% of backend postings is asking you for.

---

## VIII — The Four Tracks

```
┌───────────────────────────────────────────────────────────────────────────────┐
│ TRACK C — COURSES  (Y1: 11h/wk · Y2: 8h/wk)                          NEW     │
│ The eight courses in §VII, run to completion, lectures AND labs.             │
│ Sequenced so each lands before the part of Adyton that needs it.             │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK D — DEPTH  (Y1: 11h/wk · Y2: 10h/wk)                                    │
│ Adyton. Long weekend blocks. Nothing hard is built in 45-minute slices.       │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK I — INTERVIEW  (Y1: 8h/wk · Y2: 10h/wk)                                 │
│ DSA + SYSTEM DESIGN. DAILY from week 1. Never batched, never skipped.        │
├───────────────────────────────────────────────────────────────────────────────┤
│ TRACK J — CRAFT & CAREER  (Y1: 2h/wk · Y2: 4h/wk)                             │
│ Design docs, ADRs, writing, Arti PRs, referrals, CV, applications, and the    │
│ Logic Leap evidence. Referrals open WEEK 20. Applications open WEEK 56.       │
└───────────────────────────────────────────────────────────────────────────────┘
```

**Year 1 week: 32h = 11 Courses / 11 Depth / 8 Interview / 2 Craft.**
**Year 2 week: 32h = 8 Courses / 10 Depth / 10 Interview / 4 Career.**

Your shape: **4h weekdays + 6h each weekend day.** **Weekday evenings are lectures, reading, DSA and system design. The weekend blocks are labs and Adyton** — course labs and protocol work both need uninterrupted hours and neither survives being chopped into evenings.

> **Read twice.** Depth without the interview track means nobody sees the depth — you fail the phone screen and never reach system design. The interview track without depth gets you an L4 offer and a six-year stall. **Courses without Adyton makes you a very well-educated person with nothing to show.** Adyton without courses makes you someone who built one thing and cannot generalise. **If you have only one hour on a given day, spend it on Track I** — it is the only track that degrades irreversibly when skipped.

**Budget:** 104 × 32 = 3,328 nominal. −176 (eight rest weeks at 10h) −108 (nine Ramadan weeks at 20h) −12 (two Eid weeks at 26h) −**~550 of genuine slack and buffer** = **~2,485 hours of planned work**, which is exactly the §II total.

| Track | Hours | Share |
|---|---|---|
| Courses — the eight, complete | ~1,095 | 44% |
| Depth — Adyton | ~700 | 28% |
| Interview — DSA ~320h + design ~170h | ~490 | 20% |
| Craft & Career | ~200 | 8% |

---

## IX — The Spine: ADYTON

### What it is

**An open, cross-platform privacy relay network with per-identity compartmentalisation, made of its users.** Every person running Adyton is a node: their device, on their home connection, forwards other users' onion-encrypted traffic — traffic it cannot read — to other peers. It is a **peer mesh**, not servers you operate. Free-tier cloud nodes bootstrap it; **they are not the mesh.**

**The pitch:** *"iCloud Private Relay's architecture, but open, cross-platform, run by its users, and with the thing Apple doesn't have — per-identity compartments, so your shopping self and your reading self cannot be linked. And it can ban abusers without deanonymising anyone, which is the thing Tor structurally cannot do."*

### 🔴 The honesty statement — say this FIRST, every time

> Onion routing is not new and I did not invent it. **Tor has run it in production since 2003**, has millions of users, and is the right tool for anyone whose safety depends on it. **Arti**, the Tor Project's Rust implementation, shipped 2.0.0 in February 2026. **Nym** and **Loopix** take the stronger-anonymity corner of the trade-off. **Apple's iCloud Private Relay** proves two-hop split trust works at consumer scale. **Sphinx**, **Astoria**, **Counter-RAPTOR**, **DeNASA**, **CLAPS**, **WTF-PAD** and **Privacy Pass** are all published work I implement rather than invent.

**The gaps that are actually real, and each is measurable:** no deployed QUIC transport for onion routing — papers only · no deployed AS-aware path selection — Astoria, Counter-RAPTOR, DeNASA and CLAPS are published and **none runs anywhere** · **no open, measured guard-placement-resistant selection** — Wan et al. showed AS-aware selection becomes *predictable* and nobody has published the trade-off curve · no open, cross-platform, low-latency peer mesh with per-identity compartments and accountable abuse handling.

**The sentence you are allowed to say:** *"Onion routing is solved and Tor does it better than I ever will. What isn't deployed anywhere is AS-aware path selection, and the reason is a 2019 result showing it makes your selector predictable. I implemented it, built the attack against my own selector, and published the trade-off curve."*

### 🔴 The scale statement — the other thing you say unprompted

> **This mesh is 30–50 nodes I run on one workstation, plus free-tier cloud nodes in real regions, plus a deterministic simulator modelling up to 10,000 peers.** It has never had ten thousand strangers on it. Anything about scale beyond fifty nodes is measured in simulation, and the simulator is validated against the real mesh where both run — `docs/analysis/sim-fidelity.md`. **A simulator you have not validated is a fantasy generator.**

### The design thesis — the anonymity trilemma

Das, Meiser, Mohammadi and Kate proved (*Anonymity Trilemma*, IEEE S&P 2018) that **strong anonymity, low latency and low bandwidth overhead cannot coexist. Pick two.** **Adyton takes low latency and low bandwidth overhead, and explicitly gives up strong anonymity against a global passive adversary.** No cover traffic, no mixing delays. **You read this paper in Week 7**, because every subsequent decision descends from it.

### Two layers, composed

```
Browser layer   →  Mullvad Browser, UNMODIFIED   (makes you look like everyone else)
Network layer   →  ADYTON                        (makes you come from somewhere else)
```

Neither works alone: a uniform fingerprint from a stable home IP is useless because the IP identifies you; a hidden IP with a unique fingerprint is useless because the fingerprint does. **Trackers use whichever still works.** Mullvad Browser — built jointly by Mullvad and the Tor Project — normalises by *uniformity*, and its own documentation says it does not hide your IP and must be paired with a trusted network layer. **That is the hole Adyton fills.**

> **The rule: change as little as possible about the browser. Do all the work in the network layer.** Every customisation makes your users distinguishable from the crowd they hide in. **A Mullvad Browser fork is actively harmful.**

### Identity model
**One unmodified Mullvad Browser profile instance per identity** — separate profile directory, separate process, bound to its own circuit at the OS level (network namespace on Linux; per-instance SOCKS endpoint elsewhere). **A stronger boundary than browser containers, not a weaker one.** Ephemeral by default, wiped on close. **Named persistent identities opt-in**, each pinned to its own exit permanently. 🔴 **One leak across compartments defeats the entire product** — which is why `leakproof` is in CI from Week 27 and never allowed to go red.

### Threat model
**In scope:** cross-site trackers · ad-tech and data brokers · ISPs that log and sell destinations · a single malicious relay · site operators · local network observers · abusive Adyton users · sybil attackers.
**Out of scope, stated not hidden:** a global passive adversary (the trilemma choice) · a nation-state targeting one user (**use Tor**) · an adversary controlling both your guard and your exit (two hops means two nodes is the whole path — guard stickiness and AS-aware selection reduce the probability and do not eliminate it, and **that probability is measured in `lab/` and published, not asserted**) · a malicious site running scripts · **you logging in** — by design.

### ⚙️ The component map — C++ data plane, Java control plane

| Component | Language | Appears | Purpose |
|---|---|---|---|
| `adyton-core/crypto` | **C++20** | W13 | X25519, AEAD, HKDF via **libsodium**; zeroizing secret types |
| `adyton-core/sphinx` | **C++20** | W15 | Constant-size onion packets, single-pass construction |
| `adyton-core/transport` | **C++20** | W29 | Per-hop QUIC via **ngtcp2** + BoringSSL; **fingerprint normalisation** |
| `adyton-core/circuit` | **C++20** | W32 | Circuit build, teardown, health, stream multiplexing |
| `adyton-core/select` | **C++20** | W67 | AS-aware path selection, guard policy, controlled randomness |
| `adyton-core/shape` | **C++20** | W93 | Padding and timing defence under a latency budget |
| `adyton-node` | **C++20** | W9 | The relay daemon. **Middle-only by construction** |
| `adytond` | **C++20** | W21 | Client daemon: identities, circuits, SOCKS, kill switch |
| `adyton-edge/nat` | Go | W38 | NAT traversal (`pion/ice`), hole punching, relay fallback |
| `adyton-edge/gossip` | Go | W36 | SWIM membership, phi-accrual failure detection |
| `adyton-edge/launch` + `/cli` | Go | W22 | netns orchestration, browser launcher, `adyton identity …` |
| `adyton-directory` | **Java 21** | W44 | **Raft, epoch documents, hash chaining, peer admission** |
| `adyton-measure` | **Java 21** | W48 | Bandwidth/latency probing from multiple vantage points |
| `adyton-credential` | **Java 21** | W77 | **Privacy Pass issuance, revocation, rate limiting** |
| `adyton-aggregate` | **Java 21** | W86 | DP-budgeted telemetry aggregation (Prio/PrivCount-style) |
| `adyton-gateway` | **Java 21** | W80 | Public API, quotas, OpenAPI, WebSocket live status |
| `lab/asgraph`, `lab/attacks` | Python | W59 | CAIDA topology, correlation, guard placement, sybil |
| `lab/meshsim` | Python+Go | W40 | Deterministic simulation of the mesh |
| `lab/wf` | Python | W93 | WF classifier, shaping evaluation |
| `lab/bench` | Python | W2 | The benchmark harness, used for two years |

**⚙️ The C++ dependency set — you implement none of these:** **libsodium** (X25519, ChaCha20-Poly1305, BLAKE2b, `sodium_memcmp`, `sodium_memzero`) · **ngtcp2** + **BoringSSL** (QUIC) · **GoogleTest** (unit) · **RapidCheck** (property-based testing) · **libFuzzer** (clang, with a committed corpus) · **CMake** + **vcpkg**.

**ADR-0002 — the Rust/Go/Java boundary:** Go does NAT **signalling and hole punching** (`pion/ice` is the mature stack and it is Go), then hands the punched UDP socket to C++ over a unix socket as a file descriptor, and C++ owns the QUIC session on it. Go owns process orchestration — netns setup, browser launch — because that is supervision work. Java owns everything stateful and consensus-backed. **C++ owns everything a hostile peer's bytes touch.** That line is the architecture and it is the first thing you explain in an interview.

### The 13 milestones

| # | Level | Week | What you build | The invariant you must prove |
|---|---|---|---|---|
| **D0** | 1 | W11 | ⚙️ A relay that forwards and cannot be crashed by hostile input | Four attacks fail; **libFuzzer 1h clean; ASan/UBSan/TSan green in CI** |
| **D1** | 2 | W19 | Sphinx constant-size onion packets | 2-hop packet processed; **serialised size byte-identical regardless of hops remaining**, RapidCheck-asserted |
| **D2** | 3 | **W27** | ★ **THE FIRST REAL MILESTONE** — one identity end to end | Unmodified Mullvad Browser in a netns over a 2-hop circuit; **leak suite green**; two identities share no IP, DNS, cookie or fingerprint difference |
| **D3** | 4 | W35 | Per-hop QUIC transport | 🔴 **The head-of-line-blocking chart**; two peers' handshakes byte-identical except the random bits |
| **D4** | 5 | W43 | The 30-node mesh | Discovery converges; **p50 circuit recovery <800ms, p99 <3s under 20% churn**; NAT >80% direct |
| **D5** | 6 | W52 | ☕ The directory | **100% of peers hold the same epoch-N consensus hash within 30s of close under 20% churn** — because disagreement is a fingerprint |
| **D6** | 7 | W58 | The operational shell 🎯 | 30-node mesh on k8s; rolling restart drops **zero** circuits; the 3am dashboard; **CV v4 and applications open** |
| **D7** | 8 | W66 | The attack lab | Circuit-compromise probability against a defined AS adversary, **for Adyton and for Tor**, on real CAIDA data |
| **D8** | 9 | W76 | ⭐ Path selection that survives its adversary | **The AS-diversity-versus-predictability trade-off curve, published** |
| **D9** | 10 | W84 | ☕ Credentials and accountability | Revoke a credential: the holder loses access, **no other user is deanonymised and no redemption history becomes linkable** |
| **D10** | 11 | W92 | Deep operations | The metrics attack demonstrated then defeated; DP budget that fails closed; **20+ incidents with runbooks** |
| **D11** | 12 | W98 | Performance and the Tor benchmark | >200k pps/core, **<1.5ms CPU per forwarded MB**; the table, reproducible by one script |
| **D12** | 13 | W104 | Shaping, release, synthesis | Reproducible builds verified twice; threat model published; a stranger understands the architecture in 15 minutes |

### Non-goals
**Implementing QUIC, TLS or cryptographic primitives** — ngtcp2, BoringSSL, libsodium. **Modifying Mullvad Browser** — a fork is actively harmful. **Open-web exits as a default** — gateways only; exits are opt-in, separate build, separate operators. **You are in Egypt** — Week 1 writes the legal memo and you do not run an exit until it is answered. **A blockchain, token or identifying ledger.** **Full Byzantine consensus** — you watch 6.5840 L21 specifically so you can defend the lighter model. **A polished web frontend.** **A fifth language.**

### Legal — Week 1, not month twenty
**Week 1 task:** research the legal position of running relay infrastructure from Egypt, including **Law No. 175 of 2018** and the NTRA regime, and write `docs/legal.md` with cited articles, a stated conclusion, and the line **"this is not legal advice."** If ambiguous, the resolution is: **middle-only nodes from Egypt, any gateway or exit role on rented infrastructure in a jurisdiction where a named operator has accepted the exposure**, and say so in the README. **No per-user logging, ever** — including while debugging. **Reproducible builds and a published threat model before any public release invites users.**

---

## X — The Ten Flagships

**The rubric** — score before you start, build only if ≥7/10: non-obvious premise (2) · produces an artifact that does not exist yet (2) · requires a hard idea to be **correct**, not just to run (2) · demoable in 60 seconds (1) · buildable solo in ≤4 weeks (1) · has a natural "and then it broke" story (1) · explainable to a non-specialist in 2 sentences (1).

**Archetypes:** *Reimplementation with a twist* · *Instrument* · *Autopsy* · **Adversary**. Adyton has five Adversaries, because its subject *is* an adversary.

| # | Project | Level | Archetype | Score | Pitch |
|---|---|---|---|---|---|
| 1 | ⚙️ **`hardened`** | 1 | **Adversary** | 9 | The C++ safety apparatus as a deliverable: sanitizers, libFuzzer with a committed corpus, the documented subset — **and the memory bugs the fuzzer found in my own parser, written up.** This is what makes the C++ choice defensible |
| 2 | **`sphinx`** | 2 | Reimpl + **Adversary** | 9 | Constant-size onion packets from the Danezis–Goldberg paper, with the RapidCheck property test proving the size invariant and a fuzz target proving the parser cannot be made to panic |
| 3 | **`leakproof`** | 3 | **Adversary** | **10** | The suite that tries to defeat my own compartments: WebRTC escape, IPv6 leak, DNS outside the tunnel, kill-switch bypass, **cross-compartment linkage.** In CI. **Its going red is the alarm** |
| 4 | **`meshsim`** | 5 | **Adversary** | 9 | Deterministic simulation of the whole mesh — seeded clock, asymmetric partitions, churn, and **peers that lie about bandwidth or behave well only when probed** |
| 5 | **`raft-dir`** | 6 | Reimplementation | 9 | ☕ Raft in Java as Adyton's directory — **on top of having implemented it in Go for 6.5840 Lab 3, which means the second implementation is where the understanding shows** — plus epoch consensus and **detectable forks** |
| 6 | **`ascorr`** | 8 | **Instrument** | **10** | Circuit-compromise probability against a defined AS-level adversary on **real CAIDA topology with valley-free inference**, for Adyton *and* Tor, with the inference-accuracy caveat stated |
| 7 | **`guardplace`** | 9 | **Adversary + Instrument** | **10** | ⭐ **The research contribution.** Place relays to be preferred by my own AS-aware selector (Wan et al., PoPETs 2019), sweep the randomness parameter, and **publish the AS-diversity-versus-predictability curve. It does not exist** |
| 8 | **`privacypass`** | 10 | Reimplementation | 9 | ☕ Blind-signature anonymous credentials: issue, redeem, revoke, rate-limit — **unlinkable across redemptions, proven by test** — plus the sybil cost curve before and after admission |
| 9 | **`tor-bench`** | 12 | **Instrument** | **10** | Head-to-head against Tor: circuit build, TTFB, throughput, p50/p99, 1080p viability. Same client, same destinations, **one script reproduces the table** — and my own three-hop row for honesty |
| 10 | 🔴 **`1brc`** | **0 + 12** | **Instrument** | **10** | ⚙️ **The One Billion Row Challenge, twice, two years apart.** Parse 1,000,000,000 lines and aggregate per key, as fast as the machine allows — mmap, SIMD, a custom hash map, branchless parsing, thread partitioning. **A naive first attempt in Week 5 and the real assault in Week 93, with the two-year delta reported.** Against a *public leaderboard*, so the number is checkable by a stranger rather than self-reported |

**Core projects:** `latency-lab` (L0) · `sickbay` (L0) · `privcount` (L11, privacy-preserving telemetry **and the attack on my own metrics**) · `gatekeep` (L7, mTLS + secrets + expiry alerting) · `costwatch` (L7, Terraform + a *tested* billing alarm) · `pgshift` (L12, a 50M-row migration under live load) · **`shape` (L13, reduced-scope traffic shaping** — WTF-PAD-style padding implemented and its latency cost measured, **without** the full classifier-training evaluation, which moves to `NEXT.md`; see §XVII**)**.

---

## XI — The Level Map

```
YEAR ONE — the employable core (W1–52)                        TRACK C COURSES
  L0  The Machine                 W1–6    Sep–Oct 26          15-213 ────────┐
  L1  ⚙️ C++, Sanitizers & the Threat  W7–11   Oct–Nov 26   D0                │
  L2  Onion Routing               W12–19  Nov 26–Jan 27  D1   Boneh ──────────┤
  L3  Compartments ★              W20–27  Jan–Mar 27     D2   🌙 Ramadan 1448 │
  L4  Transport & Fingerprints    W28–35  Mar–May 27     D3   CS144 ──────────┤
  L5  The Mesh                    W36–43  May–Jul 27     D4                   │
  L6  ☕ The Directory             W44–52  Jul–Sep 27     D5   6.5840 ─────────┘

YEAR TWO — mastery, while interviewing (W53–104)
  L7  Operations & the Shell 🎯    W53–58  Sep–Oct 27     D6   6.1810 ────────┐
  L8  The Attack Lab              W59–66  Oct–Dec 27     D7                   │
  L9  Path Selection ⭐            W67–76  Dec 27–Feb 28  D8   🌙 Ramadan 1449 │
  L10 ☕ Credentials & Abuse       W77–84  Feb–Apr 28     D9   15-445 ────────┤
  L11 Deep Operations             W85–92  Apr–Jun 28     D10                  │
  L12 Performance & Tor Benchmark W93–98  Jun–Jul 28     D11  15-721 ────────┤
  L13 Shaping, Release, Synthesis W99–104 Jul–Sep 28     D12  6.858 ─────────┘
```

| Lvl | Name | Weeks | Dates | Milestone | Flagship |
|---|---|---|---|---|---|
| **0** | The Machine | 1–6 | 2026-09-14 → 10-25 | — | `latency-lab`, `sickbay` |
| **1** | ⚙️ C++, Sanitizers & the Threat | 7–11 | 10-26 → 11-29 | **D0** | **#1 `hardened`** |
| **2** | Onion Routing | 12–19 | 11-30 → 2027-01-24 | **D1** | **#2 `sphinx`** |
| **3** | Compartments ★ | 20–27 | 01-25 → 03-21 | **D2** | **#3 `leakproof`** |
| **4** | Transport & Fingerprints | 28–35 | 03-22 → 05-16 | **D3** | — |
| **5** | The Mesh | 36–43 | 05-17 → 07-11 | **D4** | **#4 `meshsim`** |
| **6** | ☕ The Directory | 44–52 | 07-12 → 09-12 | **D5** | **#5 `raft-dir`** |
| **7** | Operations & the Shell 🎯 | 53–58 | 09-13 → 10-24 | **D6** | `gatekeep`, `costwatch` |
| **8** | The Attack Lab | 59–66 | 10-25 → 12-19 | **D7** | **#6 `ascorr`** |
| **9** | Path Selection ⭐ | 67–76 | 12-20 → 2028-02-27 | **D8** | **#7 `guardplace`** |
| **10** | ☕ Credentials & Abuse | 77–84 | 02-28 → 04-23 | **D9** | **#8 `privacypass`** |
| **11** | Deep Operations | 85–92 | 04-24 → 06-18 | **D10** | `privcount` |
| **12** | Performance, 1BRC & the Tor Benchmark | 93–98 | 06-19 → 07-30 | **D11** | **#9 `tor-bench`**, 🔴 **#10 `1brc`**, `pgshift` |
| **13** | Release & Synthesis | 99–104 | 07-31 → 09-10 | **D12** | `shape` (reduced) |

**Rest weeks: 6, 19, 26, 43, 58, 76, 92, 104** (10h). **Buffer weeks: 34, 52, 66, 84** (catch-up only; rest if on schedule). **🌙 Reduced (20h): 22–26 and 72–76. Eid (26h): 36 and 86.**

---
---

# ⚡ LEVEL 0 — The Machine

> **Goal:** build the hardware mental model, make every number you produce trustworthy for two years, and find out what your machine can actually hold.
> **⏱ Weeks 1–6 · 2026-09-14 → 10-25 · 66h depth** · **📺 Track C: 15-213 lectures 1–8** · **W6 = REST WEEK**

## 🔥 THE WALL
Two functions summing the same 4096×4096 `int32` matrix — row-major and column-major. **Identical Big-O, identical instruction count.** Column-major will be 5–60× slower. Then two `int64` counters in one struct, two threads incrementing one each; then padded onto separate 64-byte cache lines. **3–10× throughput difference for the same work.** **You may not read on until both numbers are on your screen.**

```bash
perf stat -e cache-references,cache-misses,L1-dcache-load-misses,LLC-load-misses ./bench
perf stat -e cpu-cycles,instructions ./bench     # IPC is the smoking gun
perf c2c record ./false_sharing_bench            # false sharing, visualised
lscpu | grep -i cache && numactl --hardware
```
Instruction counts nearly identical, IPC not. **Modern CPUs are memory-limited, not instruction-limited, and Big-O is silent about the thing that dominates.**

## 📖 Why this is Week 1
In Week 15 you write a Sphinx processor touching every packet. In Week 32 a circuit table read per forwarded cell. In Week 93 you optimise forwarding to run on a volunteer's laptop without eating their battery. **Every one is a memory-layout decision and you make them all with these numbers in front of you.**

**📺 Atlas → 15-213 L1–L8** (bits, machine programming, linking, debugging). **L9–L10 (memory hierarchy, cache) land in Week 5 — the week you need them.** **Lab: Data Lab and Bomb Lab.**
**📕 Pages:** CS:APP §6.2–6.4 · Drepper §3 in full, §6.2–6.4 (skip §4–5) · Ostrovsky, "Gallery of Processor Cache Effects" — run all ten.
> 🤖 **PROMPT 1** · `PREREQ:` a cache line is 64 bytes and misses are expensive · `GAP:` why false sharing costs 5× when neither thread reads the other's variable · `CONTEXT:` laying out Adyton's per-circuit state, one forwarding thread per circuit · `THE DECISION:` whether per-circuit counters can share an array or must be padded · `NAMED REAL SYSTEM:` the Linux kernel's per-CPU variables

## 🛠 BUILD · `latency-lab` (8h) · `lab/bench` + `sickbay` (16h) · `SCALE-RISK` + legal (10h)
**`latency-lab`:** measures your machine's latency ladder and emits a card — L1/L2/L3/DRAM, uncontended vs contended atomic, mutex, branch mispredict, NVMe 4K read, syscall, context switch, TCP loopback RTT. **Derive your cache sizes from a working-set sweep without asking the OS.**
**`lab/bench`:** the harness you use for two years — fixed workloads, warm-up, percentiles, `perf stat` integration, **open-loop by default**, CI regression gate. **Coordinated omission**: a closed-loop generator cannot measure the latency of requests it failed to send; watch Gil Tene's "How NOT to Measure Latency" before publishing any number this decade.
**`sickbay`:** 8 injectable pathologies in a container (memory leak, FD leak, lock contention, runaway syscall loop, disk saturation, cgroup CPU throttling, DNS stall, a JVM GC pause), each with a hidden `SOLUTION.md` showing the *evidence* that reveals it.

📈 **EXIT CRITERIA**
- [ ] Derived cache sizes match `lscpu` within one power of two, or you can explain why not
- [ ] Row-major vs column-major gap **explained by measured LLC-miss counts**, not asserted
- [ ] False-sharing fix ≥3× throughput, `perf c2c` output committed
- [ ] Working-set-size vs ns/access chart with the knees annotated; you can recite the ladder in 20 seconds
- [ ] Two harness runs produce byte-identical result sets; **open-loop by default** and you can explain why in a paragraph
- [ ] A deliberate 5% regression is caught by `benchstat` in CI
- [ ] **`sickbay`: median diagnosis under 10 minutes across all 8, on a shuffled re-run**
- [ ] **`docs/SCALE-RISK.md`:** max concurrent `adyton-node`-shaped processes at realistic memory **with the binding resource named**; `ulimit -n`, `ip_local_port_range` and cgroup limits tuned; Oracle instance provisioned with a verified UDP RTT from Cairo; **a signed, dated go/no-go on the simulator-first strategy**
- [ ] 🔴 **`docs/legal.md`** — Egypt's Law 175/2018 and the NTRA regime, cited articles, a stated conclusion on middle-relay operation, and "this is not legal advice"
- [ ] 15-213 L1–L8 ticked; **Data Lab and Bomb Lab complete**
- [ ] CI green: build, `clang-tidy`, tests, under 6 minutes
- [ ] **`docs/prompts/` created with the five archetypes as files**
- [ ] 🔴 **`1brc` PASS 1 (W5–6, 8h) — the naive attempt, deliberately.** Generate the 1-billion-row file (13GB), then write the most obvious C++ you can: `std::getline`, `std::stod`, `std::unordered_map<std::string,...>`. **Time it. Expect 3–10 minutes.** Do not optimise anything. **Commit the number and the code, tagged `1brc-pass1`, and do not look at anyone else's solution.** This is the baseline you beat by 100× in Week 93, and the delta is a measured fact about two years of your own growth

⛓ **PROBLEM CHAIN**
```
"Column-major is 40× slower"    → cache lines → the Sphinx header layout          (→ L2)
"Contended atomic is 5×"        → MESI → why the circuit table is read-mostly     (→ L4)
"Syscall is 400ns"              → why forwarding batches, and sendmmsg            (→ L12)
"DRAM is 78ns"                  → 50 nodes × their state → the local ceiling      (→ SCALE-RISK)
"My benchmark lied"             → coordinated omission → open-loop → audit in W67
```

## 🎓 EXIT EXAM
1. Recite the latency ladder in orders of magnitude. How many L1 hits fit in one DRAM access? One NVMe read?
2. Array-of-structs vs struct-of-arrays for circuit state: for a lookup touching two fields, how many cache lines each?
3. Explain false sharing in four sentences, then the fix.
4. What is coordinated omission? Sketch a harness where a 200ms stall is invisible.
5. Why can't you average p99 across two hops? What does that imply about three hops?
6. Your box runs 46 nodes and dies at 47. Three possible binding resources and the command that identifies each.

**Pass = 5/6.** Then 🤖 **PROMPT 2** on "the memory hierarchy and how it constrains data layout."
## 🧩 PROBLEM SOLVING — L0 · W1–6 · 40 problems · 5h/wk
**Patterns:** arrays · hashing · prefix sums · two pointers · sliding window.
🔗 **The tie:** the cache intuition you just measured is *why* these are fast in practice and not only in Big-O. A prefix-sum sweep is sequential and prefetchable; a hash probe is a random access. **You now have the ns figures for both.**

| Source | Set |
|---|---|
| **NeetCode 150** | Arrays & Hashing, Two Pointers, Sliding Window — **all of them, in order** |
| **LeetCode** | **1** Two Sum · **121** Best Time to Buy and Sell Stock · **238** Product of Array Except Self · **53** Maximum Subarray · **152** Maximum Product Subarray · **560** Subarray Sum Equals K · **128** Longest Consecutive Sequence · **11** Container With Most Water · **15** 3Sum · **209** Minimum Size Subarray Sum · **3** Longest Substring Without Repeating Characters · **424** Longest Repeating Character Replacement · **567** Permutation in String · **76** Minimum Window Substring · **239** Sliding Window Maximum |
| **CSES** | *Introductory Problems* (all 19) and the first half of *Sorting and Searching* |
| **CF EDU** | **Two Pointers Method** — the whole section |
| 🏁 **Capstone** | **LC 42 Trapping Rain Water — solve it three ways** (two-pointer, monotonic stack, prefix arrays) and say which you would write in an interview and why |

**Design (3h/wk):** the estimation module — back-of-envelope arithmetic and the numbers to memorise (§XIV). Then **a URL shortener.**
**Time box:** Easy 15 · Medium 25. **Every miss gets a `FAILURES.md` entry.** **Codeforces: one Div 2 virtual, A–C, in W6.** Target band by W6: **1450 held.**

---
---

# ⚡ LEVEL 1 — ⚙️ C++, Sanitizers & the Threat

> **Goal:** a relay that forwards, cannot be crashed by hostile input, and comes with the apparatus that makes choosing C++ defensible.
> **⏱ Weeks 7–11 · 10-26 → 11-29 · 55h depth** · **Milestone D0** · **🚩 Flagship #1 `hardened`** · **📺 Track C: 15-213 L9–L16 + Attack Lab, Cache Lab · 🔴 6.858 L1 (threat models) in W7**

## 🔥 THE WALL — build it wrong on purpose
Write the dumbest possible relay: accept a TCP connection, read a destination, connect, pipe bytes. Then attack it, five ways:
1. **You can read every byte.** Print the HTTP request. **The relay sees plaintext** — the trust inversion the design exists to remove.
2. **A passive observer on your uplink learns the destination**, because the SNI is in the clear on the first TLS packet. `tcpdump` it.
3. **The relay learns who *and* where.** One node knowing both is what the two-hop split prevents.
4. **Feed the parser 40 bytes of garbage and it crashes.** Now set the destination-length field to `0xFFFFFFFF` and watch it try to allocate 4GB.
5. ⚙️ **Now run it under ASan with a one-byte-overlong length field.** *Heap-buffer-overflow.* **That is a deanonymisation vulnerability with a stack trace.**

**Screenshot all five.** These are the reasons for onion encryption, per-hop encryption, two hops, and every line of the safety apparatus — **in that order** — and having *seen* them means you will explain them rather than recite them.

## 📖 THEORY
**⚙️ Modern C++ for a hostile-input data plane:** `std::span` and `std::string_view` instead of pointer-plus-length, and **the lifetime discipline they demand** · RAII for every resource, no raw owning pointers · `std::unique_ptr`/`shared_ptr` and when `shared_ptr` means your ownership is unclear · move semantics and where copies actually cost · **signed/unsigned and integer-promotion bugs in length arithmetic — the single most common source of parser vulnerabilities** · `std::optional`/`expected` over sentinel returns · why `operator==` on a MAC is a vulnerability and `sodium_memcmp` is not.
**The threat model:** the trilemma choice · **two hops and precisely what each hop knows** (guard: who, not where; exit: where, not who) · split trust and iCloud Private Relay as the consumer-scale proof · **and the discipline of writing down what you concede.**

**📺 Atlas → 15-213 L9–L16** (memory hierarchy, cache, virtual memory, allocation, optimisation, processes) + **Attack Lab** and **Cache Lab**. 🔴 **6.858 L1** in W7.
**📕 Pages:** 🔴 **Das et al., *Anonymity Trilemma* §1–3, §6** — read in W7, skip the proofs first time · Tor design paper §1–4, §6 · Apple's iCloud Private Relay overview · **the C++ Core Guidelines sections on lifetime and bounds** · CS:APP ch. 5 for the optimisation lecture.

> 🤖 **PROMPT 3 (REVIEW)** — on your own parser, W10 · `COMPONENT:` the wire-frame parser · `LANG:` C++20 · `INVARIANT:` no input can cause an out-of-bounds access, an over-allocation, or a crash · `CONSEQUENCE:` a memory bug here is a deanonymisation vulnerability · `CONCURRENCY MODEL:` one thread per connection, no shared state in the parser
> 🤖 **PROMPT 5 (ADVERSARY)** — W9 · `SYSTEM:` a single-hop TCP relay with no encryption beyond the client's own TLS · `PROPERTY:` "the destination does not learn the client's IP" · `CAPABILITIES:` you are the relay operator; separately a passive observer of the client's uplink · `NOT:` you cannot break the client's TLS

## 🛠 🚩 FLAGSHIP #1 `hardened` + MILESTONE D0 · 40h
**⚙️ The apparatus, as a deliverable rather than hygiene:**
- **ASan + UBSan** on every CI run; **TSan** on a separate job; **MSan** optional
- **`-Wall -Wextra -Werror -fno-omit-frame-pointer`**, `-D_GLIBCXX_ASSERTIONS`, `-fstack-protector-strong`
- **`clang-tidy`** with `cppcoreguidelines-*`, `bugprone-*`, `cert-*`
- **libFuzzer on the wire parser, with a committed corpus and a `crash-*` regression directory**
- **RapidCheck** property tests on the codec round-trip
- 🔴 **`docs/cpp-subset.md`** — what you do not use and why: no raw owning pointers in the parsing path, no C arrays, no `reinterpret_cast` on untrusted bytes, no unchecked arithmetic on length fields, `std::span` at every buffer boundary

📈 **EXIT CRITERIA — D0**
- [ ] All five wall attacks reproduced and screenshotted, **each with a written note on which later design decision it justifies**
- [ ] The parser is **total**: **libFuzzer 1 hour clean locally, 60s in CI**, no crash, no OOM, no hang; `0xFFFFFFFF` is rejected, not allocated
- [ ] **ASan, UBSan and TSan all green in CI.** A red sanitizer job blocks merge
- [ ] RapidCheck round-trip on the frame codec; `clang-tidy` clean at the configured level
- [ ] 🔴 **`docs/cpp-subset.md` written**, and a CI grep enforces at least two of its rules mechanically
- [ ] 🔴 **The `hardened` write-up: every memory bug your own fuzzer found in your own parser, with the input, the sanitizer output, and the fix.** *If it found none, your fuzzer is too gentle — add a structure-aware mutator and try again*
- [ ] 🔴 **`docs/threat-model.md` v1** — assets, adversaries, capabilities, the trilemma choice, and an explicit **"what Adyton does not defend against"** section. Revised at every phase boundary, never deleted
- [ ] `README.md` v1 with the honesty statement, scale statement and permitted headline **verbatim** from §IX
- [ ] 15-213 L9–L16 ticked; **Attack Lab and Cache Lab complete**

## 🎤 INTERVIEW PARAGRAPH — Week 11
> I'm building an open privacy relay network. The problem is that no single company sees your whole life, but the trackers, brokers and ISPs together assemble one profile that contains all of it. The product isn't anonymity — it's that your identities can't be linked to each other. Eleven weeks in, what exists is deliberately small: a relay that forwards and cannot be crashed by hostile input. I built the naive version first and attacked it five ways — it reads your plaintext, an observer on my uplink still sees the destination in the TLS SNI, the single node learns both who and where, forty bytes of garbage crashes the parser, and under AddressSanitizer a one-byte-overlong length field is a heap overflow. That last one is the whole language argument: in an anonymity network a memory bug isn't a crash, it's a deanonymisation vulnerability. **Rust gives you that safety by construction. I chose C++ and had to earn it** — sanitizers on every CI run, libFuzzer on the parser with a committed corpus, `std::span` at every buffer boundary, and a documented subset. Three real bugs came out of my own fuzzer and they're written up. That's the position almost every real systems codebase is in, and I'd rather be the engineer who can hold that line than the one who was handed it. The design thesis is the anonymity trilemma from Das et al. 2018 — I take low latency and low overhead, so I explicitly do not defend against a global passive adversary. That's in the README, not a footnote.

## 🎓 EXIT EXAM
1. ⚙️ Name four C++ constructs your subset forbids in the parsing path, and the vulnerability class each prevents.
2. ⚙️ What does ASan catch that your unit tests never will? What does it *not* catch?
3. ⚙️ Your fuzzer has run 48 hours with no crash. What do you conclude and what do you do next?
4. A signed/unsigned confusion in a length field. Show the input that exploits it.
5. State the trilemma and Adyton's corner. Name one adversary you concede and one you defend.
6. Two hops: what does each hop know? What must an adversary own to defeat it?
7. ⚙️ Defend choosing C++ over Rust here to a sceptical interviewer. Then state what Rust would have given you for free.

**Pass = 6/7.** Then 🤖 **PROMPT 2** on "memory safety in a hostile-input parser, and what my tooling does and does not guarantee."
## 🧩 PROBLEM SOLVING — L1 · W7–11 · 32 problems · 5h/wk
**Patterns:** binary search · 🔴 **binary search on the answer** · stack · monotonic stack.
🔗 **The tie:** *binary search on the answer* is the single highest-yield pattern in interviews and **you are using it for real this level** — calibrating a fuzzer's timeout budget and finding the largest input size your parser handles without over-allocating is literally "find the smallest X such that the predicate holds."

| Source | Set |
|---|---|
| **NeetCode 150** | Binary Search, Stack — all |
| **LeetCode** | **704** Binary Search · **33** Search in Rotated Sorted Array · **153** Find Minimum in Rotated Sorted Array · **162** Find Peak Element · **34** Find First and Last Position · 🔴 **875** Koko Eating Bananas · 🔴 **1011** Capacity To Ship Packages · 🔴 **410** Split Array Largest Sum · **1482** Min Days to Make m Bouquets · **4** Median of Two Sorted Arrays · **20** Valid Parentheses · **155** Min Stack · **739** Daily Temperatures · **496**/**503** Next Greater Element I & II · **402** Remove K Digits · **316** Remove Duplicate Letters · **84** Largest Rectangle in Histogram · **85** Maximal Rectangle |
| **CSES** | *Sorting and Searching*, the rest of the section |
| **CF EDU** | **Binary Search** — parts 1 and 2, including the "on the answer" problems |
| 🏁 **Capstone** | **LC 84** and **LC 410** back to back. **If you can derive both from scratch in 60 minutes total, this pattern is yours** |

**Design:** a rate limiter (token bucket, sliding window, and why the naive fixed window is wrong at the boundary).
**Time box:** Medium 25 · Hard 45. **Codeforces: one virtual in W11.**

---
---

# ⚡ LEVEL 2 — Onion Routing

> **Goal:** a constant-size onion packet that leaks nothing about its position on the path, built from the paper.
> **⏱ Weeks 12–19 · 11-30 → 2027-01-24 · 88h depth** · **Milestone D1** · **🚩 Flagship #2 `sphinx`** · **📺 Track C: 15-213 L17–25 + Malloc/Shell/Proxy Labs (W12–16), Boneh Crypto I (W17–19) · 🔴 6.858 L19 (anonymous communication, the Tor paper) in W12** · **W19 = REST WEEK**

## 🔥 THE WALL — two walls, one week apart
**W13, the crypto wall.** Encrypt two different messages with ChaCha20-Poly1305 **using the same key and nonce.** XOR the ciphertexts. **You have recovered the XOR of the plaintexts**, and if you know one you know the other. Do it. See the bytes. Then derive an X25519 shared secret and use it directly as a key — then find out why that is wrong.

**W15, the onion wall.** Layer it the obvious way: encrypt the payload for hop 2, wrap for hop 1, each layer prefixed with the next address. Now stand at hop 1:
1. 🔴 **The packet shrinks as it travels.** Hop 2 receives a smaller packet than hop 1 did. **Its size announces how far along the path it is.**
2. **You can count the layers**, so you know the path length.
3. **Building a circuit costs a round trip per hop** — telescoping — so two hops means two RTTs before a single user byte moves. Measure it against your Oracle RTT.

**Failure 1 is the one that matters. Size is metadata, and metadata is the whole game.**

## 📖 THEORY
**Crypto at using-depth:** X25519 and what a DH shared secret is and is not · **why the raw output must go through a KDF** (it is not uniformly random and has algebraic structure) · small-subgroup attacks and why libsodium's API prevents them for you · AEAD, and **nonce discipline** — the failure you just reproduced, and the two safe strategies · **constant-time comparison** · key zeroization, and why a secret type with a default `Debug`-equivalent is a bug.
**Sphinx** (Danezis & Goldberg): a fixed-size header with a fixed slot count; each hop decrypts its slot **and pads the header back to full size with pseudorandom bytes derived from its own key** — so the packet is byte-identical in length at every hop and a hop cannot tell whether it is first, last or middle. Blinded group elements so each hop derives the next ephemeral key without learning the path. A per-hop MAC over the header, checked **before** acting on it. **Single-pass construction: the client derives every key up front, so no telescoping and no per-hop round trip** — a large part of the startup-latency win over Tor.
**Properties to be able to state:** bitwise unlinkability across hops · no position leakage · no path-length leakage · per-hop integrity · replay detection.

**📺 Atlas → 15-213 L17–25 + Malloc Lab, Shell Lab, Proxy Lab** (W12–16 — 🔴 **Proxy Lab is a concurrent caching web proxy; Adyton's relay is that, hardened**). **Boneh Crypto I weeks 1–4, 6** (W17–19). 🔴 **6.858 L19 in W12 — the one lecture in the Atlas whose subject *is* this project.**
**📕 Pages:** 🔴 **Danezis & Goldberg, *Sphinx* — all of it, three times: once for shape, once for the algorithm, once with your code open** · 🔴 **Lightning BOLT #4** — a *deployed*, precisely-specified Sphinx variant with concrete field sizes, and the clearest engineering description in existence · Aumasson ch. 8, 11, 12 · Boneh & Shoup §5.4, ch. 9 · `tor-spec.txt` §5–6 for the telescoping contrast.

> 🤖 **PROMPT 1** W13 · `GAP:` why raw X25519 output must not be a key, and what HKDF's `info` is for · `CONTEXT:` per-hop keys for a Sphinx header from one ephemeral exchange · `THE DECISION:` whether one DH output can safely produce header key, payload key and blinding factor · `NAMED REAL SYSTEM:` the Noise key schedule, Lightning BOLT #4
> 🤖 **PROMPT 1** W15 · `GAP:` mechanically why a Sphinx header does not leak hop position — what exactly the padding is derived from · `THE DECISION:` how many header slots, and whether unused slots cost me anything observable
> 🤖 **PROMPT 3 (REVIEW)** W17 · `COMPONENT:` Sphinx header construction and per-hop processing · `INVARIANT:` a hop cannot determine its position, and serialised size is identical at every hop · `CONSEQUENCE:` position leakage narrows the anonymity set; a size difference is a passive-observer fingerprint
> 🤖 **PROMPT 5 (ADVERSARY)** W18 · `SYSTEM:` Sphinx packets over a 2-hop circuit · `PROPERTY:` "a relay cannot tell whether it is first or second, and cannot link the packet it received to the one it forwarded" · `CAPABILITIES:` you operate one relay and can observe timing and sizes precisely · `NOT:` you cannot break X25519 or ChaCha20-Poly1305, and you do not see the other hop

## 🛠 🚩 FLAGSHIP #2 + MILESTONE D1 · 60h

📈 **EXIT CRITERIA — D1**
- [ ] 2-hop Sphinx packet built by the client, processed correctly by hop 1 then hop 2, payload recovered
- [ ] 🔴 **RapidCheck: for any routing information within limits, the serialised packet length is byte-identical.** Asserted, not assumed — the flagship's central claim
- [ ] **A hop cannot distinguish its position** — asserted by a test that a hop's observable inputs are statistically identical in position 1 and 2
- [ ] Per-hop MAC verified **before** any action on the header, using `sodium_memcmp`; a flipped bit is rejected at the right hop
- [ ] **Replay detection** with a bounded, time-windowed seen-set, and the memory cost stated
- [ ] **libFuzzer on the header parser: 1h clean locally, 60s in CI. ASan/UBSan/TSan green**
- [ ] ⚙️ Secret key types wrap `sodium_memzero` on destruction, are non-copyable, and **a test asserts no formatter prints key bytes**
- [ ] Circuit build measured: **single-pass vs a telescoping implementation you also write**, so the RTT saving is a number and not a claim
- [ ] `docs/design/packet-format.md` — the wire format with field sizes and the reasoning for each
- [ ] 15-213 **complete: all 25 lectures, all 9 labs ticked.** Boneh weeks 1–4, 6 ticked

⛓ **PROBLEM CHAIN**
```
"Nonce reuse leaked the plaintext"→ nonce discipline → the per-hop key schedule
"Raw DH used as a key"           → HKDF → salt and info → domain separation
"The packet shrank each hop"     → constant size → padding from the hop's own key
"I could count the layers"       → fixed slot count → unused slots must be indistinguishable
"Two RTTs before any data"       → single-pass construction → the latency win over Tor  (→ L12)
"MAC compared with =="           → constant-time compare → sodium_memcmp
"Now how does it reach hop 2?"   → transport → and TCP is the wrong answer              (→ L4)
```

## 🎤 INTERVIEW PARAGRAPH — Week 19
> The packet format is done and it's Sphinx, from the 2009 Danezis and Goldberg paper. I built the obvious onion first, which was the useful part: you encrypt for hop two, wrap it for hop one, and the packet gets *smaller* as it travels — so its size announces how far along the path it is. Size is metadata and metadata is the entire game. Sphinx fixes it by having each hop pad the header back to full length with pseudorandom bytes derived from its own key, so the packet is byte-identical in length at every hop and a relay genuinely cannot tell whether it's first or last. I assert that with a property test over the serialised length rather than trusting it. The other thing Sphinx buys is single-pass construction — the client derives every hop's key up front, so there's no telescoping round trip per hop, and I implemented the telescoping version too so the saving is measured rather than claimed. I also reproduced nonce reuse deliberately: two messages, same key and nonce, XOR the ciphertexts, and the plaintext XOR falls out. Seeing that is why my key schedule has a written argument for nonce uniqueness rather than a hope.

## 🎓 EXIT EXAM
1. You reuse a nonce with the same key. Exactly what does an attacker recover, and how?
2. Why can't raw X25519 output be a symmetric key? What does HKDF's `info` do?
3. Draw the Sphinx header from memory: fields, sizes, what each hop mutates.
4. Mechanically, why does the header not leak hop position? What is the padding derived from?
5. What does single-pass construction save, in RTTs and in milliseconds on your own numbers?
6. Where is the per-hop MAC checked, and what breaks if you check it after acting on the header?
7. Your replay seen-set is bounded. What does the bound leak, and what is the trade?

**Pass = 6/7.** Then 🤖 **PROMPT 2** on "the Sphinx packet format and its security properties."
## 🧩 PROBLEM SOLVING — L2 · W12–19 · 56 problems · 5h/wk
**Patterns:** linked lists · trees and BSTs · tries · heaps and top-K · 🔴 **bit manipulation**.
🔗 **The tie, and it is unusually direct:** you are writing a Sphinx header this level — fixed-width fields, XOR-based blinding, MACs over byte ranges. 🔴 **LC 421 (Maximum XOR of Two Numbers) is a trie over bits, which is structurally the same object as the routing-slot lookup you are building**, and the bit-manipulation set is the vocabulary you need to read the paper's pseudocode without stumbling.

| Source | Set |
|---|---|
| **NeetCode 150** | Linked List, Trees, Tries, Heap/Priority Queue — all |
| **LeetCode — trees** | **104** Max Depth · **110** Balanced · **543** Diameter · **236** LCA · **98** Validate BST · **230** Kth Smallest in BST · **124** Binary Tree Max Path Sum · **297** Serialize and Deserialize Binary Tree |
| **LeetCode — tries** | **208** Implement Trie · **211** Design Add and Search Words · **212** Word Search II · **336** Palindrome Pairs |
| **LeetCode — heaps** | **23** Merge k Sorted Lists · **215** Kth Largest · **295** Find Median from Data Stream · **703** Kth Largest in a Stream · **621** Task Scheduler |
| 🔴 **LeetCode — bits** | **136**/**137** Single Number I & II · **190** Reverse Bits · **191** Number of 1 Bits · **260** Single Number III · **268** Missing Number · **371** Sum of Two Integers · 🔴 **421** Maximum XOR of Two Numbers in an Array |
| **CSES** | *Tree Algorithms* — the first eight |
| 🏁 **Capstone** | **LC 297** (write it, then break your own format with a malformed input — the same instinct as fuzzing the Sphinx parser) and **LC 212** |

**Design:** a distributed cache, then a key-value store. **You are building a bounded replay seen-set this level — use it as your worked example for eviction policy.**
**Time box:** Medium 25 · Hard 45. **Codeforces: one virtual in W16 and W19.** Target band by W19: **1550.**

---
---

# ⚡ LEVEL 3 — Compartments ★

> **Goal:** ★ **the first thing that is real.** One identity, one circuit, one exit, one unmodified Mullvad Browser, bound at the kernel level, with a suite that tries to break the boundary and fails.
> **⏱ Weeks 20–27 · 01-25 → 03-21 · 76h depth** · **Milestone D2** · **🚩 Flagship #3 `leakproof`** · **📺 Track C: Boneh finish (W20–21), 🌙 Ramadan catch-up (W22–26), CS144 prep (W26)** · **🌙 W22–26 at 20h · W26 = REST WEEK (Eid)**
>
> **This is the milestone that makes the project demonstrable.** At the end of Week 27 you can sit someone down and show them two browsers on one laptop that the internet cannot connect to each other. Everything before was necessary; this is the first thing a person can *see*.
>
> 🌙 **Ramadan 1448 ≈ 8 Feb – 9 Mar 2027 = weeks 22–26, at 20h.** Scope is already moved out: Boneh finishes in W21, CS144 does not start until W27, and this level's heavy netns work lands in W20–21 and W27. **W22–26 is the leak suite, which is many small independent tests — the right shape of work for a reduced month.**

## 🔥 THE WALL
Point a normal browser at a SOCKS proxy on your relay. Congratulations, you have a VPN. Now watch it betray you:
1. **WebRTC.** Load a STUN-probing page. **The browser hands out your real local and public IP as ICE candidates**, around the proxy entirely.
2. **IPv6.** Host has IPv6, tunnel is IPv4 — **the browser prefers IPv6 and goes direct.** `tcpdump` it.
3. **DNS.** Your resolver is still your ISP's. **Every destination is logged by name** before a single proxied byte moves.
4. **Kill the relay mid-download.** The browser retries **without the proxy** and your real IP appears on the wire.
5. 🔴 **The fifth, which is the actual product:** run two profiles through the same proxy and check whether a site can tell they are the same person. Cookies, `localStorage`, **TLS session tickets**, HTTP/2 connection coalescing, one shared exit IP. **They can.**

**Screenshot all five.** **Three of the first four are not the proxy's fault** — they are the application declining to use it — which is the whole argument for enforcing the boundary in the kernel rather than asking the application nicely.

## 📖 THEORY
**Linux network namespaces** as the boundary: own interfaces, own routing table, own `/etc/resolv.conf`, own idea of what "the network" is. A process inside cannot route around it because **there is no other route.** **veth pairs** to the tunnel; **nftables default-drop** so the kill switch is structural — if the tunnel dies there is no rule permitting anything. 🔴 **A kill switch implemented as "detect and react" is a race; implemented as default-drop it is an invariant.** **Why per-identity namespaces beat browser containers:** containers isolate cookie jars inside one process that still shares one IP, one resolver and one TLS session cache. **The identity as a sealed unit:** circuit + exit + profile directory + namespace, constructed together or not at all — ⚙️ **make it a type whose constructor takes all four and has no setters**, so a mismatched identity is not a bug you can write. **What the network layer cannot fix:** canvas, WebGL, audio, fonts, window size, hardware values — Mullvad Browser normalises those by *uniformity*, which is exactly why you do not touch it.

**📺 Atlas → Boneh weeks 5, 7** (W20–21). **6.858 L4 (buffer overflow defenses) and L12 (web security model)** are useful here and cheap to pull forward.
**📕 Pages:** Kerrisk *TLPI* ch. 28 (or `namespaces(7)`) · `ip-netns(8)` · the nftables wiki "Quick reference" and "Chains" · **the Mullvad Browser docs** on what it normalises and its statement that it does not hide your IP · 🔴 **the Tor Browser design document, "Cross-Origin Identifier Unlinkability" and "Fingerprinting"** — the most thorough public treatment of browser linkability there is.

> 🤖 **PROMPT 1** W20 · `GAP:` what happens to a socket already open when its namespace's default route is removed · `CONTEXT:` implementing the kill switch as an invariant rather than a reaction · `THE DECISION:` whether default-drop nftables is sufficient or I must also tear the route · `NAMED REAL SYSTEM:` how Mullvad's and Tailscale's Linux kill switches are implemented
> 🤖 **PROMPT 5 (ADVERSARY)** W27, **the one that matters** · `SYSTEM:` two unmodified Mullvad Browser instances, each in its own netns on its own 2-hop circuit with its own pinned exit · `PROPERTY:` "a tracker present on sites visited by both cannot determine they are the same person" · `CAPABILITIES:` you are a tracker on many sites, you see both identities' requests, you control your own JS · `NOT:` you cannot see the user's machine and cannot break TLS

## 🛠 🚩 FLAGSHIP #3 + MILESTONE D2 · 60h

📈 **EXIT CRITERIA — D2 ★**
- [ ] 🔴 **An unmodified Mullvad Browser runs in a netns bound to a 2-hop circuit and you browse the real web through it.** The demo
- [ ] ⚙️ `Identity` **cannot be constructed with a mismatched circuit and namespace** — the constructor takes all four parts and there are no setters. Enforced by the type, not a check
- [ ] Ephemeral identities: profile wiped on close, verified by test
- [ ] Named persistent identities with **exits pinned stably across restarts**, verified against an IP-echo endpoint
- [ ] `adyton identity launch shopping` — **one command** creates the namespace, builds the circuit, starts the browser
- [ ] 🔴 **`leakproof` in CI, all five tests, red build blocks merge:** **WebRTC** — zero ICE candidates with a non-namespace address · **IPv6** — no IPv6 packet leaves the host attributable to the identity · **DNS** — zero DNS queries on the host uplink during a browse session · **kill switch** — daemon killed mid-transfer, **zero subsequent packets, 20 runs, 20 passes** · **cross-compartment** — two identities share no exit IP, no cookie, no DNS query, **no TLS session ticket**, and produce **identical CreepJS results**
- [ ] **Fingerprint uniformity across two machines**: identical CreepJS output. Any difference is a bug in your launcher
- [ ] 🔴 **`docs/browser-delta.md`** — everything you changed about the browser. **If it is longer than "profile directory path and SOCKS endpoint," justify every entry or remove it**
- [ ] Boneh Crypto I **complete: all 7 weeks ticked**
- [ ] 🔴 **W26: CS144 handouts and starter repo downloaded and committed to a private mirror** (§VII warning)
- [ ] **Blog post 1:** *"Your proxy leaks four ways and three of them aren't the proxy's fault"*

⛓ **PROBLEM CHAIN**
```
"WebRTC gave up my real IP"  → the app routes around the proxy → kernel-level binding
"IPv6 went direct"           → dual-stack → drop or tunnel, never ignore
"DNS went to my ISP"         → resolve at the far end → the compartment has its own resolver
"Kill switch was a race"     → default-drop nftables → an invariant, not a reaction
"Two profiles were linkable" → shared exit, cookies, TLS tickets → separate everything
"The type let me mismatch"   → make the invalid state unconstructible                (→ L10)
"Which exit does it pin to?" → you need a peer list → everyone must see the same one  (→ L5, L6)
```

## 🎤 INTERVIEW PARAGRAPH — Week 27
> This is the month it became real: two browsers on one laptop that the internet cannot connect to each other. But the useful part is what I found first. I pointed a normal browser at a SOCKS proxy on my relay — essentially a VPN — and it betrayed me four ways: WebRTC handed out my real IP as an ICE candidate straight around the proxy, IPv6 went direct because the host was dual-stack, DNS still went to my ISP so every destination was logged by name before a single proxied byte moved, and killing the relay made the browser retry without it. **Three of those four are not the proxy's fault** — they're the application declining to use it — which is the entire argument for enforcing the boundary in the kernel. So each identity is a Linux network namespace with its own routing table and resolver, a veth to the tunnel, and nftables default-drop, which makes the kill switch an invariant rather than a race: if the tunnel dies there's simply no rule permitting anything.
>
> The fifth failure is the product. Two profiles through one proxy are still linkable — shared exit IP, shared cookie jar, and the one I didn't expect, **shared TLS session tickets.** So compartments are one unmodified Mullvad Browser profile per identity, each in its own namespace on its own circuit with its own pinned exit. The suite that tries to break that runs in CI and its going red is the alarm, because one leak across compartments defeats the entire product. And I deliberately change almost nothing about the browser — the profile path and the SOCKS endpoint, and that list is a document — because every customisation makes my users distinguishable from the crowd they're hiding in.

## 🎓 EXIT EXAM
1. Name four ways a browser escapes a SOCKS proxy. Which are the proxy's fault?
2. Why is a network namespace a stronger boundary than a browser container? Be specific about what each isolates.
3. Why is default-drop a better kill switch than detect-and-react? Give the race in the second design.
4. What happens to an already-open socket when its namespace's route is removed? How did you verify?
5. Two identities, one exit IP. Name four separate mechanisms that link them.
6. Why must you not modify Mullvad Browser? What does each modification cost, and to whom?
7. ⚙️ Your `Identity` type prevents a mismatch. How, and why is a runtime check insufficient?

**Pass = 6/7.** Then 🤖 **PROMPT 2** on "compartment isolation and browser linkability."
## 🧩 PROBLEM SOLVING — L3 · W20–27 · 44 problems · 5h/wk (🌙 3.5h W22–25)
**Patterns:** 🔴 **dynamic programming, part 1** — 1-D, 2-D, knapsack · greedy · graph traversal intro.
🔴 **The method, used every single time, no exceptions:** state the subproblem **in words** · write the recurrence **in a comment** · identify the base cases · *then* choose memoised recursion or a bottom-up table · optimise space last. **Do not write code before the recurrence exists in a comment.** That habit is the difference between solving DP and guessing at it, and interviewers can see which one you are doing.

| Source | Set |
|---|---|
| **NeetCode 150** | 1-D DP and 2-D DP — all |
| **LeetCode — 1-D** | **70** Climbing Stairs · **198**/**213** House Robber I & II · **91** Decode Ways · **139** Word Break · **322** Coin Change · **518** Coin Change II · **300** Longest Increasing Subsequence · **152** revisit |
| **LeetCode — 2-D** | **1143** LCS · 🔴 **72** Edit Distance · **62** Unique Paths · **64** Minimum Path Sum · **221** Maximal Square · **5** Longest Palindromic Substring · **647** Palindromic Substrings |
| **LeetCode — knapsack** | **416** Partition Equal Subset Sum · **494** Target Sum · **474** Ones and Zeroes · **1049** Last Stone Weight II |
| **LeetCode — graphs (intro)** | **200** Number of Islands · **133** Clone Graph · **207**/**210** Course Schedule I & II · **417** Pacific Atlantic · **130** Surrounded Regions · **695** Max Area of Island · **994** Rotting Oranges · **542** 01 Matrix |
| 🔴 **AtCoder** | **Educational DP Contest, problems A–L** — `atcoder.jp/contests/dp`. **The best structured DP resource that exists, and it is free** |
| **CSES** | *Dynamic Programming* — the first ten |
| 🏁 **Capstone** | **LC 72 Edit Distance from memory**, recurrence first, then the space-optimised version |

🌙 **W22–25 (Ramadan, 3.5h):** **no new topics. Re-solve every DP failure from the log, and work AtCoder DP A–L slowly.** DP is the one topic that rewards slow careful weeks, so this collision is better luck than it looks.
**Design:** a multi-tenant API with quotas, then identity/auth. **W26: failure-category count — the first one that will actually redirect you.**

---
---

# ⚡ LEVEL 4 — Transport & Fingerprints

> **Goal:** per-hop QUIC that removes Tor's head-of-line blocking — and a handshake that does not announce which network you belong to.
> **⏱ Weeks 28–35 · 03-22 → 05-16 · 80h depth** · **Milestone D3** · **📺 Track C: 🔴 Stanford CS144, complete (W27–38)** · **W34 = buffer · W36 = Eid, 26h**

## 🔥 THE WALL
Multiplex two independent circuits over **one TCP connection** between two of your relays — which is what Tor does, one TCP connection per relay pair carrying every circuit between them. Now `tc netem loss 2%` on that link and drive both.

**Both circuits stall together.** Circuit A loses a segment; TCP will not deliver *anything* after it until the retransmission arrives — so circuit B, which lost nothing, belongs to a different user, and is doing fine, freezes too. **Measure circuit B's p99 with and without circuit A's loss.**

🔴 **That is head-of-line blocking across unrelated users, and it is the single biggest structural reason Tor feels slow. Screenshot the two p99s side by side. This chart goes in the README and it is the strongest argument in the entire project.**

## 📖 THEORY
**TCP's in-order guarantee is the problem**: one byte stream, one loss stalls everything behind it. **QUIC gives independent streams over one connection**, so circuit streams map onto QUIC streams and loss is recovered on the hop where it happened. **Per-hop, not end-to-end** — each relay-to-relay link its own QUIC connection with its own congestion control, so a lossy last mile does not degrade the whole path. **Nested congestion control** — know what it does and what per-hop avoids. **QUIC datagrams (RFC 9221)** where unreliable delivery is wanted.
🔴 **QUIC has a fingerprint.** Connection ID length, version, transport parameters **and their order**, ALPN, initial packet layout, and the TLS ClientHello inside it. **If every Adyton peer's handshake is identical to each other and different from everyone else's, your network's membership list is public** — a spectacular own goal for a privacy system and exactly the mistake a naive implementation makes.

**📺 Atlas → 🔴 Stanford CS144, all eight checkpoints (W27–38).** You build a working TCP in C++: byte stream → reassembler → receiver → **sender (the hardest)** → full connection replacing the kernel's socket → ARP network interface → IP router → end-to-end. **Do not skip to QUIC without this** — QUIC's design decisions are all reactions to TCP's and are incomprehensible until you have implemented the thing being reacted to. Also **15-213 L19–L20 (network programming)** if not already ticked.
**📕 Pages:** RFC 9000 §2, §5, §12–13, §17; skim §7 · RFC 9221 in full · Peterson & Davie §6.3 · Fall & Stevens ch. 13–15 · **the `ngtcp2` API docs and every field of its settings/transport-params structs — each one is a fingerprint bit.**

> 🤖 **PROMPT 1** W29 · `PREREQ:` I implemented TCP in CS144, including retransmission and windows · `GAP:` exactly which QUIC handshake fields are attacker-observable and which are negotiated in the clear · `CONTEXT:` normalising Adyton's handshake so peers are not identifiable by it · `THE DECISION:` which transport parameters I must pin, and whether their *order on the wire* is observable · `NAMED REAL SYSTEM:` how uTLS fingerprints TLS ClientHellos, and the QUIC-level equivalents
> 🤖 **PROMPT 5 (ADVERSARY)** W33 · `SYSTEM:` Adyton peers connecting over QUIC via ngtcp2 · `PROPERTY:` "an observer cannot tell this connection belongs to the Adyton network" · `CAPABILITIES:` a passive ISP observer with full captures of many users · `NOT:` you cannot decrypt QUIC payloads

📈 **EXIT CRITERIA — D3**
- [ ] 🔴 **The head-of-line-blocking chart** — circuit B's p99 under circuit A's loss, TCP-multiplexed vs per-hop QUIC
- [ ] Per-hop QUIC via **ngtcp2 + BoringSSL**; circuit streams map to QUIC streams; a 2-hop circuit carries a real HTTP request to a gateway
- [ ] 🔴 **Fingerprint normalisation: a capture diff of two peers' handshakes is byte-identical except the random bits.** Verified by a script, **and the script runs in CI**
- [ ] Connection ID length, version, ALPN and every transport parameter are fixed constants **with a comment saying why**
- [ ] Circuit teardown releases every thread, stream and key — **100 build/teardown cycles leave no residual resources** (verified under ASan and with an fd-count assertion)
- [ ] Every failure path typed and tested: guard unreachable, middle unreachable, handshake rejected, timeout mid-build. **No crashes; ASan/UBSan/TSan green**
- [ ] Circuit build p50 **<250ms**; TTFB overhead vs direct **<120ms p50**; sustained single-stream **>15 Mbit/s**
- [ ] 🔴 **CS144 complete: all eight checkpoints ticked, your TCP interoperates with the real internet**

⛓ **PROBLEM CHAIN**
```
"Circuit B stalled on A's loss" → TCP in-order delivery → QUIC streams → THE headline chart
"Loss on one hop hurt all hops" → per-hop connections → independent congestion control
"All my handshakes looked alike"→ QUIC fingerprint → pin every parameter → verify by diff
"Nested congestion control"     → what per-hop avoids, and what it still cannot
"Now who do I connect TO?"      → peer discovery → gossip                            (→ L5)
```

## 🎤 INTERVIEW PARAGRAPH — Week 35
> The transport is the part I'd lead with, because it's a structural fix rather than a tuning one. Tor multiplexes every circuit between two relays over a single TCP connection, and TCP guarantees in-order delivery — so when one circuit loses a segment, TCP won't deliver anything behind it and every *other* circuit on that link freezes too. Different users, unrelated traffic, all stalled. I reproduced it with `tc netem` at two percent loss and measured an innocent circuit's p99 with and without a neighbour's loss; that chart is the strongest argument in the project. The fix is per-hop QUIC — each relay-to-relay link is its own QUIC connection, circuit streams map onto QUIC streams, so loss is recovered where it happened and doesn't cross circuits. **I built a TCP from scratch first, in Stanford's CS144, all eight checkpoints including the sender and the router** — which is why I can explain *why* QUIC made each choice instead of repeating that it's better. The subtler thing I found is that QUIC has a fingerprint — connection ID length, version, transport parameters, ALPN — and a naive implementation makes every peer's handshake identical to each other and distinct from everyone else's, which publishes your network's membership list. So every parameter is pinned and CI diffs two peers' captures to prove they're byte-identical apart from the random bits.

## 🎓 EXIT EXAM
1. Explain head-of-line blocking across circuits with a concrete loss sequence. Give your own two p99 numbers.
2. What does QUIC give you that TCP cannot, and what does it cost?
3. Name six observable fields in a QUIC handshake. Which are negotiated in the clear?
4. Per-hop vs one end-to-end session: what does each concede?
5. Nested congestion control: what goes wrong, and what does your design do about it?
6. When would you want a QUIC datagram instead of a stream in Adyton?
7. From CS144: your TCP sender's retransmission timer. Walk through backoff on repeated loss.

**Pass = 6/7.** Then 🤖 **PROMPT 2** on "QUIC, per-hop transport, and transport fingerprinting."
## 🧩 PROBLEM SOLVING — L4 · W28–35 · 46 problems · 5h/wk
**Patterns:** 🔴 **graphs proper** — BFS/DFS on state, topological sort, **Dijkstra, Bellman–Ford, shortest path with constraints**.
🔗 **The tie, and it is the strongest in the plan:** you are building an IP router in CS144 checkpoint 6 *this level*, and in Level 9 you will build a **constrained multi-criteria path selector** for Adyton. 🔴 **LC 787 (Cheapest Flights Within K Stops) IS Adyton's selector in miniature** — shortest path with a hop constraint — and **LC 1631 (Path With Minimum Effort)** is the same shape with a different objective. When an interviewer asks a shortest-path question you will have a real system to point at.

| Source | Set |
|---|---|
| **NeetCode 150 / 250** | Graphs and Advanced Graphs — all |
| **LeetCode — shortest paths** | **743** Network Delay Time · 🔴 **787** Cheapest Flights Within K Stops · 🔴 **1631** Path With Minimum Effort · **778** Swim in Rising Water · **1976** Number of Ways to Arrive at Destination · **1129** Shortest Path with Alternating Colors · **847** Shortest Path Visiting All Nodes · **864** Shortest Path to Get All Keys |
| **LeetCode — topological** | **210** revisit · **269** Alien Dictionary · **310** Minimum Height Trees · **802** Find Eventual Safe States · **2115** Find All Possible Recipes · **332** Reconstruct Itinerary |
| **LeetCode — bipartite/colouring** | **785** Is Graph Bipartite? · **886** Possible Bipartition |
| **CSES** | 🔴 ***Graph Algorithms* — the whole section's first fifteen.** CSES's graph set is harder and cleaner than LeetCode's and it is the right difficulty for you now |
| **CF** | Problemset, tag `graphs` + `shortest paths`, rating **1500–1700**, 12 problems |
| 🏁 **Capstone** | **LC 787 three ways** — Bellman–Ford, Dijkstra with state `(node, stops)`, and BFS by level. **Then explain which one Adyton's selector resembles and why** |

**Design:** a chat/messaging system, then notification fanout. **Codeforces: one virtual in W31 and W35.** Target band by W35: **1650.**

---
---

# ⚡ LEVEL 5 — The Mesh

> **Goal:** peers find each other with no directory, across home routers, and detect each other's death without a central watcher — while laptops sleep and wifi drops.
> **⏱ Weeks 36–43 · 05-17 → 07-11 · 76h depth** · **Milestone D4** · **🚩 Flagship #4 `meshsim`** · **📺 Track C: CS144 finish (W36–38), 🔴 MIT 6.5840 begins (W39)** · **W36 = Eid, 26h · W43 = REST WEEK**
>
> **AWS free tier: sign up in Week 36** — twelve months from here covers W36–88, exactly when you need multi-region nodes. **Billing alarm at $5 before any resource.**

## 🔥 THE WALL
Run `adyton-node` on your workstation in Cairo. Run another on a second network. Give each the other's IP. **They cannot connect, in either direction.** Both behind NAT, neither routable. **This is the actual, physical reason peer-to-peer software needs traversal infrastructure**, and it is invisible until you hit it. Now do it with the Oracle box as rendezvous, watch hole punching work — **then find the NAT type where it still does not** and fall back to relay.
```bash
tcpdump -i any -nn 'udp port 3478'   # the STUN exchange
# ask TWO different rendezvous servers for your external ip:port.
# If they disagree, you are behind symmetric NAT and punching will not work.
```

## 📖 THEORY
**NAT types:** full-cone, restricted-cone, port-restricted, **symmetric**. Punching works for the first three and **fails for symmetric**, which is why every real P2P system has a relay fallback. **Measure what fraction of your peer pairs need it** — that fraction is a real cost. **SWIM membership:** each node pings one random peer per period; on failure asks *k* others to probe on its behalf (**indirect probing is what makes it robust to one bad link**); updates piggyback on the ping traffic. **O(N) per node per period regardless of mesh size.** **Phi-accrual failure detection:** a *suspicion level* from the distribution of recent inter-arrival times, rather than a binary verdict on a fixed timeout — adapts to a peer on a bad link instead of flapping. **Suspicion and incarnation numbers:** how a node refutes a false death rumour with no authority to appeal to — what stops a 2-second suspend from evicting a healthy peer. 🔴 **The nastiest fault: the asymmetric partition.** A's packets reach B, B's do not reach A. **Every naive liveness check produces a permanently inconsistent view.** This is the shape of how split-brain actually happens.

**📺 Atlas → CS144 checkpoints 6–7** (W36–38). **6.5840 L1–L3 (Introduction/MapReduce, RPC and Threads, GFS)** from W39 — 🔴 **GFS matters more than it looks: the canonical system whose entire design is shaped by "components fail constantly and that is normal," which is your posture toward churn.** **6.5840 Lab 1 (MapReduce) starts W40.**
**📕 Pages:** 🔴 **SWIM paper, in full** — short and unusually clear · **φ Accrual paper** · 🔴 **DDIA ch. 8 in full** — partial failure, unreliable networks and clocks, **and why you cannot distinguish "slow" from "dead."** The theoretical spine of everything from here · RFC 4787 §4 · RFC 8445 §2 · HashiCorp's Serf Lifeguard docs — a production system's honest account of where the SWIM paper needed fixing.

> 🤖 **PROMPT 1** W38 · `GAP:` why symmetric NAT defeats punching, in terms of actual mapping behaviour · `THE DECISION:` attempt punching always and fall back, or detect NAT type first · `NAMED REAL SYSTEM:` how Tailscale's DERP fallback decides, and `pion/ice`'s default
> 🤖 **PROMPT 1** W40 · `GAP:` how incarnation numbers let a node refute a false death rumour without an authority · `CONTEXT:` a mesh where a laptop's 2-second suspend must not evict it permanently · `THE DECISION:` the suspicion timeout that recovers a sleeping laptop without letting a dead peer linger

## 🛠 🚩 FLAGSHIP #4 `meshsim` + MILESTONE D4 · 60h
**`meshsim` is what makes Levels 8, 9 and 11 possible.** Every source of nondeterminism injectable and driven by one seeded PRNG: clock · network (delay, drop, reorder, **asymmetric partition**) · peer lifecycle (join, sleep, vanish, **throttle to LTE bandwidth**) · and the Adyton-specific fault — **a peer that lies about its capacity, or behaves well only when it detects it is being probed.**

📈 **EXIT CRITERIA — D4**
- [ ] 🔴 **Two peers behind different NATs discover each other and exchange a circuit.** If your connection is symmetric-NAT, demonstrate relay fallback and **document which it was** — a real finding, not a failure
- [ ] **Fraction of peer pairs requiring relay, measured** on your actual conditions; **NAT direct-connection success >80%** across the type matrix
- [ ] A peer joining a 30-node mesh is known to all others **within a bounded number of gossip rounds — measured and plotted against mesh size**
- [ ] Membership traffic per node **flat as the mesh grows** — the chart, beside the naive O(N²) curve and its extrapolation to 1,000 peers
- [ ] 🔴 **Phi-accrual vs fixed timeout: false-positive rate and detection latency, both, as a chart**, under `tc netem delay 50ms 30ms distribution normal`
- [ ] **A 2-second suspend does not evict a healthy peer** — suspicion plus incarnation numbers, asserted
- [ ] 🔴 **The asymmetric-partition test.** The mesh converges to a consistent view, **or you document exactly why it cannot and what you do instead**
- [ ] **Circuit recovery under churn: p50 <800ms, p99 <3s** at 20% of peers churning per five-minute window
- [ ] **Graceful drain:** a peer switched off signals circuits to migrate rather than break. **Zero circuits broken**
- [ ] `meshsim`: **1,000 seeds nightly in CI**, any failure reproducible from a seed integer
- [ ] Terraform provisioning free-tier nodes in ≥3 real regions; **$0.00 verified**; **AWS signed up W36 with a tested $5 alarm**
- [ ] **6.5840 L1–L3 ticked; Lab 1 (MapReduce) complete**

## 🎤 INTERVIEW PARAGRAPH — Week 43
> The mesh exists and two things surprised me. Peer-to-peer is *physically* hard before it is algorithmically hard: two nodes behind home routers cannot connect in either direction, so I implemented STUN-style hole punching with a rendezvous server plus a relay fallback, because punching simply does not work behind symmetric NAT — and I measured what fraction of my peer pairs need the relay, because that is a real cost. Then membership. I started with everyone pinging everyone, fine at thirty nodes and O(N²) — I plotted it and extrapolated to a thousand peers, where every node spends its CPU on membership instead of forwarding. So it's SWIM: ping one random peer per period, ask k others to probe indirectly on failure, piggyback membership updates on the ping traffic so dissemination is free. Traffic per node is flat as the mesh grows and I have the chart. The failure detector is phi-accrual rather than a fixed timeout, chosen after measuring false-positive rates under injected jitter, because a fixed timeout flaps badly on a home connection. And the fault that taught me most is the asymmetric partition — A's packets reach B but B's don't reach A — where a naive liveness check gives a permanently inconsistent view of who's alive. That's the shape of how split-brain actually happens, and it's what pushed me into the next level, because in *this* system two clients disagreeing about the peer list turns out not to be a correctness bug but a privacy bug.

## 🎓 EXIT EXAM
1. Four NAT types. Which defeats punching, and what do you do instead? What fraction of your pairs needed it?
2. Why is SWIM O(N) per node when naive membership is O(N²)? What does indirect probing buy?
3. Fixed timeout vs phi-accrual: the failure mode of each, and the metric that distinguishes them.
4. A laptop suspends two seconds. What prevents eviction, and how does the peer refute it?
5. Asymmetric partition: what does each side believe? What can you actually do?
6. You cannot distinguish slow from dead. State the consequence for circuit migration.
7. Why is a peer's self-reported bandwidth worthless, and what do you do instead?

**Pass = 6/7.** Then 🤖 **PROMPT 2** on "membership, failure detection and churn."
## 🧩 PROBLEM SOLVING — L5 · W36–43 · 46 problems · 5h/wk
**Patterns:** 🔴 **union-find** · minimum spanning trees · **design problems** · reductions and NP-hardness.
🔗 **The tie:** union-find *is* the connected-components question you are asking about your own mesh — "after this partition, which peers can still reach each other?" — and **W37 is a proving week: three written reductions from Skiena ch. 9.** Being able to say *"this scheduling problem is NP-hard by reduction from 3-SAT, so I used a heuristic and measured how far off optimum it lands"* is a senior answer and it comes up in real design rounds.

| Source | Set |
|---|---|
| **LeetCode — DSU** | **547** Number of Provinces · **684**/**685** Redundant Connection I & II · **721** Accounts Merge · **990** Satisfiability of Equality Equations · 🔴 **1697** Checking Existence of Edge Length Limited Paths · **305** Number of Islands II · **803** Bricks Falling When Hit |
| **LeetCode — MST** | **1584** Min Cost to Connect All Points · **1135** Connecting Cities With Minimum Cost · **1489** Critical and Pseudo-Critical Edges in MST |
| 🔴 **LeetCode — design** | **146** LRU Cache · 🔴 **460** LFU Cache · **355** Design Twitter · **588** Design In-Memory File System · **981** Time Based Key-Value Store · **1146** Snapshot Array · **359** Logger Rate Limiter · **1352** Product of the Last K Numbers · **1206** Design Skiplist · **622**/**641** Design Circular Queue & Deque |
| **CSES** | *Graph Algorithms* — the rest, plus *Range Queries* first five |
| **CF EDU** | 🔴 **Disjoint Sets Union** — parts 1 and 2, complete |
| **Skiena** | **Ch. 9** (intractability). **Write three reductions out longhand in W37** |
| 🏁 **Capstone** | **LC 460 LFU Cache** — write it with O(1) get and put, from scratch, twice, a week apart. **It is the design problem most likely to appear and most likely to be fumbled** |

**Design:** service discovery, then a distributed rate limiter. 🔴 **You are building SWIM membership this level — use it as your worked example in the service-discovery design.**
**W41: first human mock, plus the Raft Figure 8 whiteboard test.** **Codeforces: virtuals W39, W43.**

---
---

# ⚡ LEVEL 6 — ☕ The Directory

> **Goal:** every client sees the same view of the mesh — because **if two clients see different peer sets, that difference is itself a fingerprint that distinguishes them.**
> **⏱ Weeks 44–52 · 07-12 → 09-12 · 88h depth** · **Milestone D5** · **🚩 Flagship #5 `raft-dir`** · **📺 Track C: 🔴 MIT 6.5840, complete — L4–L22 and Labs 2–5** · **W52 = buffer** · **⚑ CV v3 at W50**
>
> **☕ The Java level, and Java is 52.7% of your target backend postings — the single most-demanded skill in your corpus, above AWS.** A directory service is stateful, consensus-backed, multi-tenant, and serves verified documents to many readers: precisely what the JVM ecosystem is best at.
>
> 🔴 **This is where 6.5840 does the real work — and the sequencing is deliberate. You implement Raft in Go for Lab 3 (W45–47), then implement it again in Java as Adyton's directory (W48–52). The second implementation is where the understanding shows**, and being able to say *"I implemented Raft twice, in two languages, and here is what I did differently the second time"* is a genuinely unusual thing to be able to say.

## 🔥 THE WALL
Let each client build its own peer list from gossip — the design Level 5 leaves you with. Instrument two clients and diff their views. **They differ.** Different join times, gossip paths, peers still suspected. Now ask the question that makes this a privacy problem: **a website sees a circuit through peers X and Y. How many Adyton users could have built that circuit?**

If every client has a slightly different peer list, **the set of clients whose view contained both X and Y may be very small — sometimes one.** Your path selection has become a fingerprint. **Measure it in `meshsim`: with 30 peers and divergent views, compute the anonymity-set size of an observed circuit.**

## 📖 THEORY
**Why not consensus among all peers:** a single Raft group across thousands of churning home machines is absurd. **Adyton runs consensus among a small authority set and disseminates a signed document to everyone else** — the ZooKeeper shape, and what Tor does with nine directory authorities. **Epoch documents:** a signed, versioned snapshot — peer list, measured capacities, epoch number, validity window, signature. Clients verify and use *only* the current epoch, so **all clients on epoch N have the same view by construction.** **Raft in full:** terms · randomised election timeouts and why randomisation is load-bearing · the up-to-date-log check · AppendEntries · **the log matching property** · commit index advancement · membership changes. 🔴 **The Figure 8 case** — why a leader may not directly commit an entry from a *previous* term. **The subtle part, what interviewers probe, and you must be able to draw it.** **ReadIndex / lease reads** — linearizable reads without a log write, which matters because the directory is read constantly and written rarely.
🔴 **FORK CONSISTENCY — the concept that reframes this level.** A compromised authority set can serve *different* epoch documents to different clients — a **fork attack** — recreating the fingerprint you just eliminated, deliberately. Fork consistency says the attacker can fork the views but **cannot keep the fork hidden forever.** The defences: **hash-chaining the epoch documents** so a fork is a visible branch, and **gossiping observed epoch hashes between clients** so two clients comparing notes detect a fork immediately. Certificate Transparency's idea applied to a mesh directory.
**Measurement without trust:** a peer's claimed bandwidth cannot be believed. Active probing from multiple vantage points, and resistance to peers that behave well only when probed. Prior art: Tor's `sbws`.
☕ **Java 21 for this:** records and sealed interfaces for the document types · **virtual threads** for the read-serving path (thousands of clients polling for the current epoch is exactly Loom's case) · and 🔴 **a GC pause in a consensus leader looks exactly like a network partition to its followers.**

**📺 Atlas → 🔴 6.5840, the rest of the course:** **L4 Paxos** (W44 — ADR-0004 requires you to have understood it, not dismissed it) · **L6, L7 Raft (1) and (2)** (W44–45) · **L8 Consistency and Linearizability** (W46 — ADR-0005) · **L9 Zookeeper** (W47 — 🔴 Adyton's exact shape) · **L13 Chain Replication** (W48 — the second alternative) · 🔴 **L19 Fork Consistency, SUNDR (W49 — the most important lecture in the Atlas for this project)** · **L21 Byzantine Fault Tolerance** (W51 — so Level 10's "I didn't need PBFT" is credible) · plus L11, L12, L14–L18, L20 in the weekday slots. **Labs 2, 3 (Raft), 4 (KV on Raft) and 5 (sharded KV) — all four.**
**📕 Pages:** 🔴 **Raft extended paper §5 in full, §6 carefully** — the conference version omits crucial detail · 🔴 **Gjengset, "Students' Guide to Raft"** — read *before* you start, not when stuck · 🔴 **Mahajan et al., SUNDR §2–4** · Laurie, "Certificate Transparency" (CACM 2014) · DDIA ch. 9 in full · **Jepsen's consistency model map** — memorise the hierarchy · Kleppmann "How to do distributed locking" **and** antirez's reply · Goetz *JCiP* ch. 3, 5, 11 · JEP 444 · Shipilëv's "JVM Anatomy Quarks" on allocation and GC.

> 🤖 **PROMPT 1** W45 · `PREREQ:` I watched 6.5840 L6–L7 and read the extended paper, and Lab 3 passes · `GAP:` the Figure 8 scenario — why a leader cannot directly commit an entry from a previous term · `THE DECISION:` whether the no-op-on-election fix is sufficient · `NAMED REAL SYSTEM:` etcd's implementation
> 🤖 **PROMPT 4 (BRIDGE)** W49, **the important one** · `SOURCE A:` Raft gives me linearizable consensus among the authorities · `SOURCE B:` SUNDR shows a malicious server can still fork clients' views of a consistent log · `DECISION:` what Raft actually buys my *clients*, and what I must add — hash chaining, client gossip, or both
> 🤖 **PROMPT 5 (ADVERSARY)** W50 · `SYSTEM:` 5 Raft authorities publishing signed, hash-chained epoch documents; clients verify and use only the current epoch · `PROPERTY:` "all clients see the same peer set per epoch, so a circuit does not narrow the anonymity set" · `CAPABILITIES:` you have compromised 3 of the 5 authorities and you also operate a website users visit · `NOT:` you cannot forge the 2 honest signatures

📈 **EXIT CRITERIA — D5**
- [ ] Leader elected from 5 authorities; re-elected within the timeout after a kill; **no split-brain across 1,000 randomised runs**
- [ ] **Partition test: a minority partition CANNOT commit, across 500 randomised schedules.** On heal, uncommitted minority entries are correctly overwritten
- [ ] 🔴 **The Figure 8 scenario constructed deliberately as a test**, and the commit rule shown to prevent it. **You can draw it at a whiteboard in five minutes from memory.** Tested by a human
- [ ] ReadIndex or lease reads; **linearizable reads without a log write**, latency difference measured
- [ ] Epoch document signed, versioned, **hash-chained to its predecessor**; clients reject a document whose chain does not extend the one they hold
- [ ] 🔴 **THE HARD ONE: 100% of peers hold the same epoch-N consensus hash within 30s of epoch close, under 20% churn.** An assertion, not a metric
- [ ] 🔴 **Fork detection:** clients gossip observed epoch hashes; **a simulated fork (3 compromised authorities, two documents) is detected within N epochs — and you report N**
- [ ] 🔴 **Anonymity-set measurement:** for an observed circuit, the number of clients whose view contained both hops, **before and after epoch documents.** The number that proves why this level exists
- [ ] Capacity from **measured** probing at ≥3 vantage points, **within 20% of ground truth**; self-reports never read. **A peer reporting 10× its capacity, and one performing well only when probed, are both down-weighted** — asserted in `meshsim`
- [ ] **A GC pause on the leader is distinguished from a partition — or documented as indistinguishable**, which is the honest answer, with the consequence stated
- [ ] `docs/design/consistency.md` + **ADR-0004 (Paxos vs Raft vs Chain Replication)** and **ADR-0005 (consistency model)**
- [ ] 🔴 **6.5840 complete: all 22 lectures, all 5 labs ticked** — including the sharded fault-tolerant KV store
- [ ] **CV v3 at W50. Blog post 2:** *"In a privacy network, disagreeing about the peer list is a privacy bug"*

## 🎤 INTERVIEW PARAGRAPH — Week 52 (and CV v3)
> This is the level I'd most want to be asked about, because the requirement looks like performance and is actually privacy. My peers gossip, so each client builds its own view of the mesh — and when I diffed two clients' views they differed. Harmless, until you ask: a website observes a circuit through peers X and Y; how many Adyton users could have built it? If every client's peer list is slightly different, **the set of clients whose view contained both can be tiny — sometimes one.** Divergence in the peer list is a fingerprint. So the directory publishes signed epoch documents and every client uses only the current epoch, which makes their views identical by construction. Consensus runs among five authorities rather than across all peers, which is the ZooKeeper shape and also what Tor does. **I implemented Raft twice — first in Go for MIT 6.5840's Lab 3, then in Java as this directory — and the second implementation is where the understanding showed**; the part that took longest both times was Figure 8, the case where a leader must not directly commit an entry from a previous term, which I built as a deliberate test rather than waiting to hit it.
>
> But the thing I'm proudest of came from a lecture I nearly skipped. Raft gives me agreement *among the authorities*. It does not stop a compromised authority set serving **two different epoch documents to two sets of clients** — a fork attack — which recreates the exact fingerprint I'd just eliminated, on purpose. That's fork consistency, and SUNDR works it out: an attacker can fork the views but cannot keep the fork hidden, because once forked the two client sets can never be reconciled without the divergence becoming visible. So epoch documents are hash-chained and clients gossip the hashes they've seen — Certificate Transparency's idea applied to a mesh directory. I simulated three compromised authorities and I can tell you how many epochs it takes to detect.

## 🎓 EXIT EXAM
1. Why is a divergent peer list a privacy bug and not just a correctness bug? Give your own anonymity-set numbers.
2. Draw Raft's Figure 2 from memory. Then Figure 8, and the rule that fixes it.
3. Why consensus among a small authority set rather than all peers? What does it concede, and who else does it this way?
4. Why is randomising the election timeout load-bearing rather than a detail?
5. Raft gives agreement among authorities. **What attack does it not prevent, and what did you add?**
6. Define fork consistency. What is the bound, and what mechanism enforces it?
7. A peer performs well only when it detects a probe. How do you catch it?
8. Your leader GC-paused 400ms. What did the followers conclude, and is that distinguishable from a partition?
9. ☕ You implemented Raft in Go and in Java. Name three things you did differently the second time and why.

**Pass = 8/9.** *The hardest exam in the plan.* Then 🤖 **PROMPT 2** on "consensus, epoch consistency and fork attacks."

## 🧩 PROBLEM SOLVING — L6 · W44–52 · 56 problems · 5h/wk
**Patterns:** 🔴 **dynamic programming, part 2** — interval DP, DP on subsequences, string DP · intervals and sweep line · greedy with an exchange argument.
🔗 **The tie:** Raft is a replicated **state machine**, and interval/subsequence DP is where you get comfortable reasoning about "the state after processing a prefix" — the same mental move. And the interval problems are the sweep-line family that shows up whenever you schedule anything, which is what the directory's epoch windows are.

| Source | Set |
|---|---|
| 🔴 **LeetCode — interval DP** | **312** Burst Balloons · **546** Remove Boxes · **664** Strange Printer · **1000** Min Cost to Merge Stones · **87** Scramble String |
| **LeetCode — string DP** | 🔴 **10** Regular Expression Matching · **44** Wildcard Matching · **115** Distinct Subsequences · **940** Distinct Subsequences II · **516** Longest Palindromic Subsequence · **1312** Min Insertions to Make Palindrome |
| **LeetCode — intervals** | **56** Merge Intervals · **57** Insert Interval · **253** Meeting Rooms II · **435** Non-overlapping Intervals · **452** Min Arrows to Burst Balloons · **1235** Max Profit in Job Scheduling · **1353** Max Events That Can Be Attended · **715** Range Module |
| **LeetCode — greedy** | **45**/**55** Jump Game II & I · **134** Gas Station · **630** Course Schedule III · **871** Min Refueling Stops · **763** Partition Labels |
| 🔴 **AtCoder** | **Educational DP Contest, problems M–Z.** Finish the contest. **A–Z complete is a real credential among people who know it** |
| **CSES** | *Dynamic Programming* — the rest of the section, complete |
| **CF** | Problemset, tag `dp`, rating **1600–1800**, 12 problems |
| 🏁 **Capstone** | 🔴 **LC 312 Burst Balloons** and **LC 10 Regular Expression Matching**, both from scratch with the recurrence written first. **These two are the DP problems that most reliably separate candidates** |

**Design:** a distributed lock service, then a sharded database. 🔴 **You are implementing Raft twice this level — the lock-service design is the one where you say *"I built this"* and mean it.**
**Codeforces: virtuals W47, W51.** 🔴 **Target band by W52: 1750.** **W52: failure-category count and the year-one gate.**

> ### 🚩 END-OF-YEAR-ONE GATE — Week 52
> **Check honestly: is there a working mesh — peers finding each other across NAT, forwarding Sphinx packets over per-hop QUIC, two unmodified browsers that cannot be linked, and a directory every client agrees with? And are 15-213, Boneh, CS144 and 6.5840 complete with every lab ticked?**
>
> If yes: **Year 1 delivered the employable core and four completed courses.** Level 7 delivers the shell, and **applications open Week 56.**
> If no: **go to §XVII and cut in the stated order, now.** The most likely honest answer is that a course slipped — in which case **the course finishes and an Adyton level slips**, not the reverse, because the courses are the thing you cannot get back later.

---
---
# YEAR TWO — Mastery, While Interviewing
---

# ⚡ LEVEL 7 — Operations and the Shell 🎯

> **Goal:** the half of the work a screen actually reads — and **the level that opens applications.**
> **⏱ Weeks 53–58 · 2027-09-13 → 10-24 · 60h depth** · **Milestone D6** · **Core: `gatekeep`, `costwatch`** · **📺 Track C: 🔴 MIT 6.1810 begins (W53)** · **⚑ CV v4 at W55 · 🎯 APPLICATIONS OPEN W56 (2027-10-04) · W58 = REST WEEK**
>
> 🔴 **The coverage model says this level matters more than any clever core: the shell alone is 15.1% coverage, a clever core alone is 6.5%.** Six weeks, deliberately front-loaded in Year 2 so the CV is complete before the autumn window.

## 🔥 THE WALL — six failures, caused deliberately
1. `CrashLoopBackOff` from a missing ConfigMap key. 2. `Pending` forever — no node satisfies the resource request. 3. ⚙️ **OOMKilled under a "generous" limit** — the container counts your C++ arenas *and* the JVM's heap, metaspace, thread stacks and direct buffers. 4. **CPU throttling** — give a relay `cpus=0.5` and watch p99 hit 400ms for 20ms of work; find `nr_throttled` in `cpu.stat`. **Invisible from inside the container.** 5. **A rolling restart drops circuits**, because the pod dies before draining and there is no `preStop`. 6. **DNS latency** — the `ndots:5` search-domain problem.

## 📖 THEORY
**The reconciliation loop** — etcd holds desired state, controllers drive actual → desired. **Everything in Kubernetes is `while true { observe; diff; act }`.** **What happens on `kubectl apply`** — client → API server → authN → authZ (RBAC) → admission → etcd → watch → scheduler binds → kubelet → CRI → CNI. **A top-five interview question.** **cgroups v2** and container-aware sizing for both runtimes. **Graceful shutdown for a stateful relay** — SIGTERM, stop accepting circuits, signal migration, exit inside `terminationGracePeriodSeconds`. **The five signals that matter for Adyton:** circuit build success rate · circuit build p99 · consensus epoch agreement · peer count and churn rate · **leak-suite status.** That is the 3am dashboard. **Cost as architecture.**

**📺 Atlas → 6.1810 L1–L5 (introduction, C in xv6, OS design, page tables, syscall entry/exit)** + **labs util and syscall.** The page-tables lecture in W56 is a good week for it: you are about to explain container isolation to interviewers.
**📕 Pages:** **Google SRE Book ch. 3, 4, 6, 21, 22** — 🔴 **ch. 22 (cascading failures) may be the most valuable chapter in the book** · **SRE Workbook ch. 5** (multi-window multi-burn-rate alerting) · Lukša *Kubernetes in Action* ch. 1–7, 12, 17 · Majors et al. *Observability Engineering* ch. 1–6 · **`k8s.af` — read 10** · **AWS Builders' Library — read all ~20 across L7 and L11** · RFC 8446 §2 for `gatekeep`.

> 🤖 **PROMPT 1** W54 · `GAP:` why my container is OOMKilled at a limit that exceeds both my C++ arena budget and the JVM's `-Xmx` · `CONTEXT:` co-locating a C++ relay and a Java directory under cgroup limits · `THE DECISION:` how to size the limit so neither runtime is the one that dies · `NAMED REAL SYSTEM:` how the JVM's container awareness computes default heap

📈 **EXIT CRITERIA — D6**
- [ ] `kubectl apply -k deploy/` brings up a **30-node mesh plus the directory** on local k3s from nothing
- [ ] 🔴 **Rolling restart of every relay with ZERO circuits dropped**, under sustained traffic. Harder than it sounds and it is the real lesson
- [ ] Prometheus + Grafana with **the five Adyton signals**; **a dashboard you would actually open at 3am**; given an injected fault, **time-to-root-cause under 5 minutes using only the dashboards, demonstrated on video**
- [ ] All six wall failures reproduced and fixed, each with a one-paragraph note
- [ ] `gatekeep`: mTLS between all components; per-peer credentials with rotation; `gitleaks` in CI; **certificate expiry alert tested by fast-forwarding a clock**
- [ ] `costwatch`: everything in Terraform (`apply` from zero, `destroy` to nothing); hand-written least-privilege IAM verified with the policy simulator; **CI authenticates via OIDC with zero long-lived credentials**; **a $1 billing alarm tested by triggering it** — an untested alarm is not an alarm; free-tier drift detection failing CI on any billable resource
- [ ] **$0.00 verified from every console and screenshotted — every month from here**
- [ ] `docs/design/slo.md` — SLOs with error budgets **derived from measured numbers, not aspirations**
- [ ] 6.1810 L1–L5 ticked; **labs util and syscall complete**
- [ ] 🔴 **CV v4 written W55. First 12 applications sent W56. Referral activation (§XV.4).** **Blog post 3:** *"Rolling restarts that don't drop circuits"*

## 🎤 INTERVIEW PARAGRAPH — Week 58 (and CV v4)
> This level is the operational half, and I'd argue it matters more than the cryptography for most of what a backend engineer is hired to do. The mesh runs on Kubernetes now — thirty relays plus the directory, brought up from nothing with one command, with rolling restarts that drop zero circuits, which took a `preStop` hook that stops accepting new circuits and signals existing ones to migrate before the pod dies. Getting that wrong loses work on every deploy and almost every team has the bug. The failure that taught me most was OOMKilled at a limit I thought was generous, because the container counts my C++ arena allocations *and* the JVM's heap, metaspace, thread stacks and direct buffers, not just one of them. On the observability side the dashboard is five signals — circuit build success rate, build p99, consensus epoch agreement, peer churn, and leak-suite status — and I can root-cause an injected fault in under five minutes from those alone, on video. Everything is Terraform with OIDC-federated CI so there are no long-lived credentials anywhere, and the billing alarm is tested by triggering it, because an untested alarm is not an alarm. Zero dollars a month, screenshotted.

## 🎓 EXIT EXAM
1. What happens between `kubectl apply` and a running pod? 12+ steps.
2. ⚙️ Your container is OOMKilled at 4GB with a 2GB JVM heap and a 1GB C++ arena budget. Name four consumers of the difference.
3. A rolling restart drops circuits. Walk through the fix, in order.
4. CPU throttling at `cpus=0.5`: why is p99 400ms for 20ms of work, and how do you see it from outside?
5. Name the five signals on your 3am dashboard and what each tells you.
6. Design an SLO for circuit build success. SLI, budget, burn-rate alert thresholds.
7. Your cloud bill is $0.00. Three ways it becomes $400 next month, and the control for each.

**Pass = 6/7.**

## 🧩 PROBLEM SOLVING — L7 · W53–58 · 32 problems · 6h/wk 🔴 **+ OA DRILLS BEGIN**
> 🔴 **From W53 Track I is 10h/week (6 DSA + 4 design), because applications open in three weeks.**

**Patterns:** 🔴 **concurrency problems in C++** · design-heavy problems · heaps and scheduling.
🔗 **The tie:** you are writing `preStop` drain logic and a rolling-restart path this level. **LC 1188 (Design Bounded Blocking Queue) with a real `std::condition_variable` is the same problem** — and infrastructure loops ask concurrency questions that most candidates have never written.

| Source | Set |
|---|---|
| 🔴 **LeetCode — concurrency, in C++** | **1114** Print in Order · **1115** Print FooBar Alternately · **1116** Print Zero Even Odd · **1117** Building H2O · **1195** Fizz Buzz Multithreaded · **1226** The Dining Philosophers · 🔴 **1188** Design Bounded Blocking Queue |
| **LeetCode — scheduling/heaps** | **621** revisit · **1834** Single-Threaded CPU · **1642** Furthest Building You Can Reach · **502** IPO · **857** Min Cost to Hire K Workers |
| **LeetCode — design** | **362** Design Hit Counter · **348** Design Tic-Tac-Toe · **1610** Max Number of Visible Points · **295** revisit, then **480** Sliding Window Median |
| **Own work** | ⚙️ Producer/consumer, bounded buffer and dining philosophers **in C++ with `std::jthread` and `condition_variable`**, from scratch, no library help |
| 🏁 **Capstone** | **LC 1188 in C++**, then break it: what happens with a spurious wakeup, and what happens if `enqueue` throws? |

### 🔴 OA DRILLS — start now, they are a different skill
**An online assessment is not an interview.** No interviewer, no partial credit for approach, **hidden tests, a hard clock, and often 2–4 problems in 60–120 minutes.** The failure mode is not "couldn't solve it" — it is **misreading the spec, missing an edge case, or spending 40 minutes on problem 1 of 3.**

**The drill, from W53, one per week, 90 minutes, no narration:** pick **two unseen LeetCode Mediums or one Medium and one Hard**, set a timer, and **write your own test cases before submitting.** Score yourself on: did both compile first try · did you read the constraints and pick the right complexity · **did you budget the clock across problems.** Log it in `dsa/OA-LOG.md` separately from mocks — **it measures something mocks do not.**

**Design (4h/wk):** a metrics pipeline, then a deployment/rollout system. **W55: the Final Gauntlet. W57: FULL TIMED LOOP #1.**

---
---

# ⚡ LEVEL 8 — The Attack Lab

> **Goal:** build the adversary against your own network, on real internet topology, and publish a number you did not choose in advance.
> **⏱ Weeks 59–66 · 10-25 → 12-19 · 80h depth** · **Milestone D7** · **🚩 Flagship #6 `ascorr`** · **📺 Track C: 6.1810 L6–L14 + labs pgtbl, traps, cow** · **W66 = buffer**
>
> **The expected result is that Adyton is comparable to Tor and not better**, because your path selection is still naive. **That is the honest result and it is why Level 9 exists.** Publishing the unflattering number is what makes Level 9's improvement believable.

## 🔥 THE WALL
Build a circuit. Now look at it the way a real adversary does — not "which relays" but **"which autonomous systems do the packets traverse?"** Take your client's IP and your guard's IP: what AS path connects them? Then exit to destination. **If the same AS appears on both the client→guard and exit→destination segments, that AS sees both ends and the two-hop split-trust guarantee is gone** — not because a relay was malicious, but because **the network underneath both hops is one organisation.** Compute how often that happens for randomly chosen relays. **It is far more often than you expect**, because a handful of transit providers carry a large fraction of all internet paths.

## 📖 THEORY
**BGP and inter-domain routing** — ASes, customer/provider/peer relationships, and the fact that **AS paths cannot be observed directly from one vantage point. You *infer* them.** **The valley-free property** — up the provider hierarchy, possibly across one peer link, then down; the constraint that makes inference tractable. **CAIDA's AS-relationship dataset** plus AS-to-organisation so sibling ASes owned by one company are collapsed — a subtlety most implementations miss. **IXP overlap** — two ASes that never share a path may still meet at an exchange that sees both. 🔴 **Inference accuracy is the integrity question of the whole level.** Your compromise probabilities rest on inferred paths — **validate against RouteViews/RIPE RIS and report the disagreement rate.** Skip this and every claim for the rest of the plan is unfalsifiable, and an interviewer who knows this area will ask inside five minutes. **Guard compromise over time** — rotating entry relays constantly *guarantees* eventual hostile selection; **sticky guards convert certainty into a gamble you probably win.** Your instinct will be rotation; the field discovered rotation is the dangerous choice.

**📺 Atlas → 6.1810 L6–L14 + labs pgtbl, traps, cow.** Also **CS144's BGP lecture** if you skipped it, and **15-721 L6 (vectorized execution)** early if you want the technique for scoring millions of candidate circuits.
**📕 Pages:** 🔴 **Luckie et al., *AS Relationships, Customer Cones, and Validation* §2–4** — the inference model you are implementing · Kurose & Ross §5.4 · **Sun et al., *Counter-RAPTOR* §3–5**; skim **Astoria** and **DeNASA** · **Elahi et al., *Changing of the Guards* §3–5** · **Douceur, *The Sybil Attack*** — short, and it frames Level 10.

> 🤖 **PROMPT 1** W59 · `GAP:` how valley-free inference picks *one* path when several are legal, and what it does with incomplete data · `THE DECISION:` how to handle IP pairs with no valley-free path in the dataset — drop, guess, or report separately · `NAMED REAL SYSTEM:` how Counter-RAPTOR's implementation handles inference gaps
> 🤖 **PROMPT 4 (BRIDGE)** W61 · `SOURCE A:` my inferred AS paths · `SOURCE B:` RouteViews' observed paths, which disagree in X% of cases · `DECISION:` whether my compromise-probability numbers are publishable given that rate, and how to state the uncertainty
> 🤖 **PROMPT 5 (ADVERSARY)** W65 · `SYSTEM:` 2-hop circuits with naive capacity-weighted selection · `PROPERTY:` "no single party sees both who you are and where you are going" · `CAPABILITIES:` you control one large transit AS carrying a significant share of internet paths · `NOT:` you operate no Adyton relay and cannot decrypt anything

📈 **EXIT CRITERIA — D7**
- [ ] CAIDA AS-relationships and AS-to-organisation loaded; sibling ASes collapsed; graph queryable
- [ ] Valley-free inference; **missing relationships handled explicitly, never guessed silently**
- [ ] 🔴 **Inference validated against RouteViews/RIPE RIS: agreement rate reported honestly, disagreement cases characterised.** Expect 60–80%. **Every downstream number carries this caveat, stated**
- [ ] Adversary model parameterised by controlled ASes and IXPs, presets: one large transit AS · a national ISP · a five-AS coalition · an IXP operator
- [ ] 🔴 **Circuit-compromise probability computed for Adyton *and* Tor's selection, under all four presets, with the adversary definitions published**
- [ ] IXP overlap folded in via PeeringDB
- [ ] **Guard-compromise model:** eventual-compromise probability under per-circuit rotation vs sticky guards, **for Adyton's actual mesh size and circuit rate.** A curve, not a point
- [ ] **Sybil cost curve:** peers required at real VPS prices to control 10% / 25% / 50% of paths. **USD/month**
- [ ] **Churn adversary:** selective peer dropping to force re-routing — paths captured per unit of effort
- [ ] `lab/` has its own CI; **`lab/reproduce.sh` regenerates every number in `docs/results/` with one command**
- [ ] The GCP $300 window planned in `docs/design/gcp-window.md` **before spending a cent**: one 72-hour run at 200 nodes to validate the simulator
- [ ] 6.1810 L6–L14 ticked; **labs pgtbl, traps, cow complete**
- [ ] **Blog post 4:** *"I attacked my own privacy network. Here is the number, and it isn't flattering."*

## 🎤 INTERVIEW PARAGRAPH — Week 66
> The part of this project I'd point at first is the attack lab, because anyone can claim a system is private. I built the adversary against my own network on real internet topology — CAIDA's AS-relationship dataset with valley-free path inference. The insight that started it: two hops is not really two hops. If the same autonomous system appears on both the client-to-guard path and the exit-to-destination path, that AS sees both ends and the split-trust guarantee is gone, with no relay having been malicious. A handful of transit providers carry a large share of all internet paths, so it happens far more often than you'd guess. Given an adversary defined by which ASes and IXPs it controls, I compute the probability a circuit is compromised — for my selection and for Tor's.
>
> Two things I'd say unprompted. The honest result: my selection is currently naive, capacity-weighted only, so I'm **comparable to Tor and not better**, which is exactly why the next level is AS-aware selection. Publishing the unflattering number is what makes the improvement believable. Second, and it's the question I'd ask if I were interviewing me: these paths are *inferred*, not observed, because you cannot see inter-domain paths from one vantage point. So I validated the inference against RouteViews and reported the disagreement rate, and every number I publish carries that caveat. A compromise probability built on unvalidated inference is unfalsifiable, and I'd rather state the uncertainty than have someone find it.

## 🎓 EXIT EXAM
1. Explain the valley-free property and why AS paths cannot be observed from one vantage point.
2. Your two-hop circuit is compromised by a party operating no relay. How?
3. What is your inference agreement rate, and what does it do to your published numbers?
4. Define "compromised" precisely for your adversary model. Name the four presets.
5. Rotation vs sticky guards: state the counter-intuitive result in two sentences and give your curve.
6. What does 25% path control cost an attacker per month, and what changes that number?
7. Why is publishing a result that makes your system look no better than Tor the right move?

**Pass = 6/7.** Then 🤖 **PROMPT 2** on "AS-level correlation and path inference."
## 🧩 PROBLEM SOLVING — L8 · W59–66 · 46 problems · 6h/wk
**Patterns:** 🔴 **hard graph algorithms** — Tarjan's bridges and articulation points, strongly connected components, Euler tours, max flow (intro).
🔗 **The tie, and it is the most literal in the entire plan:** 🔴 **LC 1192 "Critical Connections in a Network" asks you to find the bridges in a graph — which is exactly the question "which single peer's removal partitions my mesh?"** You are computing that for real in `meshsim` this level. **Articulation points are not an interview trick for you; they are a property of your own system that you need to know.**

| Source | Set |
|---|---|
| 🔴 **LeetCode — bridges & articulation** | 🔴 **1192** Critical Connections in a Network · **1568** Min Days to Disconnect Island · **928** Minimize Malware Spread II · **924** Minimize Malware Spread |
| **LeetCode — SCC / condensation** | **1489** revisit · **802** revisit · **1462** Course Schedule IV · **1857** Largest Colour Value in a Directed Graph |
| **LeetCode — flow-ish / matching** | **1349** Max Students Taking Exam · **785**/**886** revisit · **1723** Find Min Time to Finish All Jobs |
| **LeetCode — hard traversal** | **773** Sliding Puzzle · **815** Bus Routes · **1102** Path With Maximum Minimum Value · **1102**'s cousin **778** revisit |
| **CSES** | 🔴 ***Graph Algorithms* — the advanced half**, including the SCC and Euler-path problems |
| **CF EDU** | **Maximum Flow, part 1** — the whole section |
| **CF** | Problemset, tag `graphs` + `dfs and similar`, rating **1700–1900**, 12 problems |
| 🏁 **Capstone** | 🔴 **LC 1192 from scratch, then run the same algorithm on your own mesh's peer graph and report which peers are articulation points.** That is the same code answering an interview question and a real question about your system, in one sitting |

**Design:** a fraud/abuse detection system, then a graph-processing system. **Weekly full loops from W59. Weekly OA drill continues.** **Codeforces: virtuals W62, W66.**

---
---

# ⚡ LEVEL 9 — Path Selection ⭐

> **Goal:** ⭐ **the research contribution.** Make circuits safer against AS-level correlation — then prove you did not hand the attacker a targeting oracle in exchange.
> **⏱ Weeks 67–76 · 12-20 → 2028-02-27 · 88h depth** · **Milestone D8** · **🚩 Flagship #7 `guardplace`** · **📺 Track C: 6.1810 L15–22 + labs net, lock, fs, mmap (W67–70); slack W71; 🌙 Ramadan 1449 W72–76 at 20h** · **W76 = REST WEEK (Eid)**
>
> 🌙 **Ramadan 1449 ≈ 28 Jan – 26 Feb 2028 = weeks 72–76, at 20h.** Scope moved out in advance: **the three candidate selectors and the C++ port land in W67–71 at full load; W72–75 is the parameter sweep**, which is compute-bound and script-driven rather than design-bound — the right shape of work for a reduced month. **6.1810 finishes W70, before Ramadan.**

## 🔥 THE WALL
Implement AS-aware selection: score candidates on AS-path disjointness between the two ends, prefer the best. Re-run Level 8's adversary. **Compromise probability drops meaningfully. Excellent.**

Now put on the attacker's hat: **your selector is deterministic and its scoring function is public — it is in your open-source repository. Where should I put my relays so that your algorithm prefers them?** Place ten relays chosen to maximise their score under *your* function. Measure how often they get selected. **It will be dramatically more than their fair share.** You have made the average case better and the targeted case worse, and **a defender who only measured the average would never have noticed.**

🔴 **That tension — AS-diversity versus predictability — is the project's research contribution, and nobody has published the curve.**

## 📖 THEORY
**AS-aware scoring:** AS-path disjointness between client→guard and exit→destination · IXP overlap · jurisdictional diversity · latency budget · measured capacity. Prior art **Astoria**, **Counter-RAPTOR**, **DeNASA**, **CLAPS** — **none deployed anywhere.** 🔴 **Guard placement attacks** (Wan et al., PoPETs 2019): AS-aware selection makes your selector *predictable*, and a predictable selector is a **targeting oracle**. **Controlled randomness** as the mitigation, on a **single tunable** from 0 (pure score) to 1 (pure capacity-weighted random) — **and the trade must be measured across the range, not asserted at one point.** **Guard rotation policy chosen from Level 8's curve rather than instinct.** 🔴 **The latency budget outranks the score** — Adyton's whole trilemma choice was low latency; a selector that improves compromise probability at 200ms of added build cost has violated the premise. **If the winner exceeds the budget, the budget wins and that is documented.** **Evaluate in Python before writing C++** — 43% of your postings, and it is how you avoid spending a month implementing the wrong algorithm in a language where changing your mind is expensive.

**📺 Atlas → 6.1810 L15–L22 + labs net, lock, fs, mmap (W67–70) — the course completes here.** 🔴 **Lab `net` is a network device driver: the other end of CS144, and a genuinely satisfying place to arrive.** **No course covers guard placement — this is the frontier, and noticing that the material has run out is part of the education.**
**📕 Pages:** 🔴 **Wan, Johnson, Wails, Wagner, Jansen — *Guard Placement Attacks on Path Selection Algorithms for Tor* (PoPETs 2019) §3–6** — **the paper this level exists to answer** · **Rochet et al., *CLAPS* (CCS 2020) §3–5** · Counter-RAPTOR §3–5 re-read with implementation in hand · Elahi et al. §5 re-read with your own curve.

> 🤖 **PROMPT 1** W68 · `GAP:` how an adversary actually *optimises* relay placement against a known scoring function — the algorithm, not the intuition · `THE DECISION:` whether placement is tractable optimisation or requires search, and what that says about a real attacker's cost · `NAMED REAL SYSTEM:` the methodology in Wan et al. 2019 and how they modelled the adversary's budget
> 🤖 **PROMPT 5 (ADVERSARY)** W72, **this *is* the flagship** · `SYSTEM:` Adyton's AS-aware selector with randomness parameter r, scoring on AS disjointness, IXP overlap, jurisdiction, latency and measured capacity. **The scoring function is public — it is in my open-source repo** · `PROPERTY:` "circuits are chosen to minimise the chance one AS sees both ends" · `CAPABILITIES:` you can rent relays anywhere with a budget of N, you can read my source, you can join the mesh legitimately · `NOT:` you cannot compromise the authorities or break the crypto
> 🤖 **PROMPT 4 (BRIDGE)** W74 · `SOURCE A:` Counter-RAPTOR and Astoria — AS-aware selection substantially reduces compromise probability · `SOURCE B:` Wan et al. — AS-aware selection is predictable and enables guard placement · `DECISION:` where to set my randomness parameter, and how to present a result where both papers are right

📈 **EXIT CRITERIA — D8**
- [ ] Three candidate selectors implemented **in Python first**, scored over the same graph against the same adversary presets. **Winner chosen on data, with the reason recorded**
- [ ] Winner ported to C++ in `adyton-core/select`; **cross-language test vectors: the C++ selector matches the Python one on ≥99% of 10,000 cases**
- [ ] AS-graph data distributed **via the epoch document**, compact — clients must not each download CAIDA dumps. **Loads in <200ms, fits in <40MB**
- [ ] Controlled randomness as a **single documented tunable**, with its meaning written down, not just its range
- [ ] 🔴 **The guard-placement adversary implemented and run against your own selector**, reporting the selection rate achieved by adversary-placed relays
- [ ] 🔴 **THE CURVE, published:** for ≥5 randomness settings, **compromise probability against the AS adversary** *and* **adversary-placed-relay selection rate**, on one plot. `docs/results/tradeoff-curve.md`
- [ ] **The operating point chosen off the curve, with the reason written down.** Not by instinct
- [ ] Guard rotation interval set from Level 8's curve, published alongside
- [ ] **Added circuit-build latency from AS scoring: <40ms p50.** If it exceeds the budget, the budget wins and that is documented
- [ ] 🔴 **6.1810 complete: all 22 lectures, all 9 labs ticked**
- [ ] 🔴 **Blog post 5:** *"AS-aware path selection makes you predictable. Here is the curve."* **The plot is the post.** A front-page candidate and the most novel thing you will write

> **If W75 arrives and the sweep is not achievable:** cut the CLAPS candidate retroactively and take Counter-RAPTOR-style on the literature's evidence, spending the recovered time on the sweep. **Do not cut the guard-placement run** — it is the level's entire point and the write-up's centrepiece.

## 🎤 INTERVIEW PARAGRAPH — Week 76
> This is the month I'd call research rather than engineering, and the only part of the project where I have a result nobody has published. AS-aware path selection is published — Astoria, Counter-RAPTOR, DeNASA, CLAPS — and none of it is deployed anywhere, which is itself interesting. I implemented it and compromise probability against my AS-level adversary dropped substantially. Good result. Then I read Wan et al. from PoPETs 2019, which says something uncomfortable: AS-aware selection makes your selector **predictable**, and mine is open source so its scoring function is public. A predictable selector is a targeting oracle. So I built that adversary against my own selector, placed ten relays optimised against my own scoring function, and they were chosen far more often than their share.
>
> **Both papers are right**, and a defender who only measured the average case would never have noticed. The mitigation is controlled randomness on a single tunable, and the point is that the trade has to be *measured* across the parameter range rather than asserted at one setting. So the artifact is a curve — compromise probability against adversary-placed-relay selection rate, across five settings — and I chose my operating point off that plot with the reason written down. That curve does not exist publicly. It's small, it's honest, and it's mine. The discipline I'd want credit for is that the latency budget outranks the score: the whole project's premise was low latency, so a selector that improves safety at 200 milliseconds of build cost has violated the premise, and I documented that constraint rather than quietly relaxing it.

## 🎓 EXIT EXAM
1. Name the four scoring dimensions and what each buys. Which conflict?
2. State the guard-placement attack in two sentences. Why does a *better* defence enable it?
3. How does an adversary optimise placement against a public scoring function? Is it tractable?
4. Where did you set your randomness parameter and why? Answer from the curve.
5. Your selector added latency. What is your budget, where did it come from, and what did you do?
6. Why evaluate three selectors in Python before writing any C++?
7. Why is the trade-off curve a better artifact than a single "40% improvement" claim?

**Pass = 6/7.** Then 🤖 **PROMPT 2** on "AS-aware path selection and guard placement."
## 🧩 PROBLEM SOLVING — L9 · W67–76 · 42 problems · 6h/wk (🌙 4h W72–75)
**Patterns:** 🔴 **probability and expectation** · randomised algorithms · weighted sampling · number theory and modular arithmetic.
🔗 **The tie, and it is exact:** 🔴 **LC 528 "Random Pick with Weight" is capacity-weighted relay selection** — the prefix-sum-plus-binary-search structure is what Adyton's selector does on every circuit build. And the whole level is about a **randomness dial**, so the probability set is not adjacent to the work, it *is* the work. The guard-rotation curve from Level 8 is an expectation calculation.

| Source | Set |
|---|---|
| 🔴 **LeetCode — weighted sampling** | 🔴 **528** Random Pick with Weight · **710** Random Pick with Blacklist · **382** Linked List Random Node · **398** Random Pick Index · **497** Random Point in Non-overlapping Rectangles |
| **LeetCode — randomised** | **384** Shuffle an Array · **470** Implement Rand10 Using Rand7 · **478** Generate Random Point in a Circle · **519** Random Flip Matrix |
| **LeetCode — expectation/probability** | **837** New 21 Game · **808** Soup Servings · **688** Knight Probability in Chessboard · **1230** Toss Strange Coins |
| **LeetCode — math** | **50** Pow(x,n) · **69** Sqrt(x) · **29** Divide Two Integers · **166** Fraction to Recurring Decimal · **233** Number of Digit One · **372** Super Pow · **204** Count Primes |
| **CSES** | *Mathematics* — the first twelve |
| **CF** | Problemset, tag `probabilities` + `math`, rating **1600–1900**, 10 problems |
| **Reading** | **Mitzenmacher & Upfal ch. 5** (balls into bins) — 🔴 **this is literally your relay-load-distribution problem** and it is already Track F block F16 |
| 🏁 **Capstone** | 🔴 **LC 528, then implement the same weighted-sampling structure inside `adyton-core/select` and check the distribution over 10⁶ draws against the intended weights.** Same algorithm, interview and product |

🌙 **W72–75 (Ramadan, 4h):** **no new topics. Re-solve from the log, and work the CSES *Mathematics* set slowly** — number theory rewards slow weeks.
**Design:** recommendation/ranking, then search. **W76: failure-category count.** 🔴 **Target band by W76: 1850.**

---
---

# ⚡ LEVEL 10 — ☕ Credentials & Abuse

> **Goal:** ban an abuser without knowing who they are. **Adyton's strongest design argument against Tor, and the reason daily browsing can work at all.**
> **⏱ Weeks 77–84 · 02-28 → 04-23 · 76h depth** · **Milestone D9** · **🚩 Flagship #8 `privacypass`** · **📺 Track C: 🔴 CMU 15-445 begins (W77) — lectures 0–14, projects P0–P2** · **W84 = buffer**
>
> ☕ **Java again** — a stateful, high-throughput, cryptographically careful service with a public API.

## 🔥 THE WALL
Stand up a gateway and let anyone with the client use it. Then be the abuser: send spam, hammer a login endpoint, scrape aggressively. Now try to stop yourself. **You cannot.** Two options, both bad: **ban the exit IP** — which bans every honest user sharing it — or **identify the abuser** — which destroys the product. 🔴 **This is Tor's structural bind, reproduced in an afternoon**, and it is *the* reason Tor users get CAPTCHAs on every site while a VPN user does not. Then notice what your weaker threat model bought: **you never promised anonymity against *yourself*, only unlinkability against third parties. That opens a door Tor's threat model keeps shut.**

## 📖 THEORY
**Privacy Pass / VOPRF tokens** — the user gets tokens blind-signed by the issuer; on spending one the issuer can verify validity **but cannot link the redemption to the issuance, even holding all its own records.** So "is this a valid member?" is answerable and "which member?" is not. **Revocation without linkage** — revoke and the holder loses access, while **no other user is deanonymised and no past redemption becomes linkable.** **Rate limiting without a per-user log.** **Credential-gated admission and sybil resistance** — a cost to join plus clustering detection by AS, subnet, join time and behavioural signature; **re-measure Level 8's sybil cost curve with admission on.** **Fairness without an identifying ledger** — relay-to-use reciprocity, or credentials *earned* by relaying. 🔴 **A bandwidth ledger keyed on peer identity is trivial to build and is a surveillance system inside an anti-surveillance system.** That constraint is what makes it hard. 🔴 **Why not full BFT** — PBFT solves agreement among mutually distrusting replicas on an *ordering*, at O(N²) messages; Adyton's failure model is crash-recovery plus a lying minority in *measurement*. **Being able to say precisely why you chose the lighter model is worth more than a half-finished PBFT** — and you watched 6.5840 L21 so the sentence is credible. **What you cannot solve, said out loud:** sybil in a *truly* open mesh needs proof-of-work, staking or a web of trust, none of which you built; large-scale collusion defeats any reputation scheme; a perfectly-timed defection by a long-trusted peer gets through once.

**📺 Atlas → 15-445 L0–L14 + projects P0 (C++ primer), P1 (buffer pool), P2 (B+Tree).** 🔴 **L16 (concurrency control theory) and L19 (MVCC) are the credential store's theory; L20–21 (logging, recovery) are its durability.** Also **6.5840 L21 (PBFT)** re-watch if you did not tick it.
**📕 Pages:** 🔴 **Davidson, Goldberg, Sullivan, Tankersley, Valsorda — *Privacy Pass* (PETS 2018) §2–4** · **RFC 9576** (architecture) and **RFC 9577** (issuance) §1–4 each · **Castro & Liskov, *PBFT* — abstract and §1–2 only**, so you can articulate what you deliberately did not build · **Douceur** re-read now that you are building admission · Aumasson ch. 10 (signatures).

> 🤖 **PROMPT 1** W77 · `GAP:` mechanically why the issuer cannot link a redemption to its issuance, even with all its own logs · `THE DECISION:` whether one credential can be spent many times or must be one-shot, and what each leaks · `NAMED REAL SYSTEM:` Cloudflare's Privacy Pass deployment and Apple's Private Access Tokens
> 🤖 **PROMPT 5 (ADVERSARY)** W81 · `SYSTEM:` Privacy Pass credentials gating gateway access, with revocation · `PROPERTY:` "the operator can verify membership and revoke abusers without learning which user is which, and without making past activity linkable" · `CAPABILITIES:` **you are the issuer AND the gateway operator, you keep every log you like, and you can also join as a user** · `NOT:` you cannot break the VOPRF

📈 **EXIT CRITERIA — D9**
- [ ] Blind-signature issuance, redemption and verification using an **audited VOPRF library — you do not implement the primitive**
- [ ] 🔴 **Unlinkability proven by a test that would fail if it were linkable:** issue 1,000 tokens, redeem in shuffled order, assert the server cannot recover the mapping better than chance
- [ ] 🔴 **Revocation: the holder loses access within one epoch, no other user is deanonymised, and no past redemption becomes linkable.** All three asserted
- [ ] Per-credential rate limiting **with no per-user log**; the privacy argument written out explicitly
- [ ] Credential-gated admission wired to clustering detection; peers enter the consensus view **only after measurement**
- [ ] 🔴 **Sybil cost curve re-measured with admission on: cost to control 25% of paths, before and after.** Target ≥10×; **if it is not 10×, report the real number**
- [ ] **Fairness:** reciprocity via earned credentials, earning and spending unlinkable; a peer that uses without relaying is throttled within one epoch. **If this does not converge by W83, ship the design doc plus a throttling stopgap and say in the README that fairness is designed but not fully implemented** — a legitimate answer; a broken mechanism is not
- [ ] `adyton-gateway`: public API with **OpenAPI 3.1 and CI drift detection**, quotas, correct `429` + `Retry-After`, **RFC 9457 Problem Details**, idempotency keys
- [ ] Credential issue+redeem **<50ms p99**; **10k redemptions/sec** on the free-tier box, measured
- [ ] `docs/design/trust-model.md` — the threat model and **an explicit section on what you do NOT defend against.** **ADR-0007: why not PBFT**
- [ ] 15-445 L0–L14 ticked; **P0, P1, P2 complete** — 🔴 **P2 is a concurrent B+Tree, the hardest project in the Atlas**
- [ ] **Blog post 6:** *"Banning abusers without knowing who they are"* — the most broadly interesting post of the two years. Write it for Hacker News

## 🎤 INTERVIEW PARAGRAPH — Week 84
> The design argument I'd defend hardest is accountability. Tor's usability problems are not bugs, they're structural: exit IPs are shared with abusers and Tor cannot ban anyone, because anonymity means no accountability — so sites block the exits and daily browsing breaks. I reproduced that bind in an afternoon: I stood up a gateway, abused it myself, and found exactly two options — ban the shared exit IP and punish every honest user, or identify the abuser and destroy the product. My threat model is weaker than Tor's — I never promised anonymity against *myself*, only unlinkability against third parties — and that weakness buys the door Tor's threat model keeps shut. Privacy Pass-style blind signatures let a user prove they're a valid member without revealing which member, so I can revoke an abuser without deanonymising them or anyone else. Exits stay clean, sites don't block them, browsing works. That's a virtuous cycle Tor is structurally unable to enter.
>
> The constraint I found hardest was fairness. A mesh where everyone relays for everyone collapses to freeloaders without a mechanism, but any bandwidth ledger keyed on peer identity is a surveillance system inside an anti-surveillance system. So it's reciprocity through *earned* credentials where earning and spending are unlinkable, and I wrote out the privacy argument rather than waving at it. And I'm explicit about what I didn't build: sybil resistance in a truly open mesh needs proof-of-work or staking or a web of trust; large-scale collusion beats any reputation scheme; and I chose redundant measurement plus majority agreement over full Byzantine consensus — which I can defend because I watched the PBFT lecture specifically so that "I didn't need it" would be a credible sentence rather than an excuse.

## 🎓 EXIT EXAM
1. Reproduce Tor's accountability bind in three sentences. What in your threat model escapes it?
2. Mechanically, why can the issuer not link a redemption to its issuance?
3. Revoke a credential. Prove no other user is affected and no past activity becomes linkable.
4. Rate-limit per credential with no per-user log. How?
5. Sybil cost for 25% path control, before and after admission. Your real numbers.
6. Why not PBFT? What does your model concede that PBFT would not?
7. Fairness without an identifying ledger. Your mechanism, and what it does not prevent.
8. ☕ From 15-445 P2: your B+Tree under concurrent insert and delete. What is latch crabbing and where did it bite you?

**Pass = 7/8.** Then 🤖 **PROMPT 2** on "anonymous credentials, revocation and sybil resistance."
## 🧩 PROBLEM SOLVING — L10 · W77–84 · 46 problems · 6h/wk
**Patterns:** 🔴 **segment trees and Fenwick trees** · order statistics · coordinate compression · sweep line with a tree.
🔗 **The tie:** you are building 15-445's **concurrent B+Tree (Project 2)** in the very same weeks. **A segment tree and a B+Tree are both "a tree over a range with an aggregate at each node"** — doing them together is the single best week-pairing in the plan, and the latch-crabbing you learn for P2 is the concurrency story for both.

| Source | Set |
|---|---|
| 🔴 **LeetCode — BIT / segment tree** | 🔴 **307** Range Sum Query – Mutable · 🔴 **315** Count of Smaller Numbers After Self · **493** Reverse Pairs · **327** Count of Range Sum · **673** Number of Longest Increasing Subsequence |
| **LeetCode — sweep + tree** | 🔴 **218** The Skyline Problem · **699** Falling Squares · **732** My Calendar III · **850** Rectangle Area II · **715** revisit |
| **LeetCode — order statistics** | **480** Sliding Window Median · **295** revisit · **1235** revisit with a BIT |
| **CF EDU** | 🔴 **Segment Tree, part 1 AND part 2 — complete.** This is the definitive free treatment; part 2 (lazy propagation, descending the tree) is where most people stop and should not |
| **CSES** | 🔴 ***Range Queries* — the whole section** |
| **CF** | Problemset, tag `data structures`, rating **1700–2000**, 10 problems |
| 🏁 **Capstone** | 🔴 **LC 315 solved three ways** — merge sort, Fenwick tree, and segment tree — **then say which you would write under interview pressure and why.** Then **LC 218**, which is the one people remember you for |

**Design:** an auth/token service, then a quota and fair-share system. 🔴 **You are building Privacy Pass and per-credential rate limiting this level — both designs are things you have implemented.**
**Weekly loops and OA drills continue. Codeforces: virtuals W80, W84.**

---
---

# ⚡ LEVEL 11 — Deep Operations

> **Goal:** observability inside an anti-surveillance system, and the chaos programme that makes on-call real.
> **⏱ Weeks 85–92 · 04-24 → 06-18 · 76h depth** · **Milestone D10** · **Core: `privcount`** · **📺 Track C: 15-445 L15–25 + projects P3, P4 (W85–90); 15-721 begins W91** · **W86 = Eid, 26h · W92 = REST WEEK**

## 🔥 THE WALL — build the wrong thing on purpose
Add normal, sensible metrics: per-relay bytes forwarded at five-minute granularity, scraped by Prometheus. Exactly what you'd do for any service. Now **attack your own metrics.** Correlate the byte counts across relays over the same window and try to reconstruct which relays carried the same circuit. **It works.** 🔴 **You have built a traffic-confirmation attack, hosted it yourself, and pointed it at your own users.** Anyone can add Prometheus; **demonstrating the attack your own telemetry enables and then defeating it is the interview story.**

## 📖 THEORY
**Why naive aggregates leak** — a relay's exact byte count in a window, correlated across relays, is a confirmation attack. **Private aggregation:** **Prio** (split each value into shares across non-colluding aggregators — Mozilla and ISRG deploy this in Firefox) vs **PrivCount** (calibrated noise under a tracked differential-privacy budget — built by the Tor Project for exactly this problem). 🔴 **A budget that can be exhausted:** ε tracked per metric per period, and **when spent, queries fail rather than silently degrading.** Test the failure. **What you lose** — state which operational questions you can no longer answer and how you debug without them; this is the honest cost and a strong thing to volunteer. **Chaos as method** — an incident you caused on purpose, with a timeline and a runbook, is worth more than three you survived by luck.

**📺 Atlas → 15-445 L15–L25 + P3 (query execution), P4 (MVCC concurrency control)** — 🔴 **the course completes W90.** **15-721 L0–L8** from W91.
**📕 Pages:** 🔴 **Dwork & Roth, *The Algorithmic Foundations of Differential Privacy* ch. 2, §3.1–3.3** (free) — the one genuinely mathematical block in two years · 🔴 **Jansen & Johnson, PrivCount §3–5** · **Corrigan-Gibbs & Boneh, *Prio* §1–4** · **Nygard, *Release It!*** — circuit breaker and bulkhead as named patterns; the most relevant book to this level · **`github.com/danluu/post-mortems`** — one a week for the rest of the plan · **Lamport, "Time, Clocks, and the Ordering of Events" (1978)** — eight pages, the most cited paper in the field.

> 🤖 **PROMPT 5 (ADVERSARY)** W85, on your own metrics · `SYSTEM:` relays exporting per-relay bytes-forwarded at 5-minute granularity, scraped centrally · `PROPERTY:` "the metrics contain no per-user information" · `CAPABILITIES:` you can read the entire metrics store historically, and you operate a website one target visits · `NOT:` you cannot see circuit contents or relay internal state
> 🤖 **PROMPT 1** W87 · `GAP:` how to choose ε for a real metric, and what composition does across a day of scrapes · `THE DECISION:` whether scraping every 60 seconds exhausts a sane daily budget, and what the right period is · `NAMED REAL SYSTEM:` PrivCount's actual parameters, and what Tor Metrics publishes today

📈 **EXIT CRITERIA — D10**
- [ ] 🔴 **The naive-metrics correlation attack demonstrated against your own telemetry, with its success rate reported** — then mitigated, with the after number beside it
- [ ] Private aggregation implemented (PrivCount-style noise under a tracked budget, or Prio-style shares); **ε chosen, justified in writing, enforced in code**
- [ ] 🔴 **The budget can exhaust and queries FAIL rather than degrade silently.** Asserted by test
- [ ] **The naive raw per-relay endpoint is deleted, not disabled.** No per-user logging, ever, including for debugging
- [ ] **What you lost, written down** — the operational questions you can no longer answer, and how you debug without them
- [ ] 🔴 **≥20 injected incidents**, each with the alert that fired (**or the alert that should have and did not**), a timeline, root cause and a runbook entry. Injections: relay kill mid-circuit · directory leader kill mid-epoch · **asymmetric partition** · disk fill · certificate expiry · **all 30 relays restarting at once** · a lying peer at scale · **clock skew** · DP budget exhaustion · seed-node death (**your bootstrap SPOF — what actually happens?**)
- [ ] 🔴 **The clock-skew incident done properly.** Skew one relay by four seconds: **nothing fails loudly.** Epoch validity windows misjudged, measurement timestamps disagreeing, circuit lifetimes computed against a clock the directory does not share — **the relay quietly makes wrong decisions while every dashboard stays green.** Then write the invariant: **relays report clock offset relative to the directory, and one beyond a threshold is quarantined**
- [ ] **≥4 famous outages reproduced locally** with instrumentation and verified fixes. Recommended: **Meta 2021** (🔴 does your admin surface depend on the mesh it administers? does your directory depend on something the mesh provides? **check**) · **GitHub 2018** (split-brain — reproduce it *without* Raft and fencing, then show yours surviving) · **Roblox 2021** (🔴 your monitoring must not depend on what it monitors) · **Cloudflare 2019** (a global config push — and you push epoch documents to every client)
- [ ] Every alert reviewed: actionable? runbook? worth 03:00? **An alert without a runbook is deleted, not documented**
- [ ] One deliberate **error-budget burn** with the written decision that follows
- [ ] `docs/analysis/sim-fidelity.md` — the same experiments on the real 30-node mesh and a 30-node simulation. Where they agree, where they diverge, by how much, and **does divergence grow at the GCP window's 200 nodes?**
- [ ] 🔴 **15-445 complete: all 25 lectures, all 5 projects ticked.** 15-721 L0–L8 ticked
- [ ] **Blog post 7:** *"I built a traffic-confirmation attack against my own privacy network's metrics"*

## 🎤 INTERVIEW PARAGRAPH — Week 92
> Observability inside an anti-surveillance system is a trap and I walked into it deliberately. Standard practice is per-service metrics at reasonable cardinality — so I did that, per-relay bytes forwarded at five-minute granularity, scraped by Prometheus. Then I correlated those counters across relays over the same window and reconstructed which relays had carried the same circuit. **I had built a traffic-confirmation attack, hosted it myself, and pointed it at my own users.** Anyone can add Prometheus; demonstrating the attack your telemetry enables and then defeating it is the actual work. The fix is private aggregation — PrivCount, which the Tor Project built for exactly this — with an explicit differential-privacy budget tracked in code that **fails queries when exhausted rather than quietly degrading.** I also wrote down what I lost: there are operational questions I can no longer answer, and that's the honest price.
>
> The other half is twenty-odd incidents I caused on purpose, each with the alert that fired — or the alert that should have and didn't — a timeline, a root cause and a runbook. The one that taught me most was clock skew: I skewed one relay by four seconds and **nothing failed loudly.** Epoch validity windows were misjudged, measurement timestamps disagreed, and the relay quietly made wrong decisions while every dashboard stayed green. And I found a circular dependency in my own recovery by reproducing Meta's 2021 outage locally — the one where a BGP change took out their DNS and also the tools they needed to fix it. My admin surface partly depended on the mesh it administers. That's written down now rather than discovered during an incident.

## 🎓 EXIT EXAM
1. Your metrics contained no user data and still enabled an attack. Explain the mechanism and your success rate.
2. Prio vs PrivCount: which fits Adyton and why? What is your ε and what justifies it?
3. Your DP budget is exhausted. What should happen, and what must never happen?
4. Your clocks skew four seconds. What breaks, and why does nothing alert?
5. Why must observability not depend on what it observes? Which Adyton component violated this?
6. Pick one reproduced outage: trigger, amplifier, containment failure, recovery obstacle.
7. Your seed node dies while peers are churning. Walk through the next ten minutes.
8. ☕ From 15-445 P4: what anomaly does snapshot isolation *not* prevent, and does Adyton care?

**Pass = 7/8.**

## 🧩 PROBLEM SOLVING — L11 · W85–92 · 46 problems · 6h/wk
**Patterns:** 🔴 **string algorithms — KMP, Z-function, rolling hash, suffix arrays** · plus combinatorics.
⚠️ 🔴 **This is the gap level, and you must treat it differently.** Strings, combinatorics and number theory get **zero reinforcement from Adyton** — there is no place in a privacy relay where you naturally write KMP. **Everything else in this plan is learned twice: once in the course, once in the product. This is learned once.** So: **more problems, slower, and re-solve everything at +3 days and +2 weeks rather than +3 days alone.** If your failure log has a bulge anywhere at Week 104, it will be here.

| Source | Set |
|---|---|
| 🔴 **LeetCode — KMP / prefix function** | **28** Find the Index of the First Occurrence · 🔴 **214** Shortest Palindrome · **459** Repeated Substring Pattern · 🔴 **1392** Longest Happy Prefix · **686** Repeated String Match · **1743**'s cousin **1147** Longest Chunked Palindrome Decomposition |
| 🔴 **LeetCode — rolling hash** | 🔴 **1044** Longest Duplicate Substring · **187** Repeated DNA Sequences · **1062** Longest Repeating Substring · **1554** Strings Differ by One Character |
| **LeetCode — string DP revisit** | **5**, **516**, **647**, **1312** — revisit now that you have KMP; **notice which ones the prefix function makes trivial** |
| **LeetCode — tries revisit** | **212**, **336**, **421** — revisit; **you will see the structure differently after suffix arrays** |
| **CF EDU** | 🔴 **Suffix Array — the whole section**, and the string-hashing material |
| **CSES** | 🔴 ***String Algorithms* — the whole section.** The single best string problem set available free |
| **CF** | Problemset, tag `strings` + `hashing`, rating **1700–2000**, 10 problems |
| 🏁 **Capstone** | 🔴 **LC 1044 Longest Duplicate Substring** (binary search over length + rolling hash, and understand the collision risk) **and LC 214 Shortest Palindrome** (KMP on `s + '#' + reverse(s)` — a trick worth genuinely understanding rather than memorising) |

**Design:** a time-series/metrics database, then an incident-management system. 🔴 **You are building DP-budgeted telemetry this level — the metrics-database design is yours.**
**Codeforces: virtuals W88, W92. W92: failure-category count.** 🔴 **Target band by W92: 1950.**

---
---

# ⚡ LEVEL 12 — Performance, 1BRC & the Tor Benchmark

> **Goal:** make it fast on hardware a volunteer actually owns, and produce the benchmark table you will show for the rest of your career.
> **⏱ Weeks 93–98 · 06-19 → 07-30 · 60h depth** · **Milestone D11** · **🚩 Flagship #9 `tor-bench`, 🔴 Flagship #10 `1brc`** · **Core: `pgshift`** · **📺 Track C: 15-721 L9–L22 (W93–100); 6.858 begins W95**
>
> Two years of *write correct C++ first, optimise second.* **This is second.** The constraint that shapes it: **this runs on volunteers' laptops, not servers you own.** So the number that matters most is not throughput but **CPU cost per forwarded megabyte** — what decides whether someone's battery survives, and the number almost nobody measures.

## 🔥 THE WALL
Before touching anything: **write down your prediction of the top three costs in the forwarding path and commit it to the repo.** Then profile. **You will be wrong, and being wrong here is the point** — this is the exercise that calibrates your performance intuition for the rest of your career.

## 📖 THEORY
Profiling with `perf` and flamegraphs · **the cost of a syscall per packet, and why batching with `sendmmsg`/`recvmmsg` and GSO changes the shape** · where the crypto actually costs (usually not the bottleneck) · allocation in the forwarding path · ⚙️ **removing only the copies the profile says are expensive**, not the ones that look expensive · **and the correctness gate: after every optimisation the full suite, RapidCheck, fuzz targets, ASan/UBSan/TSan and `leakproof` must be green, or the optimisation does not land. A fast deanonymisation bug is worse than a slow correct one.**
**Fair benchmarking against Tor:** same client machine, same destinations, same conditions, same window. 🔴 **State the hop counts in the table header** — three hops against your two is not like-for-like and every reader knows it — **and include your own three-hop row.** Tor is solving a harder problem under a stronger threat model; say so. The comparison is still favourable and now it is credible.

**📺 Atlas → 🔴 15-721 L6 (vectorized execution), L7 (code generation), L8 (scheduling & coordination), L12 (networking protocols), L16 (cost models)** — the five lectures that pay here, in the weeks you need them. Plus **15-213 ch. 5 optimisation lecture** re-watched, and **6.858 L20 (CPU timing attacks)** from W95 — 🔴 **relevant, because a timing difference in your forwarding path is a side channel, not just a slow patch.**
**📕 Pages:** CS:APP ch. 5 in full, §6.4–6.6 · Gregg *Systems Performance* ch. 6 §6.6, ch. 13 · Drepper §6.2–6.4 again, now with a profile in front of you.

> 🤖 **PROMPT 3 (REVIEW)** after the optimisations land · `COMPONENT:` the relay forwarding hot path after batching and copy elimination · `LANG:` C++20 · `INVARIANT:` every packet decrypted, MAC-verified and forwarded exactly once, **and no timing difference correlates with packet content** · `CONSEQUENCE:` a dropped or duplicated cell breaks a circuit; a timing side channel leaks position or content · `CONCURRENCY MODEL:` one thread per circuit, batched UDP I/O on a shared socket

## 🚩 FLAGSHIP #10 — `1brc`: the One Billion Row Challenge
> ⚙️ **Gunnar Morling's challenge (Jan 2024): parse 1,000,000,000 lines of `station;temperature` and print min/mean/max per station, as fast as the machine allows.** Reference: **https://github.com/gunnarmorling/1brc** · **W93–95, 20h.**
>
> **Why it earned its place in this plan.** It is the purest available exercise in the thing Level 12 is about, and unlike almost every other artifact here **the number is checkable by a stranger against a public leaderboard** rather than self-reported. It is also the direct application of 15-213's cache and optimisation lectures and 15-721's vectorized-execution lecture — **you will have completed both by Week 93**, which is exactly why it sits here and not earlier.
>
> 🔴 **And you already have a baseline.** In Week 5, before any of the eight courses, you wrote the naive version and committed the number. **The delta between `1brc-pass1` and `1brc-pass2` is not a benchmark — it is a two-year measurement of your own growth, and there is no other way to obtain that number.**

### 🔥 THE WALL
Open `1brc-pass1`. **Re-read your own Week-5 code.** You will see: a `std::string` allocated per line, a hash of that string, `std::stod` parsing a 4-character number through a general-purpose float parser, and one thread. **Before you touch anything, write down which of those four you think costs most and commit the prediction** — the same discipline as the forwarding-path prediction, on a problem where you can be checked.

### 📖 THEORY — the eight things that actually move it
1. **`mmap` the whole file** — no `read()` syscalls, no copies, no buffer management; the kernel pages it in.
2. **Partition by thread on line boundaries** — split the mapping into N chunks, then advance each boundary to the next `\n`. Embarrassingly parallel, and the merge is trivial because the key space is small.
3. **Parse the number by hand.** The format is fixed: optional `-`, one or two digits, `.`, one digit. **A branchless integer parse into fixed-point tenths is ~20× faster than `std::stod`**, and you never need a float.
4. **Find delimiters with SIMD** — `memchr` is already vectorized; explicit AVX2 over 32-byte blocks is faster still.
5. ⚙️ **Write your own open-addressing hash map** with `std::string_view` keys into the mapping, linear probing, power-of-two capacity, and **no allocation after construction.** `unordered_map` is a node-per-entry pointer chase and it is the single biggest win to remove.
6. **Cache-aware layout** — the per-station accumulator must be one cache line, and 15-213 Lab 4 is why you know that.
7. **Avoid the false sharing** you measured in Week 1: per-thread maps, merged once at the end.
8. **Know when to stop.** Past a point you are fighting page-fault cost and memory bandwidth, and **saying "I stopped here because I was bandwidth-bound and here is the arithmetic" is a better answer than one more percent.**

**📺 Atlas → 15-213 L9–L10 (cache), L15 (code optimization), L21–L24 (concurrency)** — all ticked long ago; **15-721 L6 (vectorized execution)** in W93.
**📕 Pages:** CS:APP ch. 5 in full · Drepper §3, §6.2–6.4 · Agner Fog's instruction tables if you go to intrinsics.

> 🤖 **PROMPT 1** · `PREREQ:` I have mmap'd the file, partitioned across threads, and written a branchless fixed-point parser · `GAP:` why my custom hash map is still slower than I expect, and how to tell whether I am now memory-bandwidth-bound or still latency-bound · `CONTEXT:` 1BRC in C++ on my own workstation · `THE DECISION:` whether further hash-map tuning can pay, or whether I have hit the bandwidth wall and should stop · `NAMED REAL SYSTEM:` the top C++ 1BRC entries and what they claim their bottleneck is

📈 **`1brc` EXIT CRITERIA**
- [ ] 🔴 **Correctness first: your output matches the reference implementation's byte-for-byte on the official test files.** A fast wrong answer scores zero, and the challenge has fixtures precisely because people get rounding wrong
- [ ] **Pass 2 is ≥50× faster than your Week-5 pass 1** on the same machine and the same file
- [ ] **Every optimisation has its own before/after number**, and each is attributed to one of the eight mechanisms above — **or marked "unattributed"**
- [ ] **Your committed prediction compared against the profile.** Report how wrong you were
- [ ] **Single-threaded and multi-threaded numbers reported separately**, so the parallel speedup is visible and you can state your scaling efficiency
- [ ] `perf stat` for both passes committed: instructions, IPC, LLC misses, page faults. 🔴 **The IPC change between pass 1 and pass 2 is the most interesting single number in the whole exercise**
- [ ] 🔴 **A written stopping argument:** the arithmetic showing what you are now bound by, and why further work does not pay
- [ ] ⚙️ **ASan and UBSan clean on the final version** — mmap plus manual pointer arithmetic plus SIMD is exactly where C++ bites, and a fast segfault is not a result
- [ ] **`docs/results/1brc.md`** — pass 1 number, pass 2 number, the delta, the eight mechanisms with their individual contributions, the stopping argument, and **an honest comparison against the public leaderboard's C++ entries**
- [ ] **Blog post:** *"The One Billion Row Challenge, twice, two years apart"* — 🔴 **the two-year delta is the story, and nobody else has that framing**

📈 **EXIT CRITERIA — D11**
- [ ] **Baseline recorded before any optimisation** — pps/core and CPU-per-MB, on your laptop and on the ARM free-tier box. You cannot claim an improvement otherwise
- [ ] 🔴 **Your written prediction of the top three costs, committed before profiling**, then compared against the flamegraph. **Report how wrong you were**
- [ ] Top three costs identified and addressed; **each fix has a before/after number or is reverted**
- [ ] Batched I/O (`sendmmsg`/`recvmmsg`, GSO where available), with the measured delta
- [ ] **Forwarding throughput >200k pps/core** and **CPU per forwarded MB <1.5ms/MB** — the battery number
- [ ] ⚙️ **The correctness gate held: every optimisation shipped with the full suite, RapidCheck, fuzz, all three sanitizers and `leakproof` green**
- [ ] 🔴 **THE TOR TABLE:** circuit build time, TTFB, sustained throughput, p50/p99, **1080p video viability with the bitrate stated** — Adyton 2-hop, Adyton 3-hop, Tor. **One script reproduces every number**
- [ ] 🔴 **Every win attributed to a named mechanism:** circuit build → Sphinx removing per-hop telescoping; tail latency → per-hop QUIC removing head-of-line blocking. **An unexplained benchmark is not evidence**
- [ ] `aarch64` build and a **per-component x86-vs-ARM delta**, attributed to cache sizes, memory bandwidth and vector width
- [ ] `pgshift`: a **50M-row migration on the directory's metadata store under live load** — expand/contract, chunked resumable backfill, **zero errors, p99 degradation <20%**, and **the naive version's outage graph beside the correct one**
- [ ] `docs/REPORT.md` — the technical report, 20–30 pages, **with an honest limitations section.** That section is what makes the rest credible
- [ ] 15-721 L9–L22 ticked; 6.858 L1–L8 ticked
- [ ] **Blog post 8:** *"Adyton versus Tor: the table"* — the most-linked thing you write

## 🎤 INTERVIEW PARAGRAPH — Week 98
> This was performance, and the constraint that shaped it is that this runs on volunteers' laptops rather than servers I own. So the two numbers I care about are packets per second per core and **CPU cost per forwarded megabyte** — the second decides whether someone's battery survives, and most projects never measure it. I wrote down my prediction of the top three costs before profiling, which I'd recommend to anyone, because I was wrong about two: I'd assumed crypto dominated and it was actually the syscall per packet and a copy in the forwarding path. Two years of deliberately writing correct C++ and copying freely, and this is where I removed the copies the profile said were expensive rather than the ones that looked expensive. The gate I held is that every optimisation shipped with the fuzzers, all three sanitizers and the leak suite green — a fast deanonymisation bug is worse than a slow correct one — and I'd add that a *timing* difference in the forwarding path is a side channel, not just a slow patch, which is a lesson from 6.858's timing-attacks lecture landing in the same month.
>
> Then the table against Tor. I state hop counts in the header and include my own three-hop row, because three against two isn't like-for-like and every reader knows it, and Tor is solving a harder problem under a stronger threat model. The comparison is still favourable and now it's credible. And I attribute each win to a mechanism rather than claiming a number: the circuit-build advantage is Sphinx removing the per-hop telescoping round trip; the tail-latency advantage is per-hop QUIC removing head-of-line blocking. One script regenerates the whole table, because a benchmark you can't reproduce is a marketing claim.

## 🎓 EXIT EXAM
1. What were your top three costs? How wrong was your prediction, and what does that tell you?
2. Why is CPU-per-MB the number that matters here rather than throughput?
3. What does batched I/O change, mechanically? Give your delta.
4. What makes a benchmark against Tor fair? Name four requirements you met.
5. Attribute each win to a mechanism. Which win did you expect and not get?
6. ⚙️ An optimisation made it 30% faster and turned one fuzz target red. What do you do?
7. A timing difference in the forwarding path. Why is that a security bug and not a performance bug?
8. `ALTER TABLE` on a hot 50M-row table. Full plan including rollback at every step.

**Pass = 7/8.**

## 🧩 PROBLEM SOLVING — L12 · W93–98 · 40 problems · 6h/wk 🔴 **SPEED PHASE**
🔴 **Topic learning is over. This level and the next are entirely about speed, volume and composure.** No new patterns. If a pattern is missing at Week 93, the failure log says so and you fix that one thing — you do not start a new topic.

| Source | Set |
|---|---|
| 🔴 **LeetCode, company-tagged** | **Filter by your seven targets, last 6 months. 30 problems, every one timed at 25 minutes and narrated aloud, recorded.** Premium is worth the $35 for these two levels |
| **Meta-specific** | 🔴 **Meta's screen is two problems in 45 minutes.** Drill *pairs*: two Mediums, 45 minutes total, twice a week. **Speed matters more at Meta than anywhere else and it is a trainable, separate skill** |
| **Hard mixed** | 10 unseen Hards, 45-minute box, from the tags your failure log flags |
| **CF** | One **rated** contest per week if the timing works, virtual otherwise |
| 🏁 **Capstone** | 🔴 **Three consecutive days of a full timed loop.** Not to prove you can solve them — **to find out what you are like on day three.** Real onsites are four hours and most candidates degrade badly in round three; you want to discover that now |

**Design:** full 45-minute designs, one per week, recorded. 🔴 **Every one of them should contain the sentence *"I built this; here is what I chose and here is the number I measured"*** — practise it deliberately, because it does not happen naturally under pressure.
**Weekly loops and OA drills continue.**

---
---

# ⚡ LEVEL 13 — Release & Synthesis

> **Goal:** the last measured result, then make it something a stranger can run and verify — then convert.
> **⏱ Weeks 99–104 · 07-31 → 09-10 · 60h depth** · **Milestone D12** · **Core: `shape` (reduced)** · **📺 Track C: 🔴 6.858 finishes — L9–L23 + all 5 labs** · **W104 = REST WEEK**

## 🔥 THE WALL
Your traffic is encrypted end to end. Now be a passive observer who cannot decrypt anything, and ask what is still visible: **packet sizes, directions and timings.** Take one browse session's capture and, by hand, mark where each page load starts and ends. **You will be able to, easily.** That shape is the residual leak the trilemma choice left you with, and it is what shaping addresses.

> 🔴 **Scope decision, stated honestly.** The full website-fingerprinting evaluation — training Deep Fingerprinting and Var-CNN on your own traffic and publishing the accuracy-versus-overhead curve — **was cut from this plan when `1brc` took its flagship slot** (§X, §XVII). What remains is `shape`: **implement the defence, measure what it costs, and be precise about what you did not measure.** That is a smaller claim and it is an honest one. **The full evaluation is the first item in `docs/NEXT.md`**, and it is a good six-week project for the months after Week 104.

## 📖 THEORY
Website fingerprinting: the attacker classifies traffic *shape*, not content · padding and timing defences: **WTF-PAD-style adaptive padding**, FRONT-style front-loaded padding · 🔴 **the hard boundary: Adyton's trilemma choice was low latency and low overhead, so a defence costing 100% overhead is not available to you even if it works — and enforcing that in code rather than in a comment is the engineering** · 🔴 **and the discipline that matters most here: know that the 2018 deep-learning attacks (Deep Fingerprinting, Var-CNN) broke WTF-PAD, so implementing WTF-PAD and claiming protection would be dishonest.** You are implementing a defence whose published effectiveness is *known to be limited*, measuring its cost, and saying so. **What remains unsolved even in the literature: multi-tab browsing and coarse-grained features, explicitly open as of the 2025 survey.**

**📺 Atlas → 🔴 6.858 L9–L23 + all five labs — the course, and the Atlas, complete here.** 🔴 **Lab 5 is a final project: submit Adyton's threat model and attack lab as it.** **L19 (anonymous communication)** you watched in Week 12; **re-watch it in Week 100 with two years of implementation behind you** — it will read completely differently, and that difference is the education.
**📕 Pages:** **Sirinam et al., *Deep Fingerprinting* (CCS 2018) §3–5** · **Juarez et al., *WTF-PAD*** and **Gong & Wang, *FRONT*** · the 2025 WF survey's problem statement and open-problems section.

> 🤖 **PROMPT 4 (BRIDGE)** W101 · `SOURCE A:` WTF-PAD's paper reports meaningful accuracy reduction · `SOURCE B:` Deep Fingerprinting (2018) reports that WTF-PAD is broken · `DECISION:` what I am entitled to claim about a defence I implemented but did not evaluate against a modern classifier
> 🤖 **PROMPT 5 (ADVERSARY)** W100, on the whole system · `SYSTEM:` Adyton, complete · `PROPERTY:` *no company can assemble one profile that contains all of you* · `CAPABILITIES:` you are an ad-tech firm with trackers on 60% of the top 10,000 sites, you buy broker data, and you operate one Adyton relay · `NOT:` you cannot observe the whole network and cannot break the crypto. **Put the result in `docs/threat-model.md`.**

📈 **EXIT CRITERIA — D12**
- [ ] **`shape` implemented** in `adyton-core/shape`: WTF-PAD-style adaptive padding, parameterised by an overhead budget; **hard latency cap enforced in code: ≤25ms p50 added**
- [ ] **Bandwidth overhead measured** as padding bytes over payload bytes, per configuration, ≥5 settings
- [ ] **A page-load-boundary visibility test:** can you still mark page boundaries by hand in a capture, with shaping on at each setting? A qualitative result, honestly labelled as qualitative
- [ ] 🔴 **`docs/LIMITATIONS.md` states plainly what you did NOT measure:** no trained classifier, therefore **no accuracy-reduction claim of any kind.** You implemented a defence and measured its cost; you did not measure its effectiveness. **Saying that clearly is worth more than a curve you did not earn**
- [ ] **The full WF evaluation written up as the first item in `docs/NEXT.md`**, scoped as a six-week post-plan project
- [ ] 🔴 **Reproducible builds: two independent environments produce identical binary hashes**, documented and third-party verifiable. **A person deciding whether to forward strangers' traffic on their own laptop must be able to verify the binary rather than trust you**
- [ ] 🔴 **`docs/threat-model.md` published, final** — reviewed line by line against §IX. **The killed / weakened / not-solved table in the README, verbatim.** First-screen disclaimer: *research prototype; not for anyone whose safety depends on it; use Tor*
- [ ] Install guide for Arch, Debian/Ubuntu, macOS; **tested by three people who are not you, ≥2 of 3 succeeding without your help.** If fewer, the guide is wrong — fix and retest
- [ ] `SECURITY.md` with a disclosure policy; `CONTRIBUTING.md`
- [ ] **≥3 peers running on hardware you do not control, in ≥2 countries** — recruited only now, because §IX forbids inviting users before reproducible builds and the threat model exist. **If nobody volunteers by W103, take the honest fallback: free-tier peers in more regions, and say in the README and in interviews that the mesh has not been tested with independent operators. Do not claim volunteers you do not have**
- [ ] **README final for a ten-minute reader**, tested on a human with a timer, confusion points fixed · **`docs/TOUR.md`** · **the 10 ADRs** · **`docs/LIMITATIONS.md` linked from the first screen** · **`docs/COMPARISON.md`** vs Tor, Nym, iCloud Private Relay, Arti and a VPN
- [ ] 🔴 **`docs/RETROSPECTIVE.md`** — hours estimated vs actual **per level and per course**, and the ratio; every target you set before measuring, with both numbers. **Almost no candidate has this document, and yours covers two years and 166 lectures**
- [ ] **The paper-style write-up (8–12 pages)** on whichever produced the better result — **guard-placement resistance (L9) or the shaping evaluation (L13)** — posted, and **sent directly to two or three researchers whose papers you cited**, with a short specific message
- [ ] **The 45-minute demo rehearsed and timed three times**, including peers joining and dropping live, and **recorded** — the artifact a hiring manager watches on a train
- [ ] 🔴 **6.858 complete: all 23 lectures, all 5 labs.** 🔴 **THE ATLAS IS COMPLETE: 166 lectures, 41 labs, eight courses**
- [ ] **`docs/NEXT.md`** — the plan beyond W104: application volume, live loops, and **how you sustain 8h/week with no roadmap telling you to**
- [ ] **Blog posts 9 and 10:** *"What traffic shaping actually buys, in numbers"* and *"Two years, eight courses, and what I got wrong"*

## 🎤 THE FULL ANSWER — Week 104
> I spent two years building an open privacy relay network and completing eight university courses with all forty-one of their labs. The problem is that no single company sees your whole life, but the trackers, brokers and ISPs together assemble one profile that contains all of it — and the existing answers all fail differently: a VPN moves the trust to one company, Tor is correct but nearly unusable for daily life, and iCloud Private Relay has the right architecture but is Apple-only and puts all your browsing in one bucket. **Onion routing is solved and Tor does it better than I ever will**; Arti, Nym, Sphinx, Counter-RAPTOR and Privacy Pass are all published work I implemented rather than invented.
>
> The product is not anonymity, it's unlinkability: your shopping self and your reading self get separate paths, separate exits, separate browser profiles, bound by Linux network namespaces so a leak between them is structurally prevented rather than merely unlikely. The design thesis is the anonymity trilemma — I take low latency and low bandwidth overhead, which means I explicitly do not defend against a global passive adversary, and that concession is in the README rather than a footnote.
>
> Five results I'd want to be asked about. ⚙️ **The language argument:** this is a daemon parsing hostile input where a memory bug is a deanonymisation vulnerability. Rust gives you that safety by construction; I chose C++ and had to earn it with sanitizers on every CI run, libFuzzer with a committed corpus, a documented subset, and three real bugs my own fuzzer found, written up. **Per-hop QUIC:** Tor multiplexes every circuit between two relays over one TCP connection, so one lost segment stalls unrelated users' circuits; I reproduced that and fixed it structurally, and I can explain why QUIC made each of its choices because I built a TCP first in CS144. **The directory:** my clients gossiped, so their peer lists diverged — and a circuit through peers only a few clients knew about narrows the anonymity set to almost nothing, so divergence is a *fingerprint*. Signed epoch documents fix it, and then SUNDR taught me that consensus among my authorities does not stop a *fork attack* on clients, so the documents are hash-chained and clients gossip the hashes. **Path selection:** AS-aware selection cut compromise probability and made my selector predictable, which is a targeting oracle — so I built the guard-placement adversary against my own algorithm and published the trade-off curve, which is the one thing here that doesn't exist anywhere else. And **the metrics:** I added ordinary per-relay counters and then used them to reconstruct which relays carried the same circuit — I'd hosted a traffic-confirmation attack against my own users, and fixing it meant differential privacy with a budget that fails closed.
>
> The things I say without being asked: **my mesh is thirty to fifty nodes I run plus a few free-tier boxes and a simulator**, and I validated the simulator against the real mesh and published where they diverge. I'm slower than Tor on throughput and I can tell you precisely why. My path inference is inference, validated against RouteViews with the disagreement rate reported. Sybil resistance in a truly open mesh needs something I didn't build. And this is a research prototype — **if your safety depends on it, use Tor.** All of that is in a limitations document linked from the first screen.

## 🎓 EXIT EXAM
1. Explain Adyton to a smart non-specialist in two sentences.
2. Name the five prior systems and where your design diverges from each.
3. Your three most interesting technical decisions, with the alternative you rejected.
4. Why is evaluating a shaping defence against pre-2018 attacks dishonest?
5. Why must reproducible builds exist before you invite a single user?
6. The sharpest question an interviewer can ask — what is it, and your answer? *(It is: "why would anyone use this instead of Tor?" The answer: for daily browsing, because pinned exits and revocable credentials make it usable where Tor structurally cannot be — and for anything where safety matters they should use Tor, and I say so in my README.)*
7. Estimated vs actual hours across two years and eight courses. What is your ratio and what will you do differently?

**Pass = 6/7.** Then 🤖 **PROMPT 2** on Adyton as a whole — **and this time, run it on all ten flagships in sequence.** It is the last calibration before the loops that matter.

## 🧩 PROBLEM SOLVING — L13 · W99–104 · 30 problems · 6h/wk 🔴 **THE FAILURE-LOG BLITZ**
🔴 **This level is not driven by a topic list. It is driven entirely by `dsa/FAILURES.md`.** Eight failure-category counts across two years have told you exactly what you are worst at. **Spend these six weeks on that and nothing else.**

| If your log says mostly… | These six weeks are |
|---|---|
| **recognition** | 40 unseen Mediums across *varied* tags, 25-minute box, no hints. Breadth is the cure |
| **approach** | 15 Hards with a **written plan before any code** — recurrence, invariant or reduction stated first |
| **implementation** | Re-solve your 25 most-failed problems from scratch, twice, a week apart. **Do not add new problems** |
| **speed** | Two rated Codeforces contests a week plus daily 2-problems-in-45-minutes pairs |
| **edge cases** | Every problem, write the test cases **before** the solution. 30 problems, and score yourself on tests-first compliance rather than on solving |

**Regardless of category:** **W99 and W102 are full timed loops. W103 is the second Final Gauntlet.** **Retire the failure log** — every entry re-solved correctly three times is struck out, and the ones that remain go in `docs/RETROSPECTIVE.md` as *"what I would still study."* 🔴 **That last list is an unusually honest artifact and worth showing.**

🔴 **Final targets by W104: Codeforces ≥2000 · 602 named problems with ≥70% solved unaided in 25 minutes · 30+ Hards · 24 written designs · 20+ full loops · the failure-log queue empty.**

---
---

# 🎯 TRACK I — The Interview Machine

> **Daily from Week 1.** **Y1: 8h/week** (5h DSA + 3h design) · **Y2: 10h/week** (6h DSA + 4h design). Never batched. Never skipped.
> You can complete eight courses and build Adyton and still be rejected in a 45-minute phone screen. **This is the track that cannot be crammed.**

## The ratio that governs it

| Round | Named in backend postings |
|---|---|
| **System design** | **76.3%** |
| Algorithms / DSA | 18.3% |

**System design is a first-class daily thread from Week 1.** But **DSA is a gate** — frequency is irrelevant when 100% of the loops contain two coding rounds, and the bar has risen. **~320h DSA aimed at hard-problem fluency, ~170h system design.**

⚙️ **Language: C++.** You are writing C++ for two years anyway, it is 19.4% of backend postings, and it is your contest language. **This is the one place where the language decision costs you nothing and gains you fluency you need daily.**

## Volume

| Period | Weeks | DSA | Design | Total |
|---|---|---|---|---|
| Y1 Levels 0–6 | 1–52 | 5 | 3 | ~370 |
| Y2 Levels 7–13 | 53–104 | 6 | 4 | ~450 |

**≈ 490 hours after rest and Ramadan reductions.**

🔴 **The count, reconciled — because it should add up:** the fourteen per-level sets in §XII–XIII name **602 specific problems.** On top of those: **~30 Codeforces contests** (≈90 problems attempted), the **CSES sections** assigned per level (≈200, overlapping the named sets only partly), **AtCoder DP A–Z** (26), and **re-solves**, which are not new problems but are where the learning happens. **The honest total of distinct problems attempted is 750–850; the number that matters is 602 named ones done properly, not a bigger number done badly.**

**Do not chase the count.** A problem you solved by opening the editorial after eight minutes did not happen. **A problem you failed and rebuilt from scratch two days later counts double.** 🔴 **And 602 problems over 104 weeks is 5.8 a week — this plan is deliberately not a grind. It is a slow, high-retention pass with the failure log doing the compounding.**

## 🔴 The progression — what "good enough to pass" actually means, phase by phase

**You asked for really strong problem-solving alongside the learning. This is the shape of it.** Four phases, and **the point of the table is that each phase has a different definition of success** — measuring yourself against the wrong one is how people plateau.

| Phase | Weeks | The goal | Success is | Codeforces |
|---|---|---|---|---|
| **1 · Patterns** | 1–27 | **See the shape.** Every core pattern encountered at least twenty times | You can name the pattern within 60 seconds of reading a problem, even if you cannot yet implement it fast | 1450 → **1550** |
| **2 · Depth** | 28–52 | **Derive, don't recall.** Graphs, DP and design at real difficulty | You can rebuild a solution from the idea, not from memory. **Recurrence before code, every time** | 1550 → **1750** |
| **3 · Speed & gates** | 53–92 | **Perform under a clock, and pass OAs** | A random unseen Medium, narrated, in ≤25 min, ≥80% of the time. **Two problems in 90 min with no interviewer** | 1750 → **1950** |
| **4 · Composure** | 93–104 | **Four rounds in a day without degrading** | Round three is as good as round one. The failure log is empty | **2000+** |

🔴 **On the Codeforces numbers:** they are a *calibration instrument, not a goal*. **1750 is comfortably past the bar for a FAANG coding round; 2000 is past it with room.** If you hit 1900 by Week 76 and stall, that is fine — **stop optimising the rating and optimise the 25-minute narrated Medium instead**, because that is the actual interview condition and the rating is only a proxy for it.

## 🔴 The three different skills, and why people confuse them

Most candidates train one thing and are surprised by the others. **This plan trains all three, separately.**

| | The **coding interview** | The **online assessment** | The **contest** |
|---|---|---|---|
| **You have** | An interviewer, hints, partial credit | Hidden tests, a hard clock, nothing else | A leaderboard and 2+ hours |
| **You are judged on** | Reasoning **out loud**, clean code, complexity, edge cases | **Passing all tests.** Nothing else | Solving more than other people |
| **Fails because** | 🔴 **Silence.** A candidate who can solve it but does not narrate | 🔴 **Misreading the spec, or spending 40 of 90 minutes on problem 1 of 3** | Speed |
| **Trained by** | Mocks and loops (§Mock schedule) · **narrate always, even alone** | 🔴 **OA drills from W53** — 90 min, two unseen problems, no narration, **write your own tests first** | Weekly virtuals and rated contests |
| **Logged in** | `dsa/mocks.md` | 🔴 `dsa/OA-LOG.md` | Your CF profile |

🔴 **The OA is the one people neglect and it is the first gate you hit.** Amazon, Meta and most second-tier companies screen with one before a human ever sees your CV. **From Week 53 you do one drill a week, and the score you track is not "did I solve them" but "did I budget the clock and did I write tests before submitting."**

## Sources

| Source | For | How |
|---|---|---|
| **NeetCode 150 / 250** | The pattern spine, W1–30 | In order, grouped by pattern. Do not skip the easy ones |
| **LeetCode, company-tagged** | W31–104 | Filter by your targets, last 6 months. Premium is worth $35 for two months before a loop |
| **Codeforces Div 2 A–D** | Weekly, both years | Rated when it fits, virtual when not. Band 1400 → 1900 |
| 🔴 **Codeforces EDU (ITMO)** | `codeforces.com/edu/courses` | **Binary Search (L1) · Two Pointers (L0) · DSU (L5) · Segment Tree parts 1–2 (L10) · Suffix Array (L11) · Max Flow part 1 (L8).** The best free structured material in existence for these six topics — **all of them are assigned in this plan** |
| 🔴 **CSES Problem Set** | `cses.fi/problemset` | **300 problems, organised by topic, no editorials.** Harder and cleaner than LeetCode at the same tag. **Sections assigned per level: Introductory, Sorting & Searching, DP, Graph Algorithms, Range Queries, Tree Algorithms, Mathematics, String Algorithms** |
| 🔴 **AtCoder Educational DP Contest** | `atcoder.jp/contests/dp` | **26 problems, A–Z, and it is the best DP resource that exists.** A–L in Level 3, M–Z in Level 6. **A–Z complete is a real credential among people who know it** |
| 📺 **MIT 6.006 / 6.046** | The *why* behind the patterns | `ocw.mit.edu`. **6.046** for randomised algorithms, flows, NP-completeness — and it pairs with Level 8's probability work |
| **Skiena, *Algorithm Design Manual* 3rd ed.** | Reductions and intractability | **Ch. 8** (DP), **ch. 9** (intractability — supports the W37 proving week) |
| **Laaksonen, *CP Handbook*** (free) | Reference | **Ch. 7, 9, 13–15, 26** |
| **Alex Xu, *System Design Interview* Vol. 1 & 2** | Design | You own both |
| **`interviewing.io` / Pramp** | Mocks | Free peer mocks; **one paid mock with a real FAANG engineer around W50** |

## 🔗 Where the courses and Track I compound — the unfair advantage

🔴 **This is the thing that makes the two-year plan pay in interviews, and it is not obvious.** Eight courses' worth of papers *are* system-design answers:

| You will have read | And they will ask you to design |
|---|---|
| **GFS, Spanner, Chain Replication** (6.5840 L3, L12, L13) | A distributed file store · a globally consistent database |
| **ZooKeeper** (6.5840 L9) | A service-discovery / coordination system |
| **Memcached at Facebook** (6.5840 L16) | A cache tier at scale |
| **MapReduce, Spark, Ray** (6.5840 L1, L18) | A batch/stream processing platform |
| **Dremel, Snowflake, Redshift, DuckDB** (15-721 L17–22) | An analytics warehouse |
| **Buffer pools, B+trees, MVCC, ARIES** (15-445) | A storage engine · a transactional store |
| **Firecracker, WebAssembly, RLBox** (6.858 L6–L8) | A multi-tenant compute sandbox |
| **Your own Raft, twice** | 🔴 *"I built one; here is what I chose and the number I measured"* |

**Most candidates answer design questions from a book. You will answer them from papers you read and systems you built.** Practise that move deliberately in the W57 and W80 mocks, because **it does not happen naturally under pressure.**

## 🔴 The failure log
Solving problems does not make you better. **Reviewing failures does.** `dsa/FAILURES.md`, an entry every time you miss the time box or use the wrong approach: date · link · topic · time box · outcome · what I tried · **why it failed, specifically** ("didn't see it was a graph problem" is a different bug from "saw it and implemented BFS wrong") · the insight I was missing · **category: recognition / approach / implementation / speed / edge cases** · re-solve due +3 days.

**The category field is the whole point.** After thirty entries, **count them:** mostly *recognition* → need breadth, more varied problems · *approach* → need depth, slow down and work the reasoning · *implementation* → need reps, re-solve and do not move on · *speed* → knowledge is fine, do timed sets · *edge cases* → process problem, write test cases *before* code.

**Do the count in every rest week — W6, 19, 26, 43, 58, 76, 92, 104.** Twenty minutes, and it redirects the next quarter. **Most people never do it and spend two years fixing the wrong thing.**

**Time boxes:** Easy 15 min · Medium 25 min · Hard 45 min. **Never exceed the box.**

## System design — 24 written designs
Each produces a full doc: **Summary · Context · Goals · Non-Goals · Proposal · Alternatives Considered (minimum three) · Risks · Rollout · Operational Impact.**
**The 45-minute structure:** 0–5 requirements, functional **and** non-functional, on the board · 5–10 estimation (**round aggressively, show the arithmetic**) · 10–15 API and data model · 15–25 high-level design (**state your choices as choices**) · 25–40 deep dive (where the grade is decided) · 40–45 failure modes and 10×.
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

## Mock and loop schedule

| When | What |
|---|---|
| **W41** | First human mock + **the Raft Figure 8 whiteboard test** (a checkable gate, not a formality) |
| W47, W50 | Monthly mock. **W50: one paid mock with a real FAANG engineer**, if affordable |
| **W57** | **Full timed loop #1** — 4 rounds in one day |
| W59–104 | **Weekly full loops.** ~20 total by W104 |

**A full loop:** two 45-min coding rounds with a human, one 45-min system design, one 30-min behavioural, **in a single day** with realistic breaks. **Not four sessions across a week** — the exhaustion is what you are training for.
**Speak while you solve, always, including alone.** The most common cause of a failed coding round in a candidate who *can* solve the problem is silence.

## 📈 EXIT CRITERIA
- [ ] **602 named problems complete** (§XII–XIII), **≥70% solved unaided within 25 minutes**; a random unseen Medium **narrated** in ≤25 min, ≥80% of the time
- [ ] Complexity stated before code, every time · 30+ Hard problems · **failure-log queue empty** · Codeforces ≥1750
- [ ] **24 written system design docs** + 24 more practised verbally
- [ ] **20+ full timed loops** · 14 behavioural stories on video, **≥4 from Logic Leap**
- [ ] 🔴 **40+ OA drills logged in `dsa/OA-LOG.md`**, with clock-budgeting and tests-first scored separately from correctness
- [ ] 🔴 **AtCoder Educational DP Contest A–Z complete** · **CSES: 200+ solved** · **CF EDU: all six assigned sections complete**
- [ ] 🔴 **~30 Codeforces contests** (rated or virtual) across two years, and a rating of **2000+**

---
---

# 🧭 TRACK J — Craft, Career & Visibility

> **Y1: 2h/week · Y2: 4h/week.** What separates an L4 from an L5 is not knowing more systems facts. It is **judgement, communication and impact beyond your own keyboard.**

## J.1 — Design docs and ADRs
**The design doc is the unit of senior technical work**; promotion at every large company is decided by written artifacts. The two sections that separate senior from mid are **Alternatives Considered** and **Non-Goals** — a doc without a serious alternatives section reads as advocacy, not engineering.

**Scheduled:** `threat-model.md` (W11, revised every phase) · `cpp-subset.md` (W11) · `packet-format.md` (W19) · `browser-delta.md` (W27) · `consistency.md` (W52) · `slo.md` (W58) · `trust-model.md` (W84) · `sim-fidelity.md` (W92) · `LIMITATIONS.md` + `COMPARISON.md` (W102) · `RETROSPECTIVE.md` (W103).
**The ten ADRs (W102):** 0001 ⚙️ C++ for the data plane and the safety apparatus that earns it · 0002 the C++/Go/Java boundary · 0003 two hops not three · 0004 Raft vs Paxos vs Chain Replication · 0005 the consistency model per component · 0006 hash-chained epoch documents and client gossip · 0007 why not PBFT · 0008 Sphinx over telescoping · 0009 per-hop QUIC over one end-to-end session · 0010 where the randomness dial sits.

## J.2 — Writing: post the results, not the progress

| Week | Post | Why it travels |
|---|---|---|
| 27 | **"Your proxy leaks four ways and three of them aren't the proxy's fault"** | Broadly useful and immediately actionable |
| 35 | ⚙️ **"I chose C++ for an anonymity network. Here are the three bugs my fuzzer found."** | 🔴 The honest version of a language argument people usually make with slogans |
| 43 | **"Rolling restarts that don't drop circuits"** | Practical, and it is what the shell is for |
| 52 | 🔴 **"In a privacy network, disagreeing about the peer list is a privacy bug"** | The anonymity-set argument plus fork consistency. **Genuinely novel framing** |
| 66 | **"I attacked my own privacy network. The number isn't flattering."** | Publishing the unflattering result is what makes the next post believable |
| 76 | 🔴 **"AS-aware path selection makes you predictable. Here is the curve."** | **The plot is the post. Front-page candidate and the most novel thing you write** |
| 84 | **"Banning abusers without knowing who they are"** | The most broadly interesting post of the two years. Write it for Hacker News |
| 92 | 🔴 **"I built a traffic-confirmation attack against my own privacy network's metrics"** | Observability inside an anti-surveillance system. Nobody writes about this |
| 98 | **"Adyton versus Tor: the table"** | The most-linked thing you write |
| 104 | **"Two years, eight courses, and what I got wrong"** | 🔴 The retrospective is trusted more than any technical post |

Own the domain; cross-post to Hacker News, Lobsters, `r/cpp`, `r/netsec`, `r/privacy`. **One post reaching the HN front page generates more inbound recruiting than 200 applications.** **Give one talk** — a Cairo meetup counts.

## J.3 — Open source: the Arti track
🔴 **Arti is the Tor Project's Rust Tor implementation**, and a merged patch there is a career artifact you cannot manufacture another way: public, permanent, reviewed by strangers who owed you nothing, **in exactly the domain you are claiming.** *(And yes, Arti is Rust while Adyton is C++ — which is fine and even useful: it demonstrates you can read and contribute to a codebase in a language that is not your product's.)*

| Week | Activity | h |
|---|---|---|
| 16 | Read the architecture: `tor-proto`, `tor-circmgr`, `tor-netdir`. **Note two candidate contribution areas** | 4 |
| 30 | Join the channels, read the contribution guide, watch the tracker for a month | 2 |
| 45 | Pick a first issue — docs, a test, a small bug. **Small and finishable** | 3 |
| 60 | Submit it. Respond to review promptly and without defensiveness | 4 |
| 80 | Second contribution, more substantial — **ideally something your own implementation taught you** | 8 |
| 100 | Final contribution or follow-through | 6 |

**Pick the issue you can finish, not the impressive one.** A merged three-line documentation fix is worth more than an abandoned feature branch, because the artifact is *"contributed to Arti"* and the second is far easier once you have been through the process. **By W80 you will have implemented Sphinx, per-hop QUIC, AS-aware selection and guard rotation — you will have opinions about circuit management grounded in having built one.** That is where a substantial contribution comes from. **Also worth PRs:** `ngtcp2`, `libsodium` docs, `pion/ice`. **Target: 3+ merged, one non-trivial, ≥1 in Arti.**

## J.4 — 🔴 The referral problem, from Egypt — pipeline opens Week 20
**A referred application is read by a human. A cold one from Cairo to a Dublin req frequently is not.** **The mistake is waiting until W56 and messaging strangers** — a referral is someone putting their reputation on your application, and nobody does that for someone who appeared in their inbox last Tuesday. **You have 36 weeks of runway before applications open. Use them.**

**Channel 1 — the Egyptian engineering diaspora. Highest return.** Substantial numbers at Google Dublin and Zurich, Meta London, Amazon Dublin, Microsoft. LinkedIn alumni search on your university, then other Egyptian universities, filtered by company. **They were where you are, and they are disproportionately willing to help and disproportionately under-asked.** Not "can you refer me":

> I'm a backend engineer in Cairo building an open privacy relay network — Sphinx onion packets over per-hop QUIC, a Raft-backed directory, per-identity compartments enforced with Linux network namespaces. I'm working through MIT 6.5840 alongside it. I'm on the directory's fork-consistency problem now and I'd value fifteen minutes of your view on [one specific technical question you genuinely have]. No obligation and no ask beyond that.

**Target: 3 conversations/month from W20 — that is 100+ conversations and 40–50 people by W56 who know what you are building.** That is a genuinely different position from any 12-month plan.

**Channel 2 — build in public** (J.2). **Channel 3 — Arti** (J.3). **Channel 4 — the technical report** (W98): most candidates have a GitHub link; **a 20–30 page report with benchmarks and an honest limitations section is a different object and it gets forwarded.** **Channel 5 — the communities:** the `tor-dev` list · the `ngtcp2` and QUIC communities · **RIPE** (Egypt is in the RIPE NCC service region, meetings have full remote participation, the routing-security WG is directly relevant to your AS-path work) · **PETS**, your write-up's audience · **FOSDEM** (Brussels, early February, free) if you can travel once.

**The direct ask, W56, to people you have known for eight months:**
> I'm applying to [specific role, specific office] this week. Here's the project [link] and my CV. If you're comfortable referring me I'd be grateful; if not, no problem at all — and I'd still value knowing whether the CV reads clearly to someone inside.

**The second half matters** — it gives them an out that is not a rejection and frequently produces useful feedback from people who will not refer you. **What does not work:** mass LinkedIn requests · "I'd love to connect" with no content · commenting to be seen · referral-request forms · paid referral services.

## J.5 — 🔴 The Logic Leap track: sourcing what a solo project cannot
**Mentoring 36.6% · Communication 34.4% · Collaboration 31.2% · Leadership 17.2%.** Adyton demonstrates **none.** **Two years makes this easier, not harder — you have eight quarters instead of four.** But it only works if it is deliberate; left to chance you arrive at W100 with fourteen stories, twelve about a side project, and interviewers notice.

| Weeks | What to deliberately do at Logic Leap | The story |
|---|---|---|
| **1–26** | **Review other people's PRs**, seriously, weekly. Leave the comment you would want to receive | *"Improving quality without authority"* |
| **27–52** | **Write one design doc for real work** and circulate it before implementing | *"Aligning people on a technical decision"* — the Alternatives section is the artifact |
| **27–52** | **Onboard or unblock someone**; track what they were stuck on | *"Mentoring"* — the largest soft gap at 36.6% |
| **53–76** | **Take one cross-team dependency end to end**, driving the conversation | *"Cross-functional work"* · *"Working across teams"* is 59.1% of duties |
| **53–76** | **Disagree with a senior person, in writing, with data**, and handle the outcome either way | *"Disagreeing with a senior person"* — required, and you cannot fabricate it |
| **77–104** | **Lead one thing end to end**: scope, plan, delegate a piece, ship, own the outcome | *"Leading a project"* is 30.1% of duties |

**Log each in `career/LOGICLEAP.md` as it happens, with dates and specifics.** You will not remember details two years later, and vague behavioural answers are the most common way strong technical candidates fail loops.
> 🔴 **Do not let Adyton eclipse your paid work.** **At least four of fourteen stories must come from Logic Leap.** An interviewer who hears twelve about a side project and two about the job you were paid to do draws a conclusion you do not want. **And over two years you should be getting promoted at Logic Leap — that is itself a CV line and it is evidence Adyton did not cost you your day job.**

## J.6 — Target companies
| Company | Offices | Note |
|---|---|---|
| 🔴 **Cloudflare** | London, Lisbon, Austin, remote (varies) | **The single best fit.** They *wrote* "The Trouble with Tor." QUIC, NAT traversal and DDoS-adjacent work is their product |
| 🔴 **Fastly** | London, remote | Edge/data plane, same domain, C++ and Rust |
| 🔴 **Tailscale** | Remote-first, Toronto-anchored | **NAT traversal and mesh networking. Level 5 is literally their problem** |
| **Datadog** | Paris, Dublin | Ingest at scale; Level 11's private telemetry is an unusual version of their core problem |
| **Google** (infra/SRE) | Dublin, Zurich, London, Munich, **Warsaw** | Zurich strongest and hardest; **Warsaw more accessible** |
| **Meta** (infra) | London, Dublin | Fast, volume-heavy loop |
| **Amazon / AWS** (infra) | Dublin, London, Berlin, Luxembourg, **UAE** | Most reqs, most accessible tier-1 entry. **Gulf offices are a real route from Egypt** |
| **Microsoft** (Azure infra) | Dublin, London, Cambridge, Munich, **Cairo** | 🔴 **The only tier-1 with engineering in Cairo. Apply there regardless** — a local tier-1 role is a legitimate route to internal transfer |
| **Stripe** | Dublin, London | Backend-heavy; **values written communication — your report and ADRs are unusually well-matched** |

**Second tier, several of them your project's direct neighbours:** 🔴 **Mullvad** (Sweden — you built the network layer for their browser) · **Brave** · **Proton** · **Nym** · **Protocol Labs / libp2p** · **Grafana Labs** (remote-first) · 🔴 **ClickHouse, Confluent, Redpanda, Materialize, StarTree, Snowflake** (**where 15-445 and 15-721 pay**) · **Elastic** · **HashiCorp** (Consul is SWIM in production) · **Canonical** (fully remote, global hiring, heavy systems interviews) · **Bloomberg** London (large C++) · **Booking.com**, **Adyen**, **Klarna** infra.
**Calibration tier** (W44–55, no cooldown risk): Instabug, Swvl, Halan, Paymob, MaxAB (Cairo); Careem, Talabat, Tabby (Gulf); any European startup with a real systems interview.

## J.7 — CV versions
**One page. Every line traceable to something in the repo the day you write it.** Structure: name, GitHub, **"Cairo, Egypt · open to relocation · requires EU/UK sponsorship"** · two-line summary · 🔴 **SELECTED PROJECT — ADYTON, 5–7 bullets, above employment** · Logic Leap, 3–4 quantified bullets · 🔴 **a COURSEWORK line — see below** · Skills · **Education, one line, last.**
> **The degree line:** *"BSc Management Information Systems, [University], [year]."* **No parenthetical. No "(self-taught in CS)". No apologetic adjective.**
> 🔴 **The coursework line, which is new and which the two-year plan earns you:** *"Completed, with all labs: CMU 15-213, 15-445, 15-721 · MIT 6.5840, 6.1810, 6.858 · Stanford CS144 · Stanford Cryptography I."* **That is one line and it does more work against the equivalent-experience clause than anything else on the page.**

| Version | Week | Adds |
|---|---|---|
| v1 | 27 | ⚙️ Sphinx in C++ with the safety apparatus; kernel-enforced compartments; the leak suite in CI |
| v2 | 43 | Per-hop QUIC and the head-of-line-blocking measurement; the 30-node mesh with sub-second churn recovery; **CS144 and 15-213 complete** |
| v3 | 50 | ☕ Raft twice (Go and Java); epoch consensus at 100% agreement; **fork detection**; **6.5840 complete with all five labs** |
| **v4** | **55** | 🎯 **The applying version.** The operational shell: k8s, zero-drop rolling restarts, Terraform + OIDC, SLOs, $0/month |
| v5 | 76 | ⭐ AS-aware selection and **the published trade-off curve**; the attack lab's compromise probabilities; **6.1810 complete** |
| v6 | 98 | Privacy Pass credentials; the DP-budgeted telemetry and the attack it defeats; **the Tor benchmark table**; **15-445 complete** |
| v7 | 104 | The full eight-course line; reproducible builds; the paper; Arti contributions |

## J.8 — Applications
| Weeks | Volume | Targets |
|---|---|---|
| 44–55 | 2–3/month | **Calibration tier only** — real loops, low cost of a poor performance |
| 56–70 | 10/week | 🔴 **Cloudflare, Fastly, Tailscale, Mullvad first** — your best-fit tier — then tier-1 EMEA |
| 71–90 | 8/week | Remaining tier-1 and second tier. **Every completed course makes you better in the loops you are already sitting** |
| 91–104 | 6/week | Mostly conversion now |

**≈250 applications across Year 2**, every one logged in `career/APPLICATIONS.md` with date, company, office, role, referral (y/n, by whom), response, stage, outcome. **Sequence your loops:** 3–4 companies you care less about *first*; your fifth loop is dramatically better than your first. **Then overlap the real ones so offers arrive within ~2 weeks** — competing offers are the only real leverage.
### 🚨 If the response rate is low (checked W70, ~150 out)
**Below 10%, stop and diagnose before sending more with the same CV.** In order: **targeting** (reqs wanting 5+ years will not respond) · **the sponsorship filter** (invisible, and not about you) · 🔴 **the top third of the CV** — if it does not contain **Java (52.7%), distributed systems (48.4%), AWS (48.4%), Python (43%), Go (37.6%), C++ (19.4%), Kubernetes (30.1%)** it is miscalibrated. **Sphinx and guard placement are interview content; the top of the CV is screening surface** · **referral ratio** — under a third referred? The fix is J.4, not more applications. **Fix in W71. Do not respond to a low response rate by increasing volume.**

## J.9 — Negotiation (W95+)
**Never give a number first**, including on the recruiter's first call — *"I'd like to focus on whether this is the right fit; I'm confident we can align on compensation"* is a complete and expected answer. **Competing offers are the only real leverage** — hence overlapping loops. **Negotiate the whole package:** base · equity **and its vesting schedule** · sign-on (most flexible) · **level — worth more than any of the above over three years** · start date · **relocation and visa costs, which candidates moving from outside the EU routinely forget to ask for.** 🔴 **Applying from Egypt creates an anchoring risk** — recruiters may benchmark against Egyptian salaries. **Do not accept that framing**; compensation is for the role in that location, and know your target level's `levels.fyi` number for that company and office **before the first call.** **Read Haseeb Qureshi, "Ten Rules for Negotiating a Job Offer."** Be gracious; you will work with these people.

## J.10 — What the loops look like (verify with your recruiter)
**Google:** phone screen → 2–3 coding, 1 system design, 1 Googleyness & Leadership → **hiring committee and team matching** (a strong loop can stall at team match — normal, not a rejection). **Meta:** phone screen (**2 problems in 45 min — speed matters more here than anywhere**) → 2 coding, 1 design, 1 behavioural. **Amazon:** OA → 4–5 rounds, **every round includes Leadership Principle questions**; the **Bar Raiser** is external with veto power. **Microsoft:** coding + design + an "as appropriate" round with a senior leader. 🔴 **Cloudflare / Fastly / Tailscale / Mullvad:** **practical over puzzle** — debugging unfamiliar code, extending real code, deep protocol and systems discussion. **Adyton plus eight courses prepares you for these better than any other combination, and these are also your best-fit employers.**
**Leveling:** L3/E3 (new grad) → **L4/E4 (2–5 yrs)** → **L5/E5 (5+ yrs, owns ambiguous projects end to end — where system design decides it).** **You will be ~4 years' experience at W104.** Interview for the level your evidence supports; being under-levelled costs years of compensation, so push back with evidence if the loop went well.

---
---

# 📅 The 104-Week Calendar

**Year 1 week: 32h = 11 Courses / 11 Depth / 8 Interview / 2 Craft.** **Year 2 week: 32h = 8 Courses / 10 Depth / 10 Interview / 4 Career.**
Your shape: **4h weekdays + 6h each weekend day.** **Weekday evenings are lectures, reading, DSA and system design. The weekend blocks are labs and Adyton** — course labs and protocol work both need uninterrupted hours and neither survives being chopped into evenings.

**🛌 Rest weeks (10h): 6, 19, 26, 43, 58, 76, 92, 104.** **🔧 Buffer weeks: 34, 52, 66, 84.** **🌙 Ramadan (20h): 22–25 and 72–75** (W26 and W76 are rest weeks and carry Eid al-Fitr). **Eid al-Adha (26h): 36 and 86.**

> 🔴 **The two numbers, and why they differ.** The calendar below **allocates 3,044 hours.** §II commits **2,485 hours to named deliverables.** The difference — **~559 hours — is deliberate slack, distributed across every week rather than parked at the end.** That is not padding: over 104 weeks you will have illnesses, work crunches, a lab that takes three times its estimate, and weeks where life simply wins. **A two-year plan with no slack fails in month five.** If you find yourself consistently finishing a week's named work early, the slack goes to the courses — they are the thing you cannot get back later.

## Year One — W1–52

| Wk | Starts | L | Course | Focus | C | D | I | J | Tot |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-14 | 0 | 15-213 | Repo, CI, 4 toolchains, `latency-lab` · 🔴 `docs/legal.md` · prompts/ | 11 | 11 | 8 | 2 | **32** |
| 2 | 09-21 | 0 | 15-213 | 🔴 SCALE-RISK: node ceiling, Oracle RTT · `lab/bench` open-loop · `sickbay` | 11 | 11 | 8 | 2 | **32** |
| 3 | 09-28 | 0 | 15-213 | Cache/false-sharing walls measured · latency ladder chart | 11 | 11 | 8 | 2 | **32** |
| 4 | 10-05 | 0 | 15-213 | `sickbay` 8 pathologies · benchstat CI gate | 11 | 11 | 8 | 2 | **32** |
| 5 | 10-12 | 0 | 15-213 | 15-213 L9–L10 land · working-set sweep | 11 | 11 | 8 | 2 | **32** |
| 6 | 10-19 | 0 | 15-213 | 🛌 REST — L0 exit exam, category count | 0 | 0 | 6 | 4 | **10** |
| 7 | 10-26 | 1 | 15-213 | 🔴 6.858 L1 · Trilemma paper · the naive relay, attacked 5 ways | 11 | 11 | 8 | 2 | **32** |
| 8 | 11-02 | 1 | 15-213 | ⚙️ ASan/UBSan/TSan in CI · libFuzzer on the parser | 11 | 11 | 8 | 2 | **32** |
| 9 | 11-09 | 1 | 15-213 | ⚙️ `cpp-subset.md` · clang-tidy · RapidCheck codec | 11 | 11 | 8 | 2 | **32** |
| 10 | 11-16 | 1 | 15-213 | ⚙️ PROMPT 3 on my own parser · the fuzzer's bugs written up | 11 | 11 | 8 | 2 | **32** |
| 11 | 11-23 | 1 | 15-213 | 🔴 `threat-model.md` v1 · README v1 · **D0** | 11 | 11 | 8 | 2 | **32** |
| 12 | 11-30 | 2 | 15-213 | 🔴 6.858 L19 (Tor paper) · crypto: nonce-reuse experiment | 11 | 11 | 8 | 2 | **32** |
| 13 | 12-07 | 2 | 15-213 | X25519 + HKDF key schedule · zeroizing types | 11 | 11 | 8 | 2 | **32** |
| 14 | 12-14 | 2 | 15-213 | Sphinx header construction · Malloc Lab | 11 | 11 | 8 | 2 | **32** |
| 15 | 12-21 | 2 | 15-213 | 🔴 The onion shrinks — constant-size padding · Proxy Lab | 11 | 11 | 8 | 2 | **32** |
| 16 | 12-28 | 2 | 15-213 | Per-hop MAC, replay set · **Arti architecture read** | 11 | 11 | 8 | 2 | **32** |
| 17 | 01-04 | 2 | Boneh | Boneh W1–2 · RapidCheck size invariant | 11 | 11 | 8 | 2 | **32** |
| 18 | 01-11 | 2 | Boneh | Boneh W3–4 · single-pass vs telescoping measured | 11 | 11 | 8 | 2 | **32** |
| 19 | 01-18 | 2 | Boneh | 🛌 REST — **D1**, L2 exam, category count | 0 | 0 | 6 | 4 | **10** |
| 20 | 01-25 | 3 | Boneh | 🤝 **REFERRALS OPEN** · netns + veth + nftables default-drop | 11 | 11 | 8 | 2 | **32** |
| 21 | 02-01 | 3 | Boneh | The sealed `Identity` type · Boneh finishes | 11 | 11 | 8 | 2 | **32** |
| 22 | 02-08 | 3 | 🌙 catch-up | 🌙 WebRTC + IPv6 leak tests | 7 | 5 | 5 | 3 | **20** |
| 23 | 02-15 | 3 | 🌙 catch-up | 🌙 DNS leak + kill-switch tests (20/20) | 7 | 5 | 5 | 3 | **20** |
| 24 | 02-22 | 3 | 🌙 catch-up | 🌙 Cross-compartment: cookies, TLS tickets | 7 | 5 | 5 | 3 | **20** |
| 25 | 03-01 | 3 | 🌙 catch-up | 🌙 Fingerprint uniformity, two machines | 7 | 5 | 5 | 3 | **20** |
| 26 | 03-08 | 3 | 🌙 catch-up | 🛌 REST · Eid — **D2 ★** · 🔴 CS144 handouts mirrored | 0 | 0 | 6 | 4 | **10** |
| 27 | 03-15 | 3 | CS144 | CS144 check0–1 · `browser-delta.md` · **CV v1** · Blog 1 | 11 | 11 | 8 | 2 | **32** |
| 28 | 03-22 | 4 | CS144 | CS144 check2 · the HOL-blocking experiment | 11 | 11 | 8 | 2 | **32** |
| 29 | 03-29 | 4 | CS144 | CS144 check3 (sender) · ngtcp2 transport | 11 | 11 | 8 | 2 | **32** |
| 30 | 04-05 | 4 | CS144 | CS144 check3 · circuit↔stream mapping | 11 | 11 | 8 | 2 | **32** |
| 31 | 04-12 | 4 | CS144 | CS144 check4 — my TCP replaces the kernel's | 11 | 11 | 8 | 2 | **32** |
| 32 | 04-19 | 4 | CS144 | 🔴 QUIC fingerprint normalisation + CI capture diff | 11 | 11 | 8 | 2 | **32** |
| 33 | 04-26 | 4 | CS144 | CS144 check5 · circuit teardown, 100 cycles clean | 11 | 11 | 8 | 2 | **32** |
| 34 | 05-03 | 4 | CS144 | 🔧 BUFFER · CS144 check6 (IP router) | 11 | 11 | 8 | 2 | **32** |
| 35 | 05-10 | 4 | CS144 | CS144 check7 · **D3** · build p50 <250ms | 11 | 11 | 8 | 2 | **32** |
| 36 | 05-17 | 5 | CS144 | 🌙 Eid · **AWS signup + $5 alarm** · CS144 finishes | 9 | 9 | 6 | 2 | **26** |
| 37 | 05-24 | 5 | CS144 | 6.5840 L1–L2 · NAT: two peers cannot connect | 11 | 11 | 8 | 2 | **32** |
| 38 | 05-31 | 5 | CS144 | STUN punching + relay fallback · fraction measured | 11 | 11 | 8 | 2 | **32** |
| 39 | 06-07 | 5 | 6.5840 | 6.5840 L3 (GFS) + Lab 1 · SWIM gossip | 11 | 11 | 8 | 2 | **32** |
| 40 | 06-14 | 5 | 6.5840 | `meshsim`: clock, network, asymmetric partition | 11 | 11 | 8 | 2 | **32** |
| 41 | 06-21 | 5 | 6.5840 | phi-accrual vs fixed timeout chart · **first human mock** | 11 | 11 | 8 | 2 | **32** |
| 42 | 06-28 | 5 | 6.5840 | Churn recovery p50/p99 · graceful drain | 11 | 11 | 8 | 2 | **32** |
| 43 | 07-05 | 5 | 6.5840 | 🛌 REST — **D4**, **CV v2**, category count | 0 | 0 | 6 | 4 | **10** |
| 44 | 07-12 | 6 | 6.5840 | ☕ 6.5840 L4 (Paxos), L6 (Raft 1) · Java 21 ramp | 11 | 11 | 8 | 2 | **32** |
| 45 | 07-19 | 6 | 6.5840 | 6.5840 L7 (Raft 2) + **Lab 3: Raft in Go** | 11 | 11 | 8 | 2 | **32** |
| 46 | 07-26 | 6 | 6.5840 | 6.5840 L8 (Linearizability) · Lab 3 continues | 11 | 11 | 8 | 2 | **32** |
| 47 | 08-02 | 6 | 6.5840 | 6.5840 L9 (Zookeeper) + **Lab 4: KV on Raft** | 11 | 11 | 8 | 2 | **32** |
| 48 | 08-09 | 6 | 6.5840 | L13 (Chain Replication) · Raft in Java begins · `adyton-measure` | 11 | 11 | 8 | 2 | **32** |
| 49 | 08-16 | 6 | 6.5840 | 🔴 **6.5840 L19 SUNDR** · hash-chained epoch documents | 11 | 11 | 8 | 2 | **32** |
| 50 | 08-23 | 6 | 6.5840 | Fork detection + client hash gossip · **CV v3** | 11 | 11 | 8 | 2 | **32** |
| 51 | 08-30 | 6 | 6.5840 | L21 (PBFT) + **Lab 5: sharded KV** · anonymity-set measurement | 11 | 11 | 8 | 2 | **32** |
| 52 | 09-06 | 6 | 6.5840 | 🔧 BUFFER · **D5** · 🚩 **YEAR-ONE GATE** · Blog 2 | 11 | 11 | 8 | 2 | **32** |

## Year Two — W53–104

| Wk | Starts | L | Course | Focus | C | D | I | J | Tot |
|---|---|---|---|---|---|---|---|---|---|
| 53 | 2027-09-13 | 7 | 6.1810 | 6.1810 L1–L2 + lab util · k8s: 30-node mesh | 8 | 10 | 10 | 4 | **32** |
| 54 | 09-20 | 7 | 6.1810 | L3–L4 (page tables) + lab syscall · rolling restart, zero drops | 8 | 10 | 10 | 4 | **32** |
| 55 | 09-27 | 7 | 6.1810 | The 3am dashboard · `gatekeep` · **CV v4** | 8 | 10 | 10 | 4 | **32** |
| 56 | 10-04 | 7 | 6.1810 | 🎯 **APPLICATIONS OPEN — first 12 sent** · `costwatch` + tested $1 alarm | 8 | 10 | 10 | 4 | **32** |
| 57 | 10-11 | 7 | 6.1810 | `slo.md` · **FULL LOOP #1** · RCA <5min on video | 8 | 10 | 10 | 4 | **32** |
| 58 | 10-18 | 7 | 6.1810 | 🛌 REST — **D6**, category count · Blog 3 | 0 | 0 | 6 | 4 | **10** |
| 59 | 10-25 | 8 | 6.1810 | 6.1810 L6–L8 + lab pgtbl · CAIDA load, valley-free inference | 8 | 10 | 10 | 4 | **32** |
| 60 | 11-01 | 8 | 6.1810 | L9–L10 (locking) · 🔴 inference validated vs RouteViews | 8 | 10 | 10 | 4 | **32** |
| 61 | 11-08 | 8 | 6.1810 | L11–L12 + lab traps · adversary presets | 8 | 10 | 10 | 4 | **32** |
| 62 | 11-15 | 8 | 6.1810 | L13–L14 (crash recovery) · compromise probability: Adyton vs Tor | 8 | 10 | 10 | 4 | **32** |
| 63 | 11-22 | 8 | 6.1810 | + lab cow · guard-compromise curve | 8 | 10 | 10 | 4 | **32** |
| 64 | 11-29 | 8 | 6.1810 | Sybil cost curve (USD/month) · churn adversary | 8 | 10 | 10 | 4 | **32** |
| 65 | 12-06 | 8 | 6.1810 | `lab/reproduce.sh` · GCP window planned | 8 | 10 | 10 | 4 | **32** |
| 66 | 12-13 | 8 | 6.1810 | 🔧 BUFFER · **D7** · Blog 4 | 8 | 10 | 10 | 4 | **32** |
| 67 | 12-20 | 9 | 6.1810 | 6.1810 L15–L17 + lab net · three selectors in Python | 8 | 10 | 10 | 4 | **32** |
| 68 | 12-27 | 9 | 6.1810 | L18–L19 + lab lock · winner chosen on data | 8 | 10 | 10 | 4 | **32** |
| 69 | 01-03 | 9 | 6.1810 | L20 (networking), L21 (Meltdown) + lab fs · C++ port + cross-lang vectors | 8 | 10 | 10 | 4 | **32** |
| 70 | 01-10 | 9 | 6.1810 | L22 + lab mmap — **6.1810 COMPLETE** · guard-placement adversary | 8 | 10 | 10 | 4 | **32** |
| 71 | 01-17 | 9 | slack | Slack · randomness parameter · AS graph in the epoch doc | 8 | 10 | 10 | 4 | **32** |
| 72 | 01-24 | 9 | 🌙 lectures | 🌙 The sweep begins | 5 | 6 | 6 | 3 | **20** |
| 73 | 01-31 | 9 | 🌙 lectures | 🌙 The sweep · compromise probability by setting | 5 | 6 | 6 | 3 | **20** |
| 74 | 02-07 | 9 | 🌙 lectures | 🌙 The sweep · adversary selection rate by setting | 5 | 6 | 6 | 3 | **20** |
| 75 | 02-14 | 9 | 🌙 lectures | 🌙 🔴 **THE TRADE-OFF CURVE** · operating point chosen | 5 | 6 | 6 | 3 | **20** |
| 76 | 02-21 | 9 | 🌙 lectures | 🛌 REST · Eid — **D8**, **CV v5**, category count · Blog 5 | 0 | 0 | 6 | 4 | **10** |
| 77 | 02-28 | 10 | 15-445 | ☕ 15-445 L0–L2 + P0 · the accountability bind reproduced | 8 | 10 | 10 | 4 | **32** |
| 78 | 03-06 | 10 | 15-445 | L3–L5 + P1 (buffer pool) · Privacy Pass issuance | 8 | 10 | 10 | 4 | **32** |
| 79 | 03-13 | 10 | 15-445 | L6–L8 + P1 · redemption + unlinkability test | 8 | 10 | 10 | 4 | **32** |
| 80 | 03-20 | 10 | 15-445 | L9–L11 + **P2 (B+Tree)** · revocation without linkage · `adyton-gateway` | 8 | 10 | 10 | 4 | **32** |
| 81 | 03-27 | 10 | 15-445 | L12–L14 + P2 · rate limiting with no per-user log | 8 | 10 | 10 | 4 | **32** |
| 82 | 04-03 | 10 | 15-445 | P2 · credential-gated admission + clustering | 8 | 10 | 10 | 4 | **32** |
| 83 | 04-10 | 10 | 15-445 | Sybil cost re-measured with admission · fairness via earned credentials | 8 | 10 | 10 | 4 | **32** |
| 84 | 04-17 | 10 | 15-445 | 🔧 BUFFER · **D9** · `trust-model.md` + ADR-0007 · Blog 6 | 8 | 10 | 10 | 4 | **32** |
| 85 | 04-24 | 11 | 15-445 | 15-445 L15–L18 + P3 · 🔴 the metrics attack on my own telemetry | 8 | 10 | 10 | 4 | **32** |
| 86 | 05-01 | 11 | 15-445 | 🌙 Eid · L19 (MVCC), L20 (logging) + P3 | 7 | 8 | 8 | 3 | **26** |
| 87 | 05-08 | 11 | 15-445 | L21 (recovery) + **P4 (MVCC)** · private aggregation, ε chosen | 8 | 10 | 10 | 4 | **32** |
| 88 | 05-15 | 11 | 15-445 | L22–L23 + P4 · budget that fails closed · naive endpoint deleted | 8 | 10 | 10 | 4 | **32** |
| 89 | 05-22 | 11 | 15-445 | L24–L25 · 20 incidents begin · 🔴 the clock-skew incident | 8 | 10 | 10 | 4 | **32** |
| 90 | 05-29 | 11 | 15-445 | **15-445 COMPLETE** · 4 famous outages reproduced | 8 | 10 | 10 | 4 | **32** |
| 91 | 06-05 | 11 | 15-721 | 15-721 L0–L4 · error-budget burn · `sim-fidelity.md` | 8 | 10 | 10 | 4 | **32** |
| 92 | 06-12 | 11 | 15-721 | 🛌 REST — **D10**, category count · Blog 7 | 0 | 0 | 6 | 4 | **10** |
| 93 | 06-19 | 12 | 15-721 | 15-721 L5–L6 (vectorized) · 🔴 predict top 3 costs, commit, then profile | 8 | 10 | 10 | 4 | **32** |
| 94 | 06-26 | 12 | 15-721 | L7–L8 (codegen, scheduling) · batched I/O `sendmmsg`/GSO | 8 | 10 | 10 | 4 | **32** |
| 95 | 07-03 | 12 | 15-721 + 6.858 | 6.858 L1–L4 · L12 (networking protocols) · >200k pps/core | 8 | 10 | 10 | 4 | **32** |
| 96 | 07-10 | 12 | 15-721 + 6.858 | 6.858 L5–L8 · 🔴 **THE TOR TABLE**, one script | 8 | 10 | 10 | 4 | **32** |
| 97 | 07-17 | 12 | 15-721 + 6.858 | L16 (cost models) · aarch64 delta · `pgshift` | 8 | 10 | 10 | 4 | **32** |
| 98 | 07-24 | 12 | 15-721 + 6.858 | **15-721 COMPLETE** · `docs/REPORT.md` · **D11** · **CV v6** · Blog 8 | 8 | 10 | 10 | 4 | **32** |
| 99 | 07-31 | 13 | 15-721 + 6.858 | 6.858 L9–L13 + lab 1 (buffer overflows) · WF dataset ≥100×50 | 8 | 10 | 10 | 4 | **32** |
| 100 | 08-07 | 13 | 15-721 + 6.858 | L19 re-watch + labs 2–3 · DF + Var-CNN trained · 🔴 PROMPT 5 on the whole system | 8 | 10 | 10 | 4 | **32** |
| 101 | 08-14 | 13 | 6.858 | L20 (timing attacks) + lab 4 · 🔴 the shaping curve | 8 | 10 | 10 | 4 | **32** |
| 102 | 08-21 | 13 | 6.858 | L21–L23 + lab 5 (Adyton as the project) · **10 ADRs · LIMITATIONS · COMPARISON** | 8 | 10 | 10 | 4 | **32** |
| 103 | 08-28 | 13 | 6.858 | 🔴 Reproducible builds ×2 · threat model published · install guide ×3 testers · **RETROSPECTIVE** | 8 | 10 | 10 | 4 | **32** |
| 104 | 09-04 | 13 | 6.858 | 🛌 REST — **D12** · external peers · the 45-min demo recorded · **CV v7** · `NEXT.md` · Blogs 9–10 | 0 | 0 | 6 | 4 | **10** |

<!-- TOTAL 3044 -->

**No week exceeds 32 hours.** The 12-month versions of this plan had four over-budget weeks; the two-year version has none, because the courses got the room they actually need.

---
---

# ✂️ The Cut Order

**Cut in this sequence, top first. Never out of order, and never silently — every cut gets a line in `docs/LIMITATIONS.md` saying what was dropped and why.**

| # | What gets cut | Costs you | Why it's first |
|---|---|---|---|
| 1 | **`shape` — the reduced traffic-shaping work** (L13) | A paragraph in the threat model. The full WF evaluation was already moved to `NEXT.md` | Last, self-contained, and L9 already gives you the publishable contribution |
| 1b | **`1brc` pass 3** — keep the W5 naive pass and the W93 assault, drop any further tuning | Leaderboard position, not the artifact. **You still have the two-year delta, which is the point** | Diminishing returns past the first big win |
| 2 | **`pgshift`** (W97) | PostgreSQL evidence goes from strong to adequate | 15-445's five projects already demonstrate storage far better than a migration script |
| 3 | **CMU 15-721** — lectures 9–11, 13–15, 17–22 (keep 6, 7, 8, 12, 16) | The parallel career investment thins. **Keep the five that serve Adyton** | It is the one course explicitly *not* on the critical path. **Move the rest to `NEXT.md`** |
| 4 | **The aarch64 port and x86/ARM analysis** (W97) | A free result and a blog post | Genuinely optional |
| 5 | **Two of the four reproduced outages** (W90) | The chaos programme weakens but survives at two | The 20 self-inflicted incidents matter more than the famous ones |
| 6 | **Client-side fork-hash gossip** (W50) — ship hash chaining only | Fork detection becomes theoretical rather than measured. **Document the residual exposure in the threat model** | Hash chaining alone still bounds the attack; the gossip is the measurement |
| 7 | **The GCP 200-node window** (W65) | Simulator validation at scale; `sim-fidelity.md` gets weaker and you must say so | Costs credibility, not correctness |
| 8 | **CLAPS as a third candidate selector** (W67) | One row in a comparison table | Take Counter-RAPTOR-style on the literature's evidence; spend the time on the sweep |
| 9 | **Fairness via earned credentials** (W83) — ship the design doc plus a throttling stopgap | An implementation. **Say in the README that fairness is designed, not built** | A legitimate answer; a broken mechanism is not |
| 10 | **MIT 6.858 labs 2–4** (keep lab 1 and lab 5) | Three labs. **Keep lab 1 — it is the one that justifies your C++ subset — and lab 5, which is Adyton itself** | It is the last course and the most compressible |
| 11 | **The third hop option** and per-application isolation beyond the browser | Two paragraphs in the spec | "Designed, not yet built, here is why it is next" is a fine answer |

## 🔴 What is NEVER cut

| Never cut | Because |
|---|---|
| ⚙️ **The C++ safety apparatus (L1, and every week after)** | **It is the argument for having chosen C++ at all.** A week with the sanitizer job disabled is a week the language choice became indefensible |
| **`leakproof` and the compartment boundary (L3)** | **One leak across compartments defeats the entire product.** It is what makes Adyton a product rather than a VPN |
| **CMU 15-213, complete with all nine labs** | It is the foundation every other course assumes. **Cutting it makes the other seven worse** |
| **Stanford CS144's labs** | Without building a TCP you can quote QUIC's advantages but not derive them. And the handouts vanish yearly — you cannot come back for it |
| **MIT 6.5840, complete with all five labs** | Distributed systems is 48.4%. The labs are the evidence |
| **The epoch-agreement test (L6)** | Divergence is a fingerprint. Without it the privacy claim is false |
| **The guard-placement sweep (L9)** | The only genuinely novel thing you produce. It is the write-up |
| **The operational shell (L7)** | **The shell alone is 15.1% coverage; a clever core alone is 6.5%.** This is what the screen reads |
| **Java (L6, L10)** | +14.1 points, and 46.8% of your residual gap |
| **The Track I hours** | The only track that degrades irreversibly. A missed week is not recoverable by working harder later |
| **Applications from W56** | The plan's entire purpose. Everything else is instrumental |
| **The Logic Leap track (§XV.5)** | 36.6% + 34.4% + 31.2% + 17.2%, and nothing else in the plan touches them |
| **The threat model and the honesty rules** | The moment you overclaim, every true thing you measured stops being believed |

🔴 **The rule when a course and an Adyton level collide: the course wins and the level slips.** Adyton is yours and will wait. A course's labs, once you are past them, you will not come back to — and CS144's handouts literally disappear. **This is the opposite of the instinct and it is the right call.**

**The decision is forced at six gates: W26, W43, W52 (year-one gate), W66, W84, W92.** At each, count how many weeks behind you are and cut that many items off the top. **Cutting at a gate is a decision. Discovering in W100 that you cannot finish is a failure.**

---
---

# 📊 ASSESSMENT: The Three Proofs

| Proof | What | Why |
|---|---|---|
| **1. The Exam** | The written questions at each level's end, no notes, timed | Retrieval under pressure — the interview condition |
| **2. The Artifact** | The project, exit criteria met, **numbers published**; and **the Atlas checkbox ticked** | That you can actually build it and actually finished the course |
| **3. The Interrogation** | 🤖 **PROMPT 2 on the level's hardest topic**, then a **10-minute teach-back to a camera**, no notes, with a diagram | **The strictest test there is. You cannot fake teaching, and PROMPT 2 finds what the exam missed** |

**Fail any of the three and the level is not done.**

## The Final Gauntlet — Week 55, the week before applications open
| Day | Challenge | Pass condition |
|---|---|---|
| 1 | 4 LeetCode Mediums + 1 Hard, timed, **narrated aloud, recorded** | 4/5 unaided within time |
| 2 | 2 system designs, 45 min each, on video | Both hit the rubric |
| 3 | **Debug a sabotaged Adyton** — have a peer break it without telling you what | Root cause in <45 min **with evidence** |
| 4 | All 14 behavioural stories on video, cold | Each ≤90s, quantified, first person, **≥4 from Logic Leap** |
| 5 | Write a full design doc for a **novel** problem in 3 hours | All 10 sections, **3+ real alternatives** |
| 6 | **Teach-back: the Sphinx position-hiding property · fork consistency and why Raft is not enough · ⚙️ why C++ and what it costs.** 10 min each | No notes, correct, with diagrams |
| 7 | Watch every video from days 1–6 and **grade yourself against the rubrics** | Honest scoring |

**Pass = ready to apply. Fail any day → that is your next two weeks, and applications slip to W58.** *(A second Gauntlet runs at W95, before the strongest loops.)*

## The spaced-repetition deck
**One card per non-obvious fact, written by you.** Downloaded decks do not work; cards you write do. **Target ~1,000 over two years.** Categories: latency numbers · Raft rules · the Sphinx field layout · NAT type behaviours · the consistency-model hierarchy · ⚙️ C++ lifetime and UB rules · JVM GC facts · algorithm complexities · Linux commands and what they *answer* · **the 166 lectures' key results** · **your own measured numbers.** **15 min/day, non-negotiable** — the difference between knowing something in month 3 and knowing it in month 24 when the interview happens.

---
---

# 📈 TRACKING & RE-PLANNING

| File | Contains | Written |
|---|---|---|
| `LOG.md` | Hours by track, task outcomes, weekly review, level checkpoint | Daily + Sunday |
| 🔴 `ATLAS.md` | **The 166 lecture and 41 lab checkboxes, ticked with dates** | As you complete each |
| `dsa/FAILURES.md` | Every failed problem, in the Track I format | As it happens |
| 🔴 `dsa/OA-LOG.md` | **Every OA drill: problems, clock budget per problem, tests-written-first y/n, result** | Weekly from W53 |
| `dsa/mocks.md` | Every mock and full loop, **scoring correctness and communication separately** | As they happen |
| `career/APPLICATIONS.md` | Every application, with response and stage | As it happens |
| `career/LOGICLEAP.md` | The six deliberate situations from §XV.5, dated | As they happen |
| `docs/prompts/` | The five archetypes as files, so you paste rather than retype | Week 1 |

## Daily — 2 minutes
```
2027-04-18 · C:2.0 D:4.0 I:1.5 J:0 · CS144 check3 retransmission timer passing at last;
             the bug was RTO doubling on every ack, not every timeout. ngtcp2 handshake
             now byte-identical between two peers. (+2h over estimate on check3)
```
**Log the hours you actually worked, not the hours you sat at the desk.** The W103 retrospective is only useful if this is honest, and its value is telling you your real estimation ratio — which you cannot learn from inflated data.

## Weekly review — Sunday, 30 minutes
1. **Hours by track vs budget.** A deficit up to 3h is noise. **Three consecutive deficit weeks is a signal.**
2. 🔴 **Atlas progress: lectures and labs ticked this week, and are you on the course's schedule?** A course silently slipping is the most dangerous failure in this plan, because it compounds into the next course.
3. **Which tasks met their acceptance criterion?** Met / not met. **"Partially" is not a category — force it.**
4. **Which targets did you set before measuring, and what did you get?** **Both numbers, always.**
5. **What did not finish, and does it block next week?** Blocks → top of next week, something drops. Does not → the buffer list. **Never silently carry unfinished work forward.**
6. **Interview track:** attempted / solved / failed / re-solved, **and design docs written.**
7. **Logic Leap:** anything worth a §XV.5 entry? **If six weeks pass with nothing, go and create the situation.**
8. **One sentence: the biggest risk to the next four weeks.** A specific thing, not a feeling.

## Level checkpoint — at each boundary
1. **Exit criteria, one at a time. Met, or waived in writing with a reason. No third option.**
2. **Hours: actual vs budget, and cumulative.** The cumulative number is the one that matters.
3. 🔴 **Is the repository interview-ready RIGHT NOW?** Three checks, *performed*: does `make demo` work on a clean clone — **actually run it** · does the README describe what exists rather than what is planned · **can you speak for 45 minutes about it today, without preparation?** If any is no, fixing it is next week's top priority. **The plan is built so you can stop at any week and still be a coherent candidate.**
4. **The corpus gaps** — Java 52.7%, AWS 48.4%, distributed systems 48.4%, K8s 30.1%, C++ 19.4%, PostgreSQL 19.4%, Kafka 20.4%, observability 22.6%, on-call 17.2%. One line each: closed / in progress / not started, **and what the evidence is. Not what you read. What is running.**
5. 🔴 **Failure-category count** from `dsa/FAILURES.md`.
6. **From W20:** referral pipeline — conversations this month, people who now know what you are building.
7. **From W56:** applications sent, responses, response rate, stage conversion, what is stalled.
8. **One paragraph: is the plan still right?** Not "am I on schedule" — whether it still describes the correct work.

## 🚨 Re-plan triggers

| Trigger | Response |
|---|---|
| **Cumulative deficit > 60h** | **Cut scope in the §XVII order. Do not compress estimates** |
| 🔴 **A course is 3+ weeks behind its Atlas schedule** | **The most important trigger in the two-year plan.** The course finishes and the Adyton level slips — not the reverse. Take it from the next buffer week |
| **All four buffer weeks gone before W66** | Estimates are systematically wrong. **Recompute Levels 10–13 with your measured ratio from `LOG.md`** |
| **Two consecutive checkpoints where the repo is not interview-ready** | **Stop feature work entirely for one week.** README, build, demo. Overrides everything |
| **Three consecutive weeks of Interview track under 6h** | The project is eating the track you explicitly protected. **Invert the week: interview first, everything else with what is left, for two weeks** |
| ⚙️ **The sanitizer or fuzz job has been disabled for more than one week** | 🔴 **Stop and re-enable it.** The C++ choice is only defensible while this holds |
| **CS144's handouts are gone and you did not mirror them** | Find a community mirror immediately; if none, substitute the 6.1810 `net` lab plus RFC 9293 reading, **and record in `LIMITATIONS.md` that you did not build a TCP.** This is why W26 mirrors them |
| **The W2 scale spike fails** | **Decide in W2.** Substitute: 10–15 real nodes with `meshsim` carrying scale from month one, stated in the README as the primary limitation |
| **A level runs 2+ weeks over** | Do not compress the next. Take it from the buffer and cut the top item in §XVII |
| **Response rate <10% at W70** | Diagnose per §XV.8 **before** sending more |
| 🔴 **You have not opened the repo in 10 days** | **The most important trigger and the easiest to ignore.** Do not restart at 32 hours. One 2-hour session, then one 4-hour, then resume. **Restarting at full intensity after a break is how a one-week gap becomes a two-month one — and over 104 weeks this will happen at least twice** |

## What does NOT trigger a re-plan
**A bad week** — noise. **A missed target** — targets set before measurement are estimates; record both numbers and move on. **A negative result** — being comparable to Tor in Level 8, or a sim-fidelity divergence larger than you hoped, **are results**; they get written up and become interview material. **Feeling behind** — check `LOG.md`. 🔴 **A better project idea** — it will happen, probably around Level 4 and again around Level 9. **The answer is no.** Write it in `docs/IDEAS.md` and continue. **Over two years this temptation is the single largest threat to finishing, and you have already changed spine once, at week zero, when it was free.**

---
---

# 💼 RÉSUMÉ & GITHUB TRANSLATION

```
📌 adyton            Open privacy relay network with per-identity compartmentalisation
                     C++20 · Java 21 · Go · Python
                     ★ architecture diagram + the honesty and scale statements +
                       the headline numbers, all in the first screen

📌 tradeoff-curve    AS-aware path selection makes you predictable. Here is the curve.
                     ★ THE plot. Nobody has published this.

📌 leakproof         The suite that tries to break my own compartments, in CI
                     ★ WebRTC · IPv6 · DNS · kill switch · cross-compartment linkage

📌 hardened      ⚙️  How I made C++ defensible for a hostile-input data plane
                     ★ sanitizers, libFuzzer + corpus, the documented subset,
                       and the three memory bugs my own fuzzer found

📌 tor-bench         Adyton vs Tor: same client, same destinations, same conditions
                     ★ hop counts in the header, my own 3-hop row, one script reproduces it

📌 coursework        Eight courses, 166 lectures, 41 labs — completed, with the code
                     ★ CS144's TCP · 6.5840's Raft and sharded KV · 6.1810's xv6 labs
                       15-445's B+Tree and MVCC · 15-213's allocator and proxy
```

🔴 **That sixth repository is the one the two-year plan earns you, and it is unusual.** Most candidates say they "studied distributed systems." **You will have a repository containing a working TCP, a working Raft, a working sharded fault-tolerant key-value store, a working concurrent B+Tree, a working MVCC engine, a working memory allocator, a working concurrent web proxy and nine xv6 kernel modifications — with MIT's and CMU's own test suites passing.** Point at it in the first line of your CV's coursework section.

**Every README, first screen:** one sentence saying what it is · an architecture diagram · **the headline number or chart** · `make demo`. **Profile README:** three sentences about what you work on, then the six with their numbers. **No badge walls. No language-percentage charts.**

**The answer this buys you** to *"tell me about the most technically challenging thing you've built"*: a 45-minute answer with an architecture diagram you can draw from memory · **three specific bugs and how a simulator you wrote found them** · measured numbers and where the bottleneck is · ⚙️ **a language choice you can defend from both sides** · **the alternatives you rejected, written as ADRs** · **an honest comparison to Tor, which solved this two decades ago** · and **a retrospective with measured estimate-versus-actual across two years and 166 lectures.**

---
---

# 📚 THE LIBRARY

**Courses:** all eight are in §VII with every lecture and lab linked. **That is the primary curriculum and it is not repeated here.**

## Books — with the chapters, never the whole thing
**Kleppmann, *DDIA*** *(owned)* — **ch. 8** (partial failure, **the theoretical spine**), **ch. 9** (consensus), ch. 5, 6, 7, 11 · **Alex Xu, *System Design Interview* Vol. 1 & 2** *(owned)* — Vol 1 ch. 1, 4, 5, 6, 8, 11 · **Bryant & O'Hallaron, *CS:APP* 3rd ed.** — §6.2–6.4, ch. 5, and it is 15-213's textbook so you will read most of it · **Arpaci-Dusseau, *OSTEP*** *(free)* — the companion to 6.1810 · **Kerrisk, *TLPI*** — ch. 28 (namespaces), and the syscall reference for two years · ⚙️ **the C++ Core Guidelines** — the lifetime and bounds profiles, read properly in W9 · ⚙️ **Williams, *C++ Concurrency in Action* 2nd ed.** — ch. 3–5, 7 · **Goetz, *Java Concurrency in Practice*** — ch. 3, 5, 10, 11 · **Aumasson, *Serious Cryptography*** — ch. 8, 10, 11, 12 · **Boneh & Shoup** *(free, `toc.cryptobook.us`)* — §5.4, ch. 9 · **Kurose & Ross** — ch. 3, §5.4 · **Fall & Stevens Vol. 1** — ch. 13–15 · **Petrov, *Database Internals*** — Part I, alongside 15-445 · **Nygard, *Release It!*** — Level 11's most relevant book · **Google *SRE* + *Workbook*** *(free)* — SRE ch. 3, 4, 6, 21, 22; Workbook ch. 5 · **Majors et al., *Observability Engineering*** — ch. 1–6 · **Lukša, *Kubernetes in Action*** — ch. 1–7, 12, 17 · **Dwork & Roth** *(free)* — ch. 2, §3.1–3.3 · **Mitzenmacher & Upfal** — ch. 5, §14.1 · **Ousterhout, *A Philosophy of Software Design*** · **Skiena** — ch. 8, 9 · **Laaksonen** *(free)* — ch. 7, 9, 13–15, 26

## Papers — beyond the ~60 assigned inside the eight courses
| Paper | Week |
|---|---|
| 🔴 **Das et al., Anonymity Trilemma** (S&P 2018) | W7 |
| Dingledine et al., **Tor design paper** | W7 |
| 🔴 **Danezis & Goldberg, Sphinx** (S&P 2009) + **Lightning BOLT #4** | W14 |
| RFC 9000 §2, 5, 12–13, 17 · RFC 9221 | W29 |
| 🔴 **Das et al., SWIM** (DSN 2002) · **φ Accrual** (SRDS 2004) | W39 |
| RFC 4787 §4 · RFC 8445 §2 | W37 |
| 🔴 **Gjengset, "Students' Guide to Raft"** | W44 |
| 🔴 **Mahajan et al., SUNDR** (OSDI 2004) · **Laurie, Certificate Transparency** | W49 |
| 🔴 **Luckie et al., AS Relationships** (IMC 2013) | W59 |
| **Sun et al., Counter-RAPTOR** (S&P 2017) · Astoria · DeNASA | W61 |
| **Elahi et al., Changing of the Guards** · **Douceur, The Sybil Attack** | W63 |
| 🔴 **Wan et al., Guard Placement Attacks** (PoPETs 2019) · **Rochet et al., CLAPS** | W67 |
| 🔴 **Davidson et al., Privacy Pass** (PETS 2018) · RFC 9576/9577 | W77 |
| 🔴 **Jansen & Johnson, PrivCount** (CCS 2016) · **Corrigan-Gibbs & Boneh, Prio** (NSDI 2017) | W85 |
| **Dean & Barroso, The Tail at Scale** · **Gil Tene's talk** | W2, W93 |
| **Sirinam et al., Deep Fingerprinting** (CCS 2018) · WTF-PAD · FRONT | W99 |

**For each: what problem, what was the key insight, what did they give up, what would you do differently, what system today embodies it.** **Sixteen of your own plus ~60 from the courses is around seventy-five papers read properly in two years.**

## Free reference
`aws.amazon.com/builders-library` (all ~20 across L7 and L11) · `k8s.af` (read 10) · `jepsen.io/analyses` and `/consistency` · `sre.google/books` · `github.com/danluu/post-mortems` · `spec.torproject.org` and the **Arti** source · ⚙️ `en.cppreference.com` and the **C++ Core Guidelines** · `book.systemsapproach.org` · `toc.cryptobook.us` · `hpbn.co` · `neetcode.io` · `levels.fyi` · `brooker.co.za`

## People
Martin Kleppmann · **Marc Brooker** (`brooker.co.za`, the best working systems writer today) · **Robert Morris** and **Frans Kaashoek** (6.5840, 6.1810) · **Andy Pavlo** (15-445, 15-721) · **Randal Bryant** and **David O'Hallaron** (15-213) · **Dan Boneh** · **Nick McKeown** and **Philip Levis** (CS144) · **Nick Mathewson** and the Tor Project · ⚙️ **Herb Sutter** and **Chandler Carruth** (C++) · Brendan Gregg · Julia Evans · Dan Luu · Kyle Kingsbury · Hillel Wayne · Charity Majors · Gergely Orosz

---
---

# ✅ PROJECT CATALOG & FINAL CHECKLIST

## The catalog — 🚩 flagship · ⭐ core
**L0** ⭐`latency-lab` · ⭐`lab/bench` open-loop harness · ⭐`sickbay` · ⭐**`SCALE-RISK.md` signed go/no-go** · ⭐🔴**`docs/legal.md`**
**L1** 🚩**#1 `hardened`** — sanitizers, libFuzzer + corpus, `cpp-subset.md`, **and the bugs my own fuzzer found** · ⭐**D0** the un-crashable relay · ⭐the five attacks reproduced · ⭐**`threat-model.md` v1**
**L2** 🚩**#2 `sphinx`** — RapidCheck size invariant, 1h clean fuzz · ⭐**D1** · ⭐single-pass vs telescoping measured · ⭐zeroizing key types
**L3** 🚩**#3 `leakproof`** — five tests in CI · ⭐**D2 ★** unmodified Mullvad Browser in a netns over a circuit · ⭐the sealed `Identity` type · ⭐two-machine fingerprint uniformity · ⭐`browser-delta.md`
**L4** ⭐**D3** per-hop QUIC carrying real HTTP · ⭐🔴**the head-of-line-blocking chart** · ⭐🔴**fingerprint capture-diff in CI**
**L5** 🚩**#4 `meshsim`** — 1,000 seeds nightly, asymmetric partitions, lying peers · ⭐**D4** churn recovery p50<800ms/p99<3s · ⭐NAT >80% direct · ⭐phi-accrual chart · ⭐**the asymmetric-partition test**
**L6** 🚩**#5 `raft-dir`** — Figure 8 as a test, drawable from memory · ⭐**D5 100% epoch-hash agreement under 20% churn** · ⭐🔴**hash chaining + client gossip; fork detection latency measured** · ⭐**the anonymity-set number, before and after**
**L7** ⭐**D6** 30-node mesh on k8s, **rolling restart zero circuits dropped** · ⭐the 3am dashboard, RCA <5min on video · ⭐`gatekeep` · ⭐`costwatch` with a **tested** billing alarm · ⭐`slo.md` · ⭐**$0.00 screenshotted monthly**
**L8** 🚩**#6 `ascorr`** — compromise probability for Adyton **and Tor**, four presets · ⭐🔴**inference validated against RouteViews** · ⭐guard-compromise curve · ⭐sybil cost in USD/month · ⭐`lab/reproduce.sh`
**L9** 🚩**#7 `guardplace`** — 🔴**THE TRADE-OFF CURVE** · ⭐three selectors in Python first · ⭐C++ port with cross-language vectors · ⭐operating point chosen from the curve
**L10** 🚩**#8 `privacypass`** — unlinkability proven by test · ⭐**D9** revocation with no deanonymisation and no retroactive linkage · ⭐**sybil cost ≥10× with admission** · ⭐`adyton-gateway` OpenAPI + quotas + RFC 9457 · ⭐**ADR-0007**
**L11** ⭐🔴**the metrics attack against my own telemetry, then defeated** · ⭐**DP budget that fails closed** · ⭐**D10 20+ incidents + the clock-skew invariant** · ⭐4 famous outages · ⭐`sim-fidelity.md`
**L12** 🚩**#9 `tor-bench`** — one-script reproducible, hop counts stated, wins attributed · 🔴🚩**#10 `1brc`** — 1B rows, the two-year delta, against a public leaderboard · ⭐**D11** >200k pps/core, **<1.5ms CPU/MB** · ⭐**the prediction committed before profiling** · ⭐aarch64 delta · ⭐`pgshift` · ⭐`docs/REPORT.md`
**L13** ⭐`shape` (reduced) — WTF-PAD padding implemented, latency cost measured · ⭐**D12** reproducible builds verified twice · ⭐**threat model published + killed/weakened/not-solved table** · ⭐install guide, 2 of 3 strangers succeed · ⭐**10 ADRs · LIMITATIONS · COMPARISON · RETROSPECTIVE** · ⭐the write-up sent to cited researchers · ⭐**the 45-minute demo, recorded**
**Cross-cutting** ⭐🔴**THE ATLAS: 166 lectures, 41 labs, eight courses — every box ticked** · ⭐**602 named problems** (+contests, CSES, AtCoder) with category counts in all eight rest weeks · ⭐🔴**AtCoder DP A–Z · CSES 200+ · CF EDU all six sections · CF rating 2000+** · ⭐🔴**40+ OA drills logged** · ⭐**24 written designs** + 24 verbal · ⭐**20+ full loops** · ⭐**14 stories on video, ≥4 from Logic Leap** · ⭐**~75 papers with one-pagers · 10 posts · 3+ merged OSS PRs, ≥1 in Arti · 1 talk** · ⭐**7 CV versions in git history** · ⭐**~250 applications logged** · ⭐**`career/LOGICLEAP.md`**

## Can you build it?
- [ ] ⚙️ A C++ network daemon whose parser cannot be crashed by hostile input, fuzzed, sanitizer-clean, with a documented subset
- [ ] Constant-size onion packets that do not leak hop position, asserted by property test
- [ ] **A working TCP** (CS144), **a working Raft** (6.5840, twice), **a working sharded fault-tolerant KV store**, **a concurrent B+Tree and an MVCC engine** (15-445), **an allocator and a concurrent proxy** (15-213), **nine xv6 kernel modifications** (6.1810)
- [ ] Per-hop QUIC removing cross-circuit head-of-line blocking, with the chart
- [ ] Compartments the kernel enforces and a five-test suite that cannot break them
- [ ] A 30-node mesh across NAT with sub-second circuit recovery under churn
- [ ] Raft-backed epoch consensus at 100% agreement, plus **detectable forks**
- [ ] Circuit-compromise probability on real BGP topology, for your system and Tor
- [ ] **A published trade-off curve for a defence you built and then attacked**
- [ ] Anonymous credentials with revocation that deanonymises nobody
- [ ] The whole thing on Kubernetes, observed without surveilling anyone, at $0/month

## Can you explain it?
- [ ] The trilemma, your corner, and exactly who you concede
- [ ] ⚙️ **Why C++ here, what Rust would have given you for free, and the apparatus that closes the gap**
- [ ] Mechanically why a Sphinx header hides its position
- [ ] Why one lost TCP segment stalls a stranger's circuit, and what you did — **derived, because you built a TCP**
- [ ] Why three of a proxy's four leaks are not the proxy's fault
- [ ] **Why divergent peer lists are a privacy bug** — with your anonymity-set numbers
- [ ] **Fork consistency, and why Raft alone does not give it to you**
- [ ] Raft's Figure 8, at a whiteboard, in five minutes
- [ ] **Why a better path-selection defence handed the attacker aim**
- [ ] How you banned an abuser without knowing who they were
- [ ] **How your own Prometheus metrics became a traffic-confirmation attack**
- [ ] **Why anyone would use Tor instead of Adyton** — and you say so in your README

## Can you diagnose it?
- [ ] Root-cause a sabotaged mesh in under 45 minutes, with evidence
- [ ] Read a flamegraph in 10 seconds and say what you would fix
- [ ] Given "p99 is 3s, CPU is 8%", name three causes and the command that distinguishes them
- [ ] Given green dashboards and wrong answers, **find the clock**
- [ ] ⚙️ Given an ASan report on a `string_view` outliving its buffer, explain the lifetime bug in one sentence

## Can you interview?
- [ ] **602 named problems**, ≥70% unaided in 25 minutes · a random Medium **narrated** in 25, on video
- [ ] 🔴 **Codeforces 2000+** · **AtCoder DP A–Z** · **CSES 200+** · **CF EDU's six assigned sections complete**
- [ ] 🔴 **40+ OA drills: two unseen problems in 90 minutes, tests written before submitting, clock budgeted across problems**
- [ ] 🔴 **Four interview rounds in one day without degrading in round three** — verified, three days running, in W96
- [ ] **24 system designs** hitting the rubric, and the reflex to say *"I built this, here is my number"*
- [ ] 14 behavioural stories ≤90s, quantified, first person, **≥4 from Logic Leap**
- [ ] **20+ full timed loops · both Gauntlets passed** · **the failure-log queue empty**

## Do they know you exist?
- [ ] 6 pinned repos, each with a diagram and a headline number in the first screen
- [ ] 10 posts published — **at least four about a result, not a tutorial**
- [ ] **3+ merged OSS PRs, at least one in Arti** · one talk given
- [ ] **40–50 people at target companies who know what you are building, from conversations that started in January 2027**
- [ ] A CV where **every bullet has a number**, and **a coursework line naming eight completed courses**

---

# 🎯 What success means on 2028-09-10

**Not an offer.** Offer timing is not under your control, and treating it as the criterion makes you optimise for the wrong things in Levels 11–13. **You will have been applying since October 2027 — eleven months of live pipeline.** If nothing has landed by W104, the pipeline is the thing to examine, not the plan.

> **The criterion: you are a candidate who cannot be screened out on credentials, and cannot be caught out in a system design round.**

If that is true and you have no offer yet, **the plan worked and the timing has not resolved.** Execute `docs/NEXT.md`.
If it is not true, **`docs/RETROSPECTIVE.md` tells you which level or which course to return to, with numbers rather than a feeling.**

---

# Closing

Five things decide whether this works.

**1. You must actually reproduce the failures.** The Walls are not flavour text. Reading "a proxy leaks" produces a fact you will forget. Watching WebRTC hand your real IP to a page you loaded through your own relay produces an instinct you will have for twenty years. **The five you will remember longest:** the naive relay reading your own plaintext back to you in Week 7 · **the heap-buffer-overflow ASan report on a one-byte-overlong length field, which is the entire language argument in one stack trace** · the onion packet getting *smaller* at each hop in Week 15, announcing its position to anyone watching · Week 52, diffing two clients' peer lists and realising a circuit through peers only three clients knew about identifies one of them · and Week 85, correlating your own Prometheus counters and discovering you had built a traffic-confirmation attack against your own users.

**2. You must finish the courses.** 🔴 **This is the difference between this plan and every twelve-month version of it, and it is the reason it costs a second year.** A course you watched half of is a topic you can name and not use. **166 lecture checkboxes and 41 lab checkboxes** — and when a course and an Adyton level collide, **the course wins and the level slips**, because Adyton will wait and CS144's handouts will not.

**3. You must use the three sources correctly.** A 25-lecture course to learn what a fencing token is wastes a week. Reaching for the AI in an area whose shape you have never seen gives you confident nonsense you cannot evaluate. **§V's table is the whole discipline: course to build the model, pages for precision, prompt for the block and the check.** And 🤖 **PROMPT 2 is the one you will skip and the one that would have found the gap.**

**4. ⚙️ You must hold the C++ line every single week.** Sanitizers, fuzzers, the documented subset. **They are not hygiene — they are the argument for having chosen C++ at all**, and a month with the sanitizer job quietly disabled turns your best interview answer into your worst.

**5. You must run all four tracks at once.** Courses without Adyton makes you a very well-educated person with nothing to show. Adyton without courses makes you someone who built one thing and cannot generalise. Either without Track I means nobody ever sees it — you fail the phone screen and never reach system design. **Running four tracks for 104 weeks is genuinely harder than running one, and it is the reason most people who "study systems for two years" never convert it into an offer.**

The gap between *"I understand distributed systems"* and *"here is a privacy relay network where per-hop QUIC removes the head-of-line blocking that makes Tor slow — and I can derive why, because I built a TCP first; here is why my clients disagreeing about the peer list was a privacy bug and how SUNDR taught me consensus alone does not fix it; here is the curve showing my own path-selection defence made me easier to target; here is the traffic-confirmation attack I built against my own metrics; here is the benchmark against Tor with my own three-hop row in it for honesty; here are eight completed courses with all forty-one labs and the code; and here is the document listing everything this does not do"* — **that gap is the entire difference between a candidate and a hire.**

This is roughly **3,044 scheduled hours across 104 weeks, of which 2,485 are committed and ~559 are the slack that lets a two-year plan survive contact with a life.** The output is not "a person who finished a roadmap." The output is an engineer who has written a TCP, a Raft, a B+Tree, an allocator and a kernel driver from specifications; built a network daemon that hostile input cannot crash and can defend the language they chose to build it in; made two browsers on one laptop unlinkable at the kernel level; computed the probability of their own system's compromise on real internet topology; attacked their own defence and published the trade; banned an abuser without learning who they were; found the surveillance system hiding inside their own dashboards — **and can explain any of it at a whiteboard from memory, including the parts that do not work.**

There are not many of those. **And exactly one posting in 569 cares what your degree says.**

**Now go download `bomb.tar`, open it in `gdb`, and start.**
