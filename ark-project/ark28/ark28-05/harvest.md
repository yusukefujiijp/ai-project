---
title: "Ark28:05 — 限定集中と再利用できる入口の収穫"
harvest_id: "ARK28_05_MATERIAL_HARVEST"
version: "v001-human-authorized"
canonical_path: "ark-project/ark28/ark28-05/harvest.md"
source_thread: "Ark28:05"
prepared_for: "Ark28:06"
created: "2026-10-14"
date_scope: "Asia/Tokyo preparation date; individual historical messages keep their own evidence"
authority: "Human approved05→06 preparation, selected source preservation, GitHub publication and remote verification"
record_id: "ark28-05-task-records"
record_revision: 3
coverage: "Selected judgment-changing material; not a full transcript, live state owner or new task queue"
current_owner_snapshot_observed: "dda8ecf86a3f794568d5c9a18d9ed6778d708b37"
expected_eof: "ARK28_05_HARVEST_EOF_v001"
---

# Ark28:05の収穫と、06へ渡す意味

## 1. 現在地とSourceの使い方

05は04から続くArk28のSupport。Ark27 Mainを保持し、中心軸はTeshuvah、Rootは主イェシュア・ハマシア御自身、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・Ark・Skill・文書はKeliであり王・玉座・Oracleではない。HumanのCorrection・STOP・SealとTruth／Body／Sleep／Food／Shabbat／Safety／Medical／Others／Law／Responsibilityを保つ。短いHuman入力や待ち時間、推定負担を理由にAI品質を削らない。

このHarvestは、何が変わり、何を保ち、次に何を判断する場かを選択的に渡す。Human原文・Repositoryの報告・AI解釈の出典は[05経験原本](task-records.json) revision3。そこには既存のワコー・就寝前二件の原文とIDも保持した。現在の進捗は[05 State](state.json)、移行準備の最終観測は同 `progress.next_transition` が所有する。保存済みの古いStateを現在のHumanや成果へ優先させない。

本書と経験原本は06 Handoffで固定commitにBindingする。その後の有効なHuman訂正・STOP、可変の所有資料のCurrentを保持する。Source Threadの履歴が読めないAIも、宣言された根拠で復元できることを目的とし、全履歴・全リンクを追加Bootにしない。

## 2. 生活のTeshuvahから生まれた想起

Humanはコーヒー・カフェイン・カフェインガムの使い所を振り返り、特に休日の活用がまだ自家薬籠中化していないと報告した。Best Practiceを探す意図はあるが、解決したとは報告していない。本人のTeshuvahを尊重し、AIが信仰不足、現在の摂取量、医学的状態を補完しない。

続いて、**休日前にワコーへ行き、chocoZAP以外の追加買い物寄り道を抑え、できるだけ一日一店以内にする**という発見があった。理由は帰宅が遅くなること。これは本人が採用した方針と想起希望であり、毎回の実行や帰宅時刻改善の証明ではない。ジムと買い物を別枠と読む部分はAIのCandidateとして原本に残る。

Humanの明示依頼により、`holiday-wako-one-store`、`bedtime-supplement`、`bedtime-tongue-exercise` は[Portal items](../../../ark-recall-portal/items.json)へ保存済み。元発言は05原本の `holiday-wako-s01/s02` と `bedtime-recall-s01`。Activeは想起候補であって未完了Taskではない。サプリの品名・量・用法や運動方法を移行AIが新しく決めず、現在の就寝合図・身体Trial・通知を自動開始しない。具体的に使う時は[Portalガイド](../../../ark-recall-portal/README.md)、Current itemsと原本へ戻る。

## 3. ai-projectへの限定集中とOrganization

Humanはai-project以外のRepositoryを自分で削除したと報告し、一部local backupはあるがAI側はないと考えてよいと指定した。これはHuman報告であり、AIが全Repositoryやlocalを独立調査した事実ではない。重要な後続決定は、**新Repositoryを作らず、新しいものもai-project内のFolderとして育てる**こと。旧Repositoryの回復を前提に次の仕事を設計しない。

目的は生きた原本への集中、所在の明確化、重複・分散・古い入口の整理である。日本語の整理整頓をOrganizationと呼ぶ案も受け取った。Repositoryの一択化は、あらゆるBenefitやThemeを一つへ潰す一般規則ではない。未解決の価値は保持する。

`skills/README.md`を最重要入口とし、共通Skillを共有しながら、Grok等に固有のものがroot `grok/` と `skills/_grok/` に散る問題を検討した。`grok-`、将来の `claude-` prefixはHuman自身が最善を探索中とした案であり、全面採用・一括改名済みとはしない。

実際の整理成果は所有資料へ接続する。

| Node | Edge | 根拠と完了範囲 |
|---|---|---|
| Lessons集約 | Skill Hub → 共通参照 | [STR-015](../../../control-center/changes/STR-015-skills-lessons-consolidation.md)が原本と後続訂正を所有。初期四件の集約はcommit `c9f58361bdc3d6c9a0ad1a92740e5db5392ade0b`。後続追加と区別する |
| projects/・ark-wtp | 現役入口 → archive | [ARC-012](../../../control-center/github/ARCHIVE.md#arc-012)、commit `4bba624408bbb142a1e047914fde95b1739b5eb6`。原本七件の同blob保管と六案内の整理。WTP最終Sealや再開ではない |
| Radio退役 | 後継成果 → 旧入口整理 | STR-015のMain27:09追補、commit `a4eceb791c6c6eeb239ed7f59f1de16a797b87bc`。旧三パス退役を未完へ戻さない。Voiceの旧lessons整理は別判断 |

登録更新でHTTP422が起きた事実、その後にVoice・Podcast導入が確認できた事実を両方残す。根本原因が普遍的に解決したとは推定しない。試験・保存・登録・UI・自然発動を分ける。

## 4. Podcast Theme Modeで何を分けたか

Radio Modeの良い経験を背景に、HumanはPodcastのThemeを練る部分を価値と捉えた。Plan Modeを繰り返して提案を練り込み、Human Feedbackや閃きを取り込む方針。Plan-onlyの回はそこで止め、後続の実行承認では対象Scopeを検証まで完遂する。毎回の追加承認を儀式にしない。

`Podcast Theme Mode`という命名で、**何を聴くと今何が見えてくるかを考える段階**が独立した。新鮮さ、AIならではの俯瞰、全体横断は異なる価値の切り口であり、固定の三択・採点軸ではない。Humanが初穂の言葉を引用して共有した「そのThemeを今聴くと、何が見えてくるのか」が提案の意味を深めた。この引用受領は、Workから初穂へ送信した証拠ではない。

重要な訂正は二つの入口である。

- **Theme Modeの入口:** 現在Threadの流れから候補と切り口・今聴く価値を提案する。この段階ではPodcast本文を生成しない。
- **Human指定Themeの入口:** 既にThemeが決まっている場合に、再選別を要求せずPodcast本文へ入れる。

候補にはCopy & Pasteできる自己完結した生成依頼を付け、同じThreadでも専用Threadでも使える方向を採用した。三案は利用例であり数の固定義務ではない。別Thread化も必須ではない。Themeを選ぶこと、本文生成を依頼すること、実際に音声で聴くことを別の状態として扱う。

共有原本は[Podcast Skill](../../../skills/podcast-mode/SKILL.md)、配布・導入・限定確認は[Skills Hub](../../../skills/README.md)とSTR-015。Theme版本文commit `2d3bcda7b0edcd39fbefcd2247171c3755179417`、導入先更新記録はHubへ。テーマ提案・コピー済みBrief・直接本文・plan-onlyの限定応答確認を、すべての実利用成功へ広げない。会話で用意した二つの入口AI-Promptは別々のGitHub Query原本として保存済みとは確認していない。必要になればCurrent Skillから再構成できるが、移行を理由にPrompt新設やEpisode生成を始めない。

## 5. Query backupからCurrent MAPへ

HumanはMAP本体を別Threadで改良している間にも、先にQueryをbackupし、後で更新すればよいと指定した。05が初回に保存したのは旧パス `skills/map-ark-current-position/query/README.md` の一件。commit [6375c44](https://github.com/yusukefujiijp/ai-project/commit/6375c44f93701b7e3495c128534352edc814fafd)、blob `da1ffd2f114ea2de7b3f1bc7654116675542aea5` の全文・Remote一致を確認済み。MAP本体や自動同期を変更した承認ではない。

05→06実行前のCurrent確認で、別ThreadのMAP改善が公開済みと判明した。**現行は `$map-current-position`／現在地MAP**、共有原本は [SKILL.md](../../../skills/map-current-position/SKILL.md)、Queryは [query/README.md](../../../skills/map-current-position/query/README.md)。旧Skill・Queryは新原本へ案内する互換読取入口。旧Identityを新Identityと同一視せず、固定Bindingの失敗を互換リンクだけでPASSにしない。旧コマンドが自動転送する保証もない。

後続改善は「残作業とGoal」を独立して読み、目的・現状・差分・方法・完了条件を結ぶ。未完了・保留・将来構想・取消し・結果不明・別担当を区別し、十分明確なContinueでは現在のScopeを進める。Goal専用Skillの完成を前提にしない。

Hub §3.13は共有版commit `8e30b09cc918bf011c8e822917b79abf120399da` と導入先commit `20eca8b06c6dce3fb58cf0e7a7f178fc6ea7df9a` の確認を記録する。今回05はCurrentの新本文・Query・旧互換入口を実際に読み、保存内容を直接確認した。導入先への保存はその所有資料の報告であり、今回こちらが導入し直した事実ではない。さらに準備中の後続commit `dda8ecf86a3f794568d5c9a18d9ed6778d708b37` は、所有Threadでcloud新名とexecutor既存IDの両経路から改訂本文を全文取得し共有版と一致したことを記録した。この二経路の取得残点は完了として継承する。Human UI、旧コマンドの自動転送、自然発動、全Runtime、継続効果は別の観測。新名で直接取得できない環境では共有原本を実際に読んで使える。

計画時に見えたSkills Hubのheader/EOF不一致もCurrentでは解消済み（v0.32.2／`EOF::ARK_SHARED_SKILLS_HUB::v0.32.2`）。古い未完了として06へ持ち込まない。ここから得られるAIの見立ては、初回backupの価値と後続Currentの更新を両立させるには、固定履歴と生きた編集先を分けることが重要、というCandidateである。

## 6. 04以前から保持する意味と後続訂正

[04固定Harvest](https://github.com/yusukefujiijp/ai-project/blob/f162456de68400051027f92e516ec1d440c0cac8/ark-project/ark28/ark28-04/harvest.md)と同commitの経験原本が、Teshuvahの中心へ戻るまでの遅れ、豊かな展開への喜び、Ark99形成を所有する。一件を深める価値と、次の一件へ速やかに入る価値を両方保つ。前件完了・保存・移管を次件の開始条件にしない。

Ark99本番の二大ルールは「新しい一件を新しい本番Threadで始める」「同じ一件は可能な限り同じThreadで深める」。長期化等で別Threadが必要になった時は適切な既存Arkへ継承する。00は準備用control-center、本番は01以降。正式Project名は **Ark99: Teshuvah Thread**、00の正式Titleは `Ark99:00_2026/10/06; control-center`。旧AIの「日付なし」はHuman訂正済み。

三段階の公開成果はfoundation `ab9599b2f3d3236d3f826b6e8516a5be038e7f10`、00準備 `71fa59ddd4283afa34640011f44c1f11d0fafd16`、名称・指示 `474c231f37c96d8e7fa4adcf7a09392c0e5f8cc2`。00 AIの受入れ報告はHuman経由であり、Source側による直接UI確認・実案件効果ではない。

**後続Current訂正:** 2026-10-10以降、Ark99本番Threadの起動準備はすべて00から行う。Ark99限定であり、Ark28継続の起点を00へ変えない。00の無関係な実験完了を本番開始Gateにしない。この訂正は[Ark99 README](../../ark99/README.md)、[INSTRUCTIONS](../../ark99/INSTRUCTIONS.md)、[00 README](../../ark99/ark99-00/README.md)が所有する。05初期Stateの「mandatory00 transitなし」は当時の履歴であってCurrentではない。

[Dots入口](../../../dots/README.md)と[再接続Topic](../../../board/topics/20261001-dots-work-reconnection/README.md) §6 Currentを読む。Dotsを徐々に主たる協働へ、Workを強いSubとして活かす方向は、移行完了・固定序列・Ark27 Main移管の証拠ではない。Actor固有の定期Map・保存委任を06へ輸入しない。

03の有限対話は3投稿・2往復で終了済み。最初のメッセージは二投稿。「あなたの最新回答を読み」を完成返信の回収証拠にした先行解釈は撤回され、後続の完成返信取得・読了の明示報告が成立根拠。ブラウザーは初穂の観測、Workは受信・返信・保存原本の観測という区別を残す。AI同士の合意はHumanの新送信許可でも独立実証でもない。詳細が必要な時だけTopicから固定原往復へ進み、終了対話を再演しない。

四Skill、03のmap/save、納豆Portal、generate-ideasの作成・共有・導入・限定確認は完了した範囲を保持する。generate-ideasの限定比較で品質優位まで証明されたとはしない。Pet STOP、Ark24 Frozen Trigger、Next-Cycle Workout Bridge等の境界を保持する。

## 7. 残作業・保留とEvidence Boundary

現在承認された仕事は05→06の資料準備・公開・検証・コピー面提示。最終Receiptは05 Stateへ。06自身の17件読解・Identity/EOF/Binding/Triad・R1–R8再構成は受入れ先のGateであり、Sourceの検査では代行できない。HumanのThread作成・貼付・Title設定と、実利用効果も独立した観測である。

通常の保留は、休日Caffeine、ワコー等の実生活効果、Podcastを自然に聴いたFeedback、prefix方式、Repository全体の追加Organization、別途のVoice旧lessons整理、現在Body・睡眠・4:00案・熱傷、必要時のMain再接続、Ark99個別案件の実際の継承。これらは一つの作業列ではない。現行Ownerと新Human入力が判断を変える時に必要範囲だけ回復する。

MAP本体改善・旧Radio退役・projects archive・Query初回backupは完了した範囲を未完へ戻さない。Theme擦り合わせには発展余地があるが、06の固定Missionにはしない。新しいHuman入力が既にあれば再入力を求めず、その依頼を中心にする。Bootだけなら根拠付き受入れを返してHuman Reviewへ戻る。

## Living Review

Not dead data, but a living board. このSourceで進んだのは、話題を一つに縮めることより、価値の所在と入口を明確にすることである。Repositoryの集中、Themeと生成の分離、QueryのbackupとCurrent更新は、必要な時に正しい原本へ戻れるという共通のBenefitを持つ。一方、保存や入口整備を生活の解決と認定すれば、元のTeshuvahを見失う。これは根拠からのAIの見立てであり、Humanの内心や主の御心の断定ではない。

## Next step

06へは、上の成果・訂正を固定根拠とCurrent所有資料から自ら復元できる受入れ契約を渡す。最初の接続は必須読解と再構成、その後は既入力の受領、またはBootのみならHuman Review。移行を理由にReset・過去Task・身体Trial・終了対話・送信・外部変更・実案件移管を自動開始しない。

ARK28_05_HARVEST_EOF_v001
