---
title: "Podcast Mode — Theme提案と聴取用本文"
canonical_path: "skills/podcast-mode/README.md"
version: "v001"
created: "2026-10-20"
updated: "2026-10-20"
role: "usage, invocation and formation guide"
---

# Podcast Mode

今聴く価値のあるThemeを見つけ、選んだ問いを耳だけでも追える一続きの話へつなぐSkillです。Theme提案と本文生成は、現在の依頼から使い分けます。Humanが音声ボタンを押して聴く用途を含み、音声の自動再生・予定登録・音声ファイル制作を呼出しだけで始めるものではありません。

## 起動Query

今の文脈からThemeを選びたい時に使います。これは旧Hubの承認済み入口を移したものです。

```text
$podcast-mode でPodcast Theme Modeを使い、今の文脈から、今聴くと価値があるThemeを提案してください。各案に、聴くと何が見えてくるかと、その案だけで使えるコピー用の生成依頼を添えてください。
```

Themeが決まっている時は、次の入口へ題材や現在の意図を添えられます。以下は現行Skillの本文生成用途に合わせた例で、候補選択を必須工程にしません。

```text
$podcast-mode を使い、今の文脈で指定したThemeを、耳で理解できる一続きの話にしてください。
```

方法と条件は[SKILL.md](SKILL.md)、UIの標準起動文は[agents/openai.yaml](agents/openai.yaml)が所有します。登録を使えないAI、登録側が旧版を返す環境には、次の依頼を渡せます。

```text
次の共有SKILL.mdを実際に読み、Podcast Modeを今回の依頼へ適用してください。
https://github.com/yusukefujiijp/ai-project/blob/main/skills/podcast-mode/SKILL.md
今回は、今の文脈から聴く価値のあるThemeを提案し、各案にその案だけで使えるコピー用の生成依頼を添えてください。
```

Podcast Theme ModeはこのSkill内の機能名です。別の `$podcast-theme-mode` を登録したという意味ではありません。選んだ案は同じThreadでも別Threadでも使えます。本文生成、実際のThread起動・移行、保存・公開・予定操作の権限は区別します。

## 役割と更新先

旧「Radio Mode」「ラジオモード」が聴取用依頼を指す場合も内容として継承しますが、旧 `$radio-mode` の機械的転送や全環境での新名称発動を保証しません。双方向のChatGPT Voiceの準備・相談は[Voice Mode](../voice-mode/README.md)へ接続します。

変化する学びは[集約lessons](../_references/lessons.jsonl)、その選び方・保存方法は[Skills Hub](../README.md#skills-lessons)が所有します。このREADMEは使い方とQuery、形成の読み筋を所有し、SKILL本文やlessonを別原本として複製しません。

## 形成と確認の記録

以下は[移管前Hubの固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md#radio-voice-formation)から、2026-10-20に本READMEへ移した記録です。各段落の「今回」「この会話」「未確認」は、その記録日における観測を指します。日付を越えて現在の未完了項目へ延長せず、後続確認と合わせて読みます。Voiceと共同で形成した経緯の詳細はこの節に一度だけ置き、Voiceの個別入口から参照します。

<a id="radio-voice-formation"></a>

### Radio・Voiceの形成とPodcastへの継承

**形成とHuman Correction。** 2026-10-10（Asia/Tokyo）、dot-0000との現在の会話で、YusukeJPは旧projects/・mode/の整理から、現役として育てる価値をRadio ModeとVoice Modeへ絞った。Radioは、特別なAI-Promptで聴取向けの回答を作り、Humanが音声ボタンを押してRadio化する使い方が「とても重宝しました」と報告した。以前に提示したClock-Drivenの定義は、指定時刻のReality・Current ContextをThemeへ織り込み、耳だけで追える一つの番組Messageに編成し、聴いた後に持ち帰れる一文や一手を残すというものだった。今回の明確化では手動の聴取も含め、定刻配信を全利用の必須条件にはしない。

Voiceについては、本人が普段ほぼ使わなくても、AIに疎い他者から突然の要望があるとChatGPT Voiceを使う場面があり、問題・課題・学びを蓄積したいと説明した。これは低い個人利用頻度だけで価値を退役判定しない理由である。旧Ark-Voice資料のVoice→Text→Voiceという認知的往復を、新しい目的の実証済み運用として再採用したとは扱わない。具体的な他者の発言・個人情報・未報告の不具合を、この初版の経験へ補わない。

その後Humanは二つのSkill名を明示し、既に使い慣れたlessons.jsonlによる改善の蓄積を提案した。AIが通常利用・保守し、Humanはまれな不具合確認時にも意味を追える日本語構成を希望した。references/の選択は条件付きの知識の役割を示すためであり、深い階層の普遍的優位や自動読込の保証ではない。2026-10-10 15:38 JST頃、Humanは全体用references/lessons.jsonlを新設したと報告し、「まずは混乱しない為に各スキルを作成」とGitHub実行を承認した。この実装は二Skillを先行させる範囲であり、全体のlesson移設、旧12原本のアーカイブ、他Skillの一括改訂は実施しない。

上記は当時のDot会話の編集要約。追跡識別子は、Radio定義提示 `Sentinel_8e57c232f00c8191a328e494daed0f6d`、二用途の明確化 `Sentinel_ad96756cce4081918a34d98c1c3a9af7`、二Skill指定 `Sentinel_85a6ca6bd4808191b27df4b17869984c`、JSONL提案 `Sentinel_185a2b6382ec81919054b15141673e00`、AI-primary／日本語の希望 `Sentinel_8787c115ef6881919286d3a423a76568`、先行実行承認 `Sentinel_b1f91d7321a88191b9b3671f8c98bc2b`。私的対話の識別子であり公開URLではない。アクセスできない読み手は、この公開要約と保存された成果の範囲で根拠を扱い、会話原文を独立確認済みとしない。

**二つの役割。** [podcast-mode](SKILL.md)は旧Radioから継承した耳で受け取る回答の編成、[voice-mode](../voice-mode/SKILL.md)は突発的な音声対話の準備・報告された問題・経験の想起を担う。前者は音声再生やScheduleを自動操作せず、後者はChatGPT Voice内での直接Skill呼出し・会話取得を未確認のまま保証しない。通常チャットでの準備と事後支援を独立して成立させる。深さ・構成方法・質問数・長さを固定せず、現在のHumanの目的・Correction・Plan-only・STOPを優先する。

**学びの所有先（2026-10-10初版）。** 当時の[Radio lessons](https://github.com/yusukefujiijp/ai-project/blob/96dbc5413b3ef32a4f9496819ff15930b9519678/skills/radio-mode/references/lessons.jsonl)と[Voice lessons](https://github.com/yusukefujiijp/ai-project/blob/96dbc5413b3ef32a4f9496819ff15930b9519678/skills/voice-mode/references/lessons.jsonl)を各専門領域の正本として作成した。現在の所有先は[Skills Hub](../README.md#skills-lessons)、参照切替の経過は[本書の後続確認](#registration-history)へ。初版は上記Human報告から一件ずつの条件付きlessonを置く。Skill本体は必要時の読取へ接続し、導入先へ同期されないデータコピーを増やさない。関連原本を取得できない場合、通常の支援は現在の情報から続けられるが、履歴の確認自体が依頼の核心なら不足を示す。

形式・更新・検証は[既存lesson契約の第3〜5節](../../dots/lessons/README.md#3-全行がlesson--row-schema-2)を参照して再利用する。契約本文・Dots共通lesson・Dots固有の所有範囲を各Skillへ複製・移管しない。一行は一つの現行lessonで、訂正は同じIDの行を更新する。現在の保存権限、公開範囲、最新revision、並行変更、保存後照合を守る。気づきだけから第三者会話の自動公開やSkill自動改訂へ進まない。

**構成と範囲（初版時点）。** 二つのSKILL.md、日本語の最小表示設定、二つの専門lessons、および当時のHubへの入口・形成記録を対象とする。Skill本体の更新元はGitHub共有原本、個人Skillへの導入内容は照合する。新しい常設同期・監視・Queryファイル・予定・外部AI通信は作らない。全体用references/lessons.jsonlはHumanが作成した改行のみのSeedを保持する。改行だけの内容をschema 2の有効なlessonデータや移行完了とは扱わない。

**限定検証と保存状態。** 両Skillは形式検査を通過した。元会話を渡さない一つの新規AI文脈で四つの構成した相談への応答を確認した。深いRadio解説、突然の第三者相談の開始準備、Voice内直接呼出しの未確認扱い、既存の定時配信向けの本文作成を扱った。最後のケースでは修正後本文を再読し、予定操作をせず内容だけ作成した。これは四つの独立文脈・製品内での自然発動・実聴取試験ではない。Voiceの一応答には、友人の混乱を誰の経験か明示しない引用文があり、限定確認だけで話者帰属の安定性を保証しない。仮想相談は専門lessonの実経験へ登録していない。

共有する四ファイルはmainへの保存後に再取得し、意図した全文と一致した。Radio本文のSHA-256は `47210085bb4a7ae604aadf1e388cbb95662d414e3cb6e4c9bd88a3ddd404c404`、Voice本文は `fbf51daa5ec24b0b772c7dd23336529ff4e07ef008684a66b6ce090ba9302c08`。初版本文の同一性を示す値であり、将来のCurrentを固定するBindingではない。

初回の個人SkillへのRadio登録は安全性チェックで拒否された。具体的な問題箇所は提供されず、登録なしを確認した後、この時点では再試行・別経路での導入を停止した。GitHub原本の保存と個人Skill導入を分け、この時点ではRadioを導入済みとは扱わなかった。独立したVoiceのみを通常の登録経路へ提出し、登録された有効本文を再取得して同じSHA-256で一致することを確認した。Radioの内容や変更をVoice登録へ混ぜていない。導入環境が付加した表示資源・内部情報はGitHub共有版へ複製しない。

**Radio再Challengeの観測。** 同日21:01 JST頃、Ark27:09のHumanが「Radio Modeはもう一度、Challengeして下さい！」と明示した。現行のskill-creatorが定める正規の登録手順で、同じ `radio-mode` 名と同じ本文を一度提出した。対象は[この時点の共有原本](https://github.com/yusukefujiijp/ai-project/blob/71d08cc6ea391e57228a53e1fbb0ff5a0392c1ce/skills/radio-mode/SKILL.md)と表示設定で、公式の形式検査を通過し、21:05 JST頃に登録先への保存が成功した。保存後、登録先で生成されたSkillを再取得し、本文3,910 bytes・上記SHA-256・全bytesの一致と、表示設定の元の三項目の一致を確認した。他のSkillの変更、lessonデータの複製、別名への変更は行っていない。導入環境が付加した表示資源・内部情報は共有原本へ戻さない。

この観測は登録先への保存と保存後本文の確認を成立させる。一方、この会話に公開されたSkill一覧ではRadioの反映を確認できず、その理由はUnknownのまま。保存済み内容と一覧の参照状態を分け、一覧差だけで再提出しない。初回の拒否理由は依然不明であり、今回の成功を初回判定が誤りだった証明や、拒否時の一般的な再試行規則にはしない。

実際のHuman UI、Radioの実呼出し・聴き心地、Voice内の直接呼出し、自然な自動選択、経験の継続活用による効果は未確認。GitHub原本を指示資料として読むこと、登録先への保存、各会話での参照・実利用を区別する。Radioの登録拒否を回避するために別名・別の導入経路へ送信しない。

**Podcastへの継承（2026-10-11）。** Ark28:05のHumanは、原因究明またはPodcast Modeを成立させてからRadioを退役する方向を提示し、Projectsの先行アーカイブ完了後もPlan Modeで計画を練り直した。その後「Execute GitHub OK」「Human Seal OK」と改訂計画の実行を明示した。これは本Threadの編集要約であり、未提示の会話URL・メッセージIDは作らない。Podcastの目的は聴取用応答の価値を分かりやすい入口へ継承すること。HTTP 422の原因解消や、初回Radio登録拒否の回避を改名の成果として主張しない。

Radio共有版をもとに、名称・表示・選択条件をPodcastへ更新した。深さ、現在の文脈、音声ボタンによる手動聴取、固定しない長さと構成を保持し、Skill自体の設計相談を番組本文へすり替えない案内を補った。旧Radioのlesson一件は元のID・本文・出典・日時・留保のまま集約先で継承する。Voice三件と合わせて四行は変更せず、新しい重複lesson・常設同期・予定・音声ファイル生成を加えていない。

共有二原本は[継承commit](https://github.com/yusukefujiijp/ai-project/commit/07ff0d8c8884ff072e3735cf8dc71b41192c0b01)から再取得して全文一致を確認した。既存Radioと同じ登録物を通常更新し、登録先RemoteのPodcast本文・表示三項目と共有版の一致も確認した。Voiceの集約参照更新は先に単独保存・確認した。一方、会話内のSkill経路は旧版のままで、新Podcast名の取得は成立していない。保存済みとこの未切替を分け、同じ保存の反復・別登録物の作成で埋めない。

元会話や期待回答を渡さない二つの独立文脈で、同じ候補本文を明示して限定応答を確認した。一つはRepository集約の利点と巨大化の懸念を、例・理由・条件をつないで聴取用の連続した文章にした。もう一つはPodcast Skillの改善依頼へ比較と計画を返し、番組作成や変更を実行しなかった。構成した相談であり、自然発動・旧コマンド転送・Human UI・実聴取・長期効果を実証したとは扱わず、仮想相談をlessonへ登録しない。

<a id="podcast-theme-mode"></a>

### Theme提案の拡張 — 2026-10-13

**形成と重要な訂正。** Ark28:05でHumanは、Theme段階の命名によって良いThemeの提案へ集中できると説明し、新鮮さ・AIならではの俯瞰・全体横断の切り口を歓迎した。Humanが共有した初穂の助言は、候補名だけでなく「そのThemeを今聴くと、何が見えてくるのか」を含める方向を示した。これはHuman経由で受領した助言であり、今回のAI間直接通信の観測ではない。その後Humanは、本線のThreadでThemeを練り、選んだ案を別のPodcast用Threadへコピーできる案を提示し、同一Threadの本文生成も残すと明示した。三案は例であり固定数ではない。

Humanは2026-10-13のPlan Modeによる計画提示後、GitHubと既存Skillの改訂・確認・初回三案の提示を承認した。本節は本Threadで受領した入力と実装観測の編集要約である。Themeの数や全案のArk限定、別Threadの強制、Humanによる結果の伝言義務を追加せず、Topicに必要な文脈を渡す設計とした。全履歴の複製や別Threadの自動同期を想定せず、後続のHuman訂正・STOPと受け手に適用される必須読解契約を保持する。

**確認範囲。** 改訂本文の形式検査を通過。元会話・期待回答を渡さない四つの独立したAI文脈で、Theme三案の提案、コピーした既出第三案だけからの本文生成、同じThreadでの直接生成を求める依頼、Skill見直しのPlan-only応答を確認した。提案では各案に中心の問い・聴く価値・背景付きの独立したコピー用依頼を返し、本文を生成しなかった。コピーした第三案からの応答は、Repository削除・一択化をHuman報告と方針として受け取り、可能性が広がるというAIの仮説と、集約による混雑・価値の抑圧の懸念を分けて語った。直接生成は候補選択を挟まず、Plan-onlyは比較と計画で止まった。これは限定した応答の観測であり、自然な自動選択、他社AIでの利用、Humanの実聴取・長期効果は未確認。構成した相談を実経験のlessonへ登録していない。

**共有・登録・実利用。** 共有本文は[本文改訂commit](https://github.com/yusukefujiijp/ai-project/commit/2d3bcda7b0edcd39fbefcd2247171c3755179417)、表示三項目は[入口改訂commit](https://github.com/yusukefujiijp/ai-project/commit/647e660a725508e9a22a7d1110027e0ff7105176)でmainへ保存し、それぞれRemoteから再取得して全文一致を確認した。既存のPodcast登録物を通常更新し、登録先Remoteから再取得した本文と表示三項目も共有原本と一致した。登録先の先行する別Skill更新を保持し、公開先masterへ今回の二ファイル差分を保存した。本文は8,499 bytes、SHA-256 `03541cea3801f2f93f3f8cd7019fb4a9ddaa00749bcecbeb237b91e443804430`。この値は今回版の同一性確認であり、将来のCurrentを固定しない。保存後も、この会話内のSkill読取経路はPodcast名で改訂前本文を返した。登録先保存と会話内の最新版取得を分け、同じ保存を反復せず、上の共有本文を実際に読んで今回版へ接続する。Human UI反映・自然発動・実聴取は未確認。新しい別Skill、常設同期、予定、外部送信、旧Radioの退役は行っていない。

**2026-10-14の後続接続。** 上記の改訂前本文取得は10月13日の当該会話の観測である。Ark27:09で確認したTheme拡張版の取得と、旧Radio配置の退役・復元条件は[後続確認](#registration-history)へ接続する。今回この節のコピー用Query・Skill本文・過去の試験記録は変更していない。

<a id="registration-history"></a>

### 集約・登録取得・旧配置退役の後続確認

2026-10-11、Ark28:05のHumanは当時のSkills Hubを最重要の入口とし、既存の良い部分を継承してskills内のlessonsを集約し、他AI・Future Dotsへ渡す計画を承認した。Radio 1件・Voice 3件を同一行のまま集約し、現在の読取・更新先は[Skills Hub](../README.md#skills-lessons)とする。

同日の初回作業では、集約先・共有Skill・案内の保存後全文一致を確認した一方、登録先へのRadio／Voice同時更新はHTTP 422で完了しなかった。その時点の旧版確認と退役保留は履歴として保持する。

**2026-10-11の後続保存。** Humanが改めて承認したPodcast継承計画に基づき、Voiceの参照更新と、既存Radioと同じ登録物のPodcast化を順に通常保存し、登録先Remoteから新本文を取得して共有原本との一致を確認した。422は今回再現しなかったが、以前の原因はUnknown。その時点の会話内Skill読取経路は旧Radio／旧Voiceを返し、新しいPodcast名での取得は未成立だった。当時は旧二JSONLと旧Radio共有二原本を互換参照の受け皿として保持した。現在の処置は下の2026-10-14の後続確認と所有記録へ戻り、更新先を増やさない。共有原本を読むAIは本書の起動Queryと集約lessonを使う。根拠・確認段階・各旧配置の退役条件は[STR-015の後続記録](../../control-center/changes/STR-015-skills-lessons-consolidation.md#podcast-cutover-current)が所有する。

**後続の取得観測（2026-10-13）。** Ark28:05の会話でPodcast名の登録済みSkillを取得でき、改訂前本文が共有原本（blob `bfec204f4ab1489e1a5b0fcf50c71423b23a04bb`）と一致した。10月11日時点の未取得を現在のPodcastの阻害条件へ延長しない。今回のTheme機能追加と改訂後の確認範囲は[Podcast Theme Mode](#podcast-theme-mode)へ。Voiceの再確認や旧配置の退役を、この観測だけで完了へ変えない。

**後続確認と旧Radio退役（2026-10-14）。** Ark27:09は既存Podcast登録物からTheme拡張版の全文を直接取得し、共有本文（blob `6188c1e2db9e061bae7a8a2d476f0af27205e93d`）と完全一致を確認した。既知の現役依存・lesson保存・固定commitからの復元経路を確かめ、旧Radio共有二原本と旧Radio JSONLの三ファイルを現役配置から除去した。Voiceについては、10月12日のDotsによる新参照・本文一致の[後続報告](../../records/2026/10/2026-10-12.jsonl)も保持するが、この実行ではVoice登録本文の再取得・旧JSONL除去を行わない。対象別の結果、保存後確認、復元条件は[STR-015の現在節](../../control-center/changes/STR-015-skills-lessons-consolidation.md#podcast-cutover-current)へ。過去の未取得を消さず、全Runtime・旧コマンド転送・UI・自然発動・長期効果は保証しない。

Voiceの旧JSONL退役は[Voice READMEの2026-10-15記録](../voice-mode/README.md#voice-cutover-current)へ進みます。10月11日時点の保留や10月14日時点の範囲外を、後続作業後の未完了へ戻しません。構造変更の検証・復元条件は[STR-015](../../control-center/changes/STR-015-skills-lessons-consolidation.md)が所有します。Grok／Claudeのprefix方式や既存_grokの移設、root／Dots lesson集約、別Repository作成、通知・外部AI送信は、この集約・継承作業の範囲外でした。
