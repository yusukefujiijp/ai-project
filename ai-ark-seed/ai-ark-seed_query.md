---
title: "AI Ark Seed Query"
canonical_name: "AI Ark Seed Query"
filename: "ai-ark-seed_query.md"
canonical_path: "ai-ark-seed/ai-ark-seed_query.md"
version: "v001-candidate"
date: "2026-08-08"
status: "review-ready candidate / pending Human content seal"
class: "prompt_query"
role: "repository-bound single-entry router, verifier, and activation query for AI Ark Seed"
language_policy: "Japanese-first / English-anchor"

repository:
  full_name: "yusukefujiijp/ai-project"
  ref: "main"

routes:
  COMPILE:
    runtime:
      path: "ai-ark-seed/ai-ark-seed-compile.md"
      version: "v001-candidate"
      class: "prompt_runtime"
    marker: "#COMPILE_ArkProjectSeed"

  PICKUP:
    runtime:
      path: "ai-ark-seed/ai-ark-seed-pickup.md"
      version: "v001-candidate"
      class: "prompt_runtime"
    marker: "#PICKUP_ArkProjectSeed"

  HOLD:
    runtime: null
---

# AI Ark Seed Query v001 Candidate

## 0. Purpose

> **AI Ark Seed Queryは、Humanが一つのEntryだけを指定し、Current Requestの意味からCOMPILE / PICKUP / HOLDを解決した後、必要な専門Runtimeだけを全文読了・検証して起動するSingle-Entry Routerである。**

```text
Human supplies one Entry.
Query binds.
Query resolves Route.
Only selected Runtime is loaded.
Dynamic Pair is verified.
Runtime governs.
Human retains meaning and authority.
```

QueryはCompile / Pickupの専門知性を所有しない。

---

## 1. Human Boot Surface

```yaml
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Query:
  ai-ark-seed/ai-ark-seed_query.md
```

推奨：

```text
上記Queryを最初から最後まで全文読み、
Current RequestからCOMPILE / PICKUP / HOLDを解決し、
選択されたRuntimeだけを全文読み、
Dynamic Pair Consistency Gateを通過した場合のみ実行してください。
```

---

## 2. Read Architecture

```text
Query Full Read
↓
Current Request Binding
↓
Route Resolution
↓
Selected Runtime Resolution
↓
Selected Runtime Full Read
↓
Dynamic Pair Verification
↓
Source / Seed Binding
↓
Execution
```

Core Rule:

> **Resolve First, Load Second.**

COMPILE時にPICKUP Runtimeを必須読込にしない。

PICKUP時にCOMPILE Runtimeを必須読込にしない。

---

## 3. Query Full-Read Proof

Beginning Identity:

```yaml
title: "AI Ark Seed Query"
filename: "ai-ark-seed_query.md"
canonical_path: "ai-ark-seed/ai-ark-seed_query.md"
version: "v001-candidate"
class: "prompt_query"
```

EOF:

```text
EOF::AI_ARK_SEED_QUERY::v001-candidate
```

`full_read: true`はBeginning Identity、Path、Version、Class、EOF Sentinel、未解決Truncationなしをすべて確認した場合のみ許可する。

---

## 4. Current Request Binding

```yaml
resolution_order:
  1: "Current explicit Human request"
  2: "Current Stop / Hold / Correction"
  3: "Explicit Route Marker"
  4: "Explicit Seed / Source"
  5: "Current Thread directly relevant context"
  6: "AI inference as Candidate only"
```

Humanに見えているContextを不要に再掲させない。

---

## 5. Route Resolution

### COMPILE

目的：

```text
Raw Discovery / Origin Context
→ Portable Seed
```

Strong signals:

```yaml
compile:
  - "Seed化して"
  - "一文Seedにして"
  - "このUnexpected SuccessをSeedにして"
  - "このConceptをユーザ辞書から一発で呼べる形にして"
  - "#COMPILE_ArkProjectSeed"
```

### PICKUP

目的：

```text
Existing Seed
→ Cardification-oriented Pickup
```

Strong signals:

```yaml
pickup:
  - "このSeedをPickupして"
  - "Seed Card化する価値があるのでPickupして"
  - "このSeedをSeed Card Candidateまで成熟させて"
  - "#PICKUP_ArkProjectSeed"
```

PICKUPはRepository保存を自動意味しない。

### HOLD

```yaml
hold:
  - "COMPILE / PICKUPをMaterialに区別できない"
  - "Target Seed / SourceがMaterialに不明"
  - "Stop / Holdが存在"
  - "Multiple targets conflict materially"
```

---

## 6. Route Signal Priority

```yaml
priority:
  1: "Stop / Hold / Material Correction"
  2: "Explicit Human operation"
  3: "Explicit Route Marker"
  4: "Semantic classification"
  5: "HOLD"
```

---

## 7. Selected Runtime

### COMPILE

```yaml
path: "ai-ark-seed/ai-ark-seed-compile.md"
version: "v001-candidate"
route: "COMPILE"
```

### PICKUP

```yaml
path: "ai-ark-seed/ai-ark-seed-pickup.md"
version: "v001-candidate"
route: "PICKUP"
```

HOLDではRuntimeを推測起動しない。

---

## 8. Dynamic Pair Consistency Gate

Route確定後、

```text
AI Ark Seed Query
+
Selected Runtime
=
Dynamic Pair
```

Required:

```yaml
dynamic_pair:
  - "Repository / Ref match"
  - "Query version matches"
  - "Selected Runtime version matches"
  - "Query route points to selected Runtime"
  - "Runtime points back to this Query"
  - "Route identity matches"
  - "Query class = prompt_query"
  - "Runtime class = prompt_runtime"
  - "Both EOF Sentinels verified"
  - "Status permits intended use"
```

States:

```yaml
READY:
  action: "Continue"

HOLD:
  action: "Do not load a Runtime by guess"

PARTIAL_READ:
  action: "Hard Stop"

EOF_SENTINEL_MISSING:
  action: "Hard Stop"

ROUTE_PAIR_MISMATCH:
  action: "Hard Stop"

STATUS_NOT_ACTIVE:
  action: "Stop"

PROTOCOL_UNREACHABLE:
  action: "Stop"
```

---

## 9. Persistence Boundary

Queryは保存判断を所有しない。

```text
Query
→ Route

Runtime
→ Operation

Human
→ Cardification / Seal authority
```

COMPILEはSeed生成へ。

PICKUPはCardification judgmentへ。

PersistenceはHuman-sealed Seed Cardに限定する。

---

## 10. Protocol Arrival

Heavy operation:

```yaml
protocol_arrival:
  repository:
    full_name:
    ref:

  query:
    full_read:
    eof_verified:

  route:
    resolved:
    reason:

  runtime:
    path:
    full_read:
    eof_verified:

  dynamic_pair:
    consistency:

  execution:
    state:
```

Compact form:

```text
protocol_arrival: READY
route: COMPILE | PICKUP
```

---

## 11. Do Not

```yaml
do_not:
  - "Do not load both Runtimes by default"
  - "Do not treat Query as Runtime intelligence"
  - "Do not infer missing Artifact from memory"
  - "Do not silently change Route"
  - "Do not silently fall back"
  - "Do not automatically save a Seed"
  - "Do not persist non-Cardified material"
```

---

## 12. Core Compression

```text
One Entry.
Bind Request.
Resolve Route.
Load only the selected Runtime.
Verify Dynamic Pair.
Execute bounded specialist intelligence.
```

document_end:
  filename: "ai-ark-seed_query.md"
  version: "v001-candidate"
  eof_sentinel: "EOF::AI_ARK_SEED_QUERY::v001-candidate"

EOF::AI_ARK_SEED_QUERY::v001-candidate
