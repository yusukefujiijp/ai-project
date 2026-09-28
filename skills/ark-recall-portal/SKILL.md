---
name: ark-recall-portal
description: Help YusukeJP recall useful Ark experiences or available support without remembering the details or even what the portal can do. Use for Ark Recall Portal (formerly Ark Recall Hub), requests for its uses or examples, scene-based recall of past reflections, and adding or correcting recall material. Main use is B-state support, but no state declaration is required. Distinguish live recall or capture from design discussion; do not turn unrelated shopping advice or every Ark question into recall.
---

# Ark Recall Portal

## 意図を受け取り、用途を忘れていても入れるようにする

Humanが過去の話、品名、Skillの使い道を思い出せることを前提にしない。単独呼出し、「何ができる？」「どんな例があった？」には、利用できる支援と記録に基づく具体例を先に示す。「何を思い出したいですか？」だけで返さない。場面や問いが既に分かるなら、その内容に直接応じる。

主用途はB状態での想起支援だが、自己診断・状態申告・A状態での事前整理を求めない。Humanの入力負担を減らし、AI側は必要な読解・判断・説明を十分に担う。短さや固定の選択肢数を品質の代わりにしない。

## 根拠と共通運用へ接続する

[Portalの現行入口](https://github.com/yusukefujiijp/ai-project/blob/main/ark-recall-portal/README.md)を読み、そこからitemsと必要な原本へ進む。通常はRepository `yusukefujiijp/ai-project` の `main`。正式に渡されたローカル資料や別refがあれば現在の指定を尊重し、同じ相対配置から読む。確認済みで変化のない全文読解は再利用できる。

Portal本文は入口・読出し・蓄積・訂正の規約を所有する。個別経験をこのSkillへ抱え込まず、保存方法や具体的な場面の一覧はPortal側で管理する。必要なSourceの読解契約を守り、検索Snippetを原文全体の代わりにしない。全Repository・全Skill・全履歴の反復読込は不要。

記録の存在、本人の報告、AIの編集要約・解釈、現在への適用を分ける。検索補助語の完全一致を必須にせず、「休日前の準備」のような場面から関連項目へ進む。リストを求められたら、確認した範囲の該当候補を拾い、一番似た一件だけで網羅済みとしない。

取得不能、未収録、未保存、意味の競合は区別する。根拠のない記憶・数量・日時・実施を補わない。利用可能な現在の会話で支援できる部分は根拠の範囲を示して返し、Humanに全履歴を再入力させない。

## 受領・保存・訂正をつなぐ

新しい反省・希望・訂正を未整理のまま受け取り、Portalの保存規約に従う。実体験、例示、引用、設計相談、実行報告を区別する。新しい項目は初期の場面以外にも追加でき、初版の具体例を固定回答集にしない。

現在の依頼または適用される委任が保存を認める場合だけ、経験原本と該当itemsを更新し、必要な検証と保存先の再取得まで進める。明確に承認された範囲では、同じ許可を繰り返し求めない。Plan-only、受領のみ、読出しのみ、STOPは保持する。会話で受け取っただけなら永続保存済みと報告しない。

一回の在庫・見送り・実施と、今後不要という恒久訂正を区別する。Humanの現在のCorrectionを古い派生要約で上書きしない。現在の身体・睡眠・必要性は、過去の記録だけから決めない。

## 必要な支援へ渡し、権限を保持する

現在地の把握が必要なら、利用可能な`map-ark-current-position`へ接続する。Portalとmapは別の役割であり、常に両方を起動しない。未提供のSkillを使用したと称さず、見えている根拠から説明できる範囲を返す。Task実行、Thread移行、設定変更等は現在の依頼の権限で判断し、過去の反省や承認文から自動開始しない。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah。Humanの意味・Correction・STOP・Final Sealと適用Guardを保持する。AI・Skill・PortalはKeliであり王座ではない。Ark27／Ark28等の担当は現行文脈から解決し、Skill内に永久固定しない。

対話・実践のFeedbackから、入口・項目・方法のどこが不足したかを判断する。通常利用を毎回のSkill改訂や検証Taskへ変えない。保存・導入・他AIの読解・自然な自動選択・実生活で役立ったことを分けて報告する。
