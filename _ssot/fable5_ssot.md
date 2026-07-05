---
title: "Fable5 SSOT"
canonical_name: "Fable5 Single Source of Truth"
version: "v001.1"
version_note: "v001.1 appends the Ark05 observed usage timeline from same-thread Fable5 screenshots so Future AI can reuse the data even if it cannot access the original images."
status: "human-editable / growing-ledger"
canonical_path: "_ssot/fable5_ssot.md"
role: "Fable5 usage / limit / effort / answer weight / breakthrough / adopted-patch SSOT"
growth_model: "append-only / thread-by-thread update"
language_policy: "Japanese-first / English-anchor"
core_formula:
  - "Measure usage."
  - "Record effort."
  - "Classify answer weight."
  - "Extract breakthrough."
  - "Adopt one."
  - "Backlog the rest."
  - "Update operating rule."
root: "主イェシュア・ハマシア"
root_guard: "Root is 主イェシュア・ハマシア; AI / Fable5 / ChatGPT / Grok / X / GitHub / Revenue are Fruit."
---

# Fable5 SSOT

## 0. What This File Is / このFileの役割

このFileは、Fable5について分かったことを一箇所に積み上げる **Single Source of Truth** である。

これは単なる感想メモではない。

このFileの中心は、以下を記録することである。

```text
どのEffortで、
どのくらいのAI回答が返り、
使用量が何%動き、
何がBreakthroughになり、
何を採用し、
何をBacklogにしたか。
```

Fable5は強いAIとして雑に使うのではなく、制限つき高倍率リソースとして扱う。

そのため、Fable5の価値は感覚ではなく、以下で見る。

```text
Usage %
Effort
Answer Weight
Breakthrough
Adopted Patch
Backlog
Next Operating Rule
```

---

## 1. Current Summary / 現在Summary

```yaml
current_summary:
  file: "_ssot/fable5_ssot.md"
  status: "growing SSOT"
  main_question:
    - "Fable5は、どのEffortで、どれくらい使用量%を消費し、どんな価値を返すのか？"

  current_best_use:
    - "GitHub canonical化前の設計監査"
    - "新規Skill作成前のCritical Flaw Review"
    - "重大設計判断前の高倍率Review"
    - "Move37的新要素の発見"

  current_best_effort_guess:
    new_skill_precommit_review: "高"
    one_critical_flaw_audit: "高"
    unknown_exploration: "超高 may be useful"
    light_confirmation: "中"
    copy_edit: "Fable5不要"

  current_key_breakthroughs:
    - "One New Element Rule"
    - "Safety Inheritance Gap"
    - "Safety Inheritance Rule"
    - "Fable5 as high-magnification design auditor"
```

---

## 2. Usage Delta Ledger / 使用量差分台帳

### 2.1 Purpose

Fable5使用時に最重要なのは、**どの回答で何%使ったか** を記録することである。

感想ではなく、差分で見る。

```text
Before Screenshot
→ Fable5 Answer
→ After Screenshot
→ Usage Delta
→ Adopted Breakthrough
```

### 2.2 Record Template

```yaml
usage_delta_record:
  id:
  date:
  thread:
  model: "Fable5"
  effort:
  task_type:

  before_snapshot:
    captured: true_or_false
    current_session_usage:
    weekly_all_models_usage:
    weekly_fable_only_usage:
    note:

  after_snapshot:
    captured: true_or_false
    current_session_usage:
    weekly_all_models_usage:
    weekly_fable_only_usage:
    note:

  delta:
    current_session_delta:
    weekly_all_models_delta:
    weekly_fable_only_delta:
    confidence: "exact / estimated / unknown"

  answer:
    answer_weight_class: "S / M / L / XL / XXL"
    answer_type: "review / audit / draft / rewrite / plan / markdown / code"
    rough_length:
    structure_level:
    unique_value:

  result:
    judgment:
    breakthrough:
    adopted_patch:
    backlog:
    rejected:

  efficiency:
    breakthrough_per_usage_percent:
    adopted_patch_per_usage_percent:
    roi_judgment:
    should_use_again:
```

### 2.3 Measurement Rule

```text
Deltaが取れていない使用量Snapshotは、価値があるが不完全。
Before / After が揃って初めて「この回答で何%使ったか」を推定できる。
```

---

## 3. Screenshot Ledger / 画像Snapshot台帳

### 3.1 Purpose

Fable5のUI使用状況画像は、制限・使用量・運用判断の一次観測になる。

画像Uploadから読み取った数値は、以下のように扱う。

```text
observed = 画像で確認した値
user-reported = ユーザー発言で確認した値
unverified = 未確認
unknown = 不明
```

### 3.2 Snapshot Record: 2026-07-04 / Ark05 / C2XC Review後

```yaml
screenshot_record:
  id: "fable5_usage_snapshot_20260704_ark05_001"
  source: "user uploaded screenshot"
  timing: "after Fable5 review / exact before snapshot not captured"

  observed_values:
    current_session_usage: "11% used"
    weekly_all_models_usage: "3% used"
    weekly_fable_only_usage: "6% used"

  before_snapshot:
    captured: false
    value: "unknown"

  delta:
    current_session_delta: "unknown"
    weekly_all_models_delta: "unknown"
    weekly_fable_only_delta: "unknown"
    reason: "Before Snapshotがないため、このFable5回答単体の消費%は確定不可"

  interpretation:
    - "この時点ではFable5使用量は軽めに見える"
    - "Effort 高の設計Reviewを選択投入する余地あり"
    - "ただし、この1回答の正確な消費%は未確定"

  next_measurement_rule:
    - "Fable5使用前にBefore Screenshotを保存"
    - "Fable5回答後にAfter Screenshotを保存"
    - "Before → After の差分%を記録"
```

---

## 4. Limit / Plan / Availability Notes / 制限・契約・利用可能性

このSectionは、Fable5の利用条件・制限・UI表示を記録する。

数値は必ず出典状態を付ける。

```yaml
limit_record_template:
  date:
  source_type: "observed / user-reported / unverified"
  plan_or_subscription:
  price:
  available_until:
  weekly_limit:
  session_limit:
  model_specific_limit:
  ui_warning:
  uncertainty:
  next_check:
```

### Current Notes

```yaml
current_notes:
  subscription_status:
    source_type: "user-reported"
    note: "ユーザーはFable5を契約・利用中"

  price:
    source_type: "user-reported"
    note: "約3000円という認識"

  availability_until:
    source_type: "user-reported"
    note: "7/7までという認識あり"
    caution: "日付・条件はUIまたは公式表示で再確認推奨"

  current_usage_snapshot:
    source_type: "observed"
    current_session_usage: "11%"
    weekly_all_models_usage: "3%"
    weekly_fable_only_usage: "6%"
```

---

## 5. Effort Ledger / エフォート台帳

### 5.1 Effort Meaning

```yaml
effort_scale_user_observed:
  低:
    meaning: "quick / simple"
    best_for:
      - "軽い確認"
      - "短い判断"
  中:
    meaning: "light casual"
    best_for:
      - "軽いReview"
      - "低リスク確認"
  高:
    meaning: "balanced default"
    best_for:
      - "新規SkillのPre-Commit Review"
      - "One Critical Flaw Audit"
      - "設計監査"
  超高:
    meaning: "complex / detailed"
    best_for:
      - "未知領域探索"
      - "複雑な設計比較"
      - "広めのReview"
  最大:
    meaning: "hardest / slowest"
    best_for:
      - "原則温存"
      - "未知かつ高難度かつ失敗コストが高い場合のみ"
```

### 5.2 Effort Record: C2XC v001 Pre-Commit Review

```yaml
effort_record:
  id: "fable5_effort_high_c2xc_precommit_001"
  task: "chatgpt-to-xchain_skill.md v001 pre-commit review"
  effort: "高"
  query_style: "One Critical Flaw audit"
  result: "Conditional Pass"
  critical_flaw_found: "Safety Inheritance Gap"
  adopted_patch: "Safety Inheritance Rule"

  judgment:
    - "Effort 高で十分に急所へ届いた"
    - "超高にしなくても、Queryが鋭ければCritical Flawを検出できる"
    - "新規SkillのGitHub投入前Reviewは、まず高が王道"

  next_rule:
    - "Effortを上げる前にQueryを鋭くする"
    - "高で浅い場合は、まずQueryを修正し、それでも不足なら超高へ上げる"
```

---

## 6. Answer Weight Ledger / AI回答重量台帳

### 6.1 Why This Exists

「どのくらいのAI回答で何%使ったか」を測るには、回答の大きさ・重さを分類する必要がある。

### 6.2 Answer Weight Classes

```yaml
answer_weight_class:
  S:
    meaning: "短い確認・軽い判断"
    examples:
      - "Yes/No判断"
      - "短い要約"
      - "軽い文体修正"

  M:
    meaning: "数項目Review・短め判断"
    examples:
      - "3〜5項目のReview"
      - "短い改善案"
      - "軽い比較"

  L:
    meaning: "構造化Review・Patch提案あり"
    examples:
      - "Conditional Pass"
      - "One Critical Flaw候補"
      - "Minimal Patch"
      - "Keep / Do not add"

  XL:
    meaning: "Critical Flaw検出・運用Rule化可能"
    examples:
      - "重大欠陥の命名"
      - "採用Patchの明確化"
      - "GitHub readiness判断"
      - "次回Ruleへの展開"

  XXL:
    meaning: "大規模Markdown生成・大規模再設計"
    examples:
      - "全文Artifact生成"
      - "複数System Patch統合"
      - "長大設計書"
```

### 6.3 Answer Weight Record: C2XC Review

```yaml
answer_weight_record:
  id: "answer_weight_fable5_c2xc_review_001"
  effort: "高"
  estimated_class: "L to XL"
  reason:
    - "Overall Judgment: Conditional Pass"
    - "One Critical Flaw: Safety Inheritance Gap"
    - "Minimal Patch提示"
    - "What to keep unchanged"
    - "What not to add"
    - "GitHub readiness"
    - "One-sentence final advice"

  usage_delta:
    exact: "unknown"
    reason: "Before Snapshotなし"

  value_judgment:
    - "回答重量に対してBreakthroughが明確"
    - "C2XC v001のGitHub投入前に採用すべきPatchを1つ出した"
    - "High ROIと判断"
```

---

## 7. Review Query Ledger / Review Query台帳

### 7.1 Purpose

Fable5の性能は、EffortだけでなくQuery設計に大きく依存する。

悪いQuery:

```text
このSkillをReviewしてください。
```

良いQuery:

```text
GitHub commit前に止めるべきOne Critical Flawだけ見つけてください。
```

### 7.2 Reusable Query Pattern: One Critical Flaw Audit

```text
You are reviewing a new Ark Skill Card before GitHub canonicalization.

Review goal:
Do not expand the skill unnecessarily.
Do not propose many features.
Look for one critical flaw that should be fixed before GitHub commit.

Please review for:
1. Role separation
2. Safety
3. Required structure preservation
4. One New Element
5. Simple is best
6. Failure conditions

Output format:
A. Overall Judgment
- Pass / Conditional Pass / Stop

B. One Critical Flaw
- Name:
- Why it matters:
- Minimal patch:

C. What to keep unchanged

D. What not to add

E. GitHub readiness
- Ready now / Ready after one patch / Not ready

F. One-sentence final advice
```

### 7.3 Query Rule

```text
Fable5には、広く考えさせるより、監査対象を狭く切る。
```

---

## 8. Review Result Ledger / Review結果台帳

### 8.1 Record Template

```yaml
review_result_record:
  id:
  date:
  target:
  purpose:
  effort:
  query_type:
  answer_weight:
  judgment:
  critical_flaw:
  minimal_patch:
  keep_unchanged:
  do_not_add:
  adopted:
  rejected:
  backlog:
  github_readiness:
  final_advice:
```

### 8.2 Record: C2XC v001 Pre-Commit Review

```yaml
review_result_record:
  id: "fable5_review_c2xc_v001_precommit_001"
  date: "2026-07-04"
  target: "chatgpt-to-xchain_skill.md v001 Draft"
  purpose: "GitHub commit前の重大欠陥チェック"
  effort: "高"
  query_type: "One Critical Flaw Audit"
  answer_weight: "L to XL"

  judgment: "Conditional Pass"

  critical_flaw:
    name: "Safety Inheritance Gap / 安全制約の相続切断"
    meaning: "Chain PostがParent Postの流れは相続しているが、Parent Post生成時の禁止事項・要確認情報・Do-Not-Amplify状態を相続していない"

  minimal_patch:
    - "parent_constraintsを追加"
    - "Safety Inheritance Ruleを追加"
    - "Risk Checkへ安全項目追加"
    - "Failure Conditionへ要確認情報の復活を追加"

  keep_unchanged:
    - "Do not be clever before preserving structure"
    - "one_post_chain Default"
    - "One New Element設計"
    - "Final Summary Rule"

  do_not_add:
    - "Multi-post Thread Mode"
    - "Dual-Layer移植"
    - "Difference Map移植"
    - "Pre-Verbalization Rule複製"
    - "Title micro-rules追加"

  adopted:
    - "Safety Inheritance Rule"

  later_user_correction:
    - "Same-Thread Context Rail"

  github_result:
    path: "_skill/skills/chatgpt-to-xchain_skill.md"
    commit_message: "Add chatgpt-to-xchain skill"
    commit_sha: "d23d132c64d25c25d9344da4ccd141244fc104a3"
```

---

## 9. Breakthrough Ledger / 突破口台帳

### 9.1 Breakthrough Definition

Breakthroughとは、単なる良い回答ではない。

Breakthroughとは、次回以降のWorkflowに再利用できる構造・Rule・Guard・判断基準である。

```text
Good answer = その場で役に立つ。
Breakthrough = 次回以降も勝率を上げる。
```

### 9.2 Breakthrough Record: One New Element Rule

```yaml
breakthrough_record:
  id: "one_new_element_rule_001"
  source: "Fable5 Review / C2X improvement"
  name: "One New Element Rule / 1回答1新要素Rule"
  class: "Move37-level operating principle"

  definition:
    - "AI回答は、可能な限り、元情報にGroundedした新要素を1つだけ加える"
    - "新要素は、判断基準・Guard・比喩・分類軸・次Action・失敗条件・圧縮文・運用Ruleのいずれかでよい"

  core:
    - "ゼロ新要素 = 死んだ要約"
    - "複数新要素 = 散る"
    - "1つの新要素 = 前進する"

  why_it_matters:
    - "AI回答を単なる整理から前進へ変える"
    - "全AI回答へ横展開できる"
    - "C2X / C2XCだけでなく、Review / Plan / Handoff / SSOT作成にも適用可能"

  guard:
    - "新要素は思いつきではなく、元情報と目的にGroundedしていること"
    - "新要素は原則1つに絞ること"
```

### 9.3 Breakthrough Record: Safety Inheritance Gap

```yaml
breakthrough_record:
  id: "safety_inheritance_gap_001"
  source: "Fable5 C2XC Review"
  name: "Safety Inheritance Gap / 安全制約の相続切断"

  definition:
    - "Chain PostがParent Postの流れだけを相続し、Parent Post生成時の禁止事項・要確認情報・断定禁止表現を相続していない状態"

  adopted_patch:
    - "Safety Inheritance Rule"

  why_it_matters:
    - "深掘りChainは要確認情報へ自然に漂流しやすい"
    - "First Postで捨てた危険ClaimがChainで復活する可能性がある"
    - "GitHub canonical化前に塞ぐべき重大欠陥だった"
```

---

## 10. One New Element Rule / 1回答1新要素Rule

このRuleは、Fable5由来のMove37的Breakthroughとして、全AI回答に横展開する。

### Definition

```text
AI回答は、単なる要約・整理・同意で終わらず、
元情報にGroundedした新要素を1つだけ加える。
```

### New Element Types

```yaml
one_new_element_types:
  - "新しい判断基準"
  - "新しいGuard"
  - "新しい比喩"
  - "新しい分類軸"
  - "新しい次Action"
  - "新しい失敗条件"
  - "新しい圧縮文"
  - "新しい運用Rule"
```

### Core

```text
ゼロ新要素 = 死んだ要約。
複数新要素 = 散る。
1つの新要素 = 前進する。
```

### Guard

```text
新要素は、文脈にGroundedしていなければならない。
新要素は、回答を膨張させるためではなく、次の一手を明確にするために入れる。
```

---

## 11. Adopted Patch Ledger / 採用Patch台帳

```yaml
adopted_patch_record:
  id: "c2xc_safety_inheritance_rule_001"
  source: "Fable5 Review"
  target: "chatgpt-to-xchain_skill.md v001"
  patch_name: "Safety Inheritance Rule / 安全制約相続Rule"
  adopted: true
  reason:
    - "C2XCが親Postの禁止事項を相続していなかった"
    - "Chain深掘りで要確認情報が復活する危険があった"
  result:
    - "C2XC v001に統合"
    - "GitHub commit済み"
```

```yaml
adopted_patch_record:
  id: "c2xc_same_thread_context_rail_001"
  source: "User correction"
  target: "chatgpt-to-xchain_skill.md v001"
  patch_name: "Same-Thread Context Rail / 同一Thread文脈Rail"
  adopted: true
  reason:
    - "HumanにParent PostやConstraintsを再貼付させるWorkflowは重い"
    - "同一Thread内に既にある情報はAIが読むべき"
  core:
    - "Humanは「次へ」と言う"
    - "AIは「これまで」を読む"
  result:
    - "C2XC v001に統合"
    - "GitHub commit済み"
```

---

## 12. Backlog Ledger / Backlog台帳

```yaml
backlog:
  - item: "Effort 高 vs 超高 usage delta comparison"
    reason: "高で十分な場面と超高が必要な場面を切り分ける"

  - item: "Before / After Screenshot comparison over multiple Fable5 calls"
    reason: "1回答あたり使用量%を推定する"

  - item: "Move37 New Element tracking across AI responses"
    reason: "One New Element Ruleが全AI回答でどれくらい成果を出すか見る"

  - item: "Fable5 answer weight calibration"
    reason: "S/M/L/XL/XXL分類と使用量%の関係を測る"

  - item: "High effort pre-commit review standard query"
    reason: "新規Skill投入前の標準Queryを固定する"
```

---

## 13. Operating Rules / 運用Rule

### Rule 1: Before / After Screenshot Rule

```text
Fable5使用前にBefore Screenshotを保存する。
Fable5回答後にAfter Screenshotを保存する。
差分%をUsage Delta Ledgerへ記録する。
```

### Rule 2: One Critical Flaw Audit Rule

```text
新規SkillのGitHub投入前は、Fable5に「重大欠陥を1つだけ」探させる。
```

### Rule 3: Effort Before Escalation Rule

```text
Effortを上げる前に、Queryを鋭くする。
```

### Rule 4: Extract Many / Adopt One / Backlog the Rest

```text
多く回収し、一つだけ実装し、残りを未来資産にする。
```

### Rule 5: One New Element Rule

```text
AI回答には、元情報にGroundedした新要素を1つだけ入れる。
```

---

## 14. Current Best Effort Rule / 現時点Effort方針

```yaml
current_best_effort_rule:
  low:
    use_for:
      - "短い確認"
      - "軽い言い換え"
    note: "Fable5でなくてもよい場合が多い"

  medium:
    use_for:
      - "軽いReview"
      - "低リスク確認"

  high:
    use_for:
      - "新規Skill Pre-Commit Review"
      - "One Critical Flaw Audit"
      - "設計監査"
    current_judgment:
      - "今回のC2XC Reviewでは高で十分に急所へ届いた"

  ultra_high:
    use_for:
      - "未知領域探索"
      - "複雑な設計比較"
      - "高で浅かった場合の再Review"

  max:
    use_for:
      - "原則温存"
      - "未知かつ高難度かつ失敗コストが高い場合のみ"
```

---

## 15. Case Record: C2XC v001 Pre-Commit Review

```yaml
case_record:
  id: "case_c2xc_v001_precommit_review"
  thread: "Ark05"
  target: "chatgpt-to-xchain_skill.md v001"
  purpose: "GitHub新規作成前の重大欠陥Review"
  fable5_effort: "高"

  fable5_result:
    overall_judgment: "Conditional Pass"
    one_critical_flaw: "Safety Inheritance Gap"
    github_readiness: "Ready after one patch"

  adopted_from_fable5:
    - "Safety Inheritance Rule"

  added_by_user_correction:
    - "Same-Thread Context Rail"

  final_github_commit:
    repo: "yusukefujiijp/ai-project"
    path: "_skill/skills/chatgpt-to-xchain_skill.md"
    commit_message: "Add chatgpt-to-xchain skill"
    commit_sha: "d23d132c64d25c25d9344da4ccd141244fc104a3"

  usage_snapshot:
    after_snapshot_observed:
      current_session_usage: "11%"
      weekly_all_models_usage: "3%"
      weekly_fable_only_usage: "6%"
    before_snapshot: "not captured"
    delta: "unknown"

  judgment:
    - "Fable5 Effort 高は、このPre-Commit Reviewに対してHigh ROIだった"
    - "次回からBefore / After Snapshotを撮ることで、使用量%あたりのBreakthroughを測定する"
```

---

## 16. Update Rule / 更新Rule

このFileはAppend-onlyで育てる。

新しいFable5使用があるたびに、最低限以下を追記する。

```yaml
minimum_update_packet:
  usage_delta:
    before_snapshot:
    after_snapshot:
    delta:
  effort:
  answer_weight:
  review_result:
  breakthrough:
  adopted_patch:
  backlog:
  next_rule:
```

### Natural Stop Rule

```text
SSOT更新は、完璧に書こうとして止まらない。
最低限、Usage Snapshot / Effort / Result / Adopted Patch だけ入れればよい。
```

---

## 17. Root Guard

```text
Root is 主イェシュア・ハマシア.

Fable5はRootではない。
ChatGPTもRootではない。
GrokもRootではない。
GitHubもRootではない。
XもRevenueもRootではない。

AIはFruitであり、Toolであり、Stewardship対象である。
Human Final Sealは残る。
```

---

## 18. Final Compression

Fable5 SSOTの本丸は、  
「Fable5は良かった」という感想ではない。

どのEffortで、  
どのくらいのAI回答が出て、  
使用量が何%動き、  
何が採用され、  
何がBreakthroughだったか。

これを積み上げること。

Fable5は、  
高倍率設計監査官であり、  
Move37的新要素発見器である。

ただし、制限つきリソースである。

だから、燃費を見る。

```text
Before
→ Answer
→ After
→ Delta
→ Breakthrough
→ Adopted Patch
```

One New Element Ruleは、全AI回答に使える。

```text
ゼロ新要素 = 死んだ要約。
複数新要素 = 散る。
1つの新要素 = 前進する。
```

Effortを上げる前に、Queryを鋭くする。

多く回収し、  
一つだけ実装し、  
残りを未来資産にする。

Usage %
× Effort
× Answer Weight
× Breakthrough
= Fable5 Living Review

---

## 19. Observed Usage Timeline: Ark05 / 2026-07-04

### 19.1 Purpose / このSectionの目的

このSectionは、Ark05 Thread内にUploadされたFable5使用状況画像から、現AIが読み取れた使用率・Effort・関連作業内容をFuture AIへ渡すための観測Recordである。

重要:

```text
Ruleだけでは未来へ渡らない。
Observed Recordを残して初めて、Future AIが同じ盤面から再開できる。
```

Future AIは、このThread内画像を読めない可能性がある。  
したがって、現AIが読める使用率Snapshot・Effort・作業内容・推定境界をSSOTへ固定する。

このSectionでは、以下を分けて記録する。

```text
observed = 画像またはGitHub結果から直接確認できる
inferred = 時系列・作業内容から合理的に推定した
unknown = 確定できない
```

---

### 19.2 Observed Screenshot Timeline / 画像から読めた使用率推移

```yaml
observed_usage_timeline:
  thread: "Ark05"
  source: "same-thread uploaded Fable5 usage screenshots / contact sheet"
  status: "AI-observed visual data"
  confidence: "high for visible percentages / medium for alignment to exact per-answer boundaries"

  snapshots:
    - label: "initial_zero_state"
      visible_time: "not visible / unknown"
      source_type: "observed_from_image"
      screen_type: "usage_status"
      current_session_usage: "0%"
      weekly_all_models_usage: "0%"
      weekly_fable_only_usage: "0%"
      note:
        - "Fableがまだ使用されていない、または使用開始前に近い初期状態として扱う"
        - "画面下部に『この期間中、Fableはまだ使用されていません』に近い表示あり"

    - label: "effort_selection"
      visible_time: "15:33"
      source_type: "observed_from_image"
      screen_type: "effort_selection"
      selected_effort: "高"
      effort_options_visible:
        - "低"
        - "中"
        - "高"
        - "超高"
        - "最大"
      note:
        - "Effort選択画面で『高』にチェックあり"
        - "説明上、『高』はデフォルト / balanced寄りとして扱える"

    - label: "usage_snapshot_1600"
      visible_time: "16:00"
      source_type: "observed_from_image"
      screen_type: "usage_status"
      current_session_usage: "7%"
      weekly_all_models_usage: "0%"
      weekly_fable_only_usage: "1%"
      reset_notes_visible:
        current_session: "約4時間49分後にリセット"
      note:
        - "Fable5使用が開始された後の初期Snapshot"
        - "weekly Fable onlyが0%から1%へ増加"

    - label: "usage_snapshot_1749"
      visible_time: "17:49"
      source_type: "observed_from_image"
      screen_type: "usage_status"
      current_session_usage: "14%"
      weekly_all_models_usage: "2%"
      weekly_fable_only_usage: "3%"
      reset_notes_visible:
        current_session: "約3時間0分後にリセット"
        weekly_all_models: "リセット: 1日10:00"
        weekly_fable_only: "リセット: 1日10:00"
      note:
        - "Fable5関連作業が進んだ中盤Snapshot"
        - "weekly all modelsが2%、weekly Fable onlyが3%へ増加"

    - label: "upgrade_screen_1809"
      visible_time: "18:09"
      source_type: "observed_from_image"
      screen_type: "subscription_or_upgrade_information"
      usage_values: "not a usage percentage screen"
      note:
        - "使用率Snapshotではない"
        - "Fable5利用環境・制限理解に関係する可能性がある画像"
        - "『コンテンツをレベルアップ』等の表示が見える"

    - label: "usage_snapshot_1943"
      visible_time: "19:43"
      source_type: "observed_from_image"
      screen_type: "usage_status"
      current_session_usage: "29%"
      weekly_all_models_usage: "3%"
      weekly_fable_only_usage: "5%"
      reset_notes_visible:
        current_session: "約1時間6分後にリセット"
        weekly_all_models: "リセット: 19:59"
        weekly_fable_only: "リセット: 19:59"
      note:
        - "Current Session使用率の最大観測値"
        - "weekly Fable onlyが5%へ増加"
        - "この時点までにFable5関連作業がかなり進んだと見られる"

    - label: "usage_snapshot_2225"
      visible_time: "22:25"
      source_type: "observed_from_image"
      screen_type: "usage_status"
      current_session_usage: "11%"
      weekly_all_models_usage: "3%"
      weekly_fable_only_usage: "6%"
      reset_notes_visible:
        current_session: "約4時間54分後にリセット"
      note:
        - "最終観測Snapshot"
        - "Current Sessionが29%から11%へ下がっているため、Session resetが発生した可能性が高い"
        - "weekly Fable onlyは5%から6%へ増加"

    - label: "fable_answer_screenshot"
      visible_time: "not clearly used for usage percentage"
      source_type: "observed_from_image"
      screen_type: "fable_answer_sample"
      content_summary:
        - "Minecraftの新規な世界観設定、Mojang技術デモ、ゲーム内惑星などに関する日本語回答が見える"
      note:
        - "使用率画面ではない"
        - "同Thread内でFable5回答実例が存在したことを示す画像"
        - "C2XC Reviewとの直接対応は未確定"
```

---

### 19.3 Human-readable Usage Table / 人間用Table

| Snapshot | Time | Current Session | Weekly All Models | Weekly Fable Only | Evidence | Note |
|---|---:|---:|---:|---:|---|---|
| initial_zero_state | unknown | 0% | 0% | 0% | observed | Fable未使用に近い初期状態 |
| effort_selection | 15:33 | n/a | n/a | n/a | observed | Effort「高」が選択されていた |
| usage_snapshot_1600 | 16:00 | 7% | 0% | 1% | observed | Fable使用開始後の初期Snapshot |
| usage_snapshot_1749 | 17:49 | 14% | 2% | 3% | observed | 中盤Snapshot |
| upgrade_screen_1809 | 18:09 | n/a | n/a | n/a | observed | 使用率ではなく契約/アップグレード画面 |
| usage_snapshot_1943 | 19:43 | 29% | 3% | 5% | observed | Current Session最大観測値 |
| usage_snapshot_2225 | 22:25 | 11% | 3% | 6% | observed | Session reset後の可能性あり |
| fable_answer_screenshot | unknown | n/a | n/a | n/a | observed | Fable回答実例。Minecraft関連内容が見える |

---

## 20. Thread-Level Before / After Reconstruction

### 20.1 Core Finding

このThread内で観測できる最重要の使用率推移は以下である。

```text
Weekly Fable only:
0% → 1% → 3% → 5% → 6%
```

Current Sessionは以下のように推移した。

```text
Current Session:
0% → 7% → 14% → 29% → 11%
```

ただし、`29% → 11%` は減少しているため、Current Sessionは途中でresetされた可能性が高い。  
そのため、Thread全体の累積を見るには、Current Sessionよりも **weekly Fable only usage** の方が安定した指標である。

---

### 20.2 Thread-Level Reconstruction

```yaml
thread_level_before_after_reconstruction:
  before:
    label: "initial_zero_state"
    current_session_usage: "0%"
    weekly_all_models_usage: "0%"
    weekly_fable_only_usage: "0%"
    evidence: "observed_from_image"

  progression:
    - label: "usage_snapshot_1600"
      current_session_usage: "7%"
      weekly_all_models_usage: "0%"
      weekly_fable_only_usage: "1%"
      delta_from_initial:
        current_session: "+7%"
        weekly_all_models: "+0%"
        weekly_fable_only: "+1%"

    - label: "usage_snapshot_1749"
      current_session_usage: "14%"
      weekly_all_models_usage: "2%"
      weekly_fable_only_usage: "3%"
      delta_from_initial:
        current_session: "+14%"
        weekly_all_models: "+2%"
        weekly_fable_only: "+3%"

    - label: "usage_snapshot_1943"
      current_session_usage: "29%"
      weekly_all_models_usage: "3%"
      weekly_fable_only_usage: "5%"
      delta_from_initial:
        current_session: "+29%"
        weekly_all_models: "+3%"
        weekly_fable_only: "+5%"
      note:
        - "Current Session最大観測値"

    - label: "usage_snapshot_2225"
      current_session_usage: "11%"
      weekly_all_models_usage: "3%"
      weekly_fable_only_usage: "6%"
      stable_weekly_delta_from_initial:
        weekly_all_models: "+3%"
        weekly_fable_only: "+6%"
      current_session_delta_from_initial:
        value: "not safe as continuous delta"
        reason: "Session resetが発生した可能性が高い"
```

---

### 20.3 Practical Interpretation

```yaml
practical_interpretation:
  most_stable_observed_delta:
    metric: "weekly_fable_only_usage"
    from: "0%"
    to: "6%"
    delta: "+6%"
    interpretation:
      - "同Thread観測内で、Fable only weekly usageは少なくとも6ポイント増加した"

  current_session_peak:
    metric: "current_session_usage"
    peak: "29%"
    time: "19:43"
    interpretation:
      - "少なくとも一時点で、Current Session usageは29%まで上昇した"

  session_reset_warning:
    observed: true
    evidence:
      - "19:43 = current session 29%"
      - "22:25 = current session 11%"
    interpretation:
      - "19:43から22:25の間にCurrent Session resetが起きた可能性が高い"
      - "Current SessionだけでThread全体消費を読むと誤る可能性がある"
```

---

## 21. Work Performed During Observed Usage Window

### 21.1 Purpose

使用率データだけでは不十分である。  
Future AIが再利用できるように、**何をしてその使用率になったのか**を同時に保存する。

---

### 21.2 Reconstructed Work Summary

```yaml
work_performed_during_observed_usage_window:
  thread: "Ark05"
  broad_task:
    - "Fable5 usage experiment"
    - "Fable5 effort observation"
    - "C2XC skill review"
    - "C2XC GitHub canonicalization"
    - "Fable5 SSOT creation"

  reconstructed_steps:
    - step: 1
      evidence_status: "observed"
      description: "Fable5のEffort選択画面で『高』が選択されていた"

    - step: 2
      evidence_status: "thread_context"
      description: "Fable5に chatgpt-to-xchain_skill.md v001 Draft のPre-Commit Reviewを依頼した"

    - step: 3
      evidence_status: "thread_context"
      description: "Review形式は One Critical Flaw Audit だった"

    - step: 4
      evidence_status: "thread_context"
      description: "Fable5回答は Overall Judgment = Conditional Pass だった"

    - step: 5
      evidence_status: "thread_context"
      description: "Fable5は One Critical Flaw として Safety Inheritance Gap を検出した"

    - step: 6
      evidence_status: "thread_context"
      description: "Fable5は Minimal Patch として Safety Inheritance Rule を提示した"

    - step: 7
      evidence_status: "thread_context"
      description: "ChatGPTがSafety Inheritance RuleをC2XC v001へ統合した"

    - step: 8
      evidence_status: "thread_context"
      description: "User correctionにより Same-Thread Context Rail を追加した"

    - step: 9
      evidence_status: "thread_context"
      description: "ChatGPTがC2XC v001 Final Markdownを生成した"

    - step: 10
      evidence_status: "observed_github_result"
      description: "GitHubへ _skill/skills/chatgpt-to-xchain_skill.md を新規作成した"
      commit:
        repo: "yusukefujiijp/ai-project"
        path: "_skill/skills/chatgpt-to-xchain_skill.md"
        commit_message: "Add chatgpt-to-xchain skill"
        commit_sha: "d23d132c64d25c25d9344da4ccd141244fc104a3"

    - step: 11
      evidence_status: "thread_context"
      description: "Fable5使用率・Effort・回答重量・Breakthroughを記録するSSOTを設計した"

    - step: 12
      evidence_status: "observed_github_result"
      description: "GitHubへ _ssot/fable5_ssot.md を新規作成した"
      commit:
        repo: "yusukefujiijp/ai-project"
        path: "_ssot/fable5_ssot.md"
        commit_message: "Add fable5 SSOT"
        commit_sha: "172461072d24ca79a5c8b845727b78f6518321d5"
```

---

### 21.3 Cost Attribution Guard / 使用量帰属Guard

Fable5の使用率とChatGPT側の後続作業を混同してはいけない。

```yaml
cost_attribution_guard:
  fable5_usage_scope:
    includes:
      - "Fable5へ投げたQuery"
      - "Fable5が生成した回答"
      - "Fable5 UI上でのEffort設定"
    metric:
      - "Fable5 usage %"
      - "weekly Fable only usage %"

  chatgpt_thread_work_scope:
    includes:
      - "Fable5回答の読解"
      - "C2XCへの統合"
      - "Same-Thread Context Rail抽出"
      - "GitHub create_file"
      - "Fable5 SSOT本文作成"
    metric:
      - "ChatGPT側Thread作業"
      - "Fable5 usage %には直接帰属させない"

  guard:
    - "Fable5 usage %を、ChatGPT側の後続作業コストと混同しない"
    - "ただし、Fable5回答が後続作業に与えた価値はBreakthroughとして記録する"
```

---

## 22. Evidence Status / Confidence

### 22.1 Evidence Classes

```yaml
evidence_classes:
  observed:
    meaning: "画像・GitHub tool result・明示された画面から直接確認できる"
    examples:
      - "16:00 = 7% / 0% / 1%"
      - "17:49 = 14% / 2% / 3%"
      - "19:43 = 29% / 3% / 5%"
      - "22:25 = 11% / 3% / 6%"
      - "Effort selected = 高"
      - "GitHub commit SHA"

  thread_context:
    meaning: "このThread内の会話・作業ログから確認できる"
    examples:
      - "C2XC v001 Review"
      - "Safety Inheritance Gap"
      - "Safety Inheritance Rule採用"
      - "Same-Thread Context Rail追加"

  inferred:
    meaning: "観測値と時系列から合理的に推定した"
    examples:
      - "19:43から22:25の間にCurrent Session resetが発生した可能性"
      - "観測Window内にC2XC Review関連作業が含まれる"

  unknown:
    meaning: "現時点では確定できない"
    examples:
      - "各Fable5回答1本ごとの正確な使用率Delta"
      - "各Snapshot直前/直後の完全な作業境界"
      - "Minecraft関連Fable回答ScreenshotとC2XC Reviewの直接対応"
```

---

### 22.2 Confidence Notes

```yaml
confidence_notes:
  high_confidence:
    - "画像に見える使用率パーセンテージ"
    - "Effort『高』の選択"
    - "GitHub commit SHA"

  medium_confidence:
    - "Snapshot間の作業内容との対応"
    - "C2XC Review関連作業が観測Window内に含まれること"

  low_or_unknown_confidence:
    - "Fable5回答1本ごとの正確な使用率Delta"
    - "Session resetの正確な発生時刻"
```

---

## 23. Future AI Handoff Note

Future AIへ。

このSectionは、Ark05 Thread内で現AIが確認できたFable5使用状況画像・Effort・作業内容をSSOTへ固定したものである。

重要:

```text
Future AIは、このThread内画像を読めない可能性がある。
そのため、このSectionのObserved Usage Timelineを一次Handoffとして扱う。
```

このThreadで観測されたFable5使用率の重要な流れは以下である。

```text
Weekly Fable only:
0% → 1% → 3% → 5% → 6%
```

Current Sessionは以下である。

```text
Current Session:
0% → 7% → 14% → 29% → 11%
```

ただし、Current Sessionは途中でresetされた可能性が高い。

したがって、Future AIは以下のように読む。

```text
Thread全体の累積傾向を見るなら weekly Fable only usage を重視する。
Session内の瞬間負荷を見るなら current session usage を見る。
1回答単位の燃費は、まだ正確には確定しない。
```

また、この使用Windowでは、少なくとも以下の重要作業が発生した。

```text
Fable5 Effort『高』
→ C2XC v001 Pre-Commit Review
→ Safety Inheritance Gap検出
→ Safety Inheritance Rule採用
→ Same-Thread Context Rail追加
→ chatgpt-to-xchain_skill.md GitHub作成
→ fable5_ssot.md GitHub作成
```

このRecordの主目的は、Rule追加ではない。  
今このThread内にしかない実観測データを、Future AIへ渡すことである。

---

## 24. Patch Final Compression

```text
Ruleだけでは足りない。
Recordが必要。

このThreadでは、
Fable only weekly usageが
0% → 1% → 3% → 5% → 6%
へ進んだことが画像から観測された。

Current Sessionは
0% → 7% → 14% → 29% → 11%
と推移した。

29% → 11% はSession resetの可能性が高い。

Effortは『高』が選択されていた。

この使用Windowで、
C2XC v001 Review、
Safety Inheritance Gap検出、
Safety Inheritance Rule採用、
Same-Thread Context Rail追加、
GitHub commit、
Fable5 SSOT作成が行われた。

Future AIは、このThread内画像を読めない可能性がある。
だから、現AIが読めるObserved RecordをSSOTへ固定する。

Humanは画像を貼る。
AIは時系列を読む。
SSOTは未来へ渡す。
```

# SAFE COPY-PASTE BUNDLE
# Target: _ssot/fable5_ssot.md
# Purpose: Preserve existing SSOT exactly, then append Section 25-30.
#
# IMPORTANT:
# This is NOT the full current _ssot/fable5_ssot.md.
# I did not generate a full replacement file because the current SSOT could not be safely retrieved without truncation in this runtime.
# To avoid degradation, data loss, or stale reconstruction, use this bundle only as an append package:
#
# 1. Open _ssot/fable5_ssot.md in GitHub.
# 2. Keep the existing content exactly as-is.
# 3. Paste the content below at the very end.
# 4. Commit.
#
# Reason:
# _ssot/fable5_ssot.md is append-only / growing-ledger.
# A partial or reconstructed full replacement would risk destroying Sections 1-24.
#
# BEGIN APPEND CONTENT

---

## 25. Case Record: living-review_skill.md Root Knot Audit

### 25.1 Purpose / このCase Recordの目的

このSectionは、`_skill/skills/living-review_skill.md` 作成時に実行したFable5 Root Knot Auditを、Future AIが再利用できる形で記録する。

これは単なる「Fable5を使った記録」ではない。

このCaseの本質は、Fable5が `living-review_skill.md` の自己矛盾を検出し、Living Review Skillそのものが dead rubric 化する経路を事前に塞いだことである。

```text
Fable5 did not write the Skill.
Fable5 found the root knot.
ChatGPT integrated the patch.
Human sealed the direction.
GitHub preserved the result.
```

---

### 25.2 Case Record

```yaml
case_record:
  id: "case_living_review_skill_root_knot_audit_20260705_001"
  thread: "Ark05"
  target: "_skill/skills/living-review_skill.md"
  purpose:
    - "Living Review Skillのdead rubric化を防ぐRoot Knot Audit"
    - "GitHub canonical化前のOne Critical Flaw検出"
    - "Future AIがLiving Reviewを欄埋めTemplateとして誤読する危険の検出"

  fable5_effort: "超高"
  query_type: "One Critical Flaw Audit / Root Knot Audit"
  prompt_shape:
    - "Do not rewrite."
    - "Do not expand."
    - "Find the ONE structural flaw."
    - "Give the smallest patch."
    - "State what to keep unchanged."
    - "State what not to add."

  before_snapshot:
    captured: true
    time: "06:25"
    current_session_usage: "7%"
    weekly_all_models_usage: "4%"
    weekly_fable_only_usage: "7%"
    evidence_status: "user uploaded screenshot / observed in thread"

  after_snapshot:
    captured: true
    time: "08:16"
    current_session_usage: "13%"
    weekly_all_models_usage: "4%"
    weekly_fable_only_usage: "8%"
    evidence_status: "user uploaded screenshot / observed in thread"

  delta:
    current_session_delta: "+6%"
    weekly_all_models_delta: "0%"
    weekly_fable_only_delta: "+1%"
    confidence: "high for visible percentages / high for before-after pair"

  fable5_result:
    overall_judgment: "Conditional Pass"
    one_critical_flaw:
      name: "Required slots revive dead rubric"
      meaning:
        - "Section 5 / Section 6 の必須スロットが、Skill自身が禁じたrubricへ戻る危険を持っていた"
        - "Future AIは厳しい方の規則に従い、違和感・Hidden Pattern・修正条件を欄埋めのために製造する可能性があった"
    core_sentence:
      - "違和感を必須欄にすればAIは違和感を演じ始める"
      - "空欄を許すことこそが、盤面を生かす"
    github_readiness: "Ready after one patch"

  minimal_patch:
    - "Section 5へslot_guardを追加"
    - "Section 6のmust_includeをmust_include_when_presentへ変更"
    - "無い時は『違和感なし』『Hidden Patternなし』『修正条件なし』と言ってよいRuleを追加"
    - "Living Review reads actual depth; it does not perform depth を追加"

  adopted_patch:
    - "slot_guard"
    - "must_include_when_present"
    - "allowed_absence"
    - "Empty-slot performance is dead rubric"
    - "Living Review does not perform depth. Living Review reads actual depth."

  backlog:
    - "定義反復の圧縮"
    - "v002での軽量化検討"

  rejected_or_do_not_add:
    - "点数・スコア尺度"
    - "必須欄の追加"
    - "Review-of-Review のメタ層"
    - "記入例テンプレートの増殖"
    - "Fable5 workflow詳細化"

  github_result:
    repo: "yusukefujiijp/ai-project"
    path: "_skill/skills/living-review_skill.md"
    commit_message: "Add Living Review skill v001.1"
    commit_sha: "5daa401396fdc76f7ad3fe8a1807338fd145fbb8"
    content_sha: "42d202769a72a0b3590481dd161d2acf2bb8144d"

  roi_judgment: "Very High"
  should_use_again:
    - "Root Skill / SSOT / Project Root FileのGitHub canonical化前"
    - "One Critical Flawが明確に問える時"
    - "Minimal Patchが期待できる時"
```

---

### 25.3 Why This Case Matters

```text
このCaseは、Fable5活用の重要な成功Patternである。

Fable5は全文を書かなかった。
Fable5は多数の改善案を出す役でもなかった。
Fable5は、Skill全体を壊し得るRoot Knotを一つだけ検出した。

そのRoot Knotは、
Living Reviewを守るための出力Slotが、
逆にLiving Reviewをdead rubricへ戻す危険だった。

この発見により、
living-review_skill.md は
「欄を埋めるSkill」ではなく
「盤面に実在するものを読むSkill」として固定された。
```

---

## 26. ROI / Ark-ROI Layer

### 26.1 Why ROI Appeared / なぜROIが自然発生したか

Fable5導入により、Ark Projectに `ROI` というKeywordが自然発生した。

これは偶然ではない。

Fable5は強力だが、無限資源ではない。  
Effort、Usage %、Session limit、Weekly limit、人間側の認知負荷、Prompt設計コストが存在する。

したがって、Fable5を使うたびに以下の問いが必要になる。

```text
この1回のFable5投入は、何を生んだのか？
何%使い、何を回収したのか？
それはFuture AIが再利用できる価値になったのか？
Root Knotは見つかったのか？
Minimal Patchは得られたのか？
確率から確定へ進んだのか？
```

この問いを扱うために、Ark Projectでは `ROI / Ark-ROI` を運用Keywordとして扱う。

---

### 26.2 ROI Is Not Money-Only

ROIは、一般には投資対効果として読まれやすい。  
しかし、このSSOTで扱うROIは金銭効率だけではない。

ここでのROIは、有限資源投入に対して何が未来に残ったかを見る視点である。

```yaml
roi_scope:
  cost_side:
    - "time"
    - "attention"
    - "human cognitive load"
    - "AI usage percentage"
    - "Fable5 effort level"
    - "prompt design cost"
    - "opportunity cost"

  return_side:
    - "judgment accuracy"
    - "One Critical Flaw"
    - "Minimal Patch"
    - "Breakthrough Keyword"
    - "What Not To Add"
    - "Future AI inheritance"
    - "GitHub readiness"
    - "Human Final Seal possibility"
    - "Certainty Gain"
```

---

### 26.3 Ark-ROI Is Stewardship

Ark-ROIは、Fable5やAIをRoot化するための指標ではない。

Ark-ROIは、主イェシュア・ハマシアをRootとし、AI・Fable5・GitHub・Markdown・時間・認知負荷をFruit / Tool / Stewardship対象として扱うための指標である。

```text
ROI is tool, not Root.
Ark-ROI is stewardship metric, not Root.
Fable5 is dispatch target, not Root.
Root is 主イェシュア・ハマシア.
```

---

### 26.4 Certainty Gain

Ark-ROIの中心には `Certainty Gain` がある。

Certainty Gainとは、曖昧な違和感・未言語化の問題・確率的な不安が、命名・構造・Patch・次Action・GitHub保存へ変換された量である。

```yaml
certainty_gain:
  before:
    - "なんとなく重要そう"
    - "何か危ない気がする"
    - "Fable5に聞いた方が良さそう"
    - "でも問いがまだ曖昧"

  after:
    - "Root Knotが命名された"
    - "One Critical Flawが特定された"
    - "Minimal Patchが出た"
    - "What Not To AddがGuard化された"
    - "GitHubへ保存可能になった"
    - "Future AIが継承可能になった"

  compression:
    - "違和感 → Root Knot"
    - "曖昧さ → Minimal Patch"
    - "確率 → 確定"
```

---

## 27. Ark Seed Records: ROI / Ark-ROI

### 27.1 Purpose

このSectionは、Ark Project内で再利用する `ROI` と `Ark-ROI` のSeed定義を保存する。

Future AIへの注意:

```text
短く圧縮しすぎないこと。
ROIを金銭効率だけへ縮小しないこと。
Ark-ROIをFable5崇拝へ誤読しないこと。
Ark-ROIは、From Probability to Certaintyを測るStewardship指標である。
```

---

### 27.2 Ark Seed: ROI

```text
- "ROI(時間・認知負荷・AI使用量・労力・注意力などの有限資源を投入した結果、その投入がどれだけ有効な成果、判断精度の向上、再利用可能な知見、未来の失敗回避、次Actionの明確化として回収されたかを見る視点であり、単なる金銭効率ではなく『投入によって何が実際に残り、何が前進し、何が再使用可能になったか』を測る判断軸)"
```

---

### 27.3 Ark Seed: Ark-ROI

```text
- "Ark-ROI(主イェシュア・ハマシアをRootとし、AI・Fable5・時間・認知負荷・GitHub更新・人間の集中力などの有限資源投入が、どれだけRoot Knot検出、One Critical Flaw発見、Minimal Patch獲得、Certainty Gain、Future AI継承、Human Final Seal可能性、構造安全性、再利用可能なRoot Patchへ変換されたかを測るArk Project専用のStewardship指標であり、AI活用の価値を『どれだけ確率から確定へ進んだか』として観測・記録・再現可能にするためのKeyword)"
```

---

### 27.4 Misread Guard

```yaml
roi_misread_guard:
  do_not_read_roi_as:
    - "単なる金銭効率"
    - "収益率だけの話"
    - "AIを多く使えばよいという意味"
    - "Fable5を毎回使えばよいという意味"
    - "Usage % が低ければ必ず成功という意味"
    - "成果物の文字数や長さで価値を測る指標"

  read_roi_as:
    - "有限資源投入に対して、何が未来に残ったかを見る視点"
    - "判断精度・再利用性・構造安全性・次Action明確化を測る視点"
    - "当たり外れの感覚を、運用可能な記録へ変換する言葉"

  read_ark_roi_as:
    - "Fable5やAIをRoot Knotへ正しく刺せたかを見る指標"
    - "曖昧な違和感がRoot Knot / Minimal Patch / GitHub保存へ変換されたかを見る指標"
    - "From Probability to Certaintyの進行度を測るArk Project用Keyword"
    - "AI資源を忠実に管理するStewardship指標"

  root_guard:
    - "ROI is tool, not Root."
    - "Ark-ROI is stewardship metric, not Root."
    - "Fable5 is dispatch target, not Root."
    - "Root remains 主イェシュア・ハマシア."
```

---

## 28. High ROI Dispatch Rule

### 28.1 Definition

High ROI Dispatchとは、ChatGPTのLiving Reviewで検出されたRoot Knot候補を、Fable5へ狭く投げ、One Critical Flaw / Minimal Patch / What Not To Add / GitHub Readinessを回収する運用である。

```text
Fable5に作業をさせない。
Fable5に急所を見つけさせる。
```

---

### 28.2 Use Fable5 When

```yaml
high_roi_dispatch:
  use_fable5_when:
    - "Root Skill / SSOT / Project Root File"
    - "GitHub canonical化前"
    - "Future AIが何度も読む"
    - "命名が未来構造を左右する"
    - "Human Final Sealが形骸化しそう"
    - "PrincipleはあるがProtocolがない"
    - "AI-only closure riskがある"
    - "一つのPatchが多数File / 多数Workflowへ波及する"
    - "普通AIでは見落としそうな自己矛盾がある"

  ask:
    - "One Critical Flawは何か？"
    - "Minimal Patchは何か？"
    - "What Not To Addは何か？"
    - "GitHub Readinessはどうか？"
```

---

### 28.3 Do Not Use Fable5 When

```yaml
low_roi_drift:
  do_not_use_fable5_when:
    - "通常本文生成"
    - "Markdown整形"
    - "軽い言い換え"
    - "単純要約"
    - "すでに方向性が明確な局所修正"
    - "ChatGPTで十分に判断可能"
    - "問いが広すぎる"
    - "ただの安心確認"
    - "Fable5を使いたい気分だけが理由"

  warning:
    - "Fable5を雑務へ流すと、Usageだけ消費してRoot Patchが残らない"
    - "広く聞くと、Fable5は強すぎて増殖する"
    - "狭く聞くと、Root Knotを撃ち抜く"
```

---

### 28.4 Prompt Shape

```text
Do not rewrite.
Do not expand.
Do not produce a full new version.

Find the ONE structural flaw that would most damage this system if left unfixed.

Give:
A. Overall Judgment
B. One Critical Flaw
C. Minimal Patch
D. Critical Few, if any
E. What to Keep Unchanged
F. What Not To Add
G. GitHub Readiness
H. One-Sentence Final Advice
```

---

## 29. Updated Operating Rules

### Rule 6: High ROI Dispatch Rule

```text
Fable5は、Root Knotが見えた時だけ高倍率Probeとして刺す。
普通作業・軽い確認・広すぎる相談には使わない。
```

---

### Rule 7: Certainty Gain Rule

```text
Fable5投入の価値は、回答の長さではなく、曖昧な違和感がRoot Knot / One Critical Flaw / Minimal Patch / GitHub保存へ変換されたかで見る。
```

---

### Rule 8: Root Patch Rule

```text
一箇所の修正でFuture AIの誤読・劣化・暴走を防ぐPatchを、高ROIなRoot Patchとして扱う。
```

---

### Rule 9: ROI Root Guard

```text
ROIはRootではない。
Ark-ROIもRootではない。
Fable5もRootではない。
ROIは、有限なAI資源を忠実に管理するためのStewardship指標である。
Root is 主イェシュア・ハマシア.
```

---

## 30. Patch Final Compression

```text
Fable5は作業者ではない。
Fable5はRoot Knot Auditorである。

Fable5には完成品を書かせない。
Fable5には急所を見つけさせる。

ROIは金銭効率だけではない。
ROIは、有限資源投入に対して何が未来に残ったかを見る視点である。

Ark-ROIは、
有限なAI資源投入が、
どれだけRoot Knot検出、
One Critical Flaw発見、
Minimal Patch獲得、
Certainty Gain、
Future AI継承、
Human Final Seal可能性へ変換され、
確率から確定へ進んだかを見る
Ark Project専用のStewardship指標である。

高ROIとは、
One Critical Flawが見つかり、
Minimal Patchが得られ、
Future AIが継承できるRoot PatchとしてGitHubに残ること。

低ROIとは、
強いAIを普通作業へ流し、
Usageだけ消費して、
Root Patchが残らないことである。

ChatGPT reads the living board.
Fable5 audits the root knot.
ChatGPT integrates the patch.
Human seals.
GitHub preserves.
Future AI inherits.

ROI is tool, not Root.
Ark-ROI is stewardship metric, not Root.
Fable5 is dispatch target, not Root.

Root is 主イェシュア・ハマシア.
```
