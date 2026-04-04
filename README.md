# 🗺️ The God-Level Backend Engineering Roadmap — v2
## From Junior REST APIs → FAANG-Ready Systems Engineer

> **Philosophy:** This roadmap follows a **BFS (Breadth-First) approach** — you learn topics at the same level in parallel before going deeper. Independent topics run side by side. Only when Topic B genuinely depends on Topic A does the order become strict. Every section has Theory, Technical Articles with real-world examples, hands-on Projects, and Books anchored to that topic.
>
> **v2 additions:** Two new full levels — **Level A: Software Design Patterns** and **Level B: DevOps Tooling & Container Infrastructure** — have been woven into the roadmap. Existing levels have been patched with tooling gaps (Redis operations, RabbitMQ, Celery, etc.) that v1 skipped.

---

## 📊 Learning Mix

| Type | Percentage | What It Means |
|---|---|---|
| 📖 Technical Articles / Real-World Case Studies | **50%** | How FAANG and top companies actually built this |
| 🛠️ Hands-On Projects | **30%** | Build it yourself — the only way to truly understand |
| 📚 Theory / Books | **20%** | Foundational mental models that make everything click |

---

## 🏗️ Roadmap Architecture: 9 Levels

```
Level 0 → Computer Fundamentals & Networking Internals
Level 1 → APIs, Protocols & Communication Patterns      (parallel with Level 0 Week 3+)
Level 2 → Databases Deep Cut                            (starts after Level 0)
Level A → Software Design Patterns                      (parallel with Level 2, feeds everything above)
Level B → DevOps Tooling & Container Infrastructure     (parallel with Level 3)
Level 3 → Distributed Systems Core                      (needs Level 2)
Level 4 → Infrastructure, Scalability & Reliability     (parallel with Level 3)
Level 5 → Advanced Architecture Patterns                (needs Level 3 + 4)
Level 6 → System Design Mastery & Interview Patterns    (needs everything above)
```

---

## 📚 The Core Book Stack (Read in This Order)

These are your spine. Everything else supplements them.

### 📗 Book 1: *Designing Data-Intensive Applications* — Martin Kleppmann (DDIA)
**The single most important book a backend engineer can read.** Dense, deep, and honest. Unlike books that teach you "how to use Kafka," this book teaches you *why* Kafka works, *what guarantees it makes*, and *where it will fail you*. Every chapter is referenced throughout this roadmap.

- **When to read it:** Start Chapter 1 at Level 0. Read one chapter per week alongside the corresponding roadmap level.
- **What it covers:** Storage engines, B-trees vs LSM trees, replication, partitioning, transactions, distributed systems theory, stream processing.
- **Why it's different:** It teaches you to *reason*, not memorize. After reading this, you'll understand tradeoffs instead of Googling "which database should I use."

### 📘 Book 2: *Software Architecture: The Hard Parts* — Neal Ford & Mark Richards
**The book DDIA doesn't cover.** DDIA teaches you *how the systems work*. This teaches you *how to decide what to build*. Full of real architectural ADRs, trade-off analysis, and case studies.

- **When to read it:** Start at Level 4. Read one chapter per week.
- **What it covers:** Service granularity, data ownership in distributed systems, saga patterns, transactional outbox, contract testing, evolutionary architecture.

### 📙 Book 3: *Clean Architecture* — Robert C. Martin
**The bridge between writing code and designing systems.** Where DDIA covers distributed systems and SATHA covers service architecture, Clean Architecture covers the *code-level* structural decisions that determine whether your system is maintainable or a nightmare.

- **When to read it:** Start at Level A alongside your design patterns study.
- **What it covers:** SOLID principles, dependency inversion, boundaries, use cases, entities — the "inner architecture" that frameworks can't give you.

### 📕 Book 4: *Design Patterns: Elements of Reusable Object-Oriented Software* — Gang of Four
**The original.** Dense, slightly dated syntax, but every pattern in this book is still alive in modern backend systems. You will recognize them everywhere once you've read this.

- **When to read it:** Start at Level A. Don't try to memorize — read to recognize.
- **Supplement with:** "Head First Design Patterns" (Java) or "Refactoring.Guru" online for clearer visualization.

### 🔖 Supporting Books (Read Chapters as Needed)
- **Google SRE Book** (free online) — Chapters 3, 6, 10, 14, 17
- **Building Microservices** — Sam Newman — service decomposition
- **The Linux Programming Interface** — Michael Kerrisk — OS-level depth
- **Database Internals** — Alex Petrov — deeper than DDIA on storage engines
- **Kubernetes in Action** — Marko Lukša — the best K8s book ever written
- **Docker Deep Dive** — Nigel Poulton — short, precise, practical

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
- **"What Every Programmer Should Know About Memory"** — Ulrich Drepper (lwn.net) — the classic. Read Parts 1, 2, and 3.
- **"Latency Numbers Every Programmer Should Know"** — Jeff Dean's original numbers + modern updates at "Latency Numbers" by Colin Scott. Memorize these.
- **"CPU Caches and Why You Care"** — Scott Meyers (YouTube, CppCon 2014) — best visual explanation of cache effects on data structures.
- **"How L1 and L2 CPU Caches Work"** — ExtremeTech — accessible explanation of why spatial/temporal locality matters.

#### 🛠️ Project: Cache Performance Benchmark
Write a simple benchmark in Go or Python that demonstrates:
1. Sequential array access vs random access — measure the difference
2. Row-major vs column-major matrix traversal — cache lines in action
3. False sharing: two threads writing to adjacent memory locations vs separate cache lines

**What you'll learn:** Why databases lay out data in pages. Why column-oriented databases are faster for analytics. Why Redis uses specific data structures.

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
- **"The C10K Problem"** — Dan Kegel (kegel.com/c10k.html) — the paper that defined modern async server design.
- **"How Node.js Works: A Look Behind the Scenes"** — Samer Buna — explains the libuv event loop, thread pool, and why Node can handle 10k connections single-threaded.
- **"Blocking I/O, Nonblocking I/O, And Epoll"** — Daan Leijen — technical walkthrough of Linux I/O mechanisms.
- **"Inside nginx: How we designed for performance and scale"** — NGINX blog — how nginx's event-driven model beats Apache's process-per-connection at scale.
- **"Fibers, Oh My!"** — Cloudflare blog — how Cloudflare uses coroutines in production for I/O concurrency.

#### 📚 Book Anchor
- **DDIA Chapter 1** — "Reliable, Scalable, and Maintainable Applications" — read this first as framing

#### 🛠️ Project: Build a Simple HTTP Server from Raw Sockets
No frameworks. Use raw TCP sockets to build a server that:
1. Accepts HTTP/1.1 GET requests
2. Parses headers manually
3. Returns a proper HTTP response with status codes

**Level up:** Rewrite it using non-blocking I/O with `epoll` (Linux). Benchmark both versions under 1000 concurrent connections.

---

### 0.3 — Networking Internals: TCP/IP, DNS, TLS

**Why it matters:** Every distributed system is a network of processes talking to each other. Engineers who understand TCP, DNS, and TLS debug production incidents in minutes.

#### 📖 Theory
- The OSI model (practical layers: L4 TCP/UDP, L7 HTTP)
- TCP three-way handshake, connection teardown, TIME_WAIT states
- TCP congestion control: why large data transfers start slow (slow start)
- UDP: when you want speed over reliability (DNS, video streaming, gaming)
- DNS resolution chain: browser cache → OS → recursive resolver → root → TLD → authoritative
- TLS 1.3: the handshake, certificate chain, session resumption

#### 📄 Technical Articles (Real-World)
- **"High Performance Browser Networking"** (Ch. 1–4) — Ilya Grigorik (free at hpbn.co) — the best networking primer ever written.
- **"Cloudflare: What is DNS?"** and **"How does HTTPS work?"** — Cloudflare's blog is a goldmine of clear technical explanations.
- **"How QUIC is Replacing TCP for HTTP/3"** — Fastly engineering blog — why Google invented a new transport protocol.
- **"The Story of One Latency Spike"** — Cloudflare blog — a real production incident where TCP's TIME_WAIT states caused cascading failures.
- **"TLS 1.3: 0-RTT, resumption, and anti-replay"** — Cloudflare blog — the internals of modern TLS.

#### 🛠️ Project: Build a TCP Chat Server
Raw sockets, no frameworks:
1. Multi-client server with rooms/channels
2. Message broadcast to all clients in a room
3. Handle client disconnections gracefully (detect broken connections)

**Level up:** Implement a simple binary wire protocol. Define a header (message type + length) + body. Benchmark: how many concurrent connections can your server hold?

---

### 0.4 — Linux Command Line for Backend Engineers

**Why it matters:** You will debug production. Production runs on Linux. Engineers who can fluently use `strace`, `lsof`, `netstat`, `perf`, and `tcpdump` are 10x more effective in incidents.

#### 📄 Technical Articles (Real-World)
- **"Linux Performance Analysis in 60,000 Milliseconds"** — Netflix Tech Blog (Brendan Gregg) — the canonical list of commands to run when diagnosing a production performance problem.
- **"Linux Tracing Systems & How They Fit Together"** — Julia Evans (jvns.ca) — explains strace, ltrace, perf, eBPF in plain language.
- **"The USE Method"** — Brendan Gregg — a systematic methodology for performance analysis: Utilization, Saturation, Errors.
- **"How Containers Work"** — Julia Evans — cgroups, namespaces, the actual Linux primitives behind Docker.

#### 🛠️ Project: Diagnose a Simulated Production Issue
Set up a small app with an intentional bug (memory leak, CPU spin, too many open file descriptors). Use only Linux tools to diagnose it:
- `top`/`htop` for CPU/memory
- `lsof` for file descriptors
- `strace -p <pid>` to trace syscalls
- `ss` or `netstat` for connections
- `tcpdump` to capture actual packets

---

## ⚡ Level 1: APIs, Protocols & Communication Patterns (Weeks 3–8)

> **Goal:** Master how distributed services talk to each other — at the protocol level, not just the "which framework to use" level.

> **BFS Note:** 1.1, 1.2, and 1.3 are **independent** — learn them in parallel. 1.4 synthesizes all of them.

---

### 1.1 — REST: The Deep Cut (Beyond CRUD)

Most junior engineers think they know REST because they've built CRUD APIs. Real REST is about *constraints and tradeoffs*.

#### 📖 Theory
- REST constraints: statelessness, uniform interface, hypermedia (HATEOAS)
- HTTP verbs as semantic contracts (why PUT is idempotent but POST isn't — and why that matters)
- HTTP status codes: the semantic meaning of 200 vs 202 vs 204, 400 vs 422, 429, 503
- Idempotency keys: why Stripe requires them for payment APIs
- Content negotiation: Accept / Content-Type headers and versioning strategies

#### 📄 Technical Articles (Real-World)
- **"Zalando RESTful API Guidelines"** — github.com/zalando/restful-api-guidelines — the most thorough, production-hardened REST API guide ever published.
- **"Best Practices for Designing a Pragmatic RESTful API"** — Vinay Sahni (vinaysahni.com)
- **"Stripe's API Design Principles"** — Stripe Dev Blog — how Stripe built an API used by millions of developers.
- **"How We Versioned Our REST API at Intercom"** — Intercom Engineering — real case study of API versioning strategy.
- **"Idempotency: Making APIs Safer"** — Stripe Engineering — why Stripe introduced idempotency keys.

#### 🛠️ Project: Build a Production-Quality REST API
Build a Task Management API (like a mini Jira):
- Full CRUD with proper HTTP semantics
- Cursor-based pagination
- Filtering and sorting with validation
- Idempotency keys on state-changing endpoints
- API versioning strategy
- Rate limiting (token bucket algorithm, in-memory)
- OpenAPI spec (Swagger) — document everything

---

### 1.2 — gRPC, Protobuf & Binary Protocols

**Why it matters:** Inside a microservices system, services talk to each other thousands of times per second. REST over JSON is simple but expensive. gRPC fixes this and is used heavily inside Google, Netflix, and Uber.

#### 📖 Theory
- Protocol Buffers: field numbers, varint encoding, backward/forward compatibility rules
- gRPC over HTTP/2: multiplexing, header compression, streaming
- Four gRPC modes: unary, server streaming, client streaming, bidirectional streaming
- When to use gRPC vs REST: internal service communication vs public APIs

#### 📄 Technical Articles (Real-World)
- **"Why We Use gRPC at Square"** — Square Engineering blog — real-world adoption story with measured latency improvements.
- **"gRPC vs REST"** — Google Cloud Blog — written by the people who invented gRPC.
- **"Protobuf Encoding"** — Google developers.google.com — the official encoding spec.
- **"How Netflix Uses gRPC"** — Netflix TechBlog — migration at massive scale.
- **"Schema Evolution in Avro, Protocol Buffers and Thrift"** — Martin Kleppmann's blog.

#### 📚 Book Anchor
- **DDIA Chapter 4** — "Encoding and Evolution"

#### 🛠️ Project: Build a gRPC Microservice
- Protobuf schema: User, CreateUserRequest, GetUserRequest, ListUsersResponse
- Unary and Server streaming RPCs
- Interceptors for logging and auth token validation
- Client written in a *different language* to prove interoperability

---

### 1.3 — WebSockets, SSE & Real-Time Communication

#### 📖 Theory
- HTTP's request-response limitation for real-time
- Long polling: a hack, but it works. What it costs in server resources.
- Server-Sent Events (SSE): HTTP/1.1 streaming, unidirectional, browser-native
- WebSockets: full-duplex, single TCP connection, the upgrade handshake
- WebSocket at scale: sticky sessions, connection state, horizontal scaling challenges

#### 📄 Technical Articles (Real-World)
- **"How Slack Works: WebSockets and the Real-Time Messaging API"** — Slack Engineering blog
- **"Server-Sent Events vs WebSockets"** — Ably blog — clear technical comparison
- **"Scaling WebSocket Connections to 1 Million"** — Fanout.io
- **"Discord: How Discord Handles Two and Half Million Concurrent Voice Users"** — Discord Engineering

#### 🛠️ Project: Real-Time Collaborative Whiteboard
- WebSocket server with rooms
- Real-time broadcast of drawing operations
- Reconnection with state replay
- Horizontal scaling: use Redis pub/sub so multiple server instances can relay messages

---

### 1.4 — GraphQL: When REST Isn't Enough

#### 📖 Theory
- The over-fetching and under-fetching problems with REST
- GraphQL type system: Schema Definition Language, resolvers, N+1 query problem
- DataLoader pattern: batching and caching resolver calls
- GraphQL subscriptions: real-time with WebSockets
- Federation: how large organizations split a GraphQL schema across teams

#### 📄 Technical Articles (Real-World)
- **"How Facebook Invented GraphQL"** — Lee Byron (GraphQL co-creator) at React Europe
- **"GitHub's Move to GraphQL"** — GitHub Engineering blog
- **"Shopify's Scaling GraphQL at Production"** — Shopify Engineering
- **"The N+1 Problem in GraphQL"** — Apollo blog

#### 🛠️ Project: GraphQL API with DataLoader
Build a blog platform API with GraphQL with depth limiting, complexity analysis, subscriptions, and DataLoader — benchmark before/after.

---

## ⚡ Level A: Software Design Patterns (Weeks 4–10, Parallel with Level 2)

> **Goal:** Move from writing code that *works* to writing code that *scales, changes, and survives*. Design patterns are the vocabulary senior engineers use when talking about code. Not knowing them is like discussing architecture without knowing what a load-bearing wall is.

> **Why this level exists:** The original roadmap jumped straight from API design to databases without covering the structural layer in between — the layer that determines whether your services are maintainable or a nightmare to change three months later.

> **BFS Note:** A.1 (SOLID + OOP patterns), A.2 (Creational/Structural/Behavioral GoF), A.3 (Architectural patterns), and A.4 (DDD) are largely **independent** — do them in parallel. A.5 (Concurrency patterns) depends on understanding A.1 first.

---

### A.1 — SOLID Principles and Why They Exist

**Why it matters:** SOLID is not a checklist. Each principle solves a specific pain point that you *will* encounter in any non-trivial codebase. Understanding *why* each principle exists is more important than memorizing the acronym.

#### 📖 Theory

**Single Responsibility Principle (SRP)**
- A module should have one reason to change
- Why it fails: a `UserService` that does authentication, sends emails, and handles billing has three reasons to change — and every change risks breaking the other two
- Real cost: tight coupling means you can't test or deploy components independently

**Open/Closed Principle (OCP)**
- Open for extension, closed for modification
- Why it matters: adding a new payment method shouldn't require editing your existing `PaymentProcessor` class
- Implementation: strategy pattern, dependency injection, plugin architectures

**Liskov Substitution Principle (LSP)**
- Subtypes must be substitutable for their base types
- Why it fails: a `ReadOnlyList` extending `List` but throwing on `Add()` breaks every caller that expects a real list
- Real cost: violations cause unexpected runtime crashes that the compiler can't catch

**Interface Segregation Principle (ISP)**
- Clients should not be forced to depend on interfaces they don't use
- Why it fails: a `Worker` interface with `work()` and `eat()` forces a `RobotWorker` to implement `eat()` — a method it doesn't need
- Real cost: changes to unused interface methods force unnecessary recompilation and redeployment

**Dependency Inversion Principle (DIP)**
- High-level modules should not depend on low-level modules — both should depend on abstractions
- Why it matters: `OrderService` depending directly on `MySQLRepository` means swapping to Postgres requires changing business logic
- Implementation: dependency injection, repository pattern, ports and adapters

#### 📄 Technical Articles (Real-World)
- **"SOLID Principles: The Software Developer's Framework to Robust & Maintainable Code"** — Khalil Stemmler (khalilstemmler.com) — the best modern treatment of SOLID. Each principle has real TypeScript/JS examples.
- **"SOLID Is Not Solid"** — Dan North — a useful counterargument that keeps you from applying SOLID dogmatically.
- **"The Wrong Abstraction"** — Sandi Metz — why premature abstraction (extracting too early for OCP) is worse than duplication. Essential balance to SOLID orthodoxy.
- **"Goodbye, Clean Code"** — Dan Abramov (React core team) — a senior engineer's reflection on when clean code principles become anti-patterns.
- **"Hexagonal Architecture"** — Alistair Cockburn (the original article) — the direct application of DIP at architecture scale.

#### 📚 Book Anchor
- **Clean Architecture** (Robert C. Martin) — Part III: "Design Principles" — Chapters 7–11 cover each SOLID principle with concrete examples.

#### 🛠️ Project: Refactor a Violation-Ridden Codebase
Start with a deliberately badly designed e-commerce service:
1. `OrderController` that directly queries the database, sends emails, and calculates tax — an SRP violation
2. A `PaymentProcessor` class with a giant `switch` statement for each payment type — an OCP violation
3. A `SmtpEmailSender` hardcoded into `OrderService` — a DIP violation

**Refactor step by step:**
1. Extract `OrderRepository` interface and a concrete `PostgresOrderRepository` — apply DIP
2. Create `PaymentStrategy` interface with `CreditCardPayment`, `PaypalPayment`, `StripePayment` implementations — apply OCP
3. Split `OrderService` into `OrderService` (business logic), `OrderNotifier` (email), `TaxCalculator` (tax) — apply SRP

**Measure the difference:** Can you now test `OrderService` without a database? Can you add `CryptoPayment` without touching existing code? The answers tell you if refactoring worked.

---

### A.2 — GoF Design Patterns: The 23 Patterns You'll Actually Use

The Gang of Four book has 23 patterns. In backend engineering, a subset of these appear constantly. This section focuses on the ones you'll encounter in real systems — not as academic exercises but as patterns you'll recognize in Flask, Django, Go's standard library, and Spring.

#### 📖 Theory — The Patterns That Actually Matter in Backend

**Creational Patterns (How objects are created)**

*Singleton*
- One instance of a class across the entire application — database connection pool, configuration, logger
- Why it's dangerous: global state, testing nightmares. The Go pattern: package-level variable initialized with `sync.Once`
- Real-world: `db.DB` in Go's `database/sql`, Flask's `app` object, Django settings

*Factory Method / Abstract Factory*
- Decouple the creation of objects from their use
- Real-world: SQLAlchemy's `create_engine()` — you don't know if it's Postgres or MySQL, you just get an engine
- Real-world: Go's `http.NewServeMux()`, Django's `get_user_model()`

*Builder*
- Construct complex objects step by step, especially those with many optional parameters
- Real-world: HTTP request builders, query builders (Django ORM's chained `.filter().order_by().limit()`), `testcontainers` setup
- Alternative: named parameters / options pattern in Go

*Prototype*
- Clone an existing object instead of creating from scratch
- Real-world: deep copying configuration objects, duplicating request contexts

**Structural Patterns (How objects are composed)**

*Adapter*
- Convert one interface to another — the "translator" pattern
- Real-world: wrapping a third-party payment API (`StripeAdapter` implements your `PaymentGateway` interface)
- Real-world: database drivers — they all implement the same `database/sql` interface regardless of backend

*Decorator*
- Add behavior to objects dynamically without subclassing
- Real-world: Python's `@functools.wraps`, Flask's `@app.route`, middleware in Express/Gin/FastAPI
- Real-world: adding logging, caching, or authentication to a service *without touching the service*

*Facade*
- Provide a simplified interface to a complex subsystem
- Real-world: a `NotificationService` that internally uses SMTP, SMS gateway, and push notification APIs — callers just call `send()`
- Real-world: Django's ORM is a facade over raw SQL

*Proxy*
- Control access to another object — add behavior transparently
- Real-world: lazy loading (ORM relationship not loaded until accessed), caching proxy (check cache before hitting DB), circuit breaker proxy
- Real-world: gRPC stubs are proxies — they look like local function calls but are actually network calls

*Composite*
- Treat individual objects and groups of objects the same way
- Real-world: file system (file and directory both implement same interface), middleware pipelines, permission systems (user, group, role all implement `HasPermission`)

**Behavioral Patterns (How objects communicate)**

*Strategy*
- Define a family of algorithms and make them interchangeable
- Real-world: sorting strategies in an ORM, authentication strategies (JWT vs session vs API key), rate limiting algorithms (token bucket vs sliding window)
- Real-world: Go's `sort.Interface`, Python's `key=` parameter in `sorted()`

*Observer*
- When one object changes state, all dependents are notified automatically
- Real-world: Django signals (`post_save`, `pre_delete`), event emitters in Node.js, webhook systems, UI state management
- Real-world: database triggers, message queue pub/sub

*Command*
- Encapsulate a request as an object — enables undo, queueing, logging
- Real-world: background job systems (Celery tasks are Commands), database migration files, HTTP request objects, message queue messages

*Chain of Responsibility*
- Pass a request along a chain of handlers until one handles it
- Real-world: HTTP middleware pipelines (authentication → rate limiting → routing → handler), Django middleware, exception handlers

*Template Method*
- Define the skeleton of an algorithm, let subclasses fill in specific steps
- Real-world: Django's class-based views (`get()`, `post()` override the template), base repository classes, migration frameworks

*Iterator*
- Provide a way to sequentially access elements without exposing underlying structure
- Real-world: database cursors, Go channels, Python generators, paginated API responses

*State*
- Allow an object to alter its behavior when its internal state changes
- Real-world: order status machine (pending → confirmed → shipped → delivered), circuit breaker states (closed → open → half-open), TCP connection states

*Mediator*
- Reduce chaotic dependencies between objects by centralizing communication
- Real-world: message brokers (Kafka, RabbitMQ), event buses, API gateways, Redux store

#### 📄 Technical Articles (Real-World)
- **"Refactoring.Guru — Design Patterns"** (refactoring.guru/design-patterns) — the best free visual reference. Every pattern has real code examples in multiple languages. Bookmark this and refer to it constantly.
- **"Python Patterns"** — python-patterns.guide — Brandon Rhodes' guide to GoF patterns specifically in Python. Essential for Flask/Django/FastAPI engineers.
- **"Design Patterns in Go"** — golangbyexample.com/all-design-patterns-golang — Go-idiomatic implementations of all GoF patterns.
- **"The Decorator Pattern in Python"** — Real Python blog — deep dive into Python decorators as the Decorator pattern in practice.
- **"How Django Uses Design Patterns"** — Simple is Better Than Complex — identifies every GoF pattern used throughout Django's source code.
- **"Don't Use Design Patterns"** — coding horror / various — the counterargument, for balance. Patterns can be overused.

#### 📚 Book Anchor
- **Design Patterns: Elements of Reusable OO Software** (GoF) — Read the pattern catalog. Don't start with Chapter 1 — jump directly to the patterns you encounter.
- **Head First Design Patterns** — friendlier treatment with visual examples. Better for first exposure.
- **Clean Architecture** (Robert C. Martin) — Part IV: "Component Principles"

#### 🛠️ Project: Pattern Recognition + Implementation in Your Stack

**Phase 1: Recognition exercise**
Go through a large open-source Python or Go project (Django, Flask, FastAPI's source, or a Go web framework). Identify at least one real instance of each of these patterns: Factory, Decorator, Strategy, Observer, Command, Proxy, Facade, Chain of Responsibility.

**Phase 2: Build a payment processing system using patterns deliberately**
1. **Strategy Pattern:** `PaymentProcessor` interface with `StripeStrategy`, `PaypalStrategy`, `InvoiceStrategy`
2. **Factory Pattern:** `PaymentProcessorFactory.create(method: string) → PaymentProcessor`
3. **Decorator Pattern:** Wrap any processor with `LoggingDecorator`, `RetryDecorator`, `CachingDecorator`
4. **Command Pattern:** Each payment is a `PaymentCommand` that can be queued, retried, or rolled back
5. **Observer Pattern:** On payment success/failure, notify `EmailObserver`, `WebhookObserver`, `MetricsObserver`
6. **State Pattern:** `PaymentStateMachine` with states: Pending → Processing → Completed | Refunded | Failed

**Phase 3: Test isolation exercise**
Because you used Strategy + DI, replace `StripeStrategy` with `MockPaymentStrategy` in all tests — zero code changes to the core `PaymentProcessor`.

---

### A.3 — Architectural Patterns: Beyond GoF

These are patterns at the *service* and *application* level — above individual classes but below the distributed systems level.

#### 📖 Theory

**Repository Pattern**
- Abstract all data access behind an interface. The service layer never touches SQL directly.
- `UserRepository` interface with `FindById()`, `Save()`, `Delete()` — implemented by `PostgresUserRepository`
- **Why it matters:** swap databases without touching business logic. Test without a database.

**Unit of Work Pattern**
- Track changes to multiple objects and flush them all to the database in one transaction
- Real-world: Django's `transaction.atomic()`, SQLAlchemy's `Session`, Hibernate's `EntityManager`
- **Why it matters:** prevents partial writes when multiple entities need to be saved atomically

**CQRS at the Code Level (before the distributed version)**
- Separate read models from write models within a single service
- Write side: validates business rules, applies commands, emits events
- Read side: optimized query objects that return flat DTOs — no lazy loading, no ORM overhead
- **Why it matters:** read and write patterns are different. Forcing the same model to do both creates impedance.

**Service Layer Pattern**
- A dedicated class that orchestrates business logic — calls repositories, applies domain rules, handles transactions
- Distinct from: controllers (HTTP concerns), repositories (data concerns)
- Real-world: Django's "fat models, thin views" (though service layer is often better than fat models)

**Ports and Adapters (Hexagonal Architecture)**
- Your application core depends only on abstract interfaces (ports), never on concrete implementations
- Adapters implement ports: `PostgresUserAdapter`, `InMemoryUserAdapter`, `HttpUserAdapter`
- **Why it matters:** business logic is framework-agnostic and fully testable in isolation
- Real-world: FastAPI with a clean domain layer, Go's interface-based design

**Event-Driven Architecture at the Code Level**
- Domain events: objects emitted when something significant happens in the domain
- `OrderPlaced`, `PaymentReceived`, `ItemShipped` — dispatched to handlers within the same process
- Real-world: Django signals, Spring's `ApplicationEventPublisher`
- **Why it matters:** decouples components without introducing a message broker

**Outbox Pattern**
- Atomically write a business state change and an event notification in the same DB transaction
- A poller/CDC reads the outbox table and delivers events to the message broker
- **Why it matters:** solves the "write to DB + publish to Kafka atomically" problem without distributed transactions

#### 📄 Technical Articles (Real-World)
- **"The Repository Pattern"** — Martin Fowler (martinfowler.com/eaaCatalog/repository.html) — the canonical definition.
- **"Hexagonal Architecture"** — Alistair Cockburn — the original article. Short and precise.
- **"Ports and Adapters in Python"** — Architecture Patterns with Python (free online, cosmicpython.com) — the best modern treatment of hexagonal architecture in Python. The whole book is free and excellent.
- **"The Outbox Pattern"** — Debezium blog — how to atomically write to DB and emit events using CDC.
- **"Service Layer vs Domain Model"** — Martin Fowler — when a transaction script is fine and when you need a full domain model.
- **"Patterns of Enterprise Application Architecture"** — Martin Fowler — the source book for Repository, Unit of Work, Service Layer, Data Mapper. Read as reference.

#### 📚 Book Anchor
- **"Architecture Patterns with Python"** — Harry Percival & Bob Gregory (free at cosmicpython.com) — the most practical book on applying clean architecture to a real Python web service. Read alongside Level A.

#### 🛠️ Project: Rebuild the Task Manager API with Clean Architecture

Take the Task Management API from Level 1.1 and completely restructure it using:
1. **Domain layer:** `Task` entity, `TaskRepository` interface, domain events (`TaskCreated`, `TaskAssigned`, `TaskCompleted`)
2. **Service layer:** `TaskService` orchestrates use cases — calls repository, dispatches domain events
3. **Repository layer:** `PostgresTaskRepository` and `InMemoryTaskRepository` (for tests) both implementing `TaskRepository`
4. **API layer:** FastAPI/Flask/Gin handlers that do nothing but parse HTTP and call service layer
5. **Test:** Write unit tests for `TaskService` using `InMemoryTaskRepository` — no database, no HTTP, pure logic

**Prove the architecture works:** Swap `PostgresTaskRepository` for `InMemoryTaskRepository` in all unit tests without changing a single line of service layer code.

---

### A.4 — Domain-Driven Design: Strategic Patterns

**Why it matters:** DDD is how you think about building software when the business domain is complex. Every FAANG senior engineer interview will eventually ask you to design a system — DDD gives you the vocabulary to define service boundaries correctly.

#### 📖 Theory

**Ubiquitous Language**
- Developers, product managers, and domain experts share a single language — code uses the exact terms the business uses
- Why it matters: translation between "business language" and "technical language" is where bugs are born
- Real-world: at Stripe, the word "charge" means something very specific. At Airbnb, "reservation" vs "booking" are different things. The code reflects this.

**Bounded Context**
- A bounded context is a linguistic boundary — a subsystem where a given model applies consistently
- `Order` means different things to fulfillment (has a physical address) and billing (has a payment method) — they're different models in different bounded contexts
- **Why it matters:** this is how you define microservice boundaries correctly. Each bounded context = one (or more) service.

**Aggregates and Aggregate Roots**
- A cluster of domain objects that are treated as a single unit for data changes
- The aggregate root is the only entry point — you never modify a child entity directly
- Real-world: `Order` aggregate root contains `OrderLineItems` — you never add a line item directly, you call `order.addItem()`
- **Why it matters:** aggregates define transaction boundaries. The whole aggregate is saved atomically.

**Value Objects vs Entities**
- Entity: has identity that persists over time (a User has the same ID even if their email changes)
- Value object: defined entirely by its attributes, no identity (a Money value object with amount + currency)
- **Why it matters:** value objects are immutable and can be compared by value — this eliminates a class of mutation bugs

**Domain Events**
- Something significant that happened in the domain, expressed in past tense
- `OrderPlaced`, `PaymentFailed`, `InventoryReserved` — first-class objects in the domain
- **Why it matters:** domain events are the natural integration points between bounded contexts

**Anti-Corruption Layer (ACL)**
- A translation layer between your clean domain model and an external system's messy model
- Real-world: consuming a legacy SOAP API for payments — your `PaymentAdapter` translates from your clean `Payment` entity to the SOAP DTO
- **Why it matters:** prevents the external system's data model from leaking into your domain

#### 📄 Technical Articles (Real-World)
- **"Domain-Driven Design Quickly"** — InfoQ mini-book (free PDF) — best concise introduction to DDD concepts.
- **"Implementing DDD at Airbnb"** — Airbnb Engineering — how they applied bounded contexts to split their monolith.
- **"Strategic DDD: Bounded Contexts and Context Maps"** — Alberto Brandolini — the strategic side of DDD explained clearly.
- **"Aggregates and Repositories in DDD"** — Vaughn Vernon — detailed guide to aggregate design.
- **"Domain Events vs Integration Events"** — Jimmy Bogard — the important distinction between events inside a bounded context vs events crossing context boundaries.

#### 📚 Book Anchor
- **Domain-Driven Design** (Eric Evans) — "The Blue Book." Dense. Read Parts 1 and 2 first. Refer to Part 3 as needed.
- **Implementing Domain-Driven Design** (Vaughn Vernon) — "The Red Book." More concrete examples. More practical starting point.

#### 🛠️ Project: Model a Bounded Context for an E-Commerce System
Design and implement the `Order Management` bounded context of an e-commerce system:
1. **Identify the aggregate:** `Order` (root), `OrderLineItem`, `ShippingAddress` (value object), `Money` (value object)
2. **Business rules in the aggregate:** can't ship an order with zero items, can't cancel a shipped order, total = sum of line items × quantities
3. **Repository:** `OrderRepository` interface. Implement both `PostgresOrderRepository` and `InMemoryOrderRepository`
4. **Domain events:** `OrderPlaced`, `OrderCancelled`, `OrderShipped` — dispatched by aggregate methods
5. **Anti-corruption layer:** consume a (simulated) legacy inventory SOAP API — write an `InventoryAdapter` that translates to your clean `Stock` value object
6. **Context map:** define the relationship between `Order Management` and `Inventory Management` bounded contexts — Customer/Supplier relationship, where Order is downstream

---

### A.5 — Concurrency Patterns

**Why it matters:** Every non-trivial backend service is concurrent. Race conditions, deadlocks, and thundering herds are the bugs that bring production down at 3am. Knowing the patterns means you write concurrent code that is provably safe.

#### 📖 Theory

**Mutex and Read-Write Lock**
- When to use each: write-heavy workloads (mutex), read-heavy workloads (RWMutex)
- Real-world: Go's `sync.RWMutex` for protecting an in-memory cache that's read 1000x per second but written once per minute

**Worker Pool Pattern**
- Fixed pool of goroutines/threads consuming from a shared job queue
- Prevents unbounded goroutine spawning on every request
- Real-world: image processing, sending bulk emails, database migrations
- Implementation: Go buffered channel as queue + N goroutines in a `for range` loop

**Fan-Out / Fan-In**
- Fan-out: distribute work to multiple goroutines in parallel
- Fan-in: collect results from multiple goroutines into one channel
- Real-world: scatter-gather for querying multiple services simultaneously, parallel database queries

**Pipeline Pattern**
- Chain of stages, each consuming from the previous and producing for the next
- Real-world: data ETL pipelines, image resizing pipeline (decode → resize → encode → upload)
- Implementation: Go channels connecting goroutine stages

**Semaphore Pattern**
- Limit the number of concurrent operations — don't open 10,000 database connections simultaneously
- Implementation: Go buffered channel used as a counting semaphore
- Real-world: rate-limited API client, bounded connection pool

**Context Propagation (Cancellation + Deadlines)**
- Propagate cancellation signals from incoming HTTP requests down through all goroutines
- When a user cancels their request, all in-flight work for that request should stop immediately
- Real-world: Go's `context.Context` threaded through every function call

**Optimistic Concurrency Control**
- Read → modify → write with a version check — retry if someone else modified meanwhile
- Alternative to locks: no blocking, but requires retry logic
- Real-world: database row versioning (`UPDATE ... WHERE version = $1`), CAS operations in Redis

#### 📄 Technical Articles (Real-World)
- **"Concurrency in Go"** — Katherine Cox-Buday (book, but Chapter summaries on Go blog) — the definitive guide to Go concurrency patterns.
- **"Go Concurrency Patterns"** — Rob Pike (YouTube, Google I/O 2012) — the canonical talk. Watch this.
- **"Advanced Go Concurrency Patterns"** — Sameer Ajmani (YouTube, Google I/O 2013) — the follow-up. Also essential.
- **"The Little Book of Semaphores"** — Allen B. Downey (free PDF) — the classic textbook on concurrency primitives, OS-agnostic.
- **"Visualizing Concurrency in Go"** — divan.dev — beautiful visualizations of goroutine interaction. Surprisingly illuminating.
- **"asyncio in Python: A Complete Walkthrough"** — Real Python — for async/await concurrency patterns in Python async frameworks (FastAPI, aiohttp).

#### 🛠️ Project: Concurrent Image Processing Service
Build an HTTP service that accepts image uploads and processes them (resize to 3 sizes) concurrently:
1. **Worker pool:** 5 worker goroutines, requests queue into a buffered channel
2. **Fan-out / fan-in:** each worker fans out to 3 goroutines (one per target size) and fans in the 3 results
3. **Semaphore:** limit max 10 concurrent in-flight resize operations system-wide
4. **Context cancellation:** if the HTTP request is cancelled (client disconnects), stop all in-flight work for that request
5. **Race detector:** run with `go test -race` and fix all data races
6. **Load test:** bombard with 500 concurrent requests. Verify the worker pool prevents OOM.

---

## ⚡ Level 2: Databases — The Deep Cut (Weeks 4–10)

> **Goal:** Transform from someone who *uses* databases to someone who *understands* them.

> **BFS Note:** 2.1, 2.2, and 2.3 are mostly independent — do them in parallel. 2.4 depends on understanding 2.1 internals. 2.5 depends on 2.1 + 2.2.

---

### 2.1 — Database Internals: How They Actually Store Your Data

#### 📖 Theory
- **B-Trees:** pages, branching factor, in-place updates, write amplification
- **LSM Trees:** append-only writes, SSTables, compaction, why writes are fast, read amplification
- **Write-Ahead Log (WAL):** how databases survive crashes
- **MVCC:** how PostgreSQL allows reads without blocking writes
- Buffer pool / buffer cache: why databases manage their own memory
- Page layout: how rows are stored on disk pages in PostgreSQL

#### 📄 Technical Articles (Real-World)
- **"B-Trees and Database Indexes"** — Use The Index Luke (use-the-index-luke.com) — the best practical guide to understanding how B-tree indexes affect query performance.
- **"How RocksDB Works"** — Meta Engineering Blog — LSM tree engine used inside MySQL (MyRocks), CockroachDB, TiKV.
- **"PostgreSQL's MVCC"** — Cybertec blog "MVCC and Autovacuum Explained"
- **"The Log: What every software engineer should know about real-time data's unifying abstraction"** — Jay Kreps (LinkedIn)
- **"How Does a Relational Database Work?"** — Christophe Calliau

#### 📚 Book Anchor
- **DDIA Chapter 3** — "Storage and Retrieval" — read it twice.
- **Database Internals** (Alex Petrov) — Chapters 2 and 5

#### 🛠️ Project: Build a Key-Value Store (Bitcask Style)
1. **v1:** Append-only log file + in-memory hashmap (key → byte offset in log)
2. **v2:** Log compaction — merge old log files into a new compacted file
3. **v3:** Add a Bloom filter to skip disk reads for missing keys
4. **v4:** CRC checksums on each record — detect corruption on read

---

### 2.2 — PostgreSQL: Professional-Level SQL and Indexing

#### 📖 Theory
- EXPLAIN and EXPLAIN ANALYZE: reading query plans — seq scan vs index scan vs index-only scan
- Index types: B-tree, Hash, GIN (for JSONB/full-text), GiST (for geometric/range types)
- Partial indexes, expression indexes, composite index column order
- Table statistics and the query planner — why `ANALYZE` matters
- Connection pooling: why PgBouncer exists, what "connection overhead" actually costs
- Partitioning: range, list, hash — when and why to partition

#### 📄 Technical Articles (Real-World)
- **"Explaining the Postgres Query Optimizer"** — pganalyze.com
- **"Connection Pooling with PgBouncer"** — Crunchy Data blog
- **"Partial Indexes in PostgreSQL"** — Heap Engineering Blog — real case study of a 10x query speedup
- **"How Notion Sharded Their Postgres Database"** — Notion Engineering blog
- **"Why Discord Moved from MongoDB to Cassandra... and then from Cassandra to ScyllaDB"** — Discord Engineering

#### 🛠️ Project: Advanced PostgreSQL Workshop
Load 10M+ rows, run slow queries, use EXPLAIN ANALYZE to find problems, add appropriate indexes, set up PgBouncer, implement table partitioning.

---

### 2.3 — NoSQL Databases: When and Why

#### 📖 Theory
- **Document stores (MongoDB/DynamoDB):** nested data, flexible schema, when embedding vs referencing
- **Wide-column stores (Cassandra/HBase):** data model around read patterns, partition keys, clustering columns
- **Key-value stores (Redis/DynamoDB):** single-key access, extreme speed, limited query flexibility
- **Graph databases (Neo4j):** when relationships are first-class
- **Time-series databases (InfluxDB/TimescaleDB):** high-write, time-ordered data, downsampling

#### 📄 Technical Articles (Real-World)
- **"Amazon DynamoDB: How It Works"** — AWS docs
- **"Cassandra Data Modeling"** — DataStax Academy
- **"How Instagram Uses Cassandra"** — Instagram Engineering blog
- **"Redis Data Structures and When to Use Them"** — Redis official blog
- **"Rethinking the Database Layer for Time Series"** — InfluxDB blog

#### 📚 Book Anchor
- **DDIA Chapter 2** — "Data Models and Query Languages"

#### 🛠️ Project: Build a Social Feed with Multiple Storage Backends
Use PostgreSQL for user accounts, Redis for timeline cache, Cassandra for notification history — and benchmark read latency from each under load.

---

### 2.4 — Transactions, ACID, and Isolation Levels

#### 📖 Theory
- ACID: what each property actually means in practice
- Isolation levels: Read Uncommitted → Read Committed → Repeatable Read → Serializable
- Phenomena: dirty reads, non-repeatable reads, phantom reads, write skew, lost updates
- Optimistic vs pessimistic locking
- Two-Phase Locking (2PL) vs MVCC
- Serializable Snapshot Isolation (SSI) — PostgreSQL's approach

#### 📄 Technical Articles (Real-World)
- **"Please stop calling databases CP or AP"** — Martin Kleppmann's blog
- **"A Critique of ANSI SQL Isolation Levels"** — Berenson et al. (1995 paper)
- **"Avoiding Double-Charging Users with Idempotency and Distributed Locks"** — Brandur Leach (Stripe)
- **"Transactions: Myths, Surprises, and Opportunities"** — Martin Kleppmann, GOTO 2015 (YouTube)

#### 📚 Book Anchor
- **DDIA Chapter 7** — "Transactions" — read slowly, twice.

#### 🛠️ Project: Find and Fix Real Transaction Bugs
Deliberately trigger lost updates, write skew, and phantom reads in a bank account system. Fix each correctly. Benchmark the performance cost of Serializable vs Read Committed.

---

### 2.5 — Database Scaling: Replication, Sharding, and Connection Management

#### 📖 Theory
- Single-leader replication: replication lag, read-your-writes consistency
- Multi-leader replication: conflict detection and resolution
- Leaderless replication: quorums (W + R > N), sloppy quorums
- Sharding strategies: range-based, hash-based, consistent hashing
- CQRS with read replicas

#### 📄 Technical Articles (Real-World)
- **"How Notion Sharded Their Postgres Database"** — Notion Engineering
- **"Vitess: MySQL Sharding at YouTube/GitHub Scale"** — PlanetScale blog
- **"Read Replicas at Instacart"** — Instacart Engineering
- **"How We Scaled Our Database to 1.5B Rows"** — Heap Analytics Engineering

#### 📚 Book Anchor
- **DDIA Chapter 5** — "Replication"
- **DDIA Chapter 6** — "Partitioning"

---

## ⚡ Level B: DevOps Tooling & Container Infrastructure (Weeks 6–14, Parallel with Level 3)

> **Goal:** Backend engineers at FAANG and top startups are expected to own their services — containerize them, deploy them, observe them, and not wait for a DevOps team to do it for them. This level covers the real infrastructure tooling you use daily.

> **Why this level exists:** The original roadmap completely skipped Docker, Kubernetes, CI/CD, and message queue operations. These aren't optional extras — they are core backend engineering skills in 2024. You will use these tools every single day.

> **BFS Note:** B.1 (Docker), B.2 (Compose + Networking), B.3 (Kubernetes), B.4 (Message Queues), B.5 (Redis Operations), and B.6 (CI/CD) are broadly independent — do them in roughly this order since B.2 depends on B.1 and B.3 builds on B.2's concepts.

---

### B.1 — Docker: Containers from First Principles

**Why it matters:** Every service you build will run in a container. Understanding Docker deeply means you write better Dockerfiles, debug container issues without panic, and understand what "containerized" actually means at the OS level.

#### 📖 Theory
- **Linux primitives behind Docker:** namespaces (process isolation), cgroups (resource limits), union filesystems (image layers)
- **Image layers:** how Dockerfile instructions create layers, why layer order matters for cache
- **Image vs container:** a container is a running process with an isolated filesystem and network — not a VM
- **Container networking:** bridge networks, host networking, container-to-container DNS, port publishing
- **Volumes vs bind mounts:** volume lifecycle, when to use each, what happens when a container is deleted
- **Multi-stage builds:** separate build environment from runtime image — the difference between a 800MB and 30MB image
- **Entrypoint vs CMD:** what each does, when to use each, how they interact
- **Non-root containers:** why running as root in a container is a security problem

#### 📄 Technical Articles (Real-World)
- **"Containers from Scratch"** — Liz Rice (YouTube, GOTO 2018) — the definitive talk. She builds a container from scratch using Go syscalls. Transforms your understanding.
- **"How Docker Actually Works"** — Docker blog — namespaces and cgroups explained from the Docker perspective.
- **"Docker Image Layers and the Union File System"** — Docker docs + Earthly blog "How Docker Layers Work" — visual explanation of OverlayFS.
- **"Docker Best Practices for Python"** — Hynek Schlawack — production Dockerfile patterns for Python services. Applies to any language.
- **"Distroless Container Images"** — Google container tools blog — why Google strips the OS from production images and what the security benefit is.
- **"How We Reduced Our Docker Image Size by 90%"** — multiple engineering blogs — real case studies of Dockerfile optimization.

#### 📚 Book Anchor
- **Docker Deep Dive** — Nigel Poulton — short (200 pages), precise, practical. Read in 2 days.

#### 🛠️ Project: Dockerize an Existing Service Properly

Take the Task Management API from Level 1.1 and containerize it properly:

1. **v1 — Naive Dockerfile:** single stage, copies all files, runs as root. Build it.
2. **Measure:** how big is the image? (`docker image ls`)
3. **v2 — Multi-stage build:** stage 1 (builder) compiles/installs deps, stage 2 (runtime) only copies the binary and runtime deps
4. **v3 — Non-root user:** add `USER appuser` and create the user in the Dockerfile
5. **v4 — Optimized layer ordering:** COPY requirements.txt first, then `pip install`, then COPY the rest — so code changes don't invalidate the deps layer
6. **v5 — `.dockerignore`:** exclude `.git`, `__pycache__`, `*.pyc`, `node_modules`, test files
7. **Health check:** add `HEALTHCHECK` instruction
8. **Compare:** v1 image size vs v5 image size. Compare build time on second build (cache hit) vs cold build.

**Security audit:** Run `docker scout` or `trivy` on your final image. Fix any HIGH severity vulnerabilities.

---

### B.2 — Docker Compose & Container Networking

**Why it matters:** Real services don't run in isolation. Your API needs a database, a cache, a message broker, and a background worker. Docker Compose lets you define and run all of them together locally, in CI, and in small production deployments.

#### 📖 Theory
- **Docker Compose file anatomy:** services, networks, volumes, depends_on, healthchecks
- **Service dependencies:** `depends_on` with `condition: service_healthy` — wait for Postgres to actually be ready, not just started
- **Container networking:** by default, Compose creates a bridge network — services address each other by service name (the DNS is automatic)
- **Environment variables and secrets:** `.env` files, `env_file`, `secrets` — what's right for what context
- **Override files:** `docker-compose.override.yml` for local dev settings, `docker-compose.prod.yml` for production differences
- **Named volumes vs anonymous volumes:** persistence vs ephemeral data

#### 📄 Technical Articles (Real-World)
- **"Docker Compose in Production"** — Docker blog — patterns for using Compose in a real deployment.
- **"Compose File Version 3 Reference"** — Docker docs — read the full reference once. Know what every key does.
- **"Wait for It: Docker Health Checks"** — Uffizzi blog — how to use healthchecks to properly sequence service startup.
- **"Networking in Docker Compose"** — Docker docs — how service-to-service DNS works in Compose networks.

#### 🛠️ Project: Full Local Development Stack with Docker Compose

Create a `docker-compose.yml` that runs your full application stack:

**Services to include:**
- `api` — your FastAPI/Gin/Django service (built from local Dockerfile, hot-reload in dev)
- `postgres` — PostgreSQL with a named volume for data persistence
- `redis` — Redis for caching and session storage
- `rabbitmq` — RabbitMQ with management UI (`rabbitmq:3-management`)
- `worker` — your Celery/background worker (same image as `api`, different command)
- `pgadmin` — PostgreSQL admin UI (dev only)

**Requirements:**
1. `api` doesn't start until `postgres` passes its health check (`pg_isready`)
2. `worker` doesn't start until both `postgres` and `rabbitmq` are healthy
3. All services communicate on a private `backend` network — only `api` and `pgadmin` expose ports to the host
4. Environment variables loaded from `.env` file with sensible defaults
5. `docker-compose.override.yml` mounts source code for hot-reload in development
6. Running `docker compose up` from a fresh machine gives a fully working development environment in under 2 minutes

---

### B.3 — Kubernetes: Container Orchestration

**Why it matters:** Docker Compose is for one machine. Kubernetes is for running containers across a cluster of machines — with automatic scheduling, self-healing, rolling deployments, and service discovery. FAANG engineers are expected to understand Kubernetes concepts deeply, even if they're not managing the cluster themselves.

#### 📖 Theory

**Core concepts (understand before touching kubectl)**
- **Pod:** the smallest deployable unit — one or more tightly coupled containers with shared network and storage
- **Deployment:** manages a set of identical Pod replicas. Handles rollouts and rollbacks.
- **ReplicaSet:** ensures N copies of a Pod are always running — managed by Deployment
- **Service:** a stable network endpoint for a set of Pods. Pods die and are replaced; Service IP stays constant.
- **Ingress:** HTTP routing at L7 — routes external traffic to the correct Service based on hostname/path
- **ConfigMap:** key-value configuration data injected into Pods as env vars or mounted files
- **Secret:** same as ConfigMap but base64-encoded (not truly secret — that requires Vault or SOPS)
- **Namespace:** virtual cluster within a cluster — used for environment isolation (dev/staging/prod)

**Scheduling and resources**
- **Resource requests vs limits:** request = minimum guaranteed, limit = maximum allowed. Set both or your Pod gets OOM-killed.
- **Node affinity and anti-affinity:** schedule Pods on specific nodes or spread them across nodes
- **Taints and tolerations:** reserve nodes for specific workloads (e.g., GPU nodes for ML)

**Networking**
- **kube-proxy:** manages iptables rules that route Service traffic to healthy Pods
- **CoreDNS:** internal DNS server — `my-service.my-namespace.svc.cluster.local`
- **Network policies:** firewall rules for Pod-to-Pod communication — default is "allow all"
- **CNI plugins:** Flannel, Calico, Cilium — the network implementations behind the K8s networking model

**Storage**
- **PersistentVolume (PV) and PersistentVolumeClaim (PVC):** abstract storage from the specific provider
- **StorageClass:** dynamic volume provisioning — Postgres PVC on AWS auto-provisions an EBS volume

**Workload types**
- **Deployment:** stateless services. Pods are interchangeable.
- **StatefulSet:** stateful services. Pods have stable identities (pod-0, pod-1). Used for databases, Kafka, Zookeeper.
- **DaemonSet:** run one Pod per node — log collectors (Fluentd), monitoring agents (node-exporter)
- **Job / CronJob:** run-to-completion tasks and scheduled tasks

**Scaling**
- **Horizontal Pod Autoscaler (HPA):** scale number of Pod replicas based on CPU/memory/custom metrics
- **Vertical Pod Autoscaler (VPA):** automatically adjust resource requests/limits
- **Cluster Autoscaler:** add/remove nodes based on pending Pod scheduling needs

#### 📄 Technical Articles (Real-World)
- **"Kubernetes: Up and Running"** — Kelsey Hightower — the best K8s introduction, written by one of its creators. Start here.
- **"How Kubernetes Networking Works"** — Julia Evans (jvns.ca/blog) — the clearest explanation of K8s networking on the internet.
- **"Kubernetes Failure Stories"** — k8s.af — a collection of real Kubernetes production failures. Essential reading on what goes wrong and why.
- **"How Airbnb Migrated to Kubernetes"** — Airbnb Engineering — real migration story with scale numbers and lessons learned.
- **"Kubernetes at Datadog"** — Datadog Engineering — running K8s at massive scale.
- **"The Illustrated Children's Guide to Kubernetes"** — CNCF — the visual explanation that somehow works for adults too.
- **"OOMKilled: Debugging Kubernetes Memory Issues"** — multiple engineering blogs — one of the most common production issues explained.

#### 📚 Book Anchor
- **Kubernetes in Action** — Marko Lukša — the most thorough K8s book. Read Chapters 1–9 first, then reference as needed.

#### 🛠️ Project: Deploy the Full Stack to Kubernetes (Minikube/Kind)

Deploy everything from B.2 to a local Kubernetes cluster:

**Phase 1 — Basic deployment**
1. Write Kubernetes manifests (YAML) for: Deployment + Service for API, StatefulSet + Service for PostgreSQL, Deployment + Service for Redis
2. Use ConfigMap for non-secret configuration, Secret for database passwords
3. Add liveness and readiness probes to the API Deployment
4. `kubectl apply -f` and verify all Pods are running

**Phase 2 — Traffic and scaling**
5. Add an Ingress resource and install `ingress-nginx` — route `api.local/` to your API service
6. Configure HPA: scale API from 2→10 replicas when CPU > 60%
7. Run `k6` load test — watch `kubectl get pods` scale up in real time

**Phase 3 — Rolling deployments**
8. Update the API image tag in the Deployment. Run `kubectl rollout status` — watch zero-downtime rolling update
9. Force an error (deploy a broken image) — watch Kubernetes stop the rollout automatically
10. `kubectl rollout undo` — roll back to the previous working version

**Phase 4 — Helm**
11. Package all manifests into a Helm chart with configurable `values.yaml`
12. Deploy to a `staging` namespace and a `production` namespace using the same chart with different values

---

### B.4 — Message Queues: RabbitMQ, Celery, and Task Queues

**Why it matters:** You use Kafka for high-throughput event streaming. You use RabbitMQ (or Redis as a broker) for task queues — background jobs, email sending, PDF generation, webhook delivery. These are different tools for different problems. Knowing both, and knowing when to use each, separates senior engineers from juniors.

#### 📖 Theory

**RabbitMQ vs Kafka: the actual difference**
- **Kafka:** append-only log, message retention (consumers can re-read), high-throughput, ordered per partition, designed for stream processing and event sourcing
- **RabbitMQ:** traditional message broker, messages are deleted after acknowledgment, routing flexibility (exchanges and bindings), designed for task distribution and RPC patterns
- **Rule of thumb:** Kafka when you need message replay or high throughput. RabbitMQ when you need routing flexibility, complex topologies, or task queues.

**RabbitMQ concepts**
- **Producer → Exchange → Queue → Consumer:** messages always go through an exchange, not directly to a queue
- **Exchange types:** Direct (route by routing key), Topic (route by pattern), Fanout (broadcast to all bound queues), Headers (route by message attributes)
- **Acknowledgments:** `ack` (message processed), `nack` (message failed — requeue or discard), `reject`
- **Dead Letter Exchange (DLX):** messages that fail N times go to the DLX — for inspection, alerting, or manual reprocessing
- **Durable queues and persistent messages:** survive RabbitMQ restarts — necessary for any data you can't afford to lose
- **Prefetch count:** how many unacknowledged messages a consumer can hold — prevents one slow consumer from blocking the queue
- **Publisher confirms:** the producer waits for RabbitMQ to confirm it has persisted the message before moving on

**Celery (Python task queue)**
- A distributed task queue that uses a message broker (RabbitMQ, Redis) as its transport
- Tasks are Python functions decorated with `@app.task` and sent to a broker
- Workers consume tasks from the broker and execute them
- **Beat scheduler:** Celery Beat is a scheduler that sends periodic tasks (like cron)
- **Result backend:** optional storage for task results (Redis, database) — not needed if you only care about side effects
- **Retry logic:** `task.retry(exc=exc, countdown=60, max_retries=3)` with exponential backoff
- **Task signatures and chaining:** `chain`, `group`, `chord` — compose tasks into workflows

#### 📄 Technical Articles (Real-World)
- **"RabbitMQ Tutorials"** — rabbitmq.com/getstarted.html — the official tutorials (Work Queues, Publish/Subscribe, Routing, Topics, RPC). Do all 6.
- **"RabbitMQ vs Kafka"** — CloudAMQP blog — the most balanced technical comparison on the internet. Read this before choosing.
- **"Understanding AMQP: The Protocol RabbitMQ Speaks"** — CloudAMQP blog — understand what's happening at the protocol level.
- **"Celery Best Practices"** — Deni Bertović — the canonical list of Celery production mistakes and how to avoid them.
- **"Flower: Real-Time Celery Monitoring"** — Flower docs — monitoring your Celery workers in production.
- **"Background Tasks with Celery at Robinhood"** — Robinhood Engineering — real-world Celery at scale.
- **"Task Queue Architectures"** — Brandur Leach (Stripe) — thoughtful analysis of when async task queues are the right tool.

#### 📚 Book Anchor
- **DDIA Chapter 11** — "Stream Processing" — covers message delivery semantics relevant to both Kafka and RabbitMQ

#### 🛠️ Project: Async Job Processing System

Build a system that processes document uploads asynchronously:

**Architecture:**
- API receives PDF upload → stores in S3/MinIO → sends task to RabbitMQ → returns 202 Accepted with job ID
- Celery worker picks up task → extracts text from PDF → runs word count/sentiment analysis → stores result in Postgres → notifies via webhook
- API has GET `/jobs/{id}` endpoint to poll status

**Requirements:**
1. Use a dedicated RabbitMQ exchange with a `documents` routing key
2. Configure Dead Letter Exchange: failed tasks after 3 retries go to `documents.dlq` queue
3. Celery retry with exponential backoff: 30s, 60s, 120s between retries
4. Flower running on port 5555 for real-time monitoring
5. **Priority queue:** documents marked "urgent" go to a high-priority queue consumed first
6. **Rate limiting:** limit processing to 10 documents per minute per tenant (using Celery's rate_limit)
7. Add a `CronJob` (Celery Beat) that every hour: queries for stale "processing" jobs older than 30 minutes and re-enqueues them (handles worker crashes)

**Chaos test:** Kill a Celery worker mid-processing. Verify the task is requeued and processed by another worker (requires `acks_late=True`).

---

### B.5 — Redis: Beyond GET/SET

**Why it matters:** Most engineers use Redis as a simple key-value cache. Redis is actually a data structure server with sorted sets, streams, pub/sub, Lua scripting, and distributed locking — and each of these solves real production problems. Using Redis correctly is the difference between a caching layer that works and one that causes incidents.

#### 📖 Theory

**Redis Data Structures (and when to use each)**

*String (+ atomic counters)*
- GET/SET for simple caching, INCR/INCRBY for counters (rate limiting, view counts), SETNX for distributed locks
- GETSET for atomic read-and-replace

*List*
- Ordered list of strings. LPUSH/RPUSH add elements. LPOP/RPOP remove. BLPOP blocks until an element is available.
- Use for: simple task queues, recent activity logs, chat message history

*Hash*
- Map of field → value stored under a single key. HSET, HGET, HMGET, HGETALL.
- Use for: user session storage (one key per user, fields for each session attribute), object caching with partial update

*Set*
- Unordered collection of unique strings. SADD, SMEMBERS, SINTER, SUNION, SISMEMBER.
- Use for: unique visitor tracking, tags, friend lists, "items a user has seen"

*Sorted Set (ZSet)*
- Set where each member has a floating-point score. ZADD, ZRANGE, ZRANGEBYSCORE, ZRANK.
- Use for: leaderboards (score = points), rate limiter (score = timestamp), priority queues, autocomplete (lexicographic range queries)

*HyperLogLog*
- Probabilistic cardinality estimator — estimate "how many unique items" using constant memory
- PFADD, PFCOUNT. ~0.81% error rate. 12KB maximum memory regardless of cardinality.
- Use for: unique visitor counting (when exact count isn't required), A/B test user counting

*Pub/Sub*
- Publish messages to channels, subscribers receive them. PUBLISH, SUBSCRIBE, PSUBSCRIBE.
- **Important limitation:** no persistence — subscribers that are offline miss messages. Use Streams for guaranteed delivery.
- Use for: real-time notifications where losing a message is acceptable (WebSocket fanout, live dashboards)

*Streams (Redis 5.0+)*
- Persistent append-only log with consumer groups. Similar to Kafka but simpler.
- XADD, XREAD, XREADGROUP, XACK.
- Use for: audit logs, event sourcing at small scale, guaranteed-delivery pub/sub

**Patterns**
- **Cache-aside:** app checks Redis first, on miss reads from DB and writes to Redis
- **Write-through:** every DB write also writes to Redis (stronger consistency, more write overhead)
- **Distributed lock (Redlock):** SETNX + EXPIRE for simple cases, the Redlock algorithm for HA deployments
- **Session store:** store JWT refresh tokens or session data with TTL
- **Rate limiting:** sorted set with timestamp scores for sliding window, or INCR + EXPIRE for fixed window

**Redis Cluster and Replication**
- Single Redis: simple, fast, single point of failure
- Redis Sentinel: HA — automatic failover when master dies, no horizontal scaling
- Redis Cluster: horizontal sharding across N nodes, each owns a range of hash slots (0–16383)
- **Cluster limitation:** all keys in a multi-key operation must be in the same slot (use hash tags `{user:1}:session` to force co-location)

**Persistence options**
- **RDB (snapshot):** periodic snapshot to disk. Fast restart, but you can lose data between snapshots.
- **AOF (Append Only File):** log every write operation. Slower restart, minimal data loss.
- **AOF + RDB:** best of both — use AOF for durability, RDB for fast restarts

#### 📄 Technical Articles (Real-World)
- **"Redis Data Types and Abstractions"** — Redis official docs — read the introduction to every data type.
- **"Redis as a Primary Database"** — Redis blog — when Redis can replace a traditional database.
- **"Distributed Locks with Redis"** — Martin Kleppmann vs Antirez debate — a crucial read on the limits of Redis distributed locking (the Redlock algorithm). Read both sides.
- **"Scaling Memcache at Facebook"** — USENIX 2013 — lessons that apply directly to Redis at scale.
- **"How Slack Uses Redis"** — Slack Engineering — real-world Sorted Set usage for their notification system.
- **"Rate Limiting with Redis"** — Redis blog — all common rate limiting patterns implemented in Redis.
- **"Redis Cluster Specification"** — Redis official docs — how hash slots, cluster topology, and failover work.

#### 🛠️ Project: Redis-Powered Feature Set

Build a complete Redis-backed feature layer for an existing API:

1. **Caching with TTL:** cache all `GET /users/{id}` responses with 60s TTL. Invalidate on `PUT /users/{id}`. Measure latency before/after.
2. **Leaderboard:** `GET /leaderboard` returns top 10 users by score. Use ZSet. `POST /users/{id}/score` increments score atomically.
3. **Rate limiting (sliding window):** limit each user to 100 requests per minute using ZSet + timestamp scores + Lua script (atomic eval).
4. **Distributed lock:** `POST /payments` acquires a per-user distributed lock to prevent double-charge race condition. Use SETNX + EXPIRE + unique token for safe release.
5. **Pub/Sub → WebSocket fanout:** on order status change, PUBLISH to `orders:{id}` channel. WebSocket server subscribes and pushes to connected clients.
6. **HyperLogLog:** track unique daily active users per feature flag using PFADD. Count without storing every user ID.
7. **Redis Streams audit log:** every API mutation (POST/PUT/DELETE) writes to a Redis Stream `audit:events`. A separate consumer group reads and persists to PostgreSQL asynchronously.

**Cluster exercise:** Set up Redis Cluster with 3 masters and 3 replicas. Verify hash slot distribution. Use hash tags to force related keys to the same slot. Kill one master — verify Sentinel promotes a replica automatically.

---

### B.6 — CI/CD Pipelines and Infrastructure as Code

**Why it matters:** Code that isn't deployed is worthless. Engineers who can ship their code reliably — with automated testing, security scanning, and zero-downtime deployments — are dramatically more effective than those who wait for a DevOps team.

#### 📖 Theory

**CI/CD Concepts**
- **Continuous Integration (CI):** every commit triggers an automated pipeline — build, lint, test, scan
- **Continuous Delivery (CD):** the artifact from CI can be deployed to production at any time with a button press
- **Continuous Deployment:** every successful CI run automatically deploys to production — no human gate
- **Pipeline stages:** source → build → test (unit) → test (integration) → security scan → build image → push image → deploy staging → smoke test → deploy production → notify

**GitHub Actions / GitLab CI concepts**
- **Workflow / Pipeline:** defined in YAML, triggered by events (push, PR, schedule, tag)
- **Jobs:** units of work within a workflow, run in parallel or in sequence
- **Steps:** individual commands within a job
- **Runners:** the machines that execute jobs — hosted (GitHub/GitLab provides), self-hosted (your own machines)
- **Artifacts:** files produced by one job and consumed by another (compiled binary, test report, Docker image)
- **Caching:** cache `node_modules`, `pip` packages, Go module cache — make pipelines fast
- **Secrets:** environment variables injected into jobs without appearing in logs
- **Environments and approvals:** staging deploys automatically, production requires a manual approval gate

**Deployment strategies**
- **Rolling update:** replace pods one by one — zero downtime, but two versions run simultaneously
- **Blue/Green:** spin up a completely new environment, then switch traffic — instant rollback capability, expensive
- **Canary:** send 5% of traffic to new version, gradually increase — needs sophisticated traffic splitting
- **Feature flags:** deploy code but keep it off until explicitly enabled — decouples deploy from release

**Infrastructure as Code (IaC)**
- **Why IaC:** infrastructure defined in code is version-controlled, reviewable, reproducible, and auditable
- **Terraform:** declarative IaC that works across cloud providers — define desired state, Terraform figures out the plan
- **Pulumi:** IaC using real programming languages (Python, Go, TypeScript) instead of HCL
- **AWS CDK:** define AWS infrastructure in Python/TypeScript, compiled to CloudFormation

#### 📄 Technical Articles (Real-World)
- **"CI/CD at GitHub"** — GitHub Engineering — how GitHub runs its own CI/CD using GitHub Actions at massive scale.
- **"Deployment Pipeline Best Practices"** — Continuous Delivery Foundation — the canonical guide.
- **"Blue-Green Deployments"** — Martin Fowler — the definitive explanation of blue-green.
- **"Canary Deployments"** — Google SRE Book Chapter 16 — how Google releases software to production.
- **"Terraform: Up and Running"** — Yevgeniy Brikman — the best Terraform book. Read Chapters 1–4 for fundamentals.
- **"How Netflix Deploys Code"** — Netflix TechBlog — Spinnaker, the deployment platform they open-sourced.
- **"GitOps: What You Need to Know"** — Weaveworks — how Argo CD and Flux manage Kubernetes deployments from Git.

#### 🛠️ Project: Full CI/CD Pipeline for Your Kubernetes Service

Build a complete pipeline from commit to production for the Kubernetes service from B.3:

**GitHub Actions workflow:**
1. **Lint stage:** run `golangci-lint` or `flake8` + `black` — fail on any lint error
2. **Unit test stage:** run tests, upload coverage report to Codecov
3. **Integration test stage:** spin up `docker-compose` with test DB, run integration tests
4. **Security scan stage:** run `trivy` on the built Docker image — fail on HIGH/CRITICAL CVEs
5. **Build and push stage:** build multi-arch Docker image (`linux/amd64`, `linux/arm64`), push to GHCR with commit SHA tag
6. **Deploy staging stage:** `kubectl set image deployment/api api=ghcr.io/you/api:$SHA` — runs on every push to `main`
7. **Smoke test stage:** hit `/health` and `/ready` on staging — fail if not 200
8. **Deploy production stage:** runs only on tagged releases (`v*.*.*`). Requires manual approval in GitHub Environments.
9. **Notify stage:** post deployment status to Slack

**Infrastructure as Code:**
- Define the Kubernetes namespace, RBAC roles, and resource quotas using Terraform (or Pulumi)
- Store Terraform state in S3 (or Terraform Cloud)
- The pipeline runs `terraform plan` on every PR and `terraform apply` on merge to main

---

## ⚡ Level 3: Distributed Systems Core (Weeks 8–16)

> **Goal:** This is the hardest level. After this level, you'll understand things that most "senior engineers" don't.

> **Prerequisite:** Complete Level 2 first.

> **BFS Note:** 3.1 and 3.2 are conceptually parallel. 3.3 (consensus) depends on 3.1. 3.4 (Kafka) is independent. 3.5 (clocks) can be read anytime.

---

### 3.1 — The Core Problems of Distributed Systems

#### 📖 Theory
- The **Fallacies of Distributed Computing** — eight assumptions that are wrong
- **Partial failures:** a node can be running but not responding
- **Unreliable networks:** packets get lost, duplicated, reordered, arbitrarily delayed
- **Unreliable clocks:** NTP is imprecise. Wall-clock time cannot order events across machines.
- **The Two Generals Problem:** proof that perfect communication over unreliable links is impossible
- **Byzantine faults:** what happens when nodes lie

#### 📄 Technical Articles (Real-World)
- **"Fallacies of Distributed Computing"** — Arnon Rotem-Gal-Oz
- **"Notes on Distributed Systems for Young Bloods"** — Jeff Hodges — required reading
- **"An Introduction to Distributed Systems"** — Kyle Kingsbury (aphyr)
- **"How AWS Builds Highly Available Systems"** — Werner Vogels (allthingsdistributed.com)
- **"Chaos Engineering: Building Confidence in System Behavior"** — Netflix TechBlog

#### 📚 Book Anchor
- **DDIA Chapter 8** — "The Trouble with Distributed Systems"

---

### 3.2 — MIT 6.824 Distributed Systems Course (Labs)

> This is the most valuable project on this entire roadmap. Budget 2–3 weeks.

**Lab 1: MapReduce** — Implement the MapReduce framework in Go, fault-tolerant workers

**Lab 2: Key/Value Server** — Implement a KV server with at-least-once RPC semantics

**Lab 3: Raft Consensus** — Implement the full Raft algorithm: leader election, log replication, persistence, log compaction

**Lab 4: Fault-Tolerant Key/Value Service** — Build replicated KV on top of your Raft implementation

**Lab 5: Sharded Key/Value Service** — Shard KV across multiple Raft groups with reconfiguration

---

### 3.3 — Consensus, Replication, and Consistency

#### 📖 Theory
- **Consensus problem:** why getting N machines to agree on a single value is hard
- **Paxos:** the original consensus algorithm
- **Raft:** leader election, log replication, safety invariants
- **Consistency models:** linearizability → sequential consistency → eventual consistency
- **Linearizability:** what it means for reads to "see the latest write"
- **Vector clocks and Lamport timestamps**

#### 📄 Technical Articles (Real-World)
- **"Paxos Made Simple"** — Leslie Lamport (2001)
- **"Raft: In Search of an Understandable Consensus Algorithm"** — Ongaro & Ousterhout
- **"Strong consistency models"** — Kyle Kingsbury (aphyr)
- **"How CockroachDB Does Distributed Transactions"** — CockroachDB blog
- **"Eventual Consistency is Not What You Think"** — Martin Kleppmann's blog

#### 📚 Book Anchor
- **DDIA Chapter 9** — "Consistency and Consensus"

---

### 3.4 — Apache Kafka and Event-Driven Architecture

#### 📖 Theory
- **The Log** as the fundamental abstraction
- Kafka architecture: topics, partitions, offsets, consumer groups, brokers, KRaft
- **Consumer groups:** how Kafka enables parallel consumption without duplication
- **Delivery semantics:** at-most-once, at-least-once, exactly-once
- **Log compaction:** Kafka keeps only the latest value per key
- **Change Data Capture (CDC):** capture every database mutation as a Kafka event

#### 📄 Technical Articles (Real-World)
- **"The Log: What every software engineer should know about real-time data"** — Jay Kreps (LinkedIn)
- **"Exactly-Once Semantics in Apache Kafka"** — Confluent Engineering blog
- **"Kafka at Scale: How LinkedIn Uses Kafka"** — LinkedIn Engineering
- **"How Uber Uses Apache Kafka for Real-Time Passenger and Driver Matching"** — Uber Engineering
- **"Building Real-time Data Pipelines with Kafka CDC"** — Debezium blog

#### 📚 Book Anchor
- **DDIA Chapter 11** — "Stream Processing"

#### 🛠️ Project: Event-Driven Order Processing System
Build an order system with Kafka as the backbone — OrderService, InventoryService, PaymentService, NotificationService — with Dead Letter Queue, exactly-once semantics, and Saga pattern.

---

### 3.5 — Distributed Clocks and Time

#### 📖 Theory
- **Why wall clocks fail:** NTP adjustments, clock skew, leap seconds
- **Lamport timestamps:** logical clocks that track causality
- **Vector clocks:** track causal relationships between N nodes
- **Google's TrueTime:** atomic clocks + GPS, uncertainty bounds
- **Hybrid Logical Clocks (HLC):** used by CockroachDB

#### 📄 Technical Articles (Real-World)
- **"Time, Clocks, and the Ordering of Events in a Distributed System"** — Leslie Lamport (1978)
- **"Spanner, TrueTime and the CAP Theorem"** — Google Cloud blog
- **"How CockroachDB Uses Hybrid-Logical Clocks"** — CockroachDB Engineering

---

## ⚡ Level 4: Infrastructure, Scalability & Reliability (Weeks 10–18)

> **BFS Note:** This entire level is **parallel with Level 3**.

---

### 4.1 — Load Balancing & Proxies

#### 📖 Theory
- L4 vs L7 load balancing — when each matters
- Algorithms: round-robin, least connections, IP hash, consistent hashing
- Health checks: active vs passive
- Connection draining: why you need it for zero-downtime deploys
- Reverse proxies vs API gateways: nginx vs HAProxy vs AWS ALB vs Envoy

#### 📄 Technical Articles (Real-World)
- **"The Load Balancing Problem"** — HAProxy.com blog
- **"Netflix's Load Balancer: Ribbon"** — Netflix TechBlog — client-side load balancing
- **"How AWS Elastic Load Balancing Distributes Traffic"** — AWS Architecture blog
- **"Inside NGINX: How We Designed for Performance & Scale"** — NGINX blog

#### 🛠️ Project: Multi-Node Load Balanced Service
Deploy 3 instances behind Nginx with weighted round-robin. Implement health checks. Test connection draining during a rolling deploy.

---

### 4.2 — Caching: Every Layer

#### 📖 Theory
- **Caching strategies:** cache-aside, read-through, write-through, write-behind
- **Eviction policies:** LRU, LFU, FIFO, TTL
- **Cache invalidation:** tag-based, event-driven
- **Cache stampede / thundering herd:** probabilistic early expiration, request coalescing
- **Distributed caching:** Redis Cluster, Memcached
- **CDN caching:** edge caches, cache-control headers, purging

#### 📄 Technical Articles (Real-World)
- **"TAO: Facebook's Distributed Data Store for the Social Graph"** — USENIX 2013
- **"Scaling Memcache at Facebook"** — USENIX 2013
- **"How Cloudflare Runs Its Global CDN"** — Cloudflare Blog
- **"Cache Stampede and Probabilistic Early Expiration"** — research paper

#### 🛠️ Project: Multi-Layer Caching System
In-process L1 LRU cache + Redis L2 with TTL + thundering herd protection (Redis SETNX) + metrics tracking hit/miss/eviction rate per layer.

---

### 4.3 — Rate Limiting and Throttling

#### 📖 Theory
- Algorithms: token bucket, leaky bucket, fixed window, sliding window log, sliding window counter
- Distributed rate limiting: Redis for shared counters
- Rate limiting by: IP, user, API key, tenant

#### 📄 Technical Articles (Real-World)
- **"Scaling Your API with Rate Limiters"** — Stripe Engineering blog
- **"An Alternative Approach to Rate Limiting"** — Figma Engineering
- **"How Cloudflare Built Rate Limiting Capable of Scaling to Millions of Domains"** — Cloudflare blog
- **"Envoy's Rate Limiting Service"** — Envoy Proxy docs

#### 🛠️ Project: Rate Limiting Library
Implement all 5 algorithms. Implement distributed token bucket using Redis atomic Lua scripts. Benchmark all five under concurrent load.

---

### 4.4 — Service Reliability: SLOs, Retries, Circuit Breakers

#### 📖 Theory
- **SLIs / SLOs / SLAs:** error budgets, how Google defines them
- **Retry strategies:** exponential backoff with jitter
- **Circuit breakers:** open/half-open/closed states
- **Timeouts:** the most important reliability tool — every network call needs one
- **Bulkhead pattern:** isolating failures
- **Graceful degradation:** returning stale/partial data instead of errors

#### 📄 Technical Articles (Real-World)
- **"Exponential Backoff and Jitter"** — AWS Architecture Blog
- **"Circuit Breaker Pattern"** — Martin Fowler
- **"Hystrix: Latency and Fault Tolerance for Distributed Systems"** — Netflix TechBlog
- **"Site Reliability Engineering"** — Google SRE Book — Chapters 3, 4, and 13
- **"Chaos Engineering at Netflix"** — Chaos Monkey, Chaos Kong

#### 🛠️ Project: Resilient HTTP Client
Timeout (connection + read separately), retry with exponential backoff + full jitter, circuit breaker, bulkhead (separate goroutine pools per dependency). Test against a dependency that randomly fails.

---

### 4.5 — Observability: Metrics, Logs, Traces

#### 📖 Theory
- **The three pillars:** Metrics, Logs, Traces
- **Metrics:** counters, gauges, histograms. Why p99 > average.
- **Structured logging:** JSON logs, correlation IDs
- **Distributed tracing:** spans, trace context propagation, sampling
- **RED Method:** Rate, Error rate, Duration
- **USE Method:** Utilization, Saturation, Errors
- **OpenTelemetry:** the standard for all three pillars

#### 📄 Technical Articles (Real-World)
- **"Observability vs Monitoring"** — Charity Majors (Honeycomb)
- **"Distributed Tracing at Uber Scale"** — Uber Engineering blog (Jaeger)
- **"Google SRE Book: Chapter 6 — Monitoring Distributed Systems"**
- **"How Netflix Monitors its Cloud"** — Netflix TechBlog

#### 🛠️ Project: Full Observability Stack
Prometheus + Grafana + Jaeger on any existing service. RED metrics dashboard. Distributed traces across 3 services. Alertmanager rule for p99 latency.

---

## ⚡ Level 5: Advanced Architecture Patterns (Weeks 15–22)

> **Prerequisite:** Level 3 and Level 4 must be solid before this.

---

### 5.1 — Microservices: The Real Architecture, Not the Hype

#### 📖 Theory
- **Service decomposition:** bounded contexts (DDD), business capabilities
- **Data ownership:** each service owns its data — non-negotiable
- **Synchronous vs asynchronous inter-service communication**
- **Distributed transactions:** why two-phase commit is a trap, why sagas exist
- **Service mesh:** Envoy/Istio — traffic management, mTLS
- **API gateway vs BFF**

#### 📄 Technical Articles (Real-World)
- **"Pattern: Microservice Architecture"** — Martin Fowler & James Lewis
- **"The Majestic Monolith"** — DHH (Basecamp) — the counterargument
- **"How Netflix Migrated to Microservices"** — Netflix TechBlog
- **"Service Mesh at Lyft with Envoy"** — Lyft Engineering

#### 🛠️ Project: Decompose a Monolith
UserService, TaskService, NotificationService, AuthService — each with its own database. gRPC for sync, Kafka for async. Saga pattern. API Gateway routing. Service discovery.

---

### 5.2 — Event Sourcing and CQRS

#### 📖 Theory
- **Event sourcing:** events as source of truth, projections, event replay
- **CQRS:** command model vs query model — separate optimized stores
- **Event store:** append-only log of domain events
- **Eventual consistency in CQRS**
- **Snapshotting:** avoid replaying 10M events

#### 📄 Technical Articles (Real-World)
- **"Event Sourcing"** — Martin Fowler
- **"CQRS Documents"** — Greg Young
- **"Event Sourcing at Airbnb"** — Airbnb Engineering
- **"Building a Secure Money Transfer Service"** — Monzo Engineering

#### 🛠️ Project: Bank Ledger with Event Sourcing
Write side (commands → events), read side (projections), event replay from scratch, snapshotting.

---

### 5.3 — API Design at Scale: Versioning and Backward Compatibility

#### 📖 Theory
- API versioning strategies: URL, header, content negotiation
- **Backward compatibility rules:** breaking vs non-breaking changes
- **Tolerant reader pattern**
- **API deprecation** without breaking clients
- **Contract testing:** Pact — consumer-driven contract tests

#### 📄 Technical Articles (Real-World)
- **"How Stripe Maintains API Backward Compatibility"** — Stripe Engineering
- **"API Versioning Has No 'Right Way'"** — Troy Hunt
- **"Evolving APIs at Spotify"** — Spotify Engineering

---

### 5.4 — Distributed Tracing and Service Mesh

#### 📖 Theory
- Trace context propagation: W3C Trace Context standard
- Sampling: tail-based vs head-based
- Service mesh: sidecar proxy pattern, Envoy, Istio, Linkerd
- mTLS: mutual TLS between services

#### 📄 Technical Articles (Real-World)
- **"Distributed Tracing at Uber with Jaeger"** — Uber Engineering
- **"OpenTelemetry: The New Standard for Observability"** — CNCF blog
- **"The Service Mesh: What Every Software Engineer Needs to Know"** — William Morgan
- **"How Lyft Uses Envoy as a Service Mesh"** — Lyft Engineering

#### 🛠️ Project: Full Service Mesh with Observability
Kubernetes + Istio + automatic mTLS + traffic splitting + Jaeger distributed tracing + Kiali dependency graph.

---

### 5.5 — Security Architecture for Backend Systems

#### 📖 Theory
- **Authentication vs Authorization**
- **JWT:** structure, signing algorithms, expiry, refresh tokens, and why they can't be easily revoked
- **OAuth 2.0 / OpenID Connect:** the flows, when to use which grant type
- **API Security:** input validation, SQL injection, SSRF
- **Zero trust:** why network perimeter fails in microservices
- **Secrets management:** Vault, AWS Secrets Manager

#### 📄 Technical Articles (Real-World)
- **"JSON Web Token Best Current Practices"** — IETF RFC 8725
- **"OAuth 2.0 Security Best Current Practice"** — Aaron Parecki
- **"How Uber Manages Identity and Access"** — Uber Engineering
- **"Stop Using JWT for Sessions"** — joepie91.codes

#### 🛠️ Project: Production-Ready Auth Service
Registration + bcrypt, JWT access (15min) + refresh token (30 days) with rotation, session revocation via Redis, OAuth 2.0 Google flow, rate limiting on auth endpoints, secrets in Vault.

---

## ⚡ Level 6: System Design Mastery (Weeks 18–26)

> **Goal:** Apply every concept from Levels 0–5 and A–B to design complete systems.

---

### 6.1 — The System Design Interview Framework

#### The 45-Minute Structure
1. **Clarify requirements (5 min):** Functional + Non-functional (scale, latency, consistency)
2. **Back-of-envelope estimation (5 min):** QPS, storage, bandwidth
3. **High-level design (10 min):** Core components, data flow, API contract
4. **Data model (5 min):** Schema, which database, why
5. **Deep dive (15 min):** Interviewer picks 1–2 components — go deep on tradeoffs
6. **Wrap up (5 min):** Bottlenecks, monitoring, potential improvements

#### What Interviewers Actually Listen For
- Do you ask good questions?
- Do you mention what you're optimizing for? (Read-heavy? Write-heavy? Latency? Consistency?)
- Do you justify tradeoffs? ("I chose Cassandra because X, but it means Y")
- Do you know failure modes?
- Do you go deep when asked?

---

### 6.2 — Canonical Design Problems (Build and Document Each)

**Design 1: URL Shortener (Bitly)** — Hashing, database choice, caching, analytics

**Design 2: Distributed Message Queue (Kafka-like)** — Log structure, partitioning, consumer groups

**Design 3: Rate Limiter (API Gateway Level)** — Distributed counters, sliding window, Redis

**Design 4: Twitter/X Feed** — Fan-out on write vs read, celebrity problem, denormalization

**Design 5: Distributed Cache (Redis-like)** — Consistent hashing, eviction, replication

**Design 6: Web Crawler** — Distributed coordination, URL deduplication, politeness

**Design 7: Notification System** — Fan-out, delivery guarantees, multi-channel, priority queues

**Design 8: Distributed File Storage (S3-like)** — Object storage, consistency, erasure coding

**Design 9: Search Autocomplete** — Trie data structure, distributed trie, aggregation

**Design 10: Ride-Sharing Location Service** — Geospatial indexing, real-time updates, dispatch

**Design 11: Video Upload and Streaming (YouTube)** — Object storage, transcoding pipeline, CDN, adaptive bitrate

**Design 12: Distributed Transaction (Cross-Service Payment)** — 2PC vs Saga, transactional outbox, idempotency

**Design 13: Container Orchestration Platform (Kubernetes-like)** — Scheduler, controller loop, distributed state (etcd), pod lifecycle, service discovery. How does the control plane actually work?

**Design 14: CI/CD Pipeline System (GitHub Actions-like)** — Job scheduling, artifact storage, runner fleet management, queue isolation, secret injection

---

### 6.3 — Reading the Engineering Papers That Built the Industry

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
| Large-scale cluster management at Google with Borg | Kubernetes | 2015 |
| The Dapper paper — Large-Scale Distributed Systems Tracing | Jaeger, Zipkin | 2010 |

---

### 6.4 — The Must-Follow Engineering Blogs

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

## 📅 The Parallel Reading Plan (DDIA + New Books)

**DDIA (Weeks 1–24):**

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

**Clean Architecture + GoF (Weeks 4–12, Level A):**

| Week | Book | Chapter |
|---|---|---|
| 4–5 | Clean Architecture | Part III — SOLID Principles |
| 5–6 | GoF / Refactoring.Guru | Creational patterns |
| 6–7 | GoF / Refactoring.Guru | Structural patterns |
| 7–8 | GoF / Refactoring.Guru | Behavioral patterns |
| 8–9 | Clean Architecture | Part IV — Component Principles |
| 9–10 | Architecture Patterns with Python | Ch. 1–6 (Repository, Service Layer, Events) |
| 10–12 | DDD Quickly (InfoQ free PDF) | Full |

**Software Architecture: The Hard Parts (Weeks 25–32):**

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
| Weeks 3–8 | Level 1 | APIs, protocols, WebSockets |
| Weeks 4–10 | Level 2 | Databases deep cut |
| Weeks 4–10 | **Level A** | **Software design patterns, DDD, concurrency patterns** |
| Weeks 6–14 | **Level B** | **Docker, Kubernetes, RabbitMQ, Redis ops, CI/CD** |
| Weeks 8–16 | Level 3 | Distributed systems core |
| Weeks 10–18 | Level 4 | Infrastructure, caching, reliability |
| Weeks 15–22 | Level 5 | Advanced architecture patterns |
| Weeks 18–26 | Level 6 | System design mastery |

**Total: 26–32 weeks at 2 hours/day.**
**Or: 14–18 months at 1 hour/day.**

---

## ✅ Project Portfolio Checklist — v2

By the end of this roadmap, you should have built:

**Level 0 — Fundamentals**
- [ ] Cache performance benchmark (memory hierarchy)
- [ ] Raw HTTP server + non-blocking I/O version
- [ ] TCP chat server from raw sockets + TLS
- [ ] Linux production diagnostics exercise

**Level 1 — APIs**
- [ ] Production-quality REST API (Task Manager) — idempotency, pagination, rate limiting, OpenAPI
- [ ] gRPC microservice (multi-language client)
- [ ] Real-time collaborative whiteboard (WebSockets + Redis pub/sub)
- [ ] GraphQL API with DataLoader (N+1 solved)

**Level A — Design Patterns**
- [ ] SOLID refactoring exercise (5-step violation → clean code transformation)
- [ ] Payment processing system using 6 GoF patterns deliberately (Strategy, Factory, Decorator, Command, Observer, State)
- [ ] Pattern recognition exercise in a large open-source project
- [ ] Task Manager API rebuilt with clean architecture (Ports + Adapters + Repository + Service Layer)
- [ ] E-commerce bounded context implementation (Aggregate, ValueObject, DomainEvent, ACL)
- [ ] Concurrent image processing service (worker pool + fan-out/fan-in + semaphore + context cancellation)

**Level 2 — Databases**
- [ ] Key-value store with WAL, compaction, and Bloom filter (Bitcask style)
- [ ] PostgreSQL performance workshop (10M rows, EXPLAIN, indexes, PgBouncer, partitioning)
- [ ] Social feed with multi-backend storage (PG + Redis + Cassandra)
- [ ] Transaction bug hunting exercise (lost updates, write skew, phantom reads)
- [ ] Postgres replication setup + failure simulation + replica promotion

**Level B — DevOps Tooling**
- [ ] Properly Dockerized service (multi-stage, non-root, optimized layers, health check)
- [ ] Full Docker Compose stack (API + Postgres + Redis + RabbitMQ + Worker + PGAdmin)
- [ ] Full Kubernetes deployment (Deployments, Services, Ingress, ConfigMaps, Secrets, HPA, Helm chart)
- [ ] Async job processing system (RabbitMQ + Celery + DLX + Flower + priority queues + CronJob)
- [ ] Redis feature set (caching, leaderboard, rate limiting, distributed lock, pub/sub, HyperLogLog, Streams)
- [ ] Full CI/CD pipeline (lint → test → security scan → build → push → deploy staging → approve → deploy prod → notify)

**Level 3 — Distributed Systems**
- [ ] MIT 6.824 Labs 1–5 (Raft implementation — the crown jewel)
- [ ] Kafka-based event-driven order system (saga + DLQ + exactly-once)

**Level 4 — Infrastructure**
- [ ] Multi-node load balanced service with health checks
- [ ] Multi-layer caching system with stampede protection
- [ ] Rate limiting library (all 5 algorithms benchmarked, distributed Redis version)
- [ ] Resilient HTTP client (retry + circuit breaker + bulkhead + context cancellation)
- [ ] Full observability stack (Prometheus + Grafana + Jaeger)

**Level 5 — Architecture**
- [ ] Microservices decomposition (3+ services + Kafka + API gateway + Saga)
- [ ] Bank ledger with event sourcing + projections + snapshotting
- [ ] AuthService with JWT, refresh tokens, revocation, OAuth 2.0
- [ ] Service mesh with Istio, mTLS, traffic splitting, distributed tracing

**Level 6 — System Design**
- [ ] 14 canonical system design documents with tradeoff analysis

---

## 🎯 The FAANG Interview Readiness Checklist — v2

You're ready when you can:

**Distributed Systems**
- [ ] Explain any of the 12 seminal papers without looking them up
- [ ] Explain Raft leader election in detail — and what happens when the network partitions
- [ ] Explain MVCC and why it enables reads without blocking writes
- [ ] Describe exactly what happens when a Kafka consumer crashes mid-processing
- [ ] Name the difference between linearizability and sequential consistency with examples

**System Design**
- [ ] Design any of the 14 canonical systems in 45 minutes with clear tradeoff justifications
- [ ] Answer "why did you choose X over Y?" for every technology decision
- [ ] Name 3 real-world failure modes for every architectural pattern you propose
- [ ] Quote real numbers: latency targets, QPS estimates, storage calculations
- [ ] Implement a basic consistent hash ring from scratch

**Code Architecture**
- [ ] Identify any GoF pattern in production code immediately on sight
- [ ] Refactor a service that violates SOLID into clean architecture without changing its behavior
- [ ] Define bounded context boundaries for any domain you're given
- [ ] Write concurrent code with zero data races (verified by race detector)
- [ ] Explain the difference between optimistic and pessimistic locking and when to use each

**DevOps & Infrastructure**
- [ ] Write a production-quality Dockerfile from memory (multi-stage, non-root, optimized layers)
- [ ] Explain what happens inside Kubernetes when you run `kubectl apply` — from API server to pod running
- [ ] Configure a Celery task with retry logic, DLX, and monitoring from scratch
- [ ] Explain the difference between RabbitMQ and Kafka at the architectural level — and when to use each
- [ ] Design a CI/CD pipeline for a microservice from scratch — what stages, what gates, what rollback strategy

---

*This roadmap is comprehensive but not exhaustive — distributed systems and software architecture are lifetimes of learning. The goal is to build the mental models that let you learn anything new quickly, not to memorize every technology.*
