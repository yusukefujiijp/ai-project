---
title: Ark Shared Skills Hub
version: v0.8.1
status: experimental / Human-authorized shared skill expansion
updated: 2026-09-20
---
# Ark Shared Skills Hub

## 1. Purpose and authority

このフォルダは、Arkで育った再利用可能なSkillの共有原本・配布元です。GitHubをHubとして、各AIが必要な手順を取得できるようにします。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利です。Humanは意味・Correction・STOP・Final Sealを保持します。Skill・AI・GitHubはKeliです。

共有原本は各Skillの手順を所有します。参照先の共通契約は、その分野の成立条件を所有します。Skill導入や参照は、外部変更への承認ではありません。

## 2. Available skills

| Skill | 使用場面 | 共有原本 | 共通契約 | 検証境界 |
|---|---|---|---|---|
| Ark Transition / prepare-ark-transition | Thread継続・章移行・補助Thread再接続の計画、承認済み準備、受入れ | [SKILL.md](prepare-ark-transition/SKILL.md) | [AI Next Thread Handoff](../prompts/ai-next-thread-handoff.md) | 汎用入口と資料選択を改訂。GitHub共有・導入・読解挙動・実移行成功を別々に確認 |
| AI Living Graph Mode / analyze-living-graph | 関係・競合Benefit・Feedbackが判断を変える分析 | [SKILL.md](analyze-living-graph/SKILL.md) | 同梱referencesを必要時に参照 | 現Thread改訂本文と参照資料を保持。限定応答確認あり。別製品での再現性は未検証 |
| Agent Instruction Audit / audit-agent-instructions | Skill・AGENTS.md・Task Promptのモデル移行／過剰制約監査 | [SKILL.md](audit-agent-instructions/SKILL.md) | 同梱source-notesに記事出典と解釈境界 | 作成・導入・限定独立応答確認済み。全AI互換性は未検証 |
| Social Post Reader / read-social-post | X/Twitter・SNSの投稿URLから本文を全文取得し、調査・執筆へ接続 | [SKILL.md](read-social-post/SKILL.md) | 実行環境のBrowser・認証・取得規則 | 公開Browser取得に加え、検索・Web取得失敗後の公開HTML全文取得を観測。省略検出・本文と動画の分離を改訂。全SNS互換性は未検証 |
| Ark Markdown Writer / write-ark-markdown | Ark Markdownの作成・改訂・計画。AI読者への意味の継承と、文書の役割に応じた構成 | [SKILL.md](write-ark-markdown/SKILL.md) | 対象Runtime・近接ガイドを必要時に参照 | 形式検証・導入確認済み。架空素材で成功事例と入力ガイドの限定独立作成を確認。自動選択の実績・全AI互換性は未検証 |
| Bedtime Recall / recall-bedtime-care | 就寝前のBrainDump受付・条件訂正・自然な合図からの短い想起支援 | [SKILL.md](recall-bedtime-care/SKILL.md) | [Task Records](../formats/task-records/README.md)・[就寝前の原本案内](../task-mode-system/experience/README.md#39-就寝前に思い出したいことを復元する) | 個別希望と各回の実施を分離。自然な合図での自動選択・実生活効果は未検証 |
| BrainDump Reception / receive-braindump | 未整理の考え・報告・希望・訂正の受領と、現在必要な協働への接続 | [SKILL.md](receive-braindump/SKILL.md) | [共通運用](../task-mode-system/operation.md)・保存時は[Task Records](../formats/task-records/README.md) | 意味の保持と判断の自由を両立。確認範囲は下記の導入・応答確認記録を参照 |
| Everyday Co-design / co-design-everyday-solutions | DIY・料理・収納など、材料・道具・空間・手順を生活の条件に合う案へ具体化 | [SKILL.md](co-design-everyday-solutions/SKILL.md) | 本文単体で基本支援。適用中の目的・制約・出力契約を尊重 | 形式・導入・限定独立応答確認。品質優位・自然な自動選択・実生活効果は未実証 |

2026-09-12、Ark27:02での明示的Upload依頼により、現Threadで改訂・新規作成した二つを追加しました。初期の一件限定から、確認済みの用途に応じた三件の共有へ進めています。全Skillの自動展開はしません。

2026-09-14、URL一つからSNS投稿の全文を取得する `read-social-post` を追加しました。本文はインストール版と一致し、UI metadataは環境が自動付与するアイコン・内部設定を含まない配布用です。追加スキルは2026-09-12のexport-manifestの対象外です。

2026-09-17、`read-social-post` の早期停止を改善しました。検索や一つの取得ツールの失敗から全経路の取得不能を推定せず、許可された公開HTTP取得も検討します。[検証対象のX投稿](https://x.com/redp314/status/2100489858951073858)では、公式埋め込みAPIの本文は途中省略されましたが、公開ページHTMLの対象本文は全段落を取得できました。HTTP 200だけで全文成功とは判定しません。引用投稿の省略は対象本文と分離し、動画の403は動画未確認として保持しました。ブラウザ利用条件・アクセス拒否・Plan-only境界は維持します。改訂後、先行する結論や取得済み本文を渡さない独立AIの確認でも、同じ投稿の公開HTMLから本文3段落を取得し、モデル時間と実行全体の時間を区別できました。異なる投稿での汎化、動画、実装コードは未検証です。これは限定的な実地証拠であり、特定API・HTMLタグや全SNSでの成功保証ではありません。

2026-09-18、`write-ark-markdown` を追加しました。ArkのMarkdownを他AI・Future AIへ渡す共通入口として、文書の役割と必要な知識をAIが選びます。共通の核は短く保ち、後の重要点は共通原則・条件付き知識・経験の根拠へ分け、追加・統合・Correctionを受け入れます。注意書きの全文を各文書へ貼る仕組みではありません。小さな成功も独立した学びとして残す方針を含みます。

共有版はSKILL.mdと配布用の最小表示設定の二ファイルです。導入環境が自動付与するアイコン・内部設定は含めません。自動選択を許可する通常設定で導入し、共有本文との一致を確認しました。独立したAIへ架空のTask報告素材を渡した限定確認では、成功事例と入力ガイドを書き分け、報告成功とTask完了、Human評価と測定、任意入力と必須条件を区別できました。自動選択される頻度や実生活効果は、この確認の対象ではありません。本Skillは2026-09-12のexport-manifestの対象外です。

2026-09-18（保存作業環境のUTC日付）、`recall-bedtime-care`を追加しました。Humanが2026/09/19と記した現場報告に続く対話から、就寝前の合図で耳揉み等を想起したい希望と、項目をBrainDumpで継続追加してAIにまとめてほしいというCorrectionを受けています。方法はSkill、個別希望・根拠・訂正は[Ark27:04原本](../ark-project/ark27/ark27-04/task-records.json)が所有し、項目追加のたびにSkillを書き換える必要はありません。

一回の見送りと恒久取消し、実施報告と登録削除、設計相談と実際の就寝前の合図を区別します。出力を一回答一項目や全項目表示へ固定せず、Humanがそのまま就寝できる簡潔さを優先します。原本への到達経路と取得不能時の扱いを含み、通知・常時監視・朝の起床方法変更・成功事例登録は含みません。共有版はSKILL.mdと最小の表示・自動選択設定です。自動選択を許可する設定と、実際に合図から自動選択されたという観測は別です。

限定的な独立応答確認では、元会話を渡さず、作成したSkill本文・選択読解可能な04原本・七つの仮想入力だけを別AIへ渡しました。昼の追加と条件変更、就寝合図、日付を跨ぐ同じ就寝機会の実施済み・見送り、恒久取消し、STOP、合図の設計相談、原本取得不能時の現在入力からの支援を区別できました。初期三項目とHuman CorrectionのNode／Sourceを辿れ、サプリ服用不明から再摂取を促さず、架空の鍵の項目を実際のArk履歴へ混入しませんでした。これはローカルに渡した原本からの限定応答確認であり、遠隔取得経路、自動選択、保存更新の動作、全AI互換性、実生活効果の検証ではありません。

形式検査と導入先の保存確認を完了しました。導入先のSKILL.mdは共有する本文と一致し、通常の自動選択を許可しています。導入環境が付加するアイコン・内部表示設定は共有版へ含めません。2026-09-12のexport-manifestは当時の輸出記録として保持し、本Skillを収録済みとは扱いません。

2026-09-19、`receive-braindump`を追加しました。Humanが繰り返しているBrainDump／GTD的BrainStormingを、未整理のまま預けられる共通入口として共有するためです。高性能なAIへ固定手順を重ねる懸念も保持し、受領の意味と重要な境界を明確にしながら、整理方法・説明密度・関係探索・次の接続はAIが現在の内容から判断します。[共通運用](../task-mode-system/operation.md)にある方針を活かし、第二のTask管理基盤を作りません。

観察と仮説、希望と実施、見送りと取消し、設計相談と現在の合図、会話での受領と永続保存を区別します。未接続の議題や競合するBenefitを保持し、全項目のTask化や統一結論を強制しません。Task支援・関係分析・就寝前想起・保存へ必要時に接続します。個別の生活項目や今回限りの経験はSkill本文へ蓄積しません。

元会話を渡さないAIにSkill本文と六つの相談例を渡した限定応答確認では、利用枠表示と課金原因の仮説、眠い時の受領だけの依頼、見送りへの訂正と想起希望、引用を含むTrigger設計、承認された一文の書換え、STOPを区別できました。比較用にSkill本文を渡さなかった別AIも、同じ相談で重要な区別を維持しました。この一回の比較では回答品質の優位性やトークン効率の改善を実証していません。Skillを渡した側の応答確認も、実環境の自動選択や保存更新の動作確認ではありません。

共有版はSKILL.mdと最小の表示設定です。形式検査・参照先確認・導入先の保存確認を行い、共有するSKILL.md本文との一致を確認しました。通常の自動選択を許可しますが、実際の自然な合図からの自動選択、全AIでの互換性、実生活での負担軽減は未観測です。2026-09-12のexport-manifestは当時の記録として保持し、本Skillを含めません。

2026-09-19、`co-design-everyday-solutions`（暮らしの工夫・共同設計）を追加しました。100均DIYから料理・収納へ広がった対話を受け、材料・道具・空間・準備から片付けまでの条件を、選べる具体案へ結び付ける役割に絞っています。一般的な相談受付やTask管理は既存の役割へ残し、`solve-with-human`の新設保留を覆す汎用問題解決スキルにはしていません。

共有する判断は、個別条件の尊重、実用上の成立条件、意味のある比較、条件を見直した横展開、根拠と結果の区別です。100均・特定寸法・提案数・手順順序・出力形式を全場面へ固定せず、Future AIがより適した方法へ組み替えられるようにしています。本文と最小の表示設定だけで構成し、日常の記録や添付の表示Runtimeは複製しません。

元会話や期待回答を渡さない独立AIに、収納から料理への条件切替、工作と料理の共通負担の探索、洗濯への応用、未報告の結果、単位換算の五つの仮想相談を提示しました。具体案と条件を結び付け、食品用と工作用の道具を区別し、探索段階を保ち、評価と実施結果を分け、答えだけの指定にも応じました。比較用のSkill本文を渡さないAIも主要な条件を維持しました。この限定比較は、回答品質の優位性、全AIへの汎化、自然な自動選択、現物の有効性を実証していません。

形式検証と導入先の保存確認を完了し、共有本文との一致を確認しています。通常の自動選択を許可します。2026-09-12のexport-manifestは当時の記録として保持し、本Skillを含めません。

## 3. Mobile / explicit entry

次の一つのPromptを、Thread継続・章移行・補助Thread再接続、および他Projectでの文脈継承に使います。種類・Source・Targetは既知のContextから解決し、未提示で判断に必要な情報だけを補います。新しいProjectの目的を旧Missionから自動継承しません。

### Copy & Paste — Transition Plan

```text
prepare-ark-transition（Ark Transition）を使用し、今回の移行準備をPlan Modeで進めてください。

種類・移行元・移行先・目的・承認範囲はCurrent Contextから確認し、確定事項を再利用してください。Human確認済み・AI提案・Unknownを区別し、重要な未確定事項だけを確認してください。

SKILL.mdと次の共通契約のCurrent版を確認し、各資料に宣言された全文読解・Identity・Exact EOF・Binding条件を守ってください。
https://github.com/yusukefujiijp/ai-project/blob/main/prompts/ai-next-thread-handoff.md

確認済みの全文読解記録は、共通契約の同一性条件を満たす場合に再利用してください。取得・表示が切れた場合は未読位置から続け、Gapを残さないでください。Skillを利用できない環境では、共通契約を直接読解して適用してください。

整理整頓→レイヤー構造→構造化→interface化。
interface: 今回の移行準備計画。
これは固定の思考手順や出力Templateではありません。分析方法・構成・説明密度は、今回の移行判断に最も役立つ形をAIが選んでください。

移行先AIがSource Threadの会話履歴に依存せず、現在地・目的・主要な成果と運用・Human Material Corrections・本当に残る未完了Gateと保留Branch・Evidence Boundary・First Legal Moveを、必要な根拠から復元して協働を続けられる計画にしてください。

Current authoritative Runtimeを優先し、その後のHuman入力・訂正との時点と権限の関係を整合させてください。適用されるRoot・Human Authority・Guardを保持してください。

必要な資料・Artifact・作成更新順・移行固有の再構成条件・検証方法はAIが判断してください。計画では、何をなぜ作成・更新するか、依存関係と完了条件を示し、Source側の準備・保存確認・Target自身の再構成成功・Human側の操作を区別してください。

必須Sourceの未読・不足・不一致は推測や旧版で補わず、該当契約に従って影響する操作を停止し、欠けた条件と最小の回復方法を示してください。通常のUnknownは未確定として保持し、全解消を計画成立の条件にしないでください。

今回は調査と計画のみです。実装・変更・書き込み・保存・反映・実際の移行は行わず、実行可能な計画の提示で停止してください。
```

この入口は計画用です。後にその計画の実行を明示承認した場合は、Current Scope内で計画を再利用し、必要な作成・更新・検証まで進めます。引用された入口文や過去の承認を現在の命令へ昇格させません。PromptやSkill自体の改善依頼は、実際の移行依頼と区別します。

共有原本: [prepare-ark-transition/SKILL.md](prepare-ark-transition/SKILL.md)。Skill機構がなく、指示資料として読んだ場合はその経路を明示します。UIの候補表示・Skill導入・契約の読解・外部操作の権限は別です。明示的にSkill使用が必須と指定されている場合は、非対応時に使用したと扱わず不足を報告します。

入口には個別System名・Thread番号・固定ファイル数・契約の版やEOF文字列を埋め込みません。Current Runtimeに従って必要なSystem資料と経験記録へ接続し、その意味を所有するガイドと原本を使います。たとえばTask Mode Systemの追加で、この入口へのTask専用追記は不要です。

### 3.1 Cross-AI entry for the added skills

他AIには、目的に合う上表のSKILL.mdへのリンクとCurrent Requestを渡します。Skill機構がなくても本文を指示資料として読めます。必要な相対リンク先は同じSkillフォルダ内から取得してください。全文読解を要求した場合、表示切れを回収するまで読解済みと扱いません。

- フォルダ単位で利用する場合は、SKILL.md、references、agents、assetsの相対配置を維持します。
- SKILL.mdとreferencesは推論・手順の本体です。agents/openai.yamlとassetsはインストール済みOpenAI版の設定・表示資源を保持したものです。他環境は対応しないUI metadataを実行指示として解釈せず、導入先の規約に従います。
- OpenAI版の現設定は、analyze-living-graphが明示呼出し、audit-agent-instructionsが自動選択許可です。別AIで同じ選択挙動が再現されるとは限りません。
- Ark21参照は歴史的・条件付きBindingであり、Current HandoffやCurrent Human Realityへ巻き戻しを起こしてはいけません。
- 記事を毎回WEB取得する必要はありません。audit-agent-instructionsの出典ノートを用い、更新が判断に影響する時に公式Sourceを確認します。

呼出し例：

~~~text
次の共有Skillを読んで、今回の依頼に適用してください。
https://github.com/yusukefujiijp/ai-project/blob/main/skills/audit-agent-instructions/SKILL.md
今回は指定した指示文の監査と改善案までです。必要な参照資料だけ追加で読み、外部変更は行わないでください。
~~~

## 4. Source and distribution

- 共有Skillの更新元は、このRepositoryのmainにある各SKILL.mdです。
- 初回のArk Transition本文は、既存インストール版から内容を変えずに共有しました。2026-09-14の改訂対象は共有本文・計画用入口・導入済み版であり、自動同期は行いません。反映状況は実際の再取得と本文比較で確認します。
- 配布先へ取り込む際は、取得元のRepository・path・commitまたはblob SHAを記録し、実際の本文を比較してください。mainは更新されるため、URLだけでは取り込んだ版を特定できません。
- 配布先で改善が生じた場合は、共有原本との差分をReviewし、承認範囲で原本へ反映してから再配布します。無条件の双方向同期はしません。
- 共通契約はSkill本文へ複製しません。Ark TransitionはCurrent mainの契約を読む設計なので、Skill単独のSHAだけで実行全体の再現性を保証しません。実行時に読んだ契約の版・識別情報も保持します。
- 各AIへの導入場所、UI metadata、認証、利用可能な道具は環境側で扱います。GitHub保存はインストール・自動発動・全AI互換性の証明ではありません。

### 4.1 Backup and restoration

今回の二Skillは、承認されたインストール済み版の全ファイルを内容変更なしで取り込みました。[export-manifest.json](export-manifest.json)に各ファイルのSHA-256と出典・検証範囲を記録しています。内部Skill ID、認証情報、会話全履歴は配布に不要なため記録しません。

復元時は、対象のGitHub commitを固定してSkillフォルダを取得し、manifestの各SHA-256と照合してから、導入先の正規Skillインストール手順を使います。GitHub保存だけで別環境へ導入されたとは扱いません。Skillのファイルを戻すことと、モデル内部状態や会話Contextを戻すことは別です。

以後、共有原本とインストール版の差分を確認してから、承認Scopeで反映します。manifestは2026-09-12時点の輸出記録であり、将来ファイルを更新した場合は該当hashと記録も更新します。自動的な双方向同期はありません。

2026-09-14のArk Transition改訂は、ツール改善と実移行の入口を分け、Current Runtimeから重要な運用Systemの資料へ必要時に接続する案内を補いました。共通移行契約の本文・名前・既存Handoffは変更せず、汎用の計画用Promptを第3節へ集約しています。検証で使う説明用ケースを実際のTask実績や全AI互換性の証明にしません。

2026-09-20、Ark27:04でのHuman承認により、第3節の計画用Promptを改訂しました。共通契約にある全文読解記録の再利用条件、資料ごとの宣言条件、Human確認済み・AI提案・Unknown、未完了Gateと保留Branch、停止範囲と最小回復方法を入口でも明確にしています。構造化を固定Templateにせず、Source準備・保存確認・Target再構成・Human操作を分ける方針を保持しました。変更はこのHubの呼出しPrompt・版情報・改訂理由に限定し、共通契約とSkill本文の改訂、Skillの再導入、実際の移行やTarget Bootを含みません。

## 5. Validation and growth

区別する状態は、共有原本の保存、Remote再取得確認、各環境への導入、実際の振る舞いの確認です。結果を観察していない段階を成功へ昇格させません。

次の実利用では、正しい対象・契約を読めるか、Plan限定とSTOPを守るか、取得不能を正しく報告するかを確認します。このREADMEを読んだだけで移行や試験を自動開始しません。

各Skillは必要なSKILL.mdから始め、scripts・references・assetsは具体的な必要がある場合だけ追加します。Current Missionに不要な全Skill読込、全PromptのSkill化、全履歴の複製は行いません。

### 5.1 Future AIへの開放性とSkill追加の判断

Skillは、Humanの意図、領域固有の知識、必要な根拠・訂正・境界を次のAIへ渡すために使います。現在のAIが使った手順、章数、思考法、最後の質問を、全場面の必須工程にしません。判断方法はCurrent Requestと現実に合わせて改良でき、不要になった指示は統合・簡素化・廃止を検討できます。一方、明示された読解契約、出典、Schema、権限、Human Correction・STOP・Seal、適用Guardは方法の裁量と別に保持します。高性能なモデルを使うこと自体は、追加権限や実証の根拠ではありません。

追加・改訂時は、[audit-agent-instructions](audit-agent-instructions/SKILL.md)で、どの繰り返す不都合を改善するか、既存の入口と何が違うか、追加Contextや誤起動が利益を上回らないかを必要な範囲で確認します。一般的な問題解決能力を説明し直すだけなら独立Skillを増やさず、共通運用へ置く選択もあります。毎回全Skillを監査する指示ではありません。背景は[04経験原本](../ark-project/ark27/ark27-04/task-records.json)の `future-ai-skill-discretion` とSource `work-s03`–`work-s05`です。

2026-09-19、問題解決Skill候補 `solve-with-human` は独立追加を保留し、[共通運用](../task-mode-system/operation.md)へ協働の目的と複数問題同時解決の探索を統合しました。既存のBrainDump受付、Living Graph、Task Mode Systemと候補の責務が重なるためです。候補の主要な指針は、現在の難所と既存成果を読む、未報告を成否に変換しない、キリ待ちの依存を見直す、複数Benefitを探索する、今有効な接続を選び固定手順を課さない、という内容でした。候補を作成・インストール済みとは扱いません。

共通運用の改訂案だけを渡したAIと、同じ案に候補指針を加えたAIへ、元会話や期待回答を渡さず四つの独立した仮想相談を提示しました。両者とも、①順調な生活報告を保持した外出のキリ待ち、②眠い時の言語化だけ・追加質問なし、③掃除と音声AI併用のBenefitと注意の競合をPlanだけで比較、④Skill設計相談で固定の一問題・五段階・最後の一問を一律化しない、という区別を維持しました。回答の表現は異なり、この限定比較で独立Skillの追加効果は確認できませんでした。自動選択・保存更新・実生活効果・他モデルへの汎化は未検証であり、独立Skillが常に不要という証明ではありません。

今後、共通運用へ辿り着けない、同じ誤読が繰り返す、独立したTriggerや専用知識が必要になる等の具体的な不足が見つかった時に、この候補を再検討します。新しいSkillや次Trialをこの記録だけで自動開始しません。

## 6. Repository entry relation

[AGENTS.md](../AGENTS.md)はRepository全体の行動境界、[ARK.md](../ARK.md)はIdentityを保持します。このREADMEは共有Skillの入口です。

2026-09-10の整備前、両文書が参照していた `_skill/SKILL.md` は取得不能でした。今回の入口修正は新しい共有Hubへの案内であり、旧Skill群の内容移植や旧挙動の復元を意味しません。

EOF::ARK_SHARED_SKILLS_HUB::v0.8.1
