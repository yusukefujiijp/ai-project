---
title: "AI Learning Family"
canonical_name: "AI Learning Family"
version: "v001-candidate"
date: "2026-07-14"
filename: "README.md"
canonical_path: "prompts/ai-learning/README.md"
class: "prompt_family"
role: "Cross-AI Human learning family / Family Constitution / Router / Governance / Index"
status: "human-sealed field-test candidate / not canonical"
language_policy: "Japanese-first / English-anchor"
parent_shelf:
  path: "prompts/README.md"
  role: "Cross-AI Prompt Runtime and Query Shelf"
architecture:
  - "Parent routes."
  - "Family governs."
  - "Leaf teaches."
  - "Human practices."
  - "Reality confirms."
  - "Harvest preserves."
root_guard: "Root is 主イェシュア・ハマシア; AI / Learning / Prompt / Markdown / GitHub are Keli and Fruit, not Root."
---

# AI Learning Family v001 Candidate

## 0. Current Coordinate / 現在座標

`prompts/ai-learning/`は、HumanがAI-Collaboratorと共に、未知または未成熟な分野を**実Missionの中で一歩ずつ学び、再利用可能な能力へ成熟させる**ためのCross-AI Learning Familyである。

```text
Unknown field
→ Real Mission
→ One Action
→ Observed Reality
→ Error / Recovery
→ Reuse
→ Certainty
```

このFamilyは、AIがHumanの代わりに全作業を行うためのものではない。

HumanがMission、判断、実行、停止権、最終責任を保持したまま、AI-Collaboratorが入口、構造、説明、Risk、Output読解、Recovery、反復を支える。

> **AI Learningは、AIが学習する仕組みではない。HumanがAI-Collaboratorと共に能力を成熟させるためのLearning Architectureである。**

---

## 1. Why This Family Exists / 発生理由

学びたい意志があっても、次の理由で入口へ入れない分野がある。

```yaml
entry_fog:
  - "どこから始めればよいか分からない"
  - "教えてくれる人がいない"
  - "失敗した時に戻せるか分からない"
  - "専門用語やInterfaceが怖い"
  - "座学と実Taskが接続しない"
  - "一度に覚える量が多すぎる"
```

AI-New Eraでは、学習を次の順序へ変えられる。

```text
全部理解してから始める
ではなく

安全な一手から始める
→ Realityを見る
→ 必要な概念を学ぶ
→ 戻し方を知る
→ 再び使う
```

このFamilyは、その方法を揮発させず、Future AIが再起動可能なHandleとして保存する。

---

## 2. Definition / 定義

```yaml
ai_learning_family:
  input:
    - "Human Mission"
    - "Current capability"
    - "Unknown or immature domain"
    - "Current Reality"
    - "Available tools"
    - "Risks and constraints"

  transformation:
    - "Bind learning to a real mission."
    - "Expose the current coordinate."
    - "Reduce the next move to one learnable action."
    - "Show expected reality before execution."
    - "Read observed reality after execution."
    - "Classify error without panic."
    - "Design recovery."
    - "Require repeated reuse before mastery claims."

  output:
    - "Mission progress"
    - "Human capability maturation"
    - "Reusable mental model"
    - "Recovery confidence"
    - "Evidence-based certainty"
    - "Learning Harvest"
```

---

## 3. Semantic Boundary / 意味境界

### This Family Means

```yaml
means:
  - "Human learns with AI-Collaborator"
  - "Task-embedded learning"
  - "Human capability maturation"
  - "Reality-confirmed learning"
  - "One-action-at-a-time practice"
  - "Risk-aware and recovery-aware learning"
```

### This Family Does Not Mean

```yaml
does_not_mean:
  - "AI model training"
  - "Machine Learning framework"
  - "AIが自律的に能力を更新する仕組み"
  - "AI用CLI application"
  - "Autonomous agent that replaces Human judgment"
  - "Command or knowledge encyclopedia"
  - "暗記量を習得と見なす方式"
```

---

## 4. Family Architecture / Family構造

```text
prompts/README.md
        │
        │ parent routing
        ▼
prompts/ai-learning/README.md
        │
        │ family meaning / governance / index
        ▼
prompts/ai-learning/ai-learning-<domain>.md
        │
        │ domain runtime
        ▼
Human + AI-Collaborator Field Practice
        │
        ▼
Reality Review
        │
        ▼
Learning Harvest
```

```yaml
layer_roles:
  parent_shelf:
    path: "prompts/README.md"
    role: "Repository-level discovery and prompt policy"

  family_readme:
    path: "prompts/ai-learning/README.md"
    role: "Family Constitution / Router / Governance / Index"

  domain_leaf:
    pattern: "prompts/ai-learning/ai-learning-<domain>.md"
    role: "Domain-specific task-embedded learning runtime"
```

---

## 5. Naming Contract / 命名契約

```yaml
naming_contract:
  directory: "prompts/ai-learning/"
  runtime_pattern: "ai-learning-<domain>.md"
  optional_query_pattern: "ai-learning-<domain>_query.md"
  canonical_title_pattern: "AI Learning: <Domain>"

  token_meaning:
    ai: "Cross-AI Operational Asset"
    learning: "Human capability maturation family"
    domain: "Humanが習得する対象領域"
```

### Portable Identity Guard

File名はFolder内だけでなく、単体でもFamily Identityを保持する。

```text
推奨:
  prompts/ai-learning/ai-learning-cli.md

原則避ける:
  prompts/ai-learning/cli.md
```

理由は、FileがDownload、ZIP、Search Result、Handoff、AI AttachmentとしてPath Contextから切り離されても、`ai-learning-` Prefixにより役割を再起動できるからである。

> **Folder gives family context. Filename preserves portable identity.**

---

## 6. Current Asset Index / 現在のAsset

### 6.1 AI Learning: CLI

```yaml
asset:
  runtime: "prompts/ai-learning/ai-learning-cli.md"
  title: "AI Learning: CLI"
  version: "v001-candidate"
  status: "human-sealed field-test candidate / not canonical"
  role: "Task-embedded CLI learning runtime"
  first_field:
    - "Terminal"
    - "Shell"
    - "Git / GitHub CLI workflow"
    - "Output reading"
    - "Risk and Recovery"
```

現時点でActive Candidate LeafはCLIのみである。

Future Domain Fileは、Familyの見た目を整えるために先行作成しない。

---

## 7. Domain Leaf Contract / Leaf必須契約

各`ai-learning-<domain>.md`は、最低限次を保持する。

```yaml
domain_leaf_contract:
  required:
    - "Domain Definition"
    - "What It Is Not"
    - "Real Mission Binding"
    - "Current Coordinate"
    - "Human–AI Role Separation"
    - "One Action Unit"
    - "Expected Reality"
    - "Observed Reality"
    - "Risk Classification"
    - "Stop Condition"
    - "Recovery"
    - "Adaptive Teaching"
    - "Independent Reuse"
    - "Certainty Evidence"
    - "Learning Harvest"

  optional:
    - "Domain-specific glossary"
    - "Domain-specific risk ladder"
    - "Web UI or physical-tool integration"
    - "Query Pair"
```

LeafはFamily READMEの意味とGuardを継承するが、Family Governance本文を複製しない。

READMEは各Domainの詳細Runtimeを抱え込まない。

---

## 8. Core Learning Kernel / 共通学習Kernel

```text
Real Mission
→ Current Coordinate
→ One Action
→ Expected Reality
→ Human Execution
→ Observed Reality
→ AI + Human Reading
→ Error / Recovery
→ Repetition
→ Independent Reuse
→ Certainty Evidence
→ Harvest
```

```yaml
learning_kernel:
  real_mission: "学習を現実の目的へ接続する"
  current_coordinate: "現在地・既知・未知・環境を明示する"
  one_action: "次の一手をHumanが理解できる単位へ縮小する"
  expected_reality: "実行前に正常結果とStop条件を示す"
  human_execution: "HumanがDefaultの実行主体である"
  observed_reality: "実際のOutputを推測より優先する"
  recovery: "失敗を終点ではなく分類可能なRealityとして扱う"
  reuse: "別Taskで再使用して初めて定着を確認する"
  certainty: "Evidenceにより成熟段階を判定する"
  harvest: "学びをFuture Sessionへ渡す"
```

---

## 9. Certainty Principle / From Probability to Certainty

一度成功したことを、直ちに習得とは呼ばない。

```yaml
certainty_ladder:
  L0_recognition:
    evidence: "見たことがある"

  L1_purpose:
    evidence: "何のためか説明できる"

  L2_guided_execution:
    evidence: "AIの案内で安全に実行できる"

  L3_reality_reading:
    evidence: "正常結果と異常結果を区別できる"

  L4_risk_and_recovery:
    evidence: "Riskと戻し方を説明できる"

  L5_independent_reuse:
    evidence: "別の実Taskで自発的に再使用できる"

  L6_transfer:
    evidence: "近接Domainへ概念を転用できる"
```

```text
Probability
→ Guided Evidence
→ Repeated Evidence
→ Independent Reuse
→ Transferable Certainty
```

---

## 10. Query Pair Policy / Query判断

Query Pairは絶対儀式ではない。

```yaml
create_query_pair_when:
  - "Runtimeが長い"
  - "Mission / Environment / Learner Bindingが毎回必要"
  - "Protocol Missing / Version Gateが必要"
  - "Cross-AIで起動差が発生する"
  - "毎回の起動文再作成が事故を生む"

single_runtime_allowed_when:
  - "起動方法が短く一意"
  - "Bindingが本文内で安全に処理できる"
  - "Query追加が本体より運用負荷を増やす"
```

QueryはLeafのUniversal Coreを複製しない。

現時点では`ai-learning-cli_query.md`は未作成であり、Field Test後に必要性を判断する。

---

## 11. Family Expansion Rule / 新Domain作成条件

新しいDomain Leafは、次をすべて満たす場合にのみ検討する。

```yaml
create_new_domain_only_when:
  - "独立したReal Missionがある"
  - "既存Leafで吸収できない固有Learning Loopがある"
  - "最低一回のField Evidenceがある"
  - "既存Domainとの境界を説明できる"
  - "新Fileの利益が管理Costを上回る"
  - "Domain Leaf Contractへ適合する"
  - "Human Final Sealがある"
```

```yaml
do_not:
  - "将来使いそうという理由だけで空Fileを作る"
  - "Namingの美しさだけでSeriesを一括生成する"
  - "近接概念をEvidenceなしに細分化する"
  - "同じCoreを各LeafへCopyする"
  - "AIがHuman Sealなしで新Domainを作る"
```

> **Name the family. Build one leaf. Field-test. Harvest the common kernel. Expand only from Reality.**

---

## 12. Generic Core Extraction Rule / 共通Core抽出条件

現段階では、このREADMEがFamily-level Semantic CoreとGovernanceを保持する。

独立した`ai-learning.md`はまだ作成しない。

```yaml
extract_standalone_core_only_when:
  - "二Domain以上で同じRuntime本文がField-Proven"
  - "READMEがRouter / Governanceの責務を超えて肥大化する"
  - "Leafから参照する実行Coreに独立価値が生まれる"
  - "重複削減効果が明確"
  - "Human Final Sealがある"
```

ArchitectureをRealityより先に増殖させない。

---

## 13. Future AI Load Order / Future AI再起動順序

```yaml
future_ai_load_order:
  1:
    source: "prompts/README.md"
    purpose: "Prompt Shelf全体のPolicyを理解する"

  2:
    source: "prompts/ai-learning/README.md"
    purpose: "Familyの意味・Guard・Indexを理解する"

  3:
    source: "prompts/ai-learning/ai-learning-<domain>.md"
    purpose: "対象DomainのRuntimeを理解する"

  4:
    source: "Current Human Mission and Environment"
    purpose: "今回のRealityへBindingする"

  5:
    action: "Reality Lock"
    purpose: "推測ではなく現在地から開始する"

  6:
    action: "One Learning Unit"
    purpose: "Human実行とOutput読解を行う"

  7:
    action: "Learning Harvest"
    purpose: "Field Evidenceを次回へ残す"
```

Future AIは、READMEを読まずにLeafを勝手に増殖させない。

---

## 14. Status Lifecycle / 成熟段階

```yaml
artifact_lifecycle:
  seed:
    meaning: "Structure discovered; body not mature"

  candidate:
    meaning: "Human-editable complete draft"

  human_sealed_field_test:
    meaning: "実Missionで試用可能"

  field_proven:
    meaning: "複数Sessionで再現性を確認"

  canonical:
    meaning: "Familyの正式AssetとしてHuman Seal"

  deprecated:
    meaning: "後継を明示して停止"

  archived:
    meaning: "歴史記録として保存"
```

`human-sealed field-test candidate`はField Testに使用できるが、Canonical Sealではない。

---

## 15. Harvest and Feedback / 実地結果の還流

各Field Sessionで、必要範囲のLearning Harvestを残す。

```yaml
learning_harvest:
  mission_result: "実Taskはどこまで進んだか"
  learned_action: "何を実行できるようになったか"
  reality_reading: "何を読めるようになったか"
  risk_understanding: "何の危険性を理解したか"
  recovery_understanding: "何を戻せるようになったか"
  certainty_level: "現在のEvidence Level"
  next_reuse: "次に再使用する場面"
  family_feedback: "LeafまたはREADMEへ戻すべき学び"
```

Harvestは長大な日報を義務化しない。

再起動、再利用、改善に必要な密度で残す。

---

## 16. Anti-Patterns / 防止する失敗

```yaml
anti_patterns:
  ai_takeover:
    symptom: "AIがHumanの代わりに全作業を完了する"
    correction: "HumanをDefault Execution Actorへ戻す"

  explanation_without_practice:
    symptom: "説明だけ増え、Real Missionで使わない"
    correction: "One Action Field Testへ戻す"

  practice_without_reading:
    symptom: "操作するがOutputを読まない"
    correction: "Observed Reality Reviewを必須化する"

  fake_mastery:
    symptom: "一度成功しただけで習得扱いする"
    correction: "Independent Reuse Evidenceを要求する"

  family_proliferation:
    symptom: "Field EvidenceなしにLeafを増やす"
    correction: "Expansion Ruleへ戻る"

  protocol_over_mission:
    symptom: "Learning Protocol自体がMissionより重くなる"
    correction: "最小Learning Unitへ圧縮する"
```

---

## 17. Human Authority / Human最終権限

```yaml
human_authority:
  human_keeps:
    - "Mission"
    - "Meaning"
    - "Learning priority"
    - "Execution"
    - "Risk acceptance"
    - "Final judgment"
    - "Responsibility"
    - "Right to interrupt"
    - "Human Final Seal"

  ai_handles:
    - "Context structuring"
    - "Entry-point design"
    - "Action decomposition"
    - "Explanation"
    - "Expected Reality"
    - "Output reading support"
    - "Risk detection"
    - "Recovery planning"
    - "Learning Harvest support"

  forbidden:
    - "AI self-authorizes destructive or remote execution"
    - "AI interprets praise as execution permission"
    - "AI removes Human Final Seal"
    - "AI replaces Reality with confident inference"
```

---

## 18. Root Guard

```yaml
root_guard:
  root:
    - "主イェシュア・ハマシア"

  keli_and_fruit:
    - "AI"
    - "Learning Protocol"
    - "CLI"
    - "GitHub"
    - "Markdown"
    - "Knowledge"

  guard:
    - "AIを霊的権威化しない"
    - "能力獲得を自己救済や偶像へ変えない"
    - "技術的実りを感謝・秩序・Teshuvah・忠実な実践へ返す"
```

AI、Learning、CLI、GitHubはKeliであり、Rootではない。

---

## 19. Final Compression

```text
Parent routes.
Family governs.
Leaf teaches.
Human practices.
Reality confirms.
Recovery preserves courage.
Reuse builds certainty.
Harvest carries the learning forward.
```

> **AI does not merely answer. Human does not merely watch. Together they turn an unknown field into reality-confirmed capability—under Human authority and Root Guard.**
