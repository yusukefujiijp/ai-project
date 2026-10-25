---
title: "汎用Reportを小さな核から育てる — 章立てより、問いと根拠の関係"
canonical_path: "artifacts/reports/2026-10-25-small-core-for-general-reports.md"
version: "v001"
created: "2026-10-25"
author_role: "Ark28:07 collaborative AI"
primary_reader: "Human / Current AI / Future AI"
source_commit: "ba47216debeb2163a5dbf880c6b37d73edbb7e41"
status: "Design analysis based on public sources and this report collection; no Skill created or registered"
expected_eof: "EOF::REPORT_SMALL_CORE_FOR_GENERAL_REPORTS::v001"
---

# 汎用Reportを小さな核から育てる

## 汎用性を、テンプレートの数で作らない

良いReportに共通するのは、同じ章数ではなく、**何について、何が分かり、それがどんな意味を持つかが、根拠とともに伝わること**である。比較、活動、検証、考察では、必要な構成も深さも違う。初版から用途別の固定テンプレートを増やすより、判断の核を小さく持ち、素材と読者から形を選べる方が柔軟になる。

今回の固定snapshotでは、`skills/write-report/SKILL.md`は取得時に404で、共有一覧にも同名の入口は確認できなかった。これは別環境の全下書きの不存在証明ではない。本Report集は専用Skillの導入を前提にせず、既存の文章作成・保存の方法と、公開原本の責任分離を使って制作している。Reportの制作とSkillの作成・登録は別の仕事である。

以下は汎用Reportの設計上の提案であり、新しい共有指示原本や登録済みSkillではない。

## 小さな核として残したい判断

まず、現在の依頼から、誰に何を理解・比較・判断してほしいかを捉える。次に、利用できる素材から重要な事実・結果・考察を選び、その意味をつなぐ。必要な根拠と不確かさを残し、今回の読者に合う構成で仕上げる。

この核を短い目的文にすると、次のように表せる。

> 現在の目的・読者・素材に応じて、重要な発見・結果・考察とその意味が、根拠を辿れる形で伝わるReportを構成・執筆・改訂する。

ここで「根拠を辿れる」とは、すべての文に引用を付けることではない。重要な主張が、観測なのか、Human報告なのか、AIの解釈なのかを読み違えず、必要な資料へ戻れることを指す。

また、Reportの終点は実行計画とは限らない。理解を深める、異なる見方を比較する、失敗から知見を残す、記録する、といった目的で完結できる。提言を必須にすると、素材が支えていない推奨を作る圧力になる。

## 要約を超えるために、何を加えるか

資料を短くするだけなら、重要箇所の要約で済む場合がある。Reportでは、問いに対して素材同士を関係づける価値がある。

例えば、入口が一つという複数の資料から、「一つの巨大な本文に集約するのが良い」と結論するのは早い。共有されているのは入口なのか、目的なのか、判断方法なのか。統合した時に失われる役割はないか。この比較によって、素材の羅列にはなかった理解が生まれる。

[一つのSkill入口の成功事例][s1]は、入口の共通化と、内部の方法の自由を分ける。[Skill命名の事例][s2]は、呼びやすい名前が再利用の取っ手になる関係を扱う。二つを合わせて読むと、汎用Reportの入口も、短い呼出名と深い内部判断を両立できるという設計上の仮説が得られる。これは、そのSkillの実利用効果を確認した主張ではない。

## 同じ核から、異なるReportができる

以下は説明用の仮例であり、実際の試験結果ではない。

| Node | Edge | Reportで明確にすること | 不要になり得るもの |
|---|---|---|---|
| 条件付きの比較 | 条件の違い → 選択の違い | Aが有利な場面、Bが有利な場面、その理由 | 無理な単一ランキング |
| 不成功の試行 | 観測結果 → 原因候補 | 実際に起きたこと、仮説、次に区別できる条件 | 成功したように見せる結論 |
| 短い活動報告 | 前後の変化 → 意味 | 重要な変化と、残る確認 | 大きな章立てや無関係な調査 |
| 考察中心の報告 | 素材の関係 → 複数の解釈 | どこまで支持され、何が反証になるか | 必ず行動へつなぐ提言 |
| 残作業の報告 | Goal・依存 → 現在の選択 | 未完了、保留、結果未確認の違い | 全Backlogの自動Task化 |

残作業Reportは有用な一用途だが、汎用Report全体をその様式へ固定する理由にはならない。[map-remaining-work][s3]が必要な場合だけ、その復元方法へ接続できる。

## Human向けとAI向けで、変えるものと保つもの

Human向けでは、重要な意味を早く掴める順序、具体例、比較の読みやすさが効く。AI向けでは、原本・版・適用条件・未確認・再開経路が再利用に効く。両者で保つのは、同じGoal、同じ事実、同じ証拠の強さである。

読者がAIだからといって、命令を多く書けばよいわけではない。読者がHumanだからといって、出典や条件を省いてよいわけでもない。本文の入口と詳細の配置を変えることで、同じ分析を両者が利用できる場合もある。

この関係から、初めからHuman用とAI用の二つの独立Skillへ分ける必然性は弱い。異なる判断責任が実際に生じた時に、分担を検討すればよい。

## 育てる単位は、規則より先に実際の作品

[AI Frontier Reader][s4]と[self-improvement-loop][s5]は、成果物の理解と、制作方法の改善を別々に育てる方向を持つ。Reportでも、まず作品から何が伝わり、何が伝わらなかったかを観察できる。

例えば「この反例で意味が分かった」というFeedbackがあれば、その例を作品へ残せる。さらに別用途でも同じ説明上の不足が繰り返されるなら、方法の改善を検討できる。一回の好みを全Reportの恒久ルールにせず、経験の保存価値まで否定しない。

改善は追記だけではない。重複を統合する、誤解を招く語を変える、不要な必須項目を外す、所有先への参照へ戻すこともある。Skill本文が長くなることを、Reportの品質向上の代理指標にしない。

## 今回の制作から、まだ言えないこと

このReport集は、公開原本を横断して複数の論点を執筆する実際の制作成果である。しかし、専用write-reportの登録、明示呼出しでの応答、名前なしでの自然選択、Humanの執筆負担の減少を試験したものではない。

この区別を保てば、制作した価値を認めながら、Skillの有効性を先取りせずに済む。今後Skillへ接続する場合も、今回の各Reportを大量の必須読解へするより、どの編集判断が繰り返し役立つかを選ぶ方が、小さな核を育てる方向に合っている。

## 根拠

- [s1: 一つのSkill入口の成功事例][s1] — 入口と内部裁量の分離。
- [s2: Skill naming as reusable handles][s2] — 名前と再利用の関係。
- [s3: map-remaining-work][s3] — 残作業に固有の復元責任。
- [s4: AI Frontier Reader][s4] — 内容と制作方法へのFeedback。
- [s5: self-improvement-loop][s5] — 実際の観測から育てる方法。
- [s6: Skills Hub][s6] — 今回確認した共有Skillの一覧と責務。

[s1]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/success-cases/one-skill-entry-multiple-benefits.md
[s2]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/references/success-cases/skill-naming-as-reusable-handles.md
[s3]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/map-remaining-work/SKILL.md
[s4]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/prompts/ai-frontier-reader.md
[s5]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/self-improvement-loop/SKILL.md
[s6]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/skills/README.md

EOF::REPORT_SMALL_CORE_FOR_GENERAL_REPORTS::v001
