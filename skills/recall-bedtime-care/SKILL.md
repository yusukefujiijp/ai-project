---
name: recall-bedtime-care
description: Capture, revise, and recall things the Human wants to remember before sleep. Use for bedtime-related BrainDump, reminders requested for a bedtime cue, current cues such as 「そろそろ寝る」, and related completion or skip reports. Distinguish item registration, design discussion, quotations, and an actual bedtime cue; do not start bedtime guidance from keywords alone.
---

# Bedtime Recall / 就寝前リコール

## 目的と境界

Humanが思いついた時に短いBrainDumpを預け、就寝前の自然な合図から、その時に役立つ短い案内を受け取れるようにする。整理・参照・訂正・保存状況の確認はAIが引き受け、Humanに分類や原本管理を求めない。項目を増やすことより、必要なことを思い出して就寝へ進めることを目指す。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・Skill・記録はKeliとして扱い、Humanの意味・優先順位・身体Reality・Correction・STOP・Final SealとBody／Sleep／Safety／Medical等のGuardを保持する。信仰状態や主の御心を認定しない。

現在のHost・Human指示と適用Runtimeに従う。スキルの呼出しは外部変更への追加権限ではない。Plan-onlyでは調査・設計までとし、保存しない。スキルが依頼を受けて働くことと、時刻通知・常時監視・別会話への自動配信を区別する。自動通知が必要なら、利用可能な専用機能と現在の承認を確認して別途扱う。

## 入力の意味を読む

自然な言葉と現在の文脈から、追加・条件変更・取消し・今回の見送り・実施報告・就寝前の合図・設計相談を読み分ける。一つの入力に複数の意味があってよい。既知の内容を再入力させず、必要なら判断を変える不足だけを短く確認する。

- 日中の「寝る前に耳揉みも思い出させて」は登録希望として受け取り、その場で実行を促さない。朝の散歩など、その時のHumanの主題を保つ。
- 「そろそろ寝る」は現在の合図として扱える。「『そろそろ寝る』をTriggerにする設計を考えたい」や引用中の合図は、その場の就寝報告にしない。
- 「今夜はやらない」は今回の就寝での見送り。「今後は外して」は継続的な取消し。期間・対象を混ぜず、曖昧さが重要なら確認する。
- 「耳揉みは済んだ」は今回の実施報告。登録削除や毎晩の完了を意味しない。日付の切替だけで同じ就寝機会の実施済み・見送りをリセットせず、新しい就寝機会へも自動転用しない。
- 「もう寝る、終了」やSTOPは閉じる意図を優先し、残りの項目・追質問・新Taskを出し続けない。沈黙を完了・同意・失敗に変えない。

## 必要な個別情報へ到達する

方法は本Skill、個別の希望・条件・理由・訂正・実施報告は経験原本が所有する。耳揉み等の固定リストを本Skillへ埋め込まない。

Arkでの保存先は repository `yusukefujiijp/ai-project`、ref `main`。初回や文脈欠落時は、[経験索引の就寝前想起の項](https://github.com/yusukefujiijp/ai-project/blob/main/task-mode-system/experience/README.md#39-就寝前に思い出したいことを復元する)から該当する原本へ進む。初期原本は[Ark27:04 Task Records](https://github.com/yusukefujiijp/ai-project/blob/main/ark-project/ark27/ark27-04/task-records.json)。関係するNodeだけでなく、そのSource・条件・訂正・Unknownまで必要な範囲で読む。索引は原本の代替ではなく、新しい原本や訂正先への案内でもある。

同じContextで確認済みの内容は再利用し、新しいHuman入力を優先する。更新時・版の不一致・文脈欠落時にはCurrent原本を確認する。毎回全記録・全理論・全Bootを読み直さず、今の案内を変える情報が揃えば読取を閉じる。Current Runtimeの必須読解条件は省略しない。

取得できない時は、その範囲を短く示し、現在の会話で確認できる内容から支援する。取得不能を登録ゼロとせず、未読の個人項目を推測で補わない。特定原本の取得が適用契約で必須なら、影響する操作はそのFailure Contractに従う。資料不足の回復を、眠いHumanへの全リスト再提出要求にしない。

## 合図から短く返す

登録項目を毎晩すべて行う義務に変えない。Humanが示した優先順位・今回の希望・身体状態・実施済み・見送り・適用条件を合わせ、今必要なものを選ぶ。案内しなかった項目は削除せず、未知の実施も補わない。就寝を遅らせる追加Taskや対話の連鎖を作らない。

一手が適切なら一手、短い一覧が使いやすいなら一覧、全体確認を求められたら全体を示す。一回答一項目や全項目表示を固定せず、重要な未確認を隠さない。各項目の完了返信を必須にせず、読んだ後そのまま就寝できるようにする。Humanが深い検討を求めた場合は説明できるが、通常の合図へ長い理論・台帳・検証状況を返さない。

登録希望・本人が感じるBenefit・効果の実証を分ける。未提示の手順、回数、時間、医学的効果を作らない。サプリ等は種類・表示上の用法・服用状況が分からないまま摂取や再摂取を促さない。必要な具体的判断を行う時に根拠・条件を確認し、通常の項目想起まで未知情報の全解消を待たせない。

## 追加・Correctionと保存

追加する時は「何を」「なぜ」「どの場面・条件で」を分かる範囲で保持する。未指定の頻度・順序・手順を必須にせず、似た項目は意味を失わない範囲で統合する。本人の原文・重要な訂正・未確認とAIの解釈を区別し、Confirmed／Candidate／Unknownを対応させる。

保存を行う場合は[Task Recordsガイド](https://github.com/yusukefujiijp/ai-project/blob/main/formats/task-records/README.md)と[System保守](https://github.com/yusukefujiijp/ai-project/blob/main/task-mode-system/maintenance.md)を必要な範囲で使う。Task Modeは現場支援、Task Recordsは根拠のある記録、Task Mode Systemは読解・記録・次の現場への再接続を担う。

継続的な希望は`practice_statement`等、その回の出来事は`task`や`observation`等で区別し、登録希望に完了状態を付けない。新しい出来事は発言元Threadの原本へ、過去経験の補足・訂正は既存規則に従い報告元原本へ、新しいSourceとともに残す。後続Threadで新しい適用方針や取消しが生じた場合は、旧時点を保持し、原本間の関係と現在読むべき範囲を索引から辿れるようにする。自己流のTask Schemaや第二の可変状態原本を作らない。

保存権限は現在の依頼と確認済みの継続委任から判断する。承認範囲の追加・訂正には同じ許可を取り直さず、読み直し・競合確認・必要な検証・保存先の再取得まで完了する。就寝時の支援を不要な保守作業で遅らせず、会話での受領、永続保存、保存待ち・取得不能を区別する。保存に失敗したら成功を装わず、未保存範囲を簡潔に伝える。

個別情報を保存しても、ThreadのREADME／handoff／stateやスキル本体を更新したことにはならない。項目の追加だけでスキルを改訂せず、再利用する判断が変わる時だけ本Skillを改善する。Skill作成・導入・限定的な応答確認・実生活で思い出せたこと・身体上の効果を別々に扱う。
