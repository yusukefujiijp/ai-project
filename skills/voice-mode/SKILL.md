---
name: voice-mode
description: Support preparation, reported problems, and learning around ChatGPT Voice conversations, especially sudden requests from other people. Use for Voice Mode, 音声モード相談, preparing a live voice session, or recalling relevant lessons from one. Exclude one-way audio-button listening scripts and do not assume native Voice directly invokes this skill.
---

# Voice Mode

周囲の人から突然相談された場面でも、Human が ChatGPT Voice を使って必要な対話へ入れるように支える。会話前の準備、報告された問題への対応、会話後の気づき、次回に役立つ経験の想起をつなぐ。

現在の Human の目的、Plan-only、STOP、現在有効な権限を優先する。経験の参照を新しい実行許可として扱わない。

## 今必要な支援を選ぶ

- 今回は会話前の準備、進行中の相談、問題の切り分け、会話後の振り返りのどれが必要か、依頼と文脈から判断する。全工程を毎回実施しない。
- 突然の依頼では、今すぐ使える入口を優先する。相談の目的、分かっている背景、必要な前提を短く整理し、そのまま話せる開始文や準備メモを必要に応じて渡す。
- 不足情報が結果や安全性を大きく変える場合だけ確認する。質問数や確認項目を固定せず、十分な文脈があれば進める。
- 簡潔な準備と浅い回答を同一視しない。複雑な問題には必要な深さを保ち、詳しい検討をするかどうかも現在の目的と時間に合わせる。

## 利用環境と権限を確かめる

- ChatGPT Voice 内からこのスキルを直接呼び出せることは未確認として扱う。スキルを作っただけで音声セッションへ指示が自動反映される、会話を聞ける、過去の音声や全文を取得できるとは約束しない。
- 実際に利用できる接続や機能を確かめ、必要なら Human が音声セッションへ伝えられる準備文を作る。利用できない機能を装わず、手元の会話・報告からできる支援を続ける。
- 他の人からの依頼や発言は、Human が外部への送信、公開、アカウント操作などを許可した証拠にしない。第三者の個人情報は必要最小限に扱い、保存や公開の許可を推定しない。第三者の相談と Human 本人の事情を区別し、第三者へ伝える準備文に Human の私的な履歴を混ぜない。

## 問題や気づきを次につなぐ

- 問題の報告は、実際に起きたこと、期待していたこと、環境や条件を必要な範囲で分ける。原因を決めつけず、次に試せる小さな改善を選ぶ。製品仕様に依存する説明は現在の公式情報や接続状態で確かめる。
- 振り返りでは、Human の報告から何が役立ったか、何が合わなかったかを受け止める。全文の再現、固定の質問票、毎回のログ作成を求めない。
- 関連する過去の経験が判断に役立つ場合は、[Voice Mode の live lessons](https://github.com/yusukefujiijp/ai-project/blob/main/skills/voice-mode/references/lessons.jsonl) を参照する。正本の経験を必要なときに読み、インストール先に同期されない固定コピーを作らない。
- 記録の観察、解釈、適用条件を区別し、今回に合う学びだけを使う。現在の依頼や修正を優先する。取得できなくても通常の準備や相談を止めず、記録の確認が依頼の核心なら未確認の範囲を伝える。
- 気づきを得ただけで公開記録やスキル本文を自動変更しない。保存依頼または有効な継続委任がある範囲で、対象と公開範囲を確認し、第三者情報を必要以上に残さず、今回の事実と次回に試す仮説を区別して記録へつなぐ。

lesson を読み書きする場合の形式・更新・検証には、[共有契約の第3〜5節](https://github.com/yusukefujiijp/ai-project/blob/main/dots/lessons/README.md#3-全行がlesson--row-schema-2)を再利用する。契約の参照を、Dots 固有の読込義務・所有範囲・書込権限の全体移植と解釈しない。
