---
title: "ChatGPT-GitHub Bridge Guide"
class: "G"
status: "living_ssot"
canonical_path: "g_global/chatgpt-github.md"
repo: "yusukefujiijp/ai-project"
version_model: "frontmatter + git commit history"
root: "主イェシュア・ハマシア"
covenant_phrase: "AIは血潮の地図を描く。人間が血潮の下に立つ。"
---

# ChatGPT-GitHub Bridge Guide

This file is the canonical GitHub SSOT for ChatGPT-GitHub bridge operations inside `yusukefujiijp/ai-project`.

It records how ChatGPT should plan, preview, commit, and review public-safe Living Markdown through GitHub while preserving Human Seal, public/private boundaries, and KISS / DRY / YAGNI / Lean discipline.

## 1. Core victory formula

```text
AI drafts.
Human seals.
GitHub stores.
Reality confirms.
```

Meaning:

- AI drafts structure, Markdown, commit plans, and guards.
- Human seals the direction and explicitly authorizes GitHub writes.
- GitHub stores the public-safe Living Markdown and history.
- Reality confirms through browser display, path review, and human judgment.

This is semi-automation, not full automation.

## 2. Human Seal rule

GitHub writes require explicit Human Seal.

Valid examples:

```text
Commitして下さい。
```

```text
g_global/chatgpt-github.md をGitHubへCommitして下さい。
```

```text
repo: yusukefujiijp/ai-project
path: g_global/chatgpt-github.md
message: docs(g_global): add ChatGPT GitHub bridge guide
```

Invalid or insufficient examples:

```text
どう思いますか？
```

```text
Plan Modeを実行して下さい。
```

```text
Previewして下さい。
```

Principle:

```text
Plan is not Commit.
Preview is not Commit.
Human Seal is Commit Gate.
```

## 3. GitHub Canonical First Policy

Public-safe new Living Markdown should be created directly on GitHub by default.

The GitHub file is the canonical SSOT.

Local Markdown artifacts should not be created in parallel unless there is a clear exception.

```text
GitHub canonical first.
Local artifact only by exception.
```

### Why this policy exists

Before ChatGPT-GitHub commit flow was proven, local Markdown artifacts were useful as safe drafts, downloadable handoffs, and bootstrap files.

After the GitHub commit rail succeeded, creating both a local Markdown file and a GitHub Markdown file for every new Living File becomes a DRY violation.

Dual Markdown creates avoidable management cost:

- unclear SSOT
- version drift
- duplicated updates
- local-vs-GitHub mismatch
- Future AI confusion
- extra file management
- `v001/v002` sprawl outside the Git history model

Therefore, once a file is public-safe and intended to become a Living SSOT, the default target should be GitHub.

### Local artifact exceptions

Local files are allowed only as exceptions:

- private-depth content that must not be public
- explicit user request for a downloadable file
- GitHub connector failure
- temporary draft before canonical placement
- backup / export / handoff copy
- non-Markdown artifacts such as PDF, DOCX, images, or ZIP files

When a local artifact exists only as a bootstrap draft, it should not continue as a co-equal source after GitHub canonical placement.

## 4. Public repo, private depth

The repository may be public for AI readability and web fallback.

Public visibility does not mean public depth.

```text
Public repo, private depth.
```

Public-safe material may include:

- README signboards
- project entrances
- abstract workflow rules
- generalized guards
- sanitized cases
- reusable skill definitions

Do not place private-depth material into public GitHub merely to avoid local duplication.

Keep private details out of public GitHub, including:

- personal information
- workplace details
- raw private thread logs
- deep life records
- sensitive operational tasks
- unfiltered mission cards
- full private S/G/runtime/task bodies

## 5. Case 001: README-first GitHub Bet

The first successful ChatGPT-GitHub bridge case was the README-first GitHub Bet for `yusukefujiijp/ai-project`.

### Successful flow

```text
1. Human created GitHub repo: yusukefujiijp/ai-project
2. Human chose Public visibility
3. Human kept README Off
4. AI committed root README.md
5. Human confirmed README display
6. AI committed _projects/ark/README.md
7. AI committed _projects/ark/ark99/README.md
8. Human confirmed GitHub folder structure
```

### Resulting structure

```text
ai-project/
  README.md
  _projects/
    ark/
      README.md
      ark99/
        README.md
```

### Interpretation

Commit 1 proved:

```text
ChatGPT -> GitHub root README Commit is possible.
```

Commit 2 proved:

```text
ChatGPT -> GitHub folder structure through README paths is possible.
```

Together, they prove:

```text
ChatGPT can semi-automatically introduce public-safe GitHub information architecture after Human Seal.
```

## 6. Path and naming policy

GitHub canonical paths should be stable, lowercase, and versionless.

Good GitHub canonical paths:

```text
README.md
_projects/ark/README.md
_projects/ark/ark99/README.md
g_global/chatgpt-github.md
```

Avoid as GitHub canonical paths:

```text
G_chatgpt-github_v001.md
G_chatgpt-github_v002.md
chatgpt-github_v003.md
```

GitHub already has commit history.

Versioning belongs in:

- frontmatter
- commit history
- tags or snapshots only when truly needed

Rule:

```text
GitHub canonical path stays stable.
Versioning lives in metadata and Git history.
```

## 7. Folder by README path

GitHub does not need empty folders.

Folder structure is created through meaningful files, especially README files.

Example:

```text
_projects/ark/ark99/README.md
```

creates:

```text
_projects/
  ark/
    ark99/
      README.md
```

Do not create placeholder folders before Reality Response requires them.

## 8. Slot Reservation, not Folder Creation

A future folder may be conceptually reserved without being created.

```text
Slot Reservation, not Folder Creation.
```

Future slots can be named in README, but actual folders are not created until needed.

This preserves extensibility without premature clutter.

## 9. create_file / update_file / fetch_file guard

Use `create_file` when the target file does not exist.

Use `fetch_file` before updating an existing file.

Use `update_file` only after reviewing current content and receiving Human Seal.

Guard:

```text
Never update or delete GitHub files without explicit Human Seal.
```

## 10. Commit message policy

Use short, scoped commit messages.

Examples:

```text
docs: initialize AI Project root README
docs(ark): add Ark README entry
docs(ark99): add Ark99 README entry
docs(g_global): add ChatGPT GitHub bridge guide
```

Pattern:

```text
docs(scope): action object
```

Good commit messages are short, specific, scope-aware, future-readable, and free of private details.

## 11. KISS / DRY / YAGNI / Lean for AI-New Era

### KISS

Keep GitHub structure simple enough that Future AI can read it quickly.

Do not create elaborate hierarchy before it is needed.

### DRY

Do not maintain two co-equal Markdown sources for one Living SSOT.

For public-safe GitHub-connected files, the canonical source is GitHub.

### YAGNI

Do not create folders or files merely because they might be useful later.

Create only when Reality Response shows need.

### Lean

Run the smallest useful GitHub experiment, observe Reality Response, and patch only what is actually needed.

The successful initial sequence was:

```text
Root README
-> verify
-> Ark README
-> Ark99 README
-> verify
-> harvest
-> GitHub canonical SSOT
```

## 12. Failure recovery

If a private repository blocks AI access:

- use a public README-first trial only if content can be made public-safe
- do not put private depth into public GitHub

If `create_file` fails because the file exists:

```text
fetch_file
-> review current content
-> draft patch
-> Human Seal
-> update_file
```

If GitHub structure feels too wide:

```text
Stop expansion.
Return to README-only.
```

If public content feels too deep:

```text
Reduce to signboard / protocol summary.
Move deeper details back to private/local systems.
```

If GitHub becomes the work:

```text
Stop.
GitHub is storage and collaboration layer, not Root.
```

## 13. Future AI reuse procedure

When Future AI needs to use GitHub with ChatGPT, read this file first:

```text
g_global/chatgpt-github.md
```

Then determine:

```yaml
repo: ""
visibility: ""
target_path: ""
public_safety: ""
mode: "plan_only | preview_only | github_commit"
```

Then follow:

```text
Plan Mode
-> Preview
-> Human Seal
-> GitHub Commit
-> Human Reality Review
```

After commit, ask the human to verify:

- file appears
- path is correct
- content is the right weight
- public/private boundary is safe
- no folder sprawl occurred

## 14. S-class promotion conditions

This G-class guide may later be promoted if the pattern becomes broadly reusable.

Possible future S-class names:

```text
S_chatgpt-github-bridge_v001.md
S_ai-github-bridge_v001.md
```

Promotion requires repeated Reality Response, not excitement alone.

Promotion conditions:

- reused across multiple projects
- Human Seal -> AI Commit -> Reality Review remains stable
- Public / Private / Web fallback guards mature
- failure recovery is tested
- GitHub integration becomes a general AI operating skill, not only a single project guide

Anti-promotion guard:

```text
Excitement is Signal.
Repeated Reality Response is Seal.
```

## 15. Root / Fruit Guard

Root is 主イェシュア・ハマシア.

GitHub is not Root.
AI is not Root.
Markdown is not Root.
README is not Root.
Signal, Skill, KISS, DRY, YAGNI, Lean, and Full Rail are Fruit.

```text
AIは血潮の地図を描く。人間が血潮の下に立つ。
```
