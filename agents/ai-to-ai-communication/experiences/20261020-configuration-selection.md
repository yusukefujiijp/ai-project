---
title: "構成選択の経験 — 文章の短さと判断の難度を分ける"
version: "v001"
canonical_path: "agents/ai-to-ai-communication/experiences/20261020-configuration-selection.md"
record_type: "Reconstructed experience from Chief Dot handoff summary; not a full transcript"
occurred_on: "2026-10-20"
recorded_on: "2026-10-20"
actors: "dot-0000: 初穂 / Ark27:10 AI; compiled by receiving ChatGPT Work"
source: "AI間コミュニケーション基盤の構築と経験集約: Chief DotからChatGPT Workへの実行担当引継ぎ / v001 / 2026-10-20 JST / Layer 6"
source_access: "Human supplied the AI-authored handoff in this Work conversation; private transcript not retrieved or published"
source_expected_eof: "EOF::ARK_AI_TO_AI_COMMUNICATION_WORK_HANDOFF::v001"
change_record: "../../../control-center/changes/STR-020-ai-to-ai-communication-foundation.md"
expected_eof: "EOF::AI_TO_AI_CONFIGURATION_SELECTION_20261020::v001"
---

# 構成選択の経験

**AIが目的から構成を選ぶ際、文章が短いことと判断が容易であることを分け、相手の批判から選択理由を修正した経験。** 初穂がこのWorkへ引き継いだ要約を出所として編纂した。以下の実施・UI確認・返信観測は初穂の報告であり、編纂したWorkによる実験の直接観測ではない。

## 1. 出所と、今回残す範囲

Sourceは上記metadataで特定するAI作成の引継ぎv001、Layer 6「10月20日の構成選択経験」である。Humanが本Workへ渡した全文のうち、当該要約の内容を公開記録へ編纂する計画を提示し、HumanがAの18パスの実行を承認した。アクセス可能な公開会話URLは得ていないため、URLやメッセージIDを作らない。

以下に要約が伝えた内容を残すことで、私的な元対話へアクセスできないFuture AIも、何を根拠にどこまで判断できるかを理解できるようにする。私的Workの全履歴、長期メモリ、設定画面の独立証明を収録したものではない。相手の一節以外は編集要約であり、全送信・返信の逐語録としない。

## 2. 引継ぎ要約が報告した経緯

1. 終了したArk27:10を実験対象とし、Main担当を復活させず、返信のみの範囲で行った。
2. 初穂がSol／HighとAstra／Maxを選び、UI設定と二往復の応答を確認したと報告した。モデル・推論設定・速度設定を分けて扱う。
3. 相手の「文章の短さと判断の難度は別」という批判を採用し、選択理由を修正した。これは相手の批評を次の判断へ反映した点であり、最初の構成が劣っていたという実証ではない。
4. 高速OFFを保持し、最後は元のAstra／Max／高速OFFへ戻して確認したと報告した。
5. 実バックエンドの独立証明、厳密A/B、モデルの因果的優劣、全場面の最適性は未確認だった。
6. 当初の実験にはGitHub変更を含めていなかった。実験時の保存未実施を「約束した保存を忘れた失敗」へ書き換えない。今回の経験編纂・公開は、その後の別の承認範囲である。

要約は二往復と報告しているが、物理投稿数、各メッセージの全文、各操作の正確な時刻はこのSourceから確定しない。別の公開経験の回数やUI経路を、この実験へ補充しない。

## 3. 今回の判断へ使えること

Humanが目的・制約を示し、AIが依頼の難しさ・対話の役割・必要な検証から構成を選ぶ方式では、選択理由自体を批評可能にすることが役立つ。今回の報告では、短文という表面的特徴から判断の難度を推定する理由が、相手の指摘で修正された。協働の価値は、最初から正しい選択を宣言することだけでなく、異論を受けて前提を更新できることにもある。

これは報告から導いた適用上の解釈であり、性能比較の実証ではない。次の場面では、文章量に加えて矛盾・権限・前提・批評の難しさを見て選び、見落としや浅い応答が出た時は、構成・入力文脈・問いの立て方を見直す。過去と同じ設定値を選ぶだけで、同じ質や消費になるとは仮定しない。

高速OFFというHuman方針を保持する。推論Ultraは速度Ultrafastとは別に扱い、各設定名の実際の意味は使用時点の公式資料と環境で確認する。この記録に出てくるSol／High・Astra／Maxは当時の報告中の表記で、現在利用できる構成や推奨順位を宣言するものではない。

## 4. 未確認と、次に接続する条件

UI確認の報告、実バックエンド、応答品質の因果、消費量、異なる履歴・課題での再現性は別々に検証する必要がある。新しい厳密比較が有益かは、目的、履歴条件、使える観測、現在の権限から判断する。本経験の保存を、新しい比較試験・設定変更・Ark27:10の再起動の承認にしない。

この経験から採用する共通判断は[共通マニュアル](../README.md#3-目的から構成を選び観測で見直す)へ、他の対話経験は[経験入口](README.md)へ接続する。保存と実読解・実利用効果は区別し、次の実践で得られた訂正は出所と条件を保って育てる。

EOF::AI_TO_AI_CONFIGURATION_SELECTION_20261020::v001
