---
title: "AI Living Graph Mode / analyze-living-graph"
version: v001
updated: 2026-10-20
status: skill usage and invocation guide
---

# AI Living Graph Mode / analyze-living-graph

依存関係、競合する価値、Feedback、進まない接続を読み、要素を独立して並べるだけでは見えない判断材料を返すスキルです。図を描くこと自体を目的にせず、探索・比較・決定・承認済み実行のどこにいるかに合わせます。

## 起動Query

今回の対象・相談とともに使います。次は現行UIの標準起動文です。

```text
Use $analyze-living-graph to discover relation-native insight, preserve useful exploration, and choose a guarded next connection appropriate to the current request.
```

## 使う場面と読む先

例えば、二つの改善案の価値が競合しているときや、Humanの訂正で「先に済ませる必要がある」と考えた依存が変わったときに使えます。単純な事実確認や図だけの依頼には、一律に適用しません。

- [Graph operations](references/graph-operations.md)：関係の型、接続、切断、競合が判断に効くとき。
- [Living updates](references/living-update.md)：予測とActual Reality・Human Feedbackから見立てや次の経路を更新するとき。
- [Ark binding](references/ark21-binding.md)：Arkの信仰・権限の文脈が適用されるとき。歴史的なArk21例で現在の章や依頼を巻き戻しません。

新しい図や表だけではLiving updateとは扱いません。実際の観察・訂正・新しい制約が、どの関係判断を変えたかを区別します。描画基盤が必要なArkの可視化は[Visualize Patch](../visualize-patch/README.md)へ接続します。

## 導入と確認の境界

現行の共有[表示設定](agents/openai.yaml)は明示呼出しを指定しています。別製品で同じ選択挙動が再現される保証ではありません。Skill機構がないAIには[本文URL](https://github.com/yusukefujiijp/ai-project/blob/main/skills/analyze-living-graph/SKILL.md)と現在の依頼を渡し、必要な参照だけを同じ相対配置から読めます。URLの提示を導入完了とは扱いません。

[移管前Hubの一覧とCross-AI案内](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md#2-available-skills)は、改訂本文と参照資料の共有、限定応答確認、別製品での再現性が未検証である範囲を保持しています。2026-10-16の説明用可視化への接続は、[Visualize Patchの形成・確認記録](../visualize-patch/README.md)と現行SKILL本文へ戻れます。

## 文書の役割と更新

このREADMEは説明・起動Query・形成と確認範囲を、[SKILL.md](SKILL.md)は実際の判断と手順を所有します。QueryはこのREADMEで管理し、別のQuery専用フォルダへ分けません。[表示設定](agents/openai.yaml)の標準起動文にはUI上の役割があるため、対応するQueryの変更時は意味の整合を確認します。READMEの全文を毎回の起動条件にはしません。

2026-10-20のREADME整備では、現行本文・表示設定と[移管前Hubの固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md)を根拠に、このスキルの入口と記録を個別化しました。本文中の日付付きの確認は各時点の証拠であり、今回の文書移動による再試験や全環境の動作保証を意味しません。共有・導入の共通方針は[Skills Hub](../README.md#4-source-and-distribution)を参照します。
