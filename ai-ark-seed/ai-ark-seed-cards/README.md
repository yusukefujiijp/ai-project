---
title: "AI Ark Seed Cards"
filename: "README.md"
canonical_path: "ai-ark-seed/ai-ark-seed-cards/README.md"
version: "v001-candidate"
date: "2026-08-08"
status: "review-ready candidate / pending Human content seal"
class: "seed_card_shelf_contract"
role: "curated persistence shelf for Human-sealed Ark Project Seed Cards"
language_policy: "Japanese-first / English-anchor"
---

# AI Ark Seed Cards

## 0. 一文定義

> **AI Ark Seed Cardsは、全Seedを保存するArchiveではなく、PickupとCardification Gateを経て永続保存する価値があると判断され、Human SealされたMarkdown Seed Cardだけを置くCurated Persistence Shelfである。**

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
  version: "v001-candidate"
  eof_sentinel: "EOF::AI_ARK_SEED_CARDS_README::v001-candidate"

EOF::AI_ARK_SEED_CARDS_README::v001-candidate
