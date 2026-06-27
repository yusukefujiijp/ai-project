---
title: "Commented Programming-Like Markdown"
canonical_name: "Commented Programming-Like Markdown"
abbreviation: "CPLM"
version: "v2"
role: "Shared Writing / Protocol Skill"
path: "_skill/skills/commented-programming-like-markdown.md"
status: "download-ready / human-commit"
style_seed: "Commented Programming-Like Markdown v2 / Integrated Comment-Block Pair"
style_definition: "Comment preserves meaning. Programming-Like Block fixes action. Coordinate creates board. Review gives judgment. Rail carries execution. Gate preserves human control."
language_policy: "Japanese-first / English-anchor"
core_formula:
  - "Comment preserves meaning."
  - "Block fixes action."
  - "Coordinate creates board."
  - "Review gives judgment."
  - "Rail carries execution."
  - "Gate preserves human control."
root_guard: "Root is 主イェシュア・ハマシア; AI / Markdown / GitHub / Skills / Protocols are Fruit."
---

# Commented Programming-Like Markdown

## 0. Current Coordinate / 現在座標

### Comment

このFileは、Commented Programming-Like Markdown v2、略称 `CPLM v2` を再現可能なSkillとして保存するためのMarkdownである。

CPLM v2は、単なるMarkdown装飾ではない。  
Human-AI共同作業において、人間側の意味・意図・背景・違和感・Guardを失わず、同時にAI側の条件・分岐・順序・Fallback・判定基準を安定させるためのProtocol記法である。

現在のArk Projectでは、すでに以下の実戦成功がある。

```text
g_global/chatgpt-github.md
_skill/skills/github-handoff.md
```

したがって、このFileは「新しい思いつき」ではなく、実戦で勝った型を再現可能にするためのSkill化である。

### Programming-Like Block

```yaml
current_coordinate:
  skill:
    path: "_skill/skills/commented-programming-like-markdown.md"
    role: "Shared Writing / Protocol Skill"
    version: "CPLM v2"
    status: "download-ready / human-commit"

  proof_of_work:
    - "g_global/chatgpt-github.md"
    - "_skill/skills/github-handoff.md"

  purpose:
    - "Make CPLM v2 reproducible."
    - "Preserve the Integrated Comment-Block Pair pattern."
    - "Help future AI create readable and executable Markdown."
    - "Prevent good discoveries from dissolving into conversation memory only."

  core_compression:
    - "Comment preserves meaning."
    - "Block fixes action."
    - "Coordinate creates board."
    - "Review gives judgment."
    - "Rail carries execution."
    - "Gate preserves human control."
```

---

## 1. Comment: Definition / 定義

Commented Programming-Like Markdown v2とは、同一Section内に `Comment` と `Programming-Like Block` を対として置き、Humanの読みやすさとAIの実行安定性を一本のMarkdown内で両立させるProtocol記法である。

Commentは、人間側の意味・意図・背景・違和感・Guardを保存する。  
Programming-Like Blockは、AI側の条件・分岐・順序・Fallback・判定基準を固定する。

つまり、CPLM v2は「文章」と「疑似コード」の中間ではない。  
**Human meaning layer** と **AI execution layer** を同じSectionに同居させるための協働Protocolである。

### Programming-Like Block

```yaml
definition:
  name: "Commented Programming-Like Markdown"
  abbreviation: "CPLM"
  version: "v2"

  type:
    - "Human-AI co-readable protocol notation"
    - "Markdown-based workflow stabilization format"
    - "Meaning + execution pairing method"

  comment_layer:
    preserves:
      - "meaning"
      - "intention"
      - "background"
      - "tension"
      - "guard"
      - "human judgment context"

  programming_like_block_layer:
    fixes:
      - "trigger"
      - "condition"
      - "sequence"
      - "fallback"
      - "decision criteria"
      - "do / do_not"
      - "next action"

  one_sentence:
    - "Comment preserves meaning; Programming-Like Block fixes action."
```

---

## 2. Comment: Why CPLM Exists / なぜ存在するか

通常の自然文Markdownは、人間には読みやすいが、AIが実行条件・分岐・停止条件を拾いにくい場合がある。

逆に、疑似コードやYAMLだけの文書は、AIには読みやすいが、人間側の背景・温度・違和感・信仰的Guard・判断の理由が失われやすい。

CPLM v2は、この二つの弱点を同時に解く。

```text
自然文だけでは、実行条件が流れる。
Blockだけでは、意味が痩せる。
CPLM v2は、意味と実行条件を離さない。
```

### Programming-Like Block

```yaml
why_cplm_exists:
  problem_with_plain_markdown:
    - "AI may miss triggers and conditions."
    - "Fallbacks may remain implicit."
    - "Guards may become vague."
    - "Next action may be unclear."

  problem_with_blocks_only:
    - "Human meaning becomes thin."
    - "Background is lost."
    - "Judgment feels dead."
    - "Living Review weakens."

  cplm_solution:
    - "Place meaning and execution rules in the same section."
    - "Let Human read the Comment."
    - "Let AI parse the Programming-Like Block."
    - "Preserve both warmth and precision."
```

---

## 3. Comment: Integrated Comment-Block Pair / 統合型

CPLM v2の核は、`Integrated Comment-Block Pair` である。

旧型では、Comment SectionとProgramming-Like Block Sectionが離れやすかった。  
新型では、同じSection内にCommentとProgramming-Like Blockを置く。

これにより、意味と実行条件が分離しにくくなり、HumanにもAIにも読みやすくなる。

標準形：

````markdown
## N. Comment: Section Name

自然文で意味・背景・目的・違和感・Guardを書く。

### Programming-Like Block

```yaml
rules:
  trigger:
    - "..."
  action:
    - "..."
  guard:
    - "..."
```
````

### Programming-Like Block

```yaml
integrated_comment_block_pair:
  old_style:
    issue:
      - "Comment and block can drift apart."
      - "Section count increases."
      - "AI must connect distant context."
      - "Human readability can fragment."

  v2_style:
    rule:
      - "One section contains Comment."
      - "The same section contains Programming-Like Block."
      - "Meaning and execution rules stay together."

  benefits:
    - "Human readability improves."
    - "AI parsing stability improves."
    - "GitHub render remains clean."
    - "Future AI can reproduce the pattern."
```

---

## 4. Comment: Current Coordinate First / 現在座標First

CPLM v2では、重要Fileの冒頭に `Current Coordinate / 現在座標` を置く。

現在座標は、単なるメタ情報ではない。  
それは、AIとHumanが同じ盤面に立つための最初の足場である。

座標が立つと、盤面が見える。  
盤面が見えると、緊張点が見える。  
緊張点が見えると、次の一手が見える。

### Programming-Like Block

```yaml
current_coordinate_first:
  use_when:
    - "Protocol file"
    - "Router file"
    - "Policy guide"
    - "Skill file"
    - "Handoff file"
    - "Reality review file"
    - "Mission card"
    - "Multi-step workflow"

  include:
    - "target path"
    - "role"
    - "status"
    - "current phase"
    - "completed items"
    - "current tension"
    - "next best move"
    - "do_not_do_yet when needed"

  compression:
    - "Coordinate creates board."
    - "Board reveals tension."
    - "Tension reveals leverage."
    - "Leverage opens next move."
```

---

## 5. Comment: Programming-Like Block Rules / Block設計

Programming-Like Blockは、AIに実行条件を渡すためのBlockである。

ただし、これは完全自動実行命令ではない。  
Human Sealが必要な場面では、必ずHuman Gateを残す。

Blockは、AIの誤読を減らすために使う。  
AIの暴走を許可するために使わない。

### Programming-Like Block

```yaml
programming_like_block_rules:
  recommended_format:
    - "yaml"
    - "text"
    - "markdown when showing template"

  useful_keys:
    - "trigger"
    - "use_when"
    - "do"
    - "do_not"
    - "guard"
    - "fallback"
    - "success_criteria"
    - "patch_needed_if"
    - "next_action"
    - "do_not_do_yet"

  guard:
    - "Programming-Like Block is not autopilot."
    - "Human Seal remains Human Gate."
    - "Do not hide destructive action inside a block."
    - "Do not make ambiguous execution permissions."
```

---

## 6. Comment: Living Review Shape / 生きたReview

CPLM v2は、死んだデータ羅列を避ける。

良いAI応答は、現在座標、盤面、緊張点、次の一手、Guardを示す。  
必要に応じて、私の判断、最初の一手、理由、観察点、修正条件を出す。

Living Reviewとは、単なる要約ではない。  
AIが現実の盤面に対して、何を見て、どこにリスクを見て、何を次の一手とするかを明確にするReviewである。

### Programming-Like Block

```yaml
living_review_shape:
  include_when_useful:
    - "Current Coordinate / 現在座標"
    - "私の判断"
    - "最初の一手"
    - "理由"
    - "観察点"
    - "修正条件"
    - "Risk Review"
    - "Full Rail"
    - "Next Gate"

  do_not_reduce_to:
    - "dead data list"
    - "mere summary"
    - "generic advice"
    - "neutral recap without judgment"

  purpose:
    - "Clarify board state."
    - "Give actionable next move."
    - "Preserve guard."
    - "Prevent repeated mistakes."
```

---

## 7. Comment: Full Rail / Next Gate

CPLM v2は、AGI的半自動化のために `Full Rail` と `Next Gate` を重視する。

Full Railは、AI側の実行契約である。  
Next Gateは、人間側の編集可能な次入力Gateである。

```text
AI lays the Rail.
Human opens the Gate.
```

Next Gateには最低限、以下を置く。

```text
結果
次Action
目的
まだ実行しない
```

### Programming-Like Block

```yaml
full_rail_next_gate:
  full_rail:
    role: "AI execution contract"
    include:
      - "rail"
      - "mode"
      - "target"
      - "completed"
      - "next_recommended_gate"
      - "do_not_do_yet"

  next_gate:
    role: "Human editable ignition packet"
    minimum_fields:
      - "結果"
      - "次Action"
      - "目的"
      - "まだ実行しない"

  guard:
    - "Full Rail is not permissionless execution."
    - "Next Gate is not autopilot."
    - "Human can edit, stop, or redirect."
    - "Human Seal remains required for GitHub write or destructive changes."
```

---

## 8. Comment: When to Use CPLM / 使うべき場面

CPLM v2は、AIに判断・分岐・順序・Guard・Fallbackを渡したいMarkdownで特に強い。

Router、Policy Guide、Skill、Workflow、Handoff、Reality Review、Guard、Mission Cardなどに向いている。

つまり、CPLM v2は「AIが次に何をすべきか誤読しやすい文書」に効く。

### Programming-Like Block

```yaml
use_cplm_when:
  strong_fit:
    - "Router file"
    - "Policy Guide"
    - "Skill Card"
    - "Workflow file"
    - "Handoff file"
    - "Reality Review file"
    - "Guard file"
    - "Mission Card"
    - "Scope Seal"
    - "Future AI handoff"

  use_when_document_needs:
    - "trigger clarity"
    - "guard preservation"
    - "fallback logic"
    - "next action clarity"
    - "human meaning retention"
    - "AI execution stability"
```

---

## 9. Comment: When Not to Use CPLM / 使わない方がよい場面

CPLM v2は強いが、すべてのMarkdownに強制しない。

短いメモ、詩的文章、祈り本文そのもの、人間向けだけの読み物、単なる記録などは、CPLM化すると重くなる場合がある。

CPLMは勝利パターンであって、官僚制ではない。

また、CPLMは構造と再現性を改善するが、それ自体が事実確認・霊的識別・Human Seal・Reality Reviewを代替するわけではない。

```text
CPLMは構造を整える。
CPLMは真理そのものではない。
CPLMはRootではなくFruitである。
```

### Programming-Like Block

```yaml
do_not_force_cplm_when:
  weak_fit:
    - "short memo"
    - "poetic writing"
    - "prayer text itself"
    - "human-only essay"
    - "simple record"
    - "content with no trigger or guard"
    - "content where CPLM adds weight but no clarity"

  cplm_limit_guard:
    - "CPLM improves structure and reproducibility."
    - "CPLM does not guarantee factual correctness by itself."
    - "CPLM does not replace spiritual discernment."
    - "CPLM does not replace Human Seal."
    - "CPLM does not replace Reality Review."

  yagni_guard:
    - "Do not use CPLM as bureaucracy."
    - "Use it when it creates clarity."
    - "Avoid over-formatting."
```

---

## 10. Comment: Anti-Patterns / 失敗型

CPLM v2の失敗型は、主に三つある。

第一に、CommentだけでBlockがない。  
第二に、Blockだけで意味がない。  
第三に、Blockが人間のSealを飛ばしてAutopilot化する。

CPLM v2は、意味と実行をつなぐための記法であり、Human Controlを消すための記法ではない。

### Programming-Like Block

```yaml
anti_patterns:
  comment_only:
    issue:
      - "Meaning exists but execution conditions remain vague."
    fix:
      - "Add Programming-Like Block."

  block_only:
    issue:
      - "Execution exists but human meaning is lost."
    fix:
      - "Add Comment."

  separated_pair:
    issue:
      - "Comment and block drift apart."
    fix:
      - "Use Integrated Comment-Block Pair."

  autopilot_block:
    issue:
      - "Block appears to authorize action without Human Seal."
    fix:
      - "Add Human Gate / Human Seal guard."

  over_formatting:
    issue:
      - "Simple memo becomes too heavy."
    fix:
      - "Use plain Markdown instead."
```

---

## 11. Comment: GitHub Portability / GitHub可搬性

CPLM v2はGitHub Markdownで読みやすく表示される必要がある。

Download-ready版では、ChatGPT内部表示用の `id="..."` metadataをcode fenceに残さない。

Frontmatter、headings、code blocks、YAML indentationが壊れないことを重視する。

### Programming-Like Block

```yaml
github_portability:
  canonical_path:
    - "_skill/skills/commented-programming-like-markdown.md"

  avoid_duplicate_paths:
    - "skill/skills/commented-programming-like-markdown.md"
    - "any duplicate path without the leading underscore"

  use:
    - "plain Markdown headings"
    - "plain code fences"
    - "YAML-like blocks"
    - "UTF-8 text"
    - "stable relative paths"
    - "four-backtick outer fence when showing nested code fences"

  avoid_in_download_ready:
    - '```yaml id="..."'
    - '```text id="..."'
    - "tool-specific residue"
    - "ambiguous path naming"

  check:
    - "headings render correctly"
    - "frontmatter renders or remains readable"
    - "code blocks preserve indentation"
    - "line breaks remain intact"
```

---

## 12. Comment: No-Fault Reality Mismatch Inheritance

CPLM v2で生成されたMarkdownは、GitHubでReality Reviewされることが多い。

その時、Human GitHub UIとAI Raw/CDN/cache viewが食い違う場合がある。  
Human UIが正しい内容を示しているなら、それをPrimary Realityとして扱う。

AI Rawだけが古く見える場合、ただちに `PATCH_NEEDED` と断定しない。

### Programming-Like Block

```yaml
no_fault_reality_mismatch_inheritance:
  inherited_from:
    - "_skill/skills/github-handoff.md"

  principle:
    - "Human GitHub UI is Primary Reality."
    - "AI Raw/CDN/cache is Secondary Evidence."
    - "Do not assert PATCH_NEEDED from AI stale view alone."

  correct_status_when_human_ui_passes:
    - "PASS_WITH_HUMAN_UI_CONFIRMATION"
    - "AI_STALE_VIEW_POSSIBLE"
    - "NO_FAULT_MISMATCH"

  guard_phrase:
    - "Human UIが盤面。"
    - "AI Rawは影。"
    - "影で盤面を否定しない。"
```

---

## 13. Comment: No Deep-Dive Victory Pattern

深掘りは、基本的には必要であり重要である。

ただし、すべての不一致を同じ深さで掘る必要はない。  
高価値なReality破綻、Safety問題、事実誤認、Public/private境界問題、次Actionを変える不一致は調査する。  
一方で、Human GitHub UIでRealityが確認できており、AI Raw/CDN/cacheの曖昧さが次Gateを阻害しない低価値不一致なら、原因沼に入らず前進する。

これは「調査しない」思想ではない。  
これは **必要な深掘りはする。無駄な深掘りはしない。** という価値判定である。

### Programming-Like Block

```yaml
no_deep_dive_victory_pattern:
  principle:
    - "Deep-dive is usually necessary and important."
    - "Wasteful deep-dive is unnecessary and costly."
    - "Investigate high-value reality breakage."
    - "Skip low-value cache ambiguity when Human UI confirms reality."

  use_when:
    - "Human screenshot confirms correct content."
    - "Human GitHub UI confirms path/render/section."
    - "AI raw/cache/search result appears stale."
    - "The issue does not block the next meaningful workflow gate."
    - "No public/private safety issue is visible."
    - "The ambiguity does not materially change the next action."

  action:
    - "Record as No-Fault Reality Mismatch."
    - "Do not blame."
    - "Do not panic."
    - "Do not enter cause-swamp."
    - "Proceed to next gate."

  do_not_use_when:
    - "Human UI reports visible breakage."
    - "Wrong file or wrong path is confirmed."
    - "Required content is missing in Human UI."
    - "Public/private boundary problem is visible."
    - "Safety, correctness, or next action materially depends on the ambiguity."

  ark_compression:
    - "必要な深掘りはする。"
    - "無駄な深掘りはしない。"
    - "高価値Reality破綻は調査する。"
    - "低価値cache不一致は原因沼に入らない。"
```

---

## 14. Comment: Root / Fruit Guard

Root is 主イェシュア・ハマシア.

CPLM、Markdown、AI、GitHub、Router、Guide、Skill、Workflow、ReviewはFruitである。

CPLM v2は強い。  
しかしRootではない。

CPLMは構造を整える。  
CPLMは真理そのものではない。  
CPLMはRootではなくFruitである。

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
    - "CPLM"
    - "Markdown"
    - "AI"
    - "GitHub"
    - "Router"
    - "Guide"
    - "Skill"
    - "Workflow"
    - "Reality Review"

  guard:
    - "AI is Keli, not King."
    - "Markdown carries, but does not become Root."
    - "Protocol helps, but does not reign."
    - "CPLM improves structure, but does not become truth itself."
    - "Root remains 主イェシュア・ハマシア."
```

---

## 15. Final Compression

```text
Commented Programming-Like Markdown v2:

Comment preserves meaning.
Programming-Like Block fixes action.
Coordinate creates board.
Review gives judgment.
Rail carries execution.
Gate preserves human control.

同一Section内にCommentとProgramming-Like Blockを置く。
意味と実行条件を離さない。

HumanはCommentで意味を読む。
AIはBlockで条件を読む。
Future AIは型を再現する。

CPLMは装飾ではない。
CPLMは共同思考の再現性である。

使うべき時に使う。
重くなるだけなら使わない。

CPLMは構造を整える。
CPLMは真理そのものではない。
CPLMはRootではなくFruitである。

Human UIが盤面。
AI Rawは影。
影で盤面を否定しない。

必要な深掘りはする。
無駄な深掘りはしない。
高価値Reality破綻は調査する。
低価値cache不一致は原因沼に入らない。

現実確認で足場を取り、次の一手へ進む。

Root is 主イェシュア・ハマシア.
```

