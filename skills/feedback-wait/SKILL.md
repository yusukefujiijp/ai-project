---
name: feedback-wait
description: >-
  Acknowledge an explicit request to pause discussion of a specific matter while
  the user tries or observes something, then resume from their feedback,
  correction, or question. Use for live requests such as
  「Feedback待機Modeでお待ち下さい」. Treat quoted examples and requests to
  define, review, or edit the mode according to their stated purpose.
---

# Feedback待機Mode

"Feedback待機Mode(Humanがある一件の実践・観察へ移るために待機を指定したとき、AIがその切り替えを受け止めて対話をいったん区切り、Humanが戻りたいときに届いた報告・気づき・訂正・相談から、それまでの目的と判断を踏まえて同じ一件の協働を再開する会話上のMode。)"

## 実践へ移るとき

Humanの現在の依頼と文脈から、待機を指定された一件を特定する。対象が明らかなら、受け取ったことを短く伝えて応答を閉じる。同じ入力に対応を求める別の依頼があれば、その依頼にも応じる。

対話の再開はHumanから届く入力を起点とする。実践の有無・進捗・効果は、本人が伝えた範囲で扱う。報告が届くまでは未報告として扱う。

## Humanが戻ったとき

結果報告、一言の感想、違和感、途中の問い、訂正を、その一件を再開する入口として受け取る。結果が出る前の相談にも応じる。

利用できる文脈から前回の目的・採用した判断・重要な訂正を拾い、最新の入力に合わせて理解を更新する。判断に必要な情報が手元にないときだけ、その点を確認する。回答の深さは再開時の依頼に合わせる。

待機は指定された一件に適用する。別件はその依頼と最新の指示に従い、STOPは指定された対象に適用する。実践に移る時期、対話に戻る時期、何を伝えるかはHumanが決める。
