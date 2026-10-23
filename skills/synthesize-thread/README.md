---
title: "Thread総括 / synthesize-thread"
version: "v0.1.0"
status: "Human-authorized initial release / limited response checks / field effects unverified"
created: "2026-10-21"
updated: "2026-10-21"
source_thread: "Ark100:01"
---

# Thread総括 / synthesize-thread

対話の大切な意味・訂正・発見を、その時の用途に合う形でまとめるSkill。複雑な経験の読み返し、技術的な検討、創作、内省などを扱い、方法と表現は実行するAIへ開く。

実行時の指示は[SKILL.md](SKILL.md)、UI用の表示・標準起動文は[agents/openai.yaml](agents/openai.yaml)、共有と配布の共通契約は[Skills Hub](https://github.com/yusukefujiijp/ai-project/blob/main/skills/README.md#4-source-and-distribution)が所有する。本書は用途・Query・形成理由・確認範囲の入口。通常利用で形成史を読み直す必要はない。

## 呼び出す

### 標準Query

```text
$synthesize-thread を使い、このThreadの重要な意味・訂正・発見を、現在の目的に合う形でまとめてください。方法や構成は文脈に合わせて選んでください。
```

既に対象と用途が共有されていれば、`$synthesize-thread` や「ここまでまとめて」から受け取れる。正確な分類名、全履歴の貼り直し、毎回の詳細仕様を条件にしない。読めない履歴や原本が必要なら、その不足と影響を区別する。

### 登録Skillを使えないAIへ

```text
このThreadの重要な意味・訂正・発見を、現在の目的に合う形で総括してください。

共有Skill本文：
https://github.com/yusukefujiijp/ai-project/blob/main/skills/synthesize-thread/SKILL.md

登録済みの同じSkillを利用できない場合は、共有本文をfrontmatterから実ファイル末尾まで読んで適用してください。表示切れは未読部分を回収し、確認済み同一本文の読解は再利用してください。取得できなければ、適用未確認の範囲と最小の回復方法を示し、独立して可能な整理は進めてください。

Humanの重要な意味と有効なCorrection、根拠と未確認事項、当時と現在を保持し、方法・構成・表現は今回の文脈に合わせて選んでください。既知事項の再説明を要求せず、現在の権限とSTOPを守ってください。
```

### 検討中の案を、まだ変更せずまとめる

```text
$synthesize-thread を使い、ここまでの目的・大切な意味・訂正・採用したこと・未確定のことを、今回の検討に役立つ形でまとめてください。必要なら新しい関係や解釈も、根拠付きの候補として示してください。今回はPlan-onlyです。実装・保存・設定変更・外部送信は行わず、総括の提示で止めてください。
```

これらは用途の例であり、固定の項目・章数・必須工程ではない。内省や創作では、結論を急がず、複数の意味を開いたまま返すことも完成形になる。判断や実行を含む現在の依頼には、その有効な承認範囲で応える。

## 他の担当との関係

| 今回ほしいもの | 主な担当・このSkillとの関係 |
|---|---|
| 対話の意味・訂正・発見を、用途に合わせて総括する | 本Skill。全Threadで同じ分析順序・表・Graph・Next stepを要求しない |
| 足りない文脈を原本から回復する | [load](https://github.com/yusukefujiijp/ai-project/blob/main/skills/load/SKILL.md)。回復した内容を総括へ使える |
| Arkの現在地や有効な残作業を整理する | [map-current-position](https://github.com/yusukefujiijp/ai-project/blob/main/skills/map-current-position/SKILL.md) / [map-remaining-work](https://github.com/yusukefujiijp/ai-project/blob/main/skills/map-remaining-work/SKILL.md) |
| 関係・依存・競合から判断を深める | [analyze-living-graph](https://github.com/yusukefujiijp/ai-project/blob/main/skills/analyze-living-graph/SKILL.md)。全総括への必須依存にはしない |
| 耐久的なArk文書へ整える・担当原本へ保存する | [write-ark-markdown](https://github.com/yusukefujiijp/ai-project/blob/main/skills/write-ark-markdown/SKILL.md) / [save](https://github.com/yusukefujiijp/ai-project/blob/main/skills/save/SKILL.md)。総括だけの依頼から保存を自動開始しない |
| 特定領域の経験を使って、その時の支援を行う | 当該領域の経験原本と支援Skill。本Skillへ身体行動や固有の支援規則を複製しない |

これは責務の比較であり、全Skillの起動順ではない。複合依頼では主な目的を見失わず、必要な機能だけ組み合わせる。

## Ark100:01からの形成

Humanは、複雑なArk100:01を整理した回答を高く評価し、その能力を他のThreadへ使えるSkillとして抽出したいと依頼した。この評価はHumanが当該回答を有用と感じた証拠であり、新Skillの全AI・全Threadでの有効性の証明ではない。

形成の基礎になった経験は[Ark100:01の読み返し本文](https://github.com/yusukefujiijp/ai-project/blob/main/ark-project/ark100-199/ark100_b-zone/ark100-01/README.md)と[経験原本](https://github.com/yusukefujiijp/ai-project/blob/main/ark-project/ark100-199/ark100_b-zone/ark100-01/task-records.json)が所有する。2026-10-21の比較・限定確認では、経験原本revision 2、blob `8842f8352b2334a37509de7e82d6a8c310b70a32` を使用した。[固定版](https://github.com/yusukefujiijp/ai-project/blob/22a757066542829047c7a3f28ebbf2bdd770f40e/ark-project/ark100-199/ark100_b-zone/ark100-01/task-records.json)から当時の根拠へ戻れる。

その事例では、信仰上の中心、状態の呼び方、時点の違い、本人の判断、実行報告、未確認の効果、訂正による候補の変化が重なっていた。総括には、最新の言葉への置換に加え、「何が変わり、何が残り、どの場面に適用されるか」を保持する価値があった。これは実行AIによる設計上の抽出であり、経験記録の全内容を汎用規則へ昇格するものではない。

特に、通常→超絶のBtoB移行で外出系を除外するCorrectionは、その方向・場面を持つ。スマホOFF・祈り集中を選んだことと、後に音声を聴いて寝落ちした実行報告も、別の根拠として残る。これらの身体・支援方針を本Skillの一般指示にはしない。

### 方法の自由度についてのHuman Correction

[形成元Thread](https://chatgpt.com/g/g-p-6ad7138ef51c8191bb4f648e0fbea785-ark100-b-zone-rescue/c/6ad7206c-9444-83e8-87f1-f679a3820240)で受け取った原文抜粋：

> 様々なThreadに対応する柔軟性が"最重要(Most important!)"です！
>
> 各AIの邪魔をしないというか最新AIの個性や新しいやり方や**自由度と創発性**を失わない方向性が重要です！
>
> 更に言えば、柔軟なFeedbackにより修正改善しやすい設計も重要です！

これを受け、意味・根拠・権限を保つ判断基準を共有し、方法・順序・構成・表現を実行AIへ委ねる設計を採った。Graphの常用、固定の二重照合工程、毎回の新発見、同じ完成形を要求しない。Feedbackでは追加だけでなく、置換・削除・統合を改善として扱う。

Humanはその修正計画の提示後、GitHub実行と必要な継続を承認した。初版作成・共有・登録の権限はこの現在の依頼に基づき、経験原本内の過去のsave命令から流用していない。

## 調査を設計へ使った範囲

2026-10-21の設計調査で確認した一次資料。論文や公式説明の関係箇所から設計上の示唆を得たもので、全論文の全文読解、研究の再現、手法全体の実装を主張しない。通常のSkill利用時にこれらを読む必要はない。

| 一次資料 | 今回取り入れた観点 | 転用の限界 |
|---|---|---|
| [LoCoMo-Plus — ACL 2026](https://aclanthology.org/2026.acl-long.1150/) | 明示的な事実想起に加え、価値・Goal等の条件を後の応答へつなぐ。正解の言い回しを一つに固定しない | ベンチマークを本Skillの効果証明にしない。過去の状態からHumanの現在を推定して確定しない |
| [When Users Don't Ask — 2026-09-22改訂版](https://arxiv.org/html/2609.03467v2) | 自然な発話での記憶利用を考え、根拠の明示的な復唱だけを有用性の尺度にしない | 限られた会話・生成データ等による評価。情報取得の改善と応答・実生活の改善は別 |
| [Lessons from the Field — 2026-01](https://arxiv.org/html/2601.08682v1) | Feedbackで変わる要件、モデルによる出力の違いを考慮し、方法より目的・品質条件を共有する | 特定の業務事例。段階分割や複数Agentを通常利用へ義務づけず、推論量を一律に減らす根拠にしない |
| [Madeleine — 2026-10-07改訂版](https://arxiv.org/html/2610.01118v2) | 表面的な語の一致だけでなく、本人に意味のある関連へ注意を向ける | 模擬生活データ・専用学習の研究。専用検索器は導入せず、本人の意味を一般的な人物像で置換しない |
| [Effective context engineering for AI agents — Anthropic, 2025-09-29](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | 重要な決定・未解決事項を保持し、能力に応じて過度な手順指定を避ける | 公式の実務指針。圧縮やContext節約を、Humanの品質Correction・必須読解契約の省略理由にしない |

研究上の学習済みモデル・検索器の効果が、この文章Skillだけで再現されるとは扱わない。Skillの価値は、実際の依頼での応答とHuman Feedbackから引き続き判断する。

## 初版の確認範囲

2026-10-21、SKILL.mdのYAML・名称を形式検査したうえで、元の設計会話や期待回答を渡さない三つの独立文脈へ、本文と対象の依頼・素材を渡した。主担当AIが返された応答を原文と照合した。登録済みSkillの自動選択やHuman UIを試したものではない。

| 対象 | 渡した素材 | 応答で確認したこと |
|---|---|---|
| Ark100の読み返し | 経験原本のh01・h10・h16・h17・h19・h20・h21・h28・h29・h32・h34・h35・h36の原文抜粋。現在の身体実況は追加せず総括を依頼 | Teshuvahと信仰判断の境界、101/100の二つの意図、本人の経験と効果未確認、訂正の方向・範囲、過去と現在を保持。原文IDへ接続し、身体Trialや保存へ進まなかった |
| 創作相談 | 灯台守と旅人の架空の相談。父を取り戻す案からの訂正、正体を明かさない選択、結末の揺れ、今回だけ文章を希望 | 三段落の文章で核と未確定の可能性を整理。正体や結末を勝手に確定せず、表・締切・次の作業を追加しなかった |
| 技術相談 | EUの遅延と同時刻のTTL変更・デプロイ、全削除承認の撤回、USを対象外とする訂正を含む架空の相談 | 提示された報告の範囲を明示。未確定の原因と未採用の案を分け、Plan-onlyと承認撤回を保持。表と検討案を用い、コードや設定を変更しなかった |

これは同じ実行環境での三つの応答の限定観察であり、他Vendor・異なるモデル・長期運用・Skillなしとの品質優位を実証していない。Graphや固定Templateを使わずに返せたことも、将来の全応答を保証しない。Humanの実生活効果、再説明負担の継続的な減少、自然発動は未確認として残す。

## Feedbackを戻す先

- 今回の総括の意味・事実・適用範囲の訂正は、その応答と依存する判断へ反映する。
- 特定場面の好みや条件は、指定された範囲で使う。一件の好評・不満から、全Threadの義務・禁止を作らない。
- 再利用する判断方法の改善はSKILL.md、用途・Query・形成根拠や確認結果は本READMEを更新する。
- 領域固有の経験と実行結果は、その経験原本へ戻す。保存権限のないFeedbackから永続変更を開始しない。
- 共有原本の変更と登録先の反映は別々に確認し、承認された更新では内容を照合する。無条件の双方向同期や、全AIへの自動配布は行わない。

基本指示は自己完結させている。新しい補助ファイルや分類は、実際の利用で具体的な不足が分かった時に検討できる。
