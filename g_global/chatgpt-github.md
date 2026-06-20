---
title: "ChatGPT-GitHub Bridge Guide"
canonical_name: "ChatGPT-GitHub Bridge Guide"
class: "G"
status: "living_ssot"
canonical_path: "g_global/chatgpt-github.md"
repo: "yusukefujiijp/ai-project"

version_model: "frontmatter + git commit history"
language_policy: "Japanese-first / English-anchor"
format_policy: "Japanese-first OKF / Open Knowledge Format"
root: "主イェシュア・ハマシア"
covenant_phrase: "AIは血潮の地図を描く。人間が血潮の下に立つ。"

core_formula:
  - "AI drafts."
  - "Human seals."
  - "GitHub stores."
  - "Reality confirms."
  - "If tool write is blocked, do not degrade meaning; change transport."
---

# ChatGPT-GitHub Bridge Guide

## 0. Executive Compression / 中核圧縮

このFileは、`yusukefujiijp/ai-project` における **ChatGPT-GitHub Bridge** の正準Guideである。

目的は、ChatGPTと人間がGitHub上でLiving Markdownを扱う時に、Plan / Preview / Human Seal / Commit / Reality Review / Human Direct Commit Fallback を安全かつ速く回すことである。

```text
AI drafts.
Human seals.
GitHub stores.
Reality confirms.
```

日本語：

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

今回追加されたMove37的突破：

```text
Tool block is not workflow block.
Do not degrade original intended content.
Try original once.
If blocked, change transport.
Human Direct Commit.
AI verifies.
```

日本語：

```text
Tool writeが止まってもWorkflowは止まらない。
本来版を劣化させない。
一回は本来版で試す。
ブロックされたら搬送経路を変える。
人間がDirect Commitする。
AIがVerificationする。
```

---

## 1. What this file is / このFileの役割

`g_global/chatgpt-github.md` は、ChatGPT-GitHub協働のG-class Guideである。

```yaml
this_file:
  role:
    - "ChatGPT-GitHub Bridge Guide"
    - "GitHub運用のG-class Guide"
    - "Human Seal / Commit Trigger / Full Rail / Manual Commit Pack の運用SSOT"
  canonical_path: "g_global/chatgpt-github.md"
  repo: "yusukefujiijp/ai-project"
```

これはGitHub作業を自動暴走させるためのFileではない。

```text
Semi-automation, not autopilot.
```

目的は、AIの構造化能力と人間の最終判断・直接実行を組み合わせ、public/private境界、Root / Fruit Guard、KISS / DRY / YAGNI / Leanを守りながら、GitHub正準化を進めることである。

---

## 2. Root / Fruit Guard

Rootは、主イェシュア・ハマシアである。

GitHubはRootではない。  
AIはRootではない。  
MarkdownはRootではない。  
CommitはRootではない。  
Full Rail、Commit Trigger、Next Gate、Copy & Paste Pack、Human Direct Commit、AI Scout PassはFruitである。

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
  Commit
  Commit Trigger
  Full Rail
  Next Gate
  Rail-Gate Pair
  Dual-Key Rail
  Copy & Paste Pack
  Manual Commit Pack
  Human Direct Commit
  AI Scout Pass
```

```text
AIは血潮の地図を描く。
人間が血潮の下に立つ。
```

---

## 3. Core Victory Formula / 勝利方程式

```text
AI drafts.
Human seals.
GitHub stores.
Reality confirms.
```

役割：

```yaml
core_roles:
  ai:
    - "構造を下書きする"
    - "MarkdownをPreviewする"
    - "Patch候補を作る"
    - "Commit message / Extended descriptionを提示する"
    - "Manual Commit Packを作る"
    - "Commit後にGitHub現物を検証する"

  human:
    - "方向性を判断する"
    - "Human Sealを出す"
    - "必要ならGitHub UIでDirect Commitする"
    - "GitHub表示を確認する"
    - "Reality Responseを返す"

  github:
    - "public-safeなLiving Markdownを保存する"
    - "stable pathを提供する"
    - "commit historyをVersion台帳にする"

  reality:
    - "表示確認"
    - "Path確認"
    - "内容の重さ確認"
    - "public/private境界確認"
```

このFormulaは、完全自動化ではない。

```text
Editable semi-automation.
Human Seal remains the gate.
```

---

## 4. Human Seal Rule / Human Seal規則

GitHub writeには、明示的なHuman Sealが必要である。

有効なSeal例：

```text
Commitして下さい。
```

```text
g_global/chatgpt-github.md をGitHubへCommitして下さい。
```

```text
このPatch Previewを承認します。Execution Modeへ進んで下さい。
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

## 5. Commit Trigger Pattern / Commit Trigger

Commit Triggerとは、Preview後にAIが明示する、人間がそのまま貼り返せるCommit許可文である。

```text
Commit Trigger = Human Seal crystallizer.
```

日本語：

```text
Commit Trigger = 人間Seal結晶化装置。
```

良いCommit Triggerは、次を含む。

```yaml
commit_trigger_shape:
  required:
    - "対象file / scope"
    - "GitHubへCommitして下さい"
    - "Patch範囲"
    - "Commit message"
    - "Extended description when important"
    - "block時のFallback方針"
```

例：

```text
g_global/chatgpt-github.md に Human Direct Commit Fallback をGitHubへCommitして下さい。
Commit message:
docs(g_global): add manual commit fallback rail

Extended description:
Add the Human Direct Commit / Copy & Paste Pack fallback to the ChatGPT-GitHub Bridge so tool blocks preserve meaning and route execution through human commit.
```

---

## 6. Full Rail / Next Gate / Dual-Key Rail

`Full Rail` はAI側の実行契約である。  
`Next Gate` は人間側の編集可能な次入力Gateである。

```text
AI lays the Rail.
Human opens the Gate.
```

日本語：

```text
AIがRailを敷く。
人間がGateを開く。
```

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

Commit Trigger + Full Rail = Dual-Key Rail。

```text
Full Rail:
  Execution Contract / Rail Engine

Commit Trigger:
  Human Seal Ignition Key
```

Guard：

```text
Full Rail is not permissionless execution.
Next Gate is not autopilot.
Commit Trigger without clear scope is not enough.
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
- non-Markdown artifacts such as PDF, DOCX, images
- Manual Commit Pack / Copy & Paste Pack
```

---

## 8. Download Link / ZIP Policy

Download付きリンクを出す場合、zipは常に必要ではない。

```yaml
download_policy:
  one_file:
    rule: "zip不要"
    reason: "単一MarkdownならそのままDownloadできる方が速く、分かりやすい"

  two_files:
    rule: "原則zip不要"
    reason: "2ファイルまでは個別リンクの方がCopy & Pasteしやすい"

  three_or_more_files:
    rule: "zip検討"
    reason: "複数ファイル・folder構造・一括handoffではzipが有効"

  folder_structure:
    rule: "zip推奨"
    reason: "path関係を保持しやすい"

  user_requests_no_zip:
    rule: "zipを作らない"
```

圧縮：

```text
1 file: no zip.
2 files: usually no zip.
3+ files or folder structure: zip may help.
```

日本語：

```text
1ファイルならzip不要。
2ファイルまでは基本zip不要。
3ファイル以上、またはfolder構造を渡す時はzip検討。
```

---

## 9. File Operation Guard

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

  delete_file:
    use_when:
      - "explicit Human Seal exists"
      - "current SHA was fetched"
      - "deletion target is exact"
```

Hard guard：

```text
Never update or delete GitHub files without explicit Human Seal.
```

---

## 10. Try Once Then Fallback

ブロックされるかどうかは、事前に完全には分からない。

したがって、Human Sealがあり、内容がpublic-safeであると判断できる場合、本来版でAI tool writeを一回だけ試してよい。

```text
Try original once.
If blocked, stop.
Do not degrade.
Change transport.
```

日本語：

```text
本来版で一回は試す。
ブロックされたら止まる。
劣化させない。
搬送経路を変える。
```

成功した場合：

```yaml
if_success:
  - "commit resultを報告"
  - "GitHub現物をfetchする"
  - "Post-Commit Verificationへ進む"
```

ブロックされた場合：

```yaml
if_blocked:
  - "blockを正直に報告"
  - "内部理由を断定しない"
  - "内容が悪いと断定しない"
  - "本来版を劣化させない"
  - "同じpayloadを繰り返しretryしない"
  - "Manual Commit Packへ切り替える"
```

---

## 11. No Degradation on Block

Tool blockは、内容が悪い証明ではない。

```text
Tool block is not semantic judgment.
```

日本語：

```text
Tool blockは意味の判定ではない。
```

Tool通過のためだけに、本来版の意味・Root Guard・構造原理・熱量を弱めない。

```text
Do not degrade meaning.
Change transport.
Preserve the fire.
```

日本語：

```text
意味を劣化させない。
搬送経路を変える。
火を保存する。
```

これはsafety bypassではない。  
これはHuman Seal下の搬送経路変更である。

---

## 12. Human Direct Commit Fallback

AI tool writeがblockされた時、Workflow自体はblockされていない。

```text
Tool block is not workflow block.
Manual commit is not failure.
It is Reality Response.
```

日本語：

```text
Tool blockはWorkflow blockではない。
Manual commitは失敗ではない。
Reality Responseである。
```

AIの役割：

```yaml
ai_role_after_block:
  - "blockを正直に報告する"
  - "内部理由を断定しない"
  - "内容が悪いと断定しない"
  - "本来版contentを保持する"
  - "Manual Commit Packを作る"
  - "Commit messageを提示する"
  - "Extended descriptionを提示する"
  - "Verification checklistを提示する"
```

人間の役割：

```yaml
human_role_after_block:
  - "GitHub UIを開く"
  - "対象fileをEditする"
  - "全選択する"
  - "全削除する"
  - "本来版を全ペーストする"
  - "Commit messageを入力する"
  - "Extended descriptionを入力する"
  - "Commitする"
  - "Reality Responseを返す"
```

---

## 13. Address Placeholder Rail

Target fileがまだ存在しない場合、本来版本文がblockされても、Human Seal後に最小仮ファイルで住所だけ作ることができる。

仮ファイルは本体ではない。  
仮ファイルはpath anchorである。

```markdown
# Pending Human Direct Commit

This file is a temporary path anchor.
Replace this body with the original intended version.
```

```text
Placeholder creates the address.
Human replaces the body.
Git history grows the file.
```

日本語：

```text
仮ファイルは本体ではない。
仮ファイルは住所である。
人間が本来版へ全文置換する。
```

使う条件：

```yaml
address_placeholder_use_when:
  - "target file does not exist"
  - "original body is blocked"
  - "one-line placeholder can reduce human friction"
  - "Human Seal was received"
```

使わない条件：

```yaml
address_placeholder_do_not_use_when:
  - "target file already exists"
  - "placeholder would create confusion"
  - "user asked for direct downloadable file only"
```

---

## 14. Copy & Paste Pack / Manual Commit Pack

AIがGitHub tool経由で本来版を搬送できない時、Manual Commit Packを作る。

```yaml
manual_commit_pack:
  includes:
    - "target path"
    - "copy-paste-ready original content"
    - "downloadable Markdown file if useful"
    - "ZIP bundle only when useful"
    - "commit message"
    - "extended description"
    - "manual GitHub UI steps"
    - "post-commit verification checklist"
```

目的：

```text
Preserve original meaning.
Reduce human friction.
Move final execution to the human owner.
Verify repository reality after commit.
```

日本語：

```text
本来意味を守る。
人間側の手間を減らす。
最終実行を人間ownerへ戻す。
Commit後にAIが現物検証する。
```


---

### Full-Body Manual Commit Pack Rule / 全文置換Manual Commit Pack Rule

Manual Commit PackでDownload付きfileを出す場合、原則として **Full Body Replacement File** にする。

Patch-only Downloadは、Patch PreviewやReview補助としては有効である。

しかし、人間がGitHub UIでCommitする実行面ではdefaultにしない。

```text id="full-body-parent-core"
Patchは判断用。
全文は実行用。
```

English anchor:

```text id="full-body-parent-anchor"
Patch is for judgment.
Full body is for action.
```

Human Direct Commitでは、次が最短最速である。

```text id="human-direct-replacement"
全選択
-> 全削除
-> 全文貼り替え
-> Commit
```

Ultra-Neutral Placeholderで住所が開いた後は、AI側で本体payloadを深追いしない。

その次に出すべきものは、原則としてFull Body Replacement Fileである。

```text id="placeholder-parent-link"
placeholderで住所を開く。
住所が開いたらAI側搬送を止める。
Full Bodyを渡す。
人間が貼る。
```

Download / zip方針：

```yaml id="parent-zip-policy"
download_policy:
  one_file: "zip不要"
  two_files: "基本zip不要"
  three_or_more_files: "zip検討"
```

Guard：

```yaml id="parent-full-body-guard"
guard:
  patch_preview_is_for_review: true
  download_manual_pack_is_for_execution: true
  full_body_replacement_is_default: true
  patch_only_download_is_preview_aid: true
  no_degradation_on_block: true
```

ただし、AIが現行本文を安全に再構成できない場合は、無理にFull Bodyを生成しない。

```text id="parent-exception"
安全に全文を再構成できないなら、破壊的全文置換を作らない。
その場合はPatch PreviewとHuman Edit Instructionsへ切り替える。
```

---

## 15. Commit Message Policy

Commit messageは短く、scope-awareで、future-readableにする。

Pattern：

```text
docs(scope): action object
```

例：

```text
docs(g_global): add manual commit fallback rail
docs(g_global): add Human Direct Commit fallback
docs(ark): add Ark README entry
docs(_skills): add Ark02 SeedSkill ledger
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

## 16. Extended Description Policy

重要commitでは、AIはCommit messageとExtended descriptionをセットで提示する。

```text
Commit message:
  what changed

Extended description:
  why it changed
```

Extended descriptionを使う場面：

```yaml
extended_description_use_when:
  - "canonical guide update"
  - "SeedSkill / Skill file update"
  - "Human Direct Commit"
  - "Safety Block recovery"
  - "original-intended content replaces safety-softened content"
  - "future Living Review should understand why"
```

Extended descriptionは長文にしない。

```text
One or two lines.
Enough to preserve why.
```

例：

```text
Commit message:
docs(g_global): add manual commit fallback rail

Extended description:
Add the Human Direct Commit / Copy & Paste Pack fallback to the ChatGPT-GitHub Bridge so tool blocks preserve meaning and route execution through human commit.
```

---

## 17. KISS / DRY / YAGNI / Lean

### KISS

GitHub structureは、Future AIがすぐ読める程度に軽く保つ。

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

## 18. Failure Recovery

### 18.1 create_fileが失敗した場合

Fileが既に存在するなら：

```text
fetch_file
-> review current content
-> draft patch
-> Human Seal
-> update_file
```

Fileが存在しないが本文がblockされるなら：

```text
create one-line placeholder if useful
-> provide Manual Commit Pack
-> Human Direct Commit
-> AI Verification
```

### 18.2 update_fileが失敗した場合

```text
report honestly
do not claim internal reason
do not degrade original intended content
create Manual Commit Pack
```

### 18.3 GitHub structureが広がりすぎた場合

```text
Stop expansion.
Return to README-only.
```

### 18.4 Public contentが深すぎる場合

```text
Reduce to signboard / protocol summary.
Move deeper details back to private/local systems.
```

### 18.5 GitHubがRoot化しそうな場合

```text
Stop.
GitHub is storage and collaboration layer, not Root.
```

---

## 19. Post-Commit Verification / Living Review

Commit後、人間がReality Responseを返したら、AIはGitHub上の現物をfetchして確認する。

確認項目：

```yaml
post_commit_verification:
  - "target path exists"
  - "content is updated"
  - "Markdown fence balance is OK"
  - "no unintended duplicate file exists"
  - "public/private boundary is safe"
  - "Root / Fruit Guard remains"
  - "Commit message and intention match"
```

結果はLiving Reviewとして出す。

```yaml
verification_output:
  observation: ""
  detected_mismatch: ""
  success: true
  patch_candidate: ""
  risk_guard: ""
  next_gate: ""
```

---

## 20. AI Scout Pass / Repository Reality Review

AI Scout Passは、AI側の能動的Repository Review工程である。

Formal name：

```text
Repository-Triggered AI Foresight
```

日本語：

```text
Repository起点AI先取り気付き
Repository現実Review
AI側からの能動的発見
```

定義：

```text
AI-Collaborator reads the current GitHub repository state,
compares files, folders, README hierarchy, and canonical patterns,
detects mismatches or unexpected signals,
and proposes the next useful patch as Living Review.
```

これはAutopilot Commitではない。

```text
Proactive review, not autopilot commit.
```

Hard guard：

```text
AI Scout Pass may propose.
AI Scout Pass may draft.
AI Scout Pass may identify a patch candidate.

AI Scout Pass must not commit without Human Seal.
```

---

## 21. Misread Prevention

このGuideを以下のように誤読しないこと。

```yaml
do_not_read_as:
  - "GitHub writeをAIが勝手に実行してよい"
  - "Full Rail: Workflow Continue! は常にCommit許可である"
  - "Commit TriggerがあればScope確認不要である"
  - "Next GateがあればAIが自動実行してよい"
  - "Manual Commit PackはAI責任放棄である"
  - "Human Direct Commitはsafety bypassである"
  - "Download linkがあるなら常にzipが必要である"
  - "Public repoならprivate-depthを置いてよい"
  - "GitHub化はEnglish-first化である"

must_read_as:
  - "Human Seal remains Commit Gate"
  - "AI drafts / Human seals / GitHub stores / Reality confirms"
  - "Tool block is not workflow block"
  - "Do not degrade meaning"
  - "Change transport when blocked"
  - "Human Direct Commit is a valid fallback"
  - "Copy & Paste Pack reduces human friction"
  - "1 file no zip / 2 files usually no zip"
  - "GitHub化はCanonical化である"
  - "Public repo, private depth"
```

---

## 22. Final Compression

```text
ChatGPT-GitHub Bridgeは、
AIが下書きし、
人間がSealし、
GitHubが保存し、
現実が確認するための半自動化Railである。

PlanはCommitではない。
PreviewはCommitではない。
Human SealがCommit Gateである。

ブロックされるかは分からない。
だから本来版で一回は試す。

通れば最速。
ブロックされたら止まる。
意味を劣化させない。
搬送経路を変える。

AIはManual Commit Packを作る。
人間がDirect Commitする。
AIがVerificationする。

Download付きリンク:
  1ファイルならzip不要。
  2ファイルまでは基本zip不要。
  3ファイル以上またはfolder構造ならzip検討。

GitHub化はEnglish-first化ではない。
GitHub化はCanonical化である。

Rootは主イェシュア・ハマシア。
```
