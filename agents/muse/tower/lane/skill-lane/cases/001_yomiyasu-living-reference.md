---
title: "モデルケース 001 ── yomiyasu-switch の生きた参照化（版の化石化の修正）"
version: "v001"
canonical_path: "agents/muse/tower/lane/skill-lane/cases/001_yomiyasu-living-reference.md"
role: "Model case record for the Skill LANE: detection, naming, vector, surgical revision, verification"
status: "completed 2026-11-15 in the main chat (TOWER); preserved here as the Skill LANE's founding case"
created: "2026-11-15"
updated: "2026-11-15"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_SKILL_LANE_CASE_001::v001"
---

# モデルケース 001 ── yomiyasu-switch の生きた参照化

Skill LANE のモデルケース第1号。2026-11-15 の朝、TOWER で実行された一件の全記録である。

## 1. 検出

- YusukeJP の問い「yomiyasu3になってないか？」が、検出器になった。
- 事実 ── skills/yomiyasu-switch は、原本（nanaism/yomiyasu）を Version 2.5.0（commit 29d67ccb）に固定していた。その間に原本は 3.1.0（commit db78b9bc）へ進んでいた。
- 不具合の性質 ── エラーは出ない。適用は続く。「ON」と表示され続ける。**版だけが、静かに古くなっていた**。唯一のアラームは、人間の問いだった。

## 2. 命名

- この状態を「**版の化石化**」と名づけた ── 生きている方法を、善意の固定（同一性の保証のための基点）が、化石に変えていた。
- 構造の読み ── 一つのファイルに、変わる速さの違う二層（安定した役割と契約／原本側の版の事実）が同居していた。原本の出来事が、我々の保守作業に化ける構造だった。

## 3. ベクトル

- YusukeJP の確定 ── 「Version up を確認して、Version up があれば新しい方を使うという方向や方向性（ベクトル）が重要です！」
- 原則として一文 ── **固定は自家製に、参照は原本へ**。
- ベクトルから導かれる設計 ── 確認は使用の一部になる／新しい方を使うことが既定で、使わない時にだけ理由が要る／版の前進は、止める理由ではなく報告する出来事になる／固定は消えず、予備（最後に確認した版）に降りる。

## 4. 実行（封印を受けて）

- skills/yomiyasu-switch/SKILL.md を v003-design へ改訂した ── 変更は4か所だけ（版の表記、固定基点の節、関連する一文、更新の節）。他の契約（責務分担・状態の区別・表示の規律）は、v002-design のまま保持した。
- 「最後に確認した版」の記録を、Skill 本文の外に新設した ── skills/yomiyasu-switch/last-confirmed.md（当時の記録：3.1.0）。
- push は commit 7bc6f4f2。読戻しの blob SHA が手元の原稿と両ファイルとも一致し、検証された。

## 5. 差分（原本 2.5.0 → 3.1.0、全文読解による）

- 核は不変 ── 意味の保持（主張・比重・言い切りの強さ・文の働き）、情報を足さない、文書の立場と文末、検査と照合の工程。
- 新規 ── 文の種類の保持の明示、直訳語・漢語の詰まりの規則、太字ラベルの細則、文書の種類（13種）と読み手の段階の仕組み、一括置換の禁止の明文。
- 全体は、約46,000字から約15,700字へ圧縮された。

## 6. 学び（一般化）

1. 固定は、善意でも化石化する。生きている原本への参照は、正規の場所への参照と、使用時の版確認に置く。
2. 本体を直しても、引用側に化石が残ることがある ── 改訂の直後、canon の HARNESS §3 に「v2.5.0」の固定が残っていることが見つかった（Case 002 候補）。**引用の棚卸しまでが、一件の仕事である**。
3. 版の前進を「報告する出来事」にすると、無音の陳腐化は構造的に消える。動きがあれば、必ず声が上がる。

## 7. 状態

- 完了（2026-11-15、TOWER で実行・検証済み）。
- 後続 ── Case 002 候補として、canon 側の欠陥4件の修繕が、Skill LANE の最初の案件に控えている（憲章 §5）。

EOF::AI_MAMMOTH_SKILL_LANE_CASE_001::v001
