---
title: "STR-010 — 全AI横断のAI活用日時記録"
canonical_path: "control-center/changes/STR-010-cross-ai-daily-records.md"
version: "v001"
created: "2026-10-03"
updated: "2026-10-03"
status: "implementation record / behavioral field validation pending"
source_commit: "dc52d603941cd7d2ba33274fc6c2a4d6962cea10"
expected_eof: "EOF::STR_010::v001"
---

# STR-010 — 全AI横断のAI活用日時記録

## 目的・承認・形成理由

YusukeJPは、Dots限定の旧日別recordsを戻すのでなく、ai-project全体でAIを活用した活動を日付から辿れる場所へ育てる案を提示した。ChatGPT、Work、Dots、その他GitHubを利用できるAIが参加し、Future AIが元会話なしに経緯と根拠へ戻れることが目的である。

HumanはJSONLを採用し、さらに「Humanの一日全体ではなくAIを活用した分」「多少分割しても、一行ずつ何をしたかが分かる」「One-Shot／Few-Shotで伝える」「難しく書き過ぎない」と訂正した。相談・調査・計画も対象であり、大きな完成だけを選別する台帳ではない。

複数回の計画検討後、2026-10-03のHuman入力でGitHub実装が明示承認された。実行担当はDot00:00; 初穂（dot-0000）。GitHub上のauthorとAIの記録責任は別である。

会話の根拠は次のメッセージ識別子にある。これらは公開URLではなく、元のDots会話へのアクセスが必要なtraceである。本書の説明は編集要約であり、会話全文の逐語複写ではない。

- `Sentinel_a1b635c0f71c8191ae4510c6cee07412`：全AI横断の日別記録とsaveへの接続案
- `Sentinel_b8c7818d398481918a25399117035a42`：JSONL採用
- `Sentinel_cb9ab0d8f21881918fb8ee18dd54c25b`：AI活用に範囲を絞り、一行の活動単位と例を重視
- `Sentinel_08c6646b99a88191a360fb2f59be7348`：簡単な言葉と実運用の難しさを踏まえた再計画
- `Sentinel_76f339f8490881918813516371d603bf`：失敗後の回復を重視し、計画対象の実装・GitHub保存を承認

## 変更範囲と責務

- [records/README.md](../../records/README.md)：改行のみだった入口に目的、記録契機、架空例、六項目、日付・訂正・競合・根拠の扱いを定義
- `records/YYYY/MM/YYYY-MM-DD.jsonl`：記録日のAsia/Tokyo日付で、実際に確認した活動を追記。初回は今回の仕事の範囲だけを記録し、過去全件を移植しない
- [Repository README](../../README.md)：recordsへの一行の経路と版・変更理由を追加
- [save共有本文](../../skills/save/SKILL.md)：recordsへの用途別接続を追加。形式の詳細はrecordsガイドが所有し、同じ個人Skillを更新する
- [control-center入口](../README.md)：本件への案内を追加

既存Actorログ・lessons・Boardの可変状態は変更しない。日別記録は必要な要点と原本参照を持つが、原本本文や通信Currentを二重管理しない。旧dots/recordsは[ARC-008](../ARCHIVE.md#arc-008)の保管を維持する。常設の自動収集、監視、別Skill、専用DB、実際のThread移行を追加しない。

## 確認方法と証拠の境界

READMEの架空例は実績JSONLへ混入させず、JSON構文・必須型・UUID・日時・行形式・重複をローカルで検査する。隔離した追記モデルで、他者の行と未知field保持、同ID同内容の再試行、同ID異内容の衝突、訂正行を確認する。これは文書の形式と限定モデルの試験であり、全AIの読解・自動発動・本番での同時書込み成功を証明しない。

共有本文の保存後はRemoteを直接再取得し、意図した内容と対象外の保持を照合する。個人Skillの更新は同一登録物を使い、取得本文と共有版の一致を別に確認する。実際の確認結果は初回の日別記録と実装報告へ残す。今回の保存前本文から、保存後確認や利用効果を先取りして完了と称しない。

記録作成時刻、GitHub公開時刻、出来事時刻を区別する。Plan-onlyやSTOP中には自動記録もしない。後続の明示保存承認があれば過去の検討を当時の計画として残せる。

## 残る検証と戻し方

実利用で見るのは、AIが無理なく活動を拾えるか、一行が粗過ぎたり細か過ぎたりしないか、別AIが原本へ辿れるか、並行保存や再試行で重複しないかである。今回の導入だけで実運用成功を断定しない。問題があればガイドとsaveの接続を承認範囲で修正し、既存行を消さず訂正や明示した形式移行で回復する。

構造を戻す必要がある場合は、記録実体を保全したうえで現役入口とsaveの接続を見直す。記録済み成果・Board・Actorログを巻き添えに削除しない。本記録は新しい恒久承認や自動再実行命令ではない。

EOF::STR_010::v001
