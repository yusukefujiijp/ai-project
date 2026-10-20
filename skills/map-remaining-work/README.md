# 残作業とGoal — map-remaining-work

README版: v001 / 2026-10-20（Asia/Tokyo）

今も必要な仕事と、その仕事が目指す状態・根拠・担当・再開条件を復元するスキルです。現在の依頼・会話・成果・訂正・原本から直接整理でき、前回のMAPを準備する必要はありません。ChatGPT Dotsを主経路、Workを補助経路とし、他AI・Future AIでは実際の役割と能力に合わせます。

## 1. Copy & Paste — 残作業とGoalを整理する

短い入口は次のとおり。対象Thread・案件・範囲の指定があればその指定を優先する。

~~~text
$map-remaining-work を使い、現在の残作業とGoalを整理してください。
~~~

[共有本文](SKILL.md)は、現在の協働から有効な残作業とGoalを根拠に沿って復元する独立入口。[表示設定](agents/openai.yaml)は表示名・短い説明・この呼出し文を所有する。Dotsを主用途とする明示的な経路、Workを補助用途とする経路、他AI・Future AIへの適応経路を一つの本文に置く。環境、役割、実際の能力・権限を分け、すべてのDotをChiefとみなさない。前回Mapや他Skillの全件登録を条件にせず、読めない範囲を黙って縮めて全体確認済みとしない。

現在地全体を扱うmap-current-positionと、[既存のMAP後深掘りQuery](../map-current-position/README.md#remaining-work-goal-deep-dive)は保持する。後者はMAPの特定節を起点に深める入口であり、新Skillは現在の依頼・会話・成果・訂正・原本から残件を直接引き出す。第二のTask台帳や環境別のSkill複製は追加しない。

整理の依頼だけでは保存・実装・送信・他AIの仕事の引取りを始めません。同じ依頼や後続依頼に明確な実行承認がある場合は、その範囲を適用します。登録Skillのない環境では[共有本文](https://github.com/yusukefujiijp/ai-project/blob/main/skills/map-remaining-work/SKILL.md)を実際に読み、指示資料として利用できます。読めない範囲や未報告を、完了・未実行・失敗へ推定で置き換えません。

<a id="map-remaining-work-entry"></a>

## 2. 形成・保存・確認の記録

以下は[旧Hubの同節](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md#map-remaining-work-entry)から移した2026-10-17の記録です。「今回」「未確認」は当時の観測を指し、後続の取得確認までを含みます。構成した検証例とHumanの実経験、保存・会話内取得・実利用効果を区別します。

**形成と承認（2026-10-17 JST）。** YusukeJPは定時MAPの残作業とGoalを中心的価値として評価し、長いQueryの負担からSkill化を希望した。AIが理解全般へ広げた命名案に対し、HumanはRemaining workを中心Keywordと訂正し、map-current-positionと対になるmap-remaining-workを提案した。さらに、Dots主用途・Work補助用途・他AIへの拡張を、単なる共通化で薄めず分岐として書くよう指定した。繰り返すPlan Modeの後、Humanメッセージ `Sentinel_66cb3b3fad408191a12fea052edbec97` で作成・共有・登録・確認の計画への実行承認を受けた。形成上の重要訂正は `Sentinel_07a506268b048191bdc3d664ca7c6100`（Remaining work）、`Sentinel_4cdde4d0320c81919a34059e56a4ec03`（既存Queryとの分離）、`Sentinel_de62a2b0ddfc8191a77c81290f402626`（環境別分岐）。いずれもこのDotの会話識別子で、公開会話URLではない。

**変更範囲。** 新Skill本文・最小表示設定・本Hubの案内と形成記録・保存日records、および個人Skill一件の導入。既存MAP本体、既存深掘りQuery、定時運用、予定、Board、他AI送信は変更していない。私的Work・別会話・長期メモリを実例として公開転記しない。例示検証は架空素材でありHumanの活動記録ではない。

**限定検証。** 形式検査と四つの独立AI文脈で計六応答を確認した。Dotsの複数担当・古いpendingと後続完了・担当読取不能、Workの以前の依頼・取消し・未採用案・引用の英訳、Inboxの役割境界、他AIの完了済み成果と別件必須資料不足を扱った。初回のDots応答には、次Threadでの比較を移行判断の前提へ読み替える余地があったため、Human指定の順序と比較目的を推測で変更しない条件を追記した。新しい独立文脈では、明示された「移行、その後比較」を保ち、削除判断を別扱いにする応答を確認した。これは限定応答であり、自然な選択・全製品の実機・全AI互換性・認知負荷軽減や生活効果の実証ではない。

**保存と導入。** [本文保存](https://github.com/yusukefujiijp/ai-project/commit/7d9c545b238566cddd1e921db4762337c58e53f1)と[表示設定保存](https://github.com/yusukefujiijp/ai-project/commit/eb90bfcf8aa866aaa63d4a6274a3a45ed6ab50ce)の後、mainから全文再取得し一致を確認した。本文blobは `a250da9e775a0d6f1f0d8e694fce252866a4930c`、表示設定blobは `c11c8d965614844c8d5ddb822c186f7d7c01a448`。個人Skillも作成・導入し、保存先に同名一件、本文一致、表示名・短い説明・呼出し文の一致を確認した。環境が付与する設定は共有版へ複製しない。この時点では会話内Skill取得経路が利用不可で、会話内からの全文取得は未確認。保存成功と参照経路の状態を混同せず、再作成しない。


**後続の取得確認（同日）。** 取得経路が利用可能になった後、登録済みmap-remaining-workの本文を会話内で末尾まで取得し、上記の共有本文と完全一致を確認した。先の取得不可は保存直後の観測として保持し、現在の阻害条件へ戻さない。再登録は行っていない。自然な自動選択・実利用の有用性・全環境での動作は別の確認である。

## 3. 更新先

判断と手順は[SKILL.md](SKILL.md)、コピー用Queryと利用案内・形成記録は本README、UIの短い表示・起動文は[agents/openai.yaml](agents/openai.yaml)へ置きます。Queryの配置変更を理由に、既存MAPの深掘りQueryや現在地MAP本体を再設計しません。共通の配布と照合は[Skills Hub](../README.md#4-source-and-distribution)を参照し、本READMEの履歴を通常利用の必須読込にはしません。
