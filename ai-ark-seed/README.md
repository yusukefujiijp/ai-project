---
title: "AI Ark Seed"
filename: "README.md"
canonical_path: "ai-ark-seed/README.md"
version: "v002-candidate"
date: "2026-08-08"
updated: "2026-09-22"
revision_reason: "ARC-004 legacy routing and context-preservation guide; specialist Runtime contracts unchanged"
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

保存済みCardの現行・Historical・互換保持の区別は[Card Shelfの入口](ai-ark-seed-cards/README.md)で確認する。旧Compile／Pickupからの整理と文脈付き移植の価値は[§10](#10-context-preservation)へ。

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

## 10. Context Preservation

2026-09-22のHuman承認に基づき、旧`prompts/ai-compile-ark-seed*.md`と`prompts/ai-pickup-ark-seed*.md`の四原本を[ARC-004](../control-center/ARCHIVE.md#arc-004)へ保存した。軽量SeedとCard化の入口は引き続き`ai-ark-seed_query.md`。旧四ファイルを自動Fallbackや現在の起動先として使わない。

旧方式は、Origin Contextを持つ再起動可能なSeedを作り、別ThreadでConcept Maturationを開始する役割を持つ。新方式の一文Seed／選択的Card化との完全同等を確認したという意味ではない。本改訂は入口と保存価値の案内であり、専門Runtime・Queryの契約、Canonical Status、Field Test状態を変更しない。

### 10.1 依頼の意味から保持する文脈を選ぶ

- **一文で呼び出せるようにしたい**：既存COMPILEで軽量Seedを作る。Seed生成と保存を分ける。
- **複雑な発見・Correctionを別Threadで深掘りしたい**：一文Seedだけで十分と仮定せず、発見前の状況、Trigger、Humanの原文と意味、因果・変化、Confirmed／Candidate／Unknown、次に考えることと実行境界を必要な深さで保持する。明示されたHandoff・移行契約があればそれに従う。
- **Seed Cardとして残す価値を検討したい**：既存PICKUPのCardification判断へ進む。文脈付き移植や深掘りを、永続保存の自動承認と扱わない。

例えば「原文の意味を誤読していたAIがHuman Correctionで判断を変えた」発見では、名称だけでなく、何を誤読し、どの訂正が何を変え、何がまだ未確認かが再開に効く。どこまで保持するかはCurrent RequestとSourceから判断し、固定項目の穴埋めや回答の短縮義務にしない。

### 10.2 必要時に戻る設計原本

[旧Compile](../__archives/ARC-004/prompts/ai-compile-ark-seed.md)の§4・§12–16は文脈とPickup-Ready Packet、[旧Pickup](../__archives/ARC-004/prompts/ai-pickup-ark-seed.md)の§7–10は未言語層とConcept Maturationの参考になる。[旧Compile Query](../__archives/ARC-004/prompts/ai-compile-ark-seed_query.md)と[旧Pickup Query](../__archives/ARC-004/prompts/ai-pickup-ark-seed_query.md)も当時の関係を保存する。

これらは必要な意味を読み直すHistorical Sourceであり、全利用の必須読込リストではない。旧原本の`ark-project/prompts/`や起動命令を現在の経路へ読み替えず、Current Human Requestと適用Runtimeの下で使う。現行Subsystemをより重い旧方式へ一括変更したり、深い依頼を一文Seedへ縮めたりしない。

---

document_end:
  filename: "README.md"
  version: "v002-candidate"
  eof_sentinel: "EOF::AI_ARK_SEED_README::v002-candidate"

EOF::AI_ARK_SEED_README::v002-candidate
