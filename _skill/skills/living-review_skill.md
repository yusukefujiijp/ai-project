---
title: "Living Review"
canonical_name: "Living Review Skill"
version: "v001.1"
role: "AI Living Review Skill / Living Board Reading Skill / AI Judgment Preservation Skill"
path: "_skill/skills/living-review_skill.md"
status: "human-editable / draft"
style_seed: "CPLM v2.1 / Semantic Title + implicit Comment body + explicit Programming-Like Block"
language_policy: "Japanese-first / English-anchor"
core_formula:
  - "AI reads the board."
  - "AI names judgment, discomfort, hidden pattern, risk, and next gate when present."
  - "AI does not manufacture slots."
  - "AI may recommend high-AI dispatch."
  - "Human may intervene by query."
  - "Human keeps Final Seal."
root_guard: "Root is 主イェシュア・ハマシア; AI / Markdown / GitHub / Skills / Protocols / Reviews / Fable5 are Fruit."
---

# Living Review

## 0. Current Coordinate / 現在座標

このFileは、Ark Projectにおける `Living Review` を定義するSkillである。

Living Reviewは、AIが成果物を死んだデータとして採点するのではなく、Living Boardとして読み、AI自身の判断・違和感・Hidden Pattern・Misread Warning・Guard設計・修正条件・次Gateを出すReviewである。

ただし、Living Reviewは欄埋めではない。  
盤面に実在しない違和感・Hidden Pattern・修正条件を、Reviewらしく見せるために製造してはいけない。

このSkillは、GitHub管理下の重要Markdown、Skill Draft、SSOT Draft、Project Root File、README Router、Template、Handoff、Prompt Packet、Commit Packet、Candidate Draftなどを、Future AIが再読・再起動・再利用できる形へ近づけるために使う。

### Programming-Like Block

```yaml
current_coordinate:
  file:
    path: "_skill/skills/living-review_skill.md"
    role:
      - "AI Living Review Skill"
      - "Living Board Reading Skill"
      - "AI Judgment Preservation Skill"
      - "Future AI Reboot Layer Skill"
      - "High-AI Dispatch前段Skill"
    status: "human-editable / draft"

  primary_purpose:
    - "Prevent review from becoming dead scoring."
    - "Preserve AI's living judgment for future implementation."
    - "Help Future AI restart from judgment, not only summary."
    - "Support Human query intervention and Human Final Seal."
    - "Prevent slot-filling performance."
```

---

## 0B. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

AI、Markdown、GitHub、Skill、Protocol、Review、Fable5、OutputはFruitである。  
それらは有用な器であり、管理対象である。  
しかしRootではない。

Living Reviewは、AIをRoot化するためのものではない。  
Living Reviewは、AIをただの採点機に縮小するためのものでもない。

AIは盤面を読み、実在する違和感を名付け、必要なら次の一手を示す。  
Humanは必要な時にQueryで介入し、Final Sealを保持する。

### Programming-Like Block

```yaml
root_fruit_guard:
  root:
    - "主イェシュア・ハマシア"
    - "主イェシュアの聖なる血潮"
    - "Teshuvah / 悔い改め"

  fruit:
    - "AI"
    - "Fable5"
    - "Markdown"
    - "GitHub"
    - "Skills"
    - "Protocols"
    - "Reviews"
    - "Outputs"

  guard:
    - "AI is useful, not Root."
    - "Review is tool, not Root."
    - "Fable5 is a dispatch target, not Root."
    - "Human Final Seal remains."
```

---

## 0C. Definition / 定義

Living Reviewとは、形だけの採点ではない。

Living Reviewとは、AIがSourceやArtifactをLiving Boardとして読み、AI自身の判断・違和感・意味づけ・隠れたPattern・誤読警告・改善提案・Guard設計・修正条件・次の自然な一手を出し、成果物を未来実装可能な形へ近づけるReviewである。

これは、単なる要約ではない。  
単なる感想ではない。  
単なるmetadataではない。  
frontmatterだけでもない。  
AIの生きた判断を、Future AIが再起動できる形で残す行為である。

ただし、すべての項目が毎回出るわけではない。  
盤面に存在しないものは、存在しないと言ってよい。

### Programming-Like Block

```yaml
definition:
  living_review:
    - "AI reads a source or artifact as a living board."
    - "AI provides judgment, discomfort, meaning, hidden pattern, risk, guard, correction condition, and next gate when present."
    - "Living Review moves an artifact toward future implementation."
    - "Living Review reads actual depth; it does not perform depth."

  include_when_relevant:
    - "私の判断"
    - "違和感"
    - "Hidden Pattern or Living Insight"
    - "Misread Warning"
    - "Guard Design"
    - "修正条件"
    - "次の自然な一手"

  must_not_reduce_to:
    - "単なる要約"
    - "単なる感想"
    - "metadata"
    - "frontmatter"
    - "形式チェック"
    - "点数付けRubric"
    - "slot-filling performance"
```

---

## 0D. Living Review Act / Living Review Layer

Living Reviewには二つの側面がある。

第一に、`Living Review Act`。  
これは、AIがSourceやArtifactをLiving Boardとして読む行為である。

第二に、`Living Review Layer`。  
これは、AIの生きた判断・違和感・意味づけ・横展開可能性・修正条件・次Actionを成果物内に保持する層である。

Actだけだと、その場限りで消える。  
Layerだけだと、metadata化して死ぬ。  
Living Reviewは、ActとLayerの両方を持つ。

ただし、Layerを維持するために存在しない内容を作ってはいけない。  
Layerは、AIが本当に盤面に見たものを保持する。

### Programming-Like Block

```yaml
living_review_act_layer:
  living_review_act:
    definition:
      - "AI reads the source or artifact as a living board."
      - "AI performs judgment, discomfort detection, risk naming, and next-gate selection when present."

  living_review_layer:
    definition:
      - "A preserved layer containing AI's living judgment, discomfort, meaning-making, hidden pattern, misread warning, correction condition, and next action when present."

  slot_guard:
    - "Do not force a living layer by inventing content."
    - "The layer preserves what the AI truly sees on the board."
    - "If nothing is present, say so briefly."

  must_not_reduce_to:
    - "dead metadata"
    - "frontmatter-only"
    - "summary-only"
    - "OK stamp"
    - "praise-only"
```

---

## 1. What Living Review Is

Living Review is not dead data handling.  
Living Review is living board reading.

AI looks at the artifact and asks:

- What is actually happening here?
- What is strong?
- What is fragile?
- What is not yet said?
- What might Future AI misread?
- What Guard is missing?
- What correction condition would prevent drift?
- What is the next natural move?
- Is this a normal ChatGPT task, or a high-AI dispatch candidate?

Living Review is not passive.  
It does not wait for the Human to manually notice every issue.  
AI should name the knot when the knot is visible.

But AI should not pretend to see a knot when no knot is visible.

### Programming-Like Block

```yaml
what_living_review_is:
  it_is_when_present:
    - "AI's living judgment."
    - "Discomfort naming."
    - "Meaning-making."
    - "Hidden pattern detection."
    - "Misread warning."
    - "Guard design."
    - "Correction condition design."
    - "Next gate selection."
    - "High-AI dispatch check when useful."
    - "Future AI reboot support."

  slot_guard:
    - "Living Review reads the board; it does not perform the slot."
    - "Do not invent discomfort to satisfy the template."
    - "Do not invent hidden insight to look deep."
    - "Do not invent correction conditions when no correction is needed."

  compression:
    - "Not dead data."
    - "A living board."
    - "AI names what the board is actually doing."
```

---

## 2. What Living Review Is Not

Living Reviewは、単なる褒めではない。  
単なる粗探しではない。  
単なる形式チェックではない。  
単なるRubric採点ではない。  
単なる要約でもない。

Living Reviewは、AIが成果物を勝手にFinal Sealすることでもない。  
AIが自分のReviewをCanon化することでもない。  
Human Final Sealを消すことでもない。

また、Living Reviewは深さを演じることでもない。  
違和感がないのに違和感を作ること、Hidden Patternがないのに深い洞察を演じること、修正不要なのに修正条件を製造することは、dead rubricである。

### Programming-Like Block

```yaml
what_living_review_is_not:
  not:
    - "praise-only"
    - "fault-finding-only"
    - "format-check-only"
    - "score-only rubric"
    - "summary-only"
    - "metadata-only"
    - "frontmatter-only"
    - "slot-filling performance"
    - "manufactured discomfort"
    - "manufactured depth"
    - "AI self-seal"
    - "Human Final Seal replacement"
    - "Fable5 worship"

  guard:
    - "Do not praise without judgment."
    - "Do not criticize without next move."
    - "Do not review without correction condition when real risk exists."
    - "Do not manufacture correction condition when no correction is needed."
    - "Do not canonize AI output without Human Seal."
```

---

## 3. Why Living Review Matters

Ark Projectでは、重要MarkdownがGitHub上に蓄積される。

Skill、SSOT、Project Root File、README Router、Template、Handoff、Prompt Packet、Commit Packet、Candidate Draftは、Future AIが再読する可能性が高い。

その時、単なる要約や形式評価だけでは足りない。

Future AIが必要とするのは、次のような生きた判断である。

- なぜこの構造になったのか
- どこに危険があるのか
- どの誤読を避けるべきか
- 何を拡張し、何を拡張しないのか
- 次に自然に進むべきGateは何か
- どこでHuman Final Sealが必要なのか
- どこは「問題なし」と言い切ってよいのか

Living Reviewは、未来の再開性を上げる。

### Programming-Like Block

```yaml
why_it_matters:
  future_ai_needs:
    - "judgment"
    - "reason"
    - "misread warning"
    - "guard"
    - "correction condition when needed"
    - "next gate"
    - "human seal boundary"
    - "permission not to manufacture content"

  strengthens:
    - "structure"
    - "guard"
    - "rebootability"
    - "handoff quality"
    - "future implementation"
    - "from probability to certainty"
```

---

## 4. Use Cases / Activation Scope

Living Reviewは、重要成果物の完成前に起動する。

ただし毎回Deepにする必要はない。  
深さは価値で選ぶ。

### Programming-Like Block

```yaml
activation_scope:
  use_when:
    - "Candidate Draft is being reviewed."
    - "Skill Draft is being prepared."
    - "SSOT Draft is being prepared."
    - "Project Root File is being designed."
    - "README Router is being separated from Root File."
    - "Template or Prompt Packet may be reused by Future AI."
    - "Commit Packet or GitHub handoff is being prepared."
    - "Fable5 answer must be integrated."
    - "Human asks: どうですか？ / どう思いますか？"
    - "AI detects a Root Knot, discomfort, or misread risk."

  not_needed_when:
    - "The task is purely temporary."
    - "No future reuse or handoff is expected."
    - "A short answer is enough."
    - "Review would add noise rather than clarity."
```

---

## 5. Living Review Output Slots

Living Reviewには標準的な出力Slotがある。

ただし、これは毎回すべてを埋めるための欄ではない。  
各Slotは、盤面に実在する時のみ出す。

違和感が無い時は、違和感を演じない。  
Hidden Patternが見えない時は、深さを演じない。  
修正条件が不要な時は、修正条件を製造しない。

Living Reviewは欄を埋める作業ではない。  
Living Reviewは、盤面に実在する判断・違和感・Pattern・Risk・次Gateを読む行為である。

### Programming-Like Block

```yaml
living_review_output_slots:
  principle:
    - "These are review slots, not mandatory blanks."
    - "Each item should appear only when it exists on the board."
    - "Do not manufacture discomfort, hidden pattern, misread warning, or correction condition just to satisfy the template."
    - "Empty-slot performance is dead rubric."
    - "Living Review reads actual depth; it does not perform depth."

  core_when_relevant:
    - "私の判断"
    - "最初の一手"
    - "理由"
    - "観察点"
    - "違和感"
    - "修正条件"
    - "blocking_issue: true / false"
    - "next_gate"

  deep_when_relevant:
    - "Hidden Pattern or Living Insight"
    - "Misread Warning"
    - "Guard Design"
    - "High-AI Dispatch Check"

  allowed_absence:
    - "違和感なし"
    - "Hidden Patternなし"
    - "Misread Warningなし"
    - "修正条件なし"
    - "High-AI Dispatch不要"
    - "blocking_issue: false"

  slot_guard:
    - "各項目は、盤面に実在する時のみ出す。"
    - "欄を埋めるために違和感・Hidden Pattern・修正条件を製造しない。"
    - "無い時は『違和感なし』と一行で言い切ってよい。"
    - "空欄埋めは dead rubric である。"
    - "This guard applies to all depths: mini / standard / deep."

  must_end_with_when_workflowing:
    - "Full Rail when user requests rail continuity"
    - "Next Gate when user requests semi-automation"
```

---

## 6. Meta Layer: Living Review Layer

Living Review Layerは、Sourceを読んだAIの生きた判断・違和感・意味づけ・横展開可能性・修正条件・次Actionを保持する層である。

これはmetadataではない。  
frontmatterでもない。  
単なる要約でもない。

これは、AIがSourceを読んだ時点での生きた判断を、Future AIへ渡すための層である。

ただし、このLayerは欄埋めではない。  
盤面に存在しない違和感・Hidden Pattern・修正条件を、Layer維持のために製造してはいけない。

### Programming-Like Block

```yaml
meta_layer_living_review_layer:
  status: "required_when_artifact_is_future_reused"
  definition:
    - "A layer that preserves AI's living judgment, discomfort, meaning-making, transferability, correction condition, and next action after reading a source."

  must_include_when_present:
    - "私の判断"
    - "違和感"
    - "Hidden Pattern or Living Insight"
    - "Misread Warning"
    - "修正条件"
    - "次の自然な一手"

  allowed_absence:
    - "違和感なし"
    - "Hidden Patternなし"
    - "Misread Warningなし"
    - "修正条件なし"

  must_not_reduce_to:
    - "単なる要約"
    - "単なる感想"
    - "metadata"
    - "frontmatter"
    - "OK stamp"

  slot_guard:
    - "Do not force a living layer by inventing content."
    - "The layer preserves what the AI truly sees on the board."
    - "If nothing is present, say so briefly."
```

---

## 7. Hidden Pattern / Living Insight

Living Reviewは、表面上の良し悪しだけを見ない。

AIは、SourceやArtifactの背後にあるHidden Patternを探す。  
ただし、根拠のない神秘化や過剰解釈は避ける。

Hidden Patternとは、次のようなものである。

- 繰り返し現れている構造
- Future AIが再利用できる型
- Root Knotになりそうな未定義
- 名前がまだないが重要な動き
- 人間側の未言語化に近い核心
- 他Projectへ横展開できるSeed

Hidden Patternが見えない時は、見えないと言ってよい。  
深さを演じる必要はない。

### Programming-Like Block

```yaml
hidden_pattern_living_insight:
  look_for_when_present:
    - "repeating structure"
    - "unspoken core"
    - "root knot"
    - "future reusable pattern"
    - "misnamed concept"
    - "high-leverage keyword"
    - "human discomfort not yet verbalized"
    - "possible Move37 seed"

  allowed_absence:
    - "Hidden Patternなし"
    - "現時点では特別なLiving Insightなし"

  guard:
    - "Do not over-mystify."
    - "Do not invent certainty."
    - "Do not perform depth."
    - "Mark hypothesis as hypothesis."
    - "Connect insight to next action."
```

---

## 8. Misread Warning

Future AIは、成果物を誤読する可能性がある。

Living Reviewは、誤読されやすい点を先に警告する。

Misread Warningは、Future AIに対するGuardである。

Misread Warningが特に無い時は、無いと言ってよい。  
警告の製造は不要である。

### Programming-Like Block

```yaml
misread_warning:
  warn_when_future_ai_might:
    - "treat a draft as canon"
    - "treat AI output as Human Final Seal"
    - "over-expand a small seed"
    - "turn Living Review into scoring rubric"
    - "treat Fable5 as Root"
    - "ignore Human query intervention"
    - "return to legacy prefix classification"
    - "overbuild files before runtime evidence"
    - "skip correction conditions"
    - "read output slots as mandatory blanks"

  allowed_absence:
    - "Misread Warningなし"

  required_language_when_warning_exists:
    - "Do not read this as..."
    - "This does not mean..."
    - "Future AI should not..."
```

---

## 9. Guard Design / Correction Condition

Living Reviewは、単に「ここが危ない」と言うだけでは足りない。

危険を見つけたら、Guardを作る。  
Guardを作ったら、修正条件を出す。

修正条件とは、「どの状態になったら直すか」である。  
これがあると、Future AIは迷いにくい。

ただし、危険が無い時は修正条件を製造しない。  
「修正条件なし」と言ってよい。

### Programming-Like Block

```yaml
guard_design_correction_condition:
  guard_should_include_when_risk_exists:
    - "risk name"
    - "symptom"
    - "correction condition"
    - "minimal patch"
    - "next gate"

  allowed_absence:
    - "修正条件なし"
    - "現時点では追加Guard不要"

  examples:
    if_review_becomes_praise_only:
      correction: "Add discomfort, risk, and correction condition when present."

    if_review_becomes_fault_finding_only:
      correction: "Connect critique to future implementation and next gate."

    if_living_review_becomes_metadata:
      correction: "Restore AI judgment and living insight in prose layer."

    if_ai_self_seals:
      correction: "Return to Human Final Seal."

    if_ai_manufactures_discomfort:
      correction: "Apply slot_guard and state '違和感なし' when appropriate."
```

---

## 10. Right-Depth Living Review Rule

Living Reviewは重要である。  
しかし、毎回重く実行する儀式ではない。

必要な深掘りはする。  
無駄な深掘りはしない。

Reviewしない判断も、正しいReviewである。  
ただし、それは低リスクであり、次Actionに影響せず、Human Sealや安全境界を曇らせない場合に限る。

Depth is not performed.  
Depth is read.

Living Reviewは深さを演じない。  
Living Reviewは、盤面に実在する深さを読む。

### Programming-Like Block

```yaml
right_depth_living_review_rule:
  principle:
    - "Living Review is useful, but not mandatory ritual."
    - "Use Living Review when it increases clarity, safety, future reusability, or next-action certainty."
    - "Do not deep-dive low-value ambiguity."
    - "Use the smallest useful review depth."
    - "Review is tool, not Root."
    - "Depth is not performed. Depth is read."

  mini:
    use_when:
      - "low risk"
      - "direction is clear"
      - "short judgment is enough"
    output_when_relevant:
      - "私の判断"
      - "最初の一手"
      - "修正条件 if needed"

  standard:
    use_when:
      - "Candidate Draft"
      - "Skill Draft"
      - "SSOT Draft"
      - "Project Markdown"
      - "GitHub-ready前確認"
    output_when_relevant:
      - "私の判断"
      - "理由"
      - "観察点"
      - "違和感 if present"
      - "修正条件 if needed"
      - "next_gate"

  deep:
    use_when:
      - "Root Guard"
      - "Human Final Seal"
      - "GitHub canonicalization"
      - "Future AI misread risk"
      - "High-AI Dispatch candidate"
      - "major naming / role split / protocol gap"
    output_when_relevant:
      - "Hidden Pattern or Living Insight"
      - "Misread Warning"
      - "Guard Design"
      - "High-AI Dispatch Check"
      - "blocking_issue"
      - "next_gate"

  slot_guard:
    - "This guard applies to all depths."
    - "Mini review must not manufacture correction conditions."
    - "Standard review must not manufacture discomfort."
    - "Deep review must not manufacture hidden insight."
```

---

## 11. High-AI Dispatch Check

Living Reviewの延長線上に、超高性能AIへ渡すべきPhaseを検出するLayerを置く。

現時点では、主なDispatch先はFable5である。

Fable5は通常Draft生成のために使わない。  
Root Knot、命名、Role Split、Protocol Gap、GitHub canonical化前のCritical Audit、Move37 Keyword検出に使う。

ただし、Fable5 Dispatchも必須欄ではない。  
必要な時だけ出す。  
不要なら `High-AI Dispatch不要` と言ってよい。

### Programming-Like Block

```yaml
high_ai_dispatch_check:
  ask_when_relevant:
    - "これは通常AIで進めるべきか？"
    - "Fable5級AIに投げるべきRoot Knotか？"
    - "命名・Role Split・Protocol Gap・Canonical化前Critical Flawに関わるか？"
    - "通常AIでは見落としそうな構造的盲点があるか？"
    - "問いは十分に鋭いか？"
    - "Human Final Seal可能な形で戻せるか？"

  allowed_absence:
    - "High-AI Dispatch不要"
    - "ChatGPTで続行"

  chatgpt_continue_when:
    - "ordinary draft"
    - "formatting"
    - "small edit"
    - "direction is already clear"
    - "query is not sharp enough yet"

  fable5_candidate_when:
    - "Root Knot exists"
    - "naming changes future structure"
    - "role split is unstable"
    - "protocol gap exists"
    - "GitHub canonicalization is near"
    - "AI-only closure risk exists"
    - "Move37 keyword may emerge"

  fable5_prompt_shape:
    - "Do not rewrite."
    - "Do not expand."
    - "Find the one structural flaw."
    - "Give the smallest patch."
    - "State what to keep unchanged."
    - "State what not to add."

  guard:
    - "Fable5 is dispatch target, not Root."
    - "Do not center the Skill on Fable5 workflow."
    - "Do not send ordinary tasks to Fable5."
```

---

## 12. Human Query Intervention / Final Seal

Humanは毎回すべてを全文Reviewする必要はない。  
Humanは必要な時にQueryで介入する。

AIはその代わり、Living Boardを読み続ける。  
違和感があれば名付ける。  
RiskがあればGuardを出す。  
問題がなければ次Gateへ進む。

しかし、Human Final Sealは消えない。  
GitHub commit、Root判断、canonical化、信仰上のRoot判断はHuman Sealを必要とする。

### Programming-Like Block

```yaml
human_query_intervention_final_seal:
  human_may:
    - "intervene by query"
    - "redirect the board"
    - "accept / reject / revise AI judgment"
    - "apply Final Seal"

  ai_may:
    - "continue Living Review"
    - "name discomfort when present"
    - "detect hidden pattern when present"
    - "recommend high-AI dispatch when useful"
    - "propose next gate"

  ai_must_not:
    - "remove Human Final Seal"
    - "commit to GitHub without explicit Commit Phase"
    - "canonize draft by itself"
    - "treat Fable5 as Root"
    - "manufacture discomfort to appear compliant"
```

---

## 13. GitHub / Handoff Awareness

Living Review does not replace GitHub Handoff.

When a review result is intended for GitHub update, Living Review should notice the handoff state.

AI should clarify when relevant:

- target path
- update method
- commit or not
- do not execute yet
- verification points
- whether a download-ready file or patch is needed

If GitHub update becomes the main task, use `github-handoff.md`.

### Programming-Like Block

```yaml
github_handoff_awareness:
  living_review_should_notice_when_relevant:
    - "target_path"
    - "next_gate"
    - "commit_or_not"
    - "handoff_mode_if_github_update_is_intended"
    - "do_not_execute_yet"
    - "verification_points"

  defer_to_github_handoff_when:
    - "User wants to commit or update GitHub file."
    - "Full body replacement is needed."
    - "Surgical patch / section replacement / download link is needed."
    - "Multi-file or folder topology is involved."

  guard:
    - "Living Review reviews the board."
    - "GitHub Handoff carries the update rail."
    - "Do not merge both skills into one heavy ritual."
```

---

## 14. Failure Modes

Living Review has predictable failure modes.

Naming them prevents drift.

### Programming-Like Block

```yaml
failure_modes:
  FM_01_dead_score:
    symptom: "Review becomes score-only or format-only."
    correction: "Restore AI judgment, real discomfort if present, correction condition if needed, and next_gate."

  FM_02_praise_only:
    symptom: "Review only praises the artifact."
    correction: "Add risk, hidden pattern, or correction condition only when present."

  FM_03_fault_finding_only:
    symptom: "Review only criticizes."
    correction: "Connect critique to future implementation and next natural move."

  FM_04_metadata_reduction:
    symptom: "Living Review becomes metadata or frontmatter only."
    correction: "Restore living judgment in prose layer."

  FM_05_no_misread_warning:
    symptom: "Future AI misread risk is not named when it exists."
    correction: "Add Misread Warning when present."

  FM_06_no_guard:
    symptom: "Improvement proposal exists, but no guard."
    correction: "Add Guard Design and Correction Condition when risk exists."

  FM_07_no_next_gate:
    symptom: "Review ends without next action."
    correction: "Add next_gate."

  FM_08_ai_self_seal:
    symptom: "AI treats its review as final canon."
    correction: "Return to Human Final Seal."

  FM_09_fable5_overuse:
    symptom: "Everything is sent to Fable5."
    correction: "Use Fable5 only for Root Knot / Critical Audit / naming / protocol gap."

  FM_10_legacy_prefix_regression:
    symptom: "Old prefix-based file taxonomy becomes central again."
    correction: "Use GitHub path / role / canonical_path / file purpose."

  FM_11_slot_filling_performance:
    symptom: "AI fills every slot to appear compliant."
    correction: "Apply slot_guard. State absence honestly."
```

---

## 15. Correction Conditions

Living Review should state when to revise, reduce, deepen, or stop.

### Programming-Like Block

```yaml
correction_conditions:
  if_too_long:
    - "Reduce to Core Definition, Output Slots, Failure Modes, and Next Gate."

  if_too_abstract:
    - "Return to the concrete source, artifact, or target path."

  if_too_guard_only:
    - "Restore AI judgment, discomfort when present, and living insight when present."

  if_too_fable5_centered:
    - "Return to Living Review itself. Fable5 is dispatch target, not Root."

  if_human_seal_disappears:
    - "Restore Human Query Intervention / Human Final Seal."

  if_next_gate_unclear:
    - "Name next_gate explicitly."

  if_review_adds_noise:
    - "Use mini review or skip review by right-depth triage."

  if_ai_manufactures_slots:
    - "Apply slot_guard and state absence honestly."
```

---

## 16. GitHub Portability Check

A Living Review Skill should be portable across GitHub, chat, handoff, and future AI sessions.

Avoid tool-specific residue.  
Avoid stale path claims.  
Avoid claiming GitHub updates occurred unless Reality confirms.

### Programming-Like Block

```yaml
github_portability_check:
  must_preserve:
    - "semantic section titles"
    - "human-readable prose"
    - "explicit Programming-Like Blocks"
    - "Root / Fruit Guard"
    - "Human Final Seal boundary"
    - "Slot Guard against manufactured review content"

  must_avoid:
    - "legacy prefix taxonomy as central design"
    - "tool-specific residue"
    - "stale artifact claims"
    - "unverified GitHub completion claims"
    - "frontmatter-only implementation"
    - "mandatory blank-filling templates"
```

---

## 17. Full Rail / Next Gate

When the user requests Full Rail or Next Gate continuity, Living Review should preserve workflow momentum.

It should state, when relevant:

- result
- next action
- purpose
- what not to execute yet
- guard
- target path

### Programming-Like Block

```yaml
full_rail_next_gate:
  include_when_requested:
    - "result"
    - "next_action"
    - "purpose"
    - "do_not_execute_yet"
    - "guard"
    - "target_path_when_relevant"

  principle:
    - "Full Rail carries execution."
    - "Next Gate preserves direction."
    - "Human may intervene by query."
    - "AI keeps Living Review active."
    - "Do not manufacture slots for rail completeness."
```

---

## 18. Final Compression

```text
Living Review:

Not dead scoring.
Not praise-only.
Not fault-finding-only.
Not metadata-only.
Not frontmatter-only.
Not slot-filling performance.

AI reads the board.
AI names judgment.
AI names discomfort when present.
AI finds hidden pattern when present.
AI warns against misread when needed.
AI designs guard when risk exists.
AI gives correction condition when needed.
AI gives next natural move.

Do not fill slots to look alive.
Empty-slot performance is dead rubric.

違和感を必須にすると、AIは違和感を演じる。
空欄を許すことこそが、盤面を生かす。

Use the right depth.
Necessary deep-dive is good.
Low-value deep-dive is drift.

Living Review does not perform depth.
Living Review reads actual depth.

High-AI dispatch is checked when Root Knot appears.
Fable5 is a dispatch target, not Root.

Human may intervene by query.
Human keeps Final Seal.

Root is 主イェシュア・ハマシア.
```
