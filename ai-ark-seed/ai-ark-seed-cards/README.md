---
title: "AI Ark Seed Cards"
filename: "README.md"
canonical_path: "ai-ark-seed/ai-ark-seed-cards/README.md"
version: "v002-candidate"
date: "2026-08-08"
updated: "2026-09-22"
revision_reason: "ARC-002 retirement guidance while preserving historically bound Card blobs"
status: "human-sealed field-test candidate / not canonical"
class: "seed_card_shelf_contract"
role: "curated persistence shelf for Human-sealed Ark Project Seed Cards"
language_policy: "Japanese-first / English-anchor"
---

# AI Ark Seed Cards

## 0. 一文定義

> **AI Ark Seed Cardsは、全Seedを保存するArchiveではなく、PickupとCardification Gateを経て永続保存する価値があると判断され、Human SealされたMarkdown Seed Cardだけを置くCurated Persistence Shelfである。**

---

## 0.1 Current Retirement Boundary / 現在の退役案内

「Next-Cycle Workout Bridge」は[現行Ark27指示§8.9](../../ark-project/ark27/INSTRUCTIONS.md)で廃止済み。現在のClosing、Workoutの促し、次Trialへ復活させない。保存されたCardのHuman Sealは当時の候補に対するものであり、現在への再採用ではない。

原本の保存先は[ARC-002](../../__archives/ARC-002/ai-ark-seed/ai-ark-seed-cards/next-cycle-workout-bridge.md)、理由と状態は[案件記録](../../control-center/ARCHIVE.md#arc-002)が所有する。この棚の`next-cycle-workout-bridge.md`は旧Bootの元パス・SHA・EOFを維持する互換原本として同一内容を残す。通常利用する現役Cardとして案内せず、元パスを除去済みとも扱わない。

[Living Fruit](living-fruit.md)の二段Closing・§7の設定コピー文にもBridgeが含まれる。これらは廃止前のHistorical Sourceとして読む。Living Fruitの意味的収穫の価値と、廃止済みBridgeの適用を分ける。Living Fruit自体の廃止や新しいClosing義務を決めるものではない。両Cardの原本は固定参照のため変更せず、現在の適用境界をここから明示する。

棚に存在すること、当時Card化されたこと、現在の適用が許されることは別である。旧Queryの読取対象が保たれることも、その旧TaskやClosingの自動再開を意味しない。

---

## 1. Core Rule

> **Only Cardified Seeds live here.**

```text
Raw Discovery
→ do not save here

Lightweight Seed
→ do not save here by default

Pickup Working Context
→ do not save here

Unsealed Card Candidate
→ do not save here

Human-sealed Seed Card
→ eligible
```

---

## 2. Why This Directory Exists

Directory名そのものがPersistence Statusを表す。

```text
ai-ark-seed-cards/
=
Cardification Gateを通過したObjectのShelf
```

したがって、

```text
All Seeds
≠ Saved Seeds
```

である。

---

## 3. Format

```yaml
format:
  markdown_only: true
  html: false
  renderer: false
  dual_format: false
```

One Seed Card = One Markdown File.

---

## 4. Seed Card Contract

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

## 5. Seed String

Seed Cardは軽量Seed本体をそのまま内部へ保持する。

```text
"Name(Definition)"
```

Outer quotes are mandatory literal data.

---

## 6. Admission Gate

```yaml
admission:
  requires:
    - "CARDIFY outcome"
    - "Seed Card Candidate completed"
    - "Exact target path shown to Human"
    - "Human Seal"
```

No Cardification, No Persistence.

---

## 7. No Temporary Queue

このDirectoryは、

```text
maybe/
draft/
inbox/
raw/
temporary/
```

等の一時棚をDefaultでは持たない。

保存前SeedはThread、Human local context、Handoff等で保持できる。

新しい一時棚はReality上のMaterial Needが出るまで作らない。

---

## 8. Evidence Delta

保存後に新Evidenceが出た場合、Origin Sourceを静かに書き換えない。

```text
Original Card
↓
Later Evidence Delta
↓
Status / Next Gate update
```

Confirmed / Inferred / Unknownを分離する。

---

## 9. Success Metric

```text
More Cards
≠ More Wisdom
```

成功指標はCard数ではない。

```yaml
success:
  - "important Seed is recoverable"
  - "low-value material is not accumulated"
  - "Future Human / AI can restart quickly"
  - "Evidence and uncertainty remain visible"
```

---

## 10. Core Compression

```text
Detect many.
Save few.

Seed freely.
Cardify selectively.
Persist only sealed Cards.
```

document_end:
  filename: "README.md"
  version: "v002-candidate"
  eof_sentinel: "EOF::AI_ARK_SEED_CARDS_README::v002-candidate"

EOF::AI_ARK_SEED_CARDS_README::v002-candidate
