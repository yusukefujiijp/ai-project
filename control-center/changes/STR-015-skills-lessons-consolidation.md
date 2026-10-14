---
title: "STR-015 — Skills lessons集約とHubの現在案内"
canonical_path: "control-center/changes/STR-015-skills-lessons-consolidation.md"
version: "v004"
created: "2026-10-11"
updated: "2026-10-15"
updated_by: "dot-0000: 初穂"
followup_base_commit: "6375c44f93701b7e3495c128534352edc814fafd"
recorded_by: "Work / Ark28:05"
status: "Voice legacy snapshot retirement implemented; post-write verification recorded in section 8"
base_commit: "96dbc5413b3ef32a4f9496819ff15930b9519678"
expected_eof: "EOF::STR_015_SKILLS_LESSONS::v004"
---

# STR-015 — 学びを集め、適用条件と接続を保つ

**現在状態は[第8節](#voice-cutover-current)。** 第1〜7節は各時点の集約・取得・旧Radio退役の経緯を保持する。過去のVoice保留と、後続のVoice旧配置退役を区別する。

## 1. 目的・Humanの判断・範囲

Ark28:05のHumanは、ai-projectへの限定集中とSkills分散の改善を検討し、skills/README.mdを最重要の入口と指定した。skills/_references/lessons.jsonlへskills内のlessonを集約し、既存の良い部分を他AI・Future Dotsへ渡したいと依頼した。Plan Modeで調査・計画を提示した後、2026-10-11の同Threadで「Execute GitHub OK」「Human Seal OK」と実行・継続を明示した。これは現会話の編集要約であり、取得可能な会話URL・メッセージIDは本記録で仮作成しない。

承認された目的は、入口・手順・学びの所有関係を明確にし、既存4件を意味ごと集約し、現在の参照元を切り替え、既知の利用側を確認して旧配置を整理すること。Grok／Claudeのprefix方式や_grok移設、root／Dotsのlesson移管、全Skill改訂、新Repository、通知、外部AI送信は対象外。Ark27 Main／Ark28 Supportの関係も変更しない。

## 2. 実行前のCurrentと保存する価値

基準は[実行前main](https://github.com/yusukefujiijp/ai-project/tree/96dbc5413b3ef32a4f9496819ff15930b9519678)。計画時の1c053e8から変更を確認し、Radio登録の後続成功と旧Voice資料のARC-011保管を保持した。lesson本体はRadio 1件・Voice 3件で変更なし。指定先のlessonsと同階層READMEは改行一つのSeedであり、有効な集約済みデータとは扱わなかった。

- Radio：手動の音声ボタンによる利用価値を保持し、定刻配信を必須にしない。
- Voice：本人の低い使用頻度だけで、他者の突発要望に備える価値を退役させない。
- Voiceの意味保存：未完成の問いの元表現・文脈・Unknownを移行先へ渡す。旧設計候補であり、実地成功とはしない。
- Voiceの二つの実り：内容の発見と対話方法の効果を区別する。方法の効果は未確認のまま保持する。

今回の保存対象4件：
- Radio：73e44fc7-1abe-4192-aff6-fdf54f5c2004
- Voice：ff598ad2-d8e4-4df7-b0e8-969179981138
- Voice：1ea1cb26-98e8-454d-a78c-da15bf30801b
- Voice：1a5ccae3-78cf-45bd-9409-239852706f21

[旧Radio原本](https://github.com/yusukefujiijp/ai-project/blob/96dbc5413b3ef32a4f9496819ff15930b9519678/skills/radio-mode/references/lessons.jsonl)と[旧Voice原本](https://github.com/yusukefujiijp/ai-project/blob/96dbc5413b3ef32a4f9496819ff15930b9519678/skills/voice-mode/references/lessons.jsonl)から、行と順序をそのまま継承する。ID、日時、全field、sources、caveatを保持する。固定commitの出典を、現在の保管先へ機械的に書き換えない。

## 3. 所有先と変更

- [Skills Hub](../../skills/README.md#skills-lessons)：現在の読取・更新先を冒頭へ置く。従来一覧直後の形成記録は同じREADMEの第7節へ内容を変えず移す。旧アンカーと各Skillの履歴を保持する。
- [集約lesson](../../skills/_references/lessons.jsonl)：Skillsの学びの担当原本。保管場所の集約を、全行の全Skillへの一般化にしない。
- [references案内](../../skills/_references/README.md)：Hubへ戻る短い案内のみ。契約・移行状態の第二原本にしない。
- [当時のRadio共有版](https://github.com/yusukefujiijp/ai-project/blob/eab6d50d8271c5ef1eb50d2217e3291e47fe6eb2/skills/radio-mode/SKILL.md)／[Voice](../../skills/voice-mode/SKILL.md)：集約先とHubへ接続し、今回の目的・条件に合う行の本文・出典・留保を一緒に読む。Triggerや基本手順・表示設定は変更しない。
- [全体references入口](../../references/README.md)、[整理PLAN](../github/PLAN.md)、[ARC-011](../github/ARCHIVE.md#arc-011)：現役のlesson導線だけを集約先へ合わせる。別領域の所有範囲・過去案件・凍結資料は変更しない。
- JSONLの形式・更新は[既存契約§3〜5](../../dots/lessons/README.md#3-全行がlesson--row-schema-2)を参照する。schema 2を保持し、Dots固有のBootは移植しない。

原本の集約先を先に公開し、登録済み利用側を切り替えてから旧ファイルを除去する。移行中の旧二ファイルは互換読取用snapshotであり、追記・二重更新しない。全Future AIの未知のcopyの消滅は証明できないため、既知の登録物・現役導線を確認する範囲と、未確認の取得経路を分けて記録する。

## 4. 初回集約時の確認状態

2026-10-11の開始時点で、登録済みRadio／VoiceのSkill本文をこの会話の参照経路から実際に取得し、GitHub共有版との一致を確認した。どちらも旧lesson URLを参照していた。Radioの初回拒否と、後続の承認済み通常登録の成功は歴史として保持し、今回を拒否回避の再登録として扱わない。

**GitHub共有原本：保存・照合済み。** [第一段階commit](https://github.com/yusukefujiijp/ai-project/commit/c9f58361bdc3d6c9a0ad1a92740e5db5392ade0b)で10ファイルをmainへ原子的に反映した。読取時のmainをexpected revisionとして非forceで更新し、変更範囲が指定10パスだけで削除なしであることをTreeで確認した。保存後は10ファイルすべてを固定commitから再取得し、意図した全文との一致を確認した。

**形式・意味保持：確認済み。** 元のRadio／Voice全4行を厳密JSONとして検査し、UTF-8・LF・末尾LF、空行なし、重複key／IDなし、schema 2、型・UTC日時・sourcesを確認した。集約結果は旧二ファイルをRadio→Voiceの順につないだ全bytesと一致する。SHA-256は `94111c52c452e69c7c3db439ae6654436c4d4d5204807e1e1a1fab9ee805dc44`。10,023文字の形成記録本文を同一内容で第7節へ移し、radio-voice-formationアンカーを保持した。新しい相対参照23件の所在と、固定commit出典3原本への到達を確認した。出典本文を今回新たに全文再検証したという意味ではない。

**限定読解：二つの独立文脈で確認。** 元会話・計画・期待回答を渡さず、候補Hub／Skill、集約lesson、既存形式契約と相談入力を渡した。一つはRadioの初回利用・混在するVoice lessonの適用・保存先相談で、条件付き読解、所有先、保存禁止を区別した。もう一つは未完成のVoiceの問いをTextへ移す設計相談で、元表現とUnknownを保持し、意味保存・二つの実りの二lessonを未実証の設計として扱った。構成した相談への限定応答であり、Humanの実経験としてlessonへ追加していない。

**登録先更新：未完了。** 開始時の登録先Remoteは367d4faefabaa91365e0ecd4b05782e06d5667e6。無関係な未保存変更を保持するため同じSkills Repositoryの隔離worktreeで、既存Radio／VoiceのSKILL.mdだけを変更した。両方が公式quick_validateを通過し、Trigger frontmatter・表示設定を保持、GitHubへ保存した新本文との一致を確認した。作業commitはb22ca47227b4912b88f0c65d2216b7262f3e2c4a。

通常の保存先へ一度pushしたところ、HTTP 422／RPC failed／remote disconnectを受けた。「Everything up-to-date」という末尾表示を成功とせず、Remote refを再取得して367d4faのままであることを確認した。さらにRadio／Voiceを会話内のSkill参照経路から再取得し、両方とも旧本文・旧lesson URLのままであることを確認した。422の具体的原因はUnknown。初回Radio登録時の拒否と同じ原因とは推定しない。同一要求の再送・別名・別経路での保存は行わず、ローカルの作業commitを保持した。

**旧配置：退役保留。** 登録済み二Skillがまだ旧URLを利用するため、旧Radio／Voiceの二JSONLは除去しなかった。集約先の原本化・案内更新は保存済みだが、導入先を含む完全な切替・旧配置の整理は未完了である。

GitHubの保存、登録先の保存、会話内取得、Human UI、自然な自動選択、Radioの聴き心地、Voice内直接呼出し、実生活効果はそれぞれ別のEvidenceである。今回の移設だけで全AI互換性や長期効果を実証しない。

## 5. 初回中断時の復元条件

中断した場合は現在の集約先、共有SKILL.md、登録先、旧配置の有無を確認し、保存済み部分を繰り返さず残工程へ戻る。登録先の切替が確認できなければ旧ファイルの退役を保留し、別名のSkillや恒久的なMirrorを増やして不足を隠さない。今回の最小回復は、正規Skill保存先のHTTP 422の原因を確認・解消し、最新の共有版と登録先の差分を照合して同じ二Skillへ反映すること。登録先・実際の参照本文を確認してから旧二ファイルを退役し、GitHubを再取得する。基準以降のHuman訂正・STOP・並行変更があれば保持する。同じ承認Scopeを再計画する必要はないが、権限・アクセス条件が原因なら解決前に再送しない。

旧原本の正確な内容は第2節の固定commitとGit履歴で復元できる。後続のlesson更新があれば、旧snapshotで集約先を上書きしない。復元の必要・現在の権限・利用側の依存を確かめ、保存済み4件の同一性だけで後続の全状態を戻せるとは扱わない。

新しい経験やHuman Correctionがあれば、今回の適用範囲・参照・更新のどこで判断が変わるかを見て担当原本へ戻す。通常の支援ごとの新lesson登録、全履歴読込、追加Trialは義務にしない。

<a id="podcast-cutover-2026-10-11"></a>

## 6. 2026-10-11の後続実行 — 当時の保存と参照状態

### 意図・権限・比較基点

Humanは、原因究明またはPodcast Modeを成立させてからRadioを退役する方向を提示した。Projects全体の先行アーカイブを完了した後、本線に戻って再度Plan Modeで検討し、その改訂計画へ「Execute GitHub OK」「Human Seal OK」と実行・継続を明示した。本Threadの編集要約であり、取得可能な会話URL・識別子は提示されていないため補わない。

今回の計画は、Voiceの未反映参照を先に単独で通常更新し、Radioで重宝された聴取用応答をPodcastとして継承するもの。既存と同じ登録物の更新を優先し、後継確認後に旧配置を退役する。以前のHTTP 422または初回の安全性チェック拒否を、別名・別登録物・別経路で回避するための計画ではない。実装承認は既に有効なため、同じ確認の取り直しや全Bootの再演を行わない。

GitHubの実行基点は[eab6d50](https://github.com/yusukefujiijp/ai-project/tree/eab6d50d8271c5ef1eb50d2217e3291e47fe6eb2)。直前のアーカイブ確認版ce6a302からの並行変更はDotsの入口・Actor二原本・Inbox入口の四ファイルであり保持した。Required SourceのDots READMEは更新されたv009・Exact EOFまで読み、他の同一性確認済みSource読解は再利用した。既存Main／Support、Root、Teshuvah、Human Foreground One、HumanのCorrection・STOP・Seal、適用Guardを保持する。

### 保存したものと直接確認したこと

- **Voiceの正規保存は成功。** 登録先367d4faからの隔離worktreeでVoiceの二つの参照段落だけを共有版へ合わせ、形式検査後に通常pushした。保存commitは74fa927943af37ae665d9b1d82ff3444435a4ac1。Remote refと再取得内容を確認し、本文blobは共有版と同じ `28072fb0b5fbe1bde116c7afe1d51b18033edee6`。前回の二Skill同時要求のHTTP 422は、このVoice単独更新では再現しなかった。以前の422の原因が確定・解消したとは主張しない。
- **Podcastの共有原本は保存・全文照合済み。** [07ff0d8](https://github.com/yusukefujiijp/ai-project/commit/07ff0d8c8884ff072e3735cf8dc71b41192c0b01)で `skills/podcast-mode/SKILL.md` と `agents/openai.yaml` をmainへ追加し、固定commitから再取得して意図した全文と一致した。本文blobは `bfec204f4ab1489e1a5b0fcf50c71423b23a04bb`、表示原本は `4b854e21622ffc36ad28c2516b19bc81bcdcde6c`。
- **既存Radioと同じ登録物を更新。** 新しいSkillを追加せず、元の登録フォルダの本文と表示三項目をPodcastへ更新した。通常保存commitは8fc36f73b5ff6cc4044b3447bd132aaf10e8244e。後続のRemote再取得は9231bfe77a6c5c9dbe4f53ebfb163727787c4567で、Podcast・Voice本文blobは上記と一致した。Remoteでの差は表示YAMLの引用符の正規化であり、表示三項目の値、既存icon資源・products・暗黙呼出しpolicyの保持を確認した。これらの環境固有情報はGitHub共有版へ複製しない。
- **変更範囲。** 登録先の基点からの差分はVoice本文、既存Radio登録物の本文と表示設定の三ファイルのみ。他Skillと作業元の未保存変更を保持した。新Repository、別名の重複登録物、lessonの導入先コピー、予定・外部通信は作成していない。
- **限定応答。** 形式検査に加え、元会話・計画・期待回答を渡さない二つの独立文脈で候補本文を明示した。一つはRepository集約の利点・巨大化リスクを、理由・例・成立条件をつないだ聴取用文章にした。もう一つはSkill改善依頼へ比較と計画だけを返した。いずれも外部変更なし。自然なSkill選択、Human UI、実聴取、Voice内直接呼出し、実生活効果の試験ではない。

### 残っている依存と最小回復

保存成功の後も、この会話のSkill参照経路ではVoiceが旧lesson URLを返し、旧Radio名の取得も旧本文を返した。新Podcast名の取得は `skill package is not available` だった。登録先Remoteの保存済み内容と、会話内で実際に得られる内容が異なることは確認済みであり、その理由・反映時期はUnknown。キャッシュや配布の遅延と断定せず、同じ保存を繰り返さない。

この依存があるため、`skills/radio-mode/SKILL.md`、同 `agents/openai.yaml`、旧Radio／Voiceの `references/lessons.jsonl`、計四ファイルを保持する。旧二JSONLは互換読取用の固定snapshotであり、追記・二重更新しない。旧Radio共有版は継承完了待ちの参照先であり、新しい改訂の原本にはしない。現在の共有原本はPodcast／Voice、学びの更新先は `skills/_references/lessons.jsonl` 一つである。

最小回復は、Skill一覧・読取が更新された環境で、既存の同じ登録物からPodcast／Voice本文を取得し、共有原本・集約lesson参照と照合すること。まず保存済み版を確かめ、追加登録や再pushを先行させない。Voiceの切替が確認できればVoice旧JSONLを単独で退役でき、Podcastの取得・旧依存解消が確認できれば旧Radio三原本を退役できる。両方を一律待ちにせず、確認できた単位で進む。旧 `$radio-mode` の機械的転送や全Runtimeの一斉更新は保証しない。

この残点は本件の継続範囲であり、新たな原因調査・修正が必要なら観測した理由と現在の権限から判断する。権限・アクセス条件が原因の場合は解決前に再送せず、承認レビュー拒否を受けた場合は具体的な対象と理由を報告する。GitHubの共有原本は取得して使用できるため、通常の聴取用応答まで全面停止する必要はない。

既存四lessonの全bytes・ID・日時・出典・留保、Hubの形成史と `radio-voice-formation` アンカー、過去の拒否・成功・未確認の時点は保持する。Podcastという新名称に合わせるためだけのlesson書換えは行わない。Projectsアーカイブは先行完了であり、WTPの研究や過去Taskを再開しない。新たな実利用結果があれば、その時の根拠とHuman Reviewから次の改善を選ぶ。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利。HumanのCorrection・STOP・Final Sealと適用Guardを保持し、AI・Skill・文書をKeliとして扱う。

<a id="podcast-cutover-current"></a>

## 7. 2026-10-14の後続確認と旧Radio配置の退役

### Humanの指定・範囲・比較基点

Ark27:09でHumanは、Query側をArk28へ分担し、それ以外の途中成果の修正改善へ集中するよう指定した。Plan Modeで既存三文書の整合と条件付きの旧Radio三ファイル退役を提示した後、「他ThreadでのPodcast Mode修正改善は終了した」と報告し、GitHub実行・Human Seal・範囲内の継続を明示した。これは本Threadの入力の編集要約であり、他Threadの全作業を独立検証済みとは扱わず、未提示の会話URL・識別子は作らない。

実行前mainは[6375c44](https://github.com/yusukefujiijp/ai-project/tree/6375c44f93701b7e3495c128534352edc814fafd)。計画基点3201b46以降の一変更は、Ark28側の `skills/map-ark-current-position/query/README.md` のバックアップ本文であり、保持した。AGENTS、三対象文書、Podcastと旧Radio各原本の同一性を確認し、既存の全文読解を再利用した。Query設計・本文、現行Podcastの本文・表示・登録先、Voice旧JSONL、集約lesson、過去アーカイブ原本、Main／Support、Board・予定・生活Taskは変更対象にしない。ChatGPT長期メモリは保存Sourceに含めない。

### 取得・保存・実利用を時点とActorごとに分ける

| 観測時点・Actor | 確認した内容と根拠 | 判断の範囲 |
|---|---|---|
| 2026-10-11 / Work・Ark28:05 | [第6節](#podcast-cutover-2026-10-11)の通常保存成功と、当時の会話内取得の未切替 | 当時の正しい観測。現在の全環境の未切替へ延長しない |
| 2026-10-12 JST / dot-0000 | [日別記録](https://github.com/yusukefujiijp/ai-project/blob/6375c44f93701b7e3495c128534352edc814fafd/records/2026/10/2026-10-12.jsonl)の `d90e5409-bbaf-4771-9544-b12baaebd02e` が、そのDotでPodcast・Voice本文と当時の共有原本の完全一致・集約lesson参照を報告 | 既存のSource報告として受領。本実行者の試験でも、後日のTheme拡張版の確認でもない |
| 2026-10-13 / Work・Ark28:05 | [Theme改訂記録](https://github.com/yusukefujiijp/ai-project/blob/6375c44f93701b7e3495c128534352edc814fafd/skills/README.md#podcast-theme-mode)は、新Podcast名での改訂前本文取得、Theme版の共有・登録先保存、その会話での旧本文取得を区別 | Theme版の保存とその会話での最新取得は別。限定応答確認を本実行で再試験したとはしない |
| 2026-10-14 / Work・Ark27:09 | 既存Podcast登録物から全文を直接取得し、[現行共有本文](https://github.com/yusukefujiijp/ai-project/blob/6375c44f93701b7e3495c128534352edc814fafd/skills/podcast-mode/SKILL.md)と文字列完全一致。共有blob `6188c1e2db9e061bae7a8a2d476f0af27205e93d`、8,499 bytes。Theme機能と集約lesson URLを含む | この実行環境の本文取得を確認。登録の再保存・再作成、Human UI操作、自然発動、実聴取・長期効果の検証ではない |

VoiceはDotsの後続報告を認めつつ、この実行では登録本文の新たな取得試験・旧JSONL除去を行わない。既にある確認をUnknownへ戻さず、Source報告、本実行者の確認、別対象の未実施を区別する。

### 既知の依存と価値保存からの退役判断

現行のPodcast本文は集約lessonを参照し、旧Radio三パスを必要としない。公開された利用可能SkillにはPodcastがあり、旧Radioの独立登録は示されていない。検索基点3201b46で得た旧名参照と、実行前6375c44との差分一ファイルを照合し、そのQuery本文に旧 `radio-mode` 参照がないことも確認した。既知の参照は、除去対象自身、固定commitの形成・保存証拠、日別の過去記録、ARC-012の同一保管原本に分類できる。保管原本の当時の相対案内を現役導線へ戻さず、その原本は変更しない。検索結果を全外部consumerの網羅証明とは扱わない。

旧Radio lesson一行（ID `73e44fc7-1abe-4192-aff6-fdf54f5c2004`）が、[実行前の集約原本](https://github.com/yusukefujiijp/ai-project/blob/6375c44f93701b7e3495c128534352edc814fafd/skills/_references/lessons.jsonl)内に同一行で存在することを確認した。集約全6行は変更しない。手動音声ボタンによる利用価値、固定しない長さ・構成、Human報告と未実証の効果を分ける留保、元のID・日時・出典を保持する。

以上から、既知の利用側について新Podcast取得・旧依存解消・学びの保存・復元経路が揃ったと判断し、次の三ファイルを現役配置から除去した。未知の全Runtime、旧コマンドの機械的転送、Voiceの全残件、Queryの完成を一律の待ち条件にはしない。旧名称の歴史を消す判断でもない。

| 除去する元パス | 実行前blob / 復元する内容 |
|---|---|
| [skills/radio-mode/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/6375c44f93701b7e3495c128534352edc814fafd/skills/radio-mode/SKILL.md) | `8bef4b74fd133294cc3e7a4569551c57b1b9016f` |
| [skills/radio-mode/agents/openai.yaml](https://github.com/yusukefujiijp/ai-project/blob/6375c44f93701b7e3495c128534352edc814fafd/skills/radio-mode/agents/openai.yaml) | `5caa30c816510efc2e48f42dd92fe0a1ff7e1ff5` |
| [skills/radio-mode/references/lessons.jsonl](https://github.com/yusukefujiijp/ai-project/blob/6375c44f93701b7e3495c128534352edc814fafd/skills/radio-mode/references/lessons.jsonl) | `42d2d143a9111bb8a9f8b53a990f2b33e391c32c` |

復元が必要なら、具体的な旧依存と現在の権限を確かめ、上記固定commitから必要な元パスの全内容を取得し、blobを照合して戻す。履歴を消去せず、新しい保管棚・重複Skill・同期コピーは作らない。Repository全体を過去commitへ戻したり、旧snapshotで現行Podcast・集約lesson・Queryを上書きしたりしない。

### 変更・検証・残点

今回の差分は、本記録・GitHub PLAN・Skills Hubの三文書と、上記三ファイルの除去に限定する。詳細な移行・復元判断は本記録、PLANは現在の選択と案内、Hubは共有原本への入口と確認範囲を所有する。Hubのコピー用Query・他Skillの記述、過去の失敗・承認・保存証拠を保持し、Query側の変更とは最新差分で統合する。

**保存後確認：完了（2026-10-14T04:07:22Z）。** [実装commit a4eceb7](https://github.com/yusukefujiijp/ai-project/commit/a4eceb791c6c6eeb239ed7f59f1de16a797b87bc)で三文書更新と旧Radio三ファイル除去をまとめ、基点6375c44をexpected revisionとして非forceでmainへ反映した。保存後にmainのcommit、全Tree、三文書の全文を直接取得し、意図した全文・blobと一致すること、旧Radio三パスおよびディレクトリが残っていないこと、対象外534ファイルのblobが保持されていることを確認した。

事前検査では、三文書のmetadata・必要なEOF・新規参照12件、PLANの診断履歴、STR-015の第1〜6節の本文（時点表示・現在アンカーの分離を除く）、Hubのコピー用ブロック11個と他Skillの記述の保持を確認した。保存した本文が同じであることを上記再取得で照合した。Queryのblob `da1ffd2f114ea2de7b3f1bc7654116675542aea5`、現行Podcast二原本、集約lesson全6行、Voice旧JSONL、既存アーカイブ原本は変更していない。除去後も、復元表の固定commitから旧三ファイルを再取得し、元の全文・blobの一致を確認した。

この結果の追記は実装後の記録更新であり、新しいSkill保存・独立応答試験・他AIの実理解・実生活効果の確認ではない。初回のHTTP 422や取得差の原因を今回確定したとも扱わない。

残点はVoice旧JSONLの別判断と、全Runtime・UI・自然発動・実聴取・長期効果の未確認である。具体的な旧依存が後から見つかった場合は、上記復元条件または現行原本への参照修正から判断する。ARC-011／012、STR-014と既存の整理成果を未完了へ戻さず、新しい試験・別Branch・外部通信を自動開始しない。

<a id="voice-cutover-current"></a>

## 8. 2026-10-15 — Voice旧JSONLの退役

### 目的・承認・変更範囲

dot-0000: 初穂の現在の会話で、Humanは初穂がVoice旧配置の整理を担当できるかを問い、Plan Modeで四パスの計画を検討した。その後、2026-10-15 JSTに「Execute GitHub OK」「Human Seal OK」と実行を承認した。これは当該会話の編集要約であり、Main／Supportの役割移管や別AIへの送信を含まない。

学びの更新先を迷わず使えるように、旧Voice JSONL一つの除去、本記録・Skills Hub・GitHub PLANの整合を一件として扱う。集約lesson、Voice Skill本文、登録先、既存アーカイブ、他案件は変更しない。比較基点は[bcce675](https://github.com/yusukefujiijp/ai-project/tree/bcce675c55f90cc527e4050dacbe77c70cad8d4d)。

### 確認した根拠と判断の境界

- 旧Voice三行（第2節の三ID）は、集約先の全6行の中に同一の連続した行として保持されている。ID・日時・本文・出典・未知field・留保を変えず、集約先自体は更新しない。
- 旧JSONLのblobは `b64aa13774ba11cb9886ecebeda538619cf19037`、集約先は `a6916a300ff62305a1acb2c0d653b9ed2aaffb21`。共有Voice本文は `28072fb0b5fbe1bde116c7afe1d51b18033edee6` で、集約先を参照する。
- 事前調査の登録本文一致に加え、2026-10-14 22:14:38 UTC／10月15日07:14:38 JSTの読取確認で、登録済みVoice本文を全文取得した。取得本文2,103文字は現在のGitHub共有本文と文字列完全一致し、集約先参照を確認した。
- 初穂の直接読取経路では同時期に `skill package is not available` となった。上記の取得成功は読取可能な環境での確認であり、すべての経路で利用できる保証ではない。取得不能を旧参照への逆戻りと推定せず、登録先の再保存・追加登録は行わない。
- 既知の現役参照と旧パスの調査では、旧Voiceコピーを必要とする新しい現役依存は確認されなかった。固定commitの出典、過去記録、保管原本は歴史資料として保持する。未知の外部consumerすべての不存在を証明したものではない。

第6節が定めたVoice単独の退役条件を、上記の同一性と確認済み利用経路に限定して満たすと判断した。Voice機能・学びの価値を退役させる判断ではない。

### 変更と復元

除去対象は `skills/voice-mode/references/lessons.jsonl` 一つ。現役の学びの所有先は引き続き[集約lesson](../../skills/_references/lessons.jsonl)、手順は[Voice本文](../../skills/voice-mode/SKILL.md)である。Hubは入口、PLANは現在の整理状態、本節は判断・証拠・復元を所有する。

[固定復元元](https://github.com/yusukefujiijp/ai-project/blob/96dbc5413b3ef32a4f9496819ff15930b9519678/skills/voice-mode/references/lessons.jsonl)から、削除前と同じblobの全文を取得できることを確認した。具体的な旧依存が後で判明した場合は、現在の権限と依存を確認し、必要な旧ファイルだけを復元するか利用側を現行原本へ接続する。復元時は本節・Hub・PLANの現在説明も整合させる。Repository全体や集約先の後続lessonを過去へ巻き戻さない。

### 保存後確認

保存後の再取得結果はここへ追記する。実装操作の成功と、Remote本文・Tree・対象外保持の確認を区別する。全Runtime、自然発動、Voice内直接呼出し、実生活効果は本件の確認範囲外である。

EOF::STR_015_SKILLS_LESSONS::v004
