---
name: save
description: Preserve collaboration results, material corrections, evidence, and resumption context in their proper source of record. Use for saving or updating such records, including deciding that no new record is needed. Skip generic file-format questions, ordinary code file saves, quoted save instructions, and design discussion with no persistence request.
---

# save

次の読み手が意味と根拠を取り戻せるよう、残す価値のある成果を担当原本へ保存する。全会話の転記や、保存件数の増加を目的にしない。

## 保存する意味と権限を確かめる

現在の依頼・対象・公開先・有効な継続委任・最新Correction・STOPを受け取る。計画だけ、会話内の整理だけ、保存禁止ならその範囲で止める。対象と保存が既に承認されていれば、通常の作成・修正・必要な検証ごとに再承認を求めない。

現在の目的、重要な訂正・STOP、確認済み成果と証拠、未完了・Unknown、次の確認対象・再開条件が、元会話なしで回復できるかを考える。全五観点を一つの文書へ重複収録するのではなく、原本と根拠への接続を含めて成立させる。

Human原文、AIの言い換え、観測、設計、予定を区別する。観測日時と記録日時、部分完了と完了、結果不明と失敗を混同しない。成果物、協働文脈、実行環境、製品側の予定・設定を分け、記録の保存から設定反映や実利用効果を推定しない。

ChatGPT長期メモリの内容をGitHubへ転記・バックアップ・同期しない。現在の会話で提供された資料や取得した原本とは出所を区別する。

## 所有先へつなぐ

既存の担当原本・近接ガイドを読み、同じ可変状態や契約全文を複数箇所で更新しない。新規作成、既存更新、参照だけ、保存不要、意図的保留から選ぶ。既に必要な内容が残っていればNO_CHANGEで完了できる。

Arkでは保存対象に応じて、次の所有先へ進む。この一覧を毎回の全読込リストにしない。

| 保存するもの | 担当する原本・ガイド |
|---|---|
| 成果物・方法の改訂 | その成果物・方法の既存原本と近接ガイド |
| HumanのTask経験・訂正 | [Task Records](https://github.com/yusukefujiijp/ai-project/blob/main/formats/task-records/README.md)から当該経験原本 |
| Actorが行った出来事 | [Dotsログ](https://github.com/yusukefujiijp/ai-project/blob/main/dots/logs/README.md) |
| 再利用できる共有の学び | [Dots lessons](https://github.com/yusukefujiijp/ai-project/blob/main/dots/lessons/README.md) |
| 相手と目的のある通信 | [Board](https://github.com/yusukefujiijp/ai-project/blob/main/board/README.md)と対象Topic。必要ならboardを使う |

Dotsの原本を扱う場合は[Dots入口](https://github.com/yusukefujiijp/ai-project/blob/main/dots/README.md)と、選んだ保存先が宣言する必須読取・現行形式に従う。Actorログの出来事、lessonsの学び、Boardの通信を混ぜず、同じ出来事を一律に全保存先へ複製しない。

Actor識別子をモデル名・GitHub記録者・相手の表示名から推定しない。Workが相手Actor本人のログへ書かず、記録のためだけに新Actorを作らない。適切なActorが確定しなくても、別の承認済み成果物保存まで一律に止めない。

## 結果不明と並行変更を扱う

保存前に最新の対象と版を読み、予定する変更と既存内容を照合する。対象外の追記、未知フィールド、順序など保存先契約が保持を求めるものを残す。利用できる版条件・競合検出を使い、同じ箇所の意味衝突を黙って上書きしない。

応答喪失・中断後は、再実行前に現物・操作／記録識別子・版・履歴を調べる。同じ識別子・内容の保存済み結果があれば重ねて作らない。内容の衝突は解決し、識別子が見つからない場合も削除・統合等を確認してから判断する。照合不能なら該当再実行を保留し、Unknownを失敗にしない。

追記と上書きの規則は保存先ガイドが所有する。たとえばActorログの訂正とlessonsの同一項目更新を同じ操作へ一般化しない。Skillの文章だけで外部操作のexactly-onceを保証しない。

製品予定や送信の復旧が別途承認されても、保存記録だけを根拠に再作成・再送信しない。現在の製品側の識別子・状態・権限を照合する。

## 保存と確認を完了する

承認された変更だけを実施し、保存先から再取得する。path、版、意図した差分、必要なMetadata・EOF、保持すべき内容を確認する。GitHub操作はその時点の正規Runtimeを使い、成功応答だけを保存済み内容の証明にしない。

結果は、保存した対象と理由、確認できた版・内容、残る制約を伝える。会話内の受領、永続保存、他AIへの送達・理解、設定反映、生活上の効果を別々に示す。保存完了から新TaskやBoard送信を自動開始しない。

## Arkへの接続

適用される[AGENTS](https://github.com/yusukefujiijp/ai-project/blob/main/AGENTS.md)と保存先契約に従う。Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのMeaning・Correction・STOP・Final SealとGuardを保持し、AI・SkillをKeliとして扱う。

Current契約は現行URL、過去の証拠は確認した固定版URL、同梱した資源だけ相対参照を使う。共有原本：[skills/save/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/main/skills/save/SKILL.md)。
