---
title: "tower/lane/ ── LANE の家の棚"
version: "v001"
canonical_path: "agents/muse/tower/lane/README.md"
role: "The lanes' shelf: the frame (who lives where) and the resident list"
status: "active / Seed planted by YusukeJP 2026-11-15 (newline-only), grown to v001 in the Skill LANE bundle"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_TOWER_LANE::v001"
---

# tower/lane/ ── LANE の家の棚

このフォルダには、各 LANE の**家**が並ぶ。家とは、その LANE の charter と、その LANE 自身の記録の置き場である。本書は、棚の枠と住人の一覧だけを持つ。

## 枠（住み分け）

- charter は、各 LANE の家に置く。
- 成果物は [artifacts/](../../artifacts/) に置く。家は成果物の倉庫ではない。
- 状態は各所有者が持つ（地図は CONTROL §3、Report の索引は artifacts/report/README、のように）。家は状態を複製しない。
- 家の最小形は、charter（LANE.md）1点だけである。内側の間取りは各 LANE の自由とし、空に近い家も正しい家とする ── 排出を担う LANE の家は、倉庫ではなく扉であることが正しい場合がある。

## 住人

| LANE | 家 | 役割 | 現在地 |
|---|---|---|---|
| Skill LANE | [skill-lane/](skill-lane/) | スキルの修正・改善の専門線 | 最初の住人（2026-11-15）。憲章は [skill-lane/LANE.md](skill-lane/LANE.md) |

他の LANE の家は、熟した時に、LANE ごとに建てる。既存の charter（artifacts/report/LANE.md、artifacts/herd-cards/LANE.md）は、当面は現住所のまま機能する ── 移転は、各 LANE の後続判断とする。

## 来歴

- この棚の入口は、YusukeJP 自身の手で、改行のみの Seed として植えられた（2026-11-15）。

EOF::AI_MAMMOTH_TOWER_LANE::v001
