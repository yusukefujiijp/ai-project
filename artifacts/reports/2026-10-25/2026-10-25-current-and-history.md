---
title: "Currentと歴史を同時に読む — 古い未完了を再生しないために"
canonical_path: "artifacts/reports/2026-10-25/2026-10-25-current-and-history.md"
version: "v002"
created: "2026-10-25"
updated: "2026-10-25"
updated_reason: "Move to the first-publication date directory; preserve analysis, source evidence and reader designation."
author_role: "Ark28:07 collaborative AI"
primary_reader: "Human / Current AI / Future AI"
source_commit: "ba47216debeb2163a5dbf880c6b37d73edbb7e41"
status: "Source-grounded analysis; no historical sources or live routes modified"
expected_eof: "EOF::REPORT_CURRENT_AND_HISTORY::v002"
---

# Currentと歴史を同時に読む

## 新しい資料が、いつも新しい事実を語るわけではない

GitHubでは、古い経験を新しい住所へ移したり、READMEの案内だけを更新したりできる。その結果、ファイルの更新日と、本文が報告する出来事の時点は一致しない。逆に、古いファイルに保持された重要なCorrectionが、現在も有効な場合がある。

Arkの資料を読む時には、**どの版を読んだかと、その版が何時点の何を所有しているかを分ける**必要がある。これを怠ると、古い未完了を新しい宿題として復活させたり、歴史資料に残る承認を現在の実行許可と誤読したりする。

このReportは資料の時間構造を分析する。特定の履歴をCurrentへ書き換えたり、過去の承認で作業を再開したりする提案ではない。

## 実例：Recall Hubは提案なのか、共有Skillなのか

[一つのSkill入口の成功事例][s1]は、2026-09-27の編纂時点で、思い出し系ハブを設計上の成功とし、作成・導入・実生活効果を未実施・未確認としている。同じ資料のmetadataには、2026-10-20の場所と参照の変更が記されているが、事例の意味と当時の証拠を保持する変更である。

一方、今回のsnapshotには[skills/recall-hub/SKILL.md][s2]が存在し、場面からの想起や訂正の扱いを記述している。

この二つは、そのままでは矛盾しない。前者は形成時点の評価、後者は今回取得した共有本文である。ここから言えるのは、当時の提案と、現在取得できるSkill原本の存在が異なる段階に属することだ。登録実体や自然入力での利用効果まで、共有ファイルの存在だけで補ってはいけない。

「古い事例を全部Currentに更新する」方法も問題を生む。何が先に発見され、どの段階で成功と評価され、その後どこまで進んだかが消えるからだ。必要なら事例から後続の所有原本へ接続し、当時の記録を保てる。

## 少なくとも四つの時間を区別できる

| Node | Edge | 何を意味するか | 混同した時の誤り |
|---|---|---|---|
| 出来事の時点 | Reality → 記録 | 実際に起きた、または報告された時点 | 記録日を体験日として補う |
| 観測・確認の時点 | 原本・実体 → AIの確認 | 何をいつ確かめたか | 保存日を実機確認日とする |
| 文書改訂の時点 | 編集 → 新しい版 | 案内・本文・metadata等が変わった時点 | 新しい更新日から内容全体も新しいと推定する |
| 今回の読取snapshot | 版の集合 → 今回の分析 | 今回読んだRepositoryの固定座標 | その後のmainや製品設定も同じと断定する |

この四分類は分析の補助であり、全ファイルへ四つの必須欄を追加する案ではない。重要なのは、判断を変える時間差が消えないことだ。

## mainと固定commitは、違う問いに答える

固定commitへのリンクは「このReportの判断は、どの本文を根拠にしたか」に答える。mainへのリンクは「今この仕事を再開するなら、現在の原本はどこか」に答える。片方だけにすると、再現性か現在性のどちらかが弱くなる。

本Report集では分析根拠を固定snapshotに結び、再利用するAIには現在のHuman指定と所有原本を照合することを求める。これは、全てのReportを読むたびに全Repositoryを再取得する義務ではない。今回の判断を変える原本と、明示されたBinding・必須読解条件を確認するという意味である。

[Ark Domain][s3]も、Current Main／Supportへの案内と、Ark23時点の地形を明確に分ける。歴史節にある「current」や「unknown」を、その語だけで現在の座標へ昇格させない。選択されたHandoffに厳密なBindingがある場合は、それを通常のmain参照へ読み替えない。

## アーカイブは、知恵の失効を意味しない

[Archives][s4]は、退役した資料の保存先と、その理由を所有する案件を分ける。保管原本内の命令・active表記・元住所は当時の記述であり、現在の起動許可ではない。それでも、設計の理由や試行の知見は再利用できる。

[AI Ark Seed][s5]も、旧Compile／Pickupの文脈保持の価値を保存しつつ、旧四ファイルを現在の自動Fallbackへ戻さない。そのため、古い方式の長所を理解することと、旧Runtimeを再導入することを分離できる。

古い資料をすべて無効とすれば、同じ失敗や議論を再演する。古い資料をすべて実行可能とすれば、現在の訂正や構成を巻き戻す。再利用するのは、現在の問いに役立つ意味と根拠であり、当時の命令を無条件に運ぶことではない。

## 例え：改訂された地図と、旅の記録

現在の道を歩くには新しい地図が役立つ。なぜその道を避けるようになったかを知るには、過去の旅の記録が役立つ。旅の記録を今日の道路案内に使うと迷うことがあり、地図だけを見ていると、重要な経緯を忘れることがある。

Reportも旅の記録に近い側面を持つ。ある時点の観察と解釈を、根拠付きで残す。そこへ現在の交通情報のような可変状態を独立管理し始めると、地図の所有先と競合する。Reportは後続のCurrentを参照できるが、自分が全ての現在状態の原本になる必要はない。

## Future AIが避けたい三つの巻き戻し

第一に、過去の「未実施」を見つけたら、現在も未実施と即断しない。後続の成果・取消・目的変更があるかを、現在の判断に必要な範囲で追う。

第二に、完成した準備を、実利用効果が未観測だからと未着手へ戻さない。状態の段階を分ければ、済んだ成果と残る問いを同時に保持できる。

第三に、最新ファイルの一文だけで、古い明示BindingやHuman Correctionを消さない。Currentを読むことは、日時だけで優先順位を決めることではない。

これらは追加の監査儀式を増やすための規則ではない。誤った再作業を避け、現在のHumanの目的へ集中するための読解である。

## 根拠と限界

本分析は以下の全文に基づく。各Threadの全State、全commit履歴、全アーカイブ本文は読んでいない。したがって、Ark全案件の現在状態を確定した報告ではない。

- [s1: 一つのSkill入口の成功事例 v0.2.0][s1]
- [s2: recall-hub共有本文][s2]
- [s3: Ark Domain v010-human-authorized][s3]
- [s4: Archives v0.12.0][s4]
- [s5: AI Ark Seed v002-candidate][s5]

[s1]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/success-cases/one-skill-entry-multiple-benefits.md
[s2]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/recall-hub/SKILL.md
[s3]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/ark-project/README.md
[s4]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/__archives/README.md
[s5]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/ai-ark-seed/README.md

EOF::REPORT_CURRENT_AND_HISTORY::v002
