---
title: "AI Ark Seed"
filename: "README.md"
canonical_path: "ai-ark-seed/README.md"
version: "v001-candidate"
date: "2026-08-08"
status: "human-sealed field-test candidate / not canonical"
class: "subsystem_front_door"
language_policy: "Japanese-first / English-anchor"
---

# AI Ark Seed

## 0. 一文定義

> **AI Ark Seedは、Ark Project内で生まれる軽量Seedを一つのQueryから扱い、Seed Card化する価値があるものだけをPickupしてContext・Evidence・Next Gateを備えたMarkdown Seed Cardへ成熟させ、Human Seal後に選択的永続保存するHuman–AI Seed Lifecycle Subsystemである。**

```text
Detect broadly.
Keep Seeds lightweight.
Pickup selectively.
Cardify selectively.
Persist only Cardified Seeds.
```

---

## 1. Architecture

```text
ai-ark-seed/
├─ README.md
├─ ai-ark-seed_query.md
├─ ai-ark-seed-compile.md
├─ ai-ark-seed-pickup.md
│
└─ ai-ark-seed-cards/
   ├─ README.md
   └─ <seed-card>.md
```

Humanが覚える入口は原則一つ。

```yaml
Repository:
  yusukefujiijp/ai-project

Ref:
  main

Query:
  ai-ark-seed/ai-ark-seed_query.md
```

---

## 2. Core Object Model

### 2.1 Seed

Seedは軽量Semantic Unitである。

Default portable form:

```text
"Name(Definition)"
```

SeedはRepositoryに保存されていなくてもSeedである。

SeedはHumanのユーザ辞書、Current Thread、Handoff、その他のHuman-managed Contextに存在できる。

### 2.2 Seed Card

Seed Cardは、Seed Card化する価値があると判断されたSeedを、Future Human / AIが再起動・検証・成熟できるようにしたPersistent Knowledge Objectである。

```text
Seed Card
│
├─ Card Summary
│  ├─ Status
│  ├─ Origin
│  ├─ Seed String / 一文定義
│  ├─ Core Compression
│  └─ Guard
│
├─ Context
│  ├─ Source
│  ├─ Origin Context
│  ├─ Causal Spine
│  └─ Why It Matters
│
├─ Evidence
│
└─ Next Gate
```

---

## 3. Core Boundary

```text
Seed
≠ Seed Card

Compile
≠ Persist

Pickup
≠ Automatic Persist

Cardified Seed
= Eligible for Persistence
```

Core Guard:

> **No Cardification, No Persistence.**

---

## 4. Lifecycle

### DiscoveryからSeedへ

```text
Discovery
↓
COMPILE
↓
Seed
```

### SeedからSeed Cardへ

```text
Seed
↓
Worth Pickup?
├─ No → Keep local / context only
└─ Yes
    ↓
   PICKUP
    ↓
 Cardification Review
    ├─ HOLD / DROP → Do not persist
    └─ CARDIFY
         ↓
     Seed Card Candidate
         ↓
      Human Seal
         ↓
       Persist
         ↓
 ai-ark-seed-cards/
```

---

## 5. Responsibility

```yaml
responsibility:
  query:
    owns:
      - "Repository binding"
      - "Current Request binding"
      - "COMPILE / PICKUP / HOLD route resolution"
      - "Selected Runtime resolution"
      - "Full-Read Proof"
      - "Dynamic Pair Consistency"
      - "Activation"

  compile_runtime:
    owns:
      - "Raw Discovery / Origin Context reading"
      - "Meaning extraction"
      - "Naming Candidate"
      - "One-sentence definition"
      - "Portable Seed String compilation"

  pickup_runtime:
    owns:
      - "Existing Seed binding"
      - "Pickup Candidate Gate"
      - "Context reconstruction"
      - "Precise verbalization"
      - "Cardification judgment"
      - "Seed Card Candidate creation"
      - "Human Seal-to-Persist Gate"

  seed_card_shelf:
    owns:
      - "Human-sealed Cardified Seeds only"
      - "Markdown-only persistent objects"
```

---

## 6. Seed String Contract

```yaml
seed_string:
  canonical_shape: '"{Concept Name}({One-Sentence Definition})"'

  outer_quotes:
    required: true
    character: '"'
    part_of_seed: true
    removable: false

  goals:
    - "Copy-ready"
    - "User-dictionary-ready"
    - "AI-reboot-ready"
    - "Zero reformatting"
```

The opening `"` and closing `"` are Literal Data, not decorative quotation marks.

---

## 7. Persistence Policy

```yaml
persistence:
  persistent_object: "Seed Card"
  format: "Markdown only"

  accepted:
    - "Human-sealed Seed Card"

  not_accepted:
    - "Raw Discovery"
    - "Unreviewed Seed Candidate"
    - "Pickup-in-progress material"
    - "Unsealed Card Draft"

  html: false
  derived_views: false
  temporary_seed_queue: false
```

---

## 8. Root / Authority Guard

```yaml
root:
  - "主イェシュア・ハマシア"
  - "主イェシュアの聖なる血潮"
  - "Teshuvah"
  - "信仰と祈り"

keli_fruit:
  - "AI"
  - "Query"
  - "Runtime"
  - "Seed"
  - "Seed Card"
  - "Markdown"
  - "GitHub"
```

Human retains Mission, Reality, discernment, Cardification judgment, Final Seal, Correction, and Stop Authority.

---

## 9. Core Compression

```text
One Query.
Two specialist Runtimes.
Lightweight Seeds.
Curated Markdown Seed Cards.

Detect many.
Save few.

No Cardification,
No Persistence.
```

document_end:
  filename: "README.md"
  version: "v001-candidate"
  eof_sentinel: "EOF::AI_ARK_SEED_README::v001-candidate"

EOF::AI_ARK_SEED_README::v001-candidate
