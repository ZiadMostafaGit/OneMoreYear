# 🗺️ The Ziad ML Engineer Roadmap — v1

## From "Django backend engineer" → the engineer who can build, ship, and operate ML systems in production

> Same bones as the backend roadmap — Break→Diagnose→Theory→Rebuild→Measure→Write, numeric exit criteria, a spine project, exit exams, an honest timeline — retargeted at the full ML Engineer map, not just the infra slice. Your existing `dsa-professor`/`mock-interviewer`/`dsa-mastery-reference`/`faang-systems-cv-evaluator` skills still own DSA, interview simulation, and CV work — this document owns ML depth only, from math through production serving.
>
> **The honest starting condition:** you have zero stated prior exposure to linear algebra/calculus/ML theory, and real strength in Python, Postgres, Redis, Celery, Django, distributed-systems fundamentals, and — critically — a live production AI voice pipeline. That combination means **Levels 3–5 (MLOps, serving, ML system design) will feel like your native language and Levels 0–2 (math, classical ML, deep learning) will feel like starting over.** That's normal and it's the actual shape of the "backend engineer → ML engineer" transition — don't let the early levels feeling slow convince you you're bad at this; you're bad at the *new* 40%, and already strong at the *harder* 60%.

---

## I — The Three Laws (unchanged from the backend roadmap)

**Law 1 — Failure First.** Every topic opens with a broken model, a wrong prediction, a training run that diverges, or a serving endpoint that falls over — reproduced before it's explained.

**Law 2 — Measure Everything.** Every project ships numeric exit criteria — not "I trained a model," but "F1 went from 0.61 to 0.84, and here's the confusion matrix showing where the remaining error lives."

**Law 3 — Write It Down.** Every flagship project ships a design doc or teardown.

---

## II — The Learning Loop (unchanged)

```
1. 🔥 BREAK      Reproduce the failure yourself first.
2. 🔎 DIAGNOSE   Hypothesis before you check.
3. 📖 THEORY     Read to answer a question you're actively holding.
4. 🛠 REBUILD    Implement the fix, and the wrong fix, and prove why it's wrong.
5. 📈 MEASURE    Before/after numbers.
6. ✍️ WRITE      What broke, why, what the numbers said.
```

---

## III — The Spine Project: SENTRY

**One system, built across every level, tying directly into your real work:** a **fraud/anomaly detection system for payment approvals** — the ML counterpart to LEDGER-9, and something genuinely deployable at Logic Leap if it turns out well. SENTRY takes an approval/transaction event and scores it for anomalousness, starting with a classical model on hand-built features and ending as a full production ML system: trained, evaluated, served, monitored, and — at the final milestone — augmented with an LLM-based secondary check.

**Why this is the right spine:** it's the one project idea that legitimately requires all eight buckets from the original map — math (the model itself), classical ML (the actual anomaly detector, probably gradient boosting first), deep learning (a learned-embedding version later), MLOps (the pipeline that retrains and redeploys it), system design (the end-to-end architecture), and LLMs (the final augmentation layer). It also has real domain data available to you — transaction/approval patterns from work — though you'll build and train on a synthetic or public fraud dataset for the portfolio version, for obvious IP reasons.

### SENTRY Milestones

| Milestone | After Level | What you build |
|---|---|---|
| **S0** | 0 (Math/Python) | Feature engineering by hand, from raw transaction data, with the linear-algebra/stats groundwork to justify every feature |
| **S1** | 1 (Classical ML) | A gradient-boosted anomaly classifier, properly evaluated (not just accuracy — precision/recall tradeoffs matter enormously in fraud, since false positives block real approvals) |
| **S2** | 2 (Deep Learning) | A learned-embedding model (an autoencoder or a small transformer over transaction sequences) compared honestly against S1 — including the case where the simpler model wins |
| **S3** | 3 (MLOps) | The full production pipeline: feature store, training pipeline, model registry, drift monitoring, CI for model updates |
| **S4** | 4 (Serving) | A real-time serving endpoint with p99 latency budget (an approval can't wait 3 seconds for a fraud check), shadow-mode deployment, A/B rollout |
| **S5** | 5 (LLM layer) | An LLM-based secondary reviewer for borderline-scored cases — exactly the LEDGER-9 L8 milestone from the backend roadmap, now built out properly instead of as a stub |
| **S6** | 6 (Synthesis) | Full design doc, the classical-vs-deep-learning comparison written up honestly, and — if you want — a real proposal to your team for a lightweight version of this |

---

## IV — The Level Map

```
LEVEL 0 ──► LEVEL 1 ──► LEVEL 2 ──► LEVEL 3 ──► LEVEL 4 ──► LEVEL 5 ──► LEVEL 6
Math &      Classical   Deep        MLOps &     Production  LLMs &      Synthesis
Data        ML          Learning &  Pipelines   Serving     RAG/Agent   + ML System
Foundations             Transformers                        Infra       Design
```

| Level | Name | Spine milestone | Budget |
|---|---|---|---|
| **0** | Math, Stats & Data Foundations | S0 | 100–150h |
| **1** | Classical ML | S1 | 80–110h |
| **2** | Deep Learning & Transformers | S2 | 130–180h |
| **3** | MLOps: Pipelines, Registries & Monitoring | S3 | 80–110h |
| **4** | Production Serving (your natural strength) | S4 | 70–100h |
| **5** | LLMs, RAG & Agent Infrastructure | S5 | 70–100h |
| **6** | Synthesis: ML System Design + Portfolio | S6 | 50–80h |

**Total: ~580–830 hours.** Meaningfully less than the backend roadmap's 710–1,000, mostly because Levels 3–5 lean on skills you already have.

---

## V — The Curriculum

---

### LEVEL 0 — Math, Stats & Data Foundations

> **Goal:** stop treating models as black boxes that eat data and emit numbers. When a model does something surprising, you should be able to say whether it's a data problem, a math problem, or a code problem.
>
> **Budget:** 100–150h

#### 0.1 — Linear Algebra: the language every model is written in

> 🔥 **THE WALL — The Dimension Mismatch That Wasn't**
> Implement linear regression two ways: via the closed-form normal equation (`(XᵀX)⁻¹Xᵀy`) and via gradient descent, on the same small dataset. They should converge to the same answer. **Make them not agree** — introduce near-collinear features (two columns that are almost linear combinations of each other) and watch the normal equation blow up (numerically unstable matrix inversion) while gradient descent limps along but converges slowly. This is your first real encounter with **why regularization exists** — not as a buzzword, but as the fix for a problem you just caused yourself.

📖 **Theory:** vectors, matrices, matrix multiplication as a sequence of linear transformations (not just an operation — build the geometric intuition), eigenvalues/eigenvectors (what they mean: directions a transformation doesn't rotate, only scales — this is what PCA is built on), SVD (the decomposition underneath PCA, recommender systems, and dimensionality reduction generally), matrix rank and why near-collinearity breaks inversion, norms (L1 vs L2 — this is what separates Lasso from Ridge regression, and it's worth deriving why rather than memorizing).

📄 **Sources:** 3Blue1Brown's "Essence of Linear Algebra" (video series — build geometric intuition first, before the symbol manipulation) · "Mathematics for Machine Learning" (Deisenroth, Faisal, Ong — free PDF) Ch. 2–4 · Gilbert Strang's MIT 18.06 lectures if you want the full course.

🛠 **PROJECT — `linalg-from-scratch`**

Implement, using only NumPy's basic array operations (no `np.linalg.solve`, no `sklearn`): matrix multiply, matrix inverse via Gaussian elimination, eigendecomposition via the power iteration method, and PCA from raw SVD. Validate every one against NumPy's built-in versions.

📈 **Exit Criteria**
- [ ] Your matrix inverse matches `np.linalg.inv` to 6 decimal places on 10 random matrices, and you can explain why it *fails* on a near-singular one
- [ ] Your PCA implementation reduces a real dataset (e.g., MNIST, 784 dims) to 2D and the resulting plot visually separates digit classes — this is the "linear algebra is doing something real" moment
- [ ] Written: explain eigenvalues to someone who's never heard of them, using your PCA plot as the example

#### 0.2 — Calculus & Optimization: what backprop actually is

> 🔥 **THE WALL — Gradient Descent That Diverges**
> Implement gradient descent for a simple quadratic loss. Set the learning rate too high. Watch the loss explode instead of converge. Set it too low. Watch it crawl. Plot loss vs. iteration for five different learning rates on the same chart. **The shape of that chart — not a definition — is what "learning rate" actually means.**

📖 **Theory:** derivatives and partial derivatives as "how much does output change per unit change in this input," the chain rule (this **is** backpropagation — a neural network's backward pass is just the chain rule applied mechanically, layer by layer), gradient descent variants (SGD, momentum, Adam — know what problem each variant of the previous one was solving, not just the update rule), convexity (why some loss landscapes are easy and some aren't), and — the part people skip — **why loss landscapes for deep networks aren't convex and gradient descent still works anyway** (a genuinely open-ish area, but know the standard intuitions: saddle points vs. local minima, overparameterization helping).

📄 **Sources:** "Mathematics for Machine Learning" Ch. 5–7 · Karpathy's "The spelled-out intro to neural networks and backpropagation: building micrograd" (video + repo — build a tiny autograd engine by hand, this is the single best exercise for actually understanding backprop) · "Deep Learning" (Goodfellow, Bengio, Courville — free online) Ch. 4 (optimization).

🛠 **PROJECT — `micrograd-plus`** *(based directly on Karpathy's exercise, extended)*

Build a tiny scalar autograd engine (like Karpathy's `micrograd`) — a `Value` class that tracks operations and computes gradients via backprop through a computation graph. Then use it to train a tiny 2-layer neural network on a toy classification problem, with zero use of PyTorch/TensorFlow.

📈 **Exit Criteria**
- [ ] Your autograd engine's gradients match PyTorch's `autograd` to floating-point precision on 10 test expressions
- [ ] Your from-scratch network trains to >90% accuracy on a toy 2D classification dataset (two interleaving spirals, or similar), with a loss curve
- [ ] Written: explain backpropagation as "the chain rule, applied mechanically" with a worked example from your own code

#### 0.3 — Probability & Statistics for ML

> 🔥 **THE WALL — The Confident Wrong Model**
> Train a classifier on an imbalanced dataset (95% class A, 5% class B — like real fraud data). Report accuracy. It'll be ~95%, and the model will be predicting "class A" for everything, catching **zero** of the actual fraud cases. **This is the single most important lesson in applied ML for any domain involving rare events**, and accuracy as a metric is actively lying to you here.

📖 **Theory:** distributions (know Normal, Bernoulli, Binomial, Poisson by shape and by when each shows up), Bayes' theorem (not just the formula — the intuition: how a prior belief updates given evidence, and why this underlies everything from spam filters to medical testing to your fraud detector), expectation and variance, the bias-variance tradeoff (the single most-tested ML theory concept, and the direct explanation for why your S1 model will need tuning), hypothesis testing and p-values (know what they do and don't mean — this is a widely-misunderstood area even among practitioners), MLE (maximum likelihood estimation — the framework underneath most classical model training, including logistic regression), and the precision/recall/F1/ROC-AUC family, which the Wall above should make concrete rather than abstract.

📄 **Sources:** "Mathematics for Machine Learning" Ch. 6 · "Practical Statistics for Data Scientists" (Bruce & Bruce) — pragmatic and example-driven · StatQuest (Josh Starmer) YouTube series on Bayes, ROC/AUC, and bias-variance — genuinely the clearest free explanations that exist for these specific topics.

🛠 **PROJECT — `imbalance-lab`** (feeds SENTRY milestone S0)

Take a real imbalanced dataset (a public fraud/credit-card dataset works well as a stand-in). Report accuracy first (the trap). Then build the correct evaluation: precision/recall curves, ROC-AUC, and — critically for your fraud-detection domain — a cost-weighted metric (false positives block a real approval, false negatives let fraud through; these costs are not equal, and your metric should say so explicitly).

📈 **Exit Criteria**
- [ ] Demonstrate the "95% accuracy, 0% recall" trap explicitly, with the confusion matrix
- [ ] A precision-recall curve and a justified operating threshold, with the cost tradeoff stated in dollars-or-equivalent, not just "we chose 0.5"
- [ ] Written: why accuracy is close to useless for this class of problem, aimed at a hypothetical product manager who wants "just tell me the accuracy"

---

### LEVEL 1 — Classical ML

> **Goal:** the toolkit that solves most real business ML problems, done properly — not just `.fit()` and `.predict()`.
>
> **Spine milestone:** S1 · **Budget:** 80–110h

#### 1.1 — Regression, Classification & the Bias-Variance Tradeoff, in Practice

> 🔥 **THE WALL — The Model That Memorized**
> Train a decision tree with no depth limit on a dataset. Training accuracy: 100%. Test accuracy: mediocre. **You've built a lookup table, not a model.** Then constrain depth, add pruning, and watch the gap close — while training accuracy drops. This is overfitting made undeniable rather than theoretical.

📖 **Theory:** linear/logistic regression (and why logistic regression is really MLE under a Bernoulli assumption — ties back to 0.3), decision trees (splitting criteria: Gini vs entropy), random forests (bagging — why averaging many overfit trees produces a well-generalizing ensemble, a genuinely elegant idea worth understanding deeply, not just using), **gradient boosting** (XGBoost/LightGBM — the actual workhorse of most production tabular-data ML, including fraud detection; understand boosting as "each new tree fixes the previous ensemble's residual errors"), clustering (k-means, and its real limitation: it assumes spherical, similarly-sized clusters, which real data rarely gives you), cross-validation (why a single train/test split lies to you), and regularization (L1/Lasso for sparsity, L2/Ridge for shrinkage — tie back to 0.1's near-collinearity Wall).

📄 **Sources:** "An Introduction to Statistical Learning" (James, Witten, Hastie, Tibshirani — free PDF, the standard, very readable text) · "Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow" (Géron) Part I · the XGBoost paper ("XGBoost: A Scalable Tree Boosting System") — short, clear, and explains real engineering decisions (sparsity-aware splitting, approximate algorithms for scale) that a pure-theory source won't cover.

🛠 **PROJECT — SENTRY S1: the gradient-boosted anomaly detector**

Build the first real version of SENTRY: feature-engineer a transaction dataset (amount, timing, frequency, approver-relationship features — the kind of thing you'd actually derive from an approval-chain schema), train logistic regression, random forest, and XGBoost as three comparison points, and properly tune with cross-validation.

📈 **Exit Criteria**
- [ ] A model comparison table: precision/recall/F1/ROC-AUC for all three approaches, at a threshold chosen via the cost-weighted analysis from 0.3
- [ ] Feature importance analysis (XGBoost's built-in importance, plus SHAP values for at least the top 5 features) — and a written explanation of *why* the top features make domain sense, not just that they scored high
- [ ] A deliberately overfit version (max depth, no regularization) shown side-by-side with the tuned version — the train/test gap, quantified
- [ ] This becomes your baseline: every later SENTRY milestone must beat it or explain why it doesn't

---

### LEVEL 2 — Deep Learning & Transformers

> **Goal:** understand what's actually happening inside a neural network and a transformer, not just how to call `.fit()` on one.
>
> **Spine milestone:** S2 · **Budget:** 130–180h

#### 2.1 — Neural Network Fundamentals

> 🔥 **THE WALL — Vanishing Into Nothing**
> Build a deep (8+ layer) feedforward network with sigmoid activations and no normalization. Train it. Watch the loss barely move — the gradients vanish to near-zero by the time backprop reaches the early layers. Then swap in ReLU and add batch normalization. Watch it actually train. **You've just felt, not read about, the vanishing gradient problem** and the two most common fixes.

📖 **Theory:** layers, weights, activation functions (sigmoid/tanh/ReLU/GELU — and precisely why ReLU family won: it doesn't saturate, so gradients don't vanish), backpropagation as a direct extension of your `micrograd-plus` engine to matrices/tensors, weight initialization (why random-but-scaled matters — Xavier/He initialization), batch normalization and why it stabilizes training, dropout as regularization for neural nets (the neural-net analog of decision-tree pruning from Level 1), and the practical training loop: batches, epochs, learning rate schedules.

🛠 **PROJECT — `nn-from-scratch-to-pytorch`**

Extend `micrograd-plus` into a small tensor-based framework (or move to raw PyTorch tensors with `autograd` disabled and implement backprop by hand once more, at the matrix level this time) for a feedforward network on a real dataset (MNIST is fine — the point is the mechanics, not novelty). Then reproduce the vanishing-gradient Wall and its fixes explicitly, with loss curves for each configuration.

📈 **Exit Criteria**
- [ ] Four loss curves on one chart: sigmoid/no-norm, sigmoid/with-BN, ReLU/no-norm, ReLU/with-BN — the difference should be visually undeniable
- [ ] Your hand-rolled backprop matches PyTorch's `autograd` gradients to floating point precision
- [ ] Written: explain vanishing gradients and batch norm to someone who understands 0.2's chain-rule material but nothing else

#### 2.2 — Transformers & Attention: the architecture underneath every LLM

> 🔥 **THE WALL — The Order-Blind Model**
> Build a minimal self-attention layer. Feed it a sentence, then feed it the same words shuffled. Without positional encoding, **it produces the same output** — attention alone has no notion of word order, which is deeply counterintuitive if you've only read the "attention is all you need" summary. Add positional encoding. Watch the outputs diverge appropriately.

📖 **Theory:** the attention mechanism precisely (queries, keys, values — and the actual intuition: "for each token, how much should I weight every other token's information") — build this from the matrix operations up, not from a diagram; multi-head attention (why multiple heads instead of one bigger one — different heads learn different relationship types); positional encoding (sinusoidal vs. learned vs. rotary/RoPE, which is what most modern LLMs actually use); the encoder-decoder split, and why decoder-only architectures (GPT-family) won for generative LLMs specifically; layer norm placement (pre-norm vs post-norm) as a training-stability detail that matters more than it sounds.

📄 **Sources:** "Attention Is All You Need" (Vaswani et al., 2017) — read the original paper now that you have the math background for it · Karpathy's "Let's build GPT: from scratch, in code, spelled out" (video + `nanoGPT` repo — the best hands-on transformer-from-scratch resource that exists, and a direct continuation of the `micrograd` lineage) · Jay Alammar's "The Illustrated Transformer" for the visual intuition layer, read alongside the paper, not instead of it.

🛠 **FLAGSHIP PROJECT — `gpt-from-scratch`** *(based on Karpathy's nanoGPT exercise)*

Build a small decoder-only transformer from scratch (attention, positional encoding, feedforward blocks, layer norm — all hand-implemented in PyTorch, no `nn.MultiheadAttention` shortcut) and train it on a small text corpus to do character-level next-token prediction.

📈 **Exit Criteria**
- [ ] The model generates plausible-looking (not necessarily coherent) text after training — screenshot a sample
- [ ] The order-blindness demonstration from the Wall, shown explicitly with and without positional encoding
- [ ] You can draw the full architecture (embedding → positional encoding → N transformer blocks → output projection) from memory and explain each box
- [ ] Written: "attention, explained to someone who understands matrix multiplication but has never heard of a transformer" — this single explanation is one of the highest-value things you can have ready for an interview

#### 2.3 — SENTRY S2: does deep learning actually help here?

Build a learned-embedding approach to fraud detection — either an autoencoder (train it to reconstruct normal transactions; anomalies reconstruct poorly) or a small transformer over sequences of a user's transaction history. Compare it honestly against your S1 gradient-boosted baseline.

📈 **Exit Criteria**
- [ ] Head-to-head comparison table against S1: precision/recall/F1/AUC, plus training time and inference latency
- [ ] **An honest verdict, argued with the numbers**, on whether the deep-learning approach is actually better for this problem — tabular fraud data is a domain where gradient boosting frequently *beats* deep learning, and discovering and stating that yourself, with evidence, is a stronger signal than blindly reaching for the trendier tool
- [ ] Written: when would you actually recommend the deep model over XGBoost here, and why

---

### LEVEL 3 — MLOps: Pipelines, Registries & Monitoring

> **Goal:** everything that turns a Jupyter notebook into a system. This is where your backend engineering strength stops being "adjacent" and starts being directly load-bearing.
>
> **Spine milestone:** S3 · **Budget:** 80–110h

#### 3.1 — Experiment Tracking & Reproducibility

> 🔥 **THE WALL — The Unreproducible Model**
> Train a model. Get a good result. Try to reproduce it a week later with "the same" code. **You can't** — a random seed wasn't fixed, a data preprocessing step changed silently, or a dependency version drifted. This happens to every ML team that doesn't invest in tracking, and it's a genuinely common, genuinely embarrassing production incident.

📖 **Theory:** experiment tracking (MLflow or Weights & Biases — log every hyperparameter, metric, and artifact, not just the final number), reproducibility (seed everything, pin dependency versions, version your data — not just your code), feature stores (Feast/Tecton — the problem they solve: training-serving skew, where the features computed at training time subtly differ from the features computed at serving time, which is a real and common source of silent production degradation), model registries (versioning trained models with metadata, not just filenames).

🛠 **PROJECT — SENTRY S3: the pipeline**

Wrap SENTRY's training in a fully tracked, reproducible pipeline: MLflow experiment tracking for every run, a feature store (even a simple one) ensuring the exact same feature computation runs at training and serving time, a model registry with versioning, and an orchestrated retraining pipeline (Airflow or Prefect) that can be triggered on a schedule or on data drift.

📈 **Exit Criteria**
- [ ] Re-running the exact same tracked experiment produces bit-identical metrics — proven
- [ ] A deliberately-introduced training-serving skew (compute a feature slightly differently at serving time) is caught by a test, not discovered in production
- [ ] A full retraining run triggered end-to-end from the orchestrator, registering a new model version automatically

#### 3.2 — Monitoring & Data/Model Drift

> 🔥 **THE WALL — The Model That Quietly Died**
> Deploy a model. Feed it a data distribution that gradually shifts from what it was trained on (simulate this — e.g., transaction amounts slowly trending upward over months). **Accuracy silently degrades and nothing alerts you**, because nothing is watching for it. This is one of the most common real-world ML production failures, and it's invisible without explicit monitoring.

📖 **Theory:** data drift vs. concept drift (the input distribution changing vs. the input-output relationship changing — different problems, different fixes), detection methods (population stability index, KL divergence, or a tool like Evidently), the monitoring metrics that matter for a production model (prediction distribution, feature distributions, and — where you have it — actual outcome-based accuracy with a lag), alerting thresholds and the same alert-fatigue concerns from general SRE work.

🛠 **PROJECT — extend SENTRY S3 with drift monitoring**

📈 **Exit Criteria:** the simulated drift from the Wall is detected and alerted on before accuracy visibly degrades in your evaluation metrics — i.e., the drift detector fires *earlier* than a naive accuracy-monitoring approach would.

---

### LEVEL 4 — Production Serving

> **Goal:** this is your natural territory — everything here maps onto distributed-systems, caching, and reliability skills you already have. The job is translation, not new theory.
>
> **Spine milestone:** S4 · **Budget:** 70–100h

#### 4.1 — Serving Architecture & Latency Budgets

> 🔥 **THE WALL — The Model That Blocks the Approval**
> Wire SENTRY's model into a synchronous call path: an approval request waits on the fraud score before proceeding. Load test it. At even modest concurrency, **the fraud check becomes your system's bottleneck** — model inference isn't free, and a synchronous ML call in a hot path behaves exactly like the slow-dependency problems you already know how to diagnose from your backend work, just with a different box drawn on the diagram.

📖 **Theory:** this is almost entirely a re-application of Level 4 from your backend roadmap — timeouts, circuit breakers, fallback behavior (score everything as "needs review" if the model is down, don't block the approval entirely), caching (identical/near-identical requests don't need re-scoring), and the specific serving patterns: FastAPI/Flask for a model endpoint, batching requests where latency budget allows, and the sync-vs-async serving decision (does the approval wait for the score, or does scoring happen async with the approval proceeding provisionally and flagged for review if the score comes back bad?). **This is the level where you should feel your backend-engineering advantage most directly — resist the urge to relearn things you already know under new names.**

🛠 **PROJECT — SENTRY S4: real-time serving**

Deploy SENTRY as a FastAPI endpoint with a defined p99 latency budget, a circuit breaker + fallback (provisional-approve-and-flag) when the model is slow/down, shadow-mode deployment (score every real approval silently, compare against the eventual outcome, without affecting the actual decision — the standard safe way to validate a new model in production before trusting it), and a canary rollout path for new model versions.

📈 **Exit Criteria**
- [ ] p99 latency measured and held under budget at realistic concurrency
- [ ] Circuit-breaker fallback proven: kill the model server, approvals still proceed (flagged for review), zero approvals blocked
- [ ] Shadow-mode comparison: SENTRY's silent scores vs. eventual known outcomes, with precision/recall computed from real (simulated) shadow traffic
- [ ] Written: the deployment runbook for rolling out a new SENTRY model version safely

---

### LEVEL 5 — LLMs, RAG & Agent Infrastructure

> **Goal:** the 2026-relevant layer, and — given your production AI voice-pipeline experience — another place where you're extending real intuition rather than starting cold.
>
> **Spine milestone:** S5 · **Budget:** 70–100h

#### 5.1 — Prompting, Embeddings & RAG

> 🔥 **THE WALL — The Confidently Wrong Answer**
> Ask an LLM a question about a borderline fraud case with specifics it can't know (your actual transaction history, your actual approval policy). It will **confidently make something up.** This is the concrete, felt version of "hallucination," and it's the reason RAG exists — not as a buzzword, but as the direct fix: give the model the actual relevant context instead of relying on what it memorized during training.

📖 **Theory:** embeddings (what they are geometrically — points in a high-dimensional space where distance means semantic similarity, tying directly back to your Level 0 linear-algebra work), vector search (this is v3's HNSW content from the backend roadmap — build or use it), the RAG pipeline (retrieve relevant context → construct a prompt → generate), chunking strategies and their measurable effect on retrieval quality, fine-tuning vs. RAG vs. prompting as three different tools for three different problems (know when each is the right call — fine-tuning for style/format, RAG for facts/freshness, prompting for everything else first).

🛠 **PROJECT — SENTRY S5: the LLM secondary reviewer**

For transactions SENTRY's classical/deep models flag as borderline (not clearly fraud, not clearly clean), build an LLM-based reviewer: it receives the transaction, relevant policy documents (via RAG over a small policy corpus), and the approval history, and produces a structured recommendation with reasoning. Wire this in as a durable, retryable, timeout-bounded step — exactly like LEDGER-9's L8 milestone from the backend roadmap, now built out for real instead of as a stub.

📈 **Exit Criteria**
- [ ] The RAG retrieval step measurably improves recommendation quality vs. no-context prompting, on a small evaluation set you build by hand
- [ ] Token-aware cost tracking per review, and a per-case cost ceiling
- [ ] Timeout + fallback to human review if the LLM step fails or exceeds budget
- [ ] A golden evaluation set (even 30–50 hand-labeled borderline cases) that regression-tests any prompt or model change — **shipping a prompt change without this is shipping untested code**, exactly as flagged in the backend roadmap's agent-infra section

---

### LEVEL 6 — Synthesis: ML System Design + Portfolio

> **Budget:** 50–80h

#### 6.1 — ML System Design (the interview-specific skill)

Practice designing, end-to-end, with the same rigor as the backend roadmap's design-doc template: a recommendation system, a search-ranking system, a content-moderation/anomaly-detection system (you have the real answer here now), a fraud-detection system at scale (same), and — the 2026-relevant one — an LLM-powered feature (RAG-based support bot, or similar). For each: data pipeline, feature engineering, model choice and why, training cadence, serving architecture, monitoring, and the honest failure modes.

Route each through a `mock-interviewer` session once the doc is written — same coordination pattern as the backend roadmap.

#### 6.2 — The SENTRY Teardown

The capstone write-up: architecture diagram, the classical-vs-deep-learning verdict from Level 2 (with numbers), the production-serving numbers from Level 4, the RAG-augmentation results from Level 5, and — the section that makes this genuinely rare — an honest comparison of what it would take to actually propose a lightweight version of this to your team at Logic Leap, given real constraints (data availability, latency budget, false-positive tolerance for a live approval flow).

---

## VI — The Honest Timeline

| Level | Hours |
|---|---|
| 0 — Math/Stats/Data | 100–150 |
| 1 — Classical ML | 80–110 |
| 2 — Deep Learning/Transformers | 130–180 |
| 3 — MLOps | 80–110 |
| 4 — Serving | 70–100 |
| 5 — LLMs/RAG | 70–100 |
| 6 — Synthesis | 50–80 |
| **Total** | **580–830 hours** |

At 12–15h/week: **roughly 10–14 months.** Meaningfully shorter than the backend roadmap, and there's a real question worth sitting with rather than me answering for you: **do you run this in parallel with the backend roadmap, sequentially after it, or do you actually need to pick one as primary?** Running both at full intensity simultaneously is close to 1,300–1,800 combined hours — over two years at your stated pace either way. Worth deciding deliberately rather than defaulting into both at once.

---

## VII — The Library

| Resource | Level | Why |
|---|---|---|
| **"Mathematics for Machine Learning"** (free PDF) | 0 | The math foundation, ML-specific rather than generic |
| **3Blue1Brown "Essence of Linear Algebra" + "Neural Networks" series** | 0, 2 | Best geometric intuition available, free |
| **Karpathy's "micrograd" and "nanoGPT" series** | 0, 2 | The single best hands-on path from "backprop is a formula" to "I built a GPT" |
| **"An Introduction to Statistical Learning"** (free PDF) | 1 | The standard, readable classical-ML text |
| **"Attention Is All You Need"** | 2 | Read it once you have the math to actually parse it |
| **"Designing Machine Learning Systems"** — Chip Huyen | 3, 4, 6 | The best production-ML-systems book |
| **"AI Engineering"** — Chip Huyen | 5 | The systems view of building with LLMs, same as flagged in the backend roadmap |
| **vLLM's PagedAttention paper** | 5 | Carried over from the backend roadmap's AI-infra level — same content, now with the ML theory underneath it too |

---

## Closing

The honest shape of this roadmap: Levels 0–2 are a real, unavoidable investment where your backend background gives you no head start — budget for that emotionally, not just on the calendar. Levels 3–6 are where the investment starts paying interest, because caching, reliability, latency budgets, and system design are the same skills you already have, aimed at a new kind of dependency. SENTRY is built to make that payoff concrete: by S4, you're not learning ML *or* backend engineering, you're doing both at once on one real system, and that's the actual target state — not "an ML engineer" and not "a backend engineer," but the specific, valuable, less-common combination of both.
