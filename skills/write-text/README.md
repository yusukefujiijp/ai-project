---
title: "Text Writer"
version: v002
updated: 2026-10-24
scope: "write-textの説明・標準Query・旧共有URL・形成と確認記録"
---
# Text Writer

目的と受け手に合う文書・メッセージ・Prompt・コピー用Queryを作成・改訂・レビュー・計画する共通入口です。文章の役割、必要な根拠、専門Skillとの分担をAIが判断します。

会話内での本文提示も対象です。通常対話への回答、文章の作成、保存・公開は区別し、現在のModeと権限を保持します。Arkの記録・方法・引継ぎ資料では、明示的な読者指定がなければCurrent AI・他AI・Future AIへの意味の継承を重視します。

## 起動Query（Copy & Paste）

現在の依頼・素材とともに使います。以下はUIの標準起動文と同じです。

```text
$write-text を使い、現在の依頼・素材・Modeを保って、目的と受け手に合う文章へ整えてください。Skillを直接利用できない場合は、次の共有原本を全文読んで適用してください。取得できなければ、未確認範囲・影響・最小の回復方法を示してください。
https://github.com/yusukefujiijp/ai-project/blob/main/skills/write-text/SKILL.md
```

作成・改訂・レビュー・計画の範囲は現在の依頼から判断します。計画限定なら計画で止まり、通常の文章整形からGitHub公開を自動承認しません。登録済みSkillを利用できない環境では、[共有SKILL.md](SKILL.md)を全文読んで指示資料として使えます。本文の読解とSkillの登録・自動選択は別です。

## 文書の役割と担当原本

実行時の判断・意味の保持・Evidenceの区別は[SKILL.md](SKILL.md)が所有します。対象のRuntime・近接ガイド・明示された全文読解やBindingを必要な範囲で使い、Handoffの成立条件は適用される移行契約へ接続します。

経験は出来事と成立条件を、方法は再利用する判断基準を、入口は読む先・更新する先を保持します。小さな成功も記録でき、一件の経験を普遍的な有効性の証明にしません。詳しい背景が今回の判断を変える場合だけ、[成功事例の入口](../../references/success-cases/README.md)や[移行入口を統合した事例](../../references/success-cases/one-transition-entry.md)へ進みます。

## 通常対話・専門Skill・保存との分担

通常の質問への回答を、本Skillの必須対象にしません。文章そのものを成果物として作る時に使用し、SNS投稿・Handoff・ファイル形式等の固有条件は専門Skillへ、保存先と永続化はsave・適用保存手順へ接続します。

コピー用Queryの共通条件は[AGENTS第6.1節](https://github.com/yusukefujiijp/ai-project/blob/main/AGENTS.md#skill-query-portability)が所有し、本Skillは受け手へ渡す本文を組み立てます。next-stepは接続選択、map-current-positionは現在地との整合を担います。すべてを毎回起動する工程表ではありません。

## 旧名・旧共有URLから読む

現行名は`write-text`、表示名はText Writerです。旧[SKILL.md](../write-ark-markdown/SKILL.md)と[README](../write-ark-markdown/README.md)には現行原本への案内を残します。旧URLでの本文到達と、旧名だけでの自動呼出しは別です。旧名の自動別名対応は保証しません。

同じ既存登録物を継続し、別名の第二Writerを新規登録しません。表示名・呼出し名・GitHubの物理path・登録物の識別子を区別します。固定Bindingが旧本文を指定する場合はその固定版を使い、現行の案内でBindingを移行済みとは扱いません。

## 形成と確認記録

以下は[移管前のHub固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md#skills-formation-history)から引き継いだ記録です。「今回」「本入口」「共有ファイル数」「未確認」は各記録の当時の範囲を表します。現在の利用手順は[SKILL.md](SKILL.md)を確認し、後続の観測・Human Correctionを優先します。保存・登録・本文取得と、自然な選択・実利用の効果を区別します。

2026-09-18、`write-ark-markdown` を追加しました。ArkのMarkdownを他AI・Future AIへ渡す共通入口として、文書の役割と必要な知識をAIが選びます。共通の核は短く保ち、後の重要点は共通原則・条件付き知識・経験の根拠へ分け、追加・統合・Correctionを受け入れます。注意書きの全文を各文書へ貼る仕組みではありません。小さな成功も独立した学びとして残す方針を含みます。

共有版はSKILL.mdと配布用の最小表示設定の二ファイルです。導入環境が自動付与するアイコン・内部設定は含めません。自動選択を許可する通常設定で導入し、共有本文との一致を確認しました。独立したAIへ架空のTask報告素材を渡した限定確認では、成功事例と入力ガイドを書き分け、報告成功とTask完了、Human評価と測定、任意入力と必須条件を区別できました。自動選択される頻度や実生活効果は、この確認の対象ではありません。本Skillは2026-09-12のexport-manifestの対象外です。

## 読む先・更新する先

使い方とコピー用QueryはこのREADME、実行時の判断・手順は[SKILL.md](SKILL.md)、UIの表示・起動設定は[agents/openai.yaml](agents/openai.yaml)が所有します。Queryを専用フォルダへ分けず、このREADMEで保守します。[Skills Hub](../README.md)は一覧と共有・配布の共通方針への入口です。形成史は必要な時に参照し、通常利用の追加必読にはしません。

2026-10-20、Humanの承認に基づき、Hubの個別説明・形成記録をこのREADMEへ移し、既存UIの起動文をコピー用Queryとして収録しました。この移管から新たな挙動検証・環境への反映・実利用効果を認定しません。

2026-10-24、Ark27:11のHumanは`write-text`案を採用し、Writer／Query側に限定した共有原本・互換案内・既存登録物・直接参照の更新と保存後確認を承認しました。Ark固有の適用は保持し、文章作成の共通入口を会話内のコピー用Queryにも広げます。統合Home、添付4資料、過去の完了記録、固定Bindingはこの変更の対象外です。GitHub保存・登録先反映・本文取得・UIでの表示・自然な選択・他AIの理解・実利用効果は、それぞれ確認した範囲で判定します。
