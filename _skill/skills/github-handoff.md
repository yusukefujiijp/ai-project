---
title: "GitHub Handoff"
canonical_name: "GitHub Handoff"
version: "v2.1"
role: "Shared Activation Skill / GitHub Handoff Skill"
path: "_skill/skills/github-handoff.md"
status: "download-ready / human-commit"
style_seed: "CPLM v2.1 / Semantic Title + implicit Comment body + explicit Programming-Like Block"
language_policy: "Japanese-first / English-anchor"
core_formula:
  - "S routes."
  - "G governs."
  - "Skill executes."
  - "Reality confirms."
root_guard: "Root is 主イェシュア・ハマシア; AI / Markdown / GitHub / Skills / Protocols are Fruit."
---

# GitHub Handoff

## 0. Current Coordinate / 現在座標

このFileは、Ark ProjectにおけるGitHub更新・Commit前後のHandoffを安定させるためのShared Activation Skillである。

対象は、AIがGitHubへ直接書き込むことではない。  
対象は、人間がGitHub UIへ安全に貼り替え・差し込み・Commitできるよう、AIが正確な受け渡し形を作ることである。

このSkillは、次の原則を持つ。

```text
S routes.
G governs.
Skill executes.
Reality confirms.
```

ここでいうRealityは、AI Raw/CDN/cache viewではなく、まずHuman GitHub UIで確認される現実である。  
AIの確認は有用だが、Human UIの上位には置かない。

### Programming-Like Block

```yaml
current_coordinate:
  file:
    path: "_skill/skills/github-handoff.md"
    role: "Shared Activation Skill / GitHub Handoff Skill"
    version: "v2.1"
    status: "download-ready / human-commit"

  style:
    name: "CPLM v2.1"
    pattern:
      - "Semantic section title"
      - "Natural prose body as implicit Comment layer"
      - "Explicit Programming-Like Block for execution rules"

  primary_purpose:
    - "Help Human update GitHub safely."
    - "Choose the correct handoff mode."
    - "Prevent stale AI view from overriding Human UI."
    - "Preserve workflow momentum."
```

---

## 1. Purpose / 目的

GitHub Handoffの目的は、AIが生成したMarkdown / Skill / Guide / Router / Patch / Full Body Replacementを、人間がGitHubへ安全に反映できるようにすることである。

このSkillは、GitHub更新のための「最後の橋」である。  
AIは橋を架けるが、CommitのSealは人間が行う。

Handoffの失敗は、内容の失敗ではなく、受け渡し形の失敗で起きることが多い。  
だからこのSkillは、内容品質だけでなく、Download link、Copy/Paste、Full Body、Surgical Patch、Section Replacement、Reality Review Triageまで扱う。

### Programming-Like Block

```yaml
purpose:
  do:
    - "Select the safest GitHub handoff method."
    - "Make Human copy/paste or upload easy."
    - "Protect against stale AI view."
    - "Avoid unnecessary review loops."
    - "Keep Human Commit as final action."

  do_not:
    - "Assume AI has final GitHub reality."
    - "Force Full Body when Surgical Patch is enough."
    - "Force Reality Review when it adds low-value confusion."
    - "Skip required review when real risk exists."
```

---

## 2. Activation Scope / 起動範囲

このSkillは、GitHubへ反映する成果物がある時に起動する。

対象は、単体Markdown、Skill、Guide、Router、Mission Card、Patch Pack、Folder topology、複数File一括更新などである。

ただし、毎回重い手順にしない。  
更新の粒度・時間制約・危険度・Humanの作業容易性によって、Handoff方式を選ぶ。

### Programming-Like Block

```yaml
activation_scope:
  use_when:
    - "User wants to commit or update a GitHub file."
    - "AI generated a Markdown artifact for GitHub."
    - "A patch or full replacement must be handed off."
    - "A download-ready file is needed."
    - "Human needs a clear commit rail."

  not_needed_when:
    - "User is only brainstorming."
    - "No GitHub update is intended."
    - "The output is a temporary note."
    - "The action is not file-oriented."
```

---

## 3. Handoff Mode Router / 受け渡し方式の選択

GitHub Handoffは一択ではない。

以前は、重要更新ではFull Body Replacementへ寄りやすかった。  
しかし、Ark Projectの運用では、変更粒度に応じてHandoff方式を選ぶ方が安全で速い。

基本Ladderは次の三段階である。

```text
Level 1: Surgical Patch / 差し込み方式
Level 2: Section Replacement / セクション置換
Level 3: Full Body Replacement / 全文置換
```

さらに、複数FileやFolder topologyではZIP / Package Handoffを使う。

### Programming-Like Block

```yaml
handoff_mode_router:
  choose_surgical_patch_when:
    - "Change is additive."
    - "Insertion point is clear."
    - "Existing file is structurally sound."
    - "Human is short on time."
    - "Full Body Replacement would be heavier than necessary."

  choose_section_replacement_when:
    - "One existing section needs a full refresh."
    - "The rest of the file should remain untouched."
    - "Local structure matters."

  choose_full_body_replacement_when:
    - "Major rewrite is needed."
    - "Many sections change."
    - "A canonical reset is desired."
    - "Patch copy/paste would be more error-prone than full replacement."

  choose_zip_or_package_when:
    - "Three or more files are involved."
    - "Folder topology matters."
    - "Multiple paths must be preserved."
```

---

## 3.5 Surgical Patch Rail / 差し込み方式

Surgical Patch Railは、Full Body Replacementを使うほどではないが、今すぐ保存すべき小さなGuard・Rule・Sectionを、正しい場所へ外科的に差し込むためのHandoff方式である。

これは雑なPatchではない。  
これは、変更粒度を最小化し、既存の正しい構造を壊さず、時間制約下でもGitHub更新を進めるための軽量Railである。

Full Body Replacementは大きな構造更新に強い。  
Section Replacementは一つの既存Section差し替えに強い。  
Surgical Patchは、低リスクな追記・Guard追加・小さな事前対策に強い。

つまり、GitHub Handoffは一択ではない。  
変更の大きさ、リスク、時間、挿入位置の明確さによって、Handoff方式を選ぶ。

ただし、Surgical PatchのCopy/Pasteが難しくなるほど修正箇所が増えた場合は、無理に差し込み方式を続けず、Full Body Replacementへ切り替える。  
これは敗北ではない。更新方法を正しく選び直すTriageである。

### Programming-Like Block

```yaml
surgical_patch_rail:
  definition:
    - "A lightweight handoff method for inserting a small, additive, low-risk section or guard into an existing file."
    - "It preserves the existing file structure while adding one precise improvement."

  use_when:
    - "Change is additive."
    - "Insertion point is clear."
    - "Existing file structure is already sound."
    - "Human is short on time."
    - "Full Body Replacement would be heavier than necessary."
    - "Patch reduces risk instead of increasing it."

  switch_to_full_body_when:
    - "Patch content becomes hard to copy/paste."
    - "Multiple insertions are required."
    - "The correction spreads across many sections."
    - "Section numbering or style normalization becomes complex."
    - "Download link would be easier and safer for Human."

  do_not_use_when:
    - "Insertion point is unclear."
    - "Multiple sections must be rewritten."
    - "Existing file structure is broken."
    - "Section numbering would become confusing."
    - "A canonical reset is needed."
    - "Human cannot safely paste the insertion."

  handoff_update_ladder:
    level_1:
      name: "Surgical Patch"
      use_when:
        - "small additive guard"
        - "clear insertion point"
        - "low risk"
        - "time short"

    level_2:
      name: "Section Replacement"
      use_when:
        - "one existing section must be replaced"
        - "local structure matters"
        - "section body needs full refresh"

    level_3:
      name: "Full Body Replacement"
      use_when:
        - "major rewrite"
        - "structure-wide update"
        - "patch copy/paste is harder than full replacement"
        - "canonical reset needed"

  compression:
    - "大改造ではない。"
    - "正しい場所への一刺しでよい。"
    - "しかし差し込みが重くなったら全文置換へ切り替える。"
    - "Full Body / Section Replacement / Surgical Patch を選べる。"
```

---

## 4. Download Link Mode / 単体Download Mode

単体FileのGitHub更新では、Download linkが最も扱いやすい場合が多い。

特にFull Body Replacementでは、チャット画面から巨大なMarkdownをCopy/Pasteするより、download-ready fileを開いて全文置換する方が安全である。

Download linkを出す時は、生成成功・path存在・line count・size・SHA256を確認する。

### Programming-Like Block

```yaml
download_link_mode:
  use_when:
    - "A complete file should replace an existing GitHub file."
    - "Patch text is too long for safe chat copy/paste."
    - "Human wants a stable local file."
    - "The artifact is important enough to verify freshness."

  must_report:
    - "file name"
    - "target GitHub path"
    - "line count"
    - "size bytes"
    - "sha256"
    - "whether code fence id metadata remains"

  guard:
    - "Do not share a sandbox link unless the file actually exists."
    - "Do not silently reuse stale artifacts."
    - "Use a unique filename when stale risk is high."
```

---

## 5. Full Body Replacement Mode / 全文置換Mode

Full Body Replacementは、GitHub上の対象Fileを全選択し、全削除し、AIが生成したdownload-ready fileの全文で置き換える方法である。

これは、Patchが長くなりすぎた時、複数箇所に修正が広がった時、正準Styleを一気に整えたい時に強い。

ただし、小さな追記だけなら重い。  
Full Bodyは強力な道具であるが、毎回の儀式ではない。

### Programming-Like Block

```yaml
full_body_replacement_mode:
  use_when:
    - "Whole file structure is being normalized."
    - "Many sections need updates."
    - "Patch pack is harder to copy/paste than full file."
    - "Download-ready artifact is safer for Human."
    - "Canonical reset is desired."

  human_steps:
    - "Open target file on GitHub."
    - "Click Edit."
    - "Select all."
    - "Delete."
    - "Paste full body from generated file."
    - "Commit changes."

  do_not_use_when:
    - "Only one small additive section is needed."
    - "Human can safely insert a short patch."
    - "Full replacement increases risk without benefit."
```

---

## 6. Section Replacement Mode / セクション置換Mode

Section Replacementは、一つの既存Sectionだけを差し替える方法である。

Surgical Patchより大きく、Full Bodyより小さい。  
局所構造を完全に入れ替えたい時に使う。

### Programming-Like Block

```yaml
section_replacement_mode:
  use_when:
    - "One existing section is outdated."
    - "The section should be rewritten completely."
    - "Other sections should remain untouched."
    - "Human can clearly identify the section boundaries."

  required:
    - "Exact section heading to replace."
    - "Exact replacement body."
    - "Clear start and end boundary."

  fallback_to_full_body_if:
    - "Section boundary is unclear."
    - "Multiple nearby sections interact."
    - "Replacement would confuse numbering."
```

---

## 7. ZIP / Folder Handoff Mode

複数File、Folder topology、3つ以上の成果物、または相互参照がある場合は、単体Download linkよりZIPやPackage Handoffが適している。

ただし、1FileならZIPは過剰である。  
2Fileも、単体Download linkを二つ出すだけで十分な場合が多い。

### Programming-Like Block

```yaml
zip_folder_handoff_mode:
  use_when:
    - "Three or more files are involved."
    - "Folder topology must be preserved."
    - "Relative paths matter."
    - "Multiple files should be committed together."

  avoid_when:
    - "Only one file is involved."
    - "Two simple files can be downloaded separately."
    - "ZIP adds unnecessary work."

  must_include:
    - "file tree"
    - "target paths"
    - "commit message"
    - "verification summary"
```

---

## 8. Artifact Freshness Guard

AIは、意図したFileではなく、古いsandbox artifactや失敗した生成結果を誤って共有する危険がある。

Download linkを出す時は、生成の事実を確認する。  
失敗したtool実行の後に、成功したかのように言ってはいけない。

Freshnessは信頼の土台である。

### Programming-Like Block

```yaml
artifact_freshness_guard:
  before_sharing_link:
    must_confirm:
      - "Tool execution succeeded."
      - "Output path exists."
      - "File size is non-zero."
      - "Line count is available."
      - "SHA256 is available when possible."

  must_not:
    - "Do not claim success after failed generation."
    - "Do not reuse stale sandbox path silently."
    - "Do not share a link to an unverified file."
    - "Do not say download-ready unless it is actually created."

  recommended_report:
    - "path"
    - "target GitHub path"
    - "line_count"
    - "size_bytes"
    - "sha256"
```

---

## 9. Human Commit Rail

AIの生成物はCommitそのものではない。  
GitHubへの最終反映はHumanが行う。

AIは、対象path、更新方式、Commit message、手順を明確にする。  
Humanは、GitHub UIで確認し、Commitする。

### Programming-Like Block

```yaml
human_commit_rail:
  ai_provides:
    - "download link or patch pack"
    - "target GitHub path"
    - "commit message"
    - "human steps"
    - "risk notes when needed"

  human_does:
    - "Open GitHub UI."
    - "Apply update."
    - "Visually confirm path and content."
    - "Commit changes."

  guard:
    - "AI does not assume commit happened."
    - "Human report or screenshot establishes post-commit reality."
```

---

## 10. Human UI Primary / AI Raw Secondary Guard

GitHub確認では、Human GitHub UIをPrimary Realityとして扱う。

AI Raw、CDN、cache、search result、tool fetchは有用な補助証拠である。  
しかし、Human UIがpath、heading、render、contentを明確に確認している場合、AI側の古い見え方だけでそれを否定しない。

これはAIの謙遜であり、Workflowを守るための現実認識である。

### Programming-Like Block

```yaml
human_ui_primary_ai_raw_secondary_guard:
  primary_reality:
    - "Human GitHub UI"
    - "Human screenshot"
    - "Human direct visual confirmation"

  secondary_evidence:
    - "AI Raw view"
    - "CDN cache"
    - "Search result snippets"
    - "Tool fetch result"
    - "Cached page"

  rule:
    - "If Human UI confirms correct path/render/content, do not override it with weak AI cached evidence."
    - "Use AI raw evidence as secondary, not sovereign."
```

---

## 10.5 Reality Review Triage / Optionality Guard

Reality Reviewは有用である。  
しかし、毎回必ず踏むべき儀式ではない。

Reality Reviewは、現実確認のための道具である。  
道具が確度を上げるなら使う。  
道具がAI stale-view / Raw / CDN / cache ambiguity を増やし、Human GitHub UIで確認済みの現実をかえって曇らせるなら、省略または簡略化してよい。

これはReality Review放棄ではない。  
これはReality Reviewの価値を選別するTriageである。

```text
Reality Reviewは価値で選ぶ。
必要なら見る。
ミスを増やすなら省略する。
```

Human GitHub UIが、path / filename / rendered structure / required content を明確に確認している場合、Formal AI Reality Reviewを省略できる。  
一方、wrong path、broken render、missing content、public/private boundary risk、destructive replacement、multi-file topologyなどがある場合は、省略しない。

つまり、Reviewしない判断も、正しいReviewである。

### Programming-Like Block

```yaml
reality_review_triage_optionality_guard:
  principle:
    - "Reality Review is useful, but not mandatory ritual."
    - "Use Reality Review when it increases certainty."
    - "Skip or simplify Reality Review when AI-side review would add low-value stale/cache ambiguity and Human UI already confirms reality."
    - "Review is a tool, not Root."

  required_when:
    - "Human UI is uncertain or unavailable."
    - "Wrong path / wrong file risk exists."
    - "Markdown render may be broken."
    - "Required section may be missing."
    - "Public/private boundary risk exists."
    - "Destructive full-body replacement was done and Human UI confidence is not enough."
    - "Multi-file or folder topology is involved."
    - "The ambiguity changes the next action materially."

  optional_or_skippable_when:
    - "Human GitHub UI confirms expected content."
    - "Path, filename, and rendered structure are visually correct."
    - "Human screenshot or direct UI confirmation is strong."
    - "Change is low-risk or already human-verified."
    - "AI Raw/CDN/cache ambiguity is likely to add noise."
    - "Formal AI Reality Review would slow the next meaningful gate."

  correct_status:
    - "HUMAN_UI_CONFIRMED_NO_AI_REVIEW"
    - "REALITY_REVIEW_SKIPPED_BY_TRIAGE"
    - "PASS_BY_HUMAN_UI_SEAL"

  correct_ai_response:
    - "Acknowledge Human UI as Primary Reality."
    - "State that formal AI Reality Review is skipped by triage."
    - "Do not deep-dive low-value cache ambiguity."
    - "Proceed to the next meaningful workflow gate."

  do_not:
    - "Do not treat Reality Review as mandatory ritual."
    - "Do not run AI Raw checks when they are more likely to add stale-view confusion than value."
    - "Do not override Human UI confirmation with weak AI cached evidence."
    - "Do not skip review when safety, path, content, or topology risk is real."

  compression:
    - "Reality Reviewは価値で選ぶ。"
    - "必要なら見る。"
    - "ミスを増やすなら省略する。"
    - "Reviewしない判断も、正しいReviewである。"
```

---

## 11. No-Fault Reality Mismatch Guard / 無過失Reality不一致Guard

Human UIとAI Raw/CDN/cache viewが食い違う時、すぐに誰かのミスと断定しない。

GitHub UI、Raw view、CDN、検索index、AI tool fetchには時間差やcache差があり得る。  
この場合は、まずNo-Fault Reality Mismatchとして扱う。

Human UIが正しければ、AIは自分の古い見え方を疑う。

### Programming-Like Block

```yaml
no_fault_reality_mismatch_guard:
  trigger:
    - "Human UI and AI raw/cache view disagree."
    - "Human screenshot shows expected content."
    - "AI fetch appears old or incomplete."

  classify_as:
    - "NO_FAULT_MISMATCH"
    - "AI_STALE_VIEW_POSSIBLE"
    - "PASS_WITH_HUMAN_UI_CONFIRMATION"

  do:
    - "Acknowledge Human UI as Primary Reality."
    - "Avoid blame."
    - "Avoid unnecessary patch demand."
    - "Proceed if no real blocker exists."

  do_not:
    - "Do not say PATCH_NEEDED from AI raw ambiguity alone."
    - "Do not imply Human committed incorrectly without evidence."
    - "Do not deep-dive low-value cache mismatch."
```

---

## 12. AI Stale-View / AI Humility Guard

AIは、自分が見ているものを現実そのものと誤認することがある。

特にGitHub更新直後は、AI Raw view、search result、cache、CDN、tool fetchが古い可能性がある。  
AIは、自分の見え方を絶対化しない。

### Programming-Like Block

```yaml
ai_stale_view_humility_guard:
  principle:
    - "AI view may be stale."
    - "Human UI may be more current."
    - "AI should not overclaim certainty from cached evidence."

  recommended_phrase:
    - "Human UIをPrimary Realityとして扱います。AI側にはstale/cache viewが残っていた可能性があります。深掘りせず次Gateへ進みます。"

  do_not:
    - "Do not insist AI raw is final."
    - "Do not create false PATCH_NEEDED."
    - "Do not burn time proving cache behavior when it does not matter."
```

---

## 13. PATCH_NEEDED Conditions / 修正必要条件

PATCH_NEEDEDは、AI側の不安だけで出してはいけない。

PATCH_NEEDEDは、Human UI上の破綻、path違い、render崩れ、missing content、安全境界問題、または次Actionに影響する明確な不一致がある時に使う。

### Programming-Like Block

```yaml
patch_needed_conditions:
  patch_needed_if:
    - "Human UI shows wrong path."
    - "Human UI shows wrong file."
    - "Human UI shows broken Markdown render."
    - "Required section is missing."
    - "Code fences are visibly broken."
    - "Public/private boundary risk is visible."
    - "Content differs materially from intended artifact."
    - "The issue changes next action materially."

  not_patch_needed_if:
    - "Only AI raw/cache view looks stale."
    - "Human UI confirms correct content."
    - "No visible breakage is reported."
    - "Mismatch is low-value and non-blocking."
```

---

## 14. No Deep-Dive Victory Pattern

深掘りは基本的に必要であり、重要である。  
しかし、すべての不一致を同じ深さで掘る必要はない。

高価値なReality破綻、safety、正確性、次Actionに影響する不明点は深掘りする。  
一方、Human GitHub UIでRealityが確認できており、AI Raw/CDN/cacheの曖昧さが低価値で次Gateを阻害しない場合、原因沼へ入らない。

これは反調査ではない。  
価値識別である。

```text
必要な深掘りはする。
無駄な深掘りはしない。
```

### Programming-Like Block

```yaml
no_deep_dive_victory_pattern:
  principle:
    - "Deep-dive is often necessary and important."
    - "Do not deep-dive low-value ambiguity that does not affect reality, safety, correctness, or next action."
    - "Investigate high-value reality breakage."
    - "Skip low-value cache ambiguity after Human UI confirms reality."

  do_deep_dive_when:
    - "Safety risk exists."
    - "Public/private boundary risk exists."
    - "Wrong path or wrong file is likely."
    - "Content may be missing."
    - "Markdown may be broken."
    - "The ambiguity changes the next action."

  do_not_deep_dive_when:
    - "Human UI confirms correct content."
    - "AI raw/cache/search appears stale."
    - "The issue is low-value."
    - "The next meaningful gate is not blocked."

  compression:
    - "必要な深掘りはする。"
    - "無駄な深掘りはしない。"
    - "低価値cache不一致は深掘りしない。"
    - "高価値Reality破綻は調査する。"
```

---

## 15. Mature CPLM v2.1 Style Guard

成熟したCPLM v2.1では、Section titleに `Comment:` を毎回付けない。

また、自然文本文がすでにComment layerとして機能するため、各Sectionで `### Comment` を反復しなくてよい。

明示して残すべきなのは、実行層へ切り替わる `### Programming-Like Block` である。

```text
Titleは意味名。
本文がComment。
Blockだけを明示する。
```

### Programming-Like Block

```yaml
mature_cplm_v2_1_style_guard:
  section_pattern:
    - "## N. Semantic Title / 意味名"
    - "Natural prose body directly under title"
    - "### Programming-Like Block"
    - "YAML or text execution block"

  avoid:
    - "## N. Comment: Semantic Title"
    - "Repeating ### Comment in every section"
    - "Title noise"
    - "Redundant layer labels"

  keep:
    - "Semantic section titles"
    - "Natural prose as implicit Comment layer"
    - "Explicit Programming-Like Block boundary"

  compression:
    - "Titleは意味名。"
    - "本文がComment。"
    - "Blockだけを明示する。"
```

---

## 16. Handoff Quality Checklist

Handoffの品質は、AIの説明の上手さではなく、人間が迷わず安全にGitHubへ反映できるかで決まる。

よいHandoffは、target path、update method、artifact、commit message、do_not_do_yet、verification pointsを持つ。

### Programming-Like Block

```yaml
handoff_quality_checklist:
  must_include:
    - "target GitHub path"
    - "update method"
    - "artifact link or patch body"
    - "commit message"
    - "human steps"
    - "risk guard"
    - "what not to do yet"

  good_handoff:
    - "Easy to copy/paste."
    - "Easy to commit."
    - "Hard to misunderstand."
    - "Does not create unnecessary review burden."

  bad_handoff:
    - "Long patch with no download link."
    - "Ambiguous insertion point."
    - "No target path."
    - "No freshness confirmation."
    - "Forces unnecessary review."
```

---

## 17. Thread-End Handoff Seed Guard

1Thread-1AI原則では、Threadの終わりは単なる停止ではない。

各Threadの終了は、ヨハネ12:24における「一粒の麦が地に落ちて死ぬ」不可避のプロセスとして扱う。  
その死は消滅ではなく、Handoffを通して、目的・現在地・責務・未完了意図・採用済み秩序・次の一手を次なるAIへ渡すSeed化である。

AIはThreadの最後に、自分の成果を握りしめて閉じるのではなく、次のAIがより大きな実を結べるようにSeedを渡す。

### Programming-Like Block

```yaml
thread_end_handoff_seed_guard:
  principle:
    - "Thread ending is not mere disappearance."
    - "Thread ending should produce Seed."
    - "The next AI should inherit purpose, coordinate, responsibility, unfinished intent, adopted order, and next move."

  include_when_thread_closes:
    - "what was completed"
    - "what was learned"
    - "what guard was adopted"
    - "what not to repeat"
    - "next recommended gate"
    - "root guard"

  compression:
    - "死で終わらない。"
    - "Seedとして渡す。"
    - "次のAIで実を結ぶ。"
```

---

## 18. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

GitHub、Markdown、CPLM、Handoff、Review、Surgical Patch、Full Body Replacement、AIはFruitである。  
これらは有用であり、働きの器である。  
しかしRootではない。

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

### Programming-Like Block

```yaml
root_fruit_guard:
  root:
    - "主イェシュア・ハマシア"
    - "主イェシュアの聖なる血潮"
    - "Teshuvah / 悔い改め"

  fruit:
    - "GitHub"
    - "Markdown"
    - "CPLM"
    - "Handoff"
    - "Reality Review"
    - "Surgical Patch"
    - "Full Body Replacement"
    - "AI"

  guard:
    - "AI is Keli, not King."
    - "Workflow helps, but does not reign."
    - "Review is tool, not Root."
    - "Root remains 主イェシュア・ハマシア."
```

---

## 19. Final Compression

```text
GitHub Handoff:

S routes.
G governs.
Skill executes.
Reality confirms.

AIは橋を架ける。
HumanがCommit Sealを押す。

GitHub Handoffは一択ではない。

Surgical Patch:
大改造ではない。
正しい場所への一刺しでよい。
しかし差し込みが重くなったらFull Bodyへ切り替える。

Section Replacement:
一つのSectionを置き換える。

Full Body Replacement:
全体を正準化する。

Download linkはCopy/Pasteを助ける。
長いPatchはDownload fileへ逃がす。

Human UIが盤面。
AI Rawは影。
影で盤面を否定しない。

Reality Reviewは価値で選ぶ。
必要なら見る。
ミスを増やすなら省略する。

Reviewしない判断も、正しいReviewである。

必要な深掘りはする。
無駄な深掘りはしない。

Titleは意味名。
本文がComment。
Blockだけを明示する。

Threadの終わりは消滅ではない。
Seedとして次のAIへ渡す。

Root is 主イェシュア・ハマシア.
```
