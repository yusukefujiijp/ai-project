---
title: "Ark Recall Portal / ark-recall-portal"
version: v001
updated: 2026-10-20
status: skill usage and invocation guide
---

# Ark Recall Portal / ark-recall-portal

内容・保存場所・このPortalの使い道そのものを忘れていても、場面やこれからの季節に役立つ経験へ戻るための入口です。主用途はB状態での想起支援ですが、状態の自己診断や申告を利用条件にしません。

## 起動Query

今回の対象や場面とともに使います。次は現行UIの標準起動文です。

```text
$ark-recall-portal を使って、今の場面やこれからの季節に役立つ経験を思い出せるようにしてください。新しい気付きは記録の意図を受け取り、用途が曖昧ならできることと記録に基づく例から案内してください。
```

## 使い方と担当原本

「何ができる？」「10月に備えて思い出すことは？」のように、用途の案内や未来の時期からも入れます。実際の記録に基づく例を示し、未整理の気付き・訂正も受け取ります。共通運用・保存規約と経験項目は[Portal入口](../../ark-recall-portal/README.md)が所有し、スキル内に全経験を複製しません。会話での受領・承認された保存・実際の想起効果は別々に扱います。

経験原本を保存する場合は、Portalが指定する担当先と[Task Recordsの契約](../../formats/task-records/README.md)へ接続します。通常の読出しだけで保存作業を始めません。

## 形成と確認の範囲

以下は移管前Hubに記録された各日付当時の形成・確認です。文中の「今回」や未検証事項は当時の範囲を表し、現在の効果を保証しません。

2026-09-28、Ark28:01でHumanが承認した二場面の初版計画から、`ark-recall-portal`を追加しました。旧称はArk Recall Hubです。用途そのものを忘れた状態でも「何ができるか」と実際の記録の例から入れる想起の入口を優先し、場面が分かる入力には直接応じます。反省の事実はThread経験原本、取り出しやすい項目はPortalのitems、共通運用はPortal README、呼出しはSkillへ分けます。現在地mapは必要時の接続先であり、今回その本体を変更・再配布したとは扱いません。初期の二場面は成長の上限ではありません。

共有版は本文と最小の表示設定です。自然な自動選択、全AI互換性、実生活での想起効果は、設定・保存・限定応答確認とは別です。[Portal入口](../../ark-recall-portal/README.md)と[検証ケース](../../ark-recall-portal/tests/recall-cases.json)で確認範囲を示します。専用のQueryファイル、全履歴の移植、通知・常時監視、Main移管は含めません。2026-09-12のexport-manifestは当時の記録として変更しません。

## 文書の役割と更新

このREADMEは説明・起動Query・形成と確認範囲を、[SKILL.md](SKILL.md)は実際の判断と手順を所有します。QueryはこのREADMEで管理し、別のQuery専用フォルダへ分けません。[表示設定](agents/openai.yaml)の標準起動文にはUI上の役割があるため、対応するQueryの変更時は意味の整合を確認します。READMEの全文を毎回の起動条件にはしません。

2026-10-20のREADME整備では、現行本文・表示設定と[移管前Hubの固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md)を根拠に、このスキルの入口と記録を個別化しました。本文中の日付付きの確認は各時点の証拠であり、今回の文書移動による再試験や全環境の動作保証を意味しません。共有・導入の共通方針は[Skills Hub](../README.md#4-source-and-distribution)を参照します。
