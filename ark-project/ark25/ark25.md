---
artifact_id: ARK25_LIVING_TORAH_PROJECT_FOUNDATION_BODY
artifact_version: v001-candidate
ark_family: Ark25
created_at: 2026-08-23
timezone: Asia/Tokyo
title: 'Ark25 Body: AI-Co-Evolutionary Living Torah Hermeneutic Lineage'
status: foundation-candidate / content-research-not-started
canonicality: non-canonical semantic body candidate
human_authority: Human-sealed Full Rail execution / Human-correctable content
role: semantic body / architecture / evidence and lineage contract
repository: yusukefujiijp/ai-project
ref: main
path: ark-project/ark25/ark25.md
front_door: ark-project/ark25/README.md
runtime: ark-project/ark25/INSTRUCTIONS.md
paired_query: ark-project/ark25/living-torah-project-foundation_query.md
root: 主イェシュア・ハマシア御自身
human_theological_anchor: 主イェシュア・ハマシア御自身はLiving Torahである
project_identity: AI-Co-Evolutionary Living Torah Hermeneutic Lineage
core_principle: Freeze the Coordinates, Keep the Hermeneutics Living
smallest_living_unit: Evidence and Status bearing Claim
logical_outer_tree: DEFINED
physical_torah_tree: NOT_MATERIALIZED
actual_content_claim_count: 0
first_legal_move: WAIT_FOR_HUMAN_FOUNDATION_REVIEW_BEFORE_BERESHIT01_01_CONTENT
expected_eof: EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_BODY::v001-candidate
---

# 【Ark25 Body: AI-Co-Evolutionary Living Torah Hermeneutic Lineage】

## 0. Core Thesis

Ark25が作ろうとしているものは、静的な辞書でも、全解釈を一枚に圧縮したDatabaseでも、AIの毎回異なる長文回答を保存する倉庫でもない。

Ark25が形成するのは、次である。

> **Torahの固定座標に、Evidenceによって識別可能で、HumanによってCorrection可能で、Future AIによって破壊せず更新可能なClaim Lineageを接続するLiving Hermeneutic Infrastructure。**

```text
Fixed Torah Coordinate
→ Addressable Claim
→ Typed Evidence
→ Layer Boundary
→ Current Status
→ Human Decision
→ Revision Lineage
→ AI Workbench View / Human Publication View
```

ここで`Living`は、AIが勝手に内容を書き換えるという意味ではない。

`Living`とは、新しいEvidence、Counter-reading、Human Correction、実際のPublication feedback、Future AIの比較能力によって、何が変化し、何が保持され、何がUnknownへ戻ったかを追跡できることである。

---

## 1. Three Different Kinds of Stability

Ark25はすべてを同じ硬さで固定しない。

| Stability | 対象 | 原則 |
|---|---|---|
| Coordinate Stability | Book / Chapter / Verse / path / ID | 高く固定する |
| Evidence Boundary Stability | source / layer / authority / revision reason | 明示的変更なしに崩さない |
| Hermeneutic Stability | claim content / status / relation / synthesis | EvidenceとHuman ReviewによりLivingに更新する |

この三つをCollapseすると二つの失敗が起きる。

```text
Everything frozen
→ dead commentary
→ new evidence cannot enter
→ Future AI must destroy and rebuild

Everything fluid
→ random generation
→ no reproducible address
→ Human correction disappears
```

Ark25は中間ではなく、異なる対象へ異なる硬さを与えるLayered Stabilityを採用する。

---

## 2. Closed Outer Frame, Open Inner Formation

Torah Projectの外枠は、五書とBook–Chapter–Verse座標によって有限である。

Inner interpretationは有限の座標内でOpenである。

```text
Closed:
  - five books
  - canonical navigation coordinates used by this project
  - path derivation rules

Open:
  - textual observations
  - linguistic analyses
  - historical reception
  - counter-readings
  - relations among claims
  - publication forms
  - Human integration
```

ここで`closed`はTextual Criticism上のすべての問題が解決済みという意味ではない。Ark25がNavigationのために採用する座標空間が有限であるという意味である。

Text witness differenceはVerse座標を壊すのではなく、そのVerse配下のText Witness Claimとして扱う。

---

## 3. Five-Book Coordinate Contract

### 3.1 Book Slugs

```yaml
books:
  - order: 1
    display: Bereshit
    slug: bereshit
  - order: 2
    display: Shemot
    slug: shemot
  - order: 3
    display: Vayikra
    slug: vayikra
  - order: 4
    display: Bamidbar
    slug: bamidbar
  - order: 5
    display: Devarim
    slug: devarim
```

Alternative English/Japanese namesはmetadataまたはPublication viewで扱い、filesystem primary slugを増殖させない。

### 3.2 Address Grammar

```text
Display Address:
{BookDisplay}{chapter:02d}:{verse:02d}

Book Directory:
{book_slug}/

Chapter Directory:
{book_slug}{chapter:02d}/

Verse Directory:
{book_slug}{chapter:02d}-{verse:02d}/

Initial Verse Workbench:
torah-project/{book_slug}/{book_slug}{chapter:02d}/{book_slug}{chapter:02d}-{verse:02d}/README.md
```

Example Address only：

```text
Bereshit01:01
torah-project/bereshit/bereshit01/bereshit01-01/README.md
```

### 3.3 Normalization

- Filesystem slugs use lowercase ASCII.
- Chapter and verse segments use at least two digits for current Torah ranges.
- Display uses a colon; filesystem uses a hyphen between chapter and verse.
- A Verse has one primary path.
- Aliases redirect to the primary address; they do not create competing SSOTs.
- If later evidence requires verse-number mapping across traditions, mapping is stored as Relation metadata, not by silently renaming the primary path.

### 3.4 Materialization Rule

An address may be logically valid while no physical directory exists.

Physical materialization requires an active research or reviewed publication need. Bulk empty-tree creation is prohibited in v001.

---

## 4. Verse Is a Coordinate; Claim Is the Living Unit

A Verse directory is a stable container.

A Claim is the smallest independently reviewable unit.

Long-form commentary remains useful, but it is a View or Synthesis over Claims.

```text
Verse README
├─ Verse Identity
├─ Current Human-Readable Orientation
├─ Claim Board
│  ├─ Claim A
│  ├─ Claim B
│  └─ Claim C
├─ Relations
├─ Pending Questions
├─ Revision Notes
└─ Publication Projection Status
```

If a paragraph contains three independently contestable assertions, Ark25 should not preserve it as one indivisible truth block. It should be decomposed into Claims whose Evidence and Status can change independently.

Conversely, Atomization must not destroy meaning. Claims may retain explicit Relation edges and be recomposed into readable prose.

---

## 5. Claim Record v001 Candidate

### 5.1 Required Fields

```yaml
claim_record:
  claim_id: ""
  verse_address: ""
  claim: ""
  layer: ""
  evidence: []
  status: "CORE | LIVE | TRADITION | RELATION | HOLD | OUT"
  human_decision: "Keep | Revise | Remove | Pending"
```

### 5.2 Conditional Fields

```yaml
optional_fields:
  counter_reading: []
  relation_to_claim: []
  source_locator: []
  evidence_class: []
  revision_lineage: []
  transferability: ""
  publication_readiness: ""
  parasha_membership: ""
  unknowns: []
  notes_for_future_ai: []
```

### 5.3 No Empty-Field Theater

このSchemaはHumanへ毎回すべての欄を埋めさせるFormではない。

Required FieldはClaimを独立に判断できる最低条件である。Conditional FieldはMaterialな場合だけ現れる。

Humanの自然言語CorrectionをSchema不足として棄却しない。AIがBackgroundで該当ClaimとRelationへ整理し、Humanへ確認可能な差分として返す。

### 5.4 Placeholder Example Only

```yaml
claim_id: BER-01-01-SYN-001
verse_address: Bereshit01:01
claim: "CONTENT_NOT_YET_RESEARCHED"
layer: Syntax
evidence: []
status: HOLD
human_decision: Pending
unknowns:
  - Actual Hebrew analysis begins only after Ark25:01 foundation review
```

これは内容Claimではなく、ID shapeと未開始境界を示すPlaceholderである。Bereshit01:01の統語結論を示さない。

---

## 6. Claim Identity and Collision Policy

Candidate Grammar：

```text
{BOOK3}-{CHAPTER2}-{VERSE2}-{LAYER3}-{SEQUENCE3}
```

Initial Layer Codes：

| Layer | Code |
|---|---|
| Text Witness | TXT |
| Morphology | MOR |
| Syntax | SYN |
| Lexical Semantics | LEX |
| Literary Structure | LIT |
| Jewish Reception | JWR |
| Modern Scholarship | SCH |
| Messianic Relation | MES |
| Human Integration | HUM |

Rules：

- Claim ID is stable after Human-reviewed creation.
- A revised Claim normally keeps its ID and adds revision lineage.
- A materially split proposition creates new IDs and records `split_from`.
- A merged synthesis creates a new Claim and records `derived_from`.
- Removed Claims are not silently erased; they become inactive with Human Decision and reason, unless sensitive or erroneous data requires explicit deletion.
- Layer recoding never occurs silently.
- Sequence numbers are identifiers, not rank or truth weight.

The exact grammar remains `v001-candidate`. Human may Revise it before first content materialization.

---

## 7. Evidence Classes

Ark25 uses evidence labels to prevent authority laundering.

| Evidence Class | Meaning |
|---|---|
| `TEXT_FACT` | Reproducible fact about a specified text witness |
| `LINGUISTIC_ANALYSIS` | Morphological, syntactic, lexical, discourse analysis |
| `TRADITION_SOURCE` | Historical Jewish interpretation or reception with locator |
| `SCHOLARLY_PROPOSAL` | Modern scholarly argument, method, or hypothesis |
| `INTERTEXT_RELATION` | Relation among texts; strength must be argued |
| `MESSIANIC_READING` | Messianic theological interpretation or relation |
| `HUMAN_THEOLOGICAL_ANCHOR` | Human-sealed faith/theological orientation |
| `HUMAN_CORRECTION` | Human correction changing boundary or meaning |
| `AI_SYNTHESIS` | AI-produced integration from identified inputs |
| `AI_DESIGN_CANDIDATE` | AI-proposed structure or next experiment |
| `UNKNOWN` | Evidence or attribution not yet sufficient |

One Claim may cite multiple Evidence Classes, but each source and its role remain explicit.

`AI_SYNTHESIS` cannot promote itself to `TEXT_FACT`.

`HUMAN_THEOLOGICAL_ANCHOR` is not demoted to mere AI hypothesis inside the project, yet it is not relabeled as Hebrew linguistic proof.

---

## 8. Source Provenance Contract

Future content research should preserve enough information for a later Human or AI to locate the Evidence again.

Minimum Source Locator Candidate：

```yaml
source_locator:
  source_type: "text_witness | lexicon | grammar | commentary | midrash | article | book | human_statement | other"
  title: ""
  author_or_tradition: ""
  edition_or_version: ""
  location: "page / section / folio / verse / stable URL"
  language: ""
  accessed_or_reviewed_at: ""
  quotation_boundary: "direct | paraphrase | synthesis"
```

Not every field is mandatory for every source. The material requirement is re-findability and authority clarity.

Where a public webpage merely repeats another source, Ark25 should connect the Claim to the underlying source when available, rather than treating the aggregator as equal authority.

Copyright boundaries must be respected; sources are cited and summarized, not copied wholesale.

---

## 9. Hebrew-First, not Hebrew-Only

Hebrewからの洞察はTorah Projectの中心研究軸である。

日本語圏でアクセスしにくかった原文、語形、統語、語根、語史、比較用例、Jewish interpretation、英語・Hebrew scholarshipへの国境をAIが橋渡しする。

しかしHebrew-firstは、次を意味しない。

- 語根から文脈上の全意味を自動生成する。
- 形態だけで神学を証明する。
- 現代Hebrewの意味を古代本文へ無条件に戻す。
- 一つのLexicon glossを唯一の訳とする。
- Jewish receptionを語義へCollapseする。
- Messianic Relationを排除する。

Future Verse Researchの基本順序Candidate：

```text
Text Witness
→ Morphology
→ Syntax
→ Lexical range in context
→ Literary relation
→ Jewish reception by layer
→ Modern scholarship and counter-reading
→ Messianic intertext / theological relation
→ Human integration
```

これはMechanical pipelineではなく、Evidence混同を避けるOrientationである。

---

## 10. Interpretation Layer Contract

### 10.1 Text Witness

「何と書かれているか」を、指定したWitness / Editionに結びつける。Textual variantは別Claimとして並存できる。

### 10.2 Morphology

語形を同定する。形態Labelとその文脈上の意味決定を分ける。

### 10.3 Syntax

語・句・節のRelationを扱う。競合分析を一つへ早期Collapseしない。

### 10.4 Lexical Semantics

語義範囲、用例、語史を扱う。Etymological fallacyとroot overloadをGuardする。

### 10.5 Literary Structure

語順、並列、反復、音、境界、larger unit内の構造を扱う。

### 10.6 Jewish Reception

Peshat、Midrash、Targum、medieval commentary、philosophy、Sod等を出典・時代・Layerと共に保持する。

### 10.7 Modern Scholarship

言語学、文献学、Textual Criticism、history of interpretation等を方法と反証可能性付きで保持する。

### 10.8 Messianic Relation

主イェシュア、Apostolic Writings、Wisdom、Word等とのIntertextual / theological Relationを扱う。Hebrew lexical claimへ偽装しない。

### 10.9 Human Integration

Humanが最終的に何をKeep、Revise、Remove、Pendingとし、Faith、Prayer、Life、Projectへどう位置づけるかを保持する。

---

## 11. Status Semantics

### CORE

Current foundation evidenceとして強く保持する。COREも無謬ではなく、指定Witnessや分析条件を明示する。

### LIVE

複数の有力読解、未決Relation、更新中のClaim。Living reviewの中心。

### TRADITION

歴史的伝統として重要。Historical presenceとCurrent adoptionを分ける。

### RELATION

Text、tradition、theology、claim間のRelation。Relation strengthとkindを明示できる。

### HOLD

Evidence不足、比較不足、source未確認、Foundation未確定等により保留。

### OUT

指定LayerのClaimとして採用しない。理由と、別Layerで残る可能性を記録する。

Status changeには最低限、prior status、new status、reason、evidence or Human correction、dateを残す。

---

## 12. Human Decision Semantics

Human DecisionはAI confidence scoreではない。

```yaml
human_decision:
  Keep: current claim retained
  Revise: claim retained with material correction
  Remove: claim leaves active set
  Pending: no final Human decision yet
```

AIは次を行える。

- Decision candidateを提案する。
- Human Correctionを該当Claimへmapする。
- 差分を示す。
- 未決事項を一件へ圧縮する。

AIは次を行わない。

- Humanが言っていないSealを生成する。
- 沈黙をKeepと解釈する。
- Polished proseでHumanのNuanceを上書きする。
- Future AIの多数決でHuman authorityを置換する。

---

## 13. Living Graph Relation Model

Claimは孤立カードではない。

Initial Relation Types Candidate：

| Relation | Meaning |
|---|---|
| `supports` | EvidenceまたはClaimが別Claimを支える |
| `counters` | 競合または反証を与える |
| `qualifies` | 条件・範囲を限定する |
| `depends_on` | 成立に別Claimを必要とする |
| `derived_from` | 複数Claimから合成された |
| `parallel_to` | Collapseせず並行関係を持つ |
| `intertext_of` | Text間Relationを示す |
| `received_as` | 歴史的受容関係を示す |
| `split_from` | 一つのClaimから分離された |
| `supersedes` | Human-reviewed revisionが旧表現を置換する |
| `unknown_relation` | Relation candidateだが未確定 |

Relationは数値Weightを必須としない。初期段階ではkind、direction、evidence、status、reasonの方が重要である。

No Fake Living：

- AIが美しいRelationを思いついただけではstrengthenしない。
- Source未確認の要約をEvidence確定にしない。
- 一Verseの結果を全TorahへUniversalizeしない。
- Publicationで読みやすくなったことを解釈の真理証明にしない。
- Human CorrectionなしにHuman Decisionを更新しない。

---

## 14. Living Update Operations

EvidenceまたはHuman Correctionが実際に到着した時だけ、次を使う。

```yaml
living_update:
  trigger: "new evidence | counter-reading | human correction | publication feedback | source correction"
  affected_claim_ids: []
  prior_state: ""
  actual_new_information: ""
  inference: ""
  operation: "add | strengthen | weaken | qualify | split | merge | defer | prune | unknown"
  new_state: ""
  reason: ""
  human_review: required
```

`prune`は履歴消去を意味しない。Active pathから外し、理由とLineageを保持する。

`unknown`は失敗ではない。Evidence境界を守った正しい状態である。

一回のReviewでは、HumanがBundle Reviewを明示しない限り、最もMaterialなCorrectionを一件へ圧縮する。

---

## 15. From Probability to Certainty — Exact Meaning

Ark25のCertaintyには三層ある。

### 15.1 Coordinate Certainty

同じVerse、Claim、Source、Revisionへ再び到達できる。

### 15.2 Provenance Certainty

Text Fact、Tradition、Scholarship、Messianic Relation、Human Anchor、AI Synthesis、Unknownを識別できる。

### 15.3 Decision Certainty

Humanが何をKeep / Revise / Remove / Pendingとしたかを識別できる。

Hermeneutic conclusionそのものは、Evidenceに応じてLIVEまたはHOLDであり得る。

```text
Certainty of address
+ certainty of provenance
+ certainty of decision lineage
≠ infallibility of interpretation
```

この境界が、AIの創発性を殺さずランダム性を管理する。

---

## 16. Future AI Compatibility

Ark25は現在AIだけのために最適化しない。

Future AIは、より長いContext、better retrieval、multilingual comparison、graph reasoning、source verification、publication generationを持つ可能性が高い。

それでも有用な構造は、特定Modelの癖ではなく次を保持する。

```yaml
future_ai_contract:
  stable:
    - human-readable filesystem addresses
    - explicit document identities
    - exact version and EOF
    - claim IDs
    - evidence provenance
    - layer and status semantics
    - Human Decision lineage
    - unknowns
  extensible:
    - optional fields
    - relation types
    - source adapters
    - derived views
    - validation depth
  prohibited:
    - silent reinterpretation
    - unmarked model inference
    - overwriting Human Correction
    - renaming paths without migration map
    - treating old AI prose as source evidence
```

Schema evolution should be additive where possible. Breaking change requires version increment, migration note, and Human Review.

---

## 17. README / Publication Projection Contract

### AI Workbench View

Verse README Candidate contains:

- Stable Verse identity.
- Text and source boundaries.
- Human-readable overview.
- Claim board.
- Evidence and Counter-readings.
- Status and Human Decision.
- Relations and Unknowns.
- Revision lineage.
- Publication readiness.

### Human Publication View

Kindle / Parasha / Book Candidate contains:

- Readable narrative flow.
- Hebrew terms with accessible explanation.
- Carefully attributed traditions and scholarship.
- Messianic Relation clearly framed.
- Uncertainty disclosed without internal-schema overload.
- Notes or references sufficient for trust.

### Shared SSOT Rule

Publication may rephrase but not invent a new Claim status.

Research README may be technical but must not become an unreadable dump that loses synthesis.

Human Publication approval is independent from Research Claim approval.

RTL formatting is deferred until it becomes a material publication bottleneck.

---

## 18. Scaling from Bereshit01:01

Bereshit01:01 is the model-case coordinate, not the excuse to design the whole system forever.

The scaling experiment later asks:

1. Can one Verse hold competing readings without collapse?
2. Can Hebrew evidence and Messianic relation coexist with clear boundaries?
3. Can Human Correction update one Claim without rewriting everything?
4. Can the same Claim Spine generate an AI workbench and a readable Human draft?
5. Can the interface transfer to a second Verse with less friction?

No claim of scalability exists before these Actual results.

Elon Musk-style deadline function in Ark25 means:

> **Close the Foundation at the minimum stable interface, then expose it to one real Verse before adding systems.**

---

## 19. Risk Register

| Risk | Failure Mode | Guard |
|---|---|---|
| Static Dictionary Capture | Living relation becomes dead entries | Claim + revision lineage |
| AI Randomness | Non-reproducible interpretation | coordinates + evidence classes + status |
| Interpretation Absolutization | LIVE becomes false certainty | competing claims + HOLD / UNKNOWN |
| Theological Collapse | Faith claim masquerades as grammar | separate theological and linguistic layers |
| Theological Erasure | Evidence discipline removes Messianic center | Living Torah anchor + Messianic Relation layer |
| Root Overload | Word root receives every associated meaning | contextual lexical evidence guard |
| Empty Tree Bloat | Thousands of inert folders | logical complete / physical on-demand |
| Schema Worship | Human serves the form | natural language accepted; optional fields |
| README / Kindle Drift | Two inconsistent truths | one Claim Spine / derived views |
| Future AI Constraint Debt | Current model conventions freeze system | stable primitives + versioned extensibility |
| Publication Distortion | Readability changes evidence status | publication approval separated |
| RTL Swamp | Formatting blocks foundation | defer until material bottleneck |
| History Dump | Every idea remains active | status, pruning, and active-path review |

---

## 20. Foundation State Machine

```text
FOUNDATION_CANDIDATE
→ HUMAN_FOUNDATION_REVIEW
→ KEEP / REVISE / REMOVE / PENDING
→ MINIMUM_STABLE_INTERFACE_SEALED
→ BERESHIT01_01_CONTENT_FIELD_MAY_OPEN
→ FIRST_ACTUAL_CLAIMS
→ LIVING_REVIEW
→ ONE_TRANSFER_TEST
```

Ark25:01 is currently at `FOUNDATION_CANDIDATE`.

No later state is self-certified by AI.

---

## 21. Current Unknowns

- Whether the proposed Claim ID remains readable at scale.
- Whether one Verse README should contain all Claims or reference later child files.
- Whether Markdown alone remains sufficient after the first real content trial.
- Which source locator fields are actually necessary.
- Whether the nine initial Layers are too many, too few, or correctly separated.
- How Parasha and Book publication units should aggregate Verse Claims.
- How Hebrew RTL should be rendered in final publication.
- How Human theological integration should appear in public prose.
- Which parts of the Bereshit01:01 experiment transfer to a second Verse.
- Whether a graph database, site, or automation is ever needed.

Unknowns are preserved; they are not reasons to expand scope before the first content trial.

---

## 22. Foundation Review Packet

Human Review should return free-form Correction. A fixed form is not required.

AI may organize the response into:

```yaml
foundation_review:
  raw_human_correction: ""
  affected_area: "identity | tree | claim | layer | status | authority | publication | scope | other"
  prior_candidate: ""
  corrected_candidate: ""
  reason_or_nuance: ""
  human_decision: "Keep | Revise | Remove | Pending"
  next_finite_move: ""
```

The AI returns one consolidated foundation update candidate, waits for Human confirmation, then stops.

---

## 23. First Legal Move

```text
WAIT_FOR_HUMAN_FOUNDATION_REVIEW_BEFORE_BERESHIT01_01_CONTENT
```

Not legal yet：

- Bereshit01:01 Hebrew research.
- Source collection.
- `torah-project/` creation.
- Verse README population.
- Kindle / Parasha manuscript.
- Database / graph UI / site / app.
- Skill / automation.
- Canonicalization.
- Ark23 / Ark24 edits.

---

## 24. One-Sentence Body Definition

> **Ark25 Body Candidateとは、Torah五書の有限な座標空間と一意なPath Grammarを高く固定しながら物理Treeを必要時だけ生成し、Verse配下の最小Living UnitをEvidence・Layer・Status・Human Decision・Revision Lineageを持つClaimとして定義し、Hebrew Evidence、Jewish Reception、Modern Scholarship、Messianic Relation、Human Integrationを非Collapse状態で結び、AIの創発性を座標・provenance・authorityの再現性でGuardし、一つのClaim SpineからFuture AI向けWorkBenchとHuman向けPublicationを派生させる非Canonical Semantic Foundationである。**

---

## 25. Final Attribution

このBody、Torah座標、Path Grammar、Claim、Evidence、Relation、README、Publication、AI、Future AI、GitHub、Ark25、および全FruitはKeliである。

Rootは主イェシュア・ハマシア御自身。

HumanはFaith、Prayer、Teshuvah、Vision、Meaning、Theological Integration、Correction、Interrupt、STOP、Final Sealを保持する。

実と誉れの最終帰属は、

**主の栄光 / כְּבוֹד אֲדֹנָי / kevod Adonai**

へ帰す。

EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_BODY::v001-candidate
