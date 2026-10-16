---
title: "STR-016 — Problem Solvingの初期構成"
canonical_path: "control-center/changes/STR-016-problem-solving-foundation.md"
version: "v001"
created: "2026-10-17"
updated: "2026-10-17"
role: "Scoped structure-change rationale, authority and verification record"
status: "authorized implementation; remote verification follows publication"
source_context: "Work / Ark99:03"
base_commit: "a34becedcbfca35a9165dda6c61f5ab610232bce"
expected_eof: "EOF::STR_016_PROBLEM_SOLVING_FOUNDATION::v001"
---

# STR-016 — Problem Solvingの初期構成

## 1. なぜこの変更を行うか

Humanは就寝前の寝落ちを長年のBottleneckとして扱い、カフェイン抜きガムで防げなかった回を報告した。その後、リステリン系の刺激と歯磨きへの動線を結ぶ案を見いだし、問題の括りをCaffeineという手段から「就寝前の寝落ち問題」へ捉え直した。

このモデルケースを起点に、他の問題にも対応できる初期のフォルダ・ファイル構成を最重要とした。成果を手段別の資料へ閉じ込めず、問題のGoalと判断を引き継ぎ、経験・専門知識・方法の原本へ戻れる構成が必要になった。

Humanの原発言・Correction・現行承認は[Ark99:03経験原本](../../ark-project/ark99/ark99-03/task-records.json)の `problem-reframing / architecture-priority / documentation-approval`、Sources `sleep-s10 / sleep-s12 / sleep-s13 / sleep-s15` を参照する。生活経験の全記録を本STRへ複製しない。

## 2. 権限と書込み前の状態

2026-10-17 Asia/Tokyo、Humanは直前の初期構成案へ **Execute GitHub OK / Human Seal OK** と明示し、必要な実装・検証の継続を承認した。それ以前のPlan-onlyはこの文書整備について解かれた。摂取・身体Trial・外部通信・Reset・過去Task・Project設定変更は今回の対象ではない。

初回確認時のmain `c09413a57fa7b3a9f4132facbfe86b2da7f30a1b` で、problem-solving/README.mdは改行のみ（blob `8b137891791fe96927ad78e64b0aad7bded08bdc`）、同領域に案件本文はなかった。Humanが先に作成した入口を更新する。Rootの旧chocozap/は既に不在、lifestyle/chocozap/は存在しており、その削除・移設をこのAIの成果へ含めない。

## 3. 初期構成と役割

| 対象 | 変更 | 理由と所有する内容 |
|---|---|---|
| [共通入口](../../problem-solving/README.md) | 改行のみのSeedを本文へ更新 | 困りごとから担当原本を選ぶ。全案件の状態を重ねて管理しない |
| [最初の案件](../../problem-solving/cases/bedtime-unintended-sleep.md) | 新規作成 | 就寝前の寝落ちという問題全体のGoal・現在判断・候補・保留・根拠を所有する |
| [Source03経験原本](../../ark-project/ark99/ark99-03/task-records.json) | 新規作成 | 実際の03発言、失敗報告、Correctionと権限の変化を既存Task Records v001で保存する |
| [Root README](../../README.md) | v014・入口追加 | 新領域を発見できるようにする。表示版もmetadataへ合わせる |
| [Caffeineの使い所](../../lifestyle/caffeine/use-contexts.md) | v004・担当先への接続 | Source02当時の形成を保持し、03の進展と問題全体の担当先を区別する |
| [GitHub整理入口](../github/README.md) | v0.2.3・本STRの案内追加 | 構成の理由と検証へ戻れるようにする |
| 本STR | 新規作成 | 変更の意味・範囲・証拠を保存する |
| [日付別AI活動記録](../../records/README.md) | 完了確認後に一活動として追記 | 成果原本と検証結果へ日付から戻る。詳細本文は複製しない |

problem-solving内はREADMEと実案件を置くcases/から始める。既存領域が問題の原本を持つ場合は案内だけでよく、すべての問題を複製しない。経験原本・Caffeineの共通定義・既存Skill・references・success-casesは各役割を保つ。

この初版は、新しいmethods棚、空のtrials領域、独自Schema、専用Skill、第二の全案件管理台帳を必要としない。後の分割は、実際の更新責務・根拠の量・読解上の支障から判断する。

## 4. 保持した意味とCorrection

- Humanの切実さ、Teshuvah、早い解決への願いと、慌てず深く擦り合わせる希望を両方残す。
- 非カフェインガムで防げなかった一回の報告を、全手段の無効・カフェインガムの成功・リステリンの成功へ拡張しない。
- 刺激を目的に役立つ可能性として評価するCorrectionと、Body・Sleep等のGuardを保持する。
- 「入口の再現性」と、身体反応・行動完了・その後の睡眠を分け、実地Feedbackで判断を育てる。
- Source02はその時点の原発言を所有する。03の新報告は03へ保存し、Source02当時のUnknownや保留を黙って書き換えない。
- Ark99:03の確定Title、Handoff、READMEの受入れ契約、state.jsonをこの構成変更で改変しない。

## 5. 検証と実利用の境界

書込み前に、Task Recordsの構文・Schema・ID参照、資料のcanonical_path・版・EOF、今回追加するリンクと所有関係、既存本文の保持を確認する。公開は最新mainの内容と競合を照合し、他者の変更を保持した上で行う。

公開後は変更した対象をRemoteから直接再取得し、意図した本文・SHA・関連リンクを照合する。実際の結果はこの節へ追記し、日付別活動記録から接続する。

今回の検証で確認できるのは、文書構成と保存結果まで。他AIの独立した再構成、Project設定反映、リステリンによる寝落ち防止、毎日の行動達成、複数案件での有用性は、別の実利用・Feedbackを必要とする。

## 6. 次の接続

[案件本文](../../problem-solving/cases/bedtime-unintended-sleep.md)が、今後の就寝前の寝落ち問題の編集上の入口になる。新しい本人報告があれば経験原本へ条件と結果を残し、問題全体の判断が変わる部分をcaseへ反映する。

構成はその仕事を支える器であり、構成づくりの完了を生活上のGoal達成に置き換えない。別案件の登場や実利用で支障が現れた時に、この初期構成を目的に合わせて改訂できる。

EOF::STR_016_PROBLEM_SOLVING_FOUNDATION::v001
