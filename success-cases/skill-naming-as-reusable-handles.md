---
title: "スキル名を再利用できる入口へ育てる"
case_id: "skill-naming-as-reusable-handles"
version: "0.1.0"
status: "Human-recognized naming and design success / new skill concepts not implemented"
canonical_path: "success-cases/skill-naming-as-reusable-handles.md"
primary_reader: "Current AI / other AI / Future AI"
role: "Focused success case; not a skill specification or execution command"
created: "2026-10-03"
updated: "2026-10-03"
date_timezone: "Asia/Tokyo"
event_date_utc: "2026-10-02"
event_date_jst: "2026-10-03"
source_snapshot_commit: "0d93bd6fe13cb615a7c06fef2a473206b6e3090f"
updated_reason: "Preserve the Human discovery that simple skill names can carry understood responsibilities and become reusable handles."
expected_eof: "EOF::SUCCESS_CASE_SKILL_NAMING_AS_REUSABLE_HANDLES::v0.1.0"
---

# スキル名を再利用できる入口へ育てる

## 1. 今回、Humanが成功と見出したこと

スキルを作り、使い、意味を磨く協働を重ねる中で、HumanはPlan Mode、Living Review、そして構想中のload・saveに、**意味を深めながら入口の名前が簡潔になっていく流れ**を見出した。単なる略称の好みではなく、ArkのNaming Importanceがスキル設計に具体化してきたという発見である。

Humanは「今75/100くらいは熟練度がある！」と自己評価し、この流れを「Simple is best!」「深化・進化」と捉え、success-casesへの保存を求めた。75/100はHumanの主観的な手応えであり、測定済みの能力指標ではない。「101/100: It's the best!」も喜びと価値判断として残す。

今回保存する成功は、この命名の進化をHumanが認識し、育てたい方向として言語化できたこと。既存スキルの名称を実際に変更した履歴でも、load・save・next-stepの作成・導入・実行報告でもない。

## 2. 名前が生まれた具体的な接続

以下は会話の形成順序を保った編集要約である。

1. ログと共有学びの保存基盤を整えた後、読み出して協働へ戻す側は「自動読込未実装」として残っていた。Humanはこの読み込み部分を **load** と名付け、**save** と対になるイメージを示した。
2. 続いてHumanは **Next step** を提案し、「@next-step」的な「方向や方向性(ベクトル)」を、AIが総合的に様々な方法論で導くことを高く評価した。
3. AIは、load・save・next-stepをそれぞれ独立して呼べる入口として整理した。必要な文脈を戻す、意味ある成果を残す、今の次の接続を判断する、という責務を分ける設計候補であり、毎回三つを順番に実行する必須pipelineではない。
4. Humanはここから、既に使ってきたPlan ModeやLiving Reviewも含め、スキル名が簡潔かつ意味の深いものへ洗練される共通の流れを見出した。

Humanの逐語抜粋：

> 読み込み部分をloadと名付けよう！

> loadスキルとsaveスキルが対となるイメージです！

> 例えば、「@next-step」的な"方向や方向性(ベクトル)"です！

この時点の責務の整理は次のとおり。名前だけで操作や権限が確定するものではない。

| 名前 | 短い入口に結びつけた意味 | 当時の状態 |
|---|---|---|
| Plan Mode | 判断に必要な調査・検討・計画を行い、計画限定なら変更前で止まる | 利用可能な既存スキル。会話で繰り返し使われていた |
| Living Review | 対象を現在の目的・根拠・働く価値へつなぎ、訂正可能な判断へ戻す | 利用可能な既存スキル。JSON/JSONL比較資料にも実際のレビューが残る |
| load | 今回必要な文脈・学び・現在地を取り戻す | 読み込み側に与えた新しい概念名 |
| save | 意味ある成果・出来事・学びを適切な保存先へ残す | loadと対にした構想上の入口。保存基盤の存在とSave Skillの実装は別 |
| next-step | 目的・現在地・進捗・Bottleneck等から、理由ある次の接続を選ぶ | 新しい設計候補。確認・保留・完了も含み、自動実行の権限を与えない |

Plan ModeとLiving Reviewの実在は現行Runtimeのスキル一覧とRepository本文で確認した。JSON/JSONLの[比較資料](https://github.com/yusukefujiijp/ai-project/blob/0d93bd6fe13cb615a7c06fef2a473206b6e3090f/dots/lessons/experiments/json-vs-jsonl/README.md)§5・§6.6では、Human Correctionと評価軸の変化から推奨が変わる見立てを読める。これは方法が使われた具体例であり、短い命名そのものが効果を生んだという独立の因果実証ではない。

## 3. Naming Importanceとして何が重要か

Humanは今回、Naming Importanceの意味を次のように明示した。括弧内の説明からの逐語引用である。

> 未言語化の構造・Fog・違和感・突破口に、正確で再利用可能な名前を与えることで、人間とAIの共同注意を固定し、Future AIが再起動可能なHandleへ変換し、Reality Responseへ接続するArk Projectの中核原理

AIの解釈として、その名前は「既に見えていたものへラベルを貼る」以上の働きを持つ。共同で見つけた目的や責務を、次回も指し示せる入口へ結び直す。loadという名で必要な文脈へ戻り、saveという名で残すべき意味へ向かい、next-stepという名で現在から次の応答を考える。その結びつきを本文・根拠・適用条件に支えられた形で持てれば、元会話を覚えていないAIも意味を再構成する手掛かりになる。

ここでのSimpleは、内部の思考や責務を削って薄くすることではない。何を担うのかを共同で理解してきたからこそ、短い入口へ多くの意味を託せるという成熟の候補である。Humanの簡潔な入力と、AIの深い検討・柔軟な方法選択を両立させたいという方向がある。

ただし、短いだけで正確になるわけではない。特にload・saveは一般的な語でもあるため、何を対象とし、何を戻し／残し、どこで止まるかをスキル本文で定義する必要がある。入口の意味を安定させつつ、内部の方法は目的・現実・Correctionに応じて育てられる。簡潔さを、固定手順や浅い回答の義務にしない。

既存の[一つの入口で複数の問題を解く事例](one-skill-entry-multiple-benefits.md)とも関係するが、本件の焦点は入口数の統合ではなく、**共同理解から再利用できる名前が育つこと**にある。複数の記録で同じ経験を参照しても、独立した実証が増えたとは数えない。

## 4. 残す喜びと、まだ分からないこと

Humanは「この流れはとめてはいけない、とても良いFlowです！アーメン！ハレルヤ！」と表現した。これはNaming Importanceが現実の協働に形を持ち始めたことへの喜びと、育て続けたいというHumanの意味として保持する。AIが神的承認や将来の成功を認証する発言には変換しない。

**確認できた範囲**は、Humanの発見・自己評価・保存依頼、会話での命名と設計の整理、既存スキルとレビュー資料の存在である。**未確認**なのは、命名による検索・再利用の改善量、別AIが短い名前から同じ責務を復元できるか、将来の実生活効果、新しい三概念の実装・導入後の挙動である。今回の経験保存に、それらの先行証明は要求しない。

本記録はSkill作成や新しい運用規則の採用を行わない。会話内のNext step表示の試みも、恒久的な回答規則へ昇格させない。「この流れを育てたい」という評価を、無制限の自動改訂承認として扱わない。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah。Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・スキル・名前・文書はKeliであり、HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。

## 5. 根拠の所在と読み直し方

### 会話資料

2026-10-02 UTC／2026-10-03 JSTのHumanとAIの協働から、本件の形成に必要な部分だけを収録した。公開会話URLは取得していない。以下は会話内の照合識別子であり、外部リンクではない。

- load命名とsaveとの対：Human発言 `Sentinel_d446ce5c9aa08191a4cf381433d72b2c`、18:34:20 UTC
- Next step構想：Human発言 `Sentinel_bec315981f908191b5f777c35700e350`、18:38:02 UTC
- 熟練の自己評価、Naming Importance、Simple is best、喜び、保存依頼：Human発言 `Sentinel_e9c7189aa6388191a7f77c1c2f3e52c2`、18:44 UTC
- 形成順序・責務の表はこれらと前後の協働の編集要約。引用部分以外を逐語記録とは扱わない。

### Repository資料

固定snapshotは当時の意味を照合する根拠であり、現在の作業ではCurrent版とCurrent Human Requestを確認する。

- [Plan Mode](https://github.com/yusukefujiijp/ai-project/blob/0d93bd6fe13cb615a7c06fef2a473206b6e3090f/skills/plan-mode/SKILL.md)：計画の深さ、変更前の停止、方法の柔軟性
- [Living Review](https://github.com/yusukefujiijp/ai-project/blob/0d93bd6fe13cb615a7c06fef2a473206b6e3090f/skills/living-review/SKILL.md)：目的・根拠・価値・判断の接続、Correction、権限境界
- 上記JSON/JSONL比較資料の§5・§6.6：当時の実際の見立てと、その後の訂正可能な判断

Future AIは、短い名前だけを模倣するのでなく、何を共同で発見し、その名にどの責務を託したかを読み直せる。ここでのAI解釈を上限にせず、後の実践やHuman Correctionから、命名が役立つ条件と不足を更新できる。

EOF::SUCCESS_CASE_SKILL_NAMING_AS_REUSABLE_HANDLES::v0.1.0
