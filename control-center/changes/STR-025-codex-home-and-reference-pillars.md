---
title: "STR-025 — Codexの入口とReferences三本柱"
canonical_path: "control-center/changes/STR-025-codex-home-and-reference-pillars.md"
version: "v001"
created: "2026-10-31"
updated: "2026-10-31"
date_basis: "UTC; activity records use their own Asia/Tokyo placement contract"
role: "Codex home change rationale, evidence, scope and validation record"
expected_eof: "EOF::STR_025_CODEX_HOME::v001"
---

# STR-025 — Codexの入口とReferences三本柱

対象は`yusukefujiijp/ai-project`のmain、基準commitは`673cdc2776a21e47f048fc544dbadd8f76c58fe2`。担当はこのCodex ThreadのAI。Humanが作成した[改行のみのSeed](https://github.com/yusukefujiijp/ai-project/blob/673cdc2776a21e47f048fc544dbadd8f76c58fe2/agents/codex/README.md)（blob `8b137891791fe96927ad78e64b0aad7bded08bdc`、1バイト）から、Codexの目的・実行条件・経験を辿れる初版を作る。

## 意図・訂正・承認

Humanは長いログイン過程を繰り返す負担を問題とし、アーカイブ作業を止め、ChatGPT接続成功の継承と再現性を最重要へ変更した。続いてGitHub保存とCodex用の入口を検討し、長く使う初期構成へReferences三本柱を希望した。意味を保持した原文抜粋は[局所Feedback](../../agents/codex/references/feedback/feedback.jsonl)にある。

複数回の計画限定を経て、HumanがこのThreadへ「Mode：対象を限定した実装・GitHub保存を承認します」と明示し、Codex README・runtime・三本柱・agents入口・保存契約上の記録を指定した。通常の修正・検証を一件ごとの再承認で止めないという委任も含む。これは現在の会話本文で直接確認した承認で、正式な会話URL・message ID・正確な発言時刻は未取得。原発言時点のPlan-onlyを遡って実行承認にしない。

ChatGPT操作、アーカイブ・復元、Skill登録、設定変更、別AIへの送信、自動収録・予定・継続運用は承認対象外。本初版でそれらを実行しない。

## 変更と所有

| 範囲 | 変更・保持 |
|---|---|
| `agents/codex/`の9ファイル | 入口、実行条件、Referencesと三つの子README、三つのJSONLを作成・更新 |
| `agents/README.md` | Codexへの案内を追加。既存のAI間協働・Dots等の案内と意味を保持 |
| `control-center/github/README.md` | この変更記録の索引のみを追加し、版・更新情報を整合 |
| 本STR・日別records | 構成の理由と検証／今回の活動をそれぞれの所有先へ |
| 共有Skill・共有References・他Actor原本 | 内容・ID・所在を変更せず参照。認証情報・会話全履歴を保存しない |

共通契約は共有原本へ参照し、局所にはCodex固有の対象・経験・読む場面・戻す先を置く。共有方法の詳細をruntimeへ再定義しない。親READMEは案内、子READMEは局所利用、JSONLは記録本文を所有する。

## 初期記録と重複確認

- Feedback 3件：`3f4d674c-391e-494a-af9e-e68718b46930`、`f7632e91-3eb4-49e3-a5a7-a5b9982b387c`、`b9954d4e-07e6-49d4-a118-53544a8054b1`。それぞれ優先順位の訂正、再利用体験への希望、初期構成への希望を対象にした。原文とAIの補足、登録日時と発言日時を分ける。
- Lessons 2件：`9476a811-3e65-417e-a5d5-1a8246895ad8`、`0c404fbd-5fb0-46be-b2af-1354b43138dc`。既存接続記録を根拠に、プロフィールmetadataと実アクセスの区別、ローカル導入とクラウド会話での発見の区別を残す。新しいブラウザ実証ではない。
- 局所success-casesは0件・0バイト。共有の成功事例ID `16ce6cbe-9b5e-48b5-9e76-8c57e86ab1c4`を入口から参照し、本文・IDを複製しない。

基準版の共有Feedback 2件、共有lessons 6件、Skills lessonsの関連候補、既存接続成功事例を照合した。構成のSimpleさについての共有lesson `58a39598-788c-465c-823b-1c85c2e50e80`は親Referencesから参照し、同じ判断を再登録しない。Skill指定表記に関する共有lessonと、今回のRuntime別発見の学びは対象を区別する。同じ出来事のFeedback・lesson・共有成功事例を独立した複数実証として数えない。

## 適用した原本

- [AGENTS](https://github.com/yusukefujiijp/ai-project/blob/main/AGENTS.md)、[Artifact → GitHub](https://github.com/yusukefujiijp/ai-project/blob/main/prompts/artifact-to-github.md)、[save](https://github.com/yusukefujiijp/ai-project/blob/main/skills/save/SKILL.md)。
- [embed-reference-pillars](https://github.com/yusukefujiijp/ai-project/blob/main/skills/embed-reference-pillars/SKILL.md)、[共有References](https://github.com/yusukefujiijp/ai-project/blob/main/references/README.md)と各子契約、lesson形式の指定された第3〜5節。
- [records](https://github.com/yusukefujiijp/ai-project/blob/main/records/README.md)。活動日別ファイルは記録UTC時刻からAsia/Tokyo日付を求め、既存行を保持する。

現在契約は上記の現行URL、初版で照合した版は基準commitへ戻る。同一blob・適用条件の読解は再利用し、表示切れを回収した。構成の採用は全AIへの自動導入・送達ではない。

## 検証

<!-- publication-verification:start -->
UTC 2026-10-31T21:07:20Z、[初版commit](https://github.com/yusukefujiijp/ai-project/commit/9003b3420e79c262c18bff66bb0527c7e74c0a8c)の12ファイルをRemoteから全文再取得し、準備したUTF-8本文とblob SHAの一致を確認した。同時にmainがこのcommitを指すことを確認した。

- 公開前に68か所の新規参照の所在・必要な節、metadata／Exact EOF、JSONLの形式・型・時刻・ID一意性・sourcesを検査した。Feedback 3件・lesson 2件、局所成功事例0件を確認した。
- 公開前のtree照合では、基準版の全834ファイルを比較し、対象外の本文・modeの保持と、意図した12パスだけの作成・更新を確認した。既存共有成功事例のID・本文、共有Skill、共有References、他Actor原本を変更していない。
- GitHub Pluginの公開Git tree／commit／ref機能を使用し、期待head付き・非forceでmainを更新した。既存の別作業の更新を含む基準版から作成した。
- 元会話なしの読解を想定して、目的→実行条件／経験→根拠・後続訂正→所有原本という経路と、初版／未確認／現在の権限の区別を執筆上確認した。別AIへの送信や新規Threadでの実読解試験は行っていない。

この検証結果と[活動記録](../../records/2026/11/2026-11-01.jsonl)は、初版のRemote照合後に記録した。最終の記録保存自体も再取得して確認し、完了応答でそのcommitを報告する。確認のためだけの記録を反復追加しない。
<!-- publication-verification:end -->

## 残る確認と戻し方

新規Threadでの自動発見、元会話を持たない受け手の理解、接続の再利用、長期安定性・Humanの負担軽減はこの初版作成では検証していない。必要な後続依頼の範囲で、入口の発見・条件の理解・実行環境を分けて確認する。

文書の誤りは担当原本へ、経験の訂正は該当IDへ、方法の変更は共有Skillへ戻す。構成を戻す必要が生じた場合も最新mainと他者の変更を保持し、この差分を対象に判断する。基準Seedと既存ファイルは固定commit・Git履歴から復元できる。アーカイブの復元を意味するものではない。

EOF::STR_025_CODEX_HOME::v001
