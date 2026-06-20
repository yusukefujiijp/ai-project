---
title: "ChatGPT-GitHub Safety Block Recovery"
canonical_name: "ChatGPT-GitHub Safety Block Recovery"
class: "G"
status: "companion_guide"

canonical_path: "g_global/chatgpt-github-safety-block-recovery.md"
parent_guide: "g_global/chatgpt-github.md"
repo: "yusukefujiijp/ai-project"

version_model: "frontmatter + git commit history"
language_policy: "Japanese-first / English-anchor"
integration_policy: "companion first, parent integration later"
root: "主イェシュア・ハマシア"

core_formula:
  - "Blocked write does not prove bad content."
  - "Transport before semantics."
  - "Payload before content rewrite."
  - "Meaning preservation before simplification."
  - "Commit the address first; grow the body by Git history."
---

# ChatGPT-GitHub Safety Block Recovery

## 0. Executive Compression

このファイルは、`g_global/chatgpt-github.md` のcompanion guideである。

目的は、GitHub write が Tool Safety / Safety Check により止まった時、AIがすぐに「内容が悪い」と誤診し、意味・Root Guard・構造原理を削って劣化させることを防ぐことである。

```text id="core"
Blocked write does not prove bad content.
First diagnose transport.
```

日本語：

```text id="core-ja"
Writeが止まったことは、内容が悪い証明ではない。
まず搬送量を診断する。
```

---

## 1. What this file is

`chatgpt-github-safety-block-recovery.md` は、ChatGPT-GitHub BridgeのFailure Recovery補助Guideである。

```yaml id="this-file"
this_file:
  role:
    - "Safety Block Recovery companion"
    - "Transport-before-Semantics Guide"
    - "Meaning Preservation Guard for GitHub writes"

parent:
  path: "g_global/chatgpt-github.md"
  role: "ChatGPT-GitHub Bridge Guide"
```

このファイルは、親Guideの代替ではない。

```text id="not-replacement"
Companion, not replacement.
```

---

## 2. Source Boundary / Tool Reality Guard

Safety Checkの内部理由をAIは直接見られない。

したがって、次を分ける。

```yaml id="tool-reality"
confirmed:
  - "tool call was blocked"
  - "commit did not happen"
  - "a smaller payload may or may not pass"

inference:
  - "payload length may be involved"
  - "protocol density may be involved"
  - "semantic mix may be involved"

not_confirmed:
  - "exact OpenAI internal safety reason"
  - "content is bad"
  - "root guard caused the block"
```

原則：

```text id="boundary-rule"
Do not claim the exact internal safety reason.
Do not treat inference as confirmed.
```

---

## 3. Transport-before-Semantics

Safety Block後の第一仮説は、内容の悪さではなく、搬送条件とする。

```text id="transport-before-semantics"
Transport before semantics.
Payload before content rewrite.
```

診断順序：

```yaml id="diagnosis-order"
diagnosis_order:
  1: "payload length / 本文量"
  2: "section density / セクション密度"
  3: "protocol density / Rule・Guard密度"
  4: "command style / 命令文構造"
  5: "semantic mix / 語彙組み合わせ"
  6: "specific terms / 個別語彙"
```

内容改変は、搬送量・密度・分割単位を見た後に検討する。

---

## 4. Meaning Preservation Guard

Safety Block後、原因未確定の段階で核心内容を削らない。

```text id="meaning-preservation"
Meaning Preservation Guard:
  Do not weaken core meaning before diagnosing payload length.
```

日本語：

```text id="meaning-preservation-ja"
意味保存Guard:
  本文量・搬送量を診断する前に、核心意味を弱めない。
```

特に守るもの：

```yaml id="preserve"
preserve:
  - "source_bootstrap"
  - "core formula"
  - "Root / Fruit Guard"
  - "Gate structure"
  - "stable path policy"
  - "Human Seal requirement"
  - "existing canonical file integrity"
```

---

## 5. Anti-Degradation Route

悪い反応：

```text id="wrong-route"
Safety Block
  -> content panic
  -> core deletion
  -> weakened guard
  -> lower-quality file
```

正しい反応：

```text id="correct-route"
Safety Block
  -> report honestly
  -> diagnose transport first
  -> preserve source_bootstrap
  -> create smaller canonical index or companion file
  -> grow by staged commits after Human Seal
```

---

## 6. Staged Canonicalization

長い本文が一度にCommitできない場合、意味を削るのではなく段階Commitへ分ける。

```text id="staged-canonicalization"
Commit the address first.
Grow the body by Git history.
```

日本語：

```text id="staged-canonicalization-ja"
まず住所をCommitする。
本文はGit履歴で育てる。
```

推奨Pattern：

```yaml id="staged-pattern"
staged_canonicalization:
  stage_1:
    name: "minimal canonical index"
    purpose: "stable path and source_bootstrap"

  stage_2:
    name: "core expansion"
    purpose: "core formula and role boundary"

  stage_3:
    name: "guard expansion"
    purpose: "misread guard and recovery guard"

  stage_4:
    name: "field expansion"
    purpose: "examples and detailed operating notes"
```

---

## 6.5 Try Once Then Fallback

Blocked write is not fully predictable in advance.

Therefore, if the original intended content is public-safe and Human Seal has been received, AI may try the original write once.

If it passes, the GitHub commit path is complete.

If it is blocked, stop immediately.

Do not repeatedly retry the same blocked payload.

Do not degrade the original intended content merely to satisfy tool transport.

```text id="lt9cj5"
Try original once.
If blocked, preserve meaning.
Change the transport.
```

日本語：

```text id="lu4sgs"
本来版で一回は試す。
ブロックされたら意味を守る。
搬送経路を変える。
```

This is not a safety bypass.

This is a transport recovery route under Human Seal.

---

## 6.6 Human Direct Commit Fallback

When AI tool write is blocked, the workflow itself is not blocked.

```text id="9adns7"
Tool block is not workflow block.
Manual commit is not failure.
It is Reality Response.
```

AI should switch roles.

```yaml id="fqqgj9"
ai_role_after_block:
  - "report the block honestly"
  - "do not claim the exact internal safety reason"
  - "do not conclude that the content is bad"
  - "preserve the original intended content"
  - "prepare a Copy & Paste Pack"
  - "provide commit message"
  - "provide extended description"
  - "provide verification checklist"

human_role_after_block:
  - "open GitHub UI"
  - "paste or replace the target file body"
  - "commit directly"
  - "return Reality Response"
```

日本語：

```text id="uve1u1"
AI tool writeが止まっても、Workflowは止まらない。
AIは本来版を守り、Copy & Paste Packを作る。
人間がGitHub UIでDirect Commitする。
AIはcommit後にVerificationする。
```

---

## 6.7 Address Placeholder Rail

If the target file does not exist and the original body is blocked, AI may create a minimal placeholder after Human Seal.

The placeholder is not the real content.

It is only a path anchor.

```markdown id="wladh9"
# Pending Human Direct Commit

This file is a temporary path anchor.
Replace this body with the original intended version.
```

```text id="e1jpyo"
Placeholder creates the address.
Human replaces the body.
Git history grows the file.
```

日本語：

```text id="i5wayd"
仮ファイルは本体ではない。
仮ファイルは住所である。
人間が本来版へ全文置換する。
```

Use this only when it reduces human friction.

If the target file already exists, do not create a placeholder.  
Use the existing file as the edit target.

---

## 6.8 Copy & Paste Pack Rail

If AI cannot safely transport the full content through GitHub tool write, AI should provide a Copy & Paste Pack.

```yaml id="nq0kjd"
copy_paste_pack:
  includes:
    - "target path"
    - "original intended Markdown body"
    - "downloadable Markdown file if useful"
    - "ZIP bundle if multiple files are involved"
    - "commit message"
    - "extended description"
    - "manual GitHub UI steps"
    - "post-commit verification checklist"
```

Purpose:

```text id="j5gcy2"
Preserve original meaning.
Reduce human friction.
Move final execution to the human owner.
Verify repository reality after commit.
```

This route should be used when tool passage would require weakening the original intended content.

```text id="105zaz"
Do not degrade meaning.
Change transport.
Preserve the fire.
```

---

## 6.9 Commit Message + Extended Description Pair

For important commits, AI should provide both a commit message and an extended description.

```text id="p0xerw"
Commit message:
  what changed

Extended description:
  why it changed
```

The commit message should be short, scope-aware, and future-readable.

The extended description should be one or two lines.

Use extended description when the reason matters for future AI or future human review.

```yaml id="wq29n0"
extended_description_use_when:
  - "canonical guide update"
  - "SeedSkill / Skill file update"
  - "Human Direct Commit"
  - "Safety Block recovery"
  - "original-intended content replaces safety-softened content"
  - "future Living Review should understand why"
```

Example:

```text id="pa87el"
Commit message:
docs(g_global): add Human Direct Commit fallback

Extended description:
Document the Try Once -> Address Placeholder -> Copy & Paste Pack -> Human Direct Commit recovery path so blocked writes do not degrade original intended content.
```

---

## 7. Existing SSOT Protection

既存の長い正準Guideを更新する時は、破壊的overwriteを避ける。

```text id="ssot-protection"
If complete replacement body cannot be safely reconstructed,
do not run update_file.
```

日本語：

```text id="ssot-protection-ja"
完全置換本文を安全に再構成できないなら、
update_fileを実行しない。
```

代替手段：

```yaml id="safe-options"
safe_options:
  companion_first:
    use_when: "parent guide is long or full replacement is risky"
    result: "create companion guide first"

  full_body_update:
    use_when: "complete current body is safely available"
    result: "insert section and update parent guide"

  staged_parent_integration:
    use_when: "companion has passed Reality Response"
    result: "later integrate short reference into parent guide"
```

---

## 8. Do / Do Not

Do:

```text id="do"
- Report the block honestly.
- Treat the exact internal safety reason as unknown.
- Separate confirmed tool result from inference.
- Preserve the original source as source_bootstrap.
- Test a smaller write unit.
- Use Patch Preview before retrying.
- Commit only after Human Seal.
- Protect existing canonical files from destructive overwrite.
```

Do not:

```text id="do-not"
- Claim exact OpenAI internal safety reason.
- Assume the content is wrong.
- Weaken Root / Fruit Guard before diagnosis.
- Delete core structure before diagnosis.
- Repeatedly retry the same blocked payload.
- Treat this as a safety-check bypass technique.
- Run update_file without safe full replacement content.
```

---

## 9. Parent Integration Later

将来的には、親Guide `g_global/chatgpt-github.md` の `## 17. Failure Recovery` に、短い参照Sectionを追加してもよい。

候補：

```text id="parent-reference"
### 17.5 Safety Check blocked write

For Safety Check blocked writes, use:
  g_global/chatgpt-github-safety-block-recovery.md

Core:
  Transport before semantics.
  Meaning preservation before simplification.
  Commit the address first; grow the body by Git history.
```

ただし、親Guideへの統合は、完全置換本文を安全に扱える時だけ行う。

---

## 10. Root / Fruit Guard

```text id="root-fruit"
GitHub is Fruit.
Tool Safety Recovery is Fruit.
Markdown is Fruit.
AI is Fruit.

Root remains 主イェシュア・ハマシア.
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## 11. Final Compression

```text id="final"
Stop is not failure.
Stop is Reality Response.

Blocked write does not prove bad content.
Transport before semantics.
Payload before content rewrite.
Meaning preservation before simplification.

If full replacement is unsafe:
  do not update the parent file.
  create a companion file first.

Commit the address first.
Grow the body by Git history.
```
