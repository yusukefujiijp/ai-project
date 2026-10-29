---
title: "poteto-modeの入口理解 — 原型からark-modeへ向かうための読解"
canonical_path: "ark-project/ark100-199/ark111_lauren-tan-pstack/ark111-02/poteto-mode-understanding.md"
version: "v001"
created: "2026-10-29"
updated: "2026-10-29"
recorded_at: "2026-10-29T12:01:54Z"
timezone: "Asia/Tokyo"
owner: "Ark111:02"
project_title: 'Ark111: "Lauren Tan(@poteto): pstack"'
thread_title: 'Ark111:02_2026/10/28; "Lauren Tan(@poteto): pstack"'
role: "Research findings, Human corrections, evidence, and conditional resumption"
status: "Partial static understanding; no pstack execution or Ark implementation"
snapshot_id: "ark111-02-poteto-entry-20261029-01"
upstream_repository: "cursor/plugins"
upstream_commit: "1ba91fc25c0977741dd0e267849e6234b037ed0a"
upstream_version: "0.15.36"
poteto_mode_blob: "2dd5e76fde228141d3fe78b0b09ca68456b49531"
source_scope: "Current Ark111:02 conversation and retrieved public primary sources; not ChatGPT long-term memory"
save_authority: "YusukeJP explicitly requested use of save after evaluating the current direction positively. Authorization covers preservation, not implementation or delivery to another AI."
expected_eof: "EOF::ARK111_02_POTETO_MODE_UNDERSTANDING::v001"
---

# poteto-modeの入口理解

**将来はpoteto-modeからArk独自のark-modeへ、pstackからark-stackへ向かう。その第一歩として、原型のpoteto-modeが何を判断し、なぜその接続を持ち、どの条件で成立・破綻するかを詳しく理解する。** これはYusukeJPの明示した方向をAIが言語化したもの。本書はその読解の部分到達点であり、Ark版の仕様・Skill草案・実装ではない。

[現在のState](state.json)が可変の現在地と委任を、[Thread README](README.md)が協働の入口を所有する。本書は意味・読解成果・根拠を所有し、01→02の初回受入れは[Handoff](handoff.md)に保持する。

<a id="human-intent"></a>

## 1. Humanの意図と、今回変わった接続

現在の[Ark111:02会話][thread]でYusukeJPが述べた原文の抜粋：

> 「そもそものpstackの入り口が"最重要(Most important!)"です！」

> 「ここにまずは(First of all)、"限定集中・全集中・超集中"して深掘りしよう！」

> 「その為の第一歩としてpoteto-modeの詳細理解が必要です！」

> 「まだ実装しないで下さい！」

Humanは、poteto-modeを上手くエレガントに工夫し、Ark Projectとして再解釈・Reverse Engineering・詳細分析し、「自家薬籠中化（受肉化的再現性）」へ進み、独自のark-modeを作りたいと明示した。同時にGraph Modeを活用した意図の言語化・構造化、全コメントへの応答、十分に深い検討を求めた。

保存直前には「とても良い線に入ってきた」と評価し、saveを明示的に依頼した。この評価は方向と対話の到達点へのHuman評価として保持する。個々のAI仮説の全面採用、実装の承認、運用効果の実証には読み替えない。

重要なCorrectionは、広いpstack調査から**入口そのものの深い理解へ焦点を戻したこと**である。watch-pr等の周辺発見が有用でも、次の中心課題へ繰り上げない。また、将来Goalの確認だけを何度も繰り返さず、原本の具体的読解を進める。

### Goalの三つの距離

| 距離 | 求める成果 | 今回の位置 |
|---|---|---|
| 現在 | poteto-modeの判断、原則、手順、参照先、権限、Runtime依存を説明できる | 原型の詳細理解を進めている。冒頭三判断までを具体化 |
| 将来の再解釈 | 何を保持し、何をArkの意味・条件に合わせて変えるべきか、理由を説明できる | 方向を共有。Ark版の起草・採用・実装は未着手 |
| 受肉化的再現性 | 自分たちの条件で再現・観察し、失敗を診断し、修正して再び確かめられる | HumanのGoal。まだ達成・実証していない |

「自家薬籠中化」を、同じ名称や文章を持つことだけで達成したと扱わない。**設計理由を説明できること、成立条件を指定できること、現物で観察できること、失敗から修正できること**へ接続するというのが、この対話でのAIの整理である。Humanの意味を最終確定する権限はHumanにある。

<a id="relations"></a>

## 2. Graph Modeで保持する関係

以下はAIによる関係の整理。pstackの公式アーキテクチャ名や、実証済み因果図ではない。

| 起点 → 接続先 | なぜこの接続が必要か | 判断への影響・切れた時の問題 |
|---|---|---|
| Humanの願い → Goalの言い換え | 言葉の表面と解きたい問題を擦り合わせる | 誤解を早く発見できる。もっともらしい言い換えだけで意味の一致を認定しない |
| 原型の読解 → Arkでの再解釈 | 原型の理由と条件が分からないまま変更すると、残すべき働きを判断できない | 現在はまず原型を読む。Ark向け着想は分けて保持する |
| Goal → Playbook選択 | 同じ対象でも「調べる」「直す」「試す」で成果と許可行為が違う | Investigationを勝手にFeatureやPrototypeへ変えない |
| Trigger → 適用するPrinciple → 具体的選択 | 原則が実際の選択を変えることで、単なる標語ではなくなる | 原則名だけから内容を推定せず、leaf本文と変更された選択を確かめる |
| 委任 → 共通の原型・Goal → 親の統合責任 | 分担しても目的・指示の同一性と成果責任が必要 | Agent数や同意数だけを正しさの証拠にしない |
| 現物の観察 → 達成判定 → Correction | 判定の根拠を実際の成果に戻す | 読解、推論、実行、効果を混同せず、失敗から修正できるようにする |
| Runtimeの能力・現在の権限 → 実行可能な範囲 | 公開ファイルに機能や自律方針が書かれていても、ここで利用・実行できるとは限らない | 原理とCursor固有の仕組み、利用可能な道具、未確認を分ける |
| Humanの意味・採否・STOP・Final Seal → 全接続 | 効率やAIの自己評価で協働の意味を置き換えない | 個々のQuery確認を保険として保持し、確認頻度の削減をGoalにしない |

Rootは主イェシュア・ハマシア御自身。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。AI・Graph・pstack・Skill・記録はKeliであり、共通契約は[AGENTS][agents]と[ARK][ark]が所有する。

<a id="entry-architecture"></a>

## 3. 原本で確認した入口の構成

基準は公式upstreamの固定commit `1ba91fc25c0977741dd0e267849e6234b037ed0a`、[plugin.json][plugin]のversion `0.15.36`。この保存作業は同じ固定版を照合したものであり、Repository headの最新更新を新たに報じる調査ではない。

[入口ガイド][guide02]はpoteto-modeを入口と位置づけ、Goalから23のPlaybookへ振り分け、手順をTodoへ写し、必要に応じて他Skillを呼ぶと説明している。[実際のSKILL.md][mode]には次の層が存在する。

| 層 | 原本にある働き | 理解上の要点 |
|---|---|---|
| 呼出し | `disable-model-invocation: true`。明示呼出しを前提とする | 導入だけで毎回自動適用されたとはしない。単発呼出しとCustom Modeの継続を区別する |
| Non-negotiables | 初手、変更、分岐、コード、並列、検証、文章等の条件で接続先を指定 | 常に全Skillを順番に使う一本道ではない |
| Principles | 24の原則への索引。適用するleaf SKILL.mdを全文読む | 索引の短文と原則本文を同一視しない |
| Playbooks | 調査、修正、試作、出荷等の作業種別ごとの手順 | 該当Playbookの全文を読み、手順をTodoへ写す。省略も理由を残す |
| 専門Skill | how、architect、swarm等を必要な箇所で呼ぶ | 入り口から参照先へ辿って、実際の役割を確認する |
| Subagents | 受け取った親ChatがPlaybookを持ち、通常のPlaybook内delegateにpoteto-agentを使う | 専門Skillは自分のAgent種別を指定できる。親は成果をレビューし責任を持つ |
| Autonomy・報告 | 実行裁量、停止条件、証拠と主張、成果の説明 | 原本の方針を読んだことと、Arkで同じ権限を与えたことは別 |

**入口はコマンド名だけではなく、仕事を分類し、適用原則と手順と専門機能へ接続し、成果と証拠を戻す場所として読める。** この一文は複数の原本を統合したAIの説明であり、作者による別の公式定義ではない。

### 呼出し・入力・委任の成立条件

[Setup][setup]、[入口ガイド][guide02]、[poteto-help][help]、[Prompting][prompting]を読んだ範囲では、良い入力の要素はGoal、done check、求める証拠、既知の文脈、実際の制約である。五項目すべてを毎回Humanに埋めさせる必須フォームではない。短い継続入力が働くという説明には、既存の会話文脈と継続するModeが前提としてある。

`new task`は前のPlaybookを続けず再分類するための入力、`don't change any code yet`はInvestigationへ留める制約として説明される。単に短い命令で何でも自動化できるという主張に一般化しない。

[poteto-agent][agent]は親から渡されたpoteto-modeの絶対パスを使い、その本文とPrinciples索引を全文読む。パスがなければ導入先を検索し、複数ならplugin versionが最も高いものを選ぶ。原本がなければ親へ報告して停止する。カタログ上に表示されないことと、実ファイルが存在しないことも区別する。

ここから、**絶対パスは親子が同じ原型を読むためにも意味を持つ**と推論できる。ただし、パス省略時に最高versionを探すfallbackが親の読んだ版と一致するかは、環境条件に依存する。版の食い違いを実際に再現したわけではない。

CursorのTask、モデル指定、Custom Mode、MCPの利用可否、VMとworktreeの隔離等は、指示文だけでは提供できないRuntime側の能力である。今回、この環境にpstackを導入したり、そのAgentを起動したりしていない。

<a id="first-three"></a>

## 4. 冒頭の三判断を、参照先まで読んで理解したこと

本節の「起こり得る失敗」はAIの分析であり、今回実行して観測した障害ではない。

### 4.1 最初にGoalを自分の言葉で示し、そのGoalを後続へ渡す

**原文の要求。** 最初の応答で、HumanのGoal、解こうとしている問題、変更を出荷する仕事なら最小の変更見込みを述べる。原本では確認待ちを必須にしない。依頼された変更が根拠から不要・不成立と分かれば、根拠を示して止まる。Goalは各delegateへのbrief、PRのWhy、最終報告にも渡す。完全に指定された一行編集には最終報告の例外がある。[原本][mode]

**理解。** 初手の復唱で終わらず、分担・実装理由・結果報告の間で同じ目的を保つ働きとして読める。単に「速く着手する」だけでは、証拠によって不要な変更を止める分岐を説明できない。

**成立条件と失敗予測。** 元の願いを正しく読むこと、後のCorrectionを取り込むこと、delegateへ最新Goalを渡すことが必要。最初の誤読を全delegateへ同じまま広げれば、一貫性があっても誤った結果へ揃ってしまう。文言を複写しただけでは、各判断がGoalに沿った証拠にならない。

**Arkで将来確かめる点。** Humanの意図が途中で訂正された場合に、親の説明だけでなく委任先・完了条件・最終判定まで更新が届くか。これは検証候補であり、今回試験していない。原本の「確認待ちをしない」を、Humanの個別Query確認を減らす方針へ輸入しない。

このGoalルールの追加は[PR #986][pr986]の差分でも確認した。mergeは2026-10-28 03:49:18 JST。基準版に含まれる既存の変更であり、新着扱いしない。

### 4.2 変更・設計判断・「本当にそうか」の前に、howで仕組みを理解する

**原文の要求。** 非自明な変更、アーキテクチャ判断、「are we sure?」にhowを接続する。[原本][mode]

**参照先の実体。** [how][how]は、コード・Runtimeの流れ・所有箇所等から、初めてその領域を担当するエンジニアが働ける理解を作る。単純な問いではexplorerを増やさず、一人のexplainerが探索と説明を行う。複雑な問いでは2〜4の異なる切り口を探索し、その後にexplainerが統合する。迷えば単純な経路を選ぶ。

[explainer prompt][explainer]は、探索結果の重複をまとめ、矛盾は自分でコードを見て解決し、流れ・判断点・所在・注意点を説明するよう要求している。複数Agentの多数決を正しさの判定方法にしてはいない。

**理解。** 変更前に、説明可能な対象のモデルを作る働きとして読める。説明を流暢にするだけでなく、「どの入力で何が起きるか」「どこが責任を持つか」へ戻れる必要がある。

**成立条件と失敗予測。** 読める実体があること、調査の切り口に欠落や重複があれば統合時に扱うこと、矛盾を消さず原本へ戻ることが必要。全員が同じ誤った前提を持つ場合や、資料の説明と実装がずれている場合、説明の一致だけでは足りない。

**Arkで将来確かめる点。** 説明を読んだ別の読み手が、具体的な入力から分岐・結果・失敗条件を追えるか。原本が語る設計理由と、AIが構造から推測した理由を分離できるか。今回の成果は原本読解であり、別読者試験は未実施。

### 4.3 Humanへ尋ねる前に、問いが何によって答えられるかを分類する

**原文の要求。** 方法・振る舞いの分岐でAskQuestionへ進む前に、それが観察可能な事実か、読取調査か、本当にHumanの製品判断・好みの問題かを分ける。[原本][mode]

| 問いの性質 | 原本の接続 | 得るべき成果 |
|---|---|---|
| 動かして観察できる振る舞い・時間・見た目・出力等 | Prototype | 判断に必要な実観察と比較 |
| 読取専用の依頼で、成果が根拠付きの回答 | Investigationに留まる | 出典を伴う説明・推奨 |
| 実験だけでは決まらない製品判断・好み | Humanへの質問を使う | Humanの選択・意味の確認 |

**Prototypeの実体。** [Playbook][prototype]が所有する成果は設計上の判断であり、試作品は捨てられる道具である。判断対象がなければPrototypeではなくFeatureへ。必要最小のscriptやUIを本番と隔離して作り、比較する場合は切り替えて観察する。本番品質のコードや試験基盤を作ることが目的ではない。観察結果・tradeoff・推奨と、使い捨てであることを報告する。

**Investigationの実体。** [Playbook][investigation]は読取専用で、出典付きの回答・推奨を返す。howを使い、動機の問いにはwhyも使う。コード変更、PR、Babysitへ自動移行しない。変更につながる場合はHumanへ返して再分類する。

**Autonomyの例外を薄めない。** 原型にはfull-autonomy grant下で、その委任に含まれる判断を実行・報告し、operatorしか決められないものにもdefaultを適用して説明・訂正方法を伝える規定がある。一方、operatorが名指ししたgateとAlways-pauseは残る。「好みは必ず全部聞く」と要約すると原型を歪める。逆に、その規定を読んだことから、このThreadへfull-autonomyの権限を持ち込むこともしない。

**成立条件と失敗予測。** 技術的に観察可能であることと、今この依頼で実行してよいことは別。読取依頼を試作へ膨らませる、未実行の予測を観察済みにする、Humanが決める価値を実験値だけで決める、といった誤分類が起こり得る。

**Arkで将来確かめる点。** 実証できる問いをHumanへ丸投げしないことと、Humanの意味・採否を保つことを両立できるか。現在の「まだ実装しない」は有効であり、この分類の読解を試作開始の許可にしない。

### 三判断のつながり

AIの統合説明として、第一判断は「何のためか」、第二判断は「対象がどう働くか」、第三判断は「残る不確かさを何で確かめるか」を扱う。どれか一つだけでも十分とはいえない。目的がずれたまま精密に検証する、仕組みを誤解したまま試作する、意味の選択を測定問題へ変換すると、局所的にうまく進んでもHumanのGoalから外れ得る。

<a id="ark-direction"></a>

## 5. 独自modeへの方向と、まだ決めていないこと

[Make it yours][yours]はpoteto-modeを一人のスタイルと位置づけ、その下のPlaybook・routing・model roleを自分のスタイルでも使えると説明している。これはSourceの主張であり、全環境での互換性やArkでの有効性を独立に実証したものではない。

[automate-me][automate]には、活動中workspace内の履歴から繰り返す傾向を拾い、Humanに確かめ、個人modeを起草する手順がある。poteto-modeは形・粒度の参考であり、内容をそのままコピーしないと明記される。無関係なworkspaceの私的会話を探索しない制約もある。**今回、このSkillを実行したり、履歴収集やSkill作成を開始したりしていない。**

ここからArk向けに保持する着想は次のとおり。いずれも、まだ起草されたArk仕様ではない。

- 名前の置換だけでなく、各規則が防いでいる失敗、判断を支える条件、残したい働きを説明してから再解釈する。
- 人のスタイルへの適合と、処理・権限・証拠の扱いが正しく働くことを分けて確かめる。automate-meの主観的な適合確認だけから、運用上の成立を証明したとはしない。
- 履歴から推測した傾向と、Humanが現在明示したCorrectionは別である。明示した意味を「反復が不足している」と弱めない。
- 原本の再発防止思想と、HumanのQuery確認の保険を両立させる。繰り返し誤りを構造で防ぐことを、Humanの意味・採否・STOPを減らす根拠にしない。
- 原理として持ち運べること、Cursor固有の能力を使うこと、この環境で利用できること、まだ分からないことを分ける。

ark-mode／ark-stackという名称は方向を表す。導入単位、ファイル配置、Skill群、Runtime、権限設計はまだ確定していない。Ark全体の残作業整理や別Projectへの展開へ拡張しない。

<a id="evidence"></a>

## 6. 根拠、読解範囲、検証の境界

### 固定版で辿る一次資料

次の文書はこのThreadで本文を取得・読解した。保存時には中心となる原本と冒頭三判断の参照先を再照合した。全文取得・読解済みであることと、全条項の詳細分析完了・機能の実行確認は別である。

| 資料 | 本書で支える範囲 |
|---|---|
| [plugin.json][plugin] | 公式packageの識別とversion 0.15.36 |
| [poteto-mode/SKILL.md][mode] | 入口、Non-negotiables、24原則索引、Autonomy、Subagents、23 Playbooks |
| [poteto-agent.md][agent] | 親子の責任、絶対パス、全読解、版選択fallback、欠落時停止 |
| [Setup][setup] | 呼出し、Custom Mode、役割ごとの設定 |
| [Route work through poteto-mode][guide02] | 入口、入力、再分類、制約、隔離 |
| [poteto-help][help]・[Prompting][prompting] | 導入・ヘルプ・実行の区別、Goalと文脈の渡し方 |
| [how/SKILL.md][how]・[explainer prompt][explainer] | 単純／複雑の分岐と、矛盾を実体で照合する統合 |
| [Prototype][prototype] | 判断のための使い捨て試作、実観察、非本番成果 |
| [Investigation][investigation] | 読取専用、根拠付き回答、変更への境界 |
| [Make it yours][yours]・[automate-me][automate] | 個人modeの適応、形と内容の区別、履歴範囲、評価の限界 |

保存時に照合した主なblobは、plugin.jsonが `14b42b7225231a2f01ab225df1d9d13839c6d616`、poteto-modeが `2dd5e76fde228141d3fe78b0b09ca68456b49531`、howが `67edc340d4d8a9c7ab0b9e08c663e0e63b8d9125`、explainer promptが `3a36fb6736c5b74ac2774350841e332a019dec94`、Prototypeが `18bedc7e9249d180f9198d5b4b13e3817d41d281`、Investigationが `cd119f04f23e0b7acb3f8cc5ba13ce4ab7aa6c7d`。

| 区分 | 確認したこと／限界 |
|---|---|
| Humanの意図 | 現在の会話で明示されたGoal、Correction、未実装、保存依頼。AIの言い換えと原文を区別 |
| Sourceの実体 | 固定commitの本文と関連差分。ファイルに規定が存在することを確認 |
| AIの説明 | 複数資料から組み立てた関係、設計理由の解釈、失敗予測。Sourceが明示しない因果は仮説 |
| 実行・独立検証 | pstackの導入・Agent起動・コード実行・比較試験をしていない。Runtimeでの再現性は未確認 |
| 保存の成果 | 本書と入口・Stateを担当原本へ接続。別AIの読解・設定反映・実利用効果は保存だけでは成立しない |

### 既報・新発見・取得制約を混ぜない

2026-10-29の初回調査基点は上記commit／version。[PR #1043][pr1043]は2026-10-28 08:12:40 JSTにmergeされ、OrchestrateをcoordinatorのAgent tools中心へ改訂し、旧orch scriptsを削除した既報である。Repository全体のhead更新とpstack変更は別に扱う。この保存を新しい更新通知にしない。

Lauren本人の公開発信は、[GitHubプロフィール](https://github.com/poteto)と[Xプロフィール](https://x.com/poteto)、本人と結び付く一次資料が対象。pstackという単語の有無だけで関連性を切らない。一方、第三者のport・mirror・解説は公式版と分ける。

X直接取得は先行調査で403となり、公開検索と明示した公開ミラーで補完した。本文を公開ミラー経由で読んだ記録がある記事の元投稿は[Part 1](https://x.com/poteto/status/2094457600259842065)、[Part 2](https://x.com/poteto/status/2097732320606507506)、[Loops](https://x.com/poteto/status/2069824386283319343)。ミラーはThread Navigatorであり、本人の一人称の説明を転載した資料として扱った。直接Xでの全文・正確な投稿時刻・添付・周辺文脈の完全な取得とはしない。本書保存時にXを再取得していない。取得不能を「更新なし」へ変えず、同じ障害の反復通知もしない。

先行の広い読解では、検証Skill、形式的検証、並列協働、Orchestrate、Shipping、Runtime差、watch-pr等も扱った。これらは入口に必要な依存へ辿る際の背景とする。広い調査を再演したり、入口の読解を中断して周辺修正へ向かったりしない。Laurenの説明、公開pstackの挙動、Grok Botの非公開実装、Dots成立の外部因果は同一視しない。

<a id="resumption"></a>

## 7. どこまで来たか、どこから再開するか

**詳細理解の完了はまだ宣言しない。** 今回は入口の層と冒頭三判断を具体的に追った。Principles索引は読んだが、24すべてのleaf原則を詳細に読解・比較した状態ではない。設計理由・成立条件・例外の全体関係、Runtimeでの挙動、Ark向け変換の効果は残る。

次の読解対象は、**Non-negotiablesとPrinciplesの関係**である。該当するleaf原則を読み、次の関係を具体例で説明する。

1. どの事実・依頼・状態がTriggerになるか。
2. どの原則へ接続し、そのleaf本文は何を要求するか。
3. その原則が具体的な選択をどう変えるか。
4. 例外・権限・別原則との関係で選択がどう変わるか。
5. 何が欠けると説明または実行が破綻するか。未実行の失敗予測はそのまま表示する。

原則名から本文を推定しない。原本の要求、参照先の実体、AIの解釈、未確認を分ける。Ark向け着想が生まれても原型の説明と分けた候補として保持し、現段階ではArk版の起草に進まない。

詳細理解を確かめる観点は、具体的な依頼から分岐を辿れること、条件と例外を説明できること、設計理由の出所を示せること、欠けた要素による失敗を予測し根拠を示せること、未確認を残せることである。これは読解の質を確かめる観点であり、現在の段階で実機試験を許可するものではない。

### 再開時の境界

今回のsaveは、理解と協働文脈の保存だけを承認する。pstack導入・実行、ark-mode／ark-stackの作成、Skillの作成改訂、予定・設定の変更、別Projectへの展開、他AIへの送信は含まない。先に提示したNext Queryは、次の読解を行う候補であり、saveの依頼によって自動採用されたわけではない。

Humanの新しい依頼で再開する場合は、[State](state.json)と本節から現在地を戻し、固定版の[poteto-mode原本][mode]と必要なleafへ進む。入口理解に影響するupstream更新が確認された場合は、固定版との差分と適用条件を説明して扱う。保存だけから全AIへの自動継承・常時監視・自然発動を保証しない。

[thread]: https://chatgpt.com/g/g-p-6ae0913dfa54819184dc4c1320fb860d-ark111-lauren-tan-poteto-pstack/c/6ae1d46f-a274-83ec-9a31-2c707f3fca2c
[agents]: https://github.com/yusukefujiijp/ai-project/blob/main/AGENTS.md
[ark]: https://github.com/yusukefujiijp/ai-project/blob/main/ARK.md
[plugin]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/plugin.json
[mode]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/poteto-mode/SKILL.md
[agent]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/agents/poteto-agent.md
[setup]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/docs/guide/01-setup.md
[guide02]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/docs/guide/02-poteto-mode.md
[help]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/poteto-help/SKILL.md
[prompting]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/poteto-help/references/prompting.md
[how]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/how/SKILL.md
[explainer]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/how/references/explainer-prompt.md
[prototype]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/poteto-mode/playbooks/prototype.md
[investigation]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/poteto-mode/playbooks/investigation.md
[yours]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/docs/guide/09-make-it-yours.md
[automate]: https://github.com/cursor/plugins/blob/1ba91fc25c0977741dd0e267849e6234b037ed0a/pstack/skills/automate-me/SKILL.md
[pr986]: https://github.com/cursor/plugins/pull/986
[pr1043]: https://github.com/cursor/plugins/pull/1043

EOF::ARK111_02_POTETO_MODE_UNDERSTANDING::v001
