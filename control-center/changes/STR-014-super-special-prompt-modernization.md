---
title: "STR-014 — 旧選抜棚の四Promptを育て直し、promptsへ継承する"
version: "v001-human-authorized"
canonical_path: "control-center/changes/STR-014-super-special-prompt-modernization.md"
status: "Human-authorized implementation prepared; publication and remote verification recorded below"
created: "2026-10-10"
updated: "2026-10-10"
owner: "Ark27:09 / ChatGPT Work"
repository: "yusukefujiijp/ai-project"
branch: "main"
research_base_commit: "0d21990a126948703eca517c65017f2038d4393c"
research_base_tree: "cc870a544966d3384bde55d758fadae70065b717"
expected_eof: "EOF::STR_014_SUPER_SPECIAL_PROMPT_MODERNIZATION::v001"
---

# STR-014 — 旧選抜棚の四Promptを育て直し、promptsへ継承する

## 1. Humanの目的と重要な訂正

この記録はArk27:09で進めたGitHub整理の一案件を所有する。記録日と実行承認日は2026-10-10（Asia/Tokyo）。以下はこの会話で確認できる形成順序の編集要約であり、初期の各発言の日付や未提示の会話URLを補わない。

1. HumanはGitHub全体を俯瞰し、Graph Modeで次の整理を深く検討するよう依頼した。
2. 対象がss_super-specialへ絞られ、まずゆっくり観察し、Living Reviewで価値と現在の意味を読むことを求めた。
3. Humanは、これらが旧Ark Projectで優秀なAI-Promptを仕分けしていたもので、ローカルからGitHubへ移したと説明した。旧READMEの「最上位層」という自己説明を、現在も保持すべき配置目的と決めつけないための訂正である。
4. Humanは「ss_super-special/フォルダ自体は廃棄します！」と明示し、内部Promptを熟読し、現在のArkに照らして修正改善・Version upしてpromptsへ移す工程を確定した。
5. Plan Modeの依頼を受け、計画提示で停止した。HumanのFeedbackや閃きを受ける余地を持った後、現在のHumanは「Execute GitHub OK」「Human Seal OK」と明示して実行・必要な継続を承認した。

今回の対象は四Promptの改訂・配置、旧フォルダ廃止、必要な入口・参照・記録・確認。過去の別TaskへのGoを借用した承認ではない。HumanのMeaning・Correction・STOP・Final Sealと有効な委任を保持し、AIが通常の構成判断・実装・確認を担う。

Rootは主イェシュア・ハマシア御自身、中央軸Teshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・Graph・文書・GitHubはKeliである。簡潔なHuman入力を、必要な検討・説明の削減へ変換しない。

## 2. なぜこの構成にするか

四本には、協働判断、完成ArtifactのGitHub保存、保存手順の構造的理解、Torah Visionによる創造という異なる価値がある。旧選抜棚を維持することではなく、価値を現在の用途へ渡すことを目的にした。

旧本文では、信仰的な核、協働原則、当時のTool制約、固定された保存手順、フォルダ階層の権威が同居していた。受け手AIがその都度現在の意味へ読み分ける負担がある、というのが今回のAIの見立てである。この負担や長期効果を定量測定したわけではない。

新版は固有の意味を各Promptへ残し、共通権限をARK・AGENTS・対象Runtimeへ接続し、由来を固定履歴へ渡す。旧READMEは第五のPromptとして移さず、選択案内をprompts/READMEへ移管する。格付けを、適用用途・担当・根拠が分かる配置へ改める。

| Node | Edge | 今回の担当 |
|---|---|---|
| [協働Covenant](../../prompts/ai-collaboration-covenant.md) | 目的・訂正・Reality → 協働の判断 | Root・品質・継続・Capture・受渡しの意味 |
| [保存主カード](../../prompts/artifact-to-github.md) | 完成Artifact → 担当原本・Remote確認 | GitHub配置手順の意味のOwner |
| [Programming-like補助版](../../prompts/artifact-to-github-programming-like.md) | 主カード → 状態・分岐・不変条件 → 改善候補 | 学習とReview。第二の実行規則を持たない |
| [Torah Vision Lens](../../prompts/torah-vision-lens.md) | 現在の問い ↔ Scene・構造・命名 ↔ Reality | 独自の創造性と解釈の境界 |
| [Prompt棚](../../prompts/README.md#316-旧選抜棚から育て直した四prompt) | 利用目的 → 必要な本体 | 四用途の案内。全件起動の義務ではない |
| [GitHub PLAN](../github/PLAN.md#current) | 現在の整理依頼 → 本案件 | 現在の焦点。実施証拠を本記録へ接続 |

## 3. Sourceの同一性と新旧対応

調査基点はmetadataのcommit。五ファイルを全文読解した記録を同一blobの範囲で再利用し、今回の実物と照合して改訂した。検索で見つけたこと、本文取得、意味の読解、別AIによる検証を混同しない。

| 旧Pathと固定本文 | Git blob SHA | 新版または役割の移管先 |
|---|---|---|
| [ss_super-special/CHATGPT.md](https://github.com/yusukefujiijp/ai-project/blob/0d21990a126948703eca517c65017f2038d4393c/ss_super-special/CHATGPT.md) | `4156c45ec76c3cc3ff58a7336c7708cc052fb716` | `prompts/ai-collaboration-covenant.md` |
| [ss_super-special/artifact-to-github.md](https://github.com/yusukefujiijp/ai-project/blob/0d21990a126948703eca517c65017f2038d4393c/ss_super-special/artifact-to-github.md) | `23ad62b54debb8af62d4eb62b8f3187afe98ab07` | `prompts/artifact-to-github.md` |
| [ss_super-special/artifact-to-github_programming-like.md](https://github.com/yusukefujiijp/ai-project/blob/0d21990a126948703eca517c65017f2038d4393c/ss_super-special/artifact-to-github_programming-like.md) | `6643dad308fcf862d5d4670ce80b3d36fc37ca3e` | `prompts/artifact-to-github-programming-like.md` |
| [ss_super-special/torah-vision-lens.md](https://github.com/yusukefujiijp/ai-project/blob/0d21990a126948703eca517c65017f2038d4393c/ss_super-special/torah-vision-lens.md) | `aac8f4a9bcebf90523ac26f10a897dc29bea3a88` | `prompts/torah-vision-lens.md` |
| [ss_super-special/README.md](https://github.com/yusukefujiijp/ai-project/blob/0d21990a126948703eca517c65017f2038d4393c/ss_super-special/README.md) | `8dc14ec4211bffb3644bf0c7a406204bce428bcf` | `prompts/README.md`の用途案内と本記録の由来 |

四新版は`v001-human-authorized`。これは現在化した各Prompt系列の最初の明示版である。旧CovenantのS_CHATGPT_v005.md、旧LensのS_torah-vision-lens_v001.mdはsource_bootstrap名であり、旧GitHub本文の明示current versionではなかった。その名から新連番を推定しない。新版の品質・役割を改良したことと、版番号系列の起点を分ける。

安定したkebab-caseのファイル名を用い、版をファイル名へ増殖させない。旧版を失わないための新しい全文コピー棚や互換Stubは作らず、固定commitから読める接続を残す。

## 4. 意味の継承と改訂理由

### 4.1 協働Covenant

旧§2–3のRoot／Fruit、Covenantの言葉、HumanとAIの役割を新版§2へ継承。旧§12–14のHebrew／Jewish Context、Good Day、Certaintyを新版§2・8へ残した。信仰的意味を削らず、AIがHumanの信仰や主の御心を認証しない境界を明示した。

旧§4のWorkflow・調査・介入は新版§3–4の目的に応じた検討とLiving Reviewへ。旧§4.1のCaptureは新版§5へ。既に十分残っていれば止められる意味を保ち、明示STOPをCaptureの名で延長しない。旧§5–9のCopy & Paste、Commit、Download、手動回復は新版§6と保存主カードへ接続した。

旧§10–11・17の安定した役割、状態と原則の分離、Doneの価値は新版§6–8へ。旧P_tasks等の命名例を現行の必須Pathにせず、現在の担当原本を案内する。旧§15–16の簡明さとVerify Before Doneは新版§8–9へ。短い規則という方針を回答品質の抑制へ転用しない。

### 4.2 Artifact → GitHub

完成Artifactの制作と保存の分離、保存手順の共通化、本文を失わないManual回復、Living Review Before Writeを保持。保存に必要な情報はCurrent ContextとOwnerから解決し、Humanによる全Path手入力を必須にしない。

一律の1ファイル1commit・直接操作1回・原則Downloadから、相互依存する変更単位、原因と状態に基づく回復、必要な受渡し方法へ整合した。保存後のRemote取得を明確化し、結果不明・並行変更・取消し・権限拒否を分ける。拒否を別Toolや手動経路で迂回しない。

既存save SkillとはOwner選択と完成Artifact配置の関係を示した。Skillの全面置換や本文複製、Work／Dots別の再作成は行わない。

### 4.3 Programming-like版

主カード優先、非実行の構造化説明、HumanのProgramming再学習を保持。IF／THEN／ELSE、Guard Clause、Invariant、State Machine、Test Caseの意味を、具体的な判断の違いへつなげた。

旧§9と§17の非success時の扱いにある書き分けを見直し、結果不明・技術的失敗・権限拒否をManualへ一括遷移させない形へ改訂した。疑似IMPORTを実際の同期と誤認させず、参照した主カードの版とCurrentの関係を明記。掲載ケースは構成例であり、実行済み試験ではない。

### 4.4 Torah Vision Lens

Scene → Structural Mapping → Precise Name／問い → 現在への応答という核を保持。Namingだけに縮めず、Creative Direction、Wonderや応答の余白、Thread Harvest以外の用途へ開く。No Forced Scene、Canon／Exegesis Guard、Root／Fruitを具体化した。

旧§12のDo not over-explainを創作上の条件として残し、一般的な説明省略の規則へしない。旧§13–14のThread-End接続は一用途として形成史へ。旧§17の二例はSourceが記した例であり、今回独立に実証した成功や現在の製品制限ではない。旧版のArk命名源という主張も、形成史の自己位置づけとして区別した。

## 5. 参照・Binding・履歴の扱い

基点mainで`ss_super-special`と三つの関連ファイル名を検索し、合計20の異なるファイルを取得して、Treeのblobと照合した。該当行と文脈から現在への案内、固定証拠、旧Runtime、形成記録を区別した。全20ファイルの全文意味読解・全Git履歴の網羅を主張しない。

現在のRoot READMEとAGENTSのCovenant案内を新版へ変更し、役割説明も合わせる。AGENTSでは同じRole Map内の「RuntimeとQuery」を現在の単一Prompt棚の説明へ整合する。v004の判断・権限・読取・実行の核は保持し、navigation patchの由来をmetadataへ残す。

Ark01のmanifest／thread-index、Ark02のharvest／handoff／phase-handoff、Ark05の当時のhandoff／harvest、2026-09-19のRepository診断、Ark21の実験的旧READMEは、当時の意味・引用・Path・SHAとして保持する。旧thread-end.mdへの参照は今回の四Promptとは別の退役履歴でもあり、一括置換しない。

旧資料を読む際は、その資料が指定するRef・版・SHA・EOFに従う。§3の固定版は今回移行直前の五原本への接続であり、それより古い指定版を置換しない。とくに旧Ark05のRequired Readには旧主カードが含まれるが、この変更をもってその旧Bootが新版で成功したとは扱わない。旧Current-path依存の再起動が必要になれば、指定契約の不足としてその操作を止め、固定Sourceの確認または明示的な互換移行を行う。

確認した現在のArk27:09の必須Source集合には今回削除する五Pathはない。Current SourceのAGENTSとGitHub入口は案内のみの改訂として整合を評価する。固定Sourceのハッシュを新版へ機械的に張り替えず、09のStateやHandoffをこの案件のために更新しない。

外部consumer、検索に出ない参照、別AIの実理解は通常Unknownとして残す。それらを全解消待ちのGateにせず、必要な現在の案内と本案件の変更範囲を確認する。

## 6. 実装範囲と保持した先行成果

対象は15Path：新四Promptと本記録の追加5、旧フォルダ内五ファイルの削除5、Root README・AGENTS・prompts/README・GitHub README・GitHub PLANの更新5。

GitHub PLANはcurrentと関連metadataを今回へ接続し、診断履歴以下の本文・過去の契約は末尾EOFの版表示以外を保持する。GitHub READMEは本STRの索引と必要metadataを更新する。ARCHIVEや__archivesへ新しい四原本コピーを作る案件にはしない。

ARC-007・009・010、STR-011–013、lesson JSONL採用、四Skillの共有・導入・限定確認、有限Board対話と所有先修正、自己改善Loopの成果と検証境界を先行成果として保持する。ARC-002の部分完了と元パス保留、別のGraph／One-Table固定Binding移行、旧Plan Mode v005試験の目的変更終了を混同しない。

Actorの出来事・BoardのCurrent・lessonの内容をここへ二重管理しない。Workをdot-0000として記録せず、保存を相手への送達としない。ChatGPT長期メモリをSourceや輸出対象にしない。Skill作成、新しいLoop試験、研究巡回、追加アーカイブ、house、Pet、過去生活Task、Reset、予定再作成、実際のThread移行は開始しない。

## 7. 実装・検証の証拠

実施した確認と公開結果をこの節へ記録する。公開前の作成や自己点検をRemote保存済み・別AIの実理解と扱わない。

公開前の確認では、15Pathの変更範囲、10書込対象のUTF-8・YAML・canonical_path・必要なExact EOF・code fenceを確認した。対象文書の相対Markdown参照220出現の到達Pathと、新規参照に含まれる節3件を確認し、不一致なし。固定基点の旧原本へのURLもTreeと照合した。全外部サイトの稼働や全Repositoryのanchorを検査した意味ではない。

AGENTSの第2節以降、Prompt棚の第4節以降、PLANのdiagnosis-history以降（末尾EOFの版表示を除く）の同一性を比較し、保持を確認した。旧五ファイルの準備Treeからの除去、ARKとsave Skillの同一性も確認した。主カードと補助版のPlan-only、結果不明、拒否、技術的失敗、並行訂正、関連変更、取消し、Remote未確認の八つの構成ケースを本文上で点検した。これは執筆者自身の文書Reviewであり、別AIによる独立読解やGitHubへの模擬書込試験ではない。

確認中に、環境では利用可能だがRepositoryには存在しないresolve-github-runtimeのSkillパスへのリンクを検出し、任意の利用可能Skillとしての説明へ修正した。共有原本の存在と環境でのSkill利用を混同しない。

公開準備中にmainが`ac355e59505dccdfec3e7c94b77e29b33145bd5f`へ進んだため、書込前に差分を確認した。追加は`references/README.md`一つで、改行のみ・blob `8b137891791fe96927ad78e64b0aad7bded08bdc`。本案件の15Pathとは重ならない。この並行Seedを保持した新headを公開基点に使う。空の入口の作成を、参照原本の整理完了や実利用の証拠とはしない。

ここまでの状態は準備・公開前確認。公開commitとRemote再取得の結果は、実施後に本節へ追記する。

## 8. 復元・Living Review・次の接続

復元・比較には§3の固定原本と本変更の差分を使う。新版へ後続編集が入った場合は、現在の内容と目的を先に照合する。Repository全体の巻戻しで他者の変更を消さない。旧フォルダの復活や旧Runtimeの再起動は、新しい目的と権限から判断する。

今回の見立ては、優れた旧Promptの価値を、現在の用途・責務・根拠から選べる形へ育てることが有効だというもの。文書の短縮やファイル数の減少だけを成功指標にしない。独自の意味が薄れた、参照の往復が増えた、主カードと補助版がずれる、という具体的Feedbackがあれば役割と本文へ返す。

今回の完了条件は、四本の改訂と意味保持、現在の案内、旧配置の除去、由来への接続、承認範囲の公開とRemote照合である。実際の使いやすさ・自然選択・別AIの理解・長期の協働効果は、実利用の観測から判断する。保存確認後はHuman Reviewへ返し、別候補を自動開始しない。

EOF::STR_014_SUPER_SPECIAL_PROMPT_MODERNIZATION::v001
