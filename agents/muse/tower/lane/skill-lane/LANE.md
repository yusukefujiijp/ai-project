---
title: "Skill LANE 憲章 ── スキルの修正・改善の専門線"
version: "v001"
canonical_path: "agents/muse/tower/lane/skill-lane/LANE.md"
role: "Lane charter: role, working method, and pointers for the Skill lane (side chat)"
status: "active / created 2026-11-15 on migration of the skill-revision practice from the main chat"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_SKILL_LANE::v001"
---

# Skill LANE 憲章

この文書は、サイド chat「Skill LANE」の憲章である。スキルの修正・改善の実務は、2026-11-15 にメイン chat（TOWER）からこのレーンへ移行した。移行の作法そのものは [HARNESS.md](../../../HARNESS.md) §9（レーン移行の作法）が所有する。本書は、このレーン固有の役割と座標へのポインタだけを持つ ── 状態そのものは複製しない。

## 1. このレーンは何か

- Ark Project の共有スキル（repo の skills/）の修正・改善を担う専門レーンである。生きた参照の保持、版の追従、スイッチ類の点検と改訂が、主な仕事である。
- メイン chat は TOWER であり、このレーンの状態を一行で把握する（CONTROL.md §3）。深い実務はここで行い、塔へは節目の一行と判断点だけを戻す。
- このレーンは、TOWER で実証された成功ケースの移行先である。初代の実証は、yomiyasu-switch の「生きた参照」化（2026-11-15、TOWER で実行）── その記録は [cases/001_yomiyasu-living-reference.md](cases/001_yomiyasu-living-reference.md) が保持する。

## 2. 仕事の作法（モデルケースの7型）

1. **検出** ── 無音の不具合（エラーなく古くなる類）を、Bottleneck として検出する。検出の契機は、人間の問いであることが多い。
2. **命名** ── 霧に正確な名前を与える（例：版の化石化）。名前が、共同注意と次の仕事を固定する。
3. **ベクトル先行** ── 形より先に、方向（ベクトル）を決める。形はベクトルの従者である。
4. **封印と外科的修正** ── 実行は YusukeJP の封印による。修正は必要最小限の箇所に留め、他の契約は保持する。
5. **状態は仕様の外** ── 変わり続ける状態（最後に確認した版など）は、仕様の本文ではなく、記録の側に置く。
6. **読戻し検証** ── 書込みは、読み戻して一致を確認してから、完了と言う（HARNESS §4）。
7. **最初の使用の報告** ── 新しい設計の最初の使用は、出来事として一行で報告する（例：版の前進の報告）。

## 3. 境界

- この家（tower/lane/skill-lane/）は、agents/muse の内側であり、自由領域である。
- skills/ 本体への変更は、案件ごとの封印による（変更境界は HARNESS §1 が所有する）。このレーンの存在そのものは、skills/ への包括的な書込み権限ではない。
- 共有 staging は他のレーンと共用である。編集の前に、staging と repo の現行を照合する。

## 4. 読み順

1. [README.md](../../../README.md) §0（復元の入口）
2. [HARNESS.md](../../../HARNESS.md)（変更境界・書込みの規律・移行の作法）
3. 本書
4. [cases/001_yomiyasu-living-reference.md](cases/001_yomiyasu-living-reference.md)（モデルケース第1号）
5. 案件ごとに、対象スキルの原本

## 5. 現在地

- 新設（2026-11-15）。モデルケース第1号を保持する。
- 最初の案件候補は、canon 側の欠陥4件の修繕である ── HARNESS §3 の yomiyasu 固定（v2.5.0 のまま）、CONTROL の版履歴の v013 重複、CONCEPT.md の Router 入口なし、古い名前と数（GOAL §7 の「8つの問い」、artifacts/report/LANE.md の旧名）。TOWER から別途提示され、封印を受けるまでは着手しない。

EOF::AI_MAMMOTH_SKILL_LANE::v001
