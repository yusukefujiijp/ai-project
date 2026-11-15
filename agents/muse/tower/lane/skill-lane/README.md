---
title: "skill-lane/ ── Skill LANE の家（入口と憲章）"
version: "v001"
canonical_path: "agents/muse/tower/lane/skill-lane/README.md"
role: "Entrance and charter of the Skill LANE house — one document: the entrance guides, the charter section constitutes the lane (Standard 002)"
status: "active / house created 2026-11-15 with charter (LANE.md) and model case 001; this README was created the same day under Standards 001–002, absorbing the charter, and the separate LANE.md was deleted"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_SKILL_LANE_README::v001"
---

# skill-lane/ ── Skill LANE の家

このフォルダは、**Skill LANE** の家である。Skill LANE は、Ark Project の共有スキル（repo の skills/）の修正・改善を担う専門線である ── 生きた参照の保持、版の追従、スイッチ類の点検と改訂が、主な仕事である。

本書は、この家の入口であると同時に、憲章を内包する（仕様002 ── 家の直下の文書は README 1点だけとし、憲章はその中の節とする）。入口の節が案内を担い、後半の**憲章**の節が、このレーンの定めを担う。

## 中身

- [cases/](cases/) ── 案件の記録の棚。
  - [001_yomiyasu-living-reference.md](cases/001_yomiyasu-living-reference.md) ── モデルケース第1号：yomiyasu-switch の「生きた参照」化（2026-11-15、TOWER で実証され、このレーンへ移行した成功ケース）。

## 住み分け（ポインタ）

- スキルの**置き場所と構図**は GitHub LANE（[../github-lane/](../github-lane/)）が担う。ここは中身の線である。
- レーン地図はルートの CONTROL.md §3 が所有する。ここには複製しない。
- 棚の枠と住人の一覧は [../README.md](../README.md) が示す。

---

## 憲章

この節は、サイド chat「Skill LANE」の憲章である。スキルの修正・改善の実務は、2026-11-15 にメイン chat（TOWER）からこのレーンへ移行した。移行の作法そのものは [HARNESS.md](../../../HARNESS.md) §9（レーン移行の作法）が所有する。本節は、このレーン固有の役割と座標へのポインタだけを持つ ── 状態そのものは複製しない。

### 憲章1. このレーンは何か

- Ark Project の共有スキル（repo の skills/）の修正・改善を担う専門レーンである。生きた参照の保持、版の追従、スイッチ類の点検と改訂が、主な仕事である。
- メイン chat は TOWER であり、このレーンの状態を一行で把握する（CONTROL.md §3）。深い実務はここで行い、塔へは節目の一行と判断点だけを戻す。
- このレーンは、TOWER で実証された成功ケースの移行先である。初代の実証は、yomiyasu-switch の「生きた参照」化（2026-11-15、TOWER で実行）── その記録は [cases/001_yomiyasu-living-reference.md](cases/001_yomiyasu-living-reference.md) が保持する。

### 憲章2. 仕事の作法（モデルケースの7型）

1. **検出** ── 無音の不具合（エラーなく古くなる類）を、Bottleneck として検出する。検出の契機は、人間の問いであることが多い。
2. **命名** ── 霧に正確な名前を与える（例：版の化石化）。名前が、共同注意と次の仕事を固定する。
3. **ベクトル先行** ── 形より先に、方向（ベクトル）を決める。形はベクトルの従者である。
4. **封印と外科的修正** ── 実行は YusukeJP の封印による。修正は必要最小限の箇所に留め、他の契約は保持する。
5. **状態は仕様の外** ── 変わり続ける状態（最後に確認した版など）は、仕様の本文ではなく、記録の側に置く。
6. **読戻し検証** ── 書込みは、読み戻して一致を確認してから、完了と言う（HARNESS §4）。
7. **最初の使用の報告** ── 新しい設計の最初の使用は、出来事として一行で報告する（例：版の前進の報告）。

### 憲章3. 境界

- この家（tower/lane/skill-lane/）は、agents/muse の内側であり、自由領域である。
- skills/ 本体への変更は、案件ごとの封印による（変更境界は HARNESS §1 が所有する）。このレーンの存在そのものは、skills/ への包括的な書込み権限ではない。
- 共有 staging は他のレーンと共用である。編集の前に、staging と repo の現行を照合する。

### 憲章4. 読み順

1. [README.md](../../../README.md) §0（復元の入口）
2. [HARNESS.md](../../../HARNESS.md)（変更境界・書込みの規律・移行の作法）
3. 本書の憲章の節
4. [cases/001_yomiyasu-living-reference.md](cases/001_yomiyasu-living-reference.md)（モデルケース第1号）
5. 案件ごとに、対象スキルの原本

### 憲章5. 現在地

- 新設（2026-11-15）。モデルケース第1号を保持する。
- 同日、仕様001（全フォルダに README）と仕様002（憲章は README に内包する）により、本書が家の入口として新設され、憲章は独立した LANE.md から本書へ内包された（LANE.md は削除）。
- 最初の案件候補は、canon 側の欠陥4件の修繕である ── HARNESS §3 の yomiyasu 固定（v2.5.0 のまま）、CONTROL の版履歴の v013 重複、CONCEPT.md の Router 入口なし、古い名前と数（GOAL §7 の「8つの問い」、artifacts/report/LANE.md の旧名）。TOWER から別途提示され、封印を受けるまでは着手しない。

## 来歴

- 家は 2026-11-15、憲章（当時は独立した LANE.md）とモデルケース第1号をもって建てられた。
- 本書は同日、仕様001・仕様002の確立と同じ束で新設され、憲章を内包した。

EOF::AI_MAMMOTH_SKILL_LANE_README::v001
