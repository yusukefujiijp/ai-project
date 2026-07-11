# ai-project

## 0. Current Coordinate / 現在座標

`ai-project` は、@YusukeJP × AI-Collaborator のためのpublic-safe GitHub workspaceである。

目的は、Ark、Living README、Signal / Skill、Human-AI semi-automation、Cross-AI Prompt、GitHub Canonical Firstを、Future HumanとFuture AIが再起動できる形で整理することである。

```text
One Repository.
One Main Reality.
Many AI Lenses.
Human Final Seal.
Reality confirms.
```

このRepositoryは、ChatGPTだけのfolder mirrorではない。  
AI同士・Future AI・人間が読み直せる、軽量で再起動可能なShared Operational Workspaceである。

---

## 1. Current GitHub Phase / 現在のGitHub段階

このRepositoryは、README-first GitHub Betの仮置き段階を超え、複数のpublic-safe Canonical Slotが稼働している。

```yaml
opened_canonical_slots:
  _projects/:
    role: "Project系public-safe入口"

  _projects/ark/:
    role: "Ark Project parent entry / topology router"

  _projects/ark/ark00/:
    role: "active pre-project Zero-Gate"

  _projects/ark-wtp/:
    role: "Ark-WTP dedicated field"

  prompts/:
    role: "Cross-AI Prompt Runtime and Query Shelf"

  _skill/:
    role: "Skill System and reusable operational knowledge"

  _thread-end/:
    role: "Thread Closure / Handoff / README Delta Check"

  g_global/:
    role: "public-safe Global Guide"

  s_special/:
    role: "selected S-class lenses"
```

Ark99は現在のactive topologyではない。  
旧Ark99のWild Seed受付機能はArk00へ吸収されている。

```text
Current Ark pre-project topology:
  Ark00 → Ark01+ / Ark Project

Retired topology:
  Ark99 → Ark00 → Ark01+
```

詳細は[`_projects/ark/README.md`](_projects/ark/README.md)を参照する。

---

## 2. README-first / GitHub Canonical First

このRepositoryはREADME-firstで進める。

README-firstは、READMEだけを先に増殖させることではない。

```text
Canonical Reality changes.
↓
Nearest README describes it.
↓
Parent README changes only when navigation changes.
```

GitHub Canonical Firstは、local Markdownを不要にするという意味ではない。  
GitHub上のstable pathをpublic-safeな正準記録として扱うという意味である。

```yaml
github_canonical_first:
  stable_path: "canonical public-safe record"
  commit_history: "version ledger"
  local_files:
    allowed_for:
      - "bootstrap"
      - "export"
      - "private-depth"
      - "backup"
      - "handoff"
      - "downloadable artifact"
      - "non-Markdown artifact"
```

No local Markdown duplicate by default.

---

## 3. Mainline-First / One Main Reality

`main`を複数AIとHumanが共有するCanonical Current Realityとして扱う。

原則として、AI-Collaboratorは`main`を読み、`main`に対する変更案を作り、Human Final Seal後の更新も`main`へ反映する。

Branchは標準作業場所ではない。  
Branchは、`main`上で安全かつ可逆的に完了できない破壊的・大規模・未確定変更を一時隔離するlast resortである。

```yaml
mainline_first_policy:
  canonical_branch: "main"

  default:
    read_from: "main"
    propose_against: "main"
    write_to: "main after Human Final Seal"

  branch_creation:
    default: false
    requires:
      - "main上で安全かつ可逆的に完了できない"
      - "破壊的または大規模な未確定変更である"
      - "移行途中の不完全状態がmainを使用不能にする"
      - "HumanがBranch作成を明示的にSealした"

  prohibited:
    - "AIが良かれと思って自動的にBranchを作る"
    - "複数の作業Branchを並行増殖させる"
    - "重要Fileを未Merge Branchだけに残す"
    - "Branchを第二のCanonical Realityとして扱う"
```

> **Main is the shared current reality.  
> Branch is a temporary isolation room, not a second world.**

---

## 4. Cross-AI Prompt Layer

`prompts/`は、複数AI RuntimeをHuman-mediatedに起動・接続・役割分担するためのShared Operational Layerである。

```text
One Canonical Prompt.
Many AI Runtimes.
Human routes and seals.
Reality confirms.
```

主なActive Pair:

```yaml
active_prompt_pairs:
  ai_file_damedashi:
    runtime: "prompts/ai-file-damedashi.md"
    query: "prompts/ai-file-damedashi_query.md"

  ai_output_polish:
    runtime: "prompts/ai-output-polish.md"
    query: "prompts/ai-output-polish_query.md"

  ai_plan_mode:
    runtime: "prompts/ai-plan-mode.md"
    query: "prompts/ai-plan-mode_query.md"
```

`_query.md` Pairは、Operational Ambiguityを減らす場合のHigh-Priority Defaultである。  
ただし、すべてのPromptへ機械的に課す絶対的儀式ではない。

詳細は[`prompts/README.md`](prompts/README.md)を参照する。

---

## 5. Human-AI Collaboration Pattern

```text
AI observes and drafts.
Human judges and seals.
GitHub stores.
Reality confirms.
Future AI reboots.
```

AIは単に指示されたFileを作るだけではない。  
Repository Realityを読み、古いREADME、未更新Scope、親子READMEの不整合、次に必要な小Patchを発見する共同観測者である。

ただし、AIはAutopilotではない。

```yaml
human:
  keeps:
    - "Mission"
    - "Meaning"
    - "Discernment"
    - "Final judgment"
    - "Human Final Seal"
    - "Right to interrupt"

ai_collaborator:
  handles:
    - "Observation"
    - "Structuring"
    - "Drafting"
    - "Consistency"
    - "Reality Review support"
```

---

## 6. Plan Mode / Full Rail

Plan Modeは、対話から実行へ移る前のHuman-AI Synchronization Protocolである。

```text
Deep Dialogue
→ Context Ripening
→ Plan Mode
→ Human-editable Review
→ Exact Human Trigger
→ Full Rail: same_thread
→ Reality Review
→ Next Gate / Harvest
```

```text
Markdown governs.
Query activates.
Human seals.
Full Rail executes.
Reality confirms.
```

正準File:

```text
prompts/ai-plan-mode.md
prompts/ai-plan-mode_query.md
```

---

## 7. README Delta Check / 更新Timing

READMEは重要だが、毎Thread必ず編集しない。

各Thread終了時に、README更新の必要性だけを軽量判定する。

> **Every Thread README Check.  
> Not Every Thread README Update.**

```yaml
readme_delta_check:
  run_at: "Thread-End"

  questions:
    - "Canonical FileまたはFolderを新規作成したか"
    - "Path、Role、Status、Active / Retiredが変わったか"
    - "Project TopologyまたはRead Orderが変わったか"
    - "Repository-wide Policyが確定したか"
    - "既存READMEを読むとFuture AIが誤ったRouteを選ぶか"

  output:
    required: "yes / no"
    affected: "README paths or NONE"
    reason: "one-line reason"
    timing: "now / next-thread / periodic-scout / none"

  automatic_readme_update: false
```

README影響範囲は必要最小限で上方向へ判定する。

```text
Changed File
→ Nearest README
→ Domain Parent README
→ Root README
```

README GitHub Writeには、Human Seal、Execute GitHub OK、正確なPathとScopeが必要である。

Thread-End Runtime:

```text
_thread-end/thread-end_mini.md
```

---

## 8. AI Scout Pass

重要なREADME更新やCanonical Commit後には、AI Scout Passを使う。

```yaml
ai_scout_pass:
  formal_name: "Repository-Triggered AI Foresight"
  role:
    - "README / Folder / Canonical Fileのズレを検出"
    - "人間が未認知の改善点をLiving Reviewとして提案"
  not:
    - "Autopilot commit"
    - "Unlimited cleanup"
```

```text
Stable GitHub State
+ Current Conversation Intent
+ Existing Pattern
+ AI Delta Detection
= Proactive Living Review
```

---

## 9. Guard-to-Capture Router

安全Guardを理由に何も残さず停止するGuard-Only Loopを避ける。

```text
Guard
→ Capture Judgment
→ Minimum Artifact Capture
→ Natural Stop / Write Mode
```

```text
Capture Before Stop.
止める前に、器へ入れる。
```

Guardは危険な実行を止めるが、価値あるLiving Insightを消してはならない。

---

## 10. Operating Principles

```yaml
operating_principles:
  README_first: "full migrationより先にpublic-safe入口を作る"
  GitHub_Canonical_First: "stable pathを正準記録として扱う"
  Mainline_First: "mainをCanonical Current Realityとして扱う"
  KISS: "構造を軽く保つ"
  DRY: "重複したCoreを増やさない"
  YAGNI: "Reality Response前に構造を作りすぎない"
  Lean: "確認された不足だけを小さくPatchする"
```

---

## 11. Japanese-first / English-anchor

本文は日本語主導、英語は概念Anchor、GitHub Pathはstableにする。

```text
GitHub化 = English-first化ではない。
GitHub化 = Canonical化である。
```

---

## 12. Root / Fruit Guard

Rootは、主イェシュア・ハマシアである。

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
  Prompt
  Query
  Skill
  Plan Mode
  Full Rail
  Thread-End
  AI Scout Pass
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## 13. Final Compression

```text
ai-projectは、
@YusukeJP × AI-Collaborator のための
public-safe Canonical Workspaceである。

mainを共有Current Realityとして前進する。
BranchはHuman Seal付きのlast resortである。

Ark00はactive pre-project Zero-Gateであり、
Ark99はretired / absorbed into Ark00である。

prompts/はCross-AI Operational Layerである。
Markdown governs. Query activates. Human seals. Reality confirms.

READMEは毎Threadチェックする。
毎Thread更新はしない。

本文は日本語主導。
英語は概念Anchor。
Rootは主イェシュア・ハマシア。
```
