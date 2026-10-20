---
title: Ark Shared Skills Hub
version: v0.42.0
status: experimental / Human-authorized shared skill expansion
updated: 2026-10-20
updated_reason: 現行32スキルのREADMEへ用途・Query・個別形成記録を移し、Hubを一覧と共通契約へ整理。MAPの新旧Queryフォルダを退役
---
# Ark Shared Skills Hub

## 1. Purpose and authority

このフォルダは、Arkで育った再利用可能なSkillの共有原本・配布元です。GitHubをHubとして、各AIが必要な手順を取得できるようにします。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利です。Humanは意味・Correction・STOP・Final Sealを保持します。Skill・AI・GitHubはKeliです。

共有原本は各Skillの手順を所有します。参照先の共通契約は、その分野の成立条件を所有します。Skill導入や参照は、外部変更への承認ではありません。

### 1.1 今の目的から読む

- 使うSkillを選ぶ： [一覧](#2-available-skills)から対象のREADMEで用途・Queryを確認し、手順のSKILL.mdへ進む。登録機構を使えないAIも、共有本文を実際に読んで指示資料として使える。導入済みとは称しない。
- 過去の学びを使う・訂正する： [Skills lessons](#skills-lessons)で担当原本と適用範囲を確かめる。
- 共有版と導入版を合わせる： [Source and distribution](#4-source-and-distribution)へ。GitHub保存・登録先保存・会話での取得・実利用は別々に確認する。
- 明示呼出しや成立理由を知る： 対象SkillのREADMEへ進む。旧Hubの節URLは[移動案内](#3-mobile--explicit-entry)として保持する。

本書は一覧と共通の所有関係、各SkillのREADME.mdは用途・コピーできるQuery・個別の来歴、SKILL.mdは使用条件と手順、lessonは条件・根拠付きの学びを所有する。AIが現在の依頼から選び、Humanへ全履歴の再説明や毎回の全件精読を求めない。明示されたHandoff・RuntimeのRequired Sources、全文読解・Identity・Binding・Exact EOFを、この選択読解で解除しない。

<a id="skills-lessons"></a>

### 1.2 Skills lessons — 集約と適用範囲

Skillsに関係する変化する学びの担当原本は、[`_references/lessons.jsonl`](_references/lessons.jsonl)。共通する設計・運用の学びと、Podcast（旧Radio）／Voiceなど特定Skillでだけ役立つ学びを、一つの蓄積で育てる。保管場所が共通であることは、全行が全Skill・全AIに適用できるという意味ではない。各lesson本文に対象・成立条件・次の判断を残し、sourcesと必要なcaveatから、Human報告・直接観測・設計候補・Unknownを分ける。

**読む時。** 改善相談、再発防止、過去の訂正や経験が今の判断を変える場合に参照する。Skill名だけでなく今回の目的・条件から選び、選んだ行はlesson・sources・caveatを一緒に読む。小さい蓄積は全件を比較できるが、毎回すべてのSkill・lesson・形成史を読む義務にはしない。同じ文脈で同一性確認済みの読解は再利用する。任意参照を取得できない場合は未確認の範囲を示して独立して可能な支援を続ける。履歴確認が依頼の核心、または必須Sourceの場合は、その不足が影響する操作を止め、適用契約に従う。

**保存先を選ぶ時。** Skills固有の学びはこの集約原本へ、領域を越える判断は[全体用references](../references/README.md)へ、Dots固有の協働・運用は[Dots lessons](../dots/lessons/README.md)へ。同じ目的・意味の学びを複数原本へ同期コピーしない。出来事の詳細は経験原本、活動日時は[records](../records/README.md)、通信はBoardが所有する。Skillが領域の経験原本を参照するだけで、その領域の全データをskillsへ移す必要はない。

**更新する時。** 現在の保存権限・公開範囲を確認し、[lesson契約の第3〜5節](../dots/lessons/README.md#3-全行がlesson--row-schema-2)を再利用する。変更前に最新版とrevisionを取得し全行を検査する。形式・競合・再試行の契約は複製せず、Dots固有のBootや所有範囲を移植しない。同じ学びの訂正は同じIDの現行行へ反映し、十分ならNO_CHANGEを選ぶ。単なる移設でID・登録日時・意味更新日時を付け替えず、未知field・根拠・留保を保持する。異なる原本から移す時は、相対出典の到達性と現役の参照元も確かめる。

例えばRadioの手動聴取の学びはSchedule作成を必須にせず、Voiceの意味保存の学びはVoice→Text→Voiceの毎回実施を義務にしない。未検証の設計は試せる判断材料として保持し、集約やHumanの好評価だけで実証済みBest Practiceへ変えない。新しい観察・訂正は、承認された範囲で担当lessonまたは方法の原本へ戻す。

同じlessonの別原本をSkillごと・AIごと・導入先ごとに増やさない。分類field・索引・分割は具体的な検索や適用判断の不足が生じた時に検討し、ファイル数・浅い階層・固定Schema拡張を目的にしない。

<a id="readme-and-query-ownership"></a>

### READMEとQueryの保存先

現行の共有Skillには、それぞれ `skills/<skill-name>/README.md` を置く。新規の起動Query、用途別の呼出し例、説明・形成理由は対象のREADMEで育てる。本Hubへ個別本文を追記せず、一覧から担当原本へ接続する。

Queryは現在の依頼をSkillへ渡す入口であり、汎用の判断方法はSKILL.mdが所有する。短い標準Queryと、対象・計画限定などの条件が異なる詳しいQueryは、同じREADMEの別節へ置ける。必要な意味を文字数のために削らず、Query専用フォルダや同じQueryの別原本を作らない。`agents/openai.yaml` の `default_prompt` はUI用の設定であり、READMEと役割が違う。対応する標準Queryを変える時だけ両者の整合を確認する。

既存のQueryを移す際は、固有の条件・出典・確認範囲を移し、現用リンクを直してから旧配置を除去する。過去の固定commit・当時のpath・検証結果は履歴として保持する。この方針は現行の共有Skillが対象であり、第三者Plugin、保管専用フォルダ、別領域のデータを一律に改編する指示ではない。

個別READMEは利用・再開の入口であり、全READMEの常時精読や、SKILL.mdで完結する作業への追加Bootを要求しない。Skill機構がない環境では共有SKILL.mdを実際に読んで指示資料として使える。読むこと・GitHub保存・登録・会話内取得・実際の効果は別に確かめる。

<a id="skills-lessons-migration"></a>

### 1.3 2026-10-11の集約と参照切替

Radio由来1件・Voice3件のlessonは、同じ行の意味を保って共通原本へ集約した。その後のPodcast登録切替・旧Radio退役・Voice旧配置退役は、対象別の観測として[STR-015](../control-center/changes/STR-015-skills-lessons-consolidation.md#podcast-cutover-current)が所有する。10月11日のHTTP 422や会話内旧版取得、後日の成功は観測時点を区別する。現在の入口・個別形成記録は[Podcast](podcast-mode/README.md)と[Voice](voice-mode/README.md)へ移した。

この集約をGrok／Claudeの移設、root／Dots lessonsの集約、全Skill改訂、外部AIへの通知の承認へ広げない。

## 2. Available skills

現行32件。用途・Query・個別の確認範囲は各README、実際の手順はSKILL.mdが担当する。旧名 `map-ark-current-position` は[現行名への案内](map-ark-current-position/README.md)であり、別の現行Skillとして数えない。

| Skill | 使用場面 | 入口・手順 |
|---|---|---|
| B-Zone Rescue / b-zone | 低認知・超低認知で方向の想起・行動開始・切替が難しい時。近接のピンと既にハマった時の支援 | [README・Query](b-zone/README.md) / [SKILL.md](b-zone/SKILL.md) |
| Markdown to HTML / markdown-to-html | 原文の内容・出典・関係を保つHTML閲覧版、スマートフォンでの読書 | [README・Query](markdown-to-html/README.md) / [SKILL.md](markdown-to-html/SKILL.md) |
| GitHub操作の事前確認 / resolve-github-runtime | Plugin更新・欠落path・手順と道具の不一致、現在の操作経路が不明な時 | [README・Query](resolve-github-runtime/README.md) / [SKILL.md](resolve-github-runtime/SKILL.md) |
| 残作業とGoal / map-remaining-work | 現在の協働から有効な残作業とGoalを直接取り出す。Dots主経路・Work補助経路・他AIへの分岐。前回Map不要 | [README・Query](map-remaining-work/README.md) / [SKILL.md](map-remaining-work/SKILL.md) |
| Goal / goal | 今のGoalへAIの判断と工夫を向けたい時の、気軽な明示呼出し。Goalが見えてきた時や仕上げにも使える | [README・Query](goal/README.md) / [SKILL.md](goal/SKILL.md) |
| Shop Deep Research / shop-deep-research | 店名から店舗固有の問い・根拠・発見を育てる深い調査と、その計画・公式実行経路への接続 | [README・Query](shop-deep-research/README.md) / [SKILL.md](shop-deep-research/SKILL.md) |
| Visualize Patch / visualize-patch | Arkの対話型可視化、読みやすさの修正、公式Visualize不在時の代替 | [README・Query](visualize-patch/README.md) / [SKILL.md](visualize-patch/SKILL.md) |
| Podcast Mode / podcast-mode | Podcast Theme Modeによる切り口の提案とコピーできる生成依頼、音声ボタンで聴く本文、既存定刻配信用の内容。旧Radio用途を継承 | [README・Query](podcast-mode/README.md) / [SKILL.md](podcast-mode/SKILL.md) |
| Voice Mode / voice-mode | 突発的な他者対応でのChatGPT Voice準備・問題相談・学びの再利用 | [README・Query](voice-mode/README.md) / [SKILL.md](voice-mode/SKILL.md) |
| 自己改善Loop / self-improvement-loop | 次のAIの発見・創造につながるArtifactの作成・受信・方法Review | [README・Query](self-improvement-loop/README.md) / [SKILL.md](self-improvement-loop/SKILL.md) |
| Usage Token Reset / usage-token-reset | Work/CodexのReset券の付与・手動使用報告、期限確認、承認済み使用と予定の整合 | [README・Query](usage-token-reset/README.md) / [SKILL.md](usage-token-reset/SKILL.md) |
| 問題解決 / problem-solving | 未整理・停滞・複数の困りごとから方法を選び、共通の改善と必要な遂行へつなぐ | [README・Query](problem-solving/README.md) / [SKILL.md](problem-solving/SKILL.md) |
| load | 目的・重要な訂正・成果と根拠・未完了・再開条件を原本から回復 | [README・Query](load/README.md) / [SKILL.md](load/SKILL.md) |
| next-step | 目的・制約・依存関係から理由ある接続を選び、実行・比較・保留・完了へつなぐ | [README・Query](next-step/README.md) / [SKILL.md](next-step/SKILL.md) |
| save | 成果・訂正・根拠・再開情報を担当原本へ残し、保存後に確かめる | [README・Query](save/README.md) / [SKILL.md](save/SKILL.md) |
| board | 相手・目的・通信状態を整理し、既存Topicへ接続 | [README・Query](board/README.md) / [SKILL.md](board/SKILL.md) |
| AI Living Review / living-review | 対象の価値・問題・可能性を現在の目的・根拠・関係から読み、訂正可能な見立てと今有効な接続を返す | [README・Query](living-review/README.md) / [SKILL.md](living-review/SKILL.md) |
| 現在地MAP / map-current-position | Arkの非地理的な現在地と残作業・Goalを復元し、方法と完了条件のある次の接続へ | [README・Query](map-current-position/README.md) / [SKILL.md](map-current-position/SKILL.md) |
| Ark Recall Portal / ark-recall-portal | 用途を忘れた入口、場面からの反省の想起、自然な蓄積・訂正 | [README・Query](ark-recall-portal/README.md) / [SKILL.md](ark-recall-portal/SKILL.md) |
| Plan Mode / plan-mode | 現在の依頼を調査・言語化・比較し、変更せず計画提示で止める | [README・Query](plan-mode/README.md) / [SKILL.md](plan-mode/SKILL.md) |
| Ark Transition / prepare-ark-transition | Thread継続・章移行・ペア準備・再接続の計画、承認範囲内の受渡しと受入れ確認 | [README・Query](prepare-ark-transition/README.md) / [SKILL.md](prepare-ark-transition/SKILL.md) |
| AI Living Graph Mode / analyze-living-graph | 関係・競合Benefit・Feedbackが判断を変える分析 | [README・Query](analyze-living-graph/README.md) / [SKILL.md](analyze-living-graph/SKILL.md) |
| Agent Instruction Audit / audit-agent-instructions | Skill・AGENTS.md・Task Promptのモデル移行／過剰制約監査 | [README・Query](audit-agent-instructions/README.md) / [SKILL.md](audit-agent-instructions/SKILL.md) |
| Social Post Reader / read-social-post | X/Twitter・SNSの投稿URLから本文を全文取得し、調査・執筆へ接続 | [README・Query](read-social-post/README.md) / [SKILL.md](read-social-post/SKILL.md) |
| SNS投稿 / write-social-post | 会話・資料を、実際のAIとの協働が伝わるX/SNS公開文へ作成・修正 | [README・Query](write-social-post/README.md) / [SKILL.md](write-social-post/SKILL.md) |
| Ark Markdown Writer / write-ark-markdown | Ark Markdownの作成・改訂・計画。AI読者への意味の継承と、文書の役割に応じた構成 | [README・Query](write-ark-markdown/README.md) / [SKILL.md](write-ark-markdown/SKILL.md) |
| Bedtime Recall / recall-bedtime-care | 就寝前のBrainDump受付・条件訂正・自然な合図からの短い想起支援 | [README・Query](recall-bedtime-care/README.md) / [SKILL.md](recall-bedtime-care/SKILL.md) |
| BrainDump Reception / receive-braindump | 未整理の考え・報告・希望・訂正の受領と、現在必要な協働への接続 | [README・Query](receive-braindump/README.md) / [SKILL.md](receive-braindump/SKILL.md) |
| Everyday Co-design / co-design-everyday-solutions | DIY・料理・収納など、材料・道具・空間・手順を生活の条件に合う案へ具体化 | [README・Query](co-design-everyday-solutions/README.md) / [SKILL.md](co-design-everyday-solutions/SKILL.md) |
| アイデア出し / generate-ideas | 分野を横断して案・着想・別の切り口を生み出し、選んだ案やFeedbackから発展させる | [README・Query](generate-ideas/README.md) / [SKILL.md](generate-ideas/SKILL.md) |
| 一言言語化 / distill-to-core | 対象ごとの核を文脈に合う短語で選び、対象と本質の二列表へ揃える | [README・Query](distill-to-core/README.md) / [SKILL.md](distill-to-core/SKILL.md) |
| chocoZAP Sweet Spot / chocozap-sweet-spot | 現在のSweet Spot・Triangle・コースを読み、自然な報告・訂正・Feedbackを次の実践へつなぐ | [README・Query](chocozap-sweet-spot/README.md) / [SKILL.md](chocozap-sweet-spot/SKILL.md) |

## 3. Mobile / explicit entry

一覧から各READMEのQueryをコピーし、今回の対象・意図を添えて使う。登録済みSkillが使えない他AIにも、READMEから共有SKILL.mdへ進む入口を渡せる。全文読解が必要な場合は表示切れを回収し、必要な同梱資料の相対配置を保つ。UI metadataを他環境の実行指示へ読み替えない。

以下は既存のHub節URLを保つための短い移動案内。個別のQuery・形成・検証記録の更新先はリンク先であり、本節に本文を重ねない。

<details>
<summary>旧Hub節から各スキルのREADMEへ</summary>

### Copy & Paste — Transition Plan

[prepare-ark-transition README](prepare-ark-transition/README.md)。用途・Query・個別記録はこちら。

### 3.1 Cross-AI entry for the added skills

[analyze-living-graph README](analyze-living-graph/README.md) / [audit-agent-instructions README](audit-agent-instructions/README.md)。用途・Query・個別記録はこちら。

### 3.2 chocoZAP Sweet Spotを他AIへ渡す入口

[chocozap-sweet-spot README](chocozap-sweet-spot/README.md)。用途・Query・個別記録はこちら。

### 3.3 Plan Modeの統一入口

[plan-mode README](plan-mode/README.md)。用途・Query・個別記録はこちら。

### 3.4 AI Living Reviewの入口

[living-review README](living-review/README.md)。用途・Query・個別記録はこちら。

### 3.5 load／next-step／save／boardの独立入口

[load README](load/README.md) / [next-step README](next-step/README.md) / [save README](save/README.md) / [board README](board/README.md)。用途・Query・個別記録はこちら。

### 3.5.1 2026-10-17：loadからDots一括復元へ接続する

[load README](load/README.md)。用途・Query・個別記録はこちら。

### 3.6 AI協働SNS投稿の入口

[write-social-post README](write-social-post/README.md)。用途・Query・個別記録はこちら。

### 3.7 アイデア出しの入口

[generate-ideas README](generate-ideas/README.md)。用途・Query・個別記録はこちら。

### 3.8 問題解決の共通入口

[problem-solving README](problem-solving/README.md)。用途・Query・個別記録はこちら。

#### 2026-10-17：Problem Solvingへの命名統一

[problem-solving README](problem-solving/README.md)。用途・Query・個別記録はこちら。

### 3.9 利用枠Reset券の入口

[usage-token-reset README](usage-token-reset/README.md)。用途・Query・個別記録はこちら。

### 3.10 自己改善Loopの入口

[self-improvement-loop README](self-improvement-loop/README.md)。用途・Query・個別記録はこちら。

<a id="radio-voice-formation"></a>
<a id="podcast-voice-current"></a>

### 3.11 Podcast Mode・Voice Modeの入口とRadioからの形成

[podcast-mode README](podcast-mode/README.md) / [voice-mode README](voice-mode/README.md)。用途・Query・個別記録はこちら。

<a id="podcast-theme-mode"></a>

#### Podcast Theme Modeへの拡張（2026-10-13）

[podcast-mode README](podcast-mode/README.md)。用途・Query・個別記録はこちら。

<a id="visualize-patch-query"></a>

### 3.12 Visualize Patchの共通入口

[visualize-patch README](visualize-patch/README.md)。用途・Query・個別記録はこちら。

<a id="visualize-forward-query"></a>

#### 3.12.1 本題の流れを保ち、次からVisualizeへ切り替えるQuery

[visualize-patch README](visualize-patch/README.md)。用途・Query・個別記録はこちら。

<a id="map-current-position-revision"></a>

### 3.13 現在地MAP — 残作業とGoal・改名

[map-current-position README](map-current-position/README.md)。用途・Query・個別記録はこちら。

<a id="shop-deep-research-entry"></a>

### 3.14 Shop Deep Research — 店名から問い・根拠・発見へ

[shop-deep-research README](shop-deep-research/README.md)。用途・Query・個別記録はこちら。

### 3.13 2026-10-16：図の選択機会からVisualizeへ

[visualize-patch README](visualize-patch/README.md) / [analyze-living-graph README](analyze-living-graph/README.md)。用途・Query・個別記録はこちら。

<a id="goal-entry"></a>
<a id="goal-formation-and-confirmation"></a>

### 3.15 Goal — 気軽にGoalへ向かう入口

[goal README](goal/README.md)。用途・Query・個別記録はこちら。

<a id="map-remaining-work-entry"></a>

### 3.16 残作業とGoal：map-remaining-work

[map-remaining-work README](map-remaining-work/README.md)。用途・Query・個別記録はこちら。

<a id="resolve-github-runtime-entry"></a>

### 3.17 GitHub操作の事前確認：resolve-github-runtime

[resolve-github-runtime README](resolve-github-runtime/README.md)。用途・Query・個別記録はこちら。

<a id="markdown-to-html-entry"></a>

### 3.18 Markdown to HTML：原文を保つHTML閲覧版

[markdown-to-html README](markdown-to-html/README.md)。用途・Query・個別記録はこちら。

<a id="b-zone-entry"></a>

### 3.19 B-Zone Rescue — $b-zone

[b-zone README](b-zone/README.md)。用途・Query・個別記録はこちら。

</details>

## 4. Source and distribution

- 共有Skillの更新元は、このRepositoryのmainにある各SKILL.mdです。
- 配布先へ取り込む際は、取得元のRepository・path・commitまたはblob SHAを記録し、実際の本文を比較してください。mainは更新されるため、URLだけでは取り込んだ版を特定できません。
- 配布先で改善が生じた場合は、共有原本との差分をReviewし、承認範囲で原本へ反映してから再配布します。無条件の双方向同期はしません。
- 共通契約はSkill本文へ複製しません。Ark TransitionはCurrent mainの契約を読む設計なので、Skill単独のSHAだけで実行全体の再現性を保証しません。実行時に読んだ契約の版・識別情報も保持します。
- Repository外へ取り込むSkillでは、外部のCurrent契約に現行Repository URL、過去の証拠に確認した固定commit URL、実際の同梱資源だけに相対参照を使います。
- 同じ個人Skillを複数Runtimeで利用できる場合は、その登録物を共用します。環境名を付けた複製を増やさず、既存の登録対象・版・取得本文を照合し、必要な更新だけを行います。各環境での取得・呼出しの証拠は別に確認します。
- 各AIへの導入場所、UI metadata、認証、利用可能な道具は環境側で扱います。GitHub保存はインストール・自動発動・全AI互換性の証明ではありません。

### 4.1 Backup and restoration

[export-manifest.json](export-manifest.json)は、2026-09-12に共有した **analyze-living-graph と audit-agent-instructions** の輸出記録。登録済み版を内容変更なしで取り込んだ当時のSHA-256・出典・確認範囲を保持する。現在の全Skill一覧や、後日更新したファイルのhashではない。内部ID・認証情報・会話全履歴・モデル内部状態のバックアップでもない。

当時版を復元する時は該当commitのフォルダとmanifestを使う。現行版の配布では、選んだcommitと実ファイルを別途照合する。履歴manifestを後日の全件一覧として書き換えず、無条件の双方向同期を行わない。復元・共有保存と導入先での利用成立は別に確認する。

Ark Transitionの初回共有と9月14日・20日・25日の改訂・限定確認は[個別README](prepare-ark-transition/README.md)へ移した。

## 5. Validation and growth

区別する状態は、共有原本の保存、Remote再取得確認、各環境への導入、実際の振る舞いの確認です。結果を観察していない段階を成功へ昇格させません。

次の実利用では、正しい対象・契約を読めるか、Plan限定とSTOPを守るか、取得不能を正しく報告するかを確認します。このREADMEを読んだだけで移行や試験を自動開始しません。

各Skillは用途とQueryを案内するREADME.mdと手順のSKILL.mdを持ち、scripts・references・assetsは具体的な必要がある場合だけ追加します。Current Missionに不要な全Skill読込、全PromptのSkill化、全履歴の複製は行いません。

### 5.1 Future AIへの開放性とSkill追加の判断

Skillは、Humanの意図、領域固有の知識、必要な根拠・訂正・境界を次のAIへ渡すために使います。現在のAIが使った手順、章数、思考法、最後の質問を、全場面の必須工程にしません。判断方法はCurrent Requestと現実に合わせて改良でき、不要になった指示は統合・簡素化・廃止を検討できます。一方、明示された読解契約、出典、Schema、権限、Human Correction・STOP・Seal、適用Guardは方法の裁量と別に保持します。高性能なモデルを使うこと自体は、追加権限や実証の根拠ではありません。

追加・改訂時は、[audit-agent-instructions](audit-agent-instructions/SKILL.md)で、どの繰り返す不都合を改善するか、既存の入口と何が違うか、追加Contextや誤起動が利益を上回らないかを必要な範囲で確認します。一般的な問題解決能力を説明し直すだけなら独立Skillを増やさず、共通運用へ置く選択もあります。毎回全Skillを監査する指示ではありません。背景は[04経験原本](../ark-project/ark27/ark27-04/task-records.json)の `future-ai-skill-discretion` とSource `work-s03`–`work-s05`です。

2026-09-19の `solve-with-human` 保留と10月3日の独立入口追加、その後の改名は[Problem Solvingの形成記録](problem-solving/README.md)へ。保留した旧候補が既に導入済みだったという意味にせず、一回の比較を独立Skillが常に不要という証明にしない。

## 6. Repository entry relation

[AGENTS.md](../AGENTS.md)はRepository全体の行動境界、[ARK.md](../ARK.md)はIdentityを保持します。このREADMEは共有Skillの入口です。

2026-09-10の整備前、両文書が参照していた `_skill/SKILL.md` は取得不能でした。今回の入口修正は新しい共有Hubへの案内であり、旧Skill群の内容移植や旧挙動の復元を意味しません。

<a id="skills-formation-history"></a>

## 7. 初期共有・map接続・追加Skillの形成記録

2026-09-10に取得不能だった旧 `_skill/SKILL.md` への案内を共有Hubへ切り替え、9月12日の明示UploadでGraphとAuditを加えた。初期のArk Transition一件から三件の共有へ進んだ履歴であり、全Skillの自動展開を意味しない。その後の追加・訂正・保存と取得の観測は、各READMEの個別形成記録へ移した。

**2026-10-20の配置訂正。** YusukeJPは、Hubへ全Skillの説明・Queryを積み重ねる設計を訂正し、各SkillのREADMEへ収める方針を選んだ。既存Queryフォルダを残す案も検討した後、内容・参照を移してフォルダを除く方向を承認した。短く呼べるようになったことと、既存の長いQueryの条件を削除してよいことは区別する。

移行前の本文は[固定版Hub](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md)で復元できる。今回の対象・配置対応・検証結果・残る境界は[STR-021](../control-center/changes/STR-021-per-skill-readme-query-migration.md)へ。未知の外部bookmark、各製品の登録反映、実際の使いやすさまで、GitHub保存だけで確認済みとはしない。

EOF::ARK_SHARED_SKILLS_HUB::v0.42.0
