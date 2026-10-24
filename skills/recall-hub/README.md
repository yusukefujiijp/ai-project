---
title: "Recall Hub / recall-hub"
canonical_path: "skills/recall-hub/README.md"
version: v002
updated: 2026-10-25
updated_reason: Humanが承認した同じSkillの継続改名と、名前なしの自然な場面報告からの入口を整合。経験データ・過去の検証・固定Bindingは保持
status: skill usage and invocation guide
---

# Recall Hub / recall-hub

内容・保存場所・このPortalの使い道そのものを忘れていても、場面やこれからの季節に役立つ経験へ戻るための入口です。主用途はB状態での想起支援ですが、状態の自己診断や申告を利用条件にしません。

利用名はRecall Hub（`recall-hub`）。既存のArk Recall Portalを継続するSkillであり、経験データの保存場所 `ark-recall-portal/` と照合用Identity `Ark Recall Portal` は保持します。旧名を含む形成記録は当時の意味のまま残します。

「今、休日前です」「明日は休み」のような現在の場面報告でも、想起が役立つ文脈なら入れることを目指します。以下のQueryは意図的に呼ぶ入口であり、毎回の貼付や固定の合言葉は利用条件ではありません。引用・設計相談・過去の話は現在の生活合図と区別します。

## 起動Query

今回の対象や場面とともに使います。次は共有版の標準起動文です。配布用の表示設定と意味・本文をそろえますが、実際の登録設定・UIへの反映は別に確認します。

```text
- $recall-hub を使い、今の場面やこれからの季節に役立つ経験・希望・教訓を、現在の条件に合わせて取り出してください。用途が曖昧なら、できることと記録に基づく例から案内してください。
- 共有原本：https://github.com/yusukefujiijp/ai-project/blob/main/skills/recall-hub/SKILL.md
- Skillを直接利用できない場合は、この共有原本を全文読み、必要なSourceの読解条件を守って適用してください。新しい気付きや訂正の保存は、現在の依頼・委任の範囲で扱ってください。
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

## 2026-10-25：Recall Hubへの継続改名

Humanは、覚えやすい呼出名と、Skill名・品名・保存場所を思い出さず自然な場面報告から経験へ戻れる入口を求め、計画提示後にこの範囲の実行を承認しました。改名前の[共有本文](https://github.com/yusukefujiijp/ai-project/blob/5746930c9f9358aec589967cd2354a5b0a368440/skills/ark-recall-portal/SKILL.md)と[利用案内](https://github.com/yusukefujiijp/ai-project/blob/5746930c9f9358aec589967cd2354a5b0a368440/skills/ark-recall-portal/README.md)を継承し、同じ登録物の更新を対象とします。別Skillの追加、経験データの移設、GCI・AGENTS・予定・通知頻度の変更は含めません。

改名は明示呼出しを改善し、descriptionと本文の入口判断は名前なしの選択を支えます。後者の効果は名称変更だけでは確定しません。[確認ケース](../../ark-recall-portal/tests/recall-cases.json)では、文書整合・同一登録物への反映・明示呼出し・対象を事前に教えない自然選択・生活上の効果を分けます。新しいケース定義は実施結果ではなく、以前の明示Skill試験を自然選択の証拠へ変更しません。

旧[共有URL](../ark-recall-portal/SKILL.md)と[README](../ark-recall-portal/README.md)は現行原本への短い読取案内として残し、可変本文・旧UI配布物は二重管理しません。旧コマンドの製品上の別名対応、アカウント画面、自然選択、実生活効果は実際に観測した範囲だけを扱います。固定版・Identity・Bindingを要求する資料には、その指定と互換性確認を保持します。
