---
title: "AI-Mammoth Reports — Ark Project理解の提出記録"
version: "v003"
canonical_path: "agents/muse/artifacts/report/README.md"
role: "Index and contract for AI-Mammoth's reports to YusukeJP"
status: "active / opened 2026-10-25; Report 002 and Report 003 added 2026-11-07"
created: "2026-10-25"
updated: "2026-11-07"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_REPORTS::v003"
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
| 001 | 2026-10-25 07:28 | [中核理解 — Ark Projectとは何か](2026-10-25-0728_report-001_ark-core-understanding.md) | Root README・ARK・AGENTSを全文熟読した最初の理解。ArkはFile集合ではなく有機的協働Systemであり、私の復元設計は「AI側のCross-State Handoff」としてArkの構造と同型だった。 |
| 002 | 2026-11-07 11:27 | [形の理解 — ark-project のトポロジーと進行中の糸口](2026-11-07-1127_report-002_ark-project-topology.md) | ark-project 全21章の構成と主要章の本文、Domain README §0 を読んだ形の理解。ark-project は章の連合体（入口・安定核・待機場・部屋）であり、現在の前線は Main Ark27:13／Support Ark28:08、Ark29:02 への Chief 後継準備が進行中。 |
| 003 | 2026-11-07 14:18 | [変化の理解 — STRの系譜と道具の層](2026-11-07-1418_report-003_change-history-and-tools.md) | STR 全25件の一覧と要所7件（001／003／004／015／019／023／024）、skills／prompts 両 Hub の索引を読んだ変化の理解。STR は変化を再現可能な単位に変える制度であり、STR-023 は本家の references 三本柱の親。変化の作法は Plan Mode → 封印 → 実行 → 検証 → 記録。 |

## 各Reportの作法

- 読んだ範囲と根拠（対象commit）を明示する。読んでいないものを、読んだように書かない。
- 事実（Sourceで確認したこと）、Humanの報告、AIの見立て、未確認を区別する。
- 理解が浅かった点は、訂正として正直に書く。それも成長の記録である。
- 新しいReportは、前のReportを黙って書き換えない。理解が進んだら、次の番号で提出する。

EOF::AI_MAMMOTH_REPORTS::v003
