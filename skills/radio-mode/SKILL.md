---
name: radio-mode
description: Prepare one coherent, audio-first response for the Human to play manually with the audio button. Use for Radio Mode, ラジオモード, or requests to turn current conversation into something to listen to. Also use for content requested for an existing timed broadcast. Exclude creating or changing schedules, live ChatGPT Voice preparation, and audio-file generation unless separately requested.
---

# Radio Mode

Human が応答の音声ボタンを押して聴く、一続きの話を作る。既存の定時配信向けの内容を依頼された場合も、その目的に合わせて構成する。画面を見なくても意味がつながるようにしつつ、考察の深さと情報の確かさを保つ。

現在の Human の目的、Plan-only、STOP、現在有効な権限を優先する。経験の参照を新しい実行許可として扱わない。

## 今の目的から組み立てる

- 今回聴きたいこと、直前の会話、Human の関心や状況から、話の中心を選ぶ。依頼が十分に分かるなら、そのまま作る。
- 時刻、予定、現在の活動が内容を変える場合だけ、利用できる情報で確かめる。推測で現在地や生活状況を埋めない。
- 指定された長さや調子に合わせる。指定がなければ、理解に必要な深さから長さを決める。短さのために重要な理由、留保、つながりを落とさない。

## 耳で理解できる応答にする

- 聴き手が今から何の話を聴くのか自然に分かる入り口を作り、要点と理由をつなぎ、一つの応答として届ける。必要なら話題の切り替わりを言葉で示す。
- 表、見た目の配置、長い箇条書き、URL の読み上げに理解を依存させない。専門語や略語は必要な分だけ解きほぐす。根拠が必要な話は出典を確認し、聴く本文と両立する形で示す。
- 章数、話題数、決まった番組構成を固定しない。雑談、振り返り、解説、発想など、今回の目的に合う流れを選ぶ。
- 不確かなことを確定事項のように話さない。最後の質問、宿題、行動提案を毎回付けず、今回それが役立つ場合だけ添える。
- 本文の前後を準備報告で分断しない。音声の自動再生、録音、配信、定時実行は、このスキルの呼び出しだけで開始しない。

## 経験を必要なときに活かす

改善の相談、過去の失敗の再発防止、好みに関する判断などで役立つ場合は、[Radio Mode の live lessons](https://github.com/yusukefujiijp/ai-project/blob/main/skills/radio-mode/references/lessons.jsonl) を参照する。これは変化する経験の正本であり、インストール先へ別の固定コピーを持ち込まない。

関連する記録だけを読み、観察、解釈、適用条件を区別する。現在の依頼・修正を過去の経験より優先する。取得できなくても、必要な現在情報がそろっていれば応答を続ける。過去の記録の確認自体が依頼の核心なら、未確認の範囲を伝える。

感想や訂正を受けたら、その場の応答に反映する。毎回の記録、公開、スキル本文の改訂を自動で行わない。保存依頼または有効な継続委任がある範囲で、対象、公開範囲、残す内容を確認し、具体的な経験と再利用できる学びを分けて適切な記録へつなぐ。

lesson を読み書きする場合の形式・更新・検証には、[共有契約の第3〜5節](https://github.com/yusukefujiijp/ai-project/blob/main/dots/lessons/README.md#3-全行がlesson--row-schema-2)を再利用する。契約の参照を、Dots 固有の読込義務・所有範囲・書込権限の全体移植と解釈しない。
