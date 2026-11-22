# Japanese Quality Protocol

日本語の品質・表制約・視点制御を適用するための共通スキルです。

## 利用の入口

### 登録確認後の短い呼出し

```text
$japanese-quality-protocol
```

### 登録の有無を問わず渡す共通Query

```text
【Japanese Quality Protocol：日本語応答の品質を適用する】

宛先：このQueryをHumanが直接入力するThreadのCurrent AI

- japanese-quality-protocol を使い、日本語のまとまった回答で以下を厳守してください。
  - 表の各セル本文はtitleを除き最大3行に抑える
  - 聖書Torah的視点はHumanが明示的に指示した場合のみ使用する
  - ドラフト→自己検査→最終版の順で出力する

- $japanese-quality-protocol を直接利用できない場合は、次の共有原本SKILL.mdを実際に全文読み、指示資料として適用してください。
  https://github.com/yusukefujiijp/ai-project/blob/main/skills/japanese-quality-protocol/SKILL.md

- 自身の確認済み読解は、同一性と適用条件を確認できる範囲で再利用してください。取得・表示切れは未読箇所から回収し、適用される必須Source・読取順・Identity・Binding・Exact EOFを保持してください。

- 本文や必須資料を取得できない場合は、取得できなかったSource・未確認範囲・影響・最小回復を示してください。スキルを読解・適用済みと装わず、適用契約が許す範囲で現在の会話に基づく支援を続けてください。
```

## 共有原本

- SKILL.md: https://github.com/yusukefujiijp/ai-project/blob/main/skills/japanese-quality-protocol/SKILL.md

## 注意

- このスキルはGrok専用ではありません。どのAIでも上記Queryを使って適用できます。
- 表のセル本文はtitleを除き最大3行に抑えることを必ず守ってください。
- 聖書Torah的視点は、Humanが明示的に指示した場合のみ使用してください。
