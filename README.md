# 🗺️ The God-Level Backend Engineering Roadmap
## From Junior REST APIs → FAANG-Ready Systems Engineer

> **Philosophy:** This roadmap follows a **BFS (Breadth-First) approach** — you learn topics at the same level in parallel before going deeper. Independent topics run side by side. Only when Topic B genuinely depends on Topic A does the order become strict. Every section has Theory, Technical Articles with real-world examples, hands-on Projects, and Books anchored to that topic.

---

## 📊 Learning Mix

| Type | Percentage | What It Means |
|---|---|---|
| 📖 Technical Articles / Real-World Case Studies | **50%** | How FAANG and top companies actually built this |
| 🛠️ Hands-On Projects | **30%** | Build it yourself — the only way to truly understand |
| 📚 Theory / Books | **20%** | Foundational mental models that make everything click |

---

## 🏗️ Roadmap Architecture: 7 Levels

```
Level 0 → Computer Fundamentals & Networking Internals
Level 1 → APIs, Protocols & Communication Patterns      (parallel with Level 0 Week 3+)
Level 2 → Databases Deep Cut                            (starts after Level 0)
Level 3 → Distributed Systems Core                      (needs Level 2)
Level 4 → Infrastructure, Scalability & Reliability     (parallel with Level 3)
Level 5 → Advanced Architecture Patterns                (needs Level 3 + 4)
Level 6 → System Design Mastery & Interview Patterns    (needs everything above)
```

---

## 📚 The Core Book Stack (Read in This Order)

These two books are your spine. Everything else supplements them.

### 📗 Book 1: *Designing Data-Intensive Applications* — Martin Kleppmann (DDIA)
**The single most important book a backend engineer can read.** Dense, deep, and honest. Unlike books that teach you "how to use Kafka," this book teaches you *why* Kafka works, *what guarantees it makes*, and *where it will fail you*. Every chapter is referenced throughout this roadmap.

- **When to read it:** Start Chapter 1 at Level 0. Read one chapter per week alongside the corresponding roadmap level.
- **What it covers:** Storage engines, B-trees vs LSM trees, replication, partitioning, transactions, distributed systems theory, stream processing.
- **Why it's different:** It teaches you to *reason*, not memorize. After reading this, you'll understand tradeoffs instead of Googling "which database should I use."

### 📘 Book 2: *Software Architecture: The Hard Parts* — Neal Ford & Mark Richards
**The book DDIA doesn't cover.** DDIA teaches you *how the systems work*. This teaches you *how to decide what to build*. It's full of real architectural ADRs (Architecture Decision Records), trade-off analysis, and case studies of how companies decomposed monoliths, chose service boundaries, and designed for operational reality.

- **When to read it:** Start at Level 4. Read one chapter per week.
- **What it covers:** Service granularity, data ownership in distributed systems, saga patterns, transactional outbox, contract testing, evolutionary architecture.
- **Why it's different:** It doesn't give you answers. It teaches you *how to think about the decision* — which is what staff engineers actually do.

### 🔖 Supporting Books (Read Chapters as Needed)
- **Google SRE Book** (free online) — Chapters 3, 6, 10, 14, 17 — how Google runs production at scale
- **Building Microservices** — Sam Newman — the definitive guide to service decomposition
- **The Linux Programming Interface** — Michael Kerrisk — when you need OS-level depth
- **Database Internals** — Alex Petrov — when you want to go deeper than DDIA on storage engines

---

## ⚡ Level 0: Computer Fundamentals (Weeks 1–5)

> **Goal:** Build the mental hardware model that everything else sits on. Most junior engineers skip this and remain confused about performance forever.

> **BFS Note:** The four topic clusters in this level are **independent** — do them in parallel across your weeks.

---

### 0.1 — Memory Hierarchy & How CPUs Work

**Why it matters:** When you ask "why is Redis so fast?" or "why does my database slow down under write load?", the answer is always in the memory hierarchy. Engineers who understand caches, RAM, and disk make better performance decisions every time.

#### 📖 Theory
- CPU registers → L1/L2/L3 caches → RAM → SSD → spinning disk — know the latency at every level
- Cache lines, cache misses, false sharing in multi-threaded code
- NUMA architecture and why it matters for databases running on big servers

#### 📄 Technical Articles (Real-World)
- **"What Every Programmer Should Know About Memory"** — Ulrich Drepper (lwn.net) — the classic. Read Parts 1, 2, and 3. Written by a glibc developer, grounded in how Linux actually handles memory.
- **"Latency Numbers Every Programmer Should Know"** — Jeff Dean's original numbers + modern updates at "Latency Numbers" by Colin Scott. Memorize these — interviewers literally ask about them.
- **"CPU Caches and Why You Care"** — Scott Meyers (YouTube, CppCon 2014) — best visual explanation of cache effects on data structures.
- **"How L1 and L2 CPU Caches Work"** — ExtremeTech — accessible explanation of why spatial/temporal locality matters.

#### 🛠️ Project: Cache Performance Benchmark
Write a simple benchmark in Go or Python that demonstrates:
1. Sequential array access vs random access — measure the difference
2. Row-major vs column-major matrix traversal — cache lines in action
3. False sharing: two threads writing to adjacent memory locations vs separate cache lines

**What you'll learn:** Why databases lay out data in pages. Why column-oriented databases (Parquet, ClickHouse) are faster for analytics. Why Redis uses specific data structures.

---

### 0.2 — Operating Systems: Processes, Threads, I/O

**Why it matters:** You need to understand what happens when your web server handles a request. Is it a new process? A thread? An event loop? The answer determines your concurrency model, your memory usage, and your failure modes.

#### 📖 Theory
- Process vs thread vs coroutine/goroutine — what each costs
- Context switching: what the OS actually does, why it's expensive
- Blocking I/O vs non-blocking I/O vs async I/O — three different things
- The `select`/`poll`/`epoll` progression — why epoll changed everything
- File descriptors, sockets, and what "everything is a file" actually means

#### 📄 Technical Articles (Real-World)
- **"The C10K Problem"** — Dan Kegel (kegel.com/c10k.html) — the paper that defined modern async server design. Written in 2001 but still foundational.
- **"How Node.js Works: A Look Behind the Scenes"** — Samer Buna — explains the libuv event loop, thread pool, and why Node can handle 10k connections single-threaded.
- **"Blocking I/O, Nonblocking I/O, And Epoll"** — Daan Leijen — technical walkthrough of Linux I/O mechanisms.
- **"Inside nginx: How we designed for performance and scale"** — NGINX blog — how nginx's event-driven model beats Apache's process-per-connection at scale.
- **"Fibers, Oh My!"** — Cloudflare blog — explains how Cloudflare uses coroutines in production for I/O concurrency.

#### 📚 Book Anchor
- **DDIA Chapter 1** — "Reliable, Scalable, and Maintainable Applications" — read this first as framing

#### 🛠️ Project: Build a Simple HTTP Server from Raw Sockets
No frameworks. Use raw TCP sockets to build a server that:
1. Accepts HTTP/1.1 GET requests
2. Parses headers manually
3. Returns a proper HTTP response with status codes

**Level up:** Rewrite it using non-blocking I/O with `epoll` (Linux) or `kqueue` (macOS). Benchmark both versions under 1000 concurrent connections. Observe the difference.

**What you'll learn:** What frameworks like Express, Gin, and FastAPI are actually doing. Why connection pooling matters. What "keep-alive" really means at the socket level.

---

### 0.3 — Networking Internals: TCP/IP, DNS, TLS

**Why it matters:** Every distributed system is a network of processes talking to each other. Engineers who understand TCP, DNS, and TLS debug production incidents in minutes. Engineers who don't spend hours guessing.

#### 📖 Theory
- The OSI model (practical layers: L4 TCP/UDP, L7 HTTP)
- TCP three-way handshake, connection teardown, TIME_WAIT states
- TCP congestion control: why large data transfers start slow (slow start)
- UDP: when you want speed over reliability (DNS, video streaming, gaming)
- DNS resolution chain: browser cache → OS → recursive resolver → root → TLD → authoritative
- TLS 1.3: the handshake, certificate chain, session resumption

#### 📄 Technical Articles (Real-World)
- **"High Performance Browser Networking"** (Ch. 1–4) — Ilya Grigorik (free at hpbn.co) — the best networking primer ever written. Chapter 2 on TCP is essential.
- **"Cloudflare: What is DNS?"** and **"How does HTTPS work?"** — Cloudflare's blog is a goldmine of clear technical explanations.
- **"How QUIC is Replacing TCP for HTTP/3"** — Fastly engineering blog — real-world explanation of why Google invented a new transport protocol.
- **"The Story of One Latency Spike"** — Cloudflare blog — a real production incident where TCP's TIME_WAIT states caused cascading failures. Brilliant real-world debugging.
- **"TLS 1.3: 0-RTT, resumption, and anti-replay"** — Cloudflare blog — the internals of modern TLS.

#### 🛠️ Project: Build a TCP Chat Server
Raw sockets, no frameworks:
1. Multi-client server with rooms/channels
2. Message broadcast to all clients in a room
3. Handle client disconnections gracefully (detect broken connections)

**Level up:**
- Implement a simple binary wire protocol instead of line-based text. Define a header (message type + length) + body.
- Benchmark: how many concurrent connections can your server hold?
- Add TLS using the OS/language's TLS library

**What you'll learn:** Connection management, protocol design, backpressure basics.

---

### 0.4 — Linux Command Line for Backend Engineers

**Why it matters:** You will debug production. Production runs on Linux. Engineers who can fluently use `strace`, `lsof`, `netstat`, `perf`, and `tcpdump` are 10x more effective in incidents.

#### 📄 Technical Articles (Real-World)
- **"Linux Performance Analysis in 60,000 Milliseconds"** — Netflix Tech Blog (Brendan Gregg) — the canonical list of commands to run when diagnosing a production performance problem.
- **"Linux Tracing Systems & How They Fit Together"** — Julia Evans (jvns.ca) — explains strace, ltrace, perf, eBPF in plain language.
- **"The USE Method"** — Brendan Gregg — a systematic methodology for performance analysis: Utilization, Saturation, Errors.
- **"How Containers Work"** — Julia Evans (wizard zines) — cgroups, namespaces, the actual Linux primitives behind Docker.

#### 🛠️ Project: Diagnose a Simulated Production Issue
Set up a small app (any language) with an intentional bug (memory leak, CPU spin, too many open file descriptors). Use only Linux tools to diagnose it:
- `top`/`htop` for CPU/memory
- `lsof` for file descriptors
- `strace -p <pid>` to trace syscalls
- `ss` or `netstat` for connections
- `tcpdump` to capture actual packets

**What you'll learn:** How to actually debug real production systems.

---

## ⚡ Level 1: APIs, Protocols & Communication Patterns (Weeks 3–8)

> **Goal:** Master how distributed services talk to each other — at the protocol level, not just the "which framework to use" level.

> **BFS Note:** 1.1 (REST deep) and 1.2 (gRPC/Protobuf) and 1.3 (WebSockets/SSE) are **independent** — learn them in parallel. 1.4 (API Design Patterns) synthesizes all of them.

---

### 1.1 — REST: The Deep Cut (Beyond CRUD)

Most junior engineers think they know REST because they've built CRUD APIs. Real REST is about *constraints and tradeoffs* — when it works brilliantly and when it falls apart.

#### 📖 Theory
- REST constraints: statelessness, uniform interface, hypermedia (HATEOAS)
- HTTP verbs as semantic contracts (why PUT is idempotent but POST isn't — and why that matters)
- HTTP status codes: the semantic meaning of 200 vs 202 vs 204, 400 vs 422, 429, 503
- Idempotency keys: why Stripe requires them for payment APIs
- Content negotiation: Accept / Content-Type headers and versioning strategies

#### 📄 Technical Articles (Real-World)
- **"Zalando RESTful API Guidelines"** — github.com/zalando/restful-api-guidelines — one of the most thorough, production-hardened REST API guides ever published. Read all sections.
- **"Best Practices for Designing a Pragmatic RESTful API"** — Vinay Sahni (vinaysahni.com) — the article most senior engineers cite.
- **"Stripe's API Design Principles"** — Stripe Dev Blog — how Stripe built an API used by millions of developers and almost never breaks backward compatibility.
- **"How We Versioned Our REST API at Intercom"** — Intercom Engineering — real case study of API versioning strategy.
- **"Idempotency: Making APIs Safer"** — Stripe Engineering — why Stripe introduced idempotency keys and how they're implemented.

#### 🛠️ Project: Build a Production-Quality REST API
Build a Task Management API (like a mini Jira):
- Full CRUD with proper HTTP semantics
- Pagination (cursor-based, not offset — read why below)
- Filtering and sorting with validation
- Idempotency keys on state-changing endpoints
- API versioning strategy
- Rate limiting (token bucket algorithm, in-memory)
- OpenAPI spec (Swagger) — document everything

**What you'll learn:** The difference between building an API that works vs one that's production-ready.

---

### 1.2 — gRPC, Protobuf & Binary Protocols

**Why it matters:** Inside a microservices system, services talk to each other thousands of times per second. REST over JSON is simple but expensive — large payloads, slow parsing, no schema enforcement. gRPC fixes all three and is used heavily inside Google, Netflix, and Uber.

#### 📖 Theory
- Protocol Buffers: field numbers, varint encoding, backward/forward compatibility rules
- gRPC over HTTP/2: multiplexing, header compression, streaming
- Four gRPC modes: unary, server streaming, client streaming, bidirectional streaming
- When to use gRPC vs REST: internal service communication vs public APIs
- gRPC-Gateway: serving both gRPC and HTTP/REST from the same server

#### 📄 Technical Articles (Real-World)
- **"Why We Use gRPC at Square"** — Square Engineering blog — real-world adoption story with measured latency improvements over REST.
- **"gRPC vs REST: Understanding gRPC, OpenAPI and REST and when to use them in API Design"** — Google Cloud Blog — written by the people who invented gRPC.
- **"Protobuf Encoding"** — Google developers.google.com — the official, surprisingly readable encoding spec.
- **"How Netflix Uses gRPC"** — Netflix TechBlog — how they migrated internal communication to gRPC at massive scale.
- **"Schema Evolution in Avro, Protocol Buffers and Thrift"** — Martin Kleppmann's blog — essential reading on how to evolve your schema without breaking clients.

#### 📚 Book Anchor
- **DDIA Chapter 4** — "Encoding and Evolution" — covers Protobuf, Avro, Thrift, JSON encoding tradeoffs.

#### 🛠️ Project: Build a gRPC Microservice
Implement a User Service with:
- Protobuf schema: User, CreateUserRequest, GetUserRequest, ListUsersResponse
- Unary RPC: GetUser, CreateUser
- Server streaming RPC: ListUsers (stream users back to client)
- Proper error codes (grpc/codes package)
- Interceptors for logging and auth token validation
- Client written in a *different language* to prove the interoperability

**What you'll learn:** Schema design, streaming patterns, cross-language communication.

---

### 1.3 — WebSockets, SSE & Real-Time Communication

**Why it matters:** Chat apps, live dashboards, collaborative editing, gaming — these require the server to push data to clients. Understanding when to use WebSockets vs SSE vs long polling vs gRPC streaming is a common system design question.

#### 📖 Theory
- HTTP's request-response limitation for real-time
- Long polling: a hack, but it works. What it costs in server resources.
- Server-Sent Events (SSE): HTTP/1.1 streaming, unidirectional, browser-native
- WebSockets: full-duplex, single TCP connection, the upgrade handshake
- WebSocket at scale: sticky sessions, connection state, horizontal scaling challenges

#### 📄 Technical Articles (Real-World)
- **"How Slack Works: WebSockets and the Real-Time Messaging API"** — Slack Engineering blog — how Slack manages millions of persistent WebSocket connections.
- **"Server-Sent Events vs WebSockets"** — Ably blog — clear technical comparison with real-world use cases for each.
- **"Scaling WebSocket Connections to 1 Million"** — Fanout.io — how to horizontally scale stateful WebSocket connections using pub/sub fanout.
- **"Discord: How Discord Handles Two and Half Million Concurrent Voice Users"** — Discord Engineering — deep dive into real-time audio at scale.
- **"Building a Real-Time Bidding Platform: Architecture"** — AppNexus Engineering — high-frequency real-time systems.

#### 🛠️ Project: Real-Time Collaborative Whiteboard
Build a collaborative drawing app (think Excalidraw simplified):
- WebSocket server with rooms
- Real-time broadcast of drawing operations to all room members
- Operational transforms for conflict resolution (when two people draw simultaneously)
- Reconnection with state replay (new client catches up to current state)
- Horizontal scaling: use Redis pub/sub so multiple server instances can relay messages

**What you'll learn:** Stateful connection management, the fan-out problem, horizontal scaling challenges for real-time systems.

---

### 1.4 — GraphQL: When REST Isn't Enough

**Why it matters:** GitHub, Shopify, Twitter, and Facebook all use GraphQL. Understanding it is essential — not because you'll always use it, but because knowing *why* they chose it and *what it costs* is a system design depth signal.

#### 📖 Theory
- The over-fetching and under-fetching problems with REST
- GraphQL type system: Schema Definition Language, resolvers, N+1 query problem
- DataLoader pattern: batching and caching resolver calls
- GraphQL subscriptions: real-time with WebSockets
- Federation: how large organizations split a GraphQL schema across teams

#### 📄 Technical Articles (Real-World)
- **"How Facebook Invented GraphQL"** — Lee Byron (GraphQL co-creator) at React Europe — the original motivation and design decisions.
- **"GitHub's Move to GraphQL"** — GitHub Engineering blog — why GitHub replaced their REST API v3 with GraphQL v4.
- **"Shopify's Scaling GraphQL at Production"** — Shopify Engineering — how they run GraphQL for millions of storefronts.
- **"The N+1 Problem in GraphQL"** — Apollo blog — the most common GraphQL performance trap and how DataLoader solves it.
- **"GraphQL: A Data Query Language"** — Lee Byron's original Facebook technical post — the original design doc.

#### 🛠️ Project: GraphQL API with DataLoader
Build a blog platform API with GraphQL:
- Schema: User, Post, Comment, Tag types
- Queries with nested resolvers (posts → comments → author)
- DataLoader to batch all database queries — benchmark before/after
- Mutations with input validation
- Subscription: new comment notification via WebSocket
- Depth limiting and query complexity analysis to prevent abuse

---

## ⚡ Level 2: Databases — The Deep Cut (Weeks 4–10)

> **Goal:** Transform from someone who *uses* databases to someone who *understands* them. This is the most impactful single level for FAANG interviews.

> **BFS Note:** 2.1, 2.2, and 2.3 are mostly independent — do them in parallel. 2.4 depends on understanding 2.1 internals. 2.5 depends on 2.1 + 2.2.

---

### 2.1 — Database Internals: How They Actually Store Your Data

This is the chapter of DDIA that changes everything. Once you understand B-trees and LSM trees, you'll never blindly pick a database again.

#### 📖 Theory
- **B-Trees:** pages, branching factor, in-place updates, write amplification
- **LSM Trees (Log-Structured Merge Trees):** append-only writes, SSTables, compaction, why writes are fast, read amplification
- **Write-Ahead Log (WAL):** how databases survive crashes. Every database has one.
- **MVCC (Multi-Version Concurrency Control):** how PostgreSQL allows reads without blocking writes
- Buffer pool / buffer cache: why databases manage their own memory
- Page layout: how rows are stored on disk pages in PostgreSQL

#### 📄 Technical Articles (Real-World)
- **"B-Trees and Database Indexes"** — Use The Index Luke (use-the-index-luke.com) — the best practical guide to understanding how B-tree indexes affect query performance. Read all chapters.
- **"How RocksDB Works"** — Meta Engineering Blog — RocksDB is the LSM tree engine used inside MySQL (MyRocks), CockroachDB, TiKV, and Cassandra. Meta wrote this explaining the internals.
- **"PostgreSQL's MVCC"** — official PostgreSQL docs + Cybertec blog "MVCC and Autovacuum Explained" — how Postgres handles concurrent reads and writes without locking.
- **"The Log: What every software engineer should know about real-time data's unifying abstraction"** — Jay Kreps (Medium/LinkedIn) — the famous article that explains how the append-only log underpins databases, Kafka, and distributed systems. Essential.
- **"How Does a Relational Database Work?"** — Christophe Calliau — surprisingly deep free-text walkthrough of database internals.

#### 📚 Book Anchor
- **DDIA Chapter 3** — "Storage and Retrieval" — the best chapter in the book. Read it twice.
- **Database Internals** (Alex Petrov) — Chapter 2 (B-Trees) and Chapter 5 (LSM Trees) — go here for more depth.

#### 🛠️ Project: Build a Key-Value Store (Bitcask Style)
Implement a persistent key-value store with:
1. **v1:** Append-only log file + in-memory hashmap (key → byte offset in log)
2. **v2:** Log compaction — merge old log files into a new compacted file
3. **v3:** Add a Bloom filter to skip disk reads for missing keys
4. **v4:** CRC checksums on each record — detect corruption on read

**Reference:** Read the Bitcask paper (Riak's storage engine) — it's 10 pages and explains exactly what to build.

**What you'll learn:** WAL mechanics, compaction strategies, why Bloom filters exist, crash recovery.

---

### 2.2 — PostgreSQL: Professional-Level SQL and Indexing

**Why it matters:** You use Postgres (or MySQL) every day. Most engineers use 5% of what it can do. Knowing execution plans, index types, and query optimization separates senior engineers from juniors.

#### 📖 Theory
- EXPLAIN and EXPLAIN ANALYZE: reading query plans, understanding seq scan vs index scan vs index-only scan
- Index types: B-tree, Hash, GIN (for JSONB/full-text), GiST (for geometric/range types)
- Partial indexes, expression indexes, composite index column order
- Table statistics and the query planner — why `ANALYZE` matters
- Connection pooling: why PgBouncer exists, what "connection overhead" actually costs
- Partitioning: range, list, hash — when and why to partition

#### 📄 Technical Articles (Real-World)
- **"Explaining the Postgres Query Optimizer"** — pganalyze.com — the most thorough guide to EXPLAIN output ever written.
- **"Connection Pooling with PgBouncer"** — Crunchy Data blog — why Postgres can't handle 10,000 direct connections and how PgBouncer solves it.
- **"Partial Indexes in PostgreSQL"** — Heap (now Heap Analytics) Engineering Blog — real case study of a 10x query speedup using a partial index.
- **"How Notion Sharded Their Postgres Database"** — Notion Engineering blog — a real case study of sharding Postgres at scale, including the pain points.
- **"Why Discord Moved from MongoDB to Cassandra... and then from Cassandra to ScyllaDB"** — Discord Engineering — one of the best database migration case studies ever written.

#### 🛠️ Project: Advanced PostgreSQL Workshop
Take an existing app with a Postgres database and:
1. Load 10M+ rows using a bulk data generator
2. Run slow queries. Use EXPLAIN ANALYZE to find the problem.
3. Add appropriate indexes. Compare before/after query times.
4. Implement a partial index for a common filter (e.g., `WHERE status = 'active'`)
5. Set up PgBouncer in front of Postgres. Measure connection overhead reduction.
6. Implement table partitioning (partition posts by month)

---

### 2.3 — NoSQL Databases: When and Why

**Why it matters:** Not "NoSQL vs SQL" — that's a bad debate. The real question is: what data model fits your access pattern, and what consistency guarantees do you actually need?

#### 📖 Theory
- **Document stores (MongoDB/DynamoDB):** nested data, flexible schema, when embedding vs referencing
- **Wide-column stores (Cassandra/HBase):** data model around your read patterns, partition keys, clustering columns
- **Key-value stores (Redis/DynamoDB):** single-key access, extreme speed, limited query flexibility
- **Graph databases (Neo4j):** when relationships are first-class, Cypher query language
- **Time-series databases (InfluxDB/TimescaleDB):** high-write, time-ordered data, downsampling

#### 📄 Technical Articles (Real-World)
- **"Amazon DynamoDB: How It Works"** — AWS docs + "Amazon DynamoDB — 10 Things You Should Know" — DynamoDB is the most carefully designed NoSQL database ever built. Understanding its data model teaches you how to think about NoSQL.
- **"Cassandra Data Modeling"** — DataStax Academy — the official guide. Cassandra's data model is completely different from SQL and requires a mindset shift.
- **"How Instagram Uses Cassandra"** — Instagram Engineering blog — storing billions of photos' metadata.
- **"Redis Data Structures and When to Use Them"** — Redis official blog — most engineers only use GET/SET. Redis has sorted sets, hyperloglogs, and streams.
- **"Rethinking the Database Layer for Time Series"** — InfluxDB blog — why generic SQL is a poor fit for metrics and monitoring data.

#### 📚 Book Anchor
- **DDIA Chapter 2** — "Data Models and Query Languages" — covers document, relational, graph models side by side.

#### 🛠️ Project: Build a Social Feed with Multiple Storage Backends
Implement a Twitter-like feed system using the right database for each access pattern:
- **PostgreSQL:** User accounts, follow relationships
- **Redis:** Timeline cache (sorted set by timestamp), rate limiting counters, session store
- **Cassandra (or DynamoDB local):** Notification history (partition by user_id, cluster by time)
- Benchmark: measure read latency from each backend under load

**What you'll learn:** Why one database is never enough. How to think about access patterns before picking storage.

---

### 2.4 — Transactions, ACID, and Isolation Levels

**Why it matters:** This is the source of most data bugs in production systems. Developers assume databases are "safe" without understanding what they actually guarantee — and what they don't.

#### 📖 Theory
- ACID: what each property actually means in practice (not just the definition)
- Isolation levels: Read Uncommitted → Read Committed → Repeatable Read → Serializable
- Phenomena: dirty reads, non-repeatable reads, phantom reads, write skew, lost updates
- Optimistic vs pessimistic locking — when each strategy wins
- Two-Phase Locking (2PL) vs MVCC — how different databases implement isolation
- Serializable Snapshot Isolation (SSI) — PostgreSQL's approach

#### 📄 Technical Articles (Real-World)
- **"Please stop calling databases CP or AP"** — Martin Kleppmann's blog — the most important article about why CAP theorem is misused and what it actually means.
- **"A Critique of ANSI SQL Isolation Levels"** — Berenson et al. (1995 paper) — the academic paper that defined write skew and lost updates. Short and crucial.
- **"Avoiding Double-Charging Users with Idempotency and Distributed Locks"** — Brandur Leach (Stripe) — real-world example of transaction and distributed locking patterns in a payment system.
- **"How PostgreSQL Implements Serializable Isolation"** — Dan R. K. Ports & Kevin Grittner — the paper explaining SSI. Readable and fascinating.
- **"Transactions: Myths, Surprises, and Opportunities"** — Martin Kleppmann, GOTO 2015 (YouTube) — the best talk on distributed transactions ever given.

#### 📚 Book Anchor
- **DDIA Chapter 7** — "Transactions" — read this slowly, twice. It's the most valuable 60 pages in the book.

#### 🛠️ Project: Find and Fix Real Transaction Bugs
Set up a simple bank account system in PostgreSQL. Deliberately trigger:
1. **Lost update:** Two concurrent requests both decrement the same balance — one update is lost. Fix with `SELECT FOR UPDATE`.
2. **Write skew:** Doctor on-call problem — two doctors both check "is anyone else on call?" and both sign off. Fix with serializable isolation.
3. **Phantom read:** Booking system where two users book the last seat simultaneously. Fix properly.
4. **Measure the performance cost:** How much slower is Serializable vs Read Committed? Benchmark with pgbench.

---

### 2.5 — Database Scaling: Replication, Sharding, and Connection Management

#### 📖 Theory
- Single-leader replication: replication lag, read-your-writes consistency, monotonic reads
- Multi-leader replication: conflict detection and resolution, use cases
- Leaderless replication: quorums (W + R > N), sloppy quorums, hinted handoff
- Sharding strategies: range-based, hash-based, consistent hashing
- Why you should exhaust all other options before sharding (read replicas, caching, vertical scaling)
- CQRS (Command Query Responsibility Segregation) with read replicas

#### 📄 Technical Articles (Real-World)
- **"Scaling to 100M: MySQL vs. DynamoDB"** — High Scalability blog — real benchmarks and architectural decisions at 100M users.
- **"How Notion Sharded Their Postgres Database"** — Notion Engineering — real migration story with all the painful details.
- **"Vitess: MySQL Sharding at YouTube/GitHub Scale"** — PlanetScale blog — how YouTube runs MySQL on thousands of nodes.
- **"Read Replicas at Instacart"** — Instacart Engineering — practical guide to adding read replicas and handling replication lag bugs.
- **"How We Scaled Our Database to 1.5B Rows"** — Heap Analytics Engineering — a detailed case study.

#### 📚 Book Anchor
- **DDIA Chapter 5** — "Replication" — single-leader, multi-leader, leaderless. Essential.
- **DDIA Chapter 6** — "Partitioning" — sharding strategies and the tradeoffs.

#### 🛠️ Project: Set Up and Break Postgres Replication
1. Set up PostgreSQL with one primary and two read replicas using streaming replication
2. Write a script that continuously writes to primary and reads from replica — observe replication lag
3. Deliberately cause lag: do a large bulk insert, watch `pg_stat_replication`
4. Implement an application-level "read-your-writes" guarantee: after a write, route the next read to primary
5. Simulate primary failure: promote a replica to primary

---

## ⚡ Level 3: Distributed Systems Core (Weeks 8–16)

> **Goal:** This is the hardest level and where most engineers plateau. After this level, you'll understand things that most "senior engineers" don't.

> **Prerequisite:** Complete Level 2 first. Distributed systems concepts require understanding single-machine storage deeply.

> **BFS Note:** 3.1 and 3.2 are conceptually parallel (one is theory, one is practice). 3.3 (consensus) depends on 3.1. 3.4 (Kafka) is independent. 3.5 (clocks) can be read anytime.

---

### 3.1 — The Core Problems of Distributed Systems

**Why it matters:** Distributed systems are hard because networks fail, clocks drift, and processes crash — often simultaneously. Engineers who don't internalize this build systems that fail in mysterious ways.

#### 📖 Theory
- The **Fallacies of Distributed Computing** — eight assumptions every junior engineer makes that are wrong
- **Partial failures:** a node can be running but not responding — it's neither alive nor dead
- **Unreliable networks:** packets get lost, duplicated, reordered, arbitrarily delayed
- **Unreliable clocks:** NTP is imprecise. You cannot use wall-clock time to order events across machines.
- **The Two Generals Problem:** proof that perfect communication over unreliable links is impossible
- **Byzantine faults:** what happens when nodes lie (relevant for blockchains, distributed trust)

#### 📄 Technical Articles (Real-World)
- **"Fallacies of Distributed Computing"** — Arnon Rotem-Gal-Oz (with L. Peter Deutsch) — read the original 8 fallacies and the extended explanations.
- **"Notes on Distributed Systems for Young Bloods"** — Jeff Hodges — the pragmatic version of distributed systems wisdom. Required reading.
- **"An Introduction to Distributed Systems"** — Kyle Kingsbury (aphyr) — the best technical overview of distributed systems theory written for practitioners.
- **"How AWS Builds Highly Available Systems"** — Werner Vogels (allthingsdistributed.com) — direct from Amazon's CTO on designing for failure.
- **"Chaos Engineering: Building Confidence in System Behavior Through Experiments"** — Netflix TechBlog — how Netflix deliberately breaks their production systems to find failure modes.

#### 📚 Book Anchor
- **DDIA Chapter 8** — "The Trouble with Distributed Systems" — the most honest chapter in any distributed systems book. Read it.

---

### 3.2 — MIT 6.824 Distributed Systems Course (Labs)

**Why it matters:** This course, taught at MIT, is the gold standard of distributed systems education. The labs require you to *implement* real distributed systems algorithms — not just read about them. Engineers who've done these labs have a qualitatively different understanding.

#### The Labs (Do All of Them)

**Lab 1: MapReduce**
- Implement the MapReduce framework (coordinator + workers) in Go
- Workers are fault-tolerant: coordinator re-assigns tasks from crashed workers
- **Real-world article:** "MapReduce: Simplified Data Processing on Large Clusters" — original Google paper (2004). Read before starting.

**Lab 2: Key/Value Server**
- Implement a simple key/value server using Go's RPC
- Handle at-least-once RPC semantics (duplicate detection)
- **Real-world article:** "Spanner: Google's Globally-Distributed Database" — shows what a real distributed KV store evolved into.

**Lab 3: Raft Consensus**
- Implement the Raft consensus algorithm from the paper
- 3A: Leader election. 3B: Log replication. 3C: Persistence. 3D: Log compaction.
- **Real-world article:** "In Search of an Understandable Consensus Algorithm (Raft)" — Ongaro & Ousterhout. Read this carefully before implementing.

**Lab 4: Fault-Tolerant Key/Value Service**
- Build a replicated key/value service on top of your Raft implementation
- Handle network partitions, leader failures, state machine divergence
- **Real-world article:** "Etcd: The Kubernetes distributed key-value store" — shows how Raft is used in production Kubernetes.

**Lab 5: Sharded Key/Value Service**
- Shard your KV service across multiple Raft groups
- Implement reconfiguration: move shards between groups as load changes
- **Real-world article:** "Dynamo: Amazon's Highly Available Key-Value Store" — the classic paper.

#### 🛠️ Project: Complete MIT 6.824 Labs 1–5
> This is the most valuable project on this entire roadmap. Budget 2–3 weeks. Labs 3 and 4 are brutal but transformative.

**Tips:**
- Use Go (the labs are in Go, and Go is perfect for distributed systems)
- Read the Raft paper 3 times before starting Lab 3
- Draw state machine diagrams before writing code
- The test suite is vicious — your code must be correct, not just "usually works"

---

### 3.3 — Consensus, Replication, and Consistency

#### 📖 Theory
- **Consensus problem:** why getting N machines to agree on a single value is hard
- **Paxos:** the original consensus algorithm — why it's hard to implement correctly
- **Raft:** Paxos made understandable — leader election, log replication, safety invariants
- **Consistency models spectrum:** linearizability → sequential consistency → eventual consistency
- **Linearizability:** the gold standard. What it means for reads to "see the latest write."
- **Eventual consistency:** what "eventually" actually means, and what bugs it causes
- **Vector clocks and Lamport timestamps:** how to order events without reliable clocks

#### 📄 Technical Articles (Real-World)
- **"Paxos Made Simple"** — Leslie Lamport (2001) — the author of Paxos explaining it clearly. Short paper.
- **"Raft: In Search of an Understandable Consensus Algorithm"** — Ongaro & Ousterhout — the Raft paper. Essential.
- **"Strong consistency models"** — Kyle Kingsbury (aphyr) — the clearest explanation of linearizability, sequential consistency, and eventual consistency with real examples.
- **"How CockroachDB Does Distributed Transactions"** — CockroachDB blog — a real implementation of distributed ACID transactions using Raft.
- **"Eventual Consistency is Not What You Think"** — Martin Kleppmann's blog — what "eventual" really means and why it's harder than it sounds.

#### 📚 Book Anchor
- **DDIA Chapter 9** — "Consistency and Consensus" — covers linearizability, total order broadcast, Raft, Paxos. Read after Chapter 8.

---

### 3.4 — Apache Kafka and Event-Driven Architecture

**Why it matters:** Kafka is the central nervous system of modern distributed systems. LinkedIn, Uber, Netflix, Airbnb — all use Kafka at the core of their data infrastructure. Understanding it deeply sets you apart.

#### 📖 Theory
- **The Log** as the fundamental abstraction: why append-only logs are the foundation of databases, replication, and streaming
- Kafka architecture: topics, partitions, offsets, consumer groups, brokers, ZooKeeper/KRaft
- **Consumer groups:** how Kafka enables parallel consumption without message duplication
- **Delivery semantics:** at-most-once, at-least-once, exactly-once — how each is achieved
- **Log compaction:** how Kafka keeps only the latest value per key
- **Kafka Streams:** stream processing as a first-class Kafka citizen
- **Change Data Capture (CDC):** using Kafka to capture every database mutation

#### 📄 Technical Articles (Real-World)
- **"The Log: What every software engineer should know about real-time data"** — Jay Kreps (LinkedIn) — the most important article about Kafka ever written. Long but essential.
- **"Exactly-Once Semantics in Apache Kafka"** — Confluent Engineering blog — how they implemented the hardest guarantee in distributed messaging.
- **"Kafka at Scale: How LinkedIn Uses Kafka"** — LinkedIn Engineering — Kafka was invented at LinkedIn. This is the original production story.
- **"How Uber Uses Apache Kafka for Real-Time Passenger and Driver Matching"** — Uber Engineering — Kafka at the center of Uber's dispatch system.
- **"Building Real-time Data Pipelines with Kafka CDC"** — Debezium blog — how Change Data Capture enables event-driven microservices.

#### 📚 Book Anchor
- **DDIA Chapter 11** — "Stream Processing" — covers Kafka, stream processing patterns, and how they relate to databases.

#### 🛠️ Project: Build an Event-Driven Order Processing System
Design an order system with Kafka as the backbone:
1. **OrderService** → publishes `order.created` event to Kafka
2. **InventoryService** → consumes `order.created`, reserves stock, publishes `inventory.reserved`
3. **PaymentService** → consumes `inventory.reserved`, charges card, publishes `payment.processed`
4. **NotificationService** → consumes all events, sends email/SMS
5. **Dead Letter Queue:** handle failed messages — route to DLQ after 3 retries
6. **Exactly-once semantics:** ensure orders are never processed twice even if consumers crash

**What you'll learn:** Event-driven architecture, saga pattern, compensating transactions, idempotent consumers.

---

### 3.5 — Distributed Clocks and Time

**Why it matters:** Every bug in a distributed system is ultimately about *ordering*. Two events happened — which one came first? Without understanding distributed clocks, you can't reason about this.

#### 📖 Theory
- **Why wall clocks fail:** NTP adjustments, clock skew, leap seconds
- **Lamport timestamps:** logical clocks that track causality
- **Vector clocks:** track causal relationships between N nodes
- **Google's TrueTime:** atomic clocks + GPS in every datacenter, uncertainty bounds
- **Hybrid Logical Clocks (HLC):** the practical approach used by CockroachDB

#### 📄 Technical Articles (Real-World)
- **"Time, Clocks, and the Ordering of Events in a Distributed System"** — Leslie Lamport (1978) — the original paper. Short, beautiful, foundational.
- **"Spanner, TrueTime and the CAP Theorem"** — Google Cloud blog — how Google uses atomic clocks to build globally consistent transactions.
- **"Logical Clocks: Lamport and Vector Clocks"** — Distributed Systems course notes from Cam/MIT — visual explanation.
- **"How CockroachDB Uses Hybrid-Logical Clocks"** — CockroachDB Engineering — production use of HLC.

---

## ⚡ Level 4: Infrastructure, Scalability & Reliability (Weeks 10–18)

> **BFS Note:** This entire level is **parallel with Level 3**. These topics don't require knowing consensus or Raft. Run them side by side.

---

### 4.1 — Load Balancing & Proxies

#### 📖 Theory
- L4 vs L7 load balancing: TCP-level vs HTTP-level — when each matters
- Algorithms: round-robin, least connections, IP hash, consistent hashing
- Health checks: active vs passive, how load balancers detect dead upstreams
- Connection draining: why you need it for zero-downtime deploys
- Reverse proxies vs API gateways: nginx vs HAProxy vs AWS ALB vs Envoy

#### 📄 Technical Articles (Real-World)
- **"The Load Balancing Problem"** — Haproxy.com blog — how HAProxy handles millions of connections.
- **"Netflix's Load Balancer: Ribbon"** — Netflix TechBlog — client-side load balancing for microservices.
- **"How AWS Elastic Load Balancing Distributes Traffic"** — AWS Architecture blog — L4 vs L7 in practice.
- **"Inside NGINX: How We Designed for Performance & Scale"** — NGINX blog — event-driven architecture of the world's most popular proxy.

#### 🛠️ Project: Multi-Node Load Balanced Service
1. Deploy 3 instances of a simple HTTP service
2. Put Nginx in front with weighted round-robin
3. Implement a `/health` endpoint — intentionally kill one instance and watch Nginx stop routing to it
4. Test connection draining: deploy a new version to one node while it's serving traffic

---

### 4.2 — Caching: Every Layer

**Why it matters:** Caching is probably the most impactful performance optimization in backend systems. But it's also the source of some of the hardest bugs. Understanding every caching layer — from CPU cache to CDN — is essential.

#### 📖 Theory
- **Caching strategies:** cache-aside, read-through, write-through, write-behind (write-back)
- **Eviction policies:** LRU, LFU, FIFO, TTL — when each is correct
- **Cache invalidation:** the hardest problem. Tag-based invalidation, event-driven invalidation.
- **Cache stampede / thundering herd:** when a cache misses and 10,000 requests hit the database simultaneously. Solutions: probabilistic early expiration, request coalescing, distributed locking.
- **Distributed caching:** Redis Cluster, Memcached — sharding, replication, consistency
- **CDN caching:** edge caches, cache-control headers, purging
- **Write-heavy vs read-heavy:** different strategies for different workloads

#### 📄 Technical Articles (Real-World)
- **"TAO: Facebook's Distributed Data Store for the Social Graph"** — Facebook/USENIX 2013 — the best caching paper ever written. How Facebook caches the social graph at trillion-edge scale.
- **"Scaling Memcache at Facebook"** — Facebook/USENIX 2013 — how Facebook runs the world's largest Memcached deployment.
- **"How Cloudflare Runs Its Global CDN"** — Cloudflare Blog — edge caching internals.
- **"Cache Stampede"** — Wikipedia + "Handling the Cache Stampede with Probabilistic Early Expiration" — the research paper.
- **"Redis Cluster Specification"** — Redis official docs — how Redis distributes and replicates data across nodes.

#### 📚 Book Anchor
- **DDIA Chapter 10** — brief discussion of materialized views and derived data — read for context.

#### 🛠️ Project: Multi-Layer Caching System
Build an image metadata service with multiple cache layers:
1. **In-process cache (L1):** LRU cache in application memory (Go's sync.Map or a library)
2. **Redis cache (L2):** Cache database results with TTL
3. **Cache invalidation:** When an image is updated, invalidate all cache layers atomically
4. **Thundering herd protection:** Use Redis SETNX to let only one request populate the cache on miss
5. **Metrics:** Track hit rate, miss rate, eviction rate per layer
6. Load test with k6 or wrk: compare latency p50/p99 with and without caching

---

### 4.3 — Rate Limiting and Throttling

#### 📖 Theory
- Why rate limiting: protect backend from abuse, enforce fair usage, prevent cascading failures
- Algorithms: token bucket, leaky bucket, fixed window, sliding window log, sliding window counter
- Where to rate limit: API gateway, application layer, database layer
- Distributed rate limiting: using Redis for shared counters across multiple servers
- Rate limiting by: IP, user, API key, tenant — different scopes have different tradeoffs

#### 📄 Technical Articles (Real-World)
- **"Scaling Your API with Rate Limiters"** — Stripe Engineering blog — how Stripe built four different rate limiters and when they use each.
- **"An Alternative Approach to Rate Limiting"** — Figma Engineering — Figma's sliding window rate limiter implementation with Redis.
- **"How Cloudflare Built Rate Limiting Capable of Scaling to Millions of Domains"** — Cloudflare blog — distributed rate limiting with approximate counting.
- **"Envoy's Rate Limiting Service"** — Envoy Proxy docs + case study from Lyft — rate limiting at the service mesh level.

#### 🛠️ Project: Implement All Rate Limiting Algorithms
Build a rate limiting library with:
1. Fixed window counter (simplest — also easiest to abuse at window boundaries)
2. Sliding window log (exact but memory-intensive)
3. Sliding window counter (approximate but efficient — what most companies use)
4. Token bucket (burst-friendly — what Stripe uses)
5. Distributed version of token bucket using Redis atomic Lua scripts
6. Benchmark all five: throughput, memory, accuracy under concurrent load

---

### 4.4 — Service Reliability: SLOs, Retries, Circuit Breakers

#### 📖 Theory
- **SLIs / SLOs / SLAs:** the difference, how Google defines them, how to set error budgets
- **Retry strategies:** naive retry (causes thundering herd), exponential backoff with jitter
- **Circuit breakers:** open/half-open/closed states, when to use vs when not to
- **Timeouts:** the most important reliability tool. Every network call needs a timeout.
- **Bulkhead pattern:** isolating failures so one slow dependency doesn't sink everything
- **Graceful degradation:** returning stale/partial data instead of errors

#### 📄 Technical Articles (Real-World)
- **"Exponential Backoff and Jitter"** — AWS Architecture Blog — why naive backoff makes thundering herd worse and how to fix it with jitter.
- **"Circuit Breaker Pattern"** — Martin Fowler — the canonical definition and implementation guide.
- **"Hystrix: Latency and Fault Tolerance for Distributed Systems"** — Netflix TechBlog — how Netflix built their circuit breaker library that influenced the entire industry.
- **"Site Reliability Engineering"** — Google SRE Book (free) — Chapters 3 (Embracing Risk), 4 (SLOs), and 13 (Emergency Response).
- **"Chaos Engineering at Netflix"** — Chaos Monkey, Chaos Kong, and the full Simian Army. How Netflix deliberately breaks production.

#### 🛠️ Project: Resilient HTTP Client with All Reliability Patterns
Build a production-quality HTTP client library:
1. Timeout on every request (connection timeout + read timeout separately)
2. Retry with exponential backoff + full jitter
3. Circuit breaker (use Hystrix state machine as reference)
4. Bulkhead: separate goroutine pools for different dependencies
5. Test by running a dependency server that randomly returns 500s and times out — verify your client handles each gracefully

---

### 4.5 — Observability: Metrics, Logs, Traces

**Why it matters:** Systems that you can't observe are systems you can't operate. Senior engineers build observable systems from the start, not as an afterthought.

#### 📖 Theory
- **The three pillars:** Metrics (numbers over time), Logs (events), Traces (request journeys)
- **Metrics:** counters, gauges, histograms, summaries. Why p99 latency matters more than average.
- **Structured logging:** JSON logs vs unstructured text. Correlation IDs.
- **Distributed tracing:** spans, trace context propagation, sampling strategies
- **RED Method:** Request rate, Error rate, Duration — the three signals for every service
- **USE Method:** Utilization, Saturation, Errors — for resources (CPU, disk, network)
- **OpenTelemetry:** the standard for all three pillars

#### 📄 Technical Articles (Real-World)
- **"Observability vs Monitoring: What's the Difference?"** — Charity Majors (Honeycomb) — the most influential article defining modern observability. She coined the term as we use it today.
- **"Distributed Tracing at Uber Scale"** — Uber Engineering blog — how Jaeger (Uber's open-source tracer) was built.
- **"Practical Guide to Distributed System Observability"** — Cindy Sridharan — the book version of this thinking (free online).
- **"Google SRE Book: Chapter 6 — Monitoring Distributed Systems"** — the chapter that defined SLIs, SLOs, and alerting philosophy for the industry.
- **"How Netflix Monitors its Cloud"** — Netflix TechBlog — Atlas metrics system, real-time anomaly detection.

#### 🛠️ Project: Full Observability Stack for Your Applications
Take any project you've built and add:
1. **Metrics:** Prometheus counters/histograms for request count, latency, error rate. Grafana dashboard.
2. **Structured logs:** JSON with correlation ID, request ID, user ID, latency on every request
3. **Distributed traces:** OpenTelemetry SDK, export to Jaeger. Trace a request through 3 services.
4. **Alerting:** Prometheus AlertManager rule — alert when p99 latency > 500ms for 5 minutes
5. **Dashboard:** Grafana dashboard showing RED signals for each service

---

## ⚡ Level 5: Advanced Architecture Patterns (Weeks 15–22)

> **Prerequisite:** Level 3 and Level 4 must be solid before this. These patterns only make sense once you understand the underlying distributed systems problems they solve.

---

### 5.1 — Microservices: The Real Architecture, Not the Hype

Most "microservices" content is about the happy path. This section is about the hard parts: service boundaries, data ownership, and distributed transactions.

#### 📖 Theory
- **Service decomposition:** bounded contexts (DDD), business capabilities vs technical layers
- **Data ownership:** each service owns its data — why this is hard and non-negotiable
- **Synchronous vs asynchronous inter-service communication:** tradeoffs in real systems
- **Distributed transactions:** why two-phase commit is a trap, why sagas exist
- **Service mesh:** Envoy/Istio — traffic management, mTLS, circuit breaking at the infrastructure level
- **API gateway vs BFF (Backend for Frontend):** when each pattern applies

#### 📄 Technical Articles (Real-World)
- **"Pattern: Microservice Architecture"** — Martin Fowler & James Lewis — the original article that popularized microservices. Read the whole thing.
- **"Microservices: A Definition of This New Architectural Term"** — Martin Fowler — what makes a microservice a microservice.
- **"The Majestic Monolith"** — DHH (Basecamp) — the counterargument. Why microservices aren't always the answer.
- **"How Netflix Migrated to Microservices"** — Netflix TechBlog (multiple posts) — the real story, including the failures.
- **"Service Mesh at Lyft with Envoy"** — Lyft Engineering — why Lyft built Envoy and what problems it solved.

#### 📚 Book Anchor
- **Building Microservices** (Sam Newman) — Ch. 3 (How to Model Services), Ch. 4 (Integration), Ch. 9 (Testing)
- **Software Architecture: The Hard Parts** (Ford & Richards) — Ch. 4–7 on decomposition and data ownership

#### 🛠️ Project: Decompose a Monolith into Microservices
Take the Task Management API from Level 1.1 and decompose it:
1. Identify service boundaries: UserService, TaskService, NotificationService, AuthService
2. Each service has its own database (no shared schema)
3. Inter-service communication: gRPC for sync calls, Kafka for async events
4. Implement the Saga pattern for "create task + notify assignee": if notification fails, compensate
5. API Gateway (use Nginx or Kong) routes external requests to appropriate services
6. Add service discovery (use Consul or Kubernetes DNS)

---

### 5.2 — Event Sourcing and CQRS

**Why it matters:** Traditional CRUD destroys history. Event sourcing stores *every state change* as an immutable event. CQRS separates reads and writes for independent scaling. These patterns are used in financial systems, audit-heavy systems, and anywhere temporal queries matter.

#### 📖 Theory
- **Event sourcing:** events as the source of truth, projections/read models, event replay
- **CQRS:** command model (writes) vs query model (reads) — separate optimized data stores
- **Event store:** append-only log of domain events
- **Eventual consistency in CQRS:** read model may lag behind write model
- **Snapshotting:** periodically snapshot state to avoid replaying 10M events

#### 📄 Technical Articles (Real-World)
- **"Event Sourcing"** — Martin Fowler — the canonical definition.
- **"CQRS Documents"** — Greg Young — the person who coined CQRS explaining the full pattern.
- **"Event Sourcing at Airbnb"** — Airbnb Engineering — how Airbnb tracks availability state using event sourcing.
- **"Building a Secure Money Transfer Service"** — Monzo Engineering — how Monzo uses event sourcing for their core banking ledger.
- **"Why Event Sourcing?"** — EventStore blog — practical examples of when CQRS/ES is the right tool.

#### 🛠️ Project: Bank Ledger with Event Sourcing
Build a simple bank account ledger:
1. **Write side:** Only accepts commands (DepositMoney, WithdrawMoney, TransferMoney). Validates and appends domain events to event store (Kafka or PostgreSQL append-only table).
2. **Read side:** Separate service consumes events and maintains read-optimized projection (current balance, transaction history)
3. **Replay:** Prove you can rebuild the read model from scratch by replaying all events
4. **Snapshotting:** After N events, save a snapshot of account state so replay starts from snapshot

---

### 5.3 — API Design at Scale: Versioning, Backward Compatibility, and Breaking Changes

#### 📖 Theory
- API versioning strategies: URL versioning, header versioning, content negotiation
- **Backward compatibility rules:** what changes are breaking vs non-breaking
- **Tolerant reader pattern:** consumers should ignore unknown fields
- **API deprecation:** how to sunset APIs without breaking clients
- **OpenAPI / AsyncAPI:** machine-readable API contracts and their tooling
- **Contract testing:** Pact — consumer-driven contract tests

#### 📄 Technical Articles (Real-World)
- **"How Stripe Maintains API Backward Compatibility"** — Stripe Engineering — Stripe has maintained backward compatibility across their API for over 10 years. Read how.
- **"API Versioning Has No 'Right Way'"** — Troy Hunt — a clear-headed analysis of every versioning strategy.
- **"Evolving APIs at Spotify"** — Spotify Engineering — how Spotify manages API evolution across 50+ internal teams.
- **"Facebook's Graph API Version Policy"** — Facebook developer docs — how Facebook manages a versioned API used by millions of apps.

---

### 5.4 — Distributed Tracing and Service Mesh

#### 📖 Theory
- Why distributed tracing: a request touches 10 microservices — how do you see the full journey?
- **Trace context propagation:** W3C Trace Context standard, B3 headers
- **Sampling:** tail-based vs head-based sampling, adaptive sampling
- **Service mesh:** sidecar proxy pattern, Envoy, Istio, Linkerd
- **mTLS:** mutual TLS between services — encryption + authentication in one

#### 📄 Technical Articles (Real-World)
- **"Distributed Tracing at Uber with Jaeger"** — Uber Engineering — why they built their own tracer and open-sourced it.
- **"OpenTelemetry: The New Standard for Observability"** — CNCF blog — how OpenTelemetry unifies metrics, logs, and traces.
- **"The Service Mesh: What Every Software Engineer Needs to Know"** — William Morgan (Linkerd creator) — the definitive explanation of service mesh.
- **"How Lyft Uses Envoy as a Service Mesh"** — Lyft Engineering — real production service mesh architecture.

#### 🛠️ Project: Full Service Mesh with Observability
Take the microservices project from 5.1 and add:
1. Deploy with Kubernetes (use minikube locally)
2. Install Istio service mesh
3. Configure automatic mTLS between all services
4. Configure traffic splitting: send 10% of traffic to a new version of TaskService
5. Full distributed tracing with Jaeger — trace a request across all services
6. Visualize the service dependency graph in Kiali

---

### 5.5 — Security Architecture for Backend Systems

#### 📖 Theory
- **Authentication vs Authorization:** the difference, and why confusing them causes bugs
- **JWT:** structure, signing algorithms, expiry, refresh tokens — and why JWTs can't be easily revoked
- **OAuth 2.0 / OpenID Connect:** the flows, when to use which grant type
- **API Security:** input validation, SQL injection, SSRF, rate limiting, API keys vs OAuth
- **Zero trust:** why "network perimeter" security fails in microservices
- **Secrets management:** Vault, AWS Secrets Manager — why you should never put secrets in environment variables

#### 📄 Technical Articles (Real-World)
- **"JSON Web Token Best Current Practices"** — IETF RFC 8725 — the official guidance on using JWTs safely.
- **"OAuth 2.0 Security Best Current Practice"** — Aaron Parecki — practical OAuth 2.0 security guide.
- **"How Uber Manages Identity and Access"** — Uber Engineering — large-scale IAM architecture.
- **"Stop Using JWT for Sessions"** — joepie91.codes — the counterargument on JWT misuse.
- **"HashiCorp Vault Architecture"** — HashiCorp blog — how Vault manages secrets at scale.

#### 🛠️ Project: Production-Ready Auth Service
Build a standalone AuthService:
1. Registration with email/password (bcrypt, proper salt rounds)
2. Login → JWT access token (15min) + refresh token (30 days) stored in httpOnly cookie
3. Refresh token rotation (each use issues a new refresh token)
4. Revocation: store refresh token hash in Redis — can invalidate any session
5. OAuth 2.0 "Login with Google" flow
6. Rate limiting on auth endpoints (prevent brute force)
7. Secrets stored in Vault (or AWS Secrets Manager mock)

---

## ⚡ Level 6: System Design Mastery (Weeks 18–26)

> **Goal:** Apply every concept from Levels 0–5 to design complete systems. This is where FAANG interviews happen.

---

### 6.1 — The System Design Interview Framework

Before designing anything, internalize this framework. It's how FAANG interviewers evaluate you.

#### The 45-Minute Structure
1. **Clarify requirements (5 min):** Functional (what does it do?) + Non-functional (scale, latency, consistency)
2. **Back-of-envelope estimation (5 min):** QPS, storage, bandwidth. Show you can reason about numbers.
3. **High-level design (10 min):** Core components, data flow, API contract
4. **Data model (5 min):** Schema, which database, why
5. **Deep dive (15 min):** The interviewer picks 1-2 components. Go deep on tradeoffs.
6. **Wrap up (5 min):** Bottlenecks, monitoring, potential improvements

#### 📄 Technical Articles
- **"Hacking the System Design Interview"** — Evan King (ex-Google) — the most practical guide to the interview format.
- **"How to Crack the System Design Interview"** — Tushar Roy — framework explanation with examples.
- **System Design Interview Vol. 1 & 2** — Alex Xu — use as a reference catalog for design patterns, not as a primary learning source.

#### What Interviewers Actually Listen For
- **Do you ask good questions?** (Requirements clarification shows maturity)
- **Do you mention what you're optimizing for?** (Read-heavy? Write-heavy? Latency? Consistency?)
- **Do you justify tradeoffs?** ("I chose Cassandra because X, but it means Y")
- **Do you know failure modes?** ("This works unless the message queue goes down, in which case...")
- **Do you go deep when asked?** Can you explain B-trees, consistent hashing, replication lag on demand?

---

### 6.2 — Canonical Design Problems (Build and Document Each)

For each problem: design it on paper first, then build a simplified version, then write a design document explaining your decisions.

---

#### Design 1: URL Shortener (Bitly)
**Concepts:** Hashing, database choice, caching, redirects, analytics
- 100M URLs stored, 1B reads/day (read-heavy)
- Short URL generation: base62 encoding of auto-increment ID vs hash approaches
- Cache layer: Redis sorted set with LRU eviction for hot URLs
- Analytics: click counting with approximation (HyperLogLog for unique visitors)
- **Real-world article:** "How Bitly Uses Redis" — Redis blog. How they cache 6B+ redirects/day.

#### Design 2: Distributed Message Queue (Kafka-like)
**Concepts:** Log structure, partitioning, consumer groups, offset management
- Append-only log per partition, consumer tracks its own offset
- Leader/follower replication per partition
- **Real-world article:** "Kafka Internals" — Confluent Engineering blog.

#### Design 3: Rate Limiter (API Gateway Level)
**Concepts:** Distributed counters, sliding window, Redis atomic operations
- Sliding window counter with Redis + Lua scripts for atomicity
- Handle 100k API keys, each with different rate limits
- **Real-world article:** Stripe's rate limiter blog post (already referenced in 4.3).

#### Design 4: Twitter/X Feed (News Feed Generation)
**Concepts:** Fan-out on write vs fan-out on read, celebrity problem, denormalization
- Fan-out on write: precompute timelines on post creation
- Fan-out on read for celebrity accounts (>10k followers)
- Hybrid approach with threshold
- **Real-world article:** "Storing Data at Twitter Scale" — Twitter Engineering.

#### Design 5: Distributed Cache (Redis-like)
**Concepts:** Consistent hashing, cache eviction, replication, cluster topology
- Consistent hashing with virtual nodes for even distribution
- LRU eviction per node
- Primary-replica replication with async replication lag tradeoff
- **Real-world article:** "Scaling Memcache at Facebook" — USENIX 2013.

#### Design 6: Web Crawler
**Concepts:** Distributed coordination, URL deduplication, politeness, crawl scheduling
- URL frontier with priority queue
- Distributed deduplication using Bloom filter
- Politeness: respect robots.txt, rate limit per domain
- **Real-world article:** "Mercator: A Scalable, Extensible Web Crawler" — AltaVista paper.

#### Design 7: Notification System (WhatsApp/Push)
**Concepts:** Fan-out, delivery guarantees, multi-channel, priority queues
- Event ingestion → Kafka → per-channel workers → provider APIs
- Delivery receipts and retry with exponential backoff
- **Real-world article:** "Airbnb's Notification Platform" — Airbnb Engineering.

#### Design 8: Distributed File Storage (S3-like)
**Concepts:** Object storage, consistency, erasure coding, metadata vs data separation
- Metadata service (SQL) + object storage (blob nodes)
- Multi-part upload for large files
- Erasure coding vs replication
- **Real-world article:** "Facebook's Haystack: Finding a Needle in Haystack" — USENIX 2010.

#### Design 9: Search Autocomplete
**Concepts:** Trie data structure, distributed trie, aggregation, real-time updates
- Distributed trie with top-K tracking per node
- Aggregation service: count search queries, update trie periodically
- **Real-world article:** "Building Autocomplete at Scale" — Algolia blog.

#### Design 10: Ride-Sharing Location Service (Uber Dispatch)
**Concepts:** Geospatial indexing, real-time updates, low-latency matching
- Geohash or H3 (Uber's hexagonal grid) for location bucketing
- Redis for real-time driver location storage (TTL-based, auto-expires stale drivers)
- Dispatch: find nearest N drivers → rank → assign
- **Real-world article:** "Uber's Fulfillment Platform: Engineering the Mission-Critical Logistics" — Uber Engineering.

#### Design 11: Video Upload and Streaming (YouTube)
**Concepts:** Object storage, transcoding pipeline, CDN, adaptive bitrate streaming
- Upload → S3 → message queue → transcoding workers → multiple resolutions
- Adaptive bitrate streaming (HLS, DASH)
- CDN for global delivery, personalized caching
- **Real-world article:** "YouTube's Video Infrastructure" — multiple YouTube Engineering blog posts.

#### Design 12: Distributed Transaction (Cross-Service Payment)
**Concepts:** 2PC vs Saga, transactional outbox, idempotency
- Saga with choreography (event-driven) vs orchestration (central coordinator)
- Transactional outbox pattern: atomic write to DB + event emission
- Idempotent consumers: ensure same event can be processed multiple times safely
- **Real-world article:** "Distributed Transactions at Shopify" — Shopify Engineering.

---

### 6.3 — Reading the Engineering Papers That Built the Industry

These are the primary sources. Read the originals, not summaries.

| Paper | What It Built | Year |
|---|---|---|
| MapReduce: Simplified Data Processing on Large Clusters | Hadoop, Spark | 2004 |
| The Google File System | HDFS, distributed file systems | 2003 |
| Bigtable: A Distributed Storage System for Structured Data | Cassandra, HBase | 2006 |
| Dynamo: Amazon's Highly Available Key-Value Store | DynamoDB, Cassandra, Riak | 2007 |
| Raft: In Search of an Understandable Consensus Algorithm | etcd, CockroachDB, TiKV | 2014 |
| Spanner: Google's Globally-Distributed Database | CockroachDB, Google Cloud Spanner | 2012 |
| Kafka: A Distributed Messaging System for Log Processing | Apache Kafka | 2011 |
| TAO: Facebook's Distributed Data Store for the Social Graph | Facebook social graph | 2013 |
| Chubby Lock Service for Loosely Coupled Distributed Systems | ZooKeeper, etcd | 2006 |
| Chord: A Scalable Peer-to-peer Lookup Service | Consistent hashing | 2001 |

---

### 6.4 — The Must-Follow Engineering Blogs

Subscribe to all of these. Read 1–2 posts per week alongside your roadmap.

**Company Blogs (Primary Source)**
- Netflix TechBlog — chaos engineering, distributed systems, ML
- Uber Engineering — geospatial, dispatch, real-time systems
- Discord Engineering — scaling challenges, migration case studies
- Cloudflare Blog — networking, security, distributed systems explained clearly
- Stripe Engineering — payments, API design, reliability
- Figma Engineering — real-time collaboration, performance
- Meta Engineering — social graph, distributed storage
- Airbnb Engineering — search, pricing, infrastructure
- Dropbox Tech Blog — storage, file sync, infrastructure
- LinkedIn Engineering — Kafka (they built it), data infrastructure
- GitHub Engineering — git infrastructure, scaling developer tools
- DoorDash Engineering — logistics, real-time systems
- Shopify Engineering — ecommerce, distributed transactions

**Individual Engineers (Essential Reading)**
- Martin Kleppmann (martin.kleppmann.com) — distributed systems, CRDTs
- Martin Fowler (martinfowler.com) — architecture patterns, microservices
- Brendan Gregg (brendangregg.com) — Linux performance, eBPF
- Julia Evans (jvns.ca) — Linux internals, networking, explained simply
- Dan Luu (danluu.com) — systems, performance, computer architecture
- Werner Vogels (allthingsdistributed.com) — distributed systems, AWS architecture
- Charity Majors (charity.wtf) — observability, SRE, databases
- Kyle Kingsbury / Aphyr (aphyr.com) — distributed systems correctness, Jepsen

---

## ⚡ The Parallel Reading Plan (How to Use DDIA Week by Week)

Map DDIA chapters to your roadmap levels:

| Week | DDIA Chapter | Roadmap Level |
|---|---|---|
| 1–2 | Ch. 1 — Reliable, Scalable, Maintainable | Level 0 framing |
| 3–4 | Ch. 2 — Data Models | Level 2.3 NoSQL |
| 5–6 | Ch. 3 — Storage Engines | Level 2.1 Internals |
| 7–8 | Ch. 4 — Encoding | Level 1.2 gRPC/Protobuf |
| 9–10 | Ch. 5 — Replication | Level 2.5 Scaling |
| 11–12 | Ch. 6 — Partitioning | Level 2.5 Sharding |
| 13–14 | Ch. 7 — Transactions | Level 2.4 ACID |
| 15–16 | Ch. 8 — Distributed Systems Trouble | Level 3.1 |
| 17–18 | Ch. 9 — Consistency & Consensus | Level 3.3 |
| 19–20 | Ch. 10 — Batch Processing | Design 2 + 6 |
| 21–22 | Ch. 11 — Stream Processing | Level 3.4 Kafka |
| 23–24 | Ch. 12 — Future of Data Systems | Level 5.2 Event Sourcing |

After DDIA, start **Software Architecture: The Hard Parts**:

| Week | Hard Parts Chapter | Roadmap Level |
|---|---|---|
| 25–26 | Ch. 1–3 — Decomposition | Level 5.1 Microservices |
| 27–28 | Ch. 4–6 — Data Ownership | Level 5.1 + 5.2 |
| 29–30 | Ch. 7–9 — Distributed Transactions | Level 5.2 + Design 12 |
| 31–32 | Ch. 10–12 — Saga Patterns | Design 12 |

---

## 📅 Master Timeline

| Duration | Level | Focus |
|---|---|---|
| Weeks 1–5 | Level 0 | Computer fundamentals, networking, OS |
| Weeks 3–8 | Level 1 | APIs, protocols, WebSockets (parallel with Level 0 from week 3) |
| Weeks 4–10 | Level 2 | Databases deep cut (parallel with Level 1) |
| Weeks 8–16 | Level 3 | Distributed systems (starts after Level 2 solid) |
| Weeks 10–18 | Level 4 | Infrastructure, caching, reliability (parallel with Level 3) |
| Weeks 15–22 | Level 5 | Advanced architecture patterns |
| Weeks 18–26 | Level 6 | System design mastery, canonical problems |

**Total: 26 weeks (6–7 months) at 2 hours/day consistent.**
**Or: 12–14 months at 1 hour/day.**

---

## ✅ Project Portfolio Checklist

By the end of this roadmap, you should have built:

- [ ] TCP chat server from raw sockets + TLS
- [ ] Raw HTTP server + non-blocking I/O version
- [ ] Cache performance benchmark (memory hierarchy)
- [ ] Linux production diagnostics exercise
- [ ] Production-quality REST API (Task Manager)
- [ ] gRPC microservice (multi-language client)
- [ ] Real-time collaborative whiteboard (WebSockets + Redis pub/sub)
- [ ] GraphQL API with DataLoader (N+1 solved)
- [ ] Key-value store with WAL, compaction, and Bloom filter
- [ ] PostgreSQL performance workshop (10M rows, EXPLAIN, indexes)
- [ ] Social feed with multi-backend storage (PG + Redis + Cassandra)
- [ ] Transaction bug hunting exercise (lost updates, write skew)
- [ ] Postgres replication setup + failure simulation
- [ ] MIT 6.824 Labs 1–5 (Raft implementation)
- [ ] Kafka-based event-driven order system (saga + DLQ + exactly-once)
- [ ] Multi-node load balanced service with health checks
- [ ] Multi-layer caching system with stampede protection
- [ ] Rate limiting library (all 5 algorithms benchmarked)
- [ ] Resilient HTTP client (retry + circuit breaker + bulkhead)
- [ ] Full observability stack (Prometheus + Grafana + Jaeger)
- [ ] Microservices decomposition (3+ services + Kafka + API gateway)
- [ ] Bank ledger with event sourcing + projections + snapshotting
- [ ] AuthService with JWT, refresh tokens, revocation, OAuth
- [ ] Service mesh with Istio, mTLS, traffic splitting, distributed tracing
- [ ] 12 canonical system design documents (URL shortener → Distributed transaction)

---

## 🎯 The FAANG Interview Readiness Checklist

You're ready when you can:

- [ ] Explain any of the 10 seminal papers without looking them up
- [ ] Design any of the 12 canonical systems in 45 minutes with clear tradeoff justifications
- [ ] Answer "why did you choose X over Y?" for every technology decision
- [ ] Name 3 real-world failure modes for every architectural pattern you propose
- [ ] Quote real numbers: latency targets, QPS estimates, storage calculations
- [ ] Implement a basic consistent hash ring from scratch
- [ ] Explain Raft leader election in detail
- [ ] Explain MVCC and why it enables reads without blocking writes
- [ ] Describe exactly what happens when Kafka consumer crashes mid-processing
- [ ] Name the difference between linearizability and sequential consistency with examples

---

*This roadmap is comprehensive but not exhaustive — distributed systems is a lifetime of learning. The goal is to build the mental models that let you learn anything new quickly, not to memorize every technology. Good luck.*
