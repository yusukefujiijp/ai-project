---
name: podcast-mode
description: Propose podcast themes with copyable generation requests, or create one coherent, audio-first response for manual playback. Use for Podcast Theme Mode, podcast topic selection, Podcast Mode, ポッドキャストモード, listening-content requests including former Radio Mode or ラジオモード usage, and content for an existing timed broadcast. A request to plan, edit, or troubleshoot the skill remains that task. Exclude radio-device settings, live ChatGPT Voice preparation, and audio-file production unless separately requested.
---

# Podcast Mode

Human が今聴きたいThemeを見つける支援と、応答の音声ボタンを押して聴く一続きの話の作成を担う。Themeを選別・抽出・工夫する役割を **Podcast Theme Mode** と呼び、このSkill内で扱う。既存の定時配信向けの内容も目的に合わせて構成する。考察の深さと情報の確かさを保つ。

現在の Human の目的、Plan-only、STOP、現在有効な権限を優先する。Skill自体の設計・改善・原因調査を求められた時は、その依頼へ応答し、聴取用本文の作成へすり替えない。経験の参照を新しい実行許可として扱わない。

## 今の目的から組み立てる

- Themeの提案・比較を求められたら、候補とその選択に役立つ説明を返す。候補を示すことだけで本文生成へ進まない。
- Themeが指定・選択され、本文生成を求められたら、そのまま作る。「Themeを任せて作って」も、利用できる文脈から選んで生成する。候補選択や新しい承認を必須の前工程にしない。
- 今回聴きたいこと、直前の会話、Human の関心や状況から中心を選ぶ。既知事項の再入力を求めず、判断を変える不足だけを必要時に確認する。
- 時刻、予定、現在の活動が内容を変える場合だけ、利用できる情報で確かめる。推測で現在地や生活状況を埋めない。
- 指定された長さや調子に合わせる。指定がなければ、理解に必要な深さから長さを決める。短さのために重要な理由、留保、つながりを落とさない。

## Podcast Theme Mode — 今聴く価値から提案する

- 各案で、題名、中心の問い、なぜ今そのThemeなのか、聴くと何が見えてくるかをつなぐ。知的な面白さ・驚き・理解の深まりも価値として扱い、実用や行動提案だけへ狭めない。
- 新鮮さ、AIならではの俯瞰、領域を横断する関係など、目的に効く切り口を選ぶ。新鮮さには、今の対話で生まれた問いや古い題材の新しい見方も含める。これらを固定分類・必須三案・排他的な選択肢にせず、必要なら組み合わせる。最新の外部事実が重要なら実際に確認する。
- 同じ題材でも問いと得られる理解が異なる案にする。文脈を活かしつつ、全案をArkやAI運用の話に限定しない。案数・詳しさは今回の依頼に合わせ、Humanは番号選択に加えて切り口の修正や新しい着想も返せるようにする。
- 有力な案を推薦する場合は、その理由と判断を変える条件を示す。AIの推薦をHumanの採択や、聴取効果の実証として扱わない。
- 比較の説明に加えて、各案に一つずつ、独立してコピーできる生成依頼を `text` コードブロックで添える。Humanが別形式や題名のみを明示した時は、その指定を優先する。

## 選んだ一案だけで文脈を渡せるようにする

コピー用ブロックには、そのThemeでPodcast本文を生成してほしいという依頼と、中心の問い、今聴く価値、必要な背景・Humanの重要な訂正・指定を含める。項目名や文字数の固定Templateにはしない。「上記」「③」だけに依存せず、そのブロックだけを受け取ったAIが目的を復元できる必要十分な内容にする。

- `$podcast-mode` を入口とし、登録を使えない受け手には[共有本文](https://github.com/yusukefujiijp/ai-project/blob/main/skills/podcast-mode/SKILL.md)を実際に読んで適用する経路も入れる。未作成の `$podcast-theme-mode` を登録済みの呼出しとして案内しない。
- Human報告、Sourceからの確認、AIの仮説、Unknownを意味が変わる箇所で区別する。元会話を必要な範囲で要約し、検証に必要なSourceには到達可能なURL・識別情報を渡す。全履歴の貼付や、見えない別Threadの読解・同期を前提にしない。
- 同じThreadでの生成と、別Threadへコピーしての生成の両方を選べる形にする。Themeの提案場所と本文の生成場所を固定せず、本線の継続、Thread新設、Main移行を混同しない。
- コピーは作成時点の文脈であり、後続のHuman訂正・STOPがあればそちらを優先する。適用中のRoot・権限・Guard、必須Source・Boot・全文読解条件を解除しない。実際のThread起動・移行を求められた時は、適用される[共有移行契約](https://github.com/yusukefujiijp/ai-project/blob/main/prompts/ai-next-thread-handoff.md)へ接続する。
- この受け渡しで求める成果は本文生成である。保存・送信・公開・Thread作成・予定登録への権限を付け足さない。別Threadの結果を元Threadへ戻すこともHumanの必須作業にしない。

## 耳で理解できる応答にする

以下は本文生成時に適用する。Theme提案や設計相談の画面上の比較・コピー用ブロックとは使い分ける。

- 聴き手が今から何の話を聴くのか自然に分かる入り口を作り、要点と理由をつなぎ、一つの応答として届ける。必要なら話題の切り替わりを言葉で示す。
- 表、見た目の配置、長い箇条書き、URL の読み上げに理解を依存させない。専門語や略語は必要な分だけ解きほぐす。根拠が必要な話は出典を確認し、聴く本文と両立する形で示す。
- 章数、話題数、決まった番組構成を固定しない。雑談、振り返り、解説、発想など、今回の目的に合う流れを選ぶ。
- 不確かなことを確定事項のように話さない。最後の質問、宿題、行動提案を毎回付けず、今回それが役立つ場合だけ添える。
- 本文の前後を準備報告で分断しない。音声の自動再生、録音、配信、定時実行は、このスキルの呼び出しだけで開始しない。

## 経験を必要なときに活かす

改善の相談、過去の失敗の再発防止、好みに関する判断などで役立つ場合は、[Skills の集約lessons](https://github.com/yusukefujiijp/ai-project/blob/main/skills/_references/lessons.jsonl) を参照する。旧Radio Modeの手動聴取・Audio-Firstの学びも継承し、名前だけで除外せず、今回の目的・条件に合う行を選び、lesson・sources・caveatを一緒に読む。集約は全行の一律適用を意味せず、インストール先へ固定コピーを作らない。

関連する記録だけを読み、観察、解釈、適用条件を区別する。現在の依頼・修正を過去の経験より優先する。取得できなくても、必要な現在情報がそろっていれば応答を続ける。過去の記録の確認自体が依頼の核心なら、未確認の範囲を伝える。

感想や訂正を受けたら、その場の応答に反映する。毎回の記録、公開、スキル本文の改訂を自動で行わない。保存依頼または有効な継続委任がある範囲で、対象、公開範囲、残す内容を確認し、具体的な経験と再利用できる学びを分けて適切な記録へつなぐ。

lesson の担当原本と読取・更新先は、[Skills Hub](https://github.com/yusukefujiijp/ai-project/blob/main/skills/README.md#skills-lessons)へ。形式・更新・検証には、[共有契約の第3〜5節](https://github.com/yusukefujiijp/ai-project/blob/main/agents/dots/lessons/README.md#3-全行がlesson--row-schema-2)を再利用する。契約の参照を、Dots 固有の読込義務・所有範囲・書込権限の全体移植と解釈しない。
