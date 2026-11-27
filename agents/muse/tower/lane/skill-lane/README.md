---
title: "skill-lane/ ── Skill LANE の家（入口と憲章）"
version: "v005"
canonical_path: "agents/muse/tower/lane/skill-lane/README.md"
role: "Entrance and charter of the Skill LANE house — one document: the entrance guides, the charter section constitutes the lane (Standard 002)"
status: "active / house created 2026-11-15 with charter (LANE.md) and model case 001; this README was created the same day under Standards 001–002, absorbing the charter, and the separate LANE.md was deleted; Case 002 (canon defects repair) executed on 2026-11-15 (v002); Case 003 (question-count fossil) executed on 2026-11-15 (v003); Case 004 (skills living-reference audit, record only) recorded on 2026-11-27 (v004); Case 005 (correction of the audit count in the Case 004 record) executed on 2026-11-27 (v005)"
created: "2026-11-15"
updated: "2026-11-27"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_SKILL_LANE_README::v005"
---

# skill-lane/ ── Skill LANE の家

このフォルダは、**Skill LANE** の家である。Skill LANE は、Ark Project の共有スキル（repo の skills/）の修正・改善を担う専門線である ── 生きた参照の保持、版の追従、スイッチ類の点検と改訂が、主な仕事である。

本書は、この家の入口であると同時に、憲章を内包する（仕様002 ── 家の直下の文書は README 1点だけとし、憲章はその中の節とする）。入口の節が案内を担い、後半の**憲章**の節が、このレーンの定めを担う。

## 中身

- [cases/](cases/) ── 案件の記録の棚。
  - [001_yomiyasu-living-reference.md](cases/001_yomiyasu-living-reference.md) ── モデルケース第1号：yomiyasu-switch の「生きた参照」化（2026-11-15、TOWER で実証され、このレーンへ移行した成功ケース）。
  - [002_canon-defects-repair.md](cases/002_canon-defects-repair.md) ── Case 002：canon 側の欠陥4件の修繕（2026-11-15、Skill LANE で再検証・設計・実行）。
  - [003_question-count-fossil.md](cases/003_question-count-fossil.md) ── Case 003：問いの数の化石化の修繕（2026-11-15、引用の棚卸しの再走査から発生）。
  - [004_skills-living-reference-audit.md](cases/004_skills-living-reference-audit.md) ── Case 004：skills/ の生きた参照の初監査の記録（2026-11-16 監査実行、欠陥0件 ── 修繕ではなく記録の案件）。
  - [005_case004-count-correction.md](cases/005_case004-count-correction.md) ── Case 005：Case 004 の記録の件数の訂正（2026-11-27、注記つき訂正と第2段監査の追補の収蔵）。

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
- 最初の案件 Case 002（canon 側の欠陥4件の修繕）は、2026-11-15 に実行済みである ── HARNESS §3 の yomiyasu 固定の生きた参照化（HARNESS v011）、CONTROL の版履歴の v013 重複への注記つき訂正（CONTROL v019）、CONCEPT.md の Router 入口の追加（README v013）、古い名前と数の現行化（GOAL v003、artifacts/report/README v016）。記録は [cases/002_canon-defects-repair.md](cases/002_canon-defects-repair.md) が保持する。
- Case 003（問いの数の化石化の修繕）は、2026-11-15 に実行済みである ── README §3 の見出しの無数化（README v014）、artifacts/report/README の憲章の読み順のポインタ化（同 v017）。記録は [cases/003_question-count-fossil.md](cases/003_question-count-fossil.md) が保持する。
- Case 004（skills/ の生きた参照の初監査）は、2026-11-16 に実行済みである ── repo のスキル全件の SKILL.md を監査し、化石化の欠陥は0件だった（家はもともと生きた参照で建っていた）。修繕は無く、監査の記録は [cases/004_skills-living-reference-audit.md](cases/004_skills-living-reference-audit.md) が保持する。
- Case 005（Case 004 の記録の件数の訂正）は、2026-11-27 に実行済みである ── 第2段監査の数の照合で、監査件数の記録「47」が実際は49件だった数え違いと判明し、注記つきで訂正した（cases/004 は v002）。あわせて第2段監査（索引・_references・_grok・SKILL.md 以外のファイル）の記録を、cases/004 の追補へ収蔵した。記録は [cases/005_case004-count-correction.md](cases/005_case004-count-correction.md) が保持する。

## 来歴

- 家は 2026-11-15、憲章（当時は独立した LANE.md）とモデルケース第1号をもって建てられた。
- 本書は同日、仕様001・仕様002の確立と同じ束で新設され、憲章を内包した。
- v002（2026-11-15）: Case 002 の実行にあわせ、cases の一覧へ 002 を追加し、憲章5「現在地」を実行済みの形へ現行化した。
- v003（2026-11-15）: Case 003 の実行にあわせ、cases の一覧へ 003 を追加し、憲章5「現在地」へ Case 003 の実行済みを追記した。
- v004（2026-11-27）: Case 004（skills/ の生きた参照の初監査の記録）の新設にあわせ、cases の一覧へ 004 を追加し、憲章5「現在地」へ Case 004 の実行済みを追記した。監査は 2026-11-16 の実行であり、本版はその記録の収蔵である。
- v005（2026-11-27）: Case 005 の実行にあわせ、cases の一覧へ 005 を追加し、憲章5「現在地」へ Case 005 の実行済みを追記した。あわせて現在地の Case 004 の行から監査件数の数を外した（正確な数は cases/004 の追補が日付とともに所有する）。

EOF::AI_MAMMOTH_SKILL_LANE_README::v005
