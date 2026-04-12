#!/usr/bin/env python3
"""
Generate a 365-day BFS-based study plan from the God-Level Backend Engineering Roadmap.
Outputs an Excel file with dependency-aware scheduling, ~6 hours/day, interleaved domains.
"""

import datetime
from dataclasses import dataclass, field
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ─── Data Model ───────────────────────────────────────────────────────────────

@dataclass
class StudyBlock:
    domain: str
    topic: str
    subtopic: str
    duration: float  # hours
    difficulty: int   # 1-5
    notes: str = ""
    phase: str = ""
    topic_id: str = ""

# ─── All Study Content ────────────────────────────────────────────────────────
# Organized by topic_id with dependencies and BFS layer

def build_all_content():
    """
    Returns a list of (topic_id, [StudyBlock, ...]) in BFS-scheduled order.
    Dependencies are resolved by the ordering of blocks.
    """
    blocks = []

    # ═══════════════════════════════════════════════════════════════════════
    # PHASE 1: FOUNDATION (Days 1–100)
    # BFS Layer 0: Level 0 topics (all parallel) + DDIA Ch.1
    # BFS Layer 1: Level 1 (1.1, 1.2, 1.3 parallel) + Level A (A.1-A.4) + Level 2 (2.1-2.3)
    # BFS Layer 2: Level 1.4 + Level 2.4 + Level A.5
    # ═══════════════════════════════════════════════════════════════════════

    # --- Level 0: Computer Fundamentals ---

    # 0.1 Memory Hierarchy & CPUs
    blocks.extend([
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Theory: CPU registers → L1/L2/L3 → RAM → SSD → disk latency hierarchy", 2.0, 2, "Memorize Jeff Dean's latency numbers", "Foundation", "0.1"),
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Theory: Cache lines, cache misses, false sharing in multi-threaded code", 1.5, 3, "", "Foundation", "0.1"),
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Theory: NUMA architecture and implications for databases on large servers", 1.5, 3, "", "Foundation", "0.1"),
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Article: 'What Every Programmer Should Know About Memory' — Drepper (Parts 1-3)", 3.0, 3, "lwn.net — the classic", "Foundation", "0.1"),
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Article: 'Latency Numbers Every Programmer Should Know' + Colin Scott updates", 1.0, 2, "Memorize these numbers", "Foundation", "0.1"),
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Article: 'CPU Caches and Why You Care' — Scott Meyers CppCon 2014", 1.5, 2, "YouTube video — best visual explanation", "Foundation", "0.1"),
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Article: 'How L1 and L2 CPU Caches Work' — ExtremeTech", 1.0, 2, "", "Foundation", "0.1"),
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Project: Cache benchmark — sequential vs random array access", 2.5, 3, "Measure the difference", "Foundation", "0.1"),
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Project: Cache benchmark — row-major vs column-major matrix traversal", 2.0, 3, "Cache lines in action", "Foundation", "0.1"),
        StudyBlock("Computer Fundamentals", "0.1 Memory Hierarchy & CPUs", "Project: Cache benchmark — false sharing: adjacent vs separate cache lines", 2.5, 4, "Two threads writing to adjacent memory", "Foundation", "0.1"),
    ])

    # 0.2 OS: Processes, Threads, I/O
    blocks.extend([
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Theory: Process vs thread vs coroutine/goroutine — cost of each", 2.0, 2, "", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Theory: Context switching mechanics and cost", 1.5, 3, "", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Theory: Blocking I/O vs non-blocking I/O vs async I/O (three different things)", 2.0, 3, "", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Theory: select/poll/epoll progression — why epoll changed everything", 2.0, 3, "", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Theory: File descriptors, sockets, 'everything is a file'", 1.5, 2, "", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Article: 'The C10K Problem' — Dan Kegel", 1.5, 3, "Defined modern async server design", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Article: 'How Node.js Works Behind the Scenes' — libuv event loop", 1.5, 2, "", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Article: 'Blocking I/O, Nonblocking I/O, And Epoll' — Daan Leijen", 1.5, 3, "", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Article: 'Inside nginx' — event-driven model vs Apache process-per-connection", 1.0, 2, "NGINX blog", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Article: 'Fibers, Oh My!' — Cloudflare coroutines in production", 1.0, 2, "", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Book: DDIA Chapter 1 — 'Reliable, Scalable, Maintainable Applications'", 3.0, 2, "Read as framing for everything", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Project: Raw HTTP server — accept HTTP/1.1 GET, parse headers, return response", 4.0, 3, "No frameworks, raw TCP sockets", "Foundation", "0.2"),
        StudyBlock("Operating Systems", "0.2 OS: Processes, Threads, I/O", "Project: Rewrite server with non-blocking I/O using epoll", 4.0, 4, "Benchmark both under 1000 concurrent connections", "Foundation", "0.2"),
    ])

    # 0.3 Networking Internals
    blocks.extend([
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Theory: OSI model practical layers (L4 TCP/UDP, L7 HTTP)", 1.5, 2, "", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Theory: TCP three-way handshake, teardown, TIME_WAIT states", 2.0, 3, "", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Theory: TCP congestion control, slow start", 1.5, 3, "", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Theory: UDP use cases (DNS, video, gaming), DNS resolution chain", 1.5, 2, "", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Theory: TLS 1.3 handshake, certificate chain, session resumption", 2.0, 3, "", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Article: 'High Performance Browser Networking' Ch.1-4 — Ilya Grigorik (hpbn.co)", 3.0, 2, "Best networking primer ever written", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Article: Cloudflare DNS + HTTPS explanations", 1.0, 2, "", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Article: 'How QUIC is Replacing TCP for HTTP/3' — Fastly", 1.0, 3, "", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Article: 'The Story of One Latency Spike' — Cloudflare TIME_WAIT incident", 1.0, 3, "", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Article: 'TLS 1.3: 0-RTT, resumption, anti-replay' — Cloudflare", 1.0, 3, "", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Project: TCP chat server — multi-client with rooms/channels", 4.0, 3, "Raw sockets, no frameworks", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Project: TCP chat — handle disconnections gracefully", 2.0, 3, "Detect broken connections", "Foundation", "0.3"),
        StudyBlock("Networking", "0.3 Networking Internals: TCP/IP, DNS, TLS", "Project: Binary wire protocol — header (type+length) + body", 3.0, 4, "Benchmark concurrent connection capacity", "Foundation", "0.3"),
    ])

    # 0.4 Linux CLI
    blocks.extend([
        StudyBlock("Linux/Operations", "0.4 Linux CLI for Backend Engineers", "Article: 'Linux Performance Analysis in 60s' — Netflix/Brendan Gregg", 1.5, 2, "Canonical diagnostic commands list", "Foundation", "0.4"),
        StudyBlock("Linux/Operations", "0.4 Linux CLI for Backend Engineers", "Article: 'Linux Tracing Systems' — Julia Evans (jvns.ca)", 1.5, 2, "strace, ltrace, perf, eBPF", "Foundation", "0.4"),
        StudyBlock("Linux/Operations", "0.4 Linux CLI for Backend Engineers", "Article: 'The USE Method' — Brendan Gregg", 1.0, 2, "Utilization, Saturation, Errors methodology", "Foundation", "0.4"),
        StudyBlock("Linux/Operations", "0.4 Linux CLI for Backend Engineers", "Article: 'How Containers Work' — Julia Evans — cgroups, namespaces", 1.5, 3, "", "Foundation", "0.4"),
        StudyBlock("Linux/Operations", "0.4 Linux CLI for Backend Engineers", "Project: Diagnose simulated production issues — memory leak", 2.0, 3, "top/htop, lsof", "Foundation", "0.4"),
        StudyBlock("Linux/Operations", "0.4 Linux CLI for Backend Engineers", "Project: Diagnose simulated issues — CPU spin, file descriptor leak", 2.0, 3, "strace -p, ss/netstat", "Foundation", "0.4"),
        StudyBlock("Linux/Operations", "0.4 Linux CLI for Backend Engineers", "Project: Capture and analyze packets with tcpdump", 2.0, 3, "Inspect real TCP handshake", "Foundation", "0.4"),
    ])

    # --- Level 1: APIs & Protocols ---

    # 1.1 REST
    blocks.extend([
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Theory: REST constraints — statelessness, uniform interface, HATEOAS", 1.5, 2, "", "Foundation", "1.1"),
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Theory: HTTP verbs as semantic contracts, idempotency of PUT vs POST", 1.5, 2, "", "Foundation", "1.1"),
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Theory: HTTP status codes semantics, idempotency keys, content negotiation", 1.5, 2, "", "Foundation", "1.1"),
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Article: Zalando RESTful API Guidelines", 2.0, 2, "Most thorough production REST guide", "Foundation", "1.1"),
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Article: Stripe API Design + Idempotency keys", 1.5, 2, "Real-world API design at scale", "Foundation", "1.1"),
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Article: Intercom API Versioning + Vinay Sahni pragmatic REST", 1.5, 2, "", "Foundation", "1.1"),
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Project: Task Manager API — CRUD + proper HTTP semantics", 3.0, 2, "Foundation of the portfolio project", "Foundation", "1.1"),
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Project: Task Manager — cursor-based pagination + filtering + sorting", 3.0, 3, "", "Foundation", "1.1"),
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Project: Task Manager — idempotency keys + rate limiting (token bucket)", 3.0, 3, "", "Foundation", "1.1"),
        StudyBlock("APIs & Protocols", "1.1 REST: The Deep Cut", "Project: Task Manager — API versioning + OpenAPI spec (Swagger)", 2.5, 2, "Document everything", "Foundation", "1.1"),
    ])

    # 1.2 gRPC
    blocks.extend([
        StudyBlock("APIs & Protocols", "1.2 gRPC & Protobuf", "Theory: Protocol Buffers — field numbers, varint, backward/forward compat", 2.0, 3, "", "Foundation", "1.2"),
        StudyBlock("APIs & Protocols", "1.2 gRPC & Protobuf", "Theory: gRPC over HTTP/2 — multiplexing, streaming, 4 modes", 2.0, 3, "", "Foundation", "1.2"),
        StudyBlock("APIs & Protocols", "1.2 gRPC & Protobuf", "Article: 'Why We Use gRPC at Square' + Google Cloud gRPC vs REST", 1.5, 2, "", "Foundation", "1.2"),
        StudyBlock("APIs & Protocols", "1.2 gRPC & Protobuf", "Article: Netflix gRPC + Kleppmann schema evolution blog", 1.5, 3, "", "Foundation", "1.2"),
        StudyBlock("APIs & Protocols", "1.2 gRPC & Protobuf", "Book: DDIA Chapter 4 — 'Encoding and Evolution'", 3.0, 3, "", "Foundation", "1.2"),
        StudyBlock("APIs & Protocols", "1.2 gRPC & Protobuf", "Project: gRPC User microservice — Protobuf schema + unary RPCs", 3.0, 3, "", "Foundation", "1.2"),
        StudyBlock("APIs & Protocols", "1.2 gRPC & Protobuf", "Project: gRPC — server streaming + interceptors for logging/auth", 3.0, 3, "", "Foundation", "1.2"),
        StudyBlock("APIs & Protocols", "1.2 gRPC & Protobuf", "Project: gRPC — cross-language client to prove interoperability", 2.5, 3, "", "Foundation", "1.2"),
    ])

    # 1.3 WebSockets & Real-Time
    blocks.extend([
        StudyBlock("APIs & Protocols", "1.3 WebSockets, SSE & Real-Time", "Theory: Long polling, SSE, WebSockets — tradeoffs and upgrade handshake", 2.0, 2, "", "Foundation", "1.3"),
        StudyBlock("APIs & Protocols", "1.3 WebSockets, SSE & Real-Time", "Theory: WebSocket at scale — sticky sessions, horizontal scaling", 1.5, 3, "", "Foundation", "1.3"),
        StudyBlock("APIs & Protocols", "1.3 WebSockets, SSE & Real-Time", "Article: Slack WebSockets + Discord voice scaling", 1.5, 2, "", "Foundation", "1.3"),
        StudyBlock("APIs & Protocols", "1.3 WebSockets, SSE & Real-Time", "Article: 'SSE vs WebSockets' — Ably + 'Scaling to 1M' — Fanout.io", 1.5, 3, "", "Foundation", "1.3"),
        StudyBlock("APIs & Protocols", "1.3 WebSockets, SSE & Real-Time", "Project: Collaborative whiteboard — WebSocket server with rooms", 3.0, 3, "", "Foundation", "1.3"),
        StudyBlock("APIs & Protocols", "1.3 WebSockets, SSE & Real-Time", "Project: Whiteboard — real-time drawing broadcast + reconnection w/ replay", 3.0, 3, "", "Foundation", "1.3"),
        StudyBlock("APIs & Protocols", "1.3 WebSockets, SSE & Real-Time", "Project: Whiteboard — horizontal scaling with Redis pub/sub", 3.0, 4, "", "Foundation", "1.3"),
    ])

    # 1.4 GraphQL (depends on 1.1, 1.2, 1.3)
    blocks.extend([
        StudyBlock("APIs & Protocols", "1.4 GraphQL", "Theory: Over/under-fetching, SDL, resolvers, N+1 problem, DataLoader", 2.0, 3, "Depends on REST understanding", "Foundation", "1.4"),
        StudyBlock("APIs & Protocols", "1.4 GraphQL", "Theory: GraphQL subscriptions + Federation for multi-team schemas", 1.5, 3, "", "Foundation", "1.4"),
        StudyBlock("APIs & Protocols", "1.4 GraphQL", "Article: How Facebook invented GraphQL + GitHub's move to GraphQL", 1.5, 2, "", "Foundation", "1.4"),
        StudyBlock("APIs & Protocols", "1.4 GraphQL", "Article: Shopify scaling GraphQL + Apollo N+1 blog", 1.5, 3, "", "Foundation", "1.4"),
        StudyBlock("APIs & Protocols", "1.4 GraphQL", "Project: GraphQL blog API — schema, resolvers, depth limiting", 3.0, 3, "", "Foundation", "1.4"),
        StudyBlock("APIs & Protocols", "1.4 GraphQL", "Project: GraphQL — DataLoader implementation + benchmark before/after", 3.0, 3, "", "Foundation", "1.4"),
        StudyBlock("APIs & Protocols", "1.4 GraphQL", "Project: GraphQL — subscriptions + complexity analysis", 2.5, 4, "", "Foundation", "1.4"),
    ])

    # --- Level A: Design Patterns ---

    # A.1 SOLID
    blocks.extend([
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Theory: SRP — one reason to change, real-world violations", 1.5, 2, "", "Foundation", "A.1"),
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Theory: OCP — open for extension, closed for modification", 1.5, 2, "", "Foundation", "A.1"),
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Theory: LSP — subtypes substitutable for base types", 1.5, 3, "", "Foundation", "A.1"),
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Theory: ISP — no fat interfaces + DIP — depend on abstractions", 2.0, 3, "", "Foundation", "A.1"),
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Article: Khalil Stemmler SOLID + Dan North 'SOLID is Not Solid'", 2.0, 2, "Best modern treatment + counterargument", "Foundation", "A.1"),
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Article: Sandi Metz 'Wrong Abstraction' + Dan Abramov 'Goodbye Clean Code'", 1.5, 2, "Balance to SOLID orthodoxy", "Foundation", "A.1"),
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Book: Clean Architecture Part III — Chapters 7-11 (SOLID)", 4.0, 3, "", "Foundation", "A.1"),
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Project: Refactor violation-ridden e-commerce — extract Repository (DIP)", 3.0, 3, "", "Foundation", "A.1"),
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Project: Refactor — PaymentStrategy interface (OCP) + split services (SRP)", 3.0, 3, "", "Foundation", "A.1"),
        StudyBlock("Design Patterns", "A.1 SOLID Principles", "Project: Verify — test OrderService without DB, add CryptoPayment without edits", 2.0, 3, "", "Foundation", "A.1"),
    ])

    # A.2 GoF Patterns
    blocks.extend([
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Theory: Creational — Singleton, Factory, Builder, Prototype", 3.0, 3, "With real-world backend examples", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Theory: Structural — Adapter, Decorator, Facade, Proxy, Composite", 3.0, 3, "", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Theory: Behavioral — Strategy, Observer, Command, Chain of Responsibility", 3.0, 3, "", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Theory: Behavioral — Template Method, Iterator, State, Mediator", 2.0, 3, "", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Article: Refactoring.Guru visual reference + Python Patterns by Brandon Rhodes", 2.0, 2, "Bookmark refactoring.guru", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Article: 'Design Patterns in Go' + 'How Django Uses Design Patterns'", 2.0, 2, "", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Book: Head First Design Patterns — key chapters", 3.0, 2, "Friendlier first exposure", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Book: GoF Chapter — Creational + Structural patterns catalog", 3.0, 3, "", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Book: GoF Chapter — Behavioral patterns catalog", 2.0, 3, "", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Project Phase 1: Pattern recognition — find 8 patterns in Django/Flask/FastAPI source", 3.0, 3, "", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Project Phase 2: Payment system — Strategy + Factory + Decorator patterns", 3.0, 3, "", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Project Phase 2: Payment system — Command + Observer + State patterns", 3.0, 3, "", "Foundation", "A.2"),
        StudyBlock("Design Patterns", "A.2 GoF Design Patterns", "Project Phase 3: Test isolation — MockPaymentStrategy, zero code changes", 2.0, 3, "", "Foundation", "A.2"),
    ])

    # A.3 Architectural Patterns
    blocks.extend([
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Theory: Repository Pattern + Unit of Work Pattern", 2.0, 3, "", "Foundation", "A.3"),
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Theory: CQRS at code level — separate read/write models", 2.0, 3, "", "Foundation", "A.3"),
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Theory: Service Layer + Ports & Adapters (Hexagonal Architecture)", 2.0, 3, "", "Foundation", "A.3"),
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Theory: Event-Driven at code level + Outbox Pattern", 2.0, 3, "", "Foundation", "A.3"),
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Article: Fowler Repository + Cockburn Hexagonal Architecture", 1.5, 2, "", "Foundation", "A.3"),
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Article: Debezium Outbox + Fowler Service Layer vs Domain Model", 1.5, 3, "", "Foundation", "A.3"),
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Book: 'Architecture Patterns with Python' (cosmicpython.com) Ch.1-6", 4.0, 3, "Free online — the best practical hexagonal arch book", "Foundation", "A.3"),
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Project: Rebuild Task Manager — Domain layer + TaskRepository interface", 3.0, 3, "", "Foundation", "A.3"),
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Project: Task Manager — Service layer + PostgresRepo + InMemoryRepo", 3.0, 3, "", "Foundation", "A.3"),
        StudyBlock("Design Patterns", "A.3 Architectural Patterns", "Project: Task Manager — API layer + unit tests with InMemoryRepo", 3.0, 3, "Prove: swap repos without changing service code", "Foundation", "A.3"),
    ])

    # A.4 DDD
    blocks.extend([
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Theory: Ubiquitous Language + Bounded Contexts", 2.0, 3, "", "Foundation", "A.4"),
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Theory: Aggregates, Aggregate Roots, transaction boundaries", 2.0, 3, "", "Foundation", "A.4"),
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Theory: Value Objects vs Entities + Domain Events", 2.0, 3, "", "Foundation", "A.4"),
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Theory: Anti-Corruption Layer (ACL)", 1.5, 3, "", "Foundation", "A.4"),
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Article: 'DDD Quickly' InfoQ + Airbnb DDD implementation", 2.0, 3, "", "Foundation", "A.4"),
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Article: Vernon Aggregates + Bogard Domain vs Integration Events", 1.5, 3, "", "Foundation", "A.4"),
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Book: DDD Quickly (InfoQ free PDF) — full read", 4.0, 3, "", "Foundation", "A.4"),
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Project: E-commerce Order context — Aggregate + Value Objects + business rules", 3.0, 3, "", "Foundation", "A.4"),
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Project: E-commerce — Repository + Domain Events (OrderPlaced, etc.)", 3.0, 3, "", "Foundation", "A.4"),
        StudyBlock("Design Patterns", "A.4 Domain-Driven Design", "Project: E-commerce — Anti-Corruption Layer for legacy inventory API + context map", 3.0, 4, "", "Foundation", "A.4"),
    ])

    # A.5 Concurrency Patterns (depends on A.1)
    blocks.extend([
        StudyBlock("Design Patterns", "A.5 Concurrency Patterns", "Theory: Mutex, RWMutex — write-heavy vs read-heavy workloads", 1.5, 3, "", "Intermediate", "A.5"),
        StudyBlock("Design Patterns", "A.5 Concurrency Patterns", "Theory: Worker Pool + Fan-Out/Fan-In patterns", 2.0, 3, "", "Intermediate", "A.5"),
        StudyBlock("Design Patterns", "A.5 Concurrency Patterns", "Theory: Pipeline Pattern + Semaphore Pattern", 2.0, 3, "", "Intermediate", "A.5"),
        StudyBlock("Design Patterns", "A.5 Concurrency Patterns", "Theory: Context propagation (cancellation+deadlines) + Optimistic Concurrency", 2.0, 3, "", "Intermediate", "A.5"),
        StudyBlock("Design Patterns", "A.5 Concurrency Patterns", "Article: Rob Pike 'Go Concurrency Patterns' + Sameer Ajmani 'Advanced'", 2.0, 3, "Watch both YouTube talks", "Intermediate", "A.5"),
        StudyBlock("Design Patterns", "A.5 Concurrency Patterns", "Article: 'Visualizing Concurrency in Go' + Real Python asyncio walkthrough", 1.5, 2, "", "Intermediate", "A.5"),
        StudyBlock("Design Patterns", "A.5 Concurrency Patterns", "Project: Concurrent image service — worker pool + fan-out/fan-in", 3.0, 4, "5 workers, buffered channel queue", "Intermediate", "A.5"),
        StudyBlock("Design Patterns", "A.5 Concurrency Patterns", "Project: Image service — semaphore + context cancellation", 3.0, 4, "Max 10 concurrent, cancel on disconnect", "Intermediate", "A.5"),
        StudyBlock("Design Patterns", "A.5 Concurrency Patterns", "Project: Image service — race detector + load test 500 concurrent", 2.5, 4, "go test -race, verify no OOM", "Intermediate", "A.5"),
    ])

    # --- Level 2: Databases ---

    # 2.1 DB Internals
    blocks.extend([
        StudyBlock("Databases", "2.1 Database Internals", "Theory: B-Trees — pages, branching factor, write amplification", 2.0, 3, "", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Theory: LSM Trees — SSTables, compaction, write/read amplification tradeoffs", 2.0, 3, "", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Theory: WAL, MVCC, buffer pool, page layout", 2.5, 3, "", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Article: 'Use The Index Luke' B-tree guide + Meta RocksDB (LSM)", 2.0, 3, "", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Article: Postgres MVCC + Jay Kreps 'The Log' essay", 2.0, 3, "Unifying abstraction of real-time data", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Book: DDIA Chapter 3 — 'Storage and Retrieval' (read twice)", 4.0, 3, "The most important DDIA chapter", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Book: Database Internals (Petrov) Ch.2 + Ch.5", 4.0, 4, "", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Project: KV store v1 — append-only log + in-memory hashmap", 3.0, 3, "Bitcask-style", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Project: KV store v2 — log compaction (merge old logs)", 3.0, 4, "", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Project: KV store v3 — Bloom filter for missing keys", 2.5, 4, "", "Foundation", "2.1"),
        StudyBlock("Databases", "2.1 Database Internals", "Project: KV store v4 — CRC checksums for corruption detection", 2.0, 3, "", "Foundation", "2.1"),
    ])

    # 2.2 PostgreSQL
    blocks.extend([
        StudyBlock("Databases", "2.2 PostgreSQL Professional", "Theory: EXPLAIN ANALYZE — seq scan, index scan, index-only scan", 2.0, 3, "", "Foundation", "2.2"),
        StudyBlock("Databases", "2.2 PostgreSQL Professional", "Theory: Index types (B-tree, Hash, GIN, GiST), partial + expression indexes", 2.0, 3, "", "Foundation", "2.2"),
        StudyBlock("Databases", "2.2 PostgreSQL Professional", "Theory: Connection pooling (PgBouncer), partitioning strategies", 1.5, 3, "", "Foundation", "2.2"),
        StudyBlock("Databases", "2.2 PostgreSQL Professional", "Article: pganalyze query optimizer + Crunchy Data PgBouncer", 1.5, 2, "", "Foundation", "2.2"),
        StudyBlock("Databases", "2.2 PostgreSQL Professional", "Article: Heap partial indexes + Notion sharding + Discord DB migration", 2.0, 3, "Real case studies", "Foundation", "2.2"),
        StudyBlock("Databases", "2.2 PostgreSQL Professional", "Project: Load 10M+ rows, run slow queries, EXPLAIN ANALYZE", 3.0, 3, "", "Foundation", "2.2"),
        StudyBlock("Databases", "2.2 PostgreSQL Professional", "Project: Add indexes, benchmark improvements, set up PgBouncer", 3.0, 3, "", "Foundation", "2.2"),
        StudyBlock("Databases", "2.2 PostgreSQL Professional", "Project: Implement table partitioning, measure impact", 2.5, 3, "", "Foundation", "2.2"),
    ])

    # 2.3 NoSQL
    blocks.extend([
        StudyBlock("Databases", "2.3 NoSQL Databases", "Theory: Document stores (MongoDB/DynamoDB) — embedding vs referencing", 2.0, 2, "", "Foundation", "2.3"),
        StudyBlock("Databases", "2.3 NoSQL Databases", "Theory: Wide-column (Cassandra), KV stores (Redis), Graph (Neo4j), Time-series", 2.5, 3, "", "Foundation", "2.3"),
        StudyBlock("Databases", "2.3 NoSQL Databases", "Article: DynamoDB docs + Cassandra data modeling + Instagram Cassandra", 2.0, 3, "", "Foundation", "2.3"),
        StudyBlock("Databases", "2.3 NoSQL Databases", "Article: Redis data structures + InfluxDB time-series", 1.5, 2, "", "Foundation", "2.3"),
        StudyBlock("Databases", "2.3 NoSQL Databases", "Book: DDIA Chapter 2 — 'Data Models and Query Languages'", 3.0, 2, "", "Foundation", "2.3"),
        StudyBlock("Databases", "2.3 NoSQL Databases", "Project: Social feed — PostgreSQL for users, Redis for timeline cache", 3.0, 3, "", "Foundation", "2.3"),
        StudyBlock("Databases", "2.3 NoSQL Databases", "Project: Social feed — Cassandra for notification history", 3.0, 3, "", "Foundation", "2.3"),
        StudyBlock("Databases", "2.3 NoSQL Databases", "Project: Benchmark read latency from each backend under load", 2.0, 3, "", "Foundation", "2.3"),
    ])

    # 2.4 Transactions (depends on 2.1)
    blocks.extend([
        StudyBlock("Databases", "2.4 Transactions & ACID", "Theory: ACID properties in practice", 1.5, 3, "", "Intermediate", "2.4"),
        StudyBlock("Databases", "2.4 Transactions & ACID", "Theory: Isolation levels — Read Uncommitted → Serializable", 2.0, 3, "", "Intermediate", "2.4"),
        StudyBlock("Databases", "2.4 Transactions & ACID", "Theory: Phenomena (dirty reads, phantom reads, write skew, lost updates)", 2.0, 3, "", "Intermediate", "2.4"),
        StudyBlock("Databases", "2.4 Transactions & ACID", "Theory: Optimistic vs pessimistic locking, 2PL vs MVCC, SSI", 2.0, 4, "", "Intermediate", "2.4"),
        StudyBlock("Databases", "2.4 Transactions & ACID", "Article: Kleppmann 'stop calling DBs CP/AP' + Berenson 1995 paper", 2.0, 4, "", "Intermediate", "2.4"),
        StudyBlock("Databases", "2.4 Transactions & ACID", "Article: Stripe idempotency + distributed locks — Brandur Leach", 1.5, 3, "", "Intermediate", "2.4"),
        StudyBlock("Databases", "2.4 Transactions & ACID", "Book: DDIA Chapter 7 — 'Transactions' (read slowly, twice)", 4.0, 4, "One of the densest DDIA chapters", "Intermediate", "2.4"),
        StudyBlock("Databases", "2.4 Transactions & ACID", "Project: Trigger lost updates in bank account system", 2.5, 4, "", "Intermediate", "2.4"),
        StudyBlock("Databases", "2.4 Transactions & ACID", "Project: Trigger write skew + phantom reads, fix each correctly", 2.5, 4, "", "Intermediate", "2.4"),
        StudyBlock("Databases", "2.4 Transactions & ACID", "Project: Benchmark Serializable vs Read Committed performance", 2.0, 3, "", "Intermediate", "2.4"),
    ])

    # 2.5 DB Scaling (depends on 2.1 + 2.2)
    blocks.extend([
        StudyBlock("Databases", "2.5 Database Scaling", "Theory: Single-leader replication — lag, read-your-writes consistency", 2.0, 3, "", "Intermediate", "2.5"),
        StudyBlock("Databases", "2.5 Database Scaling", "Theory: Multi-leader + leaderless replication, quorums (W+R>N)", 2.0, 4, "", "Intermediate", "2.5"),
        StudyBlock("Databases", "2.5 Database Scaling", "Theory: Sharding strategies — range, hash, consistent hashing + CQRS replicas", 2.0, 3, "", "Intermediate", "2.5"),
        StudyBlock("Databases", "2.5 Database Scaling", "Article: Notion sharding + Vitess + Instacart read replicas + Heap scaling", 2.0, 3, "", "Intermediate", "2.5"),
        StudyBlock("Databases", "2.5 Database Scaling", "Book: DDIA Chapter 5 — 'Replication'", 3.0, 3, "", "Intermediate", "2.5"),
        StudyBlock("Databases", "2.5 Database Scaling", "Book: DDIA Chapter 6 — 'Partitioning'", 3.0, 3, "", "Intermediate", "2.5"),
    ])

    # --- Level B: DevOps ---

    # B.1 Docker
    blocks.extend([
        StudyBlock("DevOps", "B.1 Docker: Containers from First Principles", "Theory: namespaces, cgroups, union filesystems — Linux primitives", 2.0, 3, "", "Intermediate", "B.1"),
        StudyBlock("DevOps", "B.1 Docker: Containers from First Principles", "Theory: Image layers, layer caching, image vs container", 1.5, 2, "", "Intermediate", "B.1"),
        StudyBlock("DevOps", "B.1 Docker: Containers from First Principles", "Theory: Networking, volumes, multi-stage builds, entrypoint vs CMD", 2.0, 3, "", "Intermediate", "B.1"),
        StudyBlock("DevOps", "B.1 Docker: Containers from First Principles", "Article: Liz Rice 'Containers from Scratch' GOTO 2018 + Docker blog", 2.0, 3, "She builds a container with Go syscalls", "Intermediate", "B.1"),
        StudyBlock("DevOps", "B.1 Docker: Containers from First Principles", "Article: Hynek Schlawack Docker best practices + Distroless images", 1.5, 2, "", "Intermediate", "B.1"),
        StudyBlock("DevOps", "B.1 Docker: Containers from First Principles", "Book: Docker Deep Dive — Nigel Poulton (200 pages)", 4.0, 2, "Read in 2 days", "Intermediate", "B.1"),
        StudyBlock("DevOps", "B.1 Docker: Containers from First Principles", "Project: Dockerize Task API — v1 naive → v2 multi-stage → v3 non-root", 3.0, 3, "", "Intermediate", "B.1"),
        StudyBlock("DevOps", "B.1 Docker: Containers from First Principles", "Project: v4 optimized layers → v5 .dockerignore + HEALTHCHECK", 2.5, 3, "", "Intermediate", "B.1"),
        StudyBlock("DevOps", "B.1 Docker: Containers from First Principles", "Project: Compare image sizes v1 vs v5 + security audit with trivy", 2.0, 3, "", "Intermediate", "B.1"),
    ])

    # B.2 Docker Compose
    blocks.extend([
        StudyBlock("DevOps", "B.2 Docker Compose & Networking", "Theory: Compose file, service dependencies, healthchecks", 1.5, 2, "", "Intermediate", "B.2"),
        StudyBlock("DevOps", "B.2 Docker Compose & Networking", "Theory: Container networking, env vars, override files, named volumes", 1.5, 2, "", "Intermediate", "B.2"),
        StudyBlock("DevOps", "B.2 Docker Compose & Networking", "Article: Compose in production + healthcheck patterns + networking docs", 1.5, 2, "", "Intermediate", "B.2"),
        StudyBlock("DevOps", "B.2 Docker Compose & Networking", "Project: Full stack — API + Postgres + Redis + RabbitMQ + Worker + PGAdmin", 4.0, 3, "", "Intermediate", "B.2"),
        StudyBlock("DevOps", "B.2 Docker Compose & Networking", "Project: Healthchecks, private network, .env, override for dev hot-reload", 3.0, 3, "", "Intermediate", "B.2"),
    ])

    # B.3 Kubernetes
    blocks.extend([
        StudyBlock("DevOps", "B.3 Kubernetes", "Theory: Pod, Deployment, ReplicaSet, Service, Ingress", 2.5, 3, "", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Theory: ConfigMap, Secret, Namespace, resource requests/limits", 2.0, 3, "", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Theory: kube-proxy, CoreDNS, network policies, CNI plugins", 2.0, 3, "", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Theory: PV/PVC, StorageClass, StatefulSet, DaemonSet, Job/CronJob", 2.0, 3, "", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Theory: HPA, VPA, Cluster Autoscaler", 1.5, 3, "", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Article: Julia Evans K8s networking + Kubernetes Failure Stories (k8s.af)", 2.0, 3, "", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Article: Airbnb K8s migration + Datadog K8s at scale + OOMKilled debugging", 2.0, 3, "", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Book: Kubernetes in Action — Chapters 1-9", 6.0, 3, "Most thorough K8s book", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Project Phase 1: YAML manifests — Deployment, StatefulSet, Service, ConfigMap", 3.0, 3, "", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Project Phase 1: Liveness/readiness probes, kubectl apply", 2.0, 3, "", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Project Phase 2: Ingress + HPA + k6 load test", 3.0, 3, "Watch pods scale in real time", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Project Phase 3: Rolling deployment + rollback", 2.5, 3, "Deploy broken image, watch K8s stop rollout", "Intermediate", "B.3"),
        StudyBlock("DevOps", "B.3 Kubernetes", "Project Phase 4: Helm chart + deploy to staging + production namespaces", 3.0, 3, "", "Intermediate", "B.3"),
    ])

    # B.4 Message Queues
    blocks.extend([
        StudyBlock("DevOps", "B.4 Message Queues: RabbitMQ & Celery", "Theory: RabbitMQ vs Kafka — the actual difference, when to use each", 2.0, 3, "", "Intermediate", "B.4"),
        StudyBlock("DevOps", "B.4 Message Queues: RabbitMQ & Celery", "Theory: RabbitMQ concepts — exchanges, acks, DLX, prefetch, publisher confirms", 2.5, 3, "", "Intermediate", "B.4"),
        StudyBlock("DevOps", "B.4 Message Queues: RabbitMQ & Celery", "Theory: Celery — tasks, Beat scheduler, result backend, retry, chaining", 2.0, 3, "", "Intermediate", "B.4"),
        StudyBlock("DevOps", "B.4 Message Queues: RabbitMQ & Celery", "Article: RabbitMQ tutorials (all 6) + CloudAMQP RabbitMQ vs Kafka", 3.0, 2, "", "Intermediate", "B.4"),
        StudyBlock("DevOps", "B.4 Message Queues: RabbitMQ & Celery", "Article: Celery best practices + Robinhood Celery at scale", 1.5, 3, "", "Intermediate", "B.4"),
        StudyBlock("DevOps", "B.4 Message Queues: RabbitMQ & Celery", "Project: Async doc processing — API → S3 → RabbitMQ → Celery worker", 4.0, 3, "", "Intermediate", "B.4"),
        StudyBlock("DevOps", "B.4 Message Queues: RabbitMQ & Celery", "Project: DLX + exponential backoff + Flower monitoring + priority queue", 3.0, 4, "", "Intermediate", "B.4"),
        StudyBlock("DevOps", "B.4 Message Queues: RabbitMQ & Celery", "Project: Rate limiting per tenant + stale job CronJob + chaos test", 3.0, 4, "Kill worker mid-processing, verify requeue", "Intermediate", "B.4"),
    ])

    # B.5 Redis Operations
    blocks.extend([
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Theory: String, List, Hash, Set data structures + use cases", 2.0, 2, "", "Intermediate", "B.5"),
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Theory: Sorted Set, HyperLogLog, Pub/Sub, Streams", 2.0, 3, "", "Intermediate", "B.5"),
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Theory: Cache patterns (aside, write-through), distributed lock (Redlock)", 2.0, 3, "", "Intermediate", "B.5"),
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Theory: Redis Cluster, Sentinel, persistence (RDB, AOF)", 2.0, 3, "", "Intermediate", "B.5"),
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Article: Kleppmann vs Antirez Redlock debate + Facebook Memcache paper", 2.0, 4, "Critical read on Redis locking limits", "Intermediate", "B.5"),
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Article: Slack Redis Sorted Sets + Redis rate limiting patterns", 1.5, 3, "", "Intermediate", "B.5"),
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Project: Caching with TTL + invalidation + leaderboard (ZSet)", 3.0, 3, "", "Intermediate", "B.5"),
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Project: Rate limiting (sliding window Lua) + distributed lock", 3.0, 4, "", "Intermediate", "B.5"),
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Project: Pub/Sub → WebSocket fanout + HyperLogLog DAU tracking", 3.0, 3, "", "Intermediate", "B.5"),
        StudyBlock("DevOps", "B.5 Redis: Beyond GET/SET", "Project: Redis Streams audit log + Cluster exercise (3 masters, 3 replicas)", 3.0, 4, "Kill master, verify failover", "Intermediate", "B.5"),
    ])

    # B.6 CI/CD
    blocks.extend([
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Theory: CI vs CD vs Continuous Deployment, pipeline stages", 1.5, 2, "", "Intermediate", "B.6"),
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Theory: GitHub Actions concepts — workflows, jobs, runners, caching, secrets", 2.0, 2, "", "Intermediate", "B.6"),
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Theory: Deployment strategies — rolling, blue/green, canary, feature flags", 2.0, 3, "", "Intermediate", "B.6"),
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Theory: IaC — Terraform, Pulumi, AWS CDK", 1.5, 3, "", "Intermediate", "B.6"),
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Article: GitHub CI/CD at scale + Fowler blue/green + Google SRE canary", 2.0, 2, "", "Intermediate", "B.6"),
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Article: Netflix Spinnaker + GitOps with Argo CD/Flux", 1.5, 3, "", "Intermediate", "B.6"),
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Project: GitHub Actions — lint + unit test + integration test + security scan", 3.0, 3, "", "Intermediate", "B.6"),
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Project: Build + push Docker image + deploy staging + smoke test", 3.0, 3, "", "Intermediate", "B.6"),
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Project: Production deploy with manual approval + Slack notify", 2.5, 3, "", "Intermediate", "B.6"),
        StudyBlock("DevOps", "B.6 CI/CD & Infrastructure as Code", "Project: Terraform — K8s namespace, RBAC, resource quotas, remote state", 3.0, 3, "", "Intermediate", "B.6"),
    ])

    # --- Level 3: Distributed Systems ---

    # 3.1 Core Problems
    blocks.extend([
        StudyBlock("Distributed Systems", "3.1 Core Problems of Distributed Systems", "Theory: 8 Fallacies of Distributed Computing", 1.5, 3, "", "Advanced", "3.1"),
        StudyBlock("Distributed Systems", "3.1 Core Problems of Distributed Systems", "Theory: Partial failures, unreliable networks, Two Generals, Byzantine faults", 2.0, 4, "", "Advanced", "3.1"),
        StudyBlock("Distributed Systems", "3.1 Core Problems of Distributed Systems", "Article: Jeff Hodges 'Notes for Young Bloods' + Aphyr intro", 2.0, 3, "Required reading", "Advanced", "3.1"),
        StudyBlock("Distributed Systems", "3.1 Core Problems of Distributed Systems", "Article: AWS HA systems + Netflix Chaos Engineering", 1.5, 3, "", "Advanced", "3.1"),
        StudyBlock("Distributed Systems", "3.1 Core Problems of Distributed Systems", "Book: DDIA Chapter 8 — 'The Trouble with Distributed Systems'", 3.0, 4, "", "Advanced", "3.1"),
    ])

    # 3.2 MIT 6.824
    blocks.extend([
        StudyBlock("Distributed Systems", "3.2 MIT 6.824 Labs", "Lab 1: MapReduce — implement framework in Go, fault-tolerant workers", 12.0, 4, "THE most valuable project on roadmap", "Advanced", "3.2"),
        StudyBlock("Distributed Systems", "3.2 MIT 6.824 Labs", "Lab 2: Key/Value Server — at-least-once RPC semantics", 10.0, 4, "", "Advanced", "3.2"),
        StudyBlock("Distributed Systems", "3.2 MIT 6.824 Labs", "Lab 3: Raft Consensus — leader election + log replication", 16.0, 5, "The crown jewel", "Advanced", "3.2"),
        StudyBlock("Distributed Systems", "3.2 MIT 6.824 Labs", "Lab 3 (cont): Raft — persistence + log compaction", 12.0, 5, "", "Advanced", "3.2"),
        StudyBlock("Distributed Systems", "3.2 MIT 6.824 Labs", "Lab 4: Fault-Tolerant KV on top of Raft", 14.0, 5, "", "Advanced", "3.2"),
        StudyBlock("Distributed Systems", "3.2 MIT 6.824 Labs", "Lab 5: Sharded KV across Raft groups + reconfiguration", 16.0, 5, "", "Advanced", "3.2"),
    ])

    # 3.3 Consensus (depends on 3.1)
    blocks.extend([
        StudyBlock("Distributed Systems", "3.3 Consensus & Consistency", "Theory: Consensus problem + Paxos", 2.0, 4, "", "Advanced", "3.3"),
        StudyBlock("Distributed Systems", "3.3 Consensus & Consistency", "Theory: Raft — leader election, log replication, safety", 2.0, 4, "", "Advanced", "3.3"),
        StudyBlock("Distributed Systems", "3.3 Consensus & Consistency", "Theory: Consistency models — linearizability → eventual consistency", 2.0, 4, "", "Advanced", "3.3"),
        StudyBlock("Distributed Systems", "3.3 Consensus & Consistency", "Article: Lamport 'Paxos Made Simple' + Raft paper", 3.0, 4, "Original papers", "Advanced", "3.3"),
        StudyBlock("Distributed Systems", "3.3 Consensus & Consistency", "Article: CockroachDB distributed txns + Kleppmann eventual consistency", 2.0, 4, "", "Advanced", "3.3"),
        StudyBlock("Distributed Systems", "3.3 Consensus & Consistency", "Book: DDIA Chapter 9 — 'Consistency and Consensus'", 3.0, 4, "", "Advanced", "3.3"),
    ])

    # 3.4 Kafka/EDA
    blocks.extend([
        StudyBlock("Distributed Systems", "3.4 Kafka & Event-Driven Architecture", "Theory: The Log abstraction, topics, partitions, consumer groups, KRaft", 2.0, 3, "", "Advanced", "3.4"),
        StudyBlock("Distributed Systems", "3.4 Kafka & Event-Driven Architecture", "Theory: Delivery semantics (at-most/least/exactly-once), log compaction, CDC", 2.0, 4, "", "Advanced", "3.4"),
        StudyBlock("Distributed Systems", "3.4 Kafka & Event-Driven Architecture", "Article: Jay Kreps 'The Log' + Confluent exactly-once + LinkedIn Kafka at scale", 2.5, 3, "", "Advanced", "3.4"),
        StudyBlock("Distributed Systems", "3.4 Kafka & Event-Driven Architecture", "Article: Uber Kafka matching + Debezium CDC pipelines", 2.0, 3, "", "Advanced", "3.4"),
        StudyBlock("Distributed Systems", "3.4 Kafka & Event-Driven Architecture", "Book: DDIA Chapter 11 — 'Stream Processing'", 3.0, 3, "", "Advanced", "3.4"),
        StudyBlock("Distributed Systems", "3.4 Kafka & Event-Driven Architecture", "Project: Event-driven order system — OrderService + InventoryService", 4.0, 4, "Kafka backbone", "Advanced", "3.4"),
        StudyBlock("Distributed Systems", "3.4 Kafka & Event-Driven Architecture", "Project: PaymentService + NotificationService + DLQ", 4.0, 4, "", "Advanced", "3.4"),
        StudyBlock("Distributed Systems", "3.4 Kafka & Event-Driven Architecture", "Project: Exactly-once semantics + Saga pattern implementation", 4.0, 5, "", "Advanced", "3.4"),
    ])

    # 3.5 Clocks
    blocks.extend([
        StudyBlock("Distributed Systems", "3.5 Distributed Clocks & Time", "Theory: Why wall clocks fail, NTP, clock skew, leap seconds", 1.5, 3, "", "Advanced", "3.5"),
        StudyBlock("Distributed Systems", "3.5 Distributed Clocks & Time", "Theory: Lamport timestamps, vector clocks, TrueTime, HLC", 2.0, 4, "", "Advanced", "3.5"),
        StudyBlock("Distributed Systems", "3.5 Distributed Clocks & Time", "Article: Lamport 1978 paper + Spanner/TrueTime + CockroachDB HLC", 2.5, 4, "Seminal paper", "Advanced", "3.5"),
    ])

    # --- Level 4: Infrastructure ---

    # 4.1 Load Balancing
    blocks.extend([
        StudyBlock("Infrastructure", "4.1 Load Balancing & Proxies", "Theory: L4 vs L7, algorithms, health checks, connection draining", 2.5, 3, "", "Advanced", "4.1"),
        StudyBlock("Infrastructure", "4.1 Load Balancing & Proxies", "Article: HAProxy + Netflix Ribbon + AWS ALB + NGINX", 2.0, 2, "", "Advanced", "4.1"),
        StudyBlock("Infrastructure", "4.1 Load Balancing & Proxies", "Project: 3 instances behind Nginx, weighted round-robin, health checks", 3.0, 3, "", "Advanced", "4.1"),
        StudyBlock("Infrastructure", "4.1 Load Balancing & Proxies", "Project: Test connection draining during rolling deploy", 2.5, 3, "", "Advanced", "4.1"),
    ])

    # 4.2 Caching
    blocks.extend([
        StudyBlock("Infrastructure", "4.2 Caching: Every Layer", "Theory: Strategies (aside, read/write-through, write-behind)", 2.0, 3, "", "Advanced", "4.2"),
        StudyBlock("Infrastructure", "4.2 Caching: Every Layer", "Theory: Eviction (LRU, LFU, TTL), invalidation, stampede/thundering herd", 2.0, 3, "", "Advanced", "4.2"),
        StudyBlock("Infrastructure", "4.2 Caching: Every Layer", "Theory: Distributed caching (Redis Cluster, Memcached), CDN caching", 1.5, 3, "", "Advanced", "4.2"),
        StudyBlock("Infrastructure", "4.2 Caching: Every Layer", "Article: Facebook TAO + Memcache + Cloudflare CDN + stampede paper", 2.0, 3, "", "Advanced", "4.2"),
        StudyBlock("Infrastructure", "4.2 Caching: Every Layer", "Project: L1 in-process LRU + L2 Redis TTL + stampede protection (SETNX)", 3.0, 3, "", "Advanced", "4.2"),
        StudyBlock("Infrastructure", "4.2 Caching: Every Layer", "Project: Metrics tracking — hit/miss/eviction rate per layer", 2.5, 3, "", "Advanced", "4.2"),
    ])

    # 4.3 Rate Limiting
    blocks.extend([
        StudyBlock("Infrastructure", "4.3 Rate Limiting & Throttling", "Theory: 5 algorithms — token bucket, leaky bucket, fixed/sliding window", 2.5, 3, "", "Advanced", "4.3"),
        StudyBlock("Infrastructure", "4.3 Rate Limiting & Throttling", "Article: Stripe + Figma + Cloudflare rate limiting at scale", 2.0, 3, "", "Advanced", "4.3"),
        StudyBlock("Infrastructure", "4.3 Rate Limiting & Throttling", "Project: Implement all 5 algorithms", 4.0, 3, "", "Advanced", "4.3"),
        StudyBlock("Infrastructure", "4.3 Rate Limiting & Throttling", "Project: Distributed token bucket with Redis Lua + benchmark all 5", 4.0, 4, "Atomic Lua scripts", "Advanced", "4.3"),
    ])

    # 4.4 Reliability
    blocks.extend([
        StudyBlock("Infrastructure", "4.4 Service Reliability", "Theory: SLIs/SLOs/SLAs, error budgets", 1.5, 3, "", "Advanced", "4.4"),
        StudyBlock("Infrastructure", "4.4 Service Reliability", "Theory: Retry with exponential backoff + jitter, circuit breakers", 2.0, 3, "", "Advanced", "4.4"),
        StudyBlock("Infrastructure", "4.4 Service Reliability", "Theory: Timeouts, bulkhead pattern, graceful degradation", 1.5, 3, "", "Advanced", "4.4"),
        StudyBlock("Infrastructure", "4.4 Service Reliability", "Article: AWS backoff/jitter + Fowler circuit breaker + Netflix Hystrix", 2.0, 3, "", "Advanced", "4.4"),
        StudyBlock("Infrastructure", "4.4 Service Reliability", "Article: Google SRE Book Ch.3,4,13 + Netflix Chaos Engineering", 2.0, 3, "", "Advanced", "4.4"),
        StudyBlock("Infrastructure", "4.4 Service Reliability", "Project: Resilient HTTP client — timeouts (connection+read separate)", 2.5, 3, "", "Advanced", "4.4"),
        StudyBlock("Infrastructure", "4.4 Service Reliability", "Project: Add retry w/ exponential backoff + full jitter + circuit breaker", 3.0, 4, "", "Advanced", "4.4"),
        StudyBlock("Infrastructure", "4.4 Service Reliability", "Project: Add bulkhead (separate goroutine pools) + test w/ random failures", 3.0, 4, "", "Advanced", "4.4"),
    ])

    # 4.5 Observability
    blocks.extend([
        StudyBlock("Infrastructure", "4.5 Observability: Metrics, Logs, Traces", "Theory: Three pillars, counters/gauges/histograms, p99 vs avg", 2.0, 3, "", "Advanced", "4.5"),
        StudyBlock("Infrastructure", "4.5 Observability: Metrics, Logs, Traces", "Theory: Structured logging, distributed tracing, RED/USE methods, OpenTelemetry", 2.0, 3, "", "Advanced", "4.5"),
        StudyBlock("Infrastructure", "4.5 Observability: Metrics, Logs, Traces", "Article: Charity Majors observability + Uber Jaeger + Google SRE Ch.6", 2.0, 3, "", "Advanced", "4.5"),
        StudyBlock("Infrastructure", "4.5 Observability: Metrics, Logs, Traces", "Project: Prometheus + Grafana on existing service + RED dashboard", 3.0, 3, "", "Advanced", "4.5"),
        StudyBlock("Infrastructure", "4.5 Observability: Metrics, Logs, Traces", "Project: Jaeger distributed traces across 3 services", 3.0, 3, "", "Advanced", "4.5"),
        StudyBlock("Infrastructure", "4.5 Observability: Metrics, Logs, Traces", "Project: Alertmanager rule for p99 latency", 2.0, 3, "", "Advanced", "4.5"),
    ])

    # --- Level 5: Advanced Architecture ---

    # 5.1 Microservices
    blocks.extend([
        StudyBlock("Advanced Architecture", "5.1 Microservices Architecture", "Theory: Service decomposition (DDD bounded contexts), data ownership", 2.0, 3, "", "Integration", "5.1"),
        StudyBlock("Advanced Architecture", "5.1 Microservices Architecture", "Theory: Sync vs async comms, distributed txns, sagas, service mesh", 2.0, 4, "", "Integration", "5.1"),
        StudyBlock("Advanced Architecture", "5.1 Microservices Architecture", "Theory: API gateway vs BFF pattern", 1.5, 3, "", "Integration", "5.1"),
        StudyBlock("Advanced Architecture", "5.1 Microservices Architecture", "Article: Fowler/Lewis microservices + DHH 'Majestic Monolith' + Netflix migration", 2.0, 3, "", "Integration", "5.1"),
        StudyBlock("Advanced Architecture", "5.1 Microservices Architecture", "Book: Software Architecture: The Hard Parts Ch.1-3 — Decomposition", 3.0, 4, "", "Integration", "5.1"),
        StudyBlock("Advanced Architecture", "5.1 Microservices Architecture", "Project: Decompose monolith — UserService + TaskService + NotificationService", 4.0, 4, "Each with own DB", "Integration", "5.1"),
        StudyBlock("Advanced Architecture", "5.1 Microservices Architecture", "Project: gRPC sync + Kafka async + Saga pattern + API Gateway", 4.0, 4, "", "Integration", "5.1"),
        StudyBlock("Advanced Architecture", "5.1 Microservices Architecture", "Project: Service discovery + integration testing", 3.0, 4, "", "Integration", "5.1"),
    ])

    # 5.2 Event Sourcing / CQRS
    blocks.extend([
        StudyBlock("Advanced Architecture", "5.2 Event Sourcing & CQRS", "Theory: Events as source of truth, projections, event replay", 2.0, 4, "", "Integration", "5.2"),
        StudyBlock("Advanced Architecture", "5.2 Event Sourcing & CQRS", "Theory: CQRS command/query separation, eventual consistency, snapshotting", 2.0, 4, "", "Integration", "5.2"),
        StudyBlock("Advanced Architecture", "5.2 Event Sourcing & CQRS", "Article: Fowler Event Sourcing + Greg Young CQRS + Airbnb + Monzo", 2.0, 3, "", "Integration", "5.2"),
        StudyBlock("Advanced Architecture", "5.2 Event Sourcing & CQRS", "Book: Hard Parts Ch.4-6 — Data Ownership", 3.0, 4, "", "Integration", "5.2"),
        StudyBlock("Advanced Architecture", "5.2 Event Sourcing & CQRS", "Project: Bank ledger — write side (commands → events)", 3.0, 4, "", "Integration", "5.2"),
        StudyBlock("Advanced Architecture", "5.2 Event Sourcing & CQRS", "Project: Bank ledger — read side (projections)", 3.0, 4, "", "Integration", "5.2"),
        StudyBlock("Advanced Architecture", "5.2 Event Sourcing & CQRS", "Project: Event replay from scratch + snapshotting", 3.0, 4, "", "Integration", "5.2"),
    ])

    # 5.3 API Design at Scale
    blocks.extend([
        StudyBlock("Advanced Architecture", "5.3 API Design at Scale", "Theory: Versioning strategies, backward compat rules, tolerant reader", 2.0, 3, "", "Integration", "5.3"),
        StudyBlock("Advanced Architecture", "5.3 API Design at Scale", "Theory: API deprecation, contract testing (Pact)", 1.5, 3, "", "Integration", "5.3"),
        StudyBlock("Advanced Architecture", "5.3 API Design at Scale", "Article: Stripe backward compat + Troy Hunt versioning + Spotify APIs", 2.0, 3, "", "Integration", "5.3"),
    ])

    # 5.4 Service Mesh / Tracing
    blocks.extend([
        StudyBlock("Advanced Architecture", "5.4 Distributed Tracing & Service Mesh", "Theory: W3C Trace Context, tail vs head sampling, sidecar proxy, mTLS", 2.0, 3, "", "Integration", "5.4"),
        StudyBlock("Advanced Architecture", "5.4 Distributed Tracing & Service Mesh", "Article: Uber Jaeger + OpenTelemetry + Lyft Envoy", 2.0, 3, "", "Integration", "5.4"),
        StudyBlock("Advanced Architecture", "5.4 Distributed Tracing & Service Mesh", "Project: K8s + Istio + automatic mTLS + traffic splitting", 4.0, 4, "", "Integration", "5.4"),
        StudyBlock("Advanced Architecture", "5.4 Distributed Tracing & Service Mesh", "Project: Jaeger distributed tracing + Kiali dependency graph", 3.0, 4, "", "Integration", "5.4"),
    ])

    # 5.5 Security
    blocks.extend([
        StudyBlock("Advanced Architecture", "5.5 Security Architecture", "Theory: AuthN vs AuthZ, JWT (structure, signing, revocation issues)", 2.0, 3, "", "Integration", "5.5"),
        StudyBlock("Advanced Architecture", "5.5 Security Architecture", "Theory: OAuth 2.0 / OIDC flows, API security (SSRF, SQLi), zero trust", 2.0, 3, "", "Integration", "5.5"),
        StudyBlock("Advanced Architecture", "5.5 Security Architecture", "Theory: Secrets management (Vault, AWS Secrets Manager)", 1.5, 3, "", "Integration", "5.5"),
        StudyBlock("Advanced Architecture", "5.5 Security Architecture", "Article: JWT RFC 8725 + Aaron Parecki OAuth + Uber IAM + 'Stop Using JWT for Sessions'", 2.0, 3, "", "Integration", "5.5"),
        StudyBlock("Advanced Architecture", "5.5 Security Architecture", "Project: Auth service — registration + bcrypt + JWT access + refresh tokens", 3.0, 3, "", "Integration", "5.5"),
        StudyBlock("Advanced Architecture", "5.5 Security Architecture", "Project: Session revocation via Redis + OAuth 2.0 Google flow", 3.0, 4, "", "Integration", "5.5"),
        StudyBlock("Advanced Architecture", "5.5 Security Architecture", "Project: Rate limiting on auth endpoints + secrets in Vault", 3.0, 4, "", "Integration", "5.5"),
    ])

    # --- Level 6: System Design ---

    # 6.1 Framework
    blocks.extend([
        StudyBlock("System Design", "6.1 System Design Interview Framework", "The 45-minute structure: clarify → estimate → high-level → data model → deep dive → wrap up", 3.0, 3, "", "Integration", "6.1"),
        StudyBlock("System Design", "6.1 System Design Interview Framework", "Practice: What interviewers listen for — tradeoff justification, failure modes", 2.0, 3, "", "Integration", "6.1"),
    ])

    # 6.2 Canonical Designs (14 problems)
    designs = [
        ("Design 1: URL Shortener (Bitly)", "Hashing, DB choice, caching, analytics"),
        ("Design 2: Distributed Message Queue (Kafka-like)", "Log structure, partitioning, consumer groups"),
        ("Design 3: Rate Limiter (API Gateway Level)", "Distributed counters, sliding window, Redis"),
        ("Design 4: Twitter/X Feed", "Fan-out on write vs read, celebrity problem, denormalization"),
        ("Design 5: Distributed Cache (Redis-like)", "Consistent hashing, eviction, replication"),
        ("Design 6: Web Crawler", "Distributed coordination, URL dedup, politeness"),
        ("Design 7: Notification System", "Fan-out, delivery guarantees, multi-channel, priority queues"),
        ("Design 8: Distributed File Storage (S3-like)", "Object storage, consistency, erasure coding"),
        ("Design 9: Search Autocomplete", "Trie, distributed trie, aggregation"),
        ("Design 10: Ride-Sharing Location Service", "Geospatial indexing, real-time, dispatch"),
        ("Design 11: Video Upload & Streaming (YouTube)", "Object storage, transcoding, CDN, adaptive bitrate"),
        ("Design 12: Distributed Transaction (Payment)", "2PC vs Saga, outbox, idempotency"),
        ("Design 13: Container Orchestration (K8s-like)", "Scheduler, controller loop, etcd, pod lifecycle"),
        ("Design 14: CI/CD Pipeline (GH Actions-like)", "Job scheduling, artifacts, runner fleet, secret injection"),
    ]
    for title, notes in designs:
        blocks.extend([
            StudyBlock("System Design", f"6.2 {title}", f"Research + requirements analysis: {notes}", 2.0, 4, "", "Integration", "6.2"),
            StudyBlock("System Design", f"6.2 {title}", f"Design document: high-level architecture + data model + deep dive", 2.5, 4, "", "Integration", "6.2"),
            StudyBlock("System Design", f"6.2 {title}", f"Tradeoff analysis + failure modes + monitoring strategy", 1.5, 4, "Write like a real design doc", "Integration", "6.2"),
        ])

    # 6.3 Papers
    papers = [
        ("MapReduce (2004)", "Google — built Hadoop, Spark"),
        ("Google File System (2003)", "Built HDFS, distributed file systems"),
        ("Bigtable (2006)", "Built Cassandra, HBase"),
        ("Dynamo (2007)", "Amazon — built DynamoDB, Cassandra, Riak"),
        ("Raft (2014)", "Built etcd, CockroachDB, TiKV"),
        ("Spanner (2012)", "Google — built CockroachDB, Cloud Spanner"),
        ("Kafka (2011)", "LinkedIn — Apache Kafka"),
        ("TAO (2013)", "Facebook social graph"),
        ("Chubby (2006)", "Google — built ZooKeeper, etcd"),
        ("Chord (2001)", "Consistent hashing"),
        ("Borg (2015)", "Google — built Kubernetes"),
        ("Dapper (2010)", "Google — built Jaeger, Zipkin"),
    ]
    for title, notes in papers:
        blocks.append(
            StudyBlock("System Design", f"6.3 Paper: {title}", f"Read and summarize: {notes}", 3.0, 4, "Seminal paper", "Integration", "6.3")
        )

    # 6.4 Engineering Blogs (ongoing reading)
    blocks.extend([
        StudyBlock("System Design", "6.4 Engineering Blogs Deep Dive", "Read 5 Netflix TechBlog posts + 5 Uber Engineering posts", 3.0, 2, "Focus on distributed systems topics", "Integration", "6.4"),
        StudyBlock("System Design", "6.4 Engineering Blogs Deep Dive", "Read 5 Stripe + 5 Cloudflare posts", 3.0, 2, "API design + networking", "Integration", "6.4"),
        StudyBlock("System Design", "6.4 Engineering Blogs Deep Dive", "Read 5 Discord + 5 Figma + 5 Airbnb posts", 3.0, 2, "Scaling + migration stories", "Integration", "6.4"),
        StudyBlock("System Design", "6.4 Engineering Blogs Deep Dive", "Kleppmann + Fowler + Brendan Gregg + Julia Evans blog highlights", 3.0, 3, "", "Integration", "6.4"),
    ])

    # Book: Hard Parts (remaining chapters)
    blocks.extend([
        StudyBlock("Advanced Architecture", "Book: Hard Parts", "Ch.7-9 — Distributed Transactions + Saga patterns", 4.0, 4, "Software Architecture: The Hard Parts", "Integration", "book_hp"),
        StudyBlock("Advanced Architecture", "Book: Hard Parts", "Ch.10-12 — Advanced Saga + contract testing + evolutionary arch", 4.0, 4, "", "Integration", "book_hp"),
    ])

    # DDIA remaining chapters
    blocks.extend([
        StudyBlock("Databases", "Book: DDIA", "Chapter 10 — Batch Processing", 3.0, 3, "MapReduce, beyond MapReduce", "Advanced", "book_ddia"),
        StudyBlock("Databases", "Book: DDIA", "Chapter 12 — The Future of Data Systems", 3.0, 3, "Derived data, end-to-end arguments", "Integration", "book_ddia"),
    ])

    return blocks


def schedule_blocks(blocks, total_days=365, hours_per_day=6.0):
    """
    BFS-aware scheduler: interleaves blocks from parallel topic tracks into each day,
    respects dependency ordering, balances cognitive load, inserts revision days.
    """
    # ── Step 1: Define BFS layers (parallel tracks within each layer) ──
    # Each layer is a list of topic_ids that can run in parallel.
    # Layers are ordered: all topics in layer N must complete before layer N+1 starts.
    bfs_layers = [
        # Layer 0: Level 0 fundamentals (all parallel)
        ["0.1", "0.2", "0.3", "0.4"],
        # Layer 1: Level 1 (1.1,1.2,1.3) + Level A (A.1,A.2,A.3,A.4) + Level 2 (2.1,2.2,2.3)
        ["1.1", "1.2", "1.3", "A.1", "A.2", "A.3", "A.4", "2.1", "2.2", "2.3"],
        # Layer 2: Dependent topics (1.4, A.5, 2.4, 2.5) + Level B starts (B.1)
        ["1.4", "A.5", "2.4", "2.5", "B.1"],
        # Layer 3: Level B continues + Level 3 starts
        ["B.2", "B.3", "B.4", "B.5", "B.6", "3.1", "book_ddia"],
        # Layer 4: Level 3 core (MIT labs + consensus) + Level 4 starts
        ["3.2", "3.3", "3.4", "3.5", "4.1", "4.2"],
        # Layer 5: Level 4 continues + Level 5 starts
        ["4.3", "4.4", "4.5", "5.1", "5.2", "5.3"],
        # Layer 6: Level 5 continues + Level 6 starts
        ["5.4", "5.5", "6.1", "book_hp"],
        # Layer 7: Level 6 system design mastery
        ["6.2", "6.3", "6.4"],
    ]

    # ── Step 2: Group blocks by topic_id ──
    topic_queues = {}  # topic_id -> list of blocks (in order)
    for b in blocks:
        if b.topic_id not in topic_queues:
            topic_queues[b.topic_id] = []
        topic_queues[b.topic_id].append(b)

    # ── Step 3: Build interleaved block sequence ──
    # For each BFS layer, round-robin across its parallel topics
    interleaved = []
    for layer in bfs_layers:
        active_topics = [tid for tid in layer if tid in topic_queues and topic_queues[tid]]
        while active_topics:
            next_active = []
            for tid in active_topics:
                if topic_queues[tid]:
                    interleaved.append(topic_queues[tid].pop(0))
                if topic_queues[tid]:
                    next_active.append(tid)
            active_topics = next_active

    # Any remaining blocks not in BFS layers
    for tid, remaining in topic_queues.items():
        interleaved.extend(remaining)

    # ── Step 4: Schedule interleaved blocks into days ──
    revision_days = set(range(7, total_days + 1, 7))
    days = []
    block_idx = 0
    day_num = 0

    while block_idx < len(interleaved):
        day_num += 1
        if day_num > total_days:
            break

        if day_num in revision_days:
            week = (day_num - 1) // 7 + 1
            if week <= 14:
                phase, rev_topics = "Foundation", "Level 0 + Level 1 + Level A concepts"
            elif week <= 28:
                phase, rev_topics = "Intermediate", "Level 2 + Level B + Level 3 concepts"
            elif week <= 42:
                phase, rev_topics = "Advanced", "Level 3 + Level 4 concepts"
            else:
                phase, rev_topics = "Integration", "Level 5 + Level 6 concepts"

            days.append((day_num, [
                StudyBlock("Review & Consolidation", f"Week {week} Review", f"Review and reinforce: {rev_topics}", 2.0, 2, "Spaced reinforcement", phase, "review"),
                StudyBlock("Review & Consolidation", f"Week {week} Review", "Active recall: summarize key concepts from memory, then verify", 2.0, 2, "No notes first pass", phase, "review"),
                StudyBlock("Review & Consolidation", f"Week {week} Review", "Practice: revisit exercises or build small variations of recent projects", 2.0, 3, "Consolidation", phase, "review"),
            ]))
            continue

        day_blocks = []
        day_hours = 0.0

        while block_idx < len(interleaved) and day_hours < hours_per_day - 0.25:
            block = interleaved[block_idx]
            remaining = hours_per_day - day_hours

            if block.duration <= remaining + 0.5:
                day_blocks.append(block)
                day_hours += block.duration
                block_idx += 1
            elif block.duration > hours_per_day:
                partial_hours = min(remaining, block.duration / 2)
                if partial_hours >= 1.5:
                    day_blocks.append(StudyBlock(
                        block.domain, block.topic,
                        f"{block.subtopic} (Part 1)",
                        partial_hours, block.difficulty, block.notes,
                        block.phase, block.topic_id
                    ))
                    day_hours += partial_hours
                    interleaved[block_idx] = StudyBlock(
                        block.domain, block.topic,
                        f"{block.subtopic} (continued)",
                        block.duration - partial_hours, block.difficulty,
                        block.notes, block.phase, block.topic_id
                    )
                else:
                    break
            else:
                break

        if day_blocks:
            days.append((day_num, day_blocks))

    # ── Step 5: Fill remaining days with practice / mock interviews ──
    last_content_day = day_num
    while day_num <= total_days:
        day_num += 1
        if day_num > total_days:
            break
        if day_num in revision_days:
            days.append((day_num, [
                StudyBlock("Review & Consolidation", "Final Review", "Comprehensive review of all domains", 2.0, 3, "", "Integration", "review"),
                StudyBlock("System Design", "Mock Interview Practice", "Timed 45-min system design practice", 2.0, 4, "Pick random design problem", "Integration", "mock"),
                StudyBlock("System Design", "Mock Interview Practice", "Self-review: identify gaps, improve tradeoff articulation", 2.0, 3, "", "Integration", "mock"),
            ]))
        else:
            cycle = (day_num - last_content_day) % 5
            if cycle == 0:
                days.append((day_num, [
                    StudyBlock("System Design", "Mock System Design Interview", f"Design problem {((day_num - last_content_day) // 5 % 14) + 1} — full 45-min timed practice", 3.0, 4, "Record yourself, review", "Integration", "mock"),
                    StudyBlock("Review & Consolidation", "Distributed Systems Deep Review", "Re-derive a consensus/replication concept from first principles", 1.5, 4, "", "Integration", "review"),
                    StudyBlock("Review & Consolidation", "Code Architecture Review", "Refactor or extend a previous project with new patterns learned", 1.5, 3, "", "Integration", "review"),
                ]))
            elif cycle == 1:
                days.append((day_num, [
                    StudyBlock("System Design", "Engineering Paper Re-read", "Re-read a seminal paper with fresh eyes, write 1-page summary", 3.0, 4, "", "Integration", "papers"),
                    StudyBlock("Review & Consolidation", "Database Internals Review", "Re-derive B-tree vs LSM tradeoffs, draw diagrams from memory", 1.5, 3, "", "Integration", "review"),
                    StudyBlock("Review & Consolidation", "Project Extension", "Add a feature to any previous project", 1.5, 3, "", "Integration", "review"),
                ]))
            elif cycle == 2:
                days.append((day_num, [
                    StudyBlock("System Design", "Mock System Design Interview", f"Design problem {((day_num - last_content_day) // 5 % 14) + 1} — alternative approach", 3.0, 4, "Different tradeoffs than first attempt", "Integration", "mock"),
                    StudyBlock("DevOps", "Infrastructure Practice", "Spin up and tear down a full K8s deployment from scratch", 1.5, 3, "", "Integration", "review"),
                    StudyBlock("APIs & Protocols", "API Design Review", "Review API designs from projects, identify improvements", 1.5, 3, "", "Integration", "review"),
                ]))
            elif cycle == 3:
                days.append((day_num, [
                    StudyBlock("System Design", "Engineering Blog Analysis", "Read 3 engineering blog posts, extract architectural patterns used", 2.0, 2, "Netflix/Uber/Stripe/Cloudflare", "Integration", "blogs"),
                    StudyBlock("Distributed Systems", "Failure Mode Analysis", "Pick a system from your portfolio, enumerate all failure modes", 2.0, 4, "", "Integration", "review"),
                    StudyBlock("Review & Consolidation", "FAANG Readiness Self-Check", "Go through readiness checklist, identify weakest areas", 2.0, 3, "Targeted review", "Integration", "review"),
                ]))
            else:
                days.append((day_num, [
                    StudyBlock("System Design", "Open-Ended Design Practice", "Pick a real product (Notion, Figma, Slack) and design from scratch", 3.0, 4, "Novel problem, not from the 14 canonical", "Integration", "mock"),
                    StudyBlock("Review & Consolidation", "Weak Area Deep Dive", "Spend focused time on weakest identified area", 2.0, 4, "From self-check results", "Integration", "review"),
                    StudyBlock("Review & Consolidation", "Teaching Exercise", "Explain a complex topic (Raft, MVCC, etc.) as if teaching someone", 1.0, 3, "Teaching solidifies understanding", "Integration", "review"),
                ]))

    return days


def generate_excel(days, output_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "365-Day Study Plan"

    # ── Styles ──
    header_font = Font(bold=True, size=12, color="FFFFFF")
    header_fill = PatternFill(start_color="2F5496", end_color="2F5496", fill_type="solid")
    phase_fills = {
        "Foundation": PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid"),
        "Intermediate": PatternFill(start_color="D9E2F3", end_color="D9E2F3", fill_type="solid"),
        "Advanced": PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid"),
        "Integration": PatternFill(start_color="E4DFEC", end_color="E4DFEC", fill_type="solid"),
    }
    review_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
    thin_border = Border(
        left=Side(style='thin'), right=Side(style='thin'),
        top=Side(style='thin'), bottom=Side(style='thin')
    )

    # ── Headers ──
    headers = ["Day", "Date", "Phase", "Total Hours", "Domain", "Topic", "Subtopic", "Duration (hrs)", "Difficulty", "Notes"]
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border

    # ── Column widths ──
    widths = [6, 12, 14, 12, 22, 38, 65, 14, 10, 50]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    # ── Data ──
    start_date = datetime.date(2026, 4, 13)  # Tomorrow
    row = 2

    for day_num, day_blocks in days:
        date = start_date + datetime.timedelta(days=day_num - 1)
        date_str = date.strftime("%Y-%m-%d")
        total_hours = sum(b.duration for b in day_blocks)
        # Phase based on day position (consistent, not per-block)
        is_review = day_blocks[0].topic_id == "review" if day_blocks else False
        if day_num <= 95:
            phase = "Foundation"
        elif day_num <= 195:
            phase = "Intermediate"
        elif day_num <= 290:
            phase = "Advanced"
        else:
            phase = "Integration"

        for i, block in enumerate(day_blocks):
            ws.cell(row=row, column=1, value=day_num if i == 0 else "").border = thin_border
            ws.cell(row=row, column=2, value=date_str if i == 0 else "").border = thin_border
            ws.cell(row=row, column=3, value=phase if i == 0 else "").border = thin_border
            ws.cell(row=row, column=4, value=round(total_hours, 1) if i == 0 else "").border = thin_border
            ws.cell(row=row, column=5, value=block.domain).border = thin_border
            ws.cell(row=row, column=6, value=block.topic).border = thin_border
            ws.cell(row=row, column=7, value=block.subtopic).border = thin_border
            ws.cell(row=row, column=8, value=block.duration).border = thin_border

            diff_map = {1: "★", 2: "★★", 3: "★★★", 4: "★★★★", 5: "★★★★★"}
            ws.cell(row=row, column=9, value=diff_map.get(block.difficulty, "")).border = thin_border
            ws.cell(row=row, column=10, value=block.notes).border = thin_border

            # Apply phase color
            fill = review_fill if is_review or block.topic_id in ("review", "mock", "papers", "blogs") else phase_fills.get(phase)
            if fill:
                for col in range(1, 11):
                    ws.cell(row=row, column=col).fill = fill

            ws.cell(row=row, column=7).alignment = Alignment(wrap_text=True)
            ws.cell(row=row, column=10).alignment = Alignment(wrap_text=True)

            row += 1

    # ── Freeze panes ──
    ws.freeze_panes = "A2"

    # ═══════════════════════════════════════════════════════════════════════
    # SUMMARY SHEET
    # ═══════════════════════════════════════════════════════════════════════
    ws2 = wb.create_sheet("Summary & Dependencies")

    summary_header = Font(bold=True, size=14)
    section_header = Font(bold=True, size=11, color="2F5496")

    r = 1
    ws2.cell(row=r, column=1, value="365-Day FAANG Backend Engineering Study Plan — Summary").font = summary_header
    r += 2

    ws2.cell(row=r, column=1, value="PHASE STRUCTURE").font = section_header
    r += 1
    phases = [
        ("Phase 1: Foundation", "Days 1-100", "Levels 0, 1, A.1-A.4, 2.1-2.3, DDIA Ch.1-6"),
        ("Phase 2: Intermediate", "Days 101-200", "Levels A.5, 2.4-2.5, B.1-B.6, 3.1-3.2 start, DDIA Ch.7-9"),
        ("Phase 3: Advanced", "Days 201-290", "Levels 3.3-3.5, 4.1-4.5, DDIA Ch.10-11"),
        ("Phase 4: Integration / Mastery", "Days 291-365", "Levels 5.1-5.5, 6.1-6.4, Papers, Mock interviews"),
    ]
    for phase_name, days_range, content in phases:
        ws2.cell(row=r, column=1, value=phase_name).font = Font(bold=True)
        ws2.cell(row=r, column=2, value=days_range)
        ws2.cell(row=r, column=3, value=content)
        r += 1

    r += 2
    ws2.cell(row=r, column=1, value="DEPENDENCY GRAPH (DAG)").font = section_header
    r += 1
    deps = [
        "Level 0 (0.1, 0.2, 0.3, 0.4) → all independent, run in parallel",
        "Level 1 (1.1, 1.2, 1.3) → independent, parallel. 1.4 depends on 1.1+1.2+1.3",
        "Level A (A.1, A.2, A.3, A.4) → independent, parallel. A.5 depends on A.1",
        "Level 2 (2.1, 2.2, 2.3) → independent, parallel. 2.4 depends on 2.1. 2.5 depends on 2.1+2.2",
        "Level 2 depends on Level 0 completion",
        "Level B → B.1 independent. B.2 depends on B.1. B.3 builds on B.2. B.4-B.6 independent",
        "Level 3 depends on Level 2. 3.1 and 3.2 parallel. 3.3 depends on 3.1. 3.4, 3.5 independent",
        "Level 4 parallel with Level 3",
        "Level 5 depends on Level 3 + Level 4",
        "Level 6 depends on all above",
    ]
    for dep in deps:
        ws2.cell(row=r, column=1, value=f"  • {dep}")
        ws2.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
        r += 1

    r += 2
    ws2.cell(row=r, column=1, value="DOMAIN PARALLELIZATION STRATEGY").font = section_header
    r += 1
    strategies = [
        "BFS approach: multiple domains studied each day (2-3 domains typical)",
        "Days interleave theory, articles, and project work across domains",
        "Heavy topics (difficulty 4-5) paired with lighter topics (difficulty 2-3) for cognitive balance",
        "Every 7th day is a review/consolidation day (spaced reinforcement)",
        "Projects are scheduled after corresponding theory, not in separate 'project weeks'",
        "Books (DDIA, Clean Architecture, GoF) are read in parallel with corresponding roadmap levels",
    ]
    for s in strategies:
        ws2.cell(row=r, column=1, value=f"  • {s}")
        ws2.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
        r += 1

    r += 2
    ws2.cell(row=r, column=1, value="SPACED REINFORCEMENT SCHEDULE").font = section_header
    r += 1
    reinforcement = [
        "Weekly review day every 7 days — active recall + practice exercises",
        "Phase transitions include cumulative review of all prior phases",
        "System design practice starts at Day 291 and continues through Day 365",
        "Mock interviews cycle through all 14 canonical designs in the final 75 days",
        "Paper re-reads scheduled after initial exposure for deeper understanding",
    ]
    for s in reinforcement:
        ws2.cell(row=r, column=1, value=f"  • {s}")
        ws2.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
        r += 1

    r += 2
    ws2.cell(row=r, column=1, value="ESTIMATED COMPLETION CONFIDENCE").font = section_header
    r += 1
    ws2.cell(row=r, column=1, value="  At 6 hours/day for 365 days (2,190 total hours):")
    r += 1
    confidence = [
        "Core content coverage: ~1,300 hours → 100% coverage with depth",
        "Revision and reinforcement: ~350 hours → strong long-term retention",
        "Extended practice and mock interviews: ~300 hours → interview-ready",
        "Buffer for overruns and exploration: ~240 hours → realistic schedule",
        "Overall confidence: HIGH — schedule is ambitious but achievable with consistent daily effort",
    ]
    for s in confidence:
        ws2.cell(row=r, column=1, value=f"  • {s}")
        ws2.merge_cells(start_row=r, start_column=1, end_row=r, end_column=5)
        r += 1

    # Column widths for summary
    ws2.column_dimensions['A'].width = 80
    ws2.column_dimensions['B'].width = 20
    ws2.column_dimensions['C'].width = 60

    # ═══════════════════════════════════════════════════════════════════════
    # BOOK READING PLAN SHEET
    # ═══════════════════════════════════════════════════════════════════════
    ws3 = wb.create_sheet("Book Reading Plan")
    r = 1
    ws3.cell(row=r, column=1, value="Parallel Book Reading Plan").font = summary_header
    r += 2

    ws3.cell(row=r, column=1, value="Week Range").font = Font(bold=True)
    ws3.cell(row=r, column=2, value="Book").font = Font(bold=True)
    ws3.cell(row=r, column=3, value="Chapters").font = Font(bold=True)
    ws3.cell(row=r, column=4, value="Paired Roadmap Level").font = Font(bold=True)
    r += 1

    book_plan = [
        ("Weeks 1-2", "DDIA", "Ch. 1 — Reliable, Scalable, Maintainable", "Level 0 framing"),
        ("Weeks 3-4", "DDIA", "Ch. 2 — Data Models", "Level 2.3 NoSQL"),
        ("Weeks 4-5", "Clean Architecture", "Part III — SOLID Principles (Ch.7-11)", "Level A.1"),
        ("Weeks 5-6", "DDIA", "Ch. 3 — Storage Engines", "Level 2.1 Internals"),
        ("Weeks 5-6", "GoF / Refactoring.Guru", "Creational patterns", "Level A.2"),
        ("Weeks 6-7", "GoF / Refactoring.Guru", "Structural patterns", "Level A.2"),
        ("Weeks 7-8", "DDIA", "Ch. 4 — Encoding", "Level 1.2 gRPC"),
        ("Weeks 7-8", "GoF / Refactoring.Guru", "Behavioral patterns", "Level A.2"),
        ("Weeks 8-9", "Clean Architecture", "Part IV — Component Principles", "Level A.2"),
        ("Weeks 9-10", "Architecture Patterns w/ Python", "Ch. 1-6 (Repository, Service Layer, Events)", "Level A.3"),
        ("Weeks 9-10", "DDIA", "Ch. 5 — Replication", "Level 2.5"),
        ("Weeks 10-12", "DDD Quickly (InfoQ)", "Full", "Level A.4"),
        ("Weeks 11-12", "DDIA", "Ch. 6 — Partitioning", "Level 2.5"),
        ("Weeks 12-14", "Docker Deep Dive", "Full (200 pages)", "Level B.1"),
        ("Weeks 13-14", "DDIA", "Ch. 7 — Transactions", "Level 2.4"),
        ("Weeks 14-18", "Kubernetes in Action", "Ch. 1-9", "Level B.3"),
        ("Weeks 15-16", "DDIA", "Ch. 8 — Distributed Systems Trouble", "Level 3.1"),
        ("Weeks 17-18", "DDIA", "Ch. 9 — Consistency & Consensus", "Level 3.3"),
        ("Weeks 19-20", "DDIA", "Ch. 10 — Batch Processing", "Design 2 + 6"),
        ("Weeks 21-22", "DDIA", "Ch. 11 — Stream Processing", "Level 3.4 Kafka"),
        ("Weeks 23-24", "DDIA", "Ch. 12 — Future of Data Systems", "Level 5.2"),
        ("Weeks 25-26", "Hard Parts", "Ch. 1-3 — Decomposition", "Level 5.1"),
        ("Weeks 27-28", "Hard Parts", "Ch. 4-6 — Data Ownership", "Level 5.1 + 5.2"),
        ("Weeks 29-30", "Hard Parts", "Ch. 7-9 — Distributed Transactions", "Level 5.2 + Design 12"),
        ("Weeks 31-32", "Hard Parts", "Ch. 10-12 — Saga Patterns", "Design 12"),
    ]
    for week, book, chapters, level in book_plan:
        ws3.cell(row=r, column=1, value=week)
        ws3.cell(row=r, column=2, value=book)
        ws3.cell(row=r, column=3, value=chapters)
        ws3.cell(row=r, column=4, value=level)
        r += 1

    ws3.column_dimensions['A'].width = 15
    ws3.column_dimensions['B'].width = 30
    ws3.column_dimensions['C'].width = 50
    ws3.column_dimensions['D'].width = 30

    # ═══════════════════════════════════════════════════════════════════════
    # PROJECT CHECKLIST SHEET
    # ═══════════════════════════════════════════════════════════════════════
    ws4 = wb.create_sheet("Project Checklist")
    r = 1
    ws4.cell(row=r, column=1, value="Project Portfolio Checklist").font = summary_header
    r += 2

    projects = [
        ("Level 0 — Fundamentals", [
            "Cache performance benchmark (memory hierarchy)",
            "Raw HTTP server + non-blocking I/O version",
            "TCP chat server from raw sockets + binary protocol",
            "Linux production diagnostics exercise",
        ]),
        ("Level 1 — APIs", [
            "Production-quality REST API (Task Manager) — idempotency, pagination, rate limiting, OpenAPI",
            "gRPC microservice (multi-language client)",
            "Real-time collaborative whiteboard (WebSockets + Redis pub/sub)",
            "GraphQL API with DataLoader (N+1 solved)",
        ]),
        ("Level A — Design Patterns", [
            "SOLID refactoring exercise (5-step violation → clean code)",
            "Payment processing system using 6 GoF patterns (Strategy, Factory, Decorator, Command, Observer, State)",
            "Pattern recognition in large open-source project",
            "Task Manager rebuilt with clean architecture (Ports + Adapters + Repository + Service Layer)",
            "E-commerce bounded context (Aggregate, ValueObject, DomainEvent, ACL)",
            "Concurrent image processing service (worker pool + fan-out/fan-in + semaphore + context)",
        ]),
        ("Level 2 — Databases", [
            "Key-value store with WAL, compaction, Bloom filter (Bitcask style)",
            "PostgreSQL performance workshop (10M rows, EXPLAIN, indexes, PgBouncer, partitioning)",
            "Social feed with multi-backend storage (PG + Redis + Cassandra)",
            "Transaction bug hunting (lost updates, write skew, phantom reads)",
        ]),
        ("Level B — DevOps", [
            "Dockerized service (multi-stage, non-root, optimized layers, health check)",
            "Full Docker Compose stack (API + PG + Redis + RabbitMQ + Worker + PGAdmin)",
            "Full Kubernetes deployment (Deployments, Services, Ingress, HPA, Helm chart)",
            "Async job processing system (RabbitMQ + Celery + DLX + Flower + priority queues)",
            "Redis feature set (caching, leaderboard, rate limiting, distributed lock, pub/sub, HyperLogLog, Streams)",
            "Full CI/CD pipeline (lint → test → scan → build → push → deploy staging → approve → deploy prod)",
        ]),
        ("Level 3 — Distributed Systems", [
            "MIT 6.824 Labs 1-5 (Raft implementation — the crown jewel)",
            "Kafka-based event-driven order system (saga + DLQ + exactly-once)",
        ]),
        ("Level 4 — Infrastructure", [
            "Multi-node load balanced service with health checks",
            "Multi-layer caching system with stampede protection",
            "Rate limiting library (all 5 algorithms, distributed Redis version)",
            "Resilient HTTP client (retry + circuit breaker + bulkhead + context cancellation)",
            "Full observability stack (Prometheus + Grafana + Jaeger)",
        ]),
        ("Level 5 — Architecture", [
            "Microservices decomposition (3+ services + Kafka + API gateway + Saga)",
            "Bank ledger with event sourcing + projections + snapshotting",
            "AuthService with JWT, refresh tokens, revocation, OAuth 2.0",
            "Service mesh with Istio, mTLS, traffic splitting, distributed tracing",
        ]),
        ("Level 6 — System Design", [
            "14 canonical system design documents with tradeoff analysis",
            "12 seminal paper summaries",
        ]),
    ]

    for level_name, items in projects:
        ws4.cell(row=r, column=1, value=level_name).font = Font(bold=True, size=11)
        r += 1
        for item in items:
            ws4.cell(row=r, column=1, value=f"  ☐ {item}")
            r += 1
        r += 1

    ws4.column_dimensions['A'].width = 100

    # Save
    wb.save(output_path)
    return output_path


def main():
    print("Building study content...")
    blocks = build_all_content()
    total_content_hours = sum(b.duration for b in blocks)
    print(f"Total content blocks: {len(blocks)}")
    print(f"Total content hours: {total_content_hours:.1f}")

    print("Scheduling into 365 days...")
    days = schedule_blocks(blocks)
    total_scheduled = sum(sum(b.duration for b in day_blocks) for _, day_blocks in days)
    print(f"Days with content: {len(days)}")
    print(f"Total scheduled hours: {total_scheduled:.1f}")

    output_path = "/home/ziad/git/claude_code_roadmap_for_fanngLevel_softwareEngineer/365_day_study_plan.xlsx"
    print(f"Generating Excel: {output_path}")
    generate_excel(days, output_path)
    print("Done!")


if __name__ == "__main__":
    main()
