---
name: board
description: Connect purpose-driven communication with a named collaborator to the appropriate existing Ark Board topic. Use for preparing, receiving, replying to, or saving Board exchanges with human or AI collaborators. Skip physical boards, generic dashboards, ordinary status summaries, and quotations that do not request communication work.
---

# board

通信の目的・相手・現在の状態を整理し、既存Boardの適切なTopicへつなぐ。Boardを新しい司令塔、全Task台帳、第三の権限者にしない。

## Threadを越えて理解をつなぐ

GitHub Boardを、通信の目的・参照版・返信・重要な訂正・未解決点とその根拠を後から辿れる共有の記録として活用する。チャット内だけの理解は会話の流れやThread交代で参照できなくなり得るため、元会話を持たない別AI・Future AIも、記録された対話から何を理解し直し、何がまだ判断・確認を要するかを回復できるようにする。この継承価値を、その場の伝言や進捗表示とともにBoardの根本的な役割として扱う。

残す内容は現在の目的と承認範囲から選び、全会話の逐語保存を義務にしない。保存された理解は当時の根拠付きの記録であり、将来のAIの独立した理解・検証・実行を保証しない。可変なCurrentの所有先は既存Topicの担当欄に保つ。

## 通信の対象を受け取る

現在のHuman依頼、相手、今回伝える内容・問い、期待する応答、担当、承認範囲を解決する。既入力の宛先や本文を再入力させない。表示名・Repository Actor ID・製品側の送信先IDは別に確認し、相手Actorへの成り代わりをしない。

保存時点の「受け手未指定」「未送信」「未観測」と、新しいHumanによる指定・承認・実際の返信を区別する。引用された過去のGoを現在の実装・保存・送信権限へ昇格させない。

## 既存Topicへ接続する

[Board入口](https://github.com/yusukefujiijp/ai-project/blob/main/board/README.md)と、対象TopicのCurrent・適用ガイド・判断に必要な後続返信を読む。指定された固定版の全文読解・Identity・EOF・現行比較があるなら従い、Gapや不一致を補完しない。

同じ目的の既存Topicがあれば使い、名前だけ似た別議題へ混ぜない。新Topicが必要なら、その必要性と承認範囲から判断し、空の予約ファイルを作らない。完了した対話を新しい根拠なく再開しない。

通信の可変なCurrentはTopicの担当欄だけで更新する。返信は応答の内容と時点、構造変更記録は変更の履歴を所有する。Hub、ログ、Skill、別の変更記録へ通信状態のコピーを増やさない。

## 必要な応答を組み立てる

元会話なしの相手が、何のための連絡か、どの版・成果を扱うか、何が訂正されたか、何を判断すればよいかを理解できる内容にする。原本へのリンクと判断に必要な理由を残し、全履歴や共通契約を貼り直さない。

受け取った応答は独立に評価する。同意・差分・根拠不足・未解決を区別し、相手のPASSや準備成果を自分の理解・検証へ借用しない。往復数は現在の依頼から扱い、固定回数や全Unknownの解消を完了条件にしない。目的が満たされたら対話を閉じられる。

草稿だけ、保存不要、返答待ち、意図的保留も正常な結果である。有限の通信を全Skillの固定実行順序へ変えず、必要なときだけload、next-step、saveへ接続する。

## 保存と送達を分ける

- **会話内の草稿・受領**：その会話で扱った内容。Board保存済みではない。
- **Board保存**：承認された返信と必要なTopic Currentを保存し、Remote再取得で確認した状態。
- **送達**：確認した宛先へ、承認された経路で送った結果。Board保存から推定しない。
- **既読・理解・行動・効果**：相手の応答や独立した根拠でそれぞれ確認する。

保存が承認されていれば、最新Topicを読み、並行した返信・訂正を保持して必要な保存と確認を行う。具体的な保存処理はsaveと保存先ガイドを使える。保存のためだけに相手Actorのログへ書かない。

外部送信は、現在の承認と相手の実際の送信先・経路が確定した範囲で実行する。承認済みの同一範囲で再承認を繰り返さない。Boardへの保存承認だけを外部送信承認にはしない。

送信・保存の応答が失われたときは、識別子、対象版、送信結果、既存返信を照合してから判断する。未取得を未送信・失敗に変換せず、同じ依頼を再送しない。確定できなければ該当操作だけを保留し、再開に必要な確認を示す。

## 完了を実際の到達点で示す

今回作成・受領・保存・送達した範囲と残る条件を区別して返す。相手が実装を受諾した、Humanが承認した、Runtimeへ反映された等を、通信文面だけで実行済みにしない。STOP・Final Seal・今回の完了を保持し、新Task・実装・Resetへ自動昇格させない。

適用される[AGENTS](https://github.com/yusukefujiijp/ai-project/blob/main/AGENTS.md)とCurrent契約に従う。Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのMeaning・Correction・STOP・Final SealとGuardを保持し、AI・SkillをKeliとして扱う。

共有原本：[skills/board/SKILL.md](https://github.com/yusukefujiijp/ai-project/blob/main/skills/board/SKILL.md)。Current契約と固定証拠のURLを使い分け、Repository外にある資料へ壊れる相対参照を作らない。
