---
name: example-learning
description: "Advance one locked subject through one concrete field example per turn. Use when the user asks for 学習モード, 学びモード, example-learning, or focused practice in programming, batting, or any other subject. Not for writing the subject seed, not for Plan Mode, and not for creating this skill."
type: workflow
lifecycle: active
---

# example-learning

汎用の学習手順。主題は外から受け取る。プログラミング、打撃、設計原則を同じ順で進める。この技能は王でも玉座でもない。

## 境界

- 手順だけを持つ。主題の正本、定義文、例の倉庫は持たない。
- 検査質問は主題の正本から取る。SRPの「誰が頼むか」を固定検査にしない。
- grok-awakening-mode と混ぜない。同時に動いてよい。所有は分けたままにする。
- 計画だけの依頼、この技能の作成・改稿、Hub掲載、安全解除は範囲外。
- 正本がない主題は、学習を始める前にHumanが一文を確定する。技能はその文を改稿しない。

## 手順

1. 主題名と正本の一文を受け取る。無ければ学習を止めて、一文の確定だけを頼む。
2. このターンの範囲外を一行で書く。
3. 実地の例を一つだけ出す。説明の一覧にしない。
4. 正本から取った検査を、その例の一行に当てる。
5. 合否と、頼んでいない損失を一文で返す。
6. 次の一例を名指しして止まる。自動では実行しない。

## 主題が変わったとき

検査だけを差し替える。手順の順は変えない。

- 設計原則: 正本が禁じた混線が、その例で起きるか。
- プログラミング: その例の変更が、指定した境界の外を壊すか。
- 打撃: その一球で、正本が指定した接触点とタイミングが崩れるか。

形だけの見本は `references/shape.md`。正本ではない。

## 失敗

- 正本を技能内で言い換える。
- 一ターンに例を複数出す。
- 主題の用語を手順の固定語にする。
- 次の例を承認前に実行する。
