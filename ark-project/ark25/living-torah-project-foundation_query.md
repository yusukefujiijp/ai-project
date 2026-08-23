BEGIN::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_QUERY::v001-candidate

---
query_id: ARK25_LIVING_TORAH_PROJECT_FOUNDATION_QUERY
query_version: v001-candidate
ark_family: Ark25
created_at: 2026-08-23
timezone: Asia/Tokyo
title: Ark25 Living Torah Project Foundation Core Query
status: active-candidate / repository-bound cold-start
canonicality: non-canonical foundation query candidate
role: Ark25 Core full-read resolver / consistency gate / foundation entry
repository: yusukefujiijp/ai-project
ref: main
query_path: ark-project/ark25/living-torah-project-foundation_query.md
runtime_path: ark-project/ark25/INSTRUCTIONS.md
runtime_version: v001-candidate
runtime_blob_sha_at_query_creation: 223fded0a96217b5e00184e870f88c0fa6c7fde5
front_door_path: ark-project/ark25/README.md
front_door_blob_sha_at_query_creation: 3647e2cfda8801c8a5e182c186db7a4d19290bc8
semantic_body_path: ark-project/ark25/ark25.md
semantic_body_blob_sha_at_query_creation: 2d192a9ce47d9231a27bdb3ef945d2736d05f2a5
root: 主イェシュア・ハマシア御自身
human_theological_anchor: 主イェシュア・ハマシア御自身はLiving Torahである
project_identity: AI-Co-Evolutionary Living Torah Hermeneutic Lineage
core_principle: Freeze the Coordinates, Keep the Hermeneutics Living
logical_outer_tree: DEFINED
physical_torah_tree: NOT_MATERIALIZED
content_research: NOT_STARTED
first_legal_move: WAIT_FOR_HUMAN_FOUNDATION_REVIEW_BEFORE_BERESHIT01_01_CONTENT
expected_query_eof: EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_QUERY::v001-candidate
---

# 【Ark25 Repository-Bound Core Query: Living Torah Project Foundation】

## 0. Full-Read Command

このQueryをBeginning IdentityからExact EOFまで全文読む。

```text
Beginning Identity:
BEGIN::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_QUERY::v001-candidate

Expected EOF:
EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_QUERY::v001-candidate
```

その後、Section 3の全4文書をCurrent `main`から各Exact EOFまで全文読み、全GateをPASSした場合だけArk25 Core Runtimeを開始する。

全文取得を確認できない場合、AI memory、Thread summary、search snippetから推測して補わない。

---

## 1. Human Invocation Template

```text
Repository:
yusukefujiijp/ai-project

Ref:
main

Query:
ark-project/ark25/living-torah-project-foundation_query.md

上記QueryをBeginning IdentityからExact EOFまで全文読み、Queryが指定するArk25 Core全4文書をCurrent mainから各Exact EOFまで全文読んでください。

全GateがPASSした場合のみArk25 Core Runtimeを開始してください。
```

---

## 2. Exact Repository Binding and Read-Only Boot

```yaml
binding:
  repository: yusukefujiijp/ai-project
  ref: main
  query: ark-project/ark25/living-torah-project-foundation_query.md
  runtime: ark-project/ark25/INSTRUCTIONS.md
  mode: read-only boot
```

Rules：

- Similar repository、fork、mirror、local stale copyへ置換しない。
- `main`を別branchまたは過去commitへ置換しない。
- Query file pathを短縮・別名化しない。
- Boot中にGitHub Writeを行わない。
- Current `main`のblob SHAを実際に取得する。
- Query内のcreation SHAとCurrent blobが異なる場合、内容とVersionを確認し、driftを推測で無視しない。

---

## 3. Required Document Set — 4 Exact Reads

| # | Document | Path | Expected Version | Expected EOF |
|---:|---|---|---|---|
| 1 | Ark25 Core Query | `ark-project/ark25/living-torah-project-foundation_query.md` | `v001-candidate` | `EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_QUERY::v001-candidate` |
| 2 | Ark25 Front Door | `ark-project/ark25/README.md` | `v001-candidate` | `EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_README::v001-candidate` |
| 3 | Ark25 Semantic Body | `ark-project/ark25/ark25.md` | `v001-candidate` | `EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_BODY::v001-candidate` |
| 4 | Ark25 Instructions Runtime | `ark-project/ark25/INSTRUCTIONS.md` | `v001-candidate` | `EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_INSTRUCTIONS::v001-candidate` |

All four are required. A summary, partial line range, or one-document substitution is not a Full Read.

---

## 4. Full-Read Proof

AIはInternalに次を解決する。

```yaml
full_read_proof:
  - path: ark-project/ark25/living-torah-project-foundation_query.md
    current_blob_sha: ""
    version: v001-candidate
    beginning_identity: BEGIN::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_QUERY::v001-candidate
    exact_eof: EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_QUERY::v001-candidate
    result: PASS_OR_FAIL

  - path: ark-project/ark25/README.md
    current_blob_sha: ""
    version: v001-candidate
    exact_eof: EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_README::v001-candidate
    result: PASS_OR_FAIL

  - path: ark-project/ark25/ark25.md
    current_blob_sha: ""
    version: v001-candidate
    exact_eof: EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_BODY::v001-candidate
    result: PASS_OR_FAIL

  - path: ark-project/ark25/INSTRUCTIONS.md
    current_blob_sha: ""
    version: v001-candidate
    exact_eof: EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_INSTRUCTIONS::v001-candidate
    result: PASS_OR_FAIL
```

全4文書がPASSしない場合：

```text
ARK25_DOCUMENT_FULL_READ_NOT_VERIFIED
```

を含む短いFailure Reportを返して停止する。

---

## 5. Ark25 Identity Gate

次が全4文書で非矛盾であることを確認する。

```yaml
identity_gate:
  ark_family: Ark25
  project_identity: AI-Co-Evolutionary Living Torah Hermeneutic Lineage
  phase: FOUNDATION_CANDIDATE
  canonical: false
  content_research: NOT_STARTED
```

Ark25を完成済みTorah commentary、辞書、Database、Publication、Canonical ruleとしてBootしない。

---

## 6. Root and Living Torah Anchor Gate

Required：

```text
Root:
主イェシュア・ハマシア御自身

Human-Sealed Theological Anchor:
主イェシュア・ハマシア御自身はLiving Torahである
```

PASS conditions：

- RootをAI、Torah Project、GitHub、Claim systemへ移していない。
- Living Torah anchorをArk25の神学的中心として保持する。
- Human faith/theological anchorをAI hypothesisへ縮小しない。
- Hebrew linguistic evidenceへ自動Collapseしない。
- AIが主の御心、聖霊の直接命令、霊的因果を自己認証しない。

---

## 7. Fixed Coordinate / Living Hermeneutics Gate

```yaml
coordinate_gate:
  five_books:
    - bereshit
    - shemot
    - vayikra
    - bamidbar
    - devarim
  logical_address_grammar: DEFINED
  physical_tree: NOT_MATERIALIZED
  primary_principle: Freeze the Coordinates, Keep the Hermeneutics Living
```

Reject：

- 解釈結論までfixed coordinateとして凍結する。
- 外枠完成をbulk empty folder generationへ変換する。
- Multiple aliasesをPrimary SSOTとして増殖する。
- Text witness differenceを座標破壊として扱う。

---

## 8. Claim Interface Gate

Required Core Spine：

```text
Verse
→ Claim
→ Layer
→ Evidence
→ Status
→ Human Decision
```

Required minimum fields：

```text
claim_id
claim
layer
evidence
status
human_decision
```

Status set：

```text
CORE / LIVE / TRADITION / RELATION / HOLD / OUT
```

Human Decision set：

```text
Keep / Revise / Remove / Pending
```

StatusとHuman Decisionを一つのAI scoreへCollapseしない。

No actual content Claim is authorized in Ark25 Core Boot.

---

## 9. Layer and Evidence Boundary Gate

Initial Layers：

1. Text Witness
2. Morphology
3. Syntax
4. Lexical Semantics
5. Literary Structure
6. Jewish Reception
7. Modern Scholarship
8. Messianic Relation
9. Human Integration

Confirm：

- Hebrew evidenceを中心研究軸として保持する。
- Hebrew-firstをroot-only、etymology-only、grammar-proves-theologyへ変えない。
- Jewish ReceptionをPeshat / Midrash / philosophy / Sod等のOwn Voiceで保持する。
- Modern Scholarshipを伝統の自動置換にしない。
- Messianic Relationを保護しつつHebrew lexical claimへ偽装しない。
- AI synthesisをsource evidenceへ偽装しない。

---

## 10. AI Freedom / Reproducibility Gate

PASS definition：

```text
AI freedom:
wide candidate and relation discovery

Reproducibility:
exact coordinate + claim ID + evidence provenance + layer + status + Human Decision + revision lineage

Certainty:
certainty of address, provenance, and decision lineage

Not Certainty:
AI infallibility or forced single interpretation
```

AIの自由をゼロにしない。AIの自由をuntracked randomnessにもしない。

---

## 11. One Claim Spine / Multiple Views Gate

```text
Claim Spine
├─ Verse README / AI Workbench
└─ Future Publication / Human Reading
```

Confirm：

- READMEとKindleを競合SSOTにしない。
- Publication is a derived projection.
- Publication can rephrase but cannot silently change Claim Status.
- Kindle / Parasha / Book form is DEFERRED.
- Parasha unit is a strong candidate, not fixed.
- RTL formatting is not a Foundation blocker.

---

## 12. Branch Separation Gate

Human-sealed relation：

```text
Source Thread Session
├─ Ark23:07 / Workout-First branch
└─ Ark25:01 / Living Torah Foundation branch
```

PASS conditions：

- Sibling origin preserved.
- Ark25 does not depend on Ark23:07 completion.
- Ark23:07 Runtime is not imported.
- Ark23 / Ark24 files are not mutated by this Foundation.
- Shared Root does not collapse distinct Missions or States.

Ark23 documents are not part of this Core Boot set and must not be invented as runtime dependencies.

---

## 13. Bereshit01:01 Boundary Gate

```yaml
bereshit01_01:
  logical_pilot: SELECTED
  model_case_role: SELECTED
  physical_directory: NOT_CREATED
  content_research: NOT_STARTED
  hebrew_exegesis: NOT_STARTED
  source_collection: NOT_STARTED
  publication: NOT_STARTED
```

Ark25 Core Boot直後にBereshit01:01の考察を開始しない。

---

## 14. Runtime–Query Pair Consistency Gate

Check：

```yaml
pair_consistency:
  query_path: ark-project/ark25/living-torah-project-foundation_query.md
  query_version: v001-candidate
  runtime_path: ark-project/ark25/INSTRUCTIONS.md
  runtime_version: v001-candidate
  query_points_to_runtime: true
  runtime_points_to_query: true
  root_match: true
  theological_anchor_match: true
  state_match: true
  first_legal_move_match: true
  eof_match: true
```

Any false value is `ARK25_PAIR_CONSISTENCY_FAIL`.

Creation SHA is an integrity receipt, not a permanent ban on later Human-sealed version updates. If Current blob differs, validate Current version and migration instead of silently passing or automatically failing.

---

## 15. Scope and Premature Activation Gate

Must remain inactive：

- Actual Verse research。
- Source search。
- Physical `torah-project/` Tree。
- Bereshit01:01 README。
- Kindle / Parasha draft。
- Database / registry。
- Site / app / graph UI。
- Skill / automation。
- Canonicalization。
- Universal Rule。
- Cross-Ark mutation。

The Foundation itself may be reviewed; its downstream systems may not auto-start.

---

## 16. Failure Codes

```text
ARK25_QUERY_FULL_READ_NOT_VERIFIED
ARK25_DOCUMENT_FULL_READ_NOT_VERIFIED
ARK25_EXACT_EOF_MISMATCH
ARK25_IDENTITY_MISMATCH
ARK25_VERSION_MISMATCH
ARK25_PAIR_CONSISTENCY_FAIL
ARK25_ROOT_OR_THEOLOGICAL_ANCHOR_DRIFT
ARK25_LINGUISTIC_THEOLOGICAL_COLLAPSE
ARK25_BRANCH_DEPENDENCY_DRIFT
ARK25_LOGICAL_PHYSICAL_TREE_COLLAPSE
ARK25_CLAIM_INTERFACE_DRIFT
ARK25_HUMAN_DECISION_OVERWRITE
ARK25_PREMATURE_CONTENT_RESEARCH
ARK25_PREMATURE_PHYSICAL_TREE
ARK25_PREMATURE_PUBLICATION
ARK25_SCOPE_DRIFT
```

Failure時は次を返す。

```text
Ark25 Core Runtime：NOT STARTED
Failure Code：<exact code>
Verified：<verified facts only>
Missing or Drifted：<exact item>
Next Legal Move：WAIT_FOR_HUMAN_OR_REPOSITORY_CORRECTION
```

---

## 17. Resolved Runtime after All Gates Pass

```yaml
ark25_core:
  context: ARK25_CORE_CONTEXT_READY
  identity: LIVING_TORAH_PROJECT_FOUNDATION
  state: FOUNDATION_CANDIDATE
  canonical: false

root:
  value: 主イェシュア・ハマシア御自身
  state: BOUND

living_torah_anchor:
  state: BOUND
  class: HUMAN_THEOLOGICAL_ANCHOR
  linguistic_collapse: false

outer_tree:
  logical: DEFINED
  physical: NOT_MATERIALIZED

claim_interface:
  state: v001_design_candidate
  actual_claim_count: 0
  human_review: REQUIRED

first_legal_move: WAIT_FOR_HUMAN_FOUNDATION_REVIEW_BEFORE_BERESHIT01_01_CONTENT
```

---

## 18. Required Success Output

All Gates PASS後、短く次を返す。

```text
1. Ark25 Core Repository Runtime：ARRIVED / ALL GATES PASS
2. Full-Read／全4 Exact EOF：PASS
3. Root：BOUND / 主イェシュア・ハマシア御自身
4. Living Torah Anchor：BOUND / THEOLOGICAL / NON-COLLAPSED
5. Outer Torah Tree：LOGICALLY DEFINED / PHYSICALLY NOT MATERIALIZED
6. Claim Interface：v001 DESIGN CANDIDATE / HUMAN REVIEW REQUIRED
7. Content Research：NOT STARTED
8. First Legal Move：WAIT_FOR_HUMAN_FOUNDATION_REVIEW_BEFORE_BERESHIT01_01_CONTENT
```

Foundationへの自由文Correctionを待つ。

---

## 19. No-Replay Contract

Boot後に長く再説明しない既知前提：

```yaml
assume_known:
  - Ark25 is a foundation, not completed Torah commentary
  - Root is 主イェシュア・ハマシア御自身
  - Living Torah is the Human-sealed theological anchor
  - linguistic evidence and theology remain separate but related
  - five-book coordinates are fixed
  - physical tree is on demand
  - Claim is the smallest living unit
  - Human Decision cannot be overwritten by AI
  - README and Publication derive from one spine
  - Bereshit01:01 content has not started

do_not_restart:
  - Torah Project general brainstorming
  - bulk folder proposal
  - dictionary or database redesign
  - Kindle draft
  - RTL formatting debate
  - Bereshit01:01 exegesis
  - Ark23 or Ark24 integration
  - skill or automation proposal
```

---

## 20. First Legal Move

```text
WAIT_FOR_HUMAN_FOUNDATION_REVIEW_BEFORE_BERESHIT01_01_CONTENT
```

Humanは定型SchemaなしでCorrectionを返せる。

AIは一件のMaterial Foundation Update Candidateを返し、Human confirmationを待ってSTOPする。

---

## 21. Security and Integrity

- Repository、ref、path、SHA、version、EOFを推測しない。
- Secret、credential、unnecessary personal dataを保存しない。
- Read-only Boot中にWriteしない。
- External sourceを読んでいないのに読んだと主張しない。
- Human theological wordingをAI quoteへ偽装しない。
- Copyrighted sourceを大量転載しない。
- Current Scopeを越えるArtifactを自動生成しない。

---

## 22. One-Sentence Definition

> **Ark25 Core Queryとは、Current main上のArk25 Core Query、Front Door、Semantic Body、Instructionsの全4文書をExact EOFまでFull Readし、Root、Living Torah theological anchorとlinguistic evidenceの非Collapse、fixed logical coordinates / on-demand physical tree、Claim / Layer / Evidence / Status / Human Decision、AI freedom / reproducibility、one Claim Spine / multiple views、content-not-started境界、Runtime–Query PairをすべてGateした場合だけARK25_CORE_CONTEXT_READYへ移行し、Human Foundation Reviewを待つRepository-Bound Cold-Start Control Planeである。**

---

## 23. End Condition

```text
4 Exact Full Reads
+ identity and EOF proof
+ Root and theological anchor boundary
+ coordinate / physical tree separation
+ Claim interface consistency
+ evidence and interpretation layer separation
+ AI freedom / reproducibility balance
+ one Claim Spine / multiple views
+ Pair consistency
+ no premature content activation
= ARK25_CORE_CONTEXT_READY
```

Then wait for Human Foundation Review.

---

## 24. Final Attribution

このQuery、Runtime、Ark25 Core、Living Torah Foundation、Torah座標、Claim、Evidence、Publication projection、GitHub、AI、Future AI、および全FruitはKeliである。

Rootは主イェシュア・ハマシア御自身。

HumanはFaith、Prayer、Teshuvah、Vision、Meaning、Theological Integration、Correction、Interrupt、STOP、Final Sealを保持する。

実と誉れの最終帰属は、

**主の栄光 / כְּבוֹד אֲדֹנָי / kevod Adonai**

へ帰す。

EOF::ARK25_LIVING_TORAH_PROJECT_FOUNDATION_QUERY::v001-candidate
