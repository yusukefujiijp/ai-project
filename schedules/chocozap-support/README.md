---
title: chocoZAP 継続サポート
canonical_path: schedules/chocozap-support/README.md
version: v002
created: 2026-10-13
updated: 2026-10-13
updated_reason: chocoZAP原本の配置変更に伴う参照先のみ更新。配信の時刻・頻度・送信先・有効状態・実行範囲は保持
status: active
---

# chocoZAP 継続サポート

既存のchocoZAP会話へ、現在の本人の状況に合う支援を届ける日次タスク。開始前メモと現在のSweet Spotを毎回同じ入口から確認し、必要な補足を続ける。

| 項目 | 現行の関係 |
| --- | --- |
| Runtime | ChatGPTの既存タスク「chocoZAP 継続サポート」 |
| 定期時刻 | 毎日17:00、Asia/Tokyo |
| 配信先 | 既存タスクに結びついたchocoZAPの会話 |
| 実行指示の原本 | [PROMPT.md](PROMPT.md) |
| 開始前メモ・現在の方法・表示契約 | [lifestyle/chocozap/README.md](../../lifestyle/chocozap/README.md) |
| 重量・本人原文の正本 | [sweet-spots.json](../../lifestyle/chocozap/sweet-spots.json) |
| 分析・再検討条件 | [analyses.json](../../lifestyle/chocozap/analyses.json) |

## 【接続と同期】

Runtimeには、yusukefujiijp/ai-projectのmain / schedules/chocozap-support/PROMPT.mdを毎回全文取得して実行する短いLoaderを設定する。PROMPT本文やメモ・重量表をRuntimeへ複製しない。内部タスクID・会話IDはこの公開原本に保存しない。

更新時はschedules/README.mdの同期契約に従い、原本のGitHub保存を再取得で確かめてからRuntimeのLoaderを設定・再取得する。タイトル・有効状態・配信先・毎日17:00・タイムゾーンは、本人が別途変更しない限り保持する。Runtimeの現在設定を観測せず、GitHub更新だけで接続済みと報告しない。

原本取得に失敗した場合は、未取得・取得済み範囲を明示し、実行時に確認できる会話・本人の最新報告だけで限定的に続ける。未取得の一覧を完全・最新と装わない。別タスクの変更、GitHub書込み、旧アーカイブからの現行値の復元は、この自動実行へ含めない。

## 【開始前に読むこととの関係】

毎日17:00は既存の日次案内の時刻であり、Workout開始の自動検知ではない。朝の利用や別時刻の開始前相談でも、同じchocozap原本からメモと現在値を提示する。読了返信・新しい日次報告は要求しない。

2026-10-13の本人承認を受け、既存タスクの指示をGitHubの原本へ接続する構成を導入。タスク設定の確認と、次の実配信・本人が思い出せた結果は分けて観測する。

EOF::CHOCOZAP_SUPPORT_SCHEDULE::v002
