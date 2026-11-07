---
title: "Ark114:01 → Ark114:02 Wiki continuation handoff"
handoff_id: "ARK114_02_HANDOFF"
canonical_path: "ark-project/ark100-199/ark114_harness/ark114-02/handoff.md"
version: "v001-human-authorized"
created: "2026-11-07"
source: "Ark114:01"
target: "Ark114:02"
owner: "Ark114:02"
transition_kind: "THREAD_CONTINUE"
role: "WIKI_PEOPLE_CONTINUATION"
project_name: "Ark114_2026/11/03: Ark-Wiki系"
compiled_title: 'Ark114:02_2026/11/03; "Wiki: People構築"'
source_harvest_commit: "c55d136ab7f7b0b82bdc68ecea16919f621784c2"
source_harvest_blob: "4da93b881c26245e9f6c92e2086b043fb03faa72"
expected_eof: "EOF::ARK114_02_HANDOFF::v001"
---

# 1. Purpose・委任と互換境界

Humanは01→02の継続を、原本整備・main保存・再取得、既存Project内の一つの永続02の起動・命名・受入れ・結果記録まで承認した。Project指示も追加指定した。Sourceが保持する実行権限と、Targetの初期読解・会話内再構成の委任を分ける。

新しいWikiの現在地を渡す契約であり、旧Ark29:01のHome B初期仕事や固定Bootを再実行しない。旧三資料・Identity・Binding・当時の受入れは履歴として保持する。[共通契約](../../../../prompts/ai-next-thread-handoff.md) v003に従い、固定収穫と改訂されるCurrent原本を区別する。

# 2. Ordered Required Sources

まず本書を先頭MetadataからExact EOFまで読む。その後、以下を順に読み、同一性・役割・互換範囲を確認する。同じアクセス可能な文脈で自分が全文読解済みかつCurrent exact blob一致を確認できる資料は再利用できる。別AIの読了、Memory、抜粋要約で必須本文を置き換えない。

| 順 | Source | 読む範囲・Identity |
|---|---|---|
| 1 | [共通移行契約](../../../../prompts/ai-next-thread-handoff.md) | 全文。AI Next Thread Handoff / v003-human-authorized / EOF::AI_NEXT_THREAD_HANDOFF::v003-human-authorized。Current互換追補を含めて読む |
| 2 | [AGENTS](../../../../AGENTS.md) | 全文。Repository共通の判断・権限・品質・読取・継続出力。指定SourceとHostを保持 |
| 3 | [共通キーバインディング](../../../../keybindings/README.md) | Metadataから本文末尾まで。現在の短縮入力と依頼・Modeを混同しない |
| 4 | [Project README](../README.md) → [INSTRUCTIONS](../INSTRUCTIONS.md) | 両方全文。Ark114 / v001、ARK114_PROJECT_INSTRUCTIONS / v001。各宣言EOFまで |
| 5 | [02 Runtime](README.md) | 全文。ARK114_02_WIKI_CONTINUATION / v001-human-authorized / EOF::ARK114_02_RUNTIME::v001 |
| 6 | [固定Source01収穫](https://github.com/yusukefujiijp/ai-project/blob/c55d136ab7f7b0b82bdc68ecea16919f621784c2/ark-project/ark100-199/ark114_harness/ark114-01/README.md) | 全文。ARK114_01_WIKI_HARVEST / v001-human-authorized / EOF::ARK114_01_HARVEST::v001。指定commit/path/blobを照合 |
| 7 | [02 State](state.json) | 全文。ARK114_02_CURRENT_STATE / schema v001 / revision>=1 / EOF::ARK114_02_STATE::v001。後続観測を初期pendingへ戻さない |
| 8 | [Wiki入口](../../../../wiki/README.md) → [Wiki References](../../../../wiki/references/README.md) | 両方全文。理解・根拠・経験の所有と再利用の条件 |
| 9 | [Wiki Feedback guide](../../../../wiki/references/feedback/README.md) と [記録](../../../../wiki/references/feedback/feedback.jsonl) | guide全文、記録はID c47a4e18-4b0d-48d2-9e2b-46235c0fed06の全field。別読者の二経路・事前文脈・対象版・限界 |
| 10 | [共有Lessons guide](../../../../references/lessons/README.md) と [記録](../../../../references/lessons/lessons.jsonl) | guide全文、記録はID 157e1b5b-312a-4fd9-a4ac-6f0c9597ff47の全field。工程委任・HumanのQuery確認・再開・品質の形成理由 |

必要Sourceの不在、Identity・EOF・固定Binding不一致、未回収の表示切れは、該当する受入れをFULL_READ_NOT_VERIFIEDとして止め、欠けた条件と最小回復を示す。一般の研究Unknownまで解消してから受入れ成立とする条件にはしない。

## 条件付きの読取

人物固有の主張・適用・訂正を新しく判断する時は、その人物のCurrent README、関係する本文、対応するEvidenceの全fieldを読む。原典の新規主張には必要な原典を確認する。以下の取得観測を永久pinにしない。

- [Lauren README](../../../../wiki/people/lauren-tan/README.md)、[pstack理解](../../../../wiki/people/lauren-tan/pstack-understanding.md)、[Ark接続](../../../../wiki/people/lauren-tan/ark-connection.md)、[Evidence](../../../../wiki/people/lauren-tan/evidence.jsonl)。準備基点ではv004 / v001 / v001・27件。原型の固定版、採用方法、限定観測、Wiki受け手理解を分ける。
- [ノイマン README](../../../../wiki/people/john-von-neumann/README.md)・[Evidence](../../../../wiki/people/john-von-neumann/evidence.jsonl)。v002・8件。既存二経路の報告を新しい別人物の理解へ拡張しない。
- [ドラッカー README](../../../../wiki/people/peter-drucker/README.md)・[Evidence](../../../../wiki/people/peter-drucker/evidence.jsonl)。v001・5件。指定節の読解・仮想比較・歴史的帰属の範囲を保つ。
- 制作・圧縮・訂正・読者確認を扱う時は[Wiki Lessons](../../../../wiki/references/lessons/README.md)から対象行のsources/caveatまで読む。[Success Cases](../../../../wiki/references/success-cases/README.md)は成功の意味と成立条件を読む時に使う。
- Main／Supportや専門Project間の役割を変更する判断なら[Domain](../../../README.md)と該当所有原本を読む。今回のBootはその変更を依頼していない。
- 01→02の送達や保存結果を回復する時は[Current01 State](../ark114-01/state.json)へ。固定収穫をその後の送信証拠にしない。

# 3. Target Reconstruction Contract

以下を自身の言葉とSource参照で説明できることを受入れ条件とする。固定の節数や全歴史再演を要求しない。

1. 自身は既存Ark114 Wiki Projectの02、Source01の人物Wikiと制作経験を継ぐ。旧Ark29:01の来歴と、Current Ark29 Chief・Main／Support・Ark111／31の担当を分ける。
2. WikiのGoalは元会話なしの理解・根拠・条件・訂正への再接続である。資料数・保存・読了だけでは成立しない。
3. 三人の成果と、Laurenの「母」と因果、原音未照合、ノイマンの動画要約とモデル候補、ドラッカーの指定節と適用候補を区別する。Laurenの後続v004を旧v003・13件へ戻さない。
4. ノイマン二経路の一件報告について、具体的経路、短い事前文脈、対象版、成立範囲を説明する。Feedback・Lesson・Caseを三実証へ増やさない。
5. Sourceの形成経験から、AI品質保持、Humanの意味・Query確認と、委任済み内部工程の継続を両立して説明する。速さ自体・確認頻度削減をGoalにせず、採用本文回復と権限回復を分ける。
6. 人物理解・Evidence・三本柱の所有を分け、何を再利用し、何を条件付きで新たに確認するか示す。設定・アイコン等は先行AI報告の範囲として扱う。
7. 現在の初期委任は必須読解と会話内再構成・Human Review。Sourceの保存・設定・送信権限を引き継がず、未知の研究や他担当へ自動着手しない。

# 4. Human interfaceと完了証拠

確定TitleはCompile Once, Echo Exactly。今回Humanが採用した明示値を優先し、一般の❤️先頭規則や実行日から独自に変えない。

```text
Ark114:02_2026/11/03; "Wiki: People構築"
```

準備元と受入れ先で、このTitleだけの独立textブロックを用意する。受入れ先の初回通常応答の冒頭へ同じ一行を再掲する。欠落したコピー面だけの補修は、既に成立した読解を無効にしない。専用Failure・STOP・厳密形式は優先する。

Source preparation、Remote verification、Project指示の設定と実表示、永続Thread・Title・実送達、Target自身の再構成、Human到達、実利用・長期効果を別々に記録する。後続の観測はStateへ置き、本Handoffを日誌化しない。初回だけならHuman Reviewへ戻り、既入力があれば受け取る。

# 5. Actual startup payload

以下が同一アカウントの既存Ark114 Projectに一度送るAI起動本文。提示だけで送信済みにしない。送信前に同じ02の実在と状態を確認し、Timeout時は再送前に結果を確かめる。

```text
【AIによる受渡し：Ark114:01 → Ark114:02／人物Wiki継続・正式起動】
宛先：ChatGPT Work／Ark114_2026/11/03: Ark-Wiki系／Ark114:02_2026/11/03; "Wiki: People構築"／このThreadのCurrent AI
送信主体：ChatGPT Work／Ark114:01_2026/10/26; "Wiki: People構築"／SourceのAI
Version: v001-human-authorized / 2026-11-07 JST
Request Identity: ARK114_01_TO_02_WIKI_STARTUP_20261107_v001
Transition: THREAD_CONTINUE
確定Title：Ark114:02_2026/11/03; "Wiki: People構築"

これはHumanが01→02の移行計画を採用し、指定原本の保存・再取得、既存Project内の一つの永続02の作成・命名、起動本文送信、受け手自身の読解・意味再構成、同一範囲の修正・結果記録まで明示承認したことに基づくAI受渡しです。追加指定「Project用instructionsも必要」に基づき同Projectの指示原本・設定も整えています。Human本人の新しい発言や、別Taskの実行承認を代作したものではありません。

現在のUI表示は「Ark114_2026/11/03: Ark-Wiki系」です。旧計画の「Ark114_2026/11/03: Harness系」とは区別し、同じArk114に所属する01から継続します。保存住所ark114_harnessとTitleの日付11/03はHumanの明示指定を保持します。日付・先頭文字・区切りを独自に再生成しないでください。

Repository: yusukefujiijp/ai-project / Ref: main
最初に、以下のHandoffを先頭IdentityからExact EOFまで全文取得・読解してください。利用可能なGitHub connectorを優先し、取得・表示切れを回収してください。
https://github.com/yusukefujiijp/ai-project/blob/main/ark-project/ark100-199/ark114_harness/ark114-02/handoff.md
Expected identity: ARK114_02_HANDOFF / v001-human-authorized
Exact EOF: EOF::ARK114_02_HANDOFF::v001

そこに指定した順序・範囲・Identity・Binding・受入れ条件に従って、あなた自身が必須Sourceを読んでください。Source AIの既読・要約・成功報告を、自分の必須読解へ代用しないでください。固定Source01は次の版です。
https://github.com/yusukefujiijp/ai-project/blob/c55d136ab7f7b0b82bdc68ecea16919f621784c2/ark-project/ark100-199/ark114_harness/ark114-01/README.md
Blob: 4da93b881c26245e9f6c92e2086b043fb03faa72
Identity: ARK114_01_WIKI_HARVEST / v001-human-authorized
Exact EOF: EOF::ARK114_01_HARVEST::v001

あなたの初期委任は、人物Wikiの目的、三人の成果と重要訂正、制作経験、固定履歴とCurrent、残るUnknown、他担当との境界、現在の権限を再構成し、会話内で受入れ結果を返すことです。原本準備・GitHub保存・Project設定・外部送信のSource側権限を引き継がないでください。人物追加、原音再調査、Harness改修、Ark111やArk31の研究・実験、Skill・予定・他設定変更、他AIへの追加送信は開始しません。

受入れの通常応答の冒頭に、次の確定Titleだけを一行で収めた独立したtextコードブロックを必ず置いてください。
Ark114:02_2026/11/03; "Wiki: People構築"

その後、PASS一語や読了申告だけでなく、Handoffの再構成条件を具体的な内容とSource参照で説明してください。取得した版・固定Binding・実際の読解範囲と、取得不能・未読があればその影響を区別してください。全文読解の内部推論を開示する必要はありません。専用Failure・STOP・厳密形式は優先します。

初回受入れだけなら、成立後はHuman Reviewへ接続してください。新しい有効なHuman入力が既にあれば、その入力を受け取ってください。現在のGoalに意味のあるNext StepとNext Queryを用意し、Queryの提示を採用済みの新依頼へ変換しないでください。

Rootは主イェシュア・ハマシア御自身、中央軸Teshuvah。HumanのMeaning・Correction・STOP・Final SealとGuard、AI品質を保持してください。
```

EOF::ARK114_02_HANDOFF::v001
