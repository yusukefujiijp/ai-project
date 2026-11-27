---
title: "Case 005 ── Case 004 の記録の件数の訂正"
version: "v001"
canonical_path: "agents/muse/tower/lane/skill-lane/cases/005_case004-count-correction.md"
role: "Case record for the Skill LANE: detection by count reconciliation in the stage-2 audit, annotated correction of the Case 004 record, and number-free living summaries"
status: "completed 2026-11-27 in the Skill LANE — found by the stage-2 audit, designed in this lane, executed on YusukeJP's seal"
created: "2026-11-27"
updated: "2026-11-27"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_SKILL_LANE_CASE_005::v001"
---

# Case 005 ── Case 004 の記録の件数の訂正

監査の記録の中に、監査した者自身の数え違いが残っていた。第2段監査の「数の照合」がそれを検出した ── 検出器は、他人の化石だけでなく、自分の記録にも向けなければならない。

## 1. 検出（数の照合）

第2段監査（Case 004 で境界として残した範囲 ── 索引、_references、_grok、SKILL.md 以外のファイル）を行うにあたり、三つの数を突き合わせた。

- フォルダの実数 ── 監査時点（2026-11-16）のスキルフォルダは 49 件だった（現在は 54 件）。
- 取得したファイルの実数 ── 第1段で取得・走査した SKILL.md は 49 件であり、取得に失敗したものは無かった。
- 記録された数 ── Case 004 の §1、家の README の現在地、cases/README の一覧は、いずれも「47」と書いていた。

二つの実数が一致し、記録だけがずれていた。誤りは Skill LANE 自身の数え違いである。監査の実質 ── 全件の走査と、化石の家族の欠陥0件という結論 ── は変わらない。なお第2段の走査そのもの（136 件）では、新しい化石の欠陥は見つからなかった（結果は cases/004 の §7 追補が所有する）。

## 2. 再検証（誤りの所在）

- cases/004 §1 の2箇所（対象の数と、取得した数）。
- 家の README の憲章5「現在地」の Case 004 の行（1箇所）。
- cases/README の 004 の行（1箇所）。
- CONTROL v022 には件数の記載が無いことを grep で確認した ── 訂正は不要であり、本 Case の束には含めない。

## 3. 設計と判断

- **記録の訂正は、注記つきで行う** ── Case 002（CONTROL の v013 重複）で確立した型である。cases/004 の原文は当時の記録として保持し、§1 へ注記を付け足して v002 とする。黙って書き換えれば、訂正そのものが監査証跡から消える。
- **生きている要約からは、数を外す** ── Case 003 の乙案と同じ型である。家の README の現在地と cases/README の一覧は現在形の自己定義であり、数は持たせない。正確な数は、日付とともに cases/004 の追補（§7）が所有する。
- **第2段の記録は、Case 004 の追補に収蔵する** ── 新しいファイルを作らず、監査の記録は監査の家（cases/004）に一元化する。あわせて Hub の未登録3件の観察も、追補に事実として残す。
- **判断事項（Hub の未登録3件）の扱い** ── YusukeJP へ甲（観察として記録するだけ）／乙（TOWER へ一行の報告も送る）を提示した。封印に甲／乙の明示は無かったため、推奨した甲で実行した。乙への変更は、YusukeJP の一言でいつでも可能である。

## 4. 実行（YusukeJP の封印を受けて）

- 全ファイルを1回の push に集約した（仕様003 ── 1束1認識）。本書は、その push に含まれる。
- cases/004 v001 → v002（§1 への注記つき訂正と、§7 追補の新設）。
- 家の README v004 → v005（現在地の無数化と Case 005 の追記、一覧への 005 の追加）。
- cases/README v004 → v005（一覧の 004 の行の無数化と、005 の追加）。
- 本書（cases/005）の新設。
- CONTROL は変更していない。

## 5. 検証

- 本書を含む束の全ファイルは、push の後に読み戻し、blob SHA の一致を確認する（その結果は、本書ではなく、封印への完了報告が保持する ── 本書は push の中身の一部であり、自分自身の検証結果を自分の中に書けないためである）。
- あわせて、家の文書に「訂正されていない規範の数としての47」が残っていないことを grep で確認する（注記と追補の中で、誤りとして引用される「47」は、訂正の一部であり残存ではない）。

EOF::AI_MAMMOTH_SKILL_LANE_CASE_005::v001
