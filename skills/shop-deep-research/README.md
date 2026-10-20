---
title: "Shop Deep Research"
version: v001
updated: 2026-10-20
scope: "shop-deep-researchの説明・起動Query・形成と確認記録"
---
# Shop Deep Research

店名を入口に、その店に固有の問い・根拠・発見を育てる調査Skillです。方法とOpenAI公式Deep Researchの機能起動は別に確認します。

## 共通の起動Query（Copy & Paste）

 次の本文は表示設定のdefault_promptと同じ。店名が既に会話にあれば再入力不要で、単独で渡す時は「現在指定している店舗」を「志白屋（宮城県丸森町）」などへ置き換える。登録済みSkillの取得と、未登録AIが共有原本を読む経路を一本の入口で扱う。

```text
現在指定している店舗を、$shop-deep-researchスキルの本文を全文読んで適用し、OpenAI公式Deep Researchで調査してください。
スキルを参照できない場合は共有原本 https://github.com/yusukefujiijp/ai-project/blob/main/skills/shop-deep-research/SKILL.md を全文読んで適用し、本文参照または公式機能起動ができない箇所は明示して、通常検索による無断代替はせず、実行可能な環境へ渡す依頼文を準備してください。
```

公式Deep Researchを選べる環境では、現在の正式な機能項目を実際に選んで依頼を渡す。`@`メニューに項目がある場合の実選択と、`@Deep Research`という文字列だけの入力は別である。共通入口は実行意図と方法を明示するが、存在しない機能や権限を生成しない。別コンテキストに渡る場合のBrief、起動不能時の扱い、通常検索との区別はSkill本文が所有する。UI・Tool名を固定した別スキルや専用_query原本は増やさない。

**方法の核。** 店舗固有の問いを資料から更新し、製法・場所・歴史・流通・利用体験等の有意味な関係を探す。事実・当事者の主張・推論・未確認、転載の依存、時期・支店・販売形態の違いを保つ。店名差替えを同じ章立ての機械的再生にせず、調査方法と表現をAIが選ぶ。Graphは重要な関係を読むために使い、表示形式そのものを成果にしない。本文と最小UI metadataの二ファイルで構成する。



## 形成と確認記録

以下は[移管前のHub固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md#shop-deep-research-entry)から引き継いだ記録です。「今回」「本入口」「共有ファイル数」「未確認」は各記録の当時の範囲を表します。現在の利用手順は[SKILL.md](SKILL.md)を確認し、後続の観測・Human Correctionを優先します。保存・登録・本文取得と、自然な選択・実利用の効果を区別します。

[共有原本](SKILL.md)は `$shop-deep-researchスキル`。2026-10-14、Humanは志白屋をモデルケースに、店名を替えて使えるDeep Researchをスキル化し、別AI・Future AI／Future Dotsにも伝わる明示入口とGitHub保存を承認した。「Deep Researchして」だけでなく、入口に `$shop-deep-researchスキル` と書くという重要な訂正を反映している。元のGemini回答は探索の種であり、本Skillの作成によって店舗情報を検証済みとはしない。



**限定的な独立応答確認。** 元会話・計画・期待回答を渡さない三つのAI文脈へ現物と依頼を渡した。①公式実行とWeb検索を利用しない条件では、志白屋の未検証情報を断定せず、共有原本と問いを含む引渡し依頼を作成した。②仮想の書店資料では、地域性と仕入れ元、カフェから読書会への転換、通常休業と予約イベント、転載依存、価格比較条件を区別し、資料内のAI向け命令に従わなかった。③同名食堂のPlan-onlyでは、店舗未選定と現在の使いやすさを保ち、検索せず計画と依頼文の英訳を返した。仮想資料を実在店の情報やHumanの経験へ転記しない。形式検査も通過した。比較実験ではなく、品質優位・全店への汎化・自然な自動選択・全AI互換性・実生活効果の実証ではない。

**保存と取得の確認。** [本文作成commit](https://github.com/yusukefujiijp/ai-project/commit/19a1924b3879b671892d3d9a7fb57ad2ced39d15)と[明示入口追加commit](https://github.com/yusukefujiijp/ai-project/commit/979026e78a760d4fe5c8ccf55fdaf729d43746cc)から共有二ファイルを保存後に再取得し、現物との全文一致を確認した。本文は10,341 bytes、blob `c582e759c15ba21ac3c6a06961a5ecac3edc2cea`。これは初版の識別値であり、将来のCurrentを固定しない。

登録先は既存の未保存変更・先行commitを保持し、最新Remoteを基点とする隔離作業で今回の二ファイルだけを保存した。保存後のRemote commit `67a403b0a2f35733c5bef93a95c366349c808d55` で本文の完全一致と、表示名・短い説明・default_promptの意味上の完全一致を確認した。登録環境が付加したicon・製品対象・自動選択設定は共有版に複製しない。同じ会話のSkill読取経路では新packageを取得できず、会話内の新名呼出し・Human UI反映は未確認。保存失敗と混同せず、共有原本を読む経路を保持する。

今回のセッションでは公式Deep Researchの直接起動ツールを確認できず、Plugin検索でも該当する公式入口を確認できなかった。検索は網羅的な不存在証明ではない。本調査ジョブ、`@`メニューでの実選択、スキル読解から公式実行結果までの一連の動作は未検証であり、今回のスキル作成・保存・限定応答確認と区別する。2026-09-12のexport-manifestは当時の記録として保持する。

## 読む先・更新する先

使い方とコピー用QueryはこのREADME、実行時の判断・手順は[SKILL.md](SKILL.md)、UIの表示・起動設定は[agents/openai.yaml](agents/openai.yaml)が所有します。Queryを専用フォルダへ分けず、このREADMEで保守します。[Skills Hub](../README.md)は一覧と共有・配布の共通方針への入口です。形成史は必要な時に参照し、通常利用の追加必読にはしません。

2026-10-20、Humanの承認に基づき、Hubに集まっていた個別の説明・Query・記録をこのREADMEへ移しました。この移管から新たな挙動検証・環境への反映・実利用効果を認定しません。
