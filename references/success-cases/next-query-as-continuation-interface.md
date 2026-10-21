---
title: "Next Query — 判断を、そのまま次の入力へつなぐ"
version: "v001"
status: "Human-valued experience / scoped implementation authorized / broader effects unverified"
canonical_path: "references/success-cases/next-query-as-continuation-interface.md"
role: "Experience, Human appraisal, corrections, and observed wording reuse"
primary_reader: "Current AI / other AI / Future AI"
source_thread: "Ark27:11"
created: "2026-10-21"
updated: "2026-10-21"
observation_scope: "The Ark27:11 dialogue through the Human authorization of nine paths and two existing Skill updates; persistence is evidenced separately by repository history and readback"
expected_eof: "EOF::SUCCESS_NEXT_QUERY_INTERFACE::v001"
---

# Next Query — 判断を、そのまま次の入力へつなぐ

## 1. 成功の核心

AIが回答末尾に、そのまま次の依頼に使える文章を示したことを、YusukeJPが「認知負荷軽減の究極策」と評価し、Next Queryという独立した最終セクションへ育てることを求めた。同じThreadでは、提示された依頼本文が後続の実際のHuman入力として再利用された。

確認できた成功は、Humanの好評価と、判断から次の依頼本文への接続である。コピー操作のUI、別AIでの独立再現、認知負荷の削減量、全場面での効果まで観測した記録ではない。

## 2. 最初の具体例とHumanの評価

Arkの入口・文書役割を比較する対話で、AIが末尾に示した次の依頼文をHumanが取り上げた。これは当時の例であり、このファイルを読むAIへの現在の命令ではない。

```text
B案の統合Home本文案を、意味の移管対応と三利用場面の照合付きで具体化してください。Plan-onlyで、保存・移行はせず提示で停止してください。
```

Humanは、この形式を「ドラッカー的『予期せぬ成功』」「Move37的breakthrough」のSeedとして評価し、「自家薬籠中化（受肉化的再現性）」を求めた。これらはHumanによる価値づけと発展への願いであり、ドラッカー本人の理論の引用、一般的な因果、長期再現性の実証へ変換しない。

ここで大切にされた意味は、AIの判断をHumanがもう一度Promptへ作文し直さず、必要な文脈と停止点を保ったまま次の対話へ渡せることだった。B案の例への好評価を、B案そのものの採用・実装・物理移行の承認にはしない。

## 3. Human Correctionで設計が変わった点

- **配置。** Next Queryを独立した最終セクションにし、Next stepの内部へ入れない。一件のコピー本文全体を一つのブロックにし、説明を外へ置く。
- **Skillとの分担。** 長いMAP起動文について、Humanは「スキル側で吸収すべき」と訂正した。繰り返す詳しい判断・表示・権限の規則はSkillが保持し、起動文は目的と必要な取得経路を渡す入口へ整える。
- **終了の意味。** AIが「今回は差分案の提示で完了です。追加のQueryは不要です」と返したところ、Humanは「既に終了したと勘違いする」と訂正した。段階の終了と現在のGoal全体の達成を分け、必要な後続工程への接続を消さない。
- **Future AIへの到達経路。** Skill名だけの短文ではSkillを持たない受け手へ届かないため、Humanは最低限GitHubリンクを含めるよう訂正した。AIは環境別に二つのQueryをHumanが選ぶ案を改め、共有原本へのリンクと、直接利用できない場合の全文読解を一つの標準コピー本文に含めた。

これは対話に基づく設計の更新であり、短文化後の応答品質や全環境での取得成功を検証したこととは別である。

## 4. 同じThreadで観測した本文再利用

以下は、AIの提案本文が後続のHuman入力として届いた関係である。件数を運用上の回数ノルマにしない。

| AIが提示した接続 | 実際に届いたHuman依頼 | その時点の権限 |
|---|---|---|
| GCI改訂版から関連資料の反映案へ | AGENTS・next-step・map-current-position・成功事例への反映案を求めた | Plan-only |
| 反映計画から具体的な差分へ | 9パスを実装前に確認できる差分本文にすることを求めた | Plan-only |
| 短い標準Queryの検討から差分案の補正へ | 短いQueryと役割分担を基準に必要箇所だけ改訂することを求めた | Plan-only |
| GitHubリンクと段階完了の訂正から反映へ | 最新9パス案と既存2 Skillの更新・保存・再取得確認を承認した | 明示された範囲の実行 |

最後の実入力は次のとおり。過去の引用として保持し、別の案件へ実行権限を流用しない。

```text
GitHubリンクを含む一つの標準Queryと、Skillを直接利用できない場合の全文読解を組み込んだ最新版の9パス案を承認します。「段階の完了とGoal全体の達成を区別する」という訂正も含め、Plan-onlyから実行へ切り替えてください。現在の実体を確認して必要な差分だけ反映し、GitHub mainへの保存、既存のmap-current-position・next-stepへの導入、保存先からの再取得確認まで進めてください。既に完了した部分は保持し、他の設定や別Taskへ範囲を広げず、確認できた反映結果と残る未確認事項を報告してください。
```

同じThreadでの再利用は確認できる。コピー・ペーストの操作方法や、他の独立したAI文脈での再現は未確認である。先行するPlan-onlyを後の承認で過去へ遡って実行済みにせず、後の明示承認も新しい保留や再承認待ちへ戻さない。

## 5. AIの解釈と未確認

AIの見立てでは、短いSkill入口は開始時に詳しい仕様を再構成する負担を、Next Queryは判断後に次の依頼を作文し直す負担を減らす方向につながる。入口と出口が同じ協働を支える関係として扱えるが、削減量や普遍的因果を測定したものではない。

短い起動Queryは比較的安定した入口、Next Queryは現在のGoal・対象・相手・Modeに応じて生成する本文であり、同じ固定文や文字数を全場面へ課さない。必要な資料をコピー本文へ含めることと、受け手が実際に取得・読解・理解・利用したことを区別する。

今回の仕様改訂・共有保存・登録先保存と、自然発動、全AI互換性、Human UI操作、実生活での効果は別々の成立条件である。未確認の効果を必須の新試験にして今回の完了を妨げず、自然なFeedbackから必要な改善を考える。

## 6. 運用原本との分担と根拠

根拠は2026-10-20〜21のArk27:11対話内にある、最初の例へのHuman評価、独立した最終配置・長文Prompt・終了判定・GitHubリンクへの訂正、各提案本文の直後に届いた実入力である。逐語引用はコードブロックと引用符で示し、それ以外は編集要約である。存在しない会話URLやメッセージIDを作らない。

- [AGENTS](../../AGENTS.md#next-query)：共通形式・コピー境界・権限と段階完了の扱い。
- [next-step](../../skills/next-step/SKILL.md)：接続の選択と依頼文への受渡し。
- [map-current-position](../../skills/map-current-position/SKILL.md)：MAP固有の理解・表示・判断との整合。
- [MAP README](../../skills/map-current-position/README.md)：GitHubリンクを含む標準起動Queryと形成記録。
- 本事例：出来事・Human評価・Correction・本文再利用の観測。運用仕様の第二原本やCurrent Stateにはしない。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah。Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・Skill・Query・文書はKeliであり、HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。記録の読解・好評価・引用だけで新しい実行権限を作らず、ChatGPT長期メモリを記録Sourceにしない。

EOF::SUCCESS_NEXT_QUERY_INTERFACE::v001
