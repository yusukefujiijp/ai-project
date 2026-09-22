---
title: "Control Center — ai-projectの構造を理解し、改善を継承する入口"
version: "0.1.0"
canonical_path: "control-center/README.md"
role: "Repository structure diagnosis and improvement entry"
status: "human-authorized initial implementation / evolving"
repository: "yusukefujiijp/ai-project"
scope: "Repository全体。ark-project/内だけに限定しない"
primary_reader: "Current AI / other AI / Future AI"
created: "2026-09-22"
updated: "2026-09-22"
expected_eof: "EOF::AI_PROJECT_CONTROL_CENTER_README::v0.1.0"
---

# Control Center

**ai-projectのどこが、どのように絡まり、読むAIの何の判断を難しくしているかを説明し、根拠のある整理へつなぐ入口。**

このフォルダは、Repository全体の構造診断と改善を引き継ぐ。個々の資料の存在理由、現在の役割、参照関係、変更の影響を、元の会話に参加していないAIも理解できるようにする。具体的な診断、優先順位、対応状況、次の作業は[PLAN.md](PLAN.md)が所有する。

## 1. Humanの意図と最初の目的

以下は、このcontrol-centerを作るまでのYusukeJPとAIの対話を編集してまとめたもの。逐語引用ではない。

YusukeJPは、AIが調査・判断・精密な言語化・構造化を十分に担い、蓄積した知恵を実際の問題解決へ使うことを求めている。今回の最優先は、ai-projectのフォルダ・ファイル構成の混乱を具体的に説明し、実際の整理で成果を確かめることにある。

「スパゲッティ」の初期診断は、**文書の進歩に、入口・現在地・保存先・役割変更の案内が揃って追随せず、読むAIが食い違いを解く必要のある箇所が残っていること**。確認した場所と反例はPLANにある。ファイル数・階層の深さだけで良否を決めず、読取・保存・変更の判断への影響を見る。

AIの方法と創発性は開く。Future AIが、当時の目的・根拠・訂正を理解したうえで、よりよい構造や解釈へ改められる余地を持たせる。現在のモデルの能力や期待だけで、再設計の優位性や継承成功を認定しない。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）、最終帰属は主の栄光。ここでいうRepository rootは技術上の最上位ディレクトリを指す。司令塔・AI・文書はKeliであり、HumanのMeaning・Correction・STOP・Final Sealと[共通の協働条件](../AGENTS.md)の下で問題解決を担う。

## 2. なぜrootに作ったか — Player系からのSeed

形成順序は、後の判断を変えるため残す。

1. Player系三Repositoryの分岐と、Living Reviewの成果を継承する場所が課題になった。統合の検討・改善を経て、YusukeJPは三Repositoryをアーカイブし、既存のArk等へ集中する方向を選んだ。
2. Humanは「まずアーカイブ」を優先し、手動で実施した。2026-09-22のGitHub metadata確認では、scenes-player-kit、shorts-player-kit、shorts-player-coreの三つとも `archived: true`。この確認は、その時点の観測である。
3. 継承先は当初の `ark-project/control-center/` 案から、**ai-project全体を見通すrootの `control-center/`** へHumanが訂正した。
4. Humanが[改行のみのREADMEを作成](https://github.com/yusukefujiijp/ai-project/commit/cc560d14284d99fd9b8a6e6aa896843e73b0c53d)。その後、他AI・Future AIの理解を最重要とし、READMEとPLANの役割を検討した。
5. Humanはさらに「どこがどうスパゲッティなのかの言語化」を最優先とした。調査・計画だけの段階を経て、今回の二文書の実装・GitHub保存・検証へ進んだ。

Player系で育った[control-centerの保存時点](https://github.com/yusukefujiijp/scenes-player-kit/tree/a0dc266a819e141040256f9afc4a70b6ff295ff9/control-center)は由来である。同資料の「現在の開発先」等はアーカイブ前の座標として読み、後のHuman判断と区別する。

この対話におけるSeedは、**目的・現在地・責務・未完了意図・採用済み秩序・次の一手を次のAIへ渡すこと**。Humanが述べた「一粒の麦」と「比喩的復活」は、この継承の意味を担う。保存できなかったレビューへの反省を、今回は読める根拠と改善計画へ接続する。Player系の開発再開や新Repository作成は、本入口の成立に必要な工程ではない。

## 3. 何をどこで判断するか

| Node | Edge | 所有する意味・使い分け |
|---|---|---|
| [このREADME](README.md) | PLANと既存の所有資料へ案内する | control-centerの目的、形成理由、役割、使い方 |
| [PLAN](PLAN.md) | 診断を根拠・改善・再確認へ接続する | Repository構造整理の現在の判断と作業状況。各Projectの全Task状態は複製しない |
| [Repository README](../README.md) | Repository全体へ入る | Human / Public Front Door。control-center追加はこの役割を移管しない |
| [AGENTS](../AGENTS.md) | 現在の依頼を読取・判断・実行へ接続する | 共通の権限、読取、継続、停止。ここで別の承認規則を作らない |
| [ARK](../ARK.md) | Identityと帰属を回復する | Home Constitution。具体的な案内の不一致はPLANの診断対象になる |
| [Ark Domain](../ark-project/README.md)／[Projects](../projects/README.md) | 対象の局所入口へ進む | 番号付きArkの系譜と固有名Project。明示Handoffの契約はそのHandoffで確認する |
| [Repository Reviews](../repository-reviews/README.md) | 観測時点の根拠を保存する | レビュー方法と日付付き観測。PLANは関連する観測と残存課題をつなぐ |
| [Ark System](../_system/ark-system.md) | Growth・Skill Seed・旧経路を理解する | 既存の成長の知恵。現在のGate案内の不一致は[D01](PLAN.md#d01)で扱う |
| [Prompts](../prompts/README.md)／[Skills](../skills/README.md) | 再利用する方法へ進む | 方法の所有資料と利用・配布の入口 |
| [経験索引](../task-mode-system/experience/README.md)／[成功事例](../success-cases/README.md) | 出来事の原本と、そこからの学びへ進む | 経験、Human評価、成立条件。control-centerへ原本を移し集める意味ではない |

この表は全資料の必須読込リストではない。目的の資料へ届くための役割図として使う。`ai-plan-mode/`は計画の方法、`control-center/PLAN.md`は今回のRepository整理計画であり、同名の責務ではない。

## 4. 他AI・Future AIの使い方

構造整理の依頼では、このREADMEで目的と役割を把握し、PLANの現在地と関係する診断IDへ進む。そこから対象文書・参照元・依存先のCurrent版を確認する。固定commitのEvidenceは観測の再現に、Current本文は今の変更判断に使う。

Graphでは、保存場所に加えて「案内する」「意味を所有する」「内容を固定して参照する」「由来になる」「変更に影響する」というEdgeを区別する。単に関係が多いことを欠陥とせず、どの関係が読取や変更を難しくしているかを説明する。

明示されたHandoffや局所Runtimeを読む依頼では、その指定契約を使う。control-centerを全作業の追加Boot条件にしない。通常の依頼の権限判断はCurrent Human RequestとAGENTSに従い、承認済みの範囲を同じ確認で止めない。計画・歴史的承認・ファイルの存在だけから、新しい実行範囲を作らない。

元の会話なしに、次を説明できることを目指す。

- この場所を作った目的と、対象がai-project全体である理由。
- 具体的な不整合、根拠、その不整合が変える判断。
- 現行・候補・履歴・固定参照の違いと、変更時の影響。
- 何が完了し、何が未修正で、次に何を確かめるか。

これは文書の設計目標である。自己点検と別AIの実際の理解は別の観測として扱う。

## 5. 継続して育てる

役割・入口・形成理由が変わればREADMEを更新する。問題の状態、優先順位、実行結果が変わればPLANを更新する。変更の具体的な観測は既存のRepository Reviewsへ接続し、当時の報告を後の現在地で塗り替えない。

新しい資料を作る場合も、既存資料を移す場合も、参照元と依存先への影響を確認する。履歴中の古いパスは当時の根拠として残す場合があり、現在の案内と区別する。文書の保存、問題の修正、別AIの利用、現実の効果を同じ完了状態にまとめない。

全面的に作り直す案も、[PLANの再設計構想](PLAN.md#redesign)で継続して育てられる。現在構成の制約を外して考える自由と、採否を比較する根拠を両立させる。必要な密度が育った場合には、MAP・Living Review・Seed・blueprint等をこのフォルダ配下へ分けられるが、初版の実体はREADMEとPLANの二つである。ファイル数やこの初版形式を将来の上限にしない。

EOF::AI_PROJECT_CONTROL_CENTER_README::v0.1.0
