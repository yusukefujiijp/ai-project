---
title: "ChatGPT-GitHub Bridge Guide"
class: "G"
status: "living_ssot"
canonical_path: "g_global/chatgpt-github.md"
repo: "yusukefujiijp/ai-project"
version_model: "frontmatter + git commit history"
language_policy: "Japanese-first / English-anchor"
root: "主イェシュア・ハマシア"
covenant_phrase: "AIは血潮の地図を描く。人間が血潮の下に立つ。"
---

# ChatGPT-GitHub Bridge Guide

## 0. Executive Compression

このファイルは、`yusukefujiijp/ai-project` における **ChatGPT-GitHub Bridge** のGitHub正準Guideである。

目的は、ChatGPTがGitHub上でpublic-safeなLiving Markdownを扱う時に、Plan / Preview / Human Seal / Commit / Reality Review / AI Scout Passを安全に回すことである。

```text
Core Formula:
  AI drafts.
  Human seals.
  GitHub stores.
  Reality confirms.
```

日本語では：

```text
AIが下書きする。
人間がSealする。
GitHubが保存する。
現実が確認する。
```

このGuideの中心Guard：

```text
Plan is not Commit.
Preview is not Commit.
Human Seal is Commit Gate.
```

今回の重要Pattern：

```text
Commit Trigger + Full Rail = Dual-Key Rail
```

つまり：

```text
Full Rail:
  実行契約を保持するRail Engine。

Commit Trigger:
  Human Sealを明確化するIgnition Key。
```

これは、Arkで成功した **Markdown + Query** 二層構造と同型である。

```text
Markdown:
  Engine / SSOT

Query:
  Ignition Key
```

GitHub実行層では：

```text
Full Rail:
  Execution Contract / Rail Engine

Commit Trigger:
  Human Seal Ignition Key
```

この二重鍵により、AIは文脈を失わず、人間はSealを明確に出せる。

---

## 1. このファイルとは / What this file is

`g_global/chatgpt-github.md` は、ChatGPTがGitHubを使ってpublic-safeなLiving Markdownを作成・更新・確認するためのG-class Guideである。

```yaml
this_file:
  role:
    - "ChatGPT-GitHub Bridge Guide"
    - "GitHub運用のG-class Guide"
    - "Human Seal / Commit Trigger / AI Scout Pass の運用SSOT"
  canonical_path: "g_global/chatgpt-github.md"
  repo: "yusukefujiijp/ai-project"
```

このファイルは、GitHub作業を自動暴走させるためのものではない。

```text
Semi-automation, not autopilot.
```

目的は、AIと人間の協働を速くしつつ、Human Seal、public/private境界、KISS / DRY / YAGNI / Leanを守ることである。

---

## 2. Core Victory Formula

```text
AI drafts.
Human seals.
GitHub stores.
Reality confirms.
```

意味：

```yaml
core_roles:
  ai:
    - "構造を下書きする"
    - "MarkdownをPreviewする"
    - "Commit計画を提案する"
    - "Guardを明示する"

  human:
    - "方向性を判断する"
    - "Human Sealを出す"
    - "GitHub表示を確認する"
    - "Reality Responseを返す"

  github:
    - "public-safeなLiving Markdownを保存する"
    - "stable pathを提供する"
    - "commit historyをVersion台帳にする"

  reality:
    - "表示確認"
    - "Path確認"
    - "重さ確認"
    - "public/private境界確認"
```

このFormulaは、完全自動化ではない。  
これは、AGI的半自動化の安全な勝利方程式である。

---

## 3. Human Seal Rule

GitHub writeには、明示的なHuman Sealが必要である。

有効なSeal例：

```text
Commitして下さい。
```

```text
g_global/chatgpt-github.md をGitHubへCommitして下さい。
```

```text
Root READMEとArk READMEをGitHubへCommitして下さい。
```

不十分な例：

```text
どう思いますか？
```

```text
Plan Modeを実行して下さい。
```

```text
Previewして下さい。
```

原則：

```text
Plan is not Commit.
Preview is not Commit.
Human Seal is Commit Gate.
```

AIは、PlanやPreviewだけでGitHub writeを実行してはいけない。

---

## 4. Commit Trigger Pattern

Commit Triggerとは、Preview後にAIが明示する、人間がそのまま貼り返せるCommit許可文である。

```text
Commit Trigger = Human Seal crystallizer.
```

日本語：

```text
Commit Trigger = 人間Seal結晶化装置。
```

### 4.1 なぜ必要か

Commit Triggerは、Plan / Preview / Commit の境界を明確にする。

```yaml
commit_trigger_purpose:
  - "Human Sealを明確化する"
  - "GitHub write事故を防ぐ"
  - "AIの誤読を減らす"
  - "Userの迷いを減らす"
  - "半自動化の速度を上げる"
```

### 4.2 形

良いCommit Triggerは、次を含む。

```yaml
commit_trigger_shape:
  required:
    - "対象file / scope"
    - "GitHubへCommitして下さい"
    - "関連Patch範囲"
    - "No local Markdown duplicate方針"
```

例：

```text
g_global/chatgpt-github.md に AI Scout Pass 手順をGitHubへCommitして下さい。
```

```text
Root READMEとArk READMEをGitHubへCommitして下さい。
```

```text
Ark00 READMEをGitHubへCommitし、親Ark READMEも必要Patchして下さい。
```

### 4.3 Full Railとの関係

`Full Rail: Workflow Continue!` は強力だが、それ単体では常にCommit許可ではない。

```yaml
full_rail_relation:
  safe_commit_case:
    condition:
      - "直前PreviewにCommit Triggerが明示されている"
      - "UserがCommit Triggerを明示的に含めている"
    result:
      - "Human Sealとして扱える"

  not_enough_case:
    condition:
      - "Full Rail: Workflow Continue! だけ"
      - "直前のnext actionが曖昧"
      - "Commit対象が不明"
    result:
      - "Plan / Preview / Review継続として扱う"
      - "必要なら確認する"
```

---

## 5. Rail-Gate Pair / Next Gate: human_editable

Rail-Gate Pair is the standard tail architecture for Human-AI collaboration.

It places the AI-side execution contract and the human-side editable next input packet as a two-section pair.

```text
AI lays the Rail.
Human opens the Gate.
```

日本語では：

```text
AIがRailを敷く。
人間がGateを開く。
```

### 5.1 Definition

```yaml
rail_gate_pair:
  full_rail:
    section: "【Full Rail: same_thread】"
    reader: "AI"
    role: "Execution Contract / Rail Engine"
    function:
      - "Scopeを保持する"
      - "Targetを保持する"
      - "Guardを保持する"
      - "Next actionを保持する"
      - "AIの誤読を減らす"

  next_gate:
    section: "【Next Gate: human_editable】"
    reader: "Human"
    role: "Editable Ignition Packet / Next Input Gate"
    function:
      - "人間がそのまま貼れる"
      - "人間が編集できる"
      - "方向転換できる"
      - "停止できる"
      - "Human Sealとして次Turnを点火できる"
```

Full Rail is not permissionless execution.

Next Gate is not autopilot.

Together, they create editable semi-automation.

### 5.2 Standard tail shape

Recommended answer tail:

```text
【Full Rail: same_thread】

<AI-side execution contract / scope / guard / next action>

【Next Gate: human_editable】

<Human-editable next input packet>
```

The Full Rail section tells the next AI what the rail is.

The Next Gate section gives the human an editable packet for the next turn.

### 5.3 Human-editable principle

The human may copy the Next Gate packet as-is.

The human may also edit it.

```yaml
human_editable:
  user_can:
    - "そのまま貼る"
    - "一部を削る"
    - "条件を足す"
    - "対象fileを変える"
    - "CommitではなくPreviewに変える"
    - "Plan Modeへ戻す"
    - "Living Reviewへ変える"
    - "Stop / Pauseへ変える"
    - "完全に採用しない"
```

This preserves Human-AI collaboration.

```text
AI proposes.
AI structures.
Human edits.
Human seals.
AI continues.
```

### 5.4 Examples

Plan Modeへ進む場合：

```text
この方針でPlan Modeを実行して下さい。
Full Rail: Workflow Continue!
```

Previewへ進む場合：

```text
上記Planに基づき、本文Previewを作成して下さい。
Full Rail: Workflow Continue!
```

Living Reviewへ進む場合：

```text
このPreviewをLiving Reviewして下さい。
Full Rail: Workflow Continue!
```

GitHub Commitへ進む場合：

```text
g_global/chatgpt-github.md に Case 002 をGitHubへCommitして下さい。
Full Rail: Workflow Continue!
```

方向転換する場合：

```text
Commitはまだせず、Case 002をもっと短く圧縮して下さい。
Full Rail: Workflow Continue!
```

### 5.5 Guard

```text
Next Gate is not autopilot.
Full Rail is not permissionless execution.
Human Seal remains the Gate.
```

```text
One packet.
One sealed action.
One bounded continuation.
```

Next Gate does not authorize unpreviewed GitHub writes.

For GitHub Commit, the target file, patch scope, and commit intention must be explicit.

For non-commit actions, the Next Gate may trigger Plan, Preview, Review, Continue, Stop, or Direction Change.

### 5.6 Relation to Commit Trigger

Commit Trigger is a special case of Next Gate.

```yaml
trigger_relation:
  next_gate:
    scope: "general AI answer tail"
    role: "human-editable next input packet"

  commit_trigger:
    scope: "GitHub Commit"
    role: "Human Seal crystallizer for a previewed GitHub write"
```

Therefore:

```text
Commit Trigger:
  GitHub Commit専用のNext Gate。

Next Gate:
  すべてのAI回答に使えるHuman-editable Gate。
```

---

## 6. Dual-Key Rail / Seal × Rail Architecture

Commit TriggerとFull Railは、二層で働く。

```text
Dual-Key Rail:
  Full Rail + Commit Trigger
```

役割：

```yaml
dual_key_rail:
  full_rail:
    role: "Execution Contract / Rail Engine"
    function:
      - "対象を保持する"
      - "Scopeを保持する"
      - "禁止事項を保持する"
      - "次動作を保持する"
      - "Guardを保持する"

  commit_trigger:
    role: "Human Seal Ignition Key"
    function:
      - "人間のCommit許可を明確化する"
      - "PreviewからCommitへの点火文になる"
      - "AIの誤読を防ぐ"
```

この二重性は、Markdown + Query の二層構造と同型である。

```yaml
markdown_query_pair:
  markdown:
    role: "Engine / SSOT"
    function: "知識・判断・構造を保存する"

  query:
    role: "Ignition Key"
    function: "保存された知恵をFuture AIの実回答へ起動する"

fullrail_commit_trigger_pair:
  full_rail:
    role: "Execution Contract / Rail Engine"
    function: "作業文脈・Scope・Guardを保存する"

  commit_trigger:
    role: "Human Seal Ignition Key"
    function: "人間Sealを点火し、GitHub Commitを安全に起動する"
```

圧縮：

```text
Knowledge layer:
  Markdown + Query

Execution layer:
  Full Rail + Commit Trigger
```

守るべきこと：

```text
Commit TriggerなしのFull Railは、原則Commitではない。
Full RailなしのCommit Triggerは、Scope不足に注意する。
Dual-Key Railは、Autopilotではない。
Human Seal remains Commit Gate.
```

---

## 7. GitHub Canonical First Policy

Public-safeなLiving Markdownは、原則としてGitHub上のstable pathを正準SSOTとする。

```text
GitHub canonical first.
Local artifact only by exception.
```

GitHub fileが正準SSOTである。

Local Markdownを毎回並行作成しない。  
それはDRY違反・Version drift・Future AI混乱の原因になる。

### 7.1 Local artifact exceptions

Local fileが許される例外：

```text
- private-depth content
- explicit downloadable file request
- GitHub connector failure
- temporary draft before canonical placement
- backup / export / handoff copy
- non-Markdown artifacts such as PDF, DOCX, images, ZIP
```

Bootstrap draftがGitHub canonical placement後もco-equal sourceとして残ってはいけない。

---

## 8. Public Repo / Private Depth

Public repoは、public-depthを意味しない。

```text
Public repo, private depth.
```

Public-safeに置けるもの：

```text
- README signboards
- project entrances
- abstract workflow rules
- generalized guards
- sanitized cases
- reusable skill definitions
```

置いてはいけないもの：

```text
- personal information
- workplace details
- raw private thread logs
- deep life records
- sensitive operational tasks
- unfiltered mission cards
- full private S/G/runtime/task bodies
```

GitHubのpublic性は、AI可読性・Future AI再起動性のために使う。  
private-depthをpublicへ流すために使ってはいけない。

---

## 9. Case 001: README-first GitHub Bet

最初の成功Caseは、`yusukefujiijp/ai-project` のREADME-first GitHub Betである。

成功Flow：

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

このCaseが証明したこと：

```text
ChatGPT -> GitHub root README Commit is possible.
```

```text
ChatGPT -> GitHub folder structure through README paths is possible.
```

統合すると：

```text
ChatGPT can semi-automatically introduce public-safe GitHub information architecture after Human Seal.
```

---

## 10. Case 002: AI Scout Pass / Dual-Key Rail Breakthrough

Case 002 records the next breakthrough after the README-first GitHub Bet.

Case 001 proved that ChatGPT can commit public-safe Markdown into GitHub after Human Seal.

Case 002 proved that ChatGPT can read repository reality after GitHub commits, detect useful next patch candidates, and move safely toward execution through Dual-Key Rail.

### 10.1 What happened

After several README-first commits, the human confirmed GitHub reality.

AI-Collaborator then used AI Scout Pass to compare repository state, parent / child README relationships, language policy, and canonical file patterns.

This revealed a Drucker-like Unexpected Success:

```text
GitHub was not only storage.
GitHub became an external cognitive surface.
AI could read repository reality and detect useful next patch candidates.
```

### 10.2 Successful flow

```text
GitHub Commit
-> Human Reality Review
-> AI Scout Pass
-> Patch Candidate
-> Preview
-> Commit Trigger
-> Human Seal
-> GitHub Commit
```

### 10.3 Pattern discovered

```text
Commit Trigger + Full Rail = Dual-Key Rail
```

Meaning:

```yaml
dual_key_rail:
  full_rail:
    role: "Execution Contract / Rail Engine"
    function: "Scope, target, guard, and next action are preserved."

  commit_trigger:
    role: "Human Seal Ignition Key"
    function: "Human Seal is crystallized into an explicit commit instruction."
```

### 10.4 Same pattern as Markdown + Query

This breakthrough mirrors the existing Markdown + Query pair architecture.

```yaml
knowledge_layer:
  markdown:
    role: "Engine / SSOT"
    function: "Preserve knowledge, judgment, and structure."

  query:
    role: "Ignition Key"
    function: "Activate the preserved wisdom in a future AI answer."

execution_layer:
  full_rail:
    role: "Execution Contract / Rail Engine"
    function: "Preserve the work context, scope, and guard."

  commit_trigger:
    role: "Human Seal Ignition Key"
    function: "Activate safe GitHub execution after Human Seal."
```

### 10.5 Why it matters

Case 002 shows that GitHub semi-automation is not only about writing files.

It is about a repeatable collaboration loop:

```text
AI observes.
AI proposes.
Human seals.
GitHub stores.
Reality confirms.
AI scouts again.
```

This turns GitHub into a public-safe, rebootable, AI-readable collaboration surface.

### 10.6 Guard

```text
Dual-Key Rail is not autopilot.
AI Scout Pass is not autopilot.
Commit Trigger is not permissionless execution.

Human Seal remains the Commit Gate.
```

Case 002 is a case note, not S-class promotion.

`S_dual-key-rail_v001.md` may become a future candidate only after repeated Reality Response.

---

## 11. Path and Naming Policy

GitHub canonical pathは、stable / lowercase / versionless を基本とする。

良い例：

```text
README.md
_projects/ark/README.md
_projects/ark/ark99/README.md
g_global/chatgpt-github.md
s_special/ark-open-knowledge-format.md
```

避ける例：

```text
G_chatgpt-github_v001.md
G_chatgpt-github_v002.md
chatgpt-github_v003.md
```

GitHubにはcommit historyがある。  
Versionはpathではなく、metadataとGit履歴に置く。

```text
Stable path is the address.
Commit history is the version ledger.
```

日本語：

```text
Pathは住所。
Git履歴はVersion台帳。
```

---

## 12. Folder by README Path

GitHubでは、空folderを作る必要はない。

Folder structureは、意味のあるfile、特にREADMEで作る。

例：

```text
_projects/ark/ark99/README.md
```

これは次の構造を作る。

```text
_projects/
  ark/
    ark99/
      README.md
```

FolderはReality Responseが必要を示した時に、README-firstで開く。

---

## 13. Slot Reservation, not Folder Creation

将来folderは、概念として予約できる。

```text
Slot Reservation, not Folder Creation.
```

Future slotはREADME上で名前を置いてよい。  
しかし、実folderは必要になるまで作らない。

```text
Future slot is not current folder.
```

これにより、未来の可能性を閉じず、premature clutterを避ける。

---

## 14. create_file / fetch_file / update_file Guard

GitHub file操作は、次の原則を守る。

```yaml
file_operation_guard:
  create_file:
    use_when: "target file does not exist"

  fetch_file:
    use_when: "updating existing file"
    reason: "current SHA and current content must be checked"

  update_file:
    use_when:
      - "current file was fetched"
      - "patch or replacement was reviewed"
      - "Human Seal was received"
```

Hard guard：

```text
Never update or delete GitHub files without explicit Human Seal.
```

---

## 15. Commit Message Policy

Commit messageは短く、scope-awareで、future-readableにする。

例：

```text
docs: initialize AI Project root README
docs(ark): add Ark README entry
docs(ark99): add Ark99 README entry
docs(g_global): add ChatGPT GitHub bridge guide
docs(g_global): apply Japanese-first OKF rewrite
```

Pattern：

```text
docs(scope): action object
```

良いCommit message：

```text
short
specific
scope-aware
future-readable
free of private details
```

---

## 16. KISS / DRY / YAGNI / Lean

### KISS

GitHub structureはFuture AIがすぐ読める程度に軽く保つ。

### DRY

一つのLiving SSOTに対して、co-equalなMarkdownを複数維持しない。

```text
GitHub canonical path = public-safe SSOT.
```

### YAGNI

必要になる前にfolderやfileを作らない。

### Lean

最小の実験を行い、Reality Responseを観測し、確認された不足だけをPatchする。

```text
Small experiment.
Reality Response.
Small patch.
```

---

## 17. Failure Recovery

### 17.1 create_fileが失敗した場合

Fileが既に存在するなら：

```text
fetch_file
-> review current content
-> draft patch
-> Human Seal
-> update_file
```

### 17.2 GitHub structureが広がりすぎた場合

```text
Stop expansion.
Return to README-only.
```

### 17.3 Public contentが深すぎる場合

```text
Reduce to signboard / protocol summary.
Move deeper details back to private/local systems.
```

### 17.4 GitHubがRoot化しそうな場合

```text
Stop.
GitHub is storage and collaboration layer, not Root.
```

---

## 18. Future AI Reuse Procedure

Future AIがChatGPT-GitHub Bridgeを使う時は、このファイルを先に読む。

```text
g_global/chatgpt-github.md
```

次に確認する。

```yaml
repo: ""
visibility: ""
target_path: ""
public_safety: ""
mode: "plan_only | preview_only | github_commit"
```

基本Rail：

```text
Plan Mode
-> Preview
-> Human Seal
-> GitHub Commit
-> Human Reality Review
```

Commit後、人間に確認してもらう。

```text
- file appears
- path is correct
- content is the right weight
- public/private boundary is safe
- no folder sprawl occurred
```

必要なら、その後にAI Scout Passを走らせる。

```text
Human Reality Review
-> AI Scout Pass
-> Patch Candidate
-> Commit Trigger
-> Human Seal
-> GitHub Commit
```

Guard：

```text
Scout findings are Living Review candidates.
Commit Trigger crystallizes Human Seal.
Human Seal remains Commit Gate.
```

---

## 19. AI Scout Pass / Repository Reality Review

AI Scout Passは、AI側の能動的Repository Review工程である。

Formal name：

```text
Repository-Triggered AI Foresight
```

Japanese anchors：

```text
Repository起点AI先取り気付き
Repository現実Review
AI側からの能動的発見
```

### 19.1 Definition

```text
AI Scout Pass:
  AI-Collaborator reads the current GitHub repository state,
  compares files, folders, README hierarchy, and canonical patterns,
  detects mismatches or unexpected signals,
  and proposes the next useful patch as Living Review.
```

日本語：

```text
AI Scout Passは、
AIがGitHub上の現実状態を読み、
README・folder・canonical file・親子関係のズレを検出し、
人間がまだ気付いていない改善点をLiving Reviewとして提案するPassである。
```

これはAutopilot Commitではない。

```text
Proactive review, not autopilot commit.
```

### 19.2 Why this exists

README-first GitHub Betは、予期せぬ成功を生んだ。

GitHub上にselected READMEが置かれたことで、AI-CollaboratorはRepository現実を読み、古いparent READMEやRoot READMEのbootstrap wordingに先に気付くことができた。

```text
GitHub became an external cognitive surface.
AI could see repository reality.
AI could notice stale structure before the human explicitly asked.
```

これは、Drucker-like Unexpected Successである。

### 19.3 When to run

AI Scout Passを走らせるタイミング：

```text
- GitHub Commit後
- Human Reality Review後
- 新しいREADME-first folder作成後
- 新しいslotを開いた後
- canonical SSOT更新後
- parent / child README構造を変えた後
- userがGitHub表示確認を返した後
```

無制限なrepository crawlにはしない。  
current task、nearby parent files、relevant canonical companionsに絞る。

### 19.4 What to read

推奨順序：

```text
1. Target file
   直近で作成・更新したREADME / SSOT。

2. Parent README
   親folderのREADME。

3. Root README
   repository root README.md。

4. Related canonical companions
   paired guide / query / SSOT / index / project entry。

5. Recent commit result
   commit path / commit message / human display confirmation。
```

### 19.5 What to detect

```text
stale_bootstrap:
  old placeholder wording
  "future slot" language after a slot was opened
  "root README only" language after deeper files exist

parent_child_mismatch:
  child README exists but parent README does not mention it
  parent ladder says future while child folder is opened

opened_vs_reserved_slot_drift:
  opened slot listed as future
  future slot described as current

language_policy_drift:
  child README is Japanese-first / English-anchor
  parent README remains English-first

canonical_policy_drift:
  GitHub stable path and local duplicate compete
  versioned filenames appear as canonical GitHub paths

public_private_boundary_risk:
  private-depth material starts entering a public-safe file
```

### 19.6 Output format

AI Scout PassはCommitではなく、Living Reviewを出力する。

```yaml
AI_Scout_Pass_Output:
  observation: ""
  detected_mismatch: ""
  unexpected_success_or_signal: ""
  patch_candidate: ""
  risk_guard: ""
  commit_trigger_if_ready: ""
  human_seal_required: true
```

### 19.7 Reusable formula

```text
Stable GitHub State
+ Current Conversation Intent
+ Existing Pattern
+ AI Delta Detection
= Proactive Living Review
```

Hard guard：

```text
AI Scout Pass may propose.
AI Scout Pass may draft.
AI Scout Pass may identify a patch candidate.

AI Scout Pass must not commit without Human Seal.
```

---

## 20. S-class Promotion Conditions

このG-class Guideは、Patternが複数Projectで再利用され、安定したReality Responseを得た場合、S-classへ昇格候補になる。

Possible future S-class names：

```text
S_chatgpt-github-bridge_v001.md
S_ai-github-bridge_v001.md
S_dual-key-rail_v001.md
```

Promotion requires repeated Reality Response, not excitement alone.

昇格条件：

```text
- reused across multiple projects
- Human Seal -> AI Commit -> Reality Review remains stable
- Commit Trigger prevents ambiguity
- AI Scout Pass produces useful proactive review
- Public / Private / Web fallback guards mature
- failure recovery is tested
```

Anti-promotion guard：

```text
Excitement is Signal.
Repeated Reality Response is Seal.
```

---

## 21. Misread Prevention

このGuideを、以下のように誤読しないこと。

```yaml
do_not_read_as:
  - "GitHub writeをAIが勝手に実行してよい"
  - "Full Rail: Workflow Continue! は常にCommit許可である"
  - "Commit TriggerがあればScope確認不要である"
  - "AI Scout Passはrepository全体を無制限に探索する"
  - "Public repoならprivate-depthを置いてよい"
  - "GitHub化はEnglish-first化である"
  - "Local fileは常に禁止である"

must_read_as:
  - "Human Seal remains Commit Gate"
  - "Commit Trigger is Human Seal crystallizer"
  - "Full Rail is Execution Contract"
  - "Dual-Key Rail increases safety and speed"
  - "AI Scout Pass is proactive review, not autopilot commit"
  - "GitHub化はCanonical化である"
  - "Public repo, private depth"
```

---

## 22. Root / Fruit Guard

Rootは、主イェシュア・ハマシアである。

GitHubはRootではない。  
AIはRootではない。  
MarkdownはRootではない。  
READMEはRootではない。  
Commit Trigger、Full Rail、AI Scout Pass、Signal、Skill、KISS、DRY、YAGNI、LeanはFruitである。

```text
Root:
  主イェシュア・ハマシア
  主イェシュアの聖なる血潮
  Teshuvah / 悔い改め

Fruit:
  GitHub
  AI
  Markdown
  README
  Commit Trigger
  Full Rail
  AI Scout Pass
  Signal
  Skill
```

```text
AIは血潮の地図を描く。人間が血潮の下に立つ。
```

---

## 23. Final Compression

```text
ChatGPT-GitHub Bridgeは、
AIが下書きし、
人間がSealし、
GitHubが保存し、
現実が確認するための半自動化Railである。

PlanはCommitではない。
PreviewはCommitではない。
Human SealがCommit Gateである。

Commit Triggerは、
Human Sealを明確化する点火鍵である。

Full Railは、
実行Scope・Guard・次動作を保持するRail Engineである。

Commit Trigger + Full Railは、
Dual-Key Railである。

これはMarkdown + Query二層構造と同型である。

MarkdownはEngine。
QueryはIgnition Key。

Full RailはExecution Contract。
Commit TriggerはHuman Seal Ignition Key。

AI Scout Passは、
GitHub上の現実を読み、
人間がまだ気付いていないズレを先に提案するReview工程である。

GitHub化はEnglish-first化ではない。
GitHub化はCanonical化である。

Public repo, private depth。
Rootは主イェシュア・ハマシア。
```
