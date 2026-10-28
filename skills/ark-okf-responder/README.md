---
title: "Ark-OKF"
status: "Human採用済み共有原本 / Remote保存確認待ち"
design_date: "2026-10-28"
updated: "2026-10-29"
canonical_skill: "skills/ark-okf-responder/SKILL.md"
---

# Ark-OKF

現在の問いへ十分に答え、その意味・根拠・成立条件・訂正可能性を、Human・他AI・Future AIが再読・再利用できるようにするArk Project共通Skillの案内。

規範本文は[SKILL.md](SKILL.md)が所有する。本READMEは用途、呼出し例、形成理由、確認範囲を説明し、別の回答方法や追加の必須Bootを定めない。

## 1. 利用案内

Ark-OKFの適用を明示して、現在の問い・対象を渡す。例は「Ark-OKFで、この設計の判断理由と再検討条件を整理してください」。既に共有した文脈や条件を、毎回入力し直す必要はない。

短い回答、深い比較、Review、引継ぎ等で使える。回答の長さや見出しを揃えることは目的にしない。適用条件と読解・回答方法の詳細はSKILL.mdへ集約する。

共有原本の保存を確認した後に使う、登録状況に依存しない呼出し例：

```text
- この会話の現在の問いにArk-OKFを適用し、問いに合う回答を組み立ててください。
- 共通原本は https://github.com/yusukefujiijp/ai-project/blob/main/skills/ark-okf-responder/SKILL.md です。対応する登録済みSkillを直接利用できない場合は、この共有本文を全文読んで適用してください。同一性・版・文脈・適用条件を確認できる自身の全文読解は再利用し、必須Source・読取順・Identity・Binding・EOFを保持してください。取得・表示切れは回収し、必須Sourceが不足する場合は影響と最小の回復方法を示してください。
- この呼出しから新たな保存・登録・外部送信の権限を作らず、現在の依頼の対象とModeを保ってください。
```

通常は現在の問いと短い呼出しで足りる。この例を唯一の起動句や、別管理の起動原本にしない。

## 2. 原本・案内・配布の役割

Ark-OKF固有の意味、適用、読解、回答方法は共通SKILL.mdに置く。Grok等の旧配置やPrompt棚は現行本文への案内とし、独立した規則を持たせない。

[Skills Hub](https://github.com/yusukefujiijp/ai-project/blob/main/skills/README.md)は発見・配布の入口、各環境への登録物は共有原本の配布先である。登録物の存在・版・取得・呼出し・挙動は環境ごとに確認する。GitHub保存から全AIへの導入や自動適用を推定しない。

Original OKFの公式仕様、Arkの共通権限、関連する研究・Graph・表・文章構成の資料、Wiki・Referencesは、それぞれの役割を保つ。本Skillへの統合は、それら全体の移行や複製を意味しない。

## 3. 形成理由と根拠

2026-10-28のこのThreadで、YusukeJPは、Grok版とArk Project版を分けず、Ark Projectの完成版一つに統一したいと訂正した（意図の要約）。起動と本文を同じ現行原本へまとめ、利用するAIによって訂正先や判断原則が分かれることを防ぐための統合である。これは共通化の設計意図であり、各環境への登録・実利用の成立を表さない。

統合元は、[共有Promptの固定版](https://github.com/yusukefujiijp/ai-project/blob/18dcea61849d337c37e733ee18debe6887a4d9ef/prompts/ark-open-knowledge-format.md)と[Grok起動面の固定版](https://github.com/yusukefujiijp/ai-project/blob/18dcea61849d337c37e733ee18debe6887a4d9ef/grok/skills/ark-okf-responder/SKILL.md)。採用済みP1〜P5・G1〜G4を反映した当時の本文、metadata、形成史へ戻れる。

旧Bootstrap名は `S_Ark-open-knowledge-format_v002.md`。旧 `class: S` とともに形成上の識別情報として残し、現行の起動ファイル名や公式OKFの版とは扱わない。

旧Prompt §11の、v002形成時の確認範囲は次の記録である。

> このArk-OKF理解は、OKF紹介記事再読に基づく部分を含む。
> OKF v0.1仕様書全文の独立読了としては扱わない。

後続の改訂では、[Original OKF v0.2の固定SPEC](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/ad30107c31c06aec8a7d5636e0d1058118604e6f/SPEC.md)を、冒頭から§13・付録A末尾まで確認した記録がある。仕様blobは `c06e3eede0c910d0ecf12524c34204156f8795ac`。後の確認で当時の未読を書き換えず、受け手自身の読解とも区別する。

旧Prompt §16には、英語比率が高くなった出力を受けてJapanese-first／English-anchorを重視した形成時の判断が残る。当時の記録と表現は固定版に保持し、現在の品質条件は共通SKILL.mdが所有する。原文中の成功評価から、全AIでの効果を推定しない。

旧Engine／Query分割の撤回は[STR-002](https://github.com/yusukefujiijp/ai-project/blob/79770085364871cd026cb12ff669593fbf6cf6f4/control-center/changes/STR-002-single-prompt-consolidation.md)に残る。今回も別のLauncherや短縮版で二重管理を再開せず、起動に必要な意味を共通本文へ統合する。

## 4. 確認範囲

以下は2026-10-28の統合案作成時点の状態である。

- 基準Repositoryは `yusukefujiijp/ai-project`、Refは `main`、確認snapshotは `79770085364871cd026cb12ff669593fbf6cf6f4`。
- 共有Promptと現行Grok版は、採用済み改訂を含む本文として存在する。
- 共通 `skills/ark-okf-responder/SKILL.md` はこのsnapshotでは未作成で、Skills Hubにも未掲載。
- 旧 `skills/_grok/ark-okf-responder/SKILL.md` には以前の指示本文が残る。実際にどの環境で使われたかは、この存在確認だけでは分からない。
- 本統合案の保存・旧本文退役・登録・別AIの理解・実際の挙動・実利用の効果は、この設計時点では未確認。

後続の実施結果は、確認した対象・版・内容とともにこの確認範囲へ追記・更新する。実施前の状態は時点付きの形成記録として保持し、観測していない段階を完了扱いしない。

## 5. 採用・実装・確認 — 2026-10-29

Current Humanは、このThreadの完成稿と18パスの対応表を採用し、GitHub共有原本の統合・必要な案内修正・保存後確認を承認した。各環境へのSkill登録、設定変更、他AIへの送信は承認Scopeに含まれない。

実装基点は `79770085364871cd026cb12ff669593fbf6cf6f4`。採用稿の規範本文を共通SKILL.mdへまとめ、旧二本文の退役、旧Promptの案内化、Hubと現用参照の整合を一つの変更範囲として扱う。旧サンプルと対象外資料・形成史を保持する。

この段階では、保存後のRemote再取得と結果記録は未完了。確認結果が得られてから本節を更新する。登録・別AIの実理解・実際の挙動・実利用の効果は未確認のまま区別する。
