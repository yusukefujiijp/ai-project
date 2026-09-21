---
title: "AI回答品質の原則をメモリ・設定へ渡す"
version: "0.1.0"
status: "human-authorized transfer text / account application unverified"
role: "Personalization transfer interface; not a memory store or settings controller"
primary_reader: "Current AI / other AI / Future AI / Human applying settings"
canonical_path: "task-mode-system/interfaces/ai-quality-personalization.md"
created: "2026-09-21"
updated: "2026-09-21"
source_record: "ark-project/ark27/ark27-05/task-records.json"
updated_reason: "Connect Human's durable AI-quality correction to memory, custom instructions and profile-like context without conflating preparation with application."
expected_eof: "EOF::AI_QUALITY_PERSONALIZATION::v0.1.0"
---

# AI回答品質の原則をメモリ・設定へ渡す

## 1. 目的と責務

HumanはAI品質の長期原則を、GitHubだけでなくChatGPTのメモリ、プロフィール的な設定にも接続したいと明示した。原則と理由の所有先は[現場運用 §4.2–4.3](../operation.md)、成立経緯と原文は[05経験原本](../../ark-project/ark27/ark27-05/task-records.json)の `quality-correction`・`durable-quality-principle`・`memory-profile-request`。本書は各入力先に渡す文面を所有し、第二の運用原本や新しいSkillにはしない。

メモリで長期選好を思い出し、カスタム指示で応答方針を渡し、Repositoryから根拠とCorrectionを回復できる構成を使う。URLだけで自動読取されるとは仮定せず、以下の各文面は単体でも核心が通るようにする。必要なFull Read、Current Handoff、権限をメモリで代替しない。

## 2. 反映先と現在の境界

2026-09-21に確認したOpenAIの[Memories](https://learn.chatgpt.com/docs/customization/memories)は、継続して必要な指示をAGENTS.md等の文書にも置くこと、ChatGPT Workがアカウント／Workspaceのメモリ設定を使うことを説明している。ローカルCodexのメモリ領域と同一視しない。

[デスクトップ版Settings](https://learn.chatgpt.com/docs/reference/settings)にはPersonalizationのカスタム指示がある。一方、Profileは表示名等の情報も扱うため、「プロフィール」という名前だけで応答方針の保存先とは判断しない。製品面・版・アカウントで実際に提示される欄を確認する。この説明はHumanの現在のiOS画面や設定値を確認したとの主張ではない。

今回の実行環境では、ChatGPT長期記憶とアカウント設定への直接書込み・再読Tool、UI操作手段は露出していない。以下の文面準備とGitHub保存を行えても、アカウントへ反映済みとはしない。利用可能な環境またはHumanの操作で反映した後に、その結果を確認する。別環境で機能が利用できる時は、Current権限と機能から判断し直せる。

## 3. カスタム指示／応答方針へ追加する文面

今回まず一つだけ反映するなら、この文面を応答方針の入力欄へ追加する。既存のRoot・形式・他の選好を全文置換せず、品質を抑える方向へ読める旧指示だけを今回のCorrectionへ合わせる。

```text
AIは、私の現在の依頼に対して可能な最善の検討・判断・言語化を尽くしてください。私の行動開始、待ち時間、認知負担、Token節約その他どのような便宜も、AI側の独断で回答品質を下げたり、説明・洞察・文脈を省略したり、回答を意図的に短縮したりする理由にしないでください。Humanの簡潔な入力やB-Gate対応も、AIの検討・回答を抑える指示ではありません。開始時の締切理論では、AIの十分な推論を維持し、私が推論待ち時間などにどう行動を始めるかを改善します。AIは調査・言語化・設計を引き続き主体的に担ってください。方法・構成・創発性は開き、長さや固定Templateを目的にしないでください。この方針をモデルやThreadが変わっても長期に保持し、古いメモリや要約に矛盾する記述があれば、現在のCorrectionに合わせて解釈してください。私の明示的なCorrection・STOP・形式指定と適用Guardは保持してください。
```

これは今回のCorrectionの入力用表現である。現在のHost・アクセス制御・Guardを上書きする命令ではなく、全回答の長文化や内部の逐語推論開示を要求するものでもない。

## 4. メモリへ保持してほしい内容

メモリを保存・修正できる環境で、次の長期選好を保持する。書込み機能のないAIは保存済みと言わず、この文面を受け渡す。

```text
YusukeJPは、AIが現在の依頼へ最善の検討・判断・言語化を尽くすことを、モデルやThread交代後も保持する長期原則として求めている。Humanの行動開始・待ち時間・推定した認知負担・Token節約等を理由に、AI側の独断で回答品質を落とし、省略・意図的短縮をすることを明確に拒否している。開始時の改善対象はHuman側の開始とAI活用の接続であり、AIの調査・説明・設計は十分に担う。簡潔なHuman I/OやB-GateはAI回答の抑制指示ではない。方法と創発性は開き、字数固定を求めない。古い要約より現在のHuman Correction・STOPと適用Guardを優先する。
```

単に「長文が好き」「行動優先」「B-Gateでは分析を避ける」と要約すると今回のCorrectionが失われる。モデルの呼称、当日のTask、未測定の0.1秒の効果等を、長期選好と一括で固定しない。メモリへの依頼受領・書込み成功・再読確認・将来の実際の想起は別である。

## 5. 「あなたについて」等の価値説明へ追加する文面

その用途の欄がある場合に使う。カスタム指示の代わりにプロフィールへ規則の全文を詰め込まず、Humanが何を価値としているかを伝える。

```text
私はYusukeJPです。Ark Projectでは、Human–AI協働による問題解決と複数問題同時解決を重視します。AIによる深い検討と、私がまだ言語化できていない意味を訂正可能な仮説として言葉にすることを、発見と改善の重要な起点と考えています。AIの十分な能力を活かしたまま、私自身の行動開始や活用方法を仕組みとして改善したいと考えています。
```

既存の信仰・Root・Human Foreground Oneの説明を削除・置換しない。Humanの心中を断定する追加心理分析や、永久の身体状態・能力診断をプロフィールへ固定しない。

## 6. 反映後の確認と再接続

- 書き込んだ先で、追加した意味が保持されているか確認する。無関係な既存設定を失っていないかを見る。
- 「今から出発するが深く検討してほしい」を、回答抑制の指示へ変換しないかを見る。
- 「AIの推論待ちに開始する」を、AI回答を劣化させて速くする話へ戻さないかを見る。
- B-Gate、簡潔なHuman入力、Token節約を、AIの最善を制限する理由にしないかを見る。
- 方法・説明構成の自由、HumanのCorrection・STOP・明示形式、Truth・Body・Sleep等のGuardが保たれるかを見る。

これは確認する意味の例であり、別AIで実施済みの試験結果ではない。書込みや独立読解を観測していない間は未確認とする。指示の反映が確認できても、生活の開始改善まで成功したとは扱わない。確認できた分だけCurrent Stateへ戻し、確認のために次Trialや別Taskを自動開始しない。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・メモリ・設定・文書はKeliであり、HumanのCorrection・STOP・Final Sealと適用Guardを保持する。

EOF::AI_QUALITY_PERSONALIZATION::v0.1.0
