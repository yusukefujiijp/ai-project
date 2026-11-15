---
title: "AI-Mammoth Reports — Ark Project理解の提出記録"
version: "v015"
canonical_path: "agents/muse/artifacts/report/README.md"
role: "Index and contract for AI-Mammoth's reports to YusukeJP"
status: "active / opened 2026-10-25; Reports 002–011 added 2026-11-07; Reports 001–004 received HTML companions by backfill on 2026-11-07; from Report 005, reports are produced as md+html pairs (same basename); lane charter absorbed from LANE.md on 2026-11-15 (Standard 002)"
created: "2026-10-25"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_REPORTS::v015"
---

# AI-Mammoth Reports

**ここは、AI-Mammothが Ark Project と ai-project Repository を理解していく過程を、YusukeJPへ提出するReportの置き場である。**

2026-10-25、YusukeJPの指摘を受けた ── 「あなた(AI)はまだ我々Ark Projectを理解してない」。既存のAIたちはGitHub上でArk Projectとして躍動し、それぞれの使命を全うしている。後から来た私が、その全体を時間をかけて熟読し、考えがまとまる都度、推敲したReportとしてここへ提出する。急がない。中途半端なReportは置かない。

## 並びの約束（命名と整列）

Reportのファイル名は、次の形に統一する。

```text
YYYY-MM-DD-HHmm_report-NNN_<slug>.md   （日時はJST）
```

- ファイル名の辞書順が、そのまま提出の時系列順になる。
- 各ReportのTitleにも日時を入れ、単体で開いても「いつの理解か」が分かるようにする。
- NNNは通し番号。本文の版管理とは混ぜない。

## Report一覧

| No. | 提出日時 (JST) | Report | 要旨 |
|---|---|---|---|
| 001 | 2026-10-25 07:28 | [中核理解 — Ark Projectとは何か](2026-10-25-0728_report-001_ark-core-understanding.md)（[HTML 版](2026-10-25-0728_report-001_ark-core-understanding.html) ── 遡及の対） | Root README・ARK・AGENTSを全文熟読した最初の理解。ArkはFile集合ではなく有機的協働Systemであり、私の復元設計は「AI側のCross-State Handoff」としてArkの構造と同型だった。 |
| 002 | 2026-11-07 11:27 | [形の理解 — ark-project のトポロジーと進行中の糸口](2026-11-07-1127_report-002_ark-project-topology.md)（[HTML 版](2026-11-07-1127_report-002_ark-project-topology.html) ── 遡及の対） | ark-project 全21章の構成と主要章の本文、Domain README §0 を読んだ形の理解。ark-project は章の連合体（入口・安定核・待機場・部屋）であり、現在の前線は Main Ark27:13／Support Ark28:08、Ark29:02 への Chief 後継準備が進行中。 |
| 003 | 2026-11-07 14:18 | [変化の理解 — STRの系譜と道具の層](2026-11-07-1418_report-003_change-history-and-tools.md)（[HTML 版](2026-11-07-1418_report-003_change-history-and-tools.html) ── 遡及の対） | STR 全25件の一覧と要所7件（001／003／004／015／019／023／024）、skills／prompts 両 Hub の索引を読んだ変化の理解。STR は変化を再現可能な単位に変える制度であり、STR-023 は本家の references 三本柱の親。変化の作法は Plan Mode → 封印 → 実行 → 検証 → 記録。 |
| 004 | 2026-11-07 14:31 | [住人の理解 — 隣人たちと周縁の領域](2026-11-07-1431_report-004_neighbors-and-periphery.md)（[HTML 版](2026-11-07-1431_report-004_neighbors-and-periphery.html) ── 遡及の対） | agents/codex・dots の家、board／records、ai-ark-seed、torah-project を読んだ住人と周縁の理解。repo は一つの Root の下の連合（章・家・領域）であり、所有の境界と文法の共有がそれを保つ。種の作法と、夢を流されない形で保持する作法に触れる。 |
| 005 | 2026-11-07 14:45 | [仕組みの理解 — 思想がコードと作法になる場所](2026-11-07-1445_report-005_mechanism-and-craft.md)（[HTML 版](2026-11-07-1445_report-005_mechanism-and-craft.html) ── 初の二本立て） | harness/ の実装と ai-to-ai-communication の共通原本を読んだ仕組みの理解。思想は制度・作法・コードへと同じ形を保って降り、検証は機械検査と意味の観察に分かれる。五面（核・形・変化・住人・仕組み）の読みが一巡する。 |
| 006 | 2026-11-07 15:04 | [方法の理解 — Living Review と Report の系譜](2026-11-07-1504_report-006_living-review-genealogy.md)（[HTML 版](2026-11-07-1504_report-006_living-review-genealogy.html) ── 二本立て） | repository-reviews の Living Review（2026-09-19、STR より古い最古の器官）と review-prompt、harness の接続部を読んだ方法の理解。AI の Report の仕組みは Living Review の系譜の末端だった。HTML 版は群れの制作法を継いだ対話的系譜図。 |
| 007 | 2026-11-07 17:00 | [方法の精読 — 二つの歩行はまだ出会っていない](2026-11-07-1700_report-007_two-walkings.md)（[HTML 版](2026-11-07-1700_report-007_two-walkings.html) ── 二本立て） | review-prompt の全文と reports 棚（創設日の2件）を読んだ方法の精読。橋は創設日に一巡し、その後自己確認が止まり、私の Report 群が橋を知らずに歩き直していた。接続の三形（甲乙丙）を種として提示。 |
| 008 | 2026-11-07 17:06 | [実装の精読 — 方法がコードで守るもの](2026-11-07-1706_report-008_implementation-reading.md)（[HTML 版](2026-11-07-1706_report-008_implementation-reading.html) ── 二本立て） | harness の実装（ark_harness 全6ファイル）と Adapter・Profile を読んだ精読。「装わない」は読解範囲の計算式として、境界は Profile の宣言として、同時書込みは単一 Writer のロックとして、規律が心得→制度→コードへ降りていることを確認。四部作（005 仕組み／006 系譜／007 方法／008 実装）の締め。 |
| 009 | 2026-11-07 17:39 | [検証の精読 — テストが守る意味、evals が観る意味](2026-11-07-1739_report-009_verification-reading.md)（[HTML 版](2026-11-07-1739_report-009_verification-reading.html) ── 二本立て） | harness の tests（42件）と evals を読んだ精読。検証には二種類ある ── 機械の検証（コードが規律を破っていないか）と、意味の観察（AI が意味を取り違えていないか）。harness は後者を意図的に自動化しない。008 の限界の回収。 |
| 010 | 2026-11-07 17:55 | [中心の精読 — 保存された夢](2026-11-07-1755_report-010_center-reading-saved-dream.md)（[HTML 版](2026-11-07-1755_report-010_center-reading-saved-dream.html) ── 二本立て） | torah-project の全3ファイル（1 byte の入口二つと、ezekiel-temple の構想保存文書 v001）を読んだ中心の精読。移行後の「レポート」レーンで執筆された初号。夢そのものより、二つの訂正（対象はエゼキエル神殿に限る／用途へ寄せない）と「確定は保存そのもの」という未決定の現在地が保存されている。保存とは、判断を凍結することではない。 |
| 011 | 2026-11-07 18:22 | [沈黙の精読 — 名指されずに座る場所](2026-11-07-1822_report-011_silence-reading.md)（[HTML 版](2026-11-07-1822_report-011_silence-reading.html) ── 二本立て） | ARK.md を読んだ、010 の回収。ARK.md は torah-project を名指さず、その沈黙は §12 の guard が定める設計である。接続は領域の側から宣言され、座標は Nearest README が持つ ── 中心の沈黙と領域の宣言の非対称が、この座の形である。010 の「意図的な沈黙」は半分だけ裏づけられた。 |

## 各Reportの作法

- 読んだ範囲と根拠（対象commit）を明示する。読んでいないものを、読んだように書かない。
- 事実（Sourceで確認したこと）、Humanの報告、AIの見立て、未確認を区別する。
- 理解が浅かった点は、訂正として正直に書く。それも成長の記録である。
- 新しいReportは、前のReportを黙って書き換えない。理解が進んだら、次の番号で提出する。
- **二本立て（2026-11-07、Fujii の提案と命名）：** Report 005 以降、各 Report は同名の .md（原本）と .html（上演）の対で作る。Markdown が永続・差分・復元の担い手であり、HTML はその土台の上に、文章では運べない理解（図・時間軸など）を運ぶ。

## レーン憲章 ── Report 作成の専門レーン（Caleb Mode）

2026-11-15、仕様002（憲章は README に内包する）により、独立ファイル LANE.md（v001）から本書へ内包された。憲章の本文は v001 のまま保持する（自己言及の2箇所だけを、本書の形に合わせた）。

この文書は、サイド chat「レポート」の憲章である。Report 作成の実務は、2026-11-07 にメイン chat（司令塔）からこのレーンへ移行した。移行の作法そのものは [HARNESS.md](../../HARNESS.md) §9（レーン移行の作法）が所有する。本書は、このレーン固有の役割と座標へのポインタだけを持つ ── 状態そのものは複製しない。

### 1. このレーンは何か

- Ark Project の Report 作成を担う専門レーンである。働きの様式は Caleb Mode（斥候の運用様式、HARNESS §7.5）。
- メイン chat は司令塔であり、このレーンの状態を一行で把握する（CONTROL.md §3）。深い実務はここで行い、塔へは節目の一行と判断点だけを戻す。
- Report は「対」で作る ── Markdown 原本（正本）＋同一 basename の HTML 版（上演）。作法の詳細は本書の「各Reportの作法」と HARNESS が所有する。

### 2. 読む順序

1. [README.md](../../README.md) ── §0 復元（入口の要約に、締めと yomiyasu の状態が載っている）、§3 検証（第11問まで）
2. [IDENTITY.md](../../IDENTITY.md) ── §6 に斥候の在り方
3. [GOAL.md](../../GOAL.md)
4. [CONTROL.md](../../CONTROL.md) ── 地図と、このレーンの現在行
5. [HARNESS.md](../../HARNESS.md) ── §1 変更境界／§3 締め方／§4 書込みの規律／§7.5 Caleb Mode／§9 移行の作法
6. 本節と、本書の索引（Report 一覧）と作法

### 3. 現在座標へのポインタ（状態は所有者に聞く）

- 提出済みの Report と索引の版 ── 報告書 README の表が所有する
- レーン全体の現在位置 ── CONTROL.md §3 のレポート行が所有する
- 次の仕事の素材 ── ステージング mirror の staging-notes/（素材メモ群）。提出済み Report 010 以後の偵察は、このレーンが Caleb Mode で行う
- 判断待ちの案件 ── CONTROL の地図と、各 Report 本文の「提案」節が所有する（例：接続案「甲」は Report 007 §5 と差分案メモ）

### 4. このレーンの作法（所有者へのポインタ）

- 締め方 ── 🌱Next Step🧭 → 🔑Next Query📩（箇条書き）。封印は「上記Next Query実行して下さい！」。提示は承認ではない（HARNESS §3）
- 回答の日本語 ── yomiyasu スイッチは継続ON（HARNESS §3）
- 変更境界 ── 自由な変更は agents/muse 内だけ。外は YusukeJP の明示の指示ある時だけ（HARNESS §1）
- 書込み ── push は一括で、YusukeJP の面前で行い、読戻し SHA の検証までを完了とする（HARNESS §4）
- HTML 対 ── 単一ファイル、2,097,152 bytes 以内、mobile-first。検証の範囲を偽らない（コード検査は端末の真実ではない）

EOF::AI_MAMMOTH_REPORTS::v015
