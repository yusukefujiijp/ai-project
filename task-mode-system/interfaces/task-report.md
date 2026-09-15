---
title: "Task報告 — コピー用フォームと解釈"
version: "0.2.0"
status: "prototype / existing Human-supplied template preserved"
role: "AI-managed source for presenting and interpreting Human Task reports"
primary_reader: "Current AI / other AI / Future AI"
updated_reason: "Define the file as AI-managed form source while preserving the Human input template."
canonical_path: "task-mode-system/interfaces/task-report.md"
created: "2026-09-15"
updated: "2026-09-15"
expected_eof: "EOF::TASK_MODE_SYSTEM_TASK_REPORT::v0.2.0"
---

# Task報告

## 1. AIが提示・解釈する原本

本書の読者はAIである。Humanへ本書の読解やSchema理解を要求せず、必要なフォーム・項目を会話へ取り出して使う。コピー用本文だけがHumanへ渡す内容であり、内部の解釈・更新規則まで一緒に提示する必要はない。フォーム不要の報告にはそのまま応答する。

入力は埋められる項目だけでよい。自由文だけでも受け取れる。候補は選択肢であり、全部を選んだ意味ではない。候補外の表現を自由に使える。辞書登録や端末上の選択UIの導入状況は、別に確認する。

下記はHumanがArk27:03で提示した既存Templateを基に、内容欄の固定例「起床→カフェインガム」を空欄へ変更したコピー用版である。新しい報告が誤ってその実行報告になるのを防ぐための編集である。固定例を含む提示内容は、空白を整えた転記と明示して[03経験原本](../../ark-project/ark27/ark27-03/task-records.json)の`s07`に残す。

## 2. Copy & Paste — Task報告

```text
✍️【Task報告】
Task名:
〔候補: 起床Task／ベッドメイクTask／コロコロTask／トイレTask／歯磨きTask／シャワーTask／着替えTask／食事Task／Laundry Task／ゴミ捨てTask／Workout Task／Walking Task／帰宅Task／その他〕
種別:
〔候補: 実行報告／予定／訂正／気付き／相談〕
状態:
〔候補: 開始／途中／終了／一部終了／中断／見送り／再開／不明／該当なし〕
日付:
時刻:
〔必要なら: ○時頃／開始○時／終了○時／○時〜○時〕
内容:
補足:
〔必要なら: 場所／きっかけ／順序変更の理由／他Taskとの関係〕
Feedback:
〔必要なら: 感想／身体感覚／良かったこと／困ったこと／予想との差〕
BrainDump:
```

## 3. AI側の読み方

Task名は活動の名前、種別は発言の性質、状態は今回の対象範囲における状態である。この三つを合わせて理解する。種別が「予定」なら、状態欄に「終了」とあっても実際の終了と決めつけない。

日付・時刻が空欄なら、過去Threadの日付やプロフィールのtimezoneで埋めない。「今」は発言時点を指す相対表現として保持できる。記録作成日とTask実行日を分ける。

同じTask名でも、別実行なら別の出来事である。「シャワー終了」から歯磨きの終了を推測しない。「ゴミを出した」から収集成功まで推測しない。

内容・補足・Feedback・BrainDumpの境界を厳密にHumanへ強制しない。必要な情報が別欄にあっても意味から読む。身体感覚は報告された感覚として保持し、医学的因果を補わない。

## 4. 記録Schemaとの関係

このフォームは、[v001記録Schema](../../formats/task-records/v001.schema.json)へそのまま機械変換する仕様ではない。状態とEvidenceの意味は[共有ガイド](../../formats/task-records/README.md)に従う。

「開始」「中断」「再開」「一部終了」はSchemaの状態値と一対一では対応しない。原文、時点、範囲をSourceに保持し、必要なら出来事や部分Taskを分ける。解釈できない値を黙って`completed`や`in_progress`へ変換しない。形式拡張が本当に必要なら、互換性を扱う改訂として検討する。

Humanの「完了か分からない」という発言を確認できても、Task完了そのものはUnknownであり得る。異なる確かさの主張を一つのConfirmed Nodeへ混ぜない。

## 5. 返却と改善

AIは現在の依頼に必要な意味を返し、記録する場合は対象原本と差分を区別する。全欄の清書や全Unknownの解消を前提にしない。欄が多い、候補が選びにくい、何を書くか迷う等のFeedbackから、項目と見せ方を[委任範囲で改訂](../maintenance.md)できる。内部の読者設定を変える今回の版では、コピー用本文と項目名を保持する。

[共通運用](../operation.md)／[B-Gate報告](b-gate-report.md)／[改訂ガイド](../maintenance.md)

EOF::TASK_MODE_SYSTEM_TASK_REPORT::v0.2.0
