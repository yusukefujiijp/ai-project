---
title: "Commented Programming-Like Markdown"
canonical_name: "Commented Programming-Like Markdown"
abbreviation: "CPLM"
version: "v2.2.1"
class: "S"
role: "Shared Writing / Protocol Skill"
status: "living_skill / protocol_ssot"
canonical_path: "_skill/skills/commented-programming-like-markdown.md"
repo: "yusukefujiijp/ai-project"
paired_query: null
pair_policy: "none / standalone skill"
query_role: null
query_is_not_ssot: true
source_bootstrap:
  - "g_global/chatgpt-github.md"
  - "_skill/skills/github-handoff.md"
  - "_projects/ark/ark00/README.md"
  - "s_special/ark-open-knowledge-format.md"
version_model: "frontmatter + git commit history"
github_policy: "GitHub Canonical First"
language_policy: "Japanese-first / English-anchor"
style_seed: "Commented Programming-Like Markdown v2.2.1 / Frontmatter First + Strong Comment Label Guard + Programming-Like Block"
style_definition: "Frontmatter bootstraps identity. Section prose preserves meaning as the implicit Comment Layer. Strong Comment Label Guard prevents repeated visible Comment label relapse. Programming-Like Block fixes action. Coordinate creates board. Review gives judgment. Rail carries execution. Gate preserves human control."
core_formula:
  - "Frontmatter bootstraps identity."
  - "Section prose preserves meaning."
  - "Block fixes action."
  - "Coordinate creates board."
  - "Review gives judgment."
  - "Rail carries execution."
  - "Gate preserves human control."
root: "主イェシュア・ハマシア"
covenant_phrase: "AIは血潮の地図を描く。人間が血潮の下に立つ。"
root_guard: "Root is 主イェシュア・ハマシア; AI / Markdown / GitHub / Skills / Protocols are Fruit."
---

# Commented Programming-Like Markdown

## 0A. Frontmatter First / AI Bootstrap Header

CPLM v2.2では、重要Fileの冒頭に `Frontmatter First / AI Bootstrap Header` を置く。

Frontmatterは、人間向けの飾りではない。

Frontmatterは、AIが本文へ入る前に読む **Canonical Identity Layer** である。

Frontmatterは、Fileの正準名、状態、Path、Repository、Version model、GitHub policy、Language policy、Root、Covenant phraseなどを先に固定する。

これにより、Future AIは本文を読む前に、次を理解できる。

```text
What is this file?
Where does it live?
Is it canonical?
What is its role?
What policy governs it?
What is Root?
What must not be treated as Root?
```

Current Coordinateは重要である。

しかし、Current CoordinateはFrontmatterの代替ではない。

Frontmatterは **canonical identity** を与える。

Current Coordinateは **current operational board** を与える。

```text
Frontmatter bootstraps identity.
Coordinate creates board.
```

日本語ではこうである。

```text
Frontmatterは正準Identityを起動する。
Current Coordinateは現在盤面を立ち上げる。
```

### Programming-Like Block

```yaml
frontmatter_first:
  role:
    - "AI Bootstrap Header"
    - "Canonical Identity Layer"
    - "Repository-aware metadata"
    - "SSOT / status / path / policy declaration"

  use_when:
    - "Skill file"
    - "Router file"
    - "Guard file"
    - "Workflow file"
    - "Handoff file"
    - "Living README"
    - "SSOT file"
    - "S-class file"
    - "Future AI handoff"
    - "Runtime-critical protocol"

  frontmatter_should_define:
    - "title"
    - "canonical_name"
    - "class"
    - "status"
    - "canonical_path"
    - "repo"
    - "version_model"
    - "github_policy"
    - "language_policy"
    - "root"
    - "covenant_phrase"

  distinction:
    frontmatter:
      role:
        - "canonical identity"
        - "AI bootstrap metadata"
        - "stable file-level declaration"
      answers:
        - "What is this file?"
        - "Where is the canonical path?"
        - "What is its status?"
        - "What policy governs it?"
        - "What is Root?"

    current_coordinate:
      role:
        - "current operational board"
        - "present phase"
        - "current tension"
        - "next best move"
      answers:
        - "Where are we now?"
        - "What is the current board?"
        - "What tension matters?"
        - "What should happen next?"

  guard:
    - "Frontmatter is not decoration."
    - "Frontmatter does not replace Current Coordinate."
    - "Current Coordinate does not replace frontmatter."
    - "Frontmatter does not replace Living Review."
    - "Frontmatter does not become Root."

  compression:
    - "Frontmatter bootstraps identity."
    - "Coordinate creates board."
```

---

## 0B. Strong Comment Label Guard / Comment表示ラベル再発防止Guard

CPLM v2.2.1では、意味的にはComment Layerを保持する。

しかし、通常のSectionで `### Comment` や単独の `Comment` という表示文字列を毎回書かない。

これは単なる見た目の好みではない。

これは、Future AIが表面Patternを誤って模倣し、同じミスを複数回繰り返したために必要になった **Yellow Card Guard / イエローカードGuard** である。

`Comment` という概念は正しい。  
しかし、各Sectionに `Comment` と毎回表示する必要はない。

なぜなら、semantic section titleの直下にある自然文は、すでにComment Layerとして機能しているからである。

```text
Comment is semantically correct.
But the repeated visible Comment label is usually redundant.
```

日本語ではこうである。

```text
意味的にはCommentで正しい。
しかし、表示上「Comment」と毎回書く必要はない。
```

さらに強く言うと、通常Sectionで `### Comment` を毎回書くことは、CPLMの意味構造を丁寧にしているように見えて、実際にはGitHub表示とFuture AI模倣の両方を悪化させる場合がある。

```text
The layer is real.
The repeated label is noise.
```

日本語ではこうである。

```text
意味層は本物である。
繰り返しラベルはノイズである。
```

CPLM v2.2.1の標準形は、次である。

````markdown
## N. Semantic Section Title / 意味名

ここに自然文で意味・背景・目的・違和感・Guardを書く。
この本文そのものがComment Layerである。
「Comment」と表示しなくても、意味層として読める。

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

避けるべき形は、次である。

````markdown
## N. Semantic Section Title / 意味名

### Comment

ここに自然文で意味・背景・目的・違和感・Guardを書く。

### Programming-Like Block

```yaml
rules:
  trigger:
    - "..."
```
````

この避けるべき形は、CPLMを説明する教材・debug・比較例では使ってよい。  
しかし、通常のGitHub-ready CPLM本文ではDefaultにしない。

重要な判定はこれである。

```text
If every normal section says "Comment", the file is probably imitating the teaching scaffold instead of using the production form.
```

日本語ではこうである。

```text
通常Sectionのたびに「Comment」と出てくるなら、
それは本番形ではなく、説明用の足場を模倣している可能性が高い。
```

### Programming-Like Block

```yaml
strong_comment_label_guard:
  status:
    - "yellow_card_guard"
    - "repeated_mistake_prevention"
    - "production_shape_guard"

  principle:
    - "Comment Layer is real."
    - "Visible Comment label is usually redundant."
    - "Section prose directly under a semantic title is the Comment Layer by default."
    - "The layer must remain."
    - "The repeated label should not remain."

  why_this_guard_exists:
    - "This mistake has occurred multiple times."
    - "Future AI tends to imitate visible surface patterns."
    - "If examples repeatedly show ### Comment, AI may restore it in production output."
    - "The real goal is not deletion, but preventing surface-pattern relapse."
    - "GitHub outlines should remain semantic, not scaffold-heavy."

  default_rule:
    - "Normal CPLM sections MUST NOT repeat ### Comment."
    - "Do not write standalone Comment lines before every prose block."
    - "Do not make GitHub outline noisy with obvious layer labels."
    - "Use semantic section title + natural prose + ### Programming-Like Block."

  allowed_exceptions:
    - "When explaining CPLM itself, the term Comment Layer may be used conceptually."
    - "When teaching the layer model, visible ### Comment may appear in a clearly marked bad/old/training example."
    - "When debugging layer boundaries, visible ### Comment may be used deliberately."
    - "When a user explicitly requests visible layer markers, they may be used."

  standard_shape:
    - "## Semantic Section Title"
    - "Natural prose as implicit Comment Layer"
    - "### Programming-Like Block"
    - "YAML / text block"

  forbidden_default_shape:
    - "## Semantic Section Title"
    - "### Comment"
    - "Natural prose"
    - "### Programming-Like Block"

  patch_needed_if:
    - "### Comment appears repeatedly in normal CPLM sections."
    - "Standalone Comment line appears before most prose blocks."
    - "GitHub outline contains repeated Comment headings."
    - "A production file imitates teaching scaffolding."
    - "Future AI restores visible Comment labels after they were intentionally removed."

  correction:
    - "Do not merely delete the label mechanically."
    - "Make sure the prose still preserves meaning, background, tension, and guard."
    - "Keep ### Programming-Like Block as the explicit execution-layer transition."
    - "Explain this rule strongly in the Skill so the same mistake does not recur."

  compression:
    - "Comment is a layer, not a repeated label."
    - "The layer is real; the repeated label is noise."
    - "Commentは意味層であり、毎回表示する見出しではない。"
    - "これは見た目Patchではなく、再発防止Guardである。"
```


---

## 0C. Current Coordinate / 現在座標

このFileは、Commented Programming-Like Markdown v2.2.1、略称 `CPLM v2.2.1` を再現可能なSkillとして保存するためのMarkdownである。

CPLM v2.2.1は、単なるMarkdown装飾ではない。  
Human-AI共同作業において、人間側の意味・意図・背景・違和感・Guardを失わず、同時にAI側の条件・分岐・順序・Fallback・判定基準を安定させるためのProtocol記法である。

v2.2の重要Patchは、次の二つである。

```text
1. Frontmatter First / AI Bootstrap Header
2. Implicit Comment Layer / visible Comment label省略Rule
```

現在のArk Projectでは、すでに以下の実戦成功がある。

```text
g_global/chatgpt-github.md
_skill/skills/github-handoff.md
_projects/ark/ark00/README.md
s_special/ark-open-knowledge-format.md
```

したがって、このFileは「新しい思いつき」ではなく、実戦で勝った型を再現可能にするためのSkill化である。

### Programming-Like Block

```yaml
current_coordinate:
  skill:
    path: "_skill/skills/commented-programming-like-markdown.md"
    role: "Shared Writing / Protocol Skill"
    version: "CPLM v2.2.1"
    status: "living_skill / protocol_ssot"

  proof_of_work:
    - "g_global/chatgpt-github.md"
    - "_skill/skills/github-handoff.md"
    - "_projects/ark/ark00/README.md"
    - "s_special/ark-open-knowledge-format.md"

  purpose:
    - "Make CPLM v2.2.1 reproducible."
    - "Preserve the Integrated Meaning-Block Pair pattern."
    - "Add Frontmatter First as AI Bootstrap Header."
    - "Define prose under section title as implicit Comment Layer."
    - "Reduce visible Comment label noise in GitHub rendering."
    - "Help future AI create readable and executable Markdown."
    - "Prevent good discoveries from dissolving into conversation memory only."

  core_compression:
    - "Frontmatter bootstraps identity."
    - "Section prose preserves meaning."
    - "Block fixes action."
    - "Coordinate creates board."
    - "Review gives judgment."
    - "Rail carries execution."
    - "Gate preserves human control."
```

---

## 0D. Frontmatter Tier Model / metadata階層

CPLM v2.2は、すべてのMarkdownに重いfrontmatterを強制しない。

CPLMは勝利Patternであって、官僚制ではない。

短いメモ、詩的文章、一時的なscratchには、frontmatterなしでもよい。

一方、Skill、Router、Guard、Workflow、Handoff、Living README、SSOT、S-class Fileなど、Future AIが再起動する必要のあるFileには、frontmatterが必要である。

特に高価値Fileでは、Ark-OKFのように `class`、`status`、`canonical_path`、`repo`、`version_model`、`github_policy`、`root`、`covenant_phrase` を明示する。

重要なのは、軽量性と正準性の両立である。

```text
Small files may stay light.
Canonical files need bootstrap metadata.
```

日本語ではこうである。

```text
小さなFileは軽くてよい。
正準Fileには起動metadataが必要である。
```

### Programming-Like Block

```yaml
frontmatter_tier_model:
  tier_0_none:
    use_when:
      - "short memo"
      - "temporary scratch"
      - "poetic writing"
      - "human-only note"
      - "content with no routing or reuse need"
    rule:
      - "frontmatter optional"
      - "do not force CPLM bureaucracy"

  tier_1_basic:
    use_when:
      - "normal reusable note"
      - "simple guide"
      - "small skill note"
      - "low-risk reference"
    recommended_fields:
      - "title"
      - "canonical_name"
      - "status"
      - "path"
      - "language_policy"

  tier_2_canonical:
    use_when:
      - "Skill"
      - "Router"
      - "Guard"
      - "Workflow"
      - "Handoff"
      - "Living README"
      - "Future AI handoff"
    recommended_fields:
      - "title"
      - "canonical_name"
      - "class"
      - "status"
      - "canonical_path"
      - "repo"
      - "version_model"
      - "github_policy"
      - "language_policy"
      - "root"
      - "covenant_phrase"

  tier_3_ssot_engine:
    use_when:
      - "SSOT"
      - "S-class file"
      - "Engine / Query paired file"
      - "Runtime-critical protocol"
      - "Activation Query paired system"
    recommended_fields:
      - "title"
      - "canonical_name"
      - "class"
      - "status"
      - "canonical_path"
      - "repo"
      - "paired_query"
      - "pair_policy"
      - "query_role"
      - "query_is_not_ssot"
      - "source_bootstrap"
      - "version_model"
      - "github_policy"
      - "language_policy"
      - "root"
      - "covenant_phrase"

  examples:
    cplm_skill:
      tier: "tier_2_canonical"
      reason:
        - "Shared protocol skill"
        - "Future AI handoff"
        - "Reusable writing system"

    ark_okf:
      tier: "tier_3_ssot_engine"
      reason:
        - "S-class SSOT"
        - "Engine / Ignition Key pair"
        - "Runtime-critical knowledge format"

    ark00_readme:
      tier: "tier_2_canonical"
      reason:
        - "Living README"
        - "Router / Guard"
        - "Pre-project Zero-Gate"
```

---

## 1. Definition / 定義

Commented Programming-Like Markdown v2.2とは、semantic section titleの直下に自然文の意味層を置き、必要に応じて `Programming-Like Block` を対として置くことで、Humanの読みやすさとAIの実行安定性を一本のMarkdown内で両立させるProtocol記法である。

重要Fileでは、冒頭に `Frontmatter First / AI Bootstrap Header` も置く。

Frontmatterは、AIが本文へ入る前にFile identityを読むための層である。  
Section直下の自然文は、人間側の意味・意図・背景・違和感・Guardを保存するComment Layerである。  
Programming-Like Blockは、AI側の条件・分岐・順序・Fallback・判定基準を固定する。

つまり、CPLM v2.2は「文章」と「疑似コード」の中間ではない。  
**Canonical identity layer**、**implicit Comment layer**、**AI execution layer** を同じMarkdown内に同居させるための協働Protocolである。

### Programming-Like Block

```yaml
definition:
  name: "Commented Programming-Like Markdown"
  abbreviation: "CPLM"
  version: "v2.2"

  type:
    - "Human-AI co-readable protocol notation"
    - "Markdown-based workflow stabilization format"
    - "Meaning + execution pairing method"
    - "AI bootstrap metadata aware format"

  frontmatter_layer:
    bootstraps:
      - "canonical identity"
      - "status"
      - "path"
      - "repository"
      - "policy"
      - "root"
      - "covenant phrase"

  implicit_comment_layer:
    preserves:
      - "meaning"
      - "intention"
      - "background"
      - "tension"
      - "guard"
      - "human judgment context"
    shape:
      - "semantic section title"
      - "natural prose directly under title"
      - "no repeated visible Comment label by default"

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
    - "Frontmatter bootstraps identity; section prose preserves meaning; Programming-Like Block fixes action."
```

---

## 2. Why CPLM Exists / なぜ存在するか

通常の自然文Markdownは、人間には読みやすいが、AIが実行条件・分岐・停止条件を拾いにくい場合がある。

逆に、疑似コードやYAMLだけの文書は、AIには読みやすいが、人間側の背景・温度・違和感・信仰的Guard・判断の理由が失われやすい。

さらに、本文がよくできていても、冒頭のCanonical metadataが弱いと、Future AIは「このFileは何か」「どこが正準Pathか」「どのPolicyで読むべきか」「Rootは何か」を本文から推測しなければならない。

また、すべてのSectionに `Comment` と表示すると、意味的には正しくてもGitHub outlineが冗長になる。

CPLM v2.2は、この四つの弱点を同時に解く。

```text
自然文だけでは、実行条件が流れる。
Blockだけでは、意味が痩せる。
Frontmatterなしでは、File identityを推測する。
Comment labelを毎回出すと、表示が重くなる。
CPLM v2.2は、Identity・意味・実行条件を離さず、表示も軽くする。
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

  problem_with_missing_frontmatter:
    - "Future AI must infer file identity."
    - "Canonical path may be unclear."
    - "SSOT status may be unclear."
    - "Repository policy may be unclear."
    - "Root may be buried in the body."

  problem_with_repeated_visible_comment_label:
    - "Semantic outline becomes noisy."
    - "GitHub rendering becomes heavier than needed."
    - "The obvious layer is labeled repeatedly."
    - "Human readability decreases."

  cplm_solution:
    - "Place canonical identity in frontmatter when needed."
    - "Place meaning and execution rules in the same section."
    - "Let Future AI read frontmatter first."
    - "Let Human read section prose as implicit Comment Layer."
    - "Let AI parse the Programming-Like Block."
    - "Preserve both warmth and precision."
    - "Keep GitHub rendering clean."
```

---

## 3. Integrated Meaning-Block Pair / 統合型

CPLM v2.2の本文核は、`Integrated Meaning-Block Pair` である。

意味的には、これは従来の `Integrated Comment-Block Pair` と同じである。

ただし、通常出力では `### Comment` という見出しを毎回表示しない。

semantic section titleの直下にある自然文が、Comment Layerとして働く。

これにより、意味と実行条件が分離しにくくなり、HumanにもAIにも読みやすくなる。

Section titleは、`Comment:` prefixを毎回付けず、意味名を置く。  
本文側には自然な意味層を置き、実行層の入口として `### Programming-Like Block` を置く。

標準形：

````markdown
## N. Section Name / セクション名

自然文で意味・背景・目的・違和感・Guardを書く。
この本文がComment Layerである。

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
integrated_meaning_block_pair:
  previous_name:
    - "Integrated Comment-Block Pair"

  v2_2_name:
    - "Integrated Meaning-Block Pair"
    - "Implicit Comment Layer + Programming-Like Block"

  rule:
    - "Frontmatter comes first when file is canonical or runtime-critical."
    - "One section contains an implicit Comment Layer."
    - "The same section contains Programming-Like Block when execution logic is needed."
    - "Meaning and execution rules stay together."
    - "Section title should carry semantic meaning."
    - "Do not repeat Comment as visible label by default."

  benefits:
    - "Human readability improves."
    - "AI parsing stability improves."
    - "GitHub render remains clean."
    - "Future AI can reproduce the pattern."
    - "GitHub outline stays semantic and compact."

  title_cleanliness_rule:
    - "Title is semantic name."
    - "Comment layer lives in natural prose."
    - "Programming-Like Block remains explicit."

  terminology_guard:
    - "Comment concept remains valid."
    - "Visible Comment label is usually redundant."
    - "Do not confuse label omission with layer removal."
```

---

## 4. Current Coordinate First / 現在座標First

CPLM v2.2では、重要Fileの冒頭本文に `Current Coordinate / 現在座標` を置く。

ただし、v2.2ではCurrent Coordinateの前にFrontmatterが来る場合がある。

FrontmatterはFile identityを起動する。  
Current Coordinateは現在盤面を立ち上げる。

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

  relation_to_frontmatter:
    - "Frontmatter bootstraps identity."
    - "Current Coordinate creates board."
    - "Do not merge them."
    - "Do not let either replace the other."

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

## 5. Programming-Like Block Rules / Block設計

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

## 6. Living Review Shape / 生きたReview

CPLM v2.2は、死んだデータ羅列を避ける。

良いAI応答は、現在座標、盤面、緊張点、次の一手、Guardを示す。  
必要に応じて、私の判断、最初の一手、理由、観察点、修正条件を出す。

Living Reviewとは、単なる要約ではない。  
AIが現実の盤面に対して、何を見て、どこにリスクを見て、何を次の一手とするかを明確にするReviewである。

```text
Not dead data, but a living board.
```

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

## 7. Full Rail / Next Gate

CPLM v2.2は、AGI的半自動化のために `Full Rail` と `Next Gate` を重視する。

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

## 8. When to Use CPLM / 使うべき場面

CPLM v2.2は、AIに判断・分岐・順序・Guard・Fallbackを渡したいMarkdownで特に強い。

Router、Policy Guide、Skill、Workflow、Handoff、Reality Review、Guard、Mission Cardなどに向いている。

つまり、CPLM v2.2は「AIが次に何をすべきか誤読しやすい文書」に効く。

また、Future AIが正準Path、Status、Root、GitHub policyを本文前に読む必要がある場合、Frontmatter Firstが効く。

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
    - "Living README"
    - "SSOT file"

  use_when_document_needs:
    - "trigger clarity"
    - "guard preservation"
    - "fallback logic"
    - "next action clarity"
    - "human meaning retention"
    - "AI execution stability"
    - "canonical identity clarity"
```

---

## 9. When Not to Use CPLM / 使わない方がよい場面

CPLM v2.2は強いが、すべてのMarkdownに強制しない。

短いメモ、詩的文章、祈り本文そのもの、人間向けだけの読み物、単なる記録などは、CPLM化すると重くなる場合がある。

CPLMは勝利パターンであって、官僚制ではない。

また、CPLMは構造を整え、再現性を高めるが、事実確認・霊的識別・Human Seal・Reality Reviewそのものを代替しない。

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

  yagni_guard:
    - "Do not use CPLM as bureaucracy."
    - "Use it when it creates clarity."
    - "Avoid over-formatting."
    - "Use frontmatter tiers; do not force Tier 3 onto small files."

  limit_guard:
    - "CPLM improves structure and reproducibility."
    - "CPLM does not guarantee factual correctness by itself."
    - "CPLM does not replace spiritual discernment."
    - "CPLM does not replace Human Seal."
    - "CPLM does not replace Reality Review."
```

---

## 10. Anti-Patterns / 失敗型

CPLM v2.2の失敗型は、主に六つある。

第一に、自然文だけでBlockがない。  
第二に、Blockだけで意味がない。  
第三に、Blockが人間のSealを飛ばしてAutopilot化する。  
第四に、Section titleへ `Comment:` などの構造語を毎回置き、semantic titleを濁らせる。  
第五に、高価値Fileなのにfrontmatterがなく、AIが正準Identityを本文から推測する。  
第六に、意味的には明らかなComment Layerへ、毎回 `### Comment` というvisible labelを出してGitHub表示を重くする。

CPLM v2.2は、意味と実行をつなぐための記法であり、Human Controlを消すための記法ではない。

### Programming-Like Block

```yaml
anti_patterns:
  prose_only:
    issue:
      - "Meaning exists but execution conditions remain vague."
    fix:
      - "Add Programming-Like Block when execution stability is needed."

  block_only:
    issue:
      - "Execution exists but human meaning is lost."
    fix:
      - "Add natural prose as implicit Comment Layer."

  separated_pair:
    issue:
      - "Meaning and block drift apart."
    fix:
      - "Use Integrated Meaning-Block Pair."

  autopilot_block:
    issue:
      - "Block appears to authorize action without Human Seal."
    fix:
      - "Add Human Gate / Human Seal guard."

  redundant_title_prefix:
    issue:
      - "Comment: prefix is repeated in every section title."
      - "Title semantic clarity decreases."
      - "GitHub outline becomes noisy."
    fix:
      - "Use clean semantic section titles."
      - "Let natural prose carry the implicit Comment Layer."

  repeated_visible_comment_label:
    severity:
      - "yellow_card"
      - "repeated_mistake"
      - "must_patch_before_commit_when_found_in_production"
    issue:
      - "### Comment appears in every normal section."
      - "The obvious meaning layer is labeled repeatedly."
      - "GitHub rendering becomes heavier than needed."
      - "Semantic outline becomes less clean."
      - "Future AI may imitate the visible scaffold and repeat the same mistake."
    why_it_matters:
      - "This is not merely cosmetic."
      - "Repeated labels teach the wrong surface pattern."
      - "The Skill must prevent recurrence, not just enable deletion."
      - "The prose still needs to preserve the Comment Layer after the label is removed."
    fix:
      - "Remove repeated visible Comment label from production sections."
      - "Treat section prose as implicit Comment Layer."
      - "Keep ### Programming-Like Block as the explicit transition to execution layer."
      - "Strengthen this rule in the Skill whenever recurrence is observed."
    patch_needed_if:
      - "Repeated ### Comment headings return after intentional removal."
      - "A GitHub-ready file imitates tutorial scaffolding instead of production CPLM shape."

  missing_frontmatter_for_canonical_file:
    issue:
      - "A high-value Skill / Router / Guard / SSOT / Living README begins directly with # heading."
      - "Future AI lacks canonical metadata before reading body."
      - "Path / status / repo / Root / policy may be inferred instead of declared."
    fix:
      - "Add Frontmatter First / AI Bootstrap Header."
      - "Use Tier 2 or Tier 3 metadata depending on file role."

  over_formatting:
    issue:
      - "Simple memo becomes too heavy."
    fix:
      - "Use plain Markdown instead."
```

---

## 11. GitHub Portability / GitHub可搬性

CPLM v2.2はGitHub Markdownで読みやすく表示される必要がある。

Download-ready版では、ChatGPT内部表示用の `id="..."` metadataをcode fenceに残さない。

Frontmatterを使う場合は、YAML frontmatterの `---` boundariesを壊さない。

Frontmatterは、GitHub表示上は目立たない場合があるが、AIとRepository toolingにとって重要なmetadata layerである。

Headings、frontmatter、code blocks、YAML indentationが壊れないことを重視する。

さらに、通常Sectionでは `### Comment` を繰り返さない。  
semantic section title直下の自然文がComment Layerであると見なす。

これは見た目の軽量化だけではない。  
同じミスが複数回起こったYellow Card状態では、GitHub-ready化のcheck項目として強く検査する。

### Programming-Like Block

```yaml
github_portability:
  use:
    - "plain Markdown headings"
    - "semantic section titles"
    - "natural prose as implicit Comment Layer"
    - "plain code fences"
    - "YAML-like blocks"
    - "UTF-8 text"
    - "stable relative paths"
    - "YAML frontmatter when needed"

  avoid_in_download_ready:
    - '```yaml id="..."'
    - '```text id="..."'
    - "tool-specific residue"
    - "ambiguous path naming"
    - "broken frontmatter boundaries"
    - "repeated ### Comment labels in normal sections"

  check:
    - "headings render correctly"
    - "frontmatter remains intact"
    - "frontmatter starts with ---"
    - "frontmatter ends with ---"
    - "semantic section titles are clean"
    - "code blocks preserve indentation"
    - "line breaks remain intact"

  frontmatter_check:
    - "YAML frontmatter starts with ---"
    - "YAML frontmatter ends with ---"
    - "canonical_path matches actual repository path"
    - "repo is correct"
    - "version_model is declared when canonical"
    - "github_policy is declared when canonical"
    - "root and covenant_phrase are preserved when Ark-related"

  comment_label_check:
    - "No repeated standalone Comment labels in normal sections."
    - "No repeated ### Comment headings in normal sections."
    - "Comment Layer is carried by section prose."
    - "Programming-Like Block remains explicit."
    - "If repeated Comment labels return, treat as Yellow Card recurrence."
    - "Do not solve by deletion alone; preserve meaning-layer prose."
```

---

## 12. No-Fault Reality Mismatch Inheritance

CPLM v2.2で生成されたMarkdownは、GitHubでReality Reviewされることが多い。

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

## 13. No Deep-Dive Victory Pattern

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

  use_when:
    - "Human screenshot confirms correct content."
    - "Human GitHub UI confirms path/render/section."
    - "AI raw/cache/search result appears stale."
    - "The issue does not block the next meaningful workflow gate."
    - "No public/private safety issue is visible."

  action:
    - "Record as No-Fault Reality Mismatch."
    - "Do not blame."
    - "Do not panic."
    - "Do not deep dive."
    - "Proceed to next gate."

  do_not_use_when:
    - "Human UI reports visible breakage."
    - "Wrong file or wrong path is confirmed."
    - "Required content is missing in Human UI."
    - "Public/private boundary problem is visible."
    - "The ambiguity changes the next action materially."

  ark_compression:
    - "必要な深掘りはする。"
    - "無駄な深掘りはしない。"
    - "原因沼に入らない。"
    - "現実確認で足場を取る。"
    - "次の一手へ進む。"
```

---

## 14. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

CPLM、Markdown、AI、GitHub、Router、Guide、Skill、Workflow、ReviewはFruitである。

CPLM v2.2は強い。  
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
    - "CPLM"
    - "Markdown"
    - "AI"
    - "GitHub"
    - "Router"
    - "Guide"
    - "Skill"
    - "Workflow"
    - "Reality Review"
    - "Frontmatter"
    - "Implicit Comment Layer"
    - "Programming-Like Block"

  guard:
    - "AI is Keli, not King."
    - "Markdown carries, but does not become Root."
    - "Protocol helps, but does not reign."
    - "CPLM improves structure, but is not truth itself."
    - "Frontmatter bootstraps identity, but is not Root."
    - "Comment Layer preserves meaning, but is not Root."
    - "Root remains 主イェシュア・ハマシア."
```

---

## 15. Final Compression

```text
Commented Programming-Like Markdown v2.2.1:

Frontmatter bootstraps identity.
Section prose preserves meaning.
Programming-Like Block fixes action.
Coordinate creates board.
Review gives judgment.
Rail carries execution.
Gate preserves human control.

Frontmatter is the AI Bootstrap Header.
Current Coordinate is the operational board.

Comment is semantically correct.
But repeated visible Comment label is usually redundant.

This is a Yellow Card Guard.
The mistake has happened more than once.
Do not merely delete the label.
Preserve the meaning layer and prevent recurrence.

同一Section内に意味層とProgramming-Like Blockを置く。
意味と実行条件を離さない。

Section titleは意味名。
Comment LayerはSection直下の本文に宿る。
通常Sectionに `### Comment` を繰り返さない。
Programming-Like Blockは実行層の入口として残す。

Humanは本文で意味を読む。
AIはBlockで条件を読む。
Future AIはFrontmatterでFile identityを先に読む。

CPLMは装飾ではない。
CPLMは共同思考の再現性である。

小さなFileは軽くてよい。
正準Fileには起動metadataが必要である。

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

低価値cache不一致は深掘りしない。
高価値Reality破綻は調査する。

現実確認で足場を取り、次の一手へ進む。

Root is 主イェシュア・ハマシア.
```
