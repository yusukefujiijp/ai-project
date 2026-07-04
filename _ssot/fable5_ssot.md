---
title: "Fable5 SSOT"
canonical_name: "Fable5 Single Source of Truth"
version: "v001"
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
