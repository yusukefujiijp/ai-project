---
title: "tower/lane/ ── LANE の家の棚"
version: "v003"
canonical_path: "agents/muse/tower/lane/README.md"
role: "The lanes' shelf: the frame (who lives where) and the resident list"
status: "active / Seed planted by YusukeJP 2026-11-15 (newline-only), grown to v001 in the Skill LANE bundle; GitHub LANE added as resident in v002; v003 aligns the frame and pointers with Standard 002 (charter inside the house README)"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_TOWER_LANE::v003"
---

# tower/lane/ ── LANE の家の棚

このフォルダには、各 LANE の**家**が並ぶ。家とは、その LANE の憲章と、その LANE 自身の記録の置き場である。本書は、棚の枠と住人の一覧だけを持つ。

## 枠（住み分け）

- 憲章は、各 LANE の家の README の中の節として置く（仕様002 ── 家の直下の文書は README 1点だけ。独立した LANE.md は置かない）。
- 成果物は [artifacts/](../../artifacts/) に置く。家は成果物の倉庫ではない。
- 状態は各所有者が持つ（地図は CONTROL §3、Report の索引は artifacts/report/README、のように）。家は状態を複製しない。
- 家の最小形は、README（入口と憲章）1点だけである。内側の間取りは各 LANE の自由とし、空に近い家も正しい家とする ── 排出を担う LANE の家は、倉庫ではなく扉であることが正しい場合がある。

## 住人

| LANE | 家 | 役割 | 現在地 |
|---|---|---|---|
| Skill LANE | [skill-lane/](skill-lane/) | スキルの修正・改善の専門線 | 最初の住人（2026-11-15）。入口と憲章は [skill-lane/README.md](skill-lane/README.md) |
| GitHub LANE | [github-lane/](github-lane/) | GitHub 構造化の専門線 ── repo（特に agents/muse）のフォルダ・ファイル構図の鳥瞰と構造化（器の線） | 二番目の住人（2026-11-15）。入口と憲章は [github-lane/README.md](github-lane/README.md)、初回構図診断は [github-lane/diagnoses/001_initial-composition-inventory.md](github-lane/diagnoses/001_initial-composition-inventory.md) |

他の LANE の家は、熟した時に、LANE ごとに建てる。既存の charter（artifacts/report/LANE.md、artifacts/herd-cards/LANE.md）は、当面は現住所のまま機能する ── 移転は、各 LANE の後続判断とする。

## 来歴

- この棚の入口は、YusukeJP 自身の手で、改行のみの Seed として植えられた（2026-11-15）。
- v002（2026-11-15）：GitHub LANE を住人に加えた ── 家（憲章と初回構図診断）の新設と対になる棚側の更新であり、枠（住み分け）そのものは v001 から変更していない。
- v003（2026-11-15）：仕様002（憲章は README に内包する、YusukeJP の KISS の決定）の確立に合わせ、枠の「家の最小形」と住人表の憲章ポインタを、README 内包の形へ更新した。既存 charter（artifacts/ の2家）は現住所のまま ── その追随は仕様002 §4 のとおり、各家の移行束による。

EOF::AI_MAMMOTH_TOWER_LANE::v003
