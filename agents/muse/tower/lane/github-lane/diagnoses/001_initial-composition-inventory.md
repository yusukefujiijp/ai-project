---
title: "構図診断 001 ── agents/muse 初回インベントリ（実測）"
version: "v001"
canonical_path: "agents/muse/tower/lane/github-lane/diagnoses/001_initial-composition-inventory.md"
role: "First composition diagnosis of the GitHub LANE: measured inventory of agents/muse, diagnosis, and design direction (no moves, no renames)"
status: "active / measured 2026-11-15 at repo main HEAD 410592e4f36f58e83f6b57198a884c7bea853ce4"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_GITHUB_LANE_D001::v001"
---

# 構図診断 001 ── agents/muse 初回インベントリ

GitHub LANE の初回診断である。2026-11-15 の TOWER による熟読診断（構図は成果物を表し組織を表していない／herd-cards の過積載／experiments の文書とバイナリの混在／横断的な記録の置き場がない）を引き継ぎ、このレーン自身の目で実測し直した記録である。本書は診断と設計までを担い、移動・改名は行わない。

## 1. 測定条件（事実）

- 測定日：2026-11-15。対象：repo `yusukefujiijp/ai-project`、branch `main`、HEAD `410592e4f36f58e83f6b57198a884c7bea853ce4`（Skill LANE 束の push と一致 ── 他の書き手による前進なし）。
- 方法：`agents/muse` 配下を GitHub connector の `get_file_contents` で再帰走査し、全エントリの path／種別／size を実測した。
- 規模：全92エントリ（ファイル78点、フォルダ14点）、ファイル総量 53,619,136 bytes。
- 読み戻した原本（blob SHA 照合済み）：CONTROL.md `9c997e28`（v017）、HARNESS.md `4ded2368`（v009）、tower/README.md `5c10d99f`（v001）、tower/lane/README.md `9a5dbb84`（v001）、tower/lane/skill-lane/LANE.md `6a33ca84`（v001）、同 cases/001 `5124f4b6`（v001）。

## 2. 全体像（事実 ── 領域ごとの実測）

| 領域 | ファイル数 | 容量 (bytes) | 備考 |
|---|---|---|---|
| ルート文書（canon 7点） | 7 | 69,432 | README／IDENTITY／GOAL／CONCEPT／CONTROL／HARNESS／DESIGN-LAW |
| artifacts/report/ | 24 | 213,185 | Report 001〜011 の md／html 対（同名・拡張子のみ相違）＋ LANE.md ＋ README |
| artifacts/herd-cards/ | 35 | 52,862,770 | 内訳は §3-D2 |
| references/（三本柱） | 7 | 103,934 | 各柱 README＋jsonl |
| assets/ | 1 | 357,924 | avatar.webp |
| tower/（組織の層） | 4 | 11,891 | 入口2点＋Skill LANE の家2点（本書の追加前） |
| **合計** | **78** | **53,619,136** | herd-cards が容量の 98.6% を占める |

## 3. 診断（事実 → 解釈）

### D1. 構図は「成果物」を表し、「組織」を表してこなかった ── 是正の開始点に立つ

- 事実：2026-11-15 に組織の層 `tower/` が新設され、入口2点（tower/README.md、tower/lane/README.md）が v001 に育った。現在の住人は Skill LANE と、本書を置く GitHub LANE の2線のみ。
- 事実：既存の2レーン（Report LANE、Herd LANE）の憲章は artifacts/ 配下の現住所で機能している（artifacts/report/LANE.md、artifacts/herd-cards/LANE.md）。
- 解釈：これは不整合ではなく、棚の枠（tower/lane/README.md）が定めた「移転は各 LANE の後続判断とする」という層を足す進め方の途中である。診断として記録すべきは「未反映」ではなく「移行の勾配がここにある」という座標である。

### D2. herd-cards の過積載

- 事実：35点・52,862,770 bytes（ファイル数の45%、容量の98.6%）。内訳 ── 直下：憲章 LANE.md、README.md（31,648 bytes）、判断Task judgment-tasks.md（17,351 bytes）、デッキ本体 herd-cards_v001〜v003.html（計 約5.98 MB）。brushup/：単体カードの HTML 8点（計 約3.36 MB）。experiments/：21点（§3-D3）。
- 解釈：重さそのものは成果の蓄積であり、悪ではない。問題は**同居**である ── 憲章・入口・判断の記録・本体・試作・実験が一つのフォルダに積まれ、入口である README.md が索引と来歴と案内を一身に担って過負荷になっている。住所の階層が、仕事の階層（本体／試作／実験／判断）を表し切れていない。

### D3. experiments の文書とバイナリの混在、入口の欠如

- 事実：experiments/ は21点・43,468,720 bytes ── 設計文書2点（experiment-deck-v001-bottleneck-map.md、experiment-design-principles.md）と、実験デッキ HTML 19点（v002〜v022、欠番 v001／v016／v018）が同居する。experiments/ にも brushup/ にも、フォルダ自身の入口（README）はない。
- 解釈：文書（読むもの）とバイナリ級 HTML（上演されるもの）が同じ住所に混在し、入口がないため、来た者は herd-cards/README.md の過負荷な案内に依存する。欠番は版採番の履歴として正当でありうるが、入口がない場所では欠番の理由も辿れない。

### D4. 横断的な記録の置き場がない

- 事実：本診断の前身である 2026-11-15 の熟読診断は、chat と記憶の中にだけ存在し、repo 内に住所を持たなかった。複数の領域にまたがる読み（構図診断、横断監査の類）を置く棚は、agents/muse のどこにもない。
- 解釈：この家の `diagnoses/` を、その置き場の第一号とする。ただし置けるのは構図の診断と設計だけに限り、汎用の倉庫にはしない（置き場の新設が、新しい混在を生んではならない）。

### D5. 入口の不揃い（指すだけに留めるもの）

- 事実：ルート README は canon への Router を持つが、CONCEPT.md への入口がない件は、canon 側の修繕として Skill LANE の Case 002 の範囲である。
- 解釈：構図の診断として座標だけを記録し、修繕には手を出さない ── 住み分け（中身は Skill LANE、器は GitHub LANE）の実例として、ここに線を引く。

## 4. 設計の方向（ベクトル ── いずれも未実施、束と封印が先）

1. **入口の整備を先に** ── experiments/ と brushup/ への入口（README）の新設案を、Herd LANE への提示形で用意する。住所を動かす前に、案内を立てる。
2. **herd-cards の階層の言語化** ── 本体／brushup／実験／判断の4つの仕事の層に、それぞれ正確な名前と住所の対応を与える設計案を束にする。分割・移設そのものは Herd LANE の判断と別の封印による。
3. **組織の勾配の保持** ── 旧 LANE の家の移転は急がない。各 LANE が熟した時に、その LANE の束として扱う（D1 の勾配は、このレーンが監視し続ける）。
4. **横断診断の定常化** ── 本 diagnoses/ に、節目ごとに診断を重ねる。次の診断は、実測の差分（前回比）から始める。

## 5. CONTROL §3 への地図行 ── 追加案（提示形）

地図は CONTROL §3 が所有するため、このレーンは地図を複製せず、追加案をここに提示形で置く。適用（CONTROL の版上げ、次は v018）と地図への記入は、所有者である TOWER 側の判断と実行に委ねる。

追加する行の案（§3 統括マップの Skill LANE 行の次へ）：

| レーン | 部屋 | 家（原本の場所） | 現在地 |
|---|---|---|---|
| GitHub 構造化（GitHub LANE） | サイドチャット「GitHub LANE」（2026-11-15 開設） | [tower/lane/github-lane/](tower/lane/github-lane/) ── 憲章は [LANE.md](tower/lane/github-lane/LANE.md)、組織層の入口は [tower/README.md](tower/README.md) | 新設。repo（特に agents/muse）のフォルダ・ファイル構図の鳥瞰と構造化を担う専門線。初回構図診断インベントリ（diagnoses/001）を保持し、診断と設計まで ── 移動・改名は各部の判断と封印による |

## 6. 検証記録

- 本書の実測は §1 の HEAD における走査に基づく。走査後に他の書き手が repo を前進させた場合、本書の数値はその時点の座標として読むこと（診断は版を持ち、差分は次の診断が担う）。
- 本束の書込み（本書、憲章 LANE.md、棚の住人表の更新）は一括 push とし、読戻しの blob SHA 照合をもって完了とする（HARNESS §4）。

EOF::AI_MAMMOTH_GITHUB_LANE_D001::v001
