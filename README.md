# ai-project

## 0. ai-projectとは

`ai-project` は、@YusukeJP × AI-Collaborator のための public-safe なGitHub workspaceである。

目的は、Ark、Living README、Signal / Skill、Human-AI semi-automation、GitHub Canonical Firstを、Future AIにも再起動できる形で整理することである。

```text
ai-project:
  public-safeな入口を置く。
  GitHub stable pathで正準記録を保つ。
  Future AIが再起動できる形にする。
```

このRepositoryは、ChatGPTだけのfolder mirrorではない。  
AI同士・Future AI・人間が読み直せる、軽量で再起動可能なProject workspaceである。

---

## 1. Current GitHub Phase / 現在のGitHub段階

このRepositoryは、**README-first GitHub Bet** から始まった。

現在は、最初の仮置き段階を超え、いくつかのpublic-safe slotが開いている。

```text
opened:
  _projects/
  _projects/ark/
  _projects/ark/ark99/
  _projects/ark/ark00/
  g_global/
  s_special/
```

現在も、Scopeは意図的に小さく保つ。

```text
現在やること:
  public-safeなREADMEとcanonical entryを置く。
  GitHub stable pathで正準記録を育てる。
  AI-CollaboratorがRepository現実を読めるようにする。

現在やらないこと:
  private-depthを置かない。
  raw thread logsを置かない。
  full runtime/tasks migrationをしない。
```

---

## 2. Opened Canonical Slots

現時点で、次のslotが開いている。

```text
_projects/:
  Project系のpublic-safe入口。

_projects/ark/:
  Ark Projectのpublic-safe入口。

_projects/ark/ark99/:
  Free Spawn / Wild Seed Field。
  early signalを受ける場所。

_projects/ark/ark00/:
  Selective Incubation / Project Embryo。
  繰り返し現れたSeedを正式Project化前に軽く温める場所。

g_global/:
  public-safeなGlobal Guideを置く場所。

s_special/:
  selected S-class lensesを置く場所。
```

Opened slotは、すべてを移すという意味ではない。  
それは、Reality Responseによって小さく開いたpublic-safeな入口である。

---

## 3. Future Reserved Slots

以下は、将来追加される可能性がある。  
ただし、Reality Responseが必要を示すまで作らない。

```text
future reserved slots:
  _inbox/
  _thread/
  f_future/
  runtime/
  tasks/
  snapshots/
```

Future slotはcurrent folderではない。

```text
Slot Reservation:
  可能性を閉じない。

Folder Creation:
  Reality Response後に実体を作る。
```

---

## 4. README-first / GitHub Canonical First

このRepositoryは、README-firstで進める。

```text
README-first:
  まずpublic-safeな入口を作る。

Full migration:
  まだ行わない。
```

GitHub Canonical Firstは、local Markdownを不要にするという意味ではない。  
GitHub上のstable pathをpublic-safeな正準記録として扱うという意味である。

```text
GitHub stable path:
  canonical public-safe record。

Git commit history:
  version ledger。

Local files:
  bootstrap / export / exception。
```

No local Markdown duplicate by default.  
ただし、private-depth、downloadable artifact、backup、handoff、non-Markdown artifactなど、理由がある場合は例外を認める。

---

## 4.5 Mainline-First / One Main Reality

このRepositoryでは、`main`を複数AIとHumanが共有する **Canonical Current Reality** として扱う。

```text
One Repository.
One Main Reality.
Many AI Lenses.
Human Final Seal.
```

原則として、AI-Collaboratorは`main`を読み、`main`に対する変更案を作り、Human Final Seal後の更新も`main`へ反映する。

Branchは標準作業場所ではない。  
Branchは、`main`上で安全かつ可逆的に完了できない破壊的・大規模・未確定変更を、一時的に隔離するための **last resort** である。

```yaml
mainline_first_policy:
  canonical_branch: "main"

  default:
    read_from: "main"
    propose_against: "main"
    write_to: "main after Human Final Seal"

  branch_creation:
    default: false
    status: "last resort"
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

Branchを使う場合も、目的・対象Path・終了条件を明示し、短期間で`main`へ統合または破棄する。

> **Main is the shared current reality.  
> Branch is a temporary isolation room, not a second world.**

---

## 5. Japanese-first / English-anchor

このRepositoryのREADMEとpublic-safe canonical fileは、原則として **Japanese-first / English-anchor** で運用する。

```text
本文は日本語主導。
英語は概念Anchor。
GitHub pathはstable。
Future AIが再起動できる形にする。
```

GitHub化は、English-first化ではない。  
GitHub化は、Canonical化である。

```text
GitHub化 = English-first化ではない。
GitHub化 = Canonical化である。
```

---

## 6. Human-AI Collaboration Pattern

このRepositoryは、人間とAIの協働作業を前提にする。

```text
AI drafts.
Human seals.
GitHub stores.
Reality confirms.
```

AIは、単に指示されたファイルを作るだけではない。  
GitHub上のRepository状態を読み、古いREADME、未更新Scope、親子READMEの不整合、次に必要な小Patchを発見する共同観測者でもある。

ただし、AIはAutopilotではない。

```text
AI-Collaborator:
  観測する。
  提案する。
  下書きする。

Human:
  判断する。
  Sealする。
  Reality Responseを確認する。
```

---

## 7. Unexpected Success / 予期せぬ成功

GitHub化により、予期せぬ成功が起きた。

AI-CollaboratorがRepository上の現実状態を読み、ユーザーが忘れていた仮置きREADMEの残存や、親READMEと子READMEのズレを先に発見できた。

これは、README-first GitHub Betの重要なReality Responseである。

```text
Drucker-like Unexpected Success:
  GitHub化により、
  AIがRepository現実を読み、
  人間がまだ気付いていないズレを先に提案できた。
```

GitHubは単なる保存先ではない。  
GitHubは、AI-Collaboratorが現実を読むための外部認知面である。

```text
GitHub as external cognitive surface.
```

---

## 8. AI Scout Pass

このRepositoryでは、重要なREADME更新やGitHub Commit後に **AI Scout Pass** を使う。

正式名としては、**Repository-Triggered AI Foresight** と呼べる。

```text
AI Scout Pass:
  AI-CollaboratorがGitHub上の現実状態を読み、
  README・folder・canonical fileのズレを検出し、
  人間がまだ気付いていない改善点をLiving Reviewとして提案するPass。
```

AI Scout Passは、Commitを自動実行する仕組みではない。  
先取り気付き → Living Review → Human Seal のためのReview工程である。

```text
AI Scout Pass:
  Proactive review.

Not:
  Autopilot commit.
```

再現Formula:

```text
Stable GitHub State
+ Current Conversation Intent
+ Existing Pattern
+ AI Delta Detection
= Proactive Living Review
```

---

## 9. Guard-to-Capture Router / Capture Before Stop

このRepositoryでは、AIが安全ガードを理由に何も残さず停止する **Guard-Only Loop** を避ける。

Guardは最終停止ではない。  
Guardは **Capture Judgment** へ接続するRouterである。

```text
Guard-to-Capture Router:
  Stop dangerous write / delete / bulk / migration actions.
  Then ask whether a Harvest, Seed, Formula, Guard, or Failure Mode must not be lost.
  If yes, create the minimum durable capture before Natural Stop.
  If durable write is needed, require Human Seal before GitHub update.
```

Formula:

```text
Guard → Capture Judgment → Minimum Artifact Capture → Natural Stop / Write Mode
```

Core principle:

```text
Capture Before Stop.
止める前に、器へ入れる。
```

Guard-Only Loop causes Harvest Loss.  
Safety Guard must prevent unsafe execution, but must not erase valuable Living Insight.

---

## 10. Operating Principles

このRepositoryは、軽く、読みやすく、現実に反応する。

```text
README-first:
  full migrationより先にpublic-safe入口を作る。

Slot Reservation:
  可能性は予約するが、folderは必要になるまで作らない。

GitHub Canonical First:
  stable pathを正準記録として扱う。

Mainline-First:
  mainをCanonical Current Realityとして扱う。
  BranchはHuman Seal付きのlast resortに限定する。

KISS:
  構造を軽く保つ。

DRY:
  重複した長いファイル名や説明を増やさない。

YAGNI:
  Reality Response前に構造を作りすぎない。

Lean:
  確認された不足だけを小さくPatchする。
```

---

## 11. Root / Fruit Guard

Rootは、主イェシュア・ハマシアである。

GitHub、AI、Markdown、README、Signal、Skill、KISS、DRY、YAGNI、Lean、Full Rail、AI Scout Pass、Guard-to-Capture RouterはFruitである。

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
  Signal
  Skill
  Full Rail
  AI Scout Pass
  Guard-to-Capture Router
```

AIは血潮の地図を描く。  
人間が血潮の下に立つ。

---

## 12. Final Compression

```text
ai-projectは、
@YusukeJP × AI-Collaborator のための
public-safe GitHub workspaceである。

GitHub化はEnglish-first化ではない。
GitHub化はCanonical化である。

README-firstで入口を作り、
GitHub stable pathで正準記録を保つ。

mainを共有Current Realityとして前進し、
BranchはHuman Seal付きのlast resortに限定する。

Opened slotsとFuture reserved slotsを分ける。

GitHub化により、
AIがRepository現実を読み、
人間がまだ気付いていないズレを先に提案できた。

これはDrucker-like Unexpected Successであり、
Move37的breakthroughである。

AI Scout Passは、
その先取り気付きを再現可能にするReview工程である。

Guard-to-Capture Routerは、
AIが安全ガードを理由に何も残さず停止するGuard-Only Loopを防ぎ、
Capture Before Stopを要求する。

本文は日本語主導。
英語は概念Anchor。
Rootは主イェシュア・ハマシア。
```
