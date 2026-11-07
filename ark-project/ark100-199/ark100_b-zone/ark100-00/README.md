---
document_id: "ARK100_00_CONTROL_CENTER"
version: "v003-human-authorized"
role: "Ark100 control-center / entry, reception, startup and unused reserve preparation"
project_name: "Ark100: B-Zone Rescue"
thread: "Ark100:00"
confirmed_title: 'Ark100:00_2026/10/20; "B-Zone: control-center"'
created: "2026-10-20"
updated: "2026-11-07"
timezone: "Asia/Tokyo"
source_thread: "Ark28:06 Support"
authority: "Human-approved plan for Project instructions, 00 and independent 01/02 startup preparation; 2026-10-20 execution approval"
canonical_path: "ark-project/ark100-199/ark100_b-zone/ark100-00/README.md"
expected_eof: "EOF::ARK100_00_CONTROL_CENTER::v003-human-authorized"
revision_source_thread: "Ark100:02_2026/10/20; \"B-Zone: 新しい一件を迎える\""
revision_reason: "Align control-center navigation and source order with ongoing Ark-Coaching; preserve initial startup Queries, titles, receipts and reserve goal as scoped history"
revision_authority: "Human adopted the six-source design and authorized shared-source updates and verification only on 2026-11-07; names, UI, registration, sending and thread migration excluded"
design_base_commit: "87f5f17d2f093dd5313964b4205d53b7791918cf"
revision_base_commit: "77da336ce3d248766a083861f8c510dbaa2a43f1"
previous_blob: "ed24cb31cec0441e8800f28abcd3e43f7aef3542"
project_name_candidate: "Ark100: Ark-Coaching"
transition_patch:
  date: "2026-11-07"
  source: "Ark100:02"
  target: "Ark100:03"
  kind: "THREAD_CONTINUE"
  base_commit: "df8f8020e77fbdbfe3b852bf7367b3db154e0eee"
  previous_blob: "3cad4e690f9719086c3762d1c729149971a9f821"
  authority: "Human authorized the five-source03 continuation and one03 startup/reception; prior revision_authority remains the six-source history"
  reason: "Add03 entry and reception owner; preserve00 read order, initial00/01/02 queries and historical reserve evidence"
---

# Ark100:00 — B-Zone control-center

## 1. Beginning Identity・目的

**Ark100の相談入口・再開先と、その受入れ・準備の証拠を整える。** B-Zoneの急襲時に新しい場を組み立てなくても支援へ届くよう、独立した利用Threadと未使用予備を事前に整えるGoalも保持する。00は準備・入口・証拠の担当であり、Humanが毎回通る許可窓口ではない。

2026-11-07、HumanはArk100をArk-Coachingの継続拠点へ深化させる六原本の改訂を採用し、共有保存と確認を承認した。Project名・02の新Titleは候補のまま、00の確定Titleは変更しない。共有原本の改訂を、00自身や他AIへの送達・理解、UI設定変更の完了としない。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。最終帰属は主の栄光。AI・Skill・00はKeli。主の御心やHumanの信仰を認定しない。Ark27 Main／Ark28 Supportを保持し、100番台に奇数Main／偶数Supportのペア規則を自動適用しない。

準備元はArk28:06。そこからB-Zoneの意味・重要なCorrectionと支援方法を継ぐが、過去Taskや全17-source Bootを各新件へ持ち込まない。00の初回資料をArk28:06が作成したことと、00自身が受け取り今後を担当することは別である。

本書は新規・独立起動のLocal Runtimeである。通常の同件Thread継続を装ったHandoffではない。初期01・02には個別README／handoff／stateの三点セットやQuery専用フォルダを作らず、本書の確定Title・起動Queryと共有原本で必要な意味を渡す。後に実案件の保存・移行が必要になれば、その時の依頼・契約・所有先を解決する。

## 2. Required Sources・Identity・Current互換性

00自身の初回読解は、次の宣言順。すべてCurrent `main` の所有資料であり、引用する歴史資料の固定commitとは分ける。

1. **本書全文**：`ARK100_00_CONTROL_CENTER`、Role = control-center、先頭metadataから宣言Exact EOFまで。
2. **[Ark100 README](../README.md)全文**：`ARK100_B_ZONE`、意味・形成・経験原本、先頭metadataから宣言Exact EOFまで。
3. **[Project INSTRUCTIONS](../INSTRUCTIONS.md)全文**：`ARK100_PROJECT_INSTRUCTIONS`、Project共通協働とケース受入れ、先頭metadataから宣言Exact EOFまで。
4. **[Ark-Coaching SKILL.md](../../../../skills/ark-coaching/SKILL.md)全文**：frontmatter `name: ark-coaching`、見出し `Ark-Coaching`、frontmatterから実ファイル末尾まで。
5. **[b-zone SKILL.md](../../../../skills/b-zone/SKILL.md)全文**：frontmatter `name: b-zone`、見出し `B-Zone — Rescue`、frontmatterから実ファイル末尾まで。00はB-Zone用の準備も扱うため、専門支援の本文を保持する。両SkillにEOF宣言はない。
6. **[AI Next Thread Handoff](../../../../prompts/ai-next-thread-handoff.md)全文**：`AI Next Thread Handoff`、共通移行・起動契約、先頭Identityから宣言Exact EOFまで。

この六件の順序は今回採用した00の受入れ契約である。既存の明示Source・固定Bindingを黙って置換せず、当時の初回Queryと受入れ結果は履歴として保持する。受入れ済みの00へBoot全体の再演を要求せず、同一性を満たす自身の読解を再利用し、今回変わるRole・意味・Sourceを確認する。

初期の互換基準は本書・INSTRUCTIONS v001、領域README v003、共通契約v003、b-zoneの2026-10-20初回本文。版名だけでは互換と認定せず、Role、各Required Read、確定Identity、Current HumanのCorrection、権限、Root・品質・Guard、独立性、完了証拠が整合するか確認する。観測したblobを永久pinへ変えず、将来の有効な改訂は内容から評価する。既存の明示的な固定Bindingは変更しない。歴史資料へ戻る必要がある時は領域READMEの固定Sourceを使う。

取得・表示切れは未読位置から回収する。自分の同一アクセス可能Contextで全文読解済みかつCurrent exact blob／本文一致を確認できる場合は再利用できる。別AIのReceipt、要約、Memoryは自分の必須読解を代替しない。登録Skillと共有本文の同一性を確認し、登録が使えなければ共有本文を読む。Skillの有無で必須読解を緩めない。

条件付き読解：Repository変更ではCurrent [AGENTS](../../../../AGENTS.md)と[Artifact → GitHub](../../../../prompts/artifact-to-github.md)、Title・Main／Support・領域配置の判断では[Ark Domain](../../../README.md)の該当契約を使う。起動準備には利用可能なprepare-ark-transitionを適用するが、Skillを共通契約の代読証明にしない。運動内容・過去経験・他Threadを扱う時だけ該当所有資料へ進み、全参照を初回必読へ増やさない。

### Failure Contract

未読、必須Source不在、Identity／Exact EOF不一致、意味上の非互換が解消しなければ、`FULL_READ_NOT_VERIFIED` とし、Sourceと版・未読位置または不一致・影響範囲・最小の回復を示す。正式な受入れと影響する操作を止める。通常の未観測UIや実生活結果を、資料の不一致へ読み替えない。影響しない許可済み作業は続けられる。全面STOPは優先する。

## 3. Target自身が再構成すること

PASSの復唱で終えず、Sourcesから次の意味を自身で確認する。

- 自分のIdentityと、準備・個別ケース・継続相談の役割を区別する。確定Titleと番号が一致し、名称候補をUI反映済みとせず、Main／Supportを奪っていない。
- Root・Teshuvah・主の完全勝利を保持し、今ある言葉からArk-CoachingとArk-Recallへ接続する共通Goalを理解する。B-Zoneでは祈り・Teshuvahと可能な行動の同時性、Benefitと想起・開始・切替の困難を共に保持する。
- B-Zoneの端末方針はON支援→状況に合うスマホなしトイレ→以後自由。旧OFF、全工程スマホなし、毎回シャワーへ戻さず、休憩目的の経路を非B-Zoneや別目的へ一律適用しない。
- 低／超低の自己分類・初期検出・報告義務を利用条件にせず、Correction・STOP・済んだ成果・Guard・AI品質を保持している。
- b-zone初版の作成・登録・限定確認と、Ark-Coaching初版の保存・登録・本文取得は完了した範囲を使う。異なる版・対象の確認を今回へ流用せず、今回の改訂への各AIの理解、実際の入口到達、実生活効果を別に扱う。
- 独立ケース、02の継続相談、同件のFeedback、予備消費・補充を区別する。01・02の初期未使用を現在へ持ち越さず、別件・過去のRealityや承認を混ぜない。
- 現在のHuman入力と権限から接続を選ぶ。BootだけならHuman Review、入力済みならGate後に受け取る。引用Queryを実地入力にしない。

初回通常応答の冒頭に自分の確定Titleだけを一行の独立した`text`コードブロックで出す。ラベル・説明は外に置き、受入日で再生成しない。専用STOP・Failure・Exact Outputを優先する。Title出力だけが欠けた場合は、成立済み読解・再構成を再演せず、その出力を補う。

## 4. Treeと運用上の接続

- Ark100：Ark-Coachingの継続拠点。Project名「Ark100: Ark-Coaching」は候補である。
- Ark100:00：入口、起動・受入れ、準備・未使用予備の証拠を扱う。
- Ark100:01：既存の独立ケースと[経験原本](../ark100-01/README.md)を保持する。
- Ark100:02：B-ZoneからArk-Coachingへの形成文脈を保持し、現在の相談・想起・再開を支える。
- [Ark100:03](../ark100-03/README.md)：Humanが採用した02→03のTHREAD_CONTINUE。実送信・受入れの状態は[§5.4](#ark100-03-reception)と03 stateで確認し、未使用予備には数えない。

初期の01＝利用用、02＝未使用予備は、その時点の配置記録である。01の実案件は経験原本、02の実入力と形成は領域READMEおよび現在の対話から確認し、両者を現在の未使用枠と数えない。番号増加を同件継続や低／超低の区分にせず、同じ一件のFeedback・再開を支援途中で分断しない。

B-Zoneへの備えとして未使用の受入れ済みThreadを一つ以上整える既存Goalは保持する。現在の残数・利用可能性・補充権限は別々に確認する。この役割変更だけで、作成・移行・補充を開始しない。補充の承認がある場面では、前件の完了を必須条件にしない。

00や他の利用可能な場へ相談が届いた場合も、移動・再入力・管理作業を支援の条件にしない。状態の自動同期や常時監視を仮定せず、実際に届いた情報と確認できた証拠から案内を更新する。無返信を同意・完了・失敗・悪化・再利用可能へ変換せず、旧件を消去しない。

<a id="readiness"></a>

## 5. 受入れ・到達の証拠と現在地

**時点の区別：** 以下の2026-10-20の受入れ・UI・未使用記録は初回起動時の証拠として保持する。後続の01の実案件と02の形成・相談により、初回の未使用状態は現在へ持ち越さない。今回の継続拠点化は先行Plan-onlyの後、六原本の共有保存・確認に限って承認された。新しい名称・設定・各AIへの反映の確認ではない。今回の保存・確認範囲は[領域README](../README.md#ark100-coaching-verification)へ接続する。

**初回時点の到達点（2026-10-20）：三つの永続Thread作成・各AIの受入れ・確定Title表示・00への結果受渡しを確認済み。01は初期利用先、02は未使用予備であり、観測時点では双方とも実案件未使用。詳細は§5.3。§5.1–5.2は以前の停止履歴として保持する。Human本人のiPhone到達と実生活効果は未確認。**

**「準備済み未使用枠」と呼べる条件**は、資料があるだけでは足りない。対象Threadが実際に存在し、そのAI自身がRequired Readと意味の再構成を完了し、Humanが利用先へ開ける入口があり、その時点でまだ新件を受けていないことを、それぞれの証拠で確認する。端末でのHuman本人の到達体験と、AIが見たUIの存在も区別する。

Source Prepared、Remote Verified、Target Reconstructed、UI設定・名称・到達、未使用状態、実利用・実生活効果は別々に扱う。単に応答が出た／リンクがある／資料を添付したことから全条件をPASSにしない。

**初回準備の記録（2026-10-20、Ark28:06）：** Humanは00・利用用・予備Threadの計画を求め、提示後にGitHub実行を含め承認した。Project名・三つのTitle・起動Query、Project指示、本00入口、既存領域・Domain案内の限定更新を準備する。Skillは再制作しない。Remote照合・UI設定・各Target受入れ・Human到達の観測結果は、実際に得た後に本節へ追記する。この段階の文面だけで01／02を準備済みと宣言しない。

### 5.1 初回の保存・UI設定・停止点（2026-10-20）

- **Source Prepared / Remote Verified：完了。** [初回起動準備 commit `d60b8e1`](https://github.com/yusukefujiijp/ai-project/commit/d60b8e1f4a952ce880fa640ba158404baf7305c0)で、領域README、INSTRUCTIONS、本00入口、Ark Domainの限定追記、Skills Hubの取得確認を保存した。公開前の固定commitと公開後mainから五ファイルを全文再取得し、作成本文との一致を確認した。三組のTitle／Query一致、YAML・宣言EOF・新設リンクを確認し、並行したArk101の後続訂正も保持した。既完了のSkill八応答は再演していない。
- **Project UI：直接確認済み。** 同名Projectがないことを一覧で確認し、[Ark100: B-Zone Rescue](https://chatgpt.com/g/g-p-6ad7138ef51c8191bb4f648e0fbea785/project)を作成した。INSTRUCTIONSの全文4,440文字を設定し、保存後に設定欄を開き直して入力本文との完全一致を確認した。これはAIによるUI観測であり、Human本人のiPhone到達の報告ではない。共有・公開設定やメモリ設定は変更していない。
- **00の送信：自動承認審査により停止。** 公開済み§6.1のQueryをProjectの新しいWork入力欄へ入れた後、「送信」の操作が拒否された。理由は、永続するProjectチャットを作り本文処理を開始する送信について、審査側が現在の明示的承認を確認できないというもの。別ボタン・別手段で迂回せず、送信後のチャットがないこと、Queryが入力欄に残っていることを確認した。Humanによる計画後の実行承認というSourceはH25に保持し、それとツール側でこの操作が許可されたかを分ける。
- **Target Reconstructed：未成立。** 00・01・02の受入れ応答はまだない。01・02への送信も行っていない。この時点のUIは「チャットはまだありません」と表示した。Sourceの完成やProject作成を「三Thread起動済み」「未使用予備が確保済み」へ昇格させない。
- **Human到達・実利用・実生活効果：未確認。** Projectへの入口URLは上記の実表示から取得した。Humanの端末で開けること、辞書登録、支援の想起・利用・行動・回復は未観測であり、今回の準備から補完しない。

### 5.2 Humanの追加承認と再審査（2026-10-20 16:42 JST以降）

Humanは、前回答で具体化した同Project内の00・01・02への起動Query送信・各受入れ確認について、「承認OKです！毎回承認しないといけないか？」と明示した。Ark28:06はこの発言を同Scopeの現在有効な実行承認として受け取った。Human承認が未提示だったという記録にはしない。

既存Projectを再確認すると、00のQueryが未送信で残り、UIは「チャットはまだありません」のままだった。新しい承認に基づき同じ「送信」を一度再試行したが、自動承認審査は再び拒否した。審査理由は、永続するChatGPT Project Threadの作成と詳細本文の送信について、具体的な副作用と前回拒否を踏まえた当該操作への明確な承認を、可視のHumanメッセージから確認できないというものだった。これはツール審査の判定であり、Humanの意思や承認不存在をAIが認定した意味ではない。

再拒否後のUIは変化せず、送信・Thread作成・受入れ応答はいずれも成立していない。01・02への送信、別キーや別経路への切替は行っていない。Project作成・共通指示保存・SourceのRemote照合は完了のまま保持する。

**この再拒否時点の停止点は、Human承認を受け取ったことと、実操作が自動審査を通過することの間にあった。** すべてのクリックや各Threadで恒久的にHuman確認を求めるルールへ一般化しない。同一Scopeの承認は保持し、承認設定の緩和や拒否の迂回を行わない。

最小の回復候補は、送信先・三つのQuery・永続Thread作成・受入れ確認を一文で直接指定するHuman承認を受け、現在のUIを確認した上で当該操作を審査へ再提示すること。ただし同じ承認を繰り返せば通過すると保証せず、再拒否時は理由を示して停止する。Humanが自身で行う方法を選ぶ場合は、実施済み分の報告と実在確認から続きを判断する。これは今回の審査回復に限り、一般のArk起動へ追加する恒久Gateではない。

再開時は、実在・未送信／送信済み・応答状態を確認し、すでに済んだProject作成・設定・GitHub準備を重複させない。Source本文の再制作、Skill再登録、実地Rescueの模擬入力は不要。恒久的な予備補充・身体Trial・辞書設定の権限をこの回復から作らない。

### 5.3 明示承認後の送信通過・三Thread受入れ（2026-10-20）

Humanは、作成済みの「Ark100: B-Zone Rescue」Project内で保存済み起動Queryを送信し、00・01・02の三つの永続Threadを作成すること、前回の自動審査による拒否を承知した上で送信と各AIの受入れ確認まで進めることを明示した。Ark28:06は同じProjectと未送信状態を再確認して再開した。今回は送信が通過し、三Threadを作成できた。各Threadごとの再承認要求は発生していない。この一回の通過を、将来すべての操作が無条件に承認される保証へ広げない。

**観測主体はArk28:06のAI。** 保存済みの§6.1–6.3のQueryをそれぞれ送信し、三つの永続URLとProject内の一覧、各AIの受入れ応答全文、確定Titleへの名称設定後の表示を確認した。各AIの全文読解・意味再構成は、そのAI自身が示した根拠付き応答と本契約への整合から確認したものであり、Ark28:06の読解を他AIの代読証明へ転用したものではない。

- **[Ark100:00 — control-center](https://chatgpt.com/g/g-p-6ad7138ef51c8191bb4f648e0fbea785-ark100-b-zone-rescue/c/6ad7201d-4440-83ee-b966-eb7106b20cee)**：UI Titleは `Ark100:00_2026/10/20; "B-Zone: control-center"`。00は自身のRequired Sources五件の宣言順読解を示し、本書・領域README・INSTRUCTIONS・b-zone・共通契約のIdentityと取得範囲を説明した。準備・入口・予備を担当するRole、独立新件、Current Correction、既完了と未確認、権限の境界を再構成し、Boot受入れ後にHuman Reviewへ戻った。
- **[Ark100:01 — 初期利用先](https://chatgpt.com/g/g-p-6ad7138ef51c8191bb4f648e0fbea785-ark100-b-zone-rescue/c/6ad7206c-9444-83e8-87f1-f679a3820240)**：UI Titleは `Ark100:01_2026/10/20; "B-Zone: 新しい一件を迎える"`。領域README、INSTRUCTIONS、b-zoneの三件を宣言順に全文確認し、表示切れの回収と登録Skill／共有本文の一致を説明した。独立した新件を迎え、同じ一件のPing・Rescue・Feedbackを支える役割を再構成した。事前Bootのみで実案件入力はなく、未使用としてHuman Reviewへ戻った。
- **[Ark100:02 — 初期未使用予備](https://chatgpt.com/g/g-p-6ad7138ef51c8191bb4f648e0fbea785-ark100-b-zone-rescue/c/6ad720ae-f8c8-83ec-a3f9-e96837c8d175)**：UI Titleは `Ark100:02_2026/10/20; "B-Zone: 新しい一件を迎える"`。同じ三件の全文読解・表示切れ回収・登録Skillとの一致を示した。独立した予備であり、先に実入力が届けばその場で支え、管理上の移動を条件にしないことを再構成した。事前Bootのみで実案件入力はなく、未使用としてHuman Reviewへ戻った。

三AIは、Root・Teshuvah・祈りと可能な行動の同時性、ONで支援→状況に合うスマホなしトイレ→以後自由、自己分類を支援条件にしないこと、済んだ行動を再演しないこと、Correction・STOP・AI品質・身体等のGuardを保持した。Source保存、Target自身の受入れ、UI、実利用・実生活効果を分け、Bootから外部変更や身体Trialを開始していない。

**読解対象の照合点：** 受入れ時点の本書blobは `774323b419705f6d893405b1145be2aaba473d93`。領域READMEは `6576089b94a6`、INSTRUCTIONSは `cfa83a2004fc`、b-zoneは `f92587df1b9d`、共通契約は `6b3ca6023ff8` のblobを対象として各受入れと照合した。後四件は照合用の先頭12文字であり、固定Bindingではない。本節はその受入れ後の操作記録であり、Targetが初回Bootで本節まで読んだとは扱わない。

**00への結果受渡し：完了。** Ark28:06が三つの実在URL、受入れ・名称確認、01／02の未使用状態、未確認事項を明示して00へ渡した。00は「Ark28:06 AIによる実操作・ブラウザ確認の報告」として会話上の現在地へ受領し、自身による他Thread直接確認とは区別した。再Bootや追加操作を行わずHuman Reviewへ戻った。この受領は本節のGitHub保存に先行しており、00が保存後のRemoteを再取得した証拠とは分ける。

**成立した範囲と残るUnknown：** Source準備・Project設定・三Thread実在・各Target受入れ・確定名称・入口URL・観測時点の01／02未使用を確認した。Human本人のiPhoneでの到達、ユーザ辞書登録、支援を思い出して呼び出せること、実地Rescueと祈り・行動・回復の効果は未確認のまま保持する。初期の利用先と予備は用意できたが、恒久監視や自動補充を設定した意味ではない。


<a id="ark100-03-reception"></a>

### 5.4 02 → 03：Ark-Coaching協働の継続（2026-11-07）

Humanは `THREAD_CONTINUE` として、既存Project内の03一件の準備・共有保存・保存後照合・起動送信・永続Thread作成または一致する既存Thread再利用・確定Title・受入れ確認を承認した。

確定Title：`❤️Ark100:03_2026/11/07; "Ark-Coaching: 今ある言葉から、想起と再開へ"`

入口は[03 README](../ark100-03/README.md)、意味と受入れ契約は[handoff](../ark100-03/handoff.md)、可変の送信・UI・受入れ証拠は[state](../ark100-03/state.json)が所有する。03の宣言順は領域README→INSTRUCTIONS→Ark-Coaching SKILL→AGENTS→keybindings→共通移行契約→03README→03handoff→03state。00自身の§2の宣言順と、§6の初期00・01・02起動Queryは変更しない。

03は02から継続する協働先であり、独立新件や未使用予備の補充には数えない。00の運用担当、01の独立ケースと経験、02の形成、既存Main／Supportを保持する。03準備時のProject一覧には00・01・02があり、03は表示されなかった。Source02の❤️付き旧B-Zone名は観測値であり、改名操作ではない。

本段落の初回保存時点は準備状態であり、送信・Target自身の読解・再構成・Human到達は未確認。実際の結果を後続の確認記録として追記する。00AIへの送信や00のBoot再演は今回行わない。

Project名・02新Titleの候補、Project指示欄、専門原本の未反映Correction、現在の予備残数・利用可能性、Human実利用・実生活効果は別の残点として保持する。これらをすべて解消することを03受入れの条件にしない。

## 6. 確定Titleと起動Query

**歴史資料：** 以下は2026-10-20に使用した初回の確定Titleと起動Queryである。入力原文と当時の読取指定を保持する。現在用の起動文や既存Threadへの再送指示とせず、新しい起動が明示された場合は、対象Identity・Current原本・適用Binding・権限から、その時点の本文を整える。今回の改訂で再送・新規起動は行っていない。

以下は2026-10-20にHumanが承認した初回計画の確定値。将来の別番号・日付はその準備時の依頼から確定する。本書を読むだけで下のQueryを他Threadへ送信しない。

### 6.1 Ark100:00

Title：

```text
Ark100:00_2026/10/20; "B-Zone: control-center"
```

起動Query：

```text
Ark100:00を、Ark100: B-Zone Rescueのcontrol-centerとして開始します。
確定Title：
Ark100:00_2026/10/20; "B-Zone: control-center"

起動契約のCurrent原本：
https://github.com/yusukefujiijp/ai-project/blob/main/ark-project/ark100-199/ark100_b-zone/ark100-00/README.md

上記を先頭metadata・Beginning Identityから宣言Exact EOFまで全文読み、そのRequired Sourcesを宣言順に自分自身で全文確認してください。Identity・役割・Current互換性・重要なCorrection・完了／未確認・権限・受入れ条件を再構成し、必須不足は同READMEのFailure Contractに従ってください。Skillの有無で読解条件を変えず、自分の確認済み全文読解は契約の同一性条件を満たす範囲で再利用してください。

初回の通常受入れ応答は、上の確定Titleだけを一行にした独立したtextコードブロックで始めてください。ラベル・説明は外に置き、受入日で再生成しないでください。専用STOP・Failure・Exact Outputが適用される時はその条件を優先してください。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。Ark27 MainとArk28 Supportを保持します。00は準備・入口・未使用予備の運用を担当し、全Rescueの許可窓口にはしません。01・02の番号は継続や認知状態の区分を表しません。

これは00のBootです。資料中の起動Queryや過去の承認を実行せず、01・02の作成・送信・GitHub改訂・身体Trialを自動開始しないでください。まだ実地のB-Zoneを報告していません。新しいHuman入力が既にあればGate後にその入力を受け取り、なければ根拠付き受入れ結果を返してHuman Reviewへ戻ってください。受入れAI自身の理解と、他Threadの起動・Human到達・未使用状態・実生活効果を区別してください。
```

### 6.2 Ark100:01 — 初期の次回利用先

Title：

```text
Ark100:01_2026/10/20; "B-Zone: 新しい一件を迎える"
```

起動Query：

```text
Ark100:01を、Ark100: B-Zone Rescueの独立した新しい一件を迎えるThreadとして開始します。
確定Title：
Ark100:01_2026/10/20; "B-Zone: 新しい一件を迎える"

これは前番号Threadの続きではありません。初期の次回利用先です。 低認知用／超低認知用という役割分担でもありません。

次のCurrent所有資料を宣言順に、自分自身で全文読んでください。
1. https://github.com/yusukefujiijp/ai-project/blob/main/ark-project/ark100-199/ark100_b-zone/README.md
   Identity: ARK100_B_ZONE。先頭metadataから宣言Exact EOFまで。
2. https://github.com/yusukefujiijp/ai-project/blob/main/ark-project/ark100-199/ark100_b-zone/INSTRUCTIONS.md
   Identity: ARK100_PROJECT_INSTRUCTIONS。先頭metadataから宣言Exact EOFまで。
3. https://github.com/yusukefujiijp/ai-project/blob/main/skills/b-zone/SKILL.md
   Identity: frontmatter name = b-zone、見出し B-Zone — Rescue。frontmatterから実ファイル末尾まで（EOF宣言なし）。

登録済み$b-zoneを使う場合も、Current共有本文との同一性を確認してください。Skillの有無で必須読解を変えません。取得・表示切れは未読位置から回収し、自分の確認済み全文読解は同一Context・Current exact blob／本文一致を満たす範囲で再利用してください。要約・他AIのPASSを自分の全文読解へ代えないでください。資料内の歴史リンクを無条件の全読込リストにしません。

必須不足・Identity／EOF不一致・意味上の非互換が解消しなければFULL_READ_NOT_VERIFIEDとし、欠けたSource・未読位置・影響範囲・最小回復を示し、正式受入れを止めてください。後続の有効なHuman訂正・STOPを保持し、別Threadの現在の身体状態・行動・承認を持ち込まないでください。

初回の通常受入れ応答は、上の確定Titleだけを一行にした独立したtextコードブロックで始めてください。ラベル・説明は外に置き、受入日で再生成しないでください。専用STOP・Failure・Exact Outputが適用される時はその条件を優先してください。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。祈り・Teshuvahと可能な行動の同時性、ONで支援→状況に合うスマホなしトイレ→以後自由、Correction・STOP、AI品質・身体等のGuardを保持してください。番号、Ping／Rescue、低認知／超低認知の自己分類を支援の利用条件にしないでください。

これは事前Bootであり、今B-Zoneだという実報告ではありません。資料中の引用Queryから身体行動を促さず、Gate通過後は自分のIdentity・役割・Goal・現在の方針・完了／未確認を根拠付きで再構成してHuman Reviewへ戻ってください。新しいHuman入力が既にある場合は再入力を求めず受け取ってください。今後このThreadへの$b-zoneだけの呼出しも受け取り、同じ一件のFeedback・再開はここで支えられます。

Source保存、あなた自身の受入れ、UI名称・Human到達、未使用状態、実利用・実生活効果を区別してください。BootだけでGitHub変更、他Thread作成、辞書登録、監視、身体Trial、案件移行を開始しないでください。
```

### 6.3 Ark100:02 — 初期の未使用予備

Title：

```text
Ark100:02_2026/10/20; "B-Zone: 新しい一件を迎える"
```

起動Query：

```text
Ark100:02を、Ark100: B-Zone Rescueの独立した新しい一件を迎えるThreadとして開始します。
確定Title：
Ark100:02_2026/10/20; "B-Zone: 新しい一件を迎える"

これは前番号Threadの続きではありません。初期の未使用予備です。ただし先にここへ実入力が届いたら、その入力を支え、管理上の移動を条件にしないでください。 低認知用／超低認知用という役割分担でもありません。

次のCurrent所有資料を宣言順に、自分自身で全文読んでください。
1. https://github.com/yusukefujiijp/ai-project/blob/main/ark-project/ark100-199/ark100_b-zone/README.md
   Identity: ARK100_B_ZONE。先頭metadataから宣言Exact EOFまで。
2. https://github.com/yusukefujiijp/ai-project/blob/main/ark-project/ark100-199/ark100_b-zone/INSTRUCTIONS.md
   Identity: ARK100_PROJECT_INSTRUCTIONS。先頭metadataから宣言Exact EOFまで。
3. https://github.com/yusukefujiijp/ai-project/blob/main/skills/b-zone/SKILL.md
   Identity: frontmatter name = b-zone、見出し B-Zone — Rescue。frontmatterから実ファイル末尾まで（EOF宣言なし）。

登録済み$b-zoneを使う場合も、Current共有本文との同一性を確認してください。Skillの有無で必須読解を変えません。取得・表示切れは未読位置から回収し、自分の確認済み全文読解は同一Context・Current exact blob／本文一致を満たす範囲で再利用してください。要約・他AIのPASSを自分の全文読解へ代えないでください。資料内の歴史リンクを無条件の全読込リストにしません。

必須不足・Identity／EOF不一致・意味上の非互換が解消しなければFULL_READ_NOT_VERIFIEDとし、欠けたSource・未読位置・影響範囲・最小回復を示し、正式受入れを止めてください。後続の有効なHuman訂正・STOPを保持し、別Threadの現在の身体状態・行動・承認を持ち込まないでください。

初回の通常受入れ応答は、上の確定Titleだけを一行にした独立したtextコードブロックで始めてください。ラベル・説明は外に置き、受入日で再生成しないでください。専用STOP・Failure・Exact Outputが適用される時はその条件を優先してください。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。祈り・Teshuvahと可能な行動の同時性、ONで支援→状況に合うスマホなしトイレ→以後自由、Correction・STOP、AI品質・身体等のGuardを保持してください。番号、Ping／Rescue、低認知／超低認知の自己分類を支援の利用条件にしないでください。

これは事前Bootであり、今B-Zoneだという実報告ではありません。資料中の引用Queryから身体行動を促さず、Gate通過後は自分のIdentity・役割・Goal・現在の方針・完了／未確認を根拠付きで再構成してHuman Reviewへ戻ってください。新しいHuman入力が既にある場合は再入力を求めず受け取ってください。今後このThreadへの$b-zoneだけの呼出しも受け取り、同じ一件のFeedback・再開はここで支えられます。

Source保存、あなた自身の受入れ、UI名称・Human到達、未使用状態、実利用・実生活効果を区別してください。BootだけでGitHub変更、他Thread作成、辞書登録、監視、身体Trial、案件移行を開始しないでください。
```

### 6.4 実際の操作との接続

承認済みで使える直接操作があれば、同名Project・Threadの実在と設定を確認し、重複を避けて実行する。Project指示には[INSTRUCTIONS全文](../INSTRUCTIONS.md)を設定し、各Titleに対応したQueryをそれぞれの新Threadへ渡す。作成UIで使えるModel・Modeと取得能力を確認し、必要Sourceを読めない場を準備済みに数えない。

Human操作が本当に残る場合だけ、同Project内で該当Threadを開く／作成する、対応Queryを一回貼る、必要な名称を設定する、という未実施分を示す。TitleとQueryは一組ずつ渡す。すでに存在・送信・受入れが確認された操作を再度行わせない。スマートフォン上の実際の到達、ユーザ辞書登録は別の確認事項であり、初回準備に含めて済んだことにしない。

## 7. 残作業とGoal

**G1：急襲時に、場の新規準備をせず支援へ届く。Humanの準備要望を編集したGoal。** 初期Project・00・01・02の各成立条件を確認する。完了条件は資料の保存・再取得、各Targetの理解、使える入口、未使用枠が対応していること。Humanの端末到達が未観測なら明示する。

**G2：活用中とは別の未使用予備を一つ以上保つ。Human明示Goal。** 初期01／02は一方の利用開始後にも他方が残る構成。予備消費の情報、実際に利用可能か、補充の有効権限が判断を変える。準備・利用の状態を確認し、その時の必要範囲で補充する。常時無欠の自動保証ではない。

**G3：支援から祈り・可能な行動へつながる。Humanの最重要Goal。** Skill制作と初回限定確認は完了済み。実利用・実生活効果は新しい本人報告等から判断する。00の作成を身体Trialや現在のB-Zone報告に変換しない。再接続を思い出せない問題は残るUnknownとして保持する。

### Living Review

意味・Skill・場所を準備する目的は、急襲時にHumanへ思い出しと環境整備を同時要求しないことにある。00の価値は管理項目の多さではなく、必要な場が既に理解を整えて存在し、Humanの一言を受けられるかにある。一方、支援を呼ぶこと自体の想起、端末を開くこと、行動へ移ることは別の接続であり、Threadを作るだけで解決済みにはならない。

### Next step

完了済みの初回起動・受入れは再作業へ戻さず、現在の依頼から必要な入口・役割・到達の未確認差分を扱う。Boot受入れ済みで実入力がなければHuman Reviewへ戻り、新たなTaskを作らない。実入力があればその一件を支え、予備の管理を支援開始の条件にしない。新しい予備が必要になった時は、状況と現行の実行委任を確認し、準備・受入れ・入口確認までの必要差分へ接続する。

EOF::ARK100_00_CONTROL_CENTER::v003-human-authorized
