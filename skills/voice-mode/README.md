---
title: "Voice Mode — 音声相談の準備と学び"
canonical_path: "skills/voice-mode/README.md"
version: "v001"
created: "2026-10-20"
updated: "2026-10-20"
role: "usage, invocation and formation guide"
---

# Voice Mode

ChatGPT Voiceを使う前の準備、報告された問題の切り分け、会話後の気づき、次に役立つ経験の想起を支えるSkillです。特に、周囲の人から突然相談され、短い準備から必要な対話へ入りたい場面を含みます。

## 起動Query

```text
$voice-mode で、これからの音声相談に必要な準備を手伝って。
```

[UI設定](agents/openai.yaml)と同じ標準起動文です。相談の目的や必要な背景がまだ会話にない時は、普段の言葉で添えてください。会話後の振り返りや問題の相談では、その目的を伝えれば、全工程を毎回やり直す必要はありません。

登録を使えないAIには、次の依頼を渡せます。

```text
次の共有SKILL.mdを実際に読み、Voice Modeを今回の依頼へ適用してください。
https://github.com/yusukefujiijp/ai-project/blob/main/skills/voice-mode/SKILL.md
これからの音声相談に必要な準備を手伝ってください。相談の目的や背景は現在の文脈から確認してください。
```

## 使い方と役割

実際の判断と手順は[SKILL.md](SKILL.md)を使います。ChatGPT Voice内から直接このSkillが呼び出せること、音声会話をAIが取得・監視できること、準備文が自動反映されることは、Skillの存在だけでは成立しません。通常チャットで作る準備文や、Humanが報告した内容からの支援と区別します。

一方向の聴取用本文やTheme提案には[Podcast Mode](../podcast-mode/README.md)を使えます。第三者の相談とHuman本人の事情を混ぜず、準備依頼を外部送信・公開の許可にしません。簡潔な準備は、AIの検討や説明の深さを下げる指定ではありません。

変化する学びの担当原本は[Skillsの集約lessons](../_references/lessons.jsonl)、読取・更新方法は[Skills Hub](../README.md#skills-lessons)です。必要な行の条件・出典・留保を一緒に読み、会話ごとに自動記録したり、専用のlessonコピーを再作成したりしません。

## 形成と確認の境界

2026-10-10、Humanは自分のVoice利用頻度が低くても、AIに疎い他者から突然要望を受ける場面に備え、問題・学びを蓄積する価値を説明しました。この採用理由を、旧Ark-VoiceのVoice→Text→Voice往復を今回実証・再採用したという意味へ変えません。

Radioと同時に形成した経緯、当時のHuman Correctionと出典識別子、四つの構成した相談を使った限定応答確認、初版の本文ハッシュと登録結果は[Podcast側の共同形成記録](../podcast-mode/README.md#radio-voice-formation)に保存しています。Voiceの一応答には友人の混乱の話者帰属が明確でない部分があり、その限定確認から安定性を保証していません。Radio初回登録拒否はVoiceの登録拒否ではなく、独立したVoice本文は通常経路で保存・再取得一致を確認しました。構成した相談をHumanの実経験としてlessonへ登録していません。

10月11日の同時更新時HTTP 422と、その後の単独保存・Remote一致、会話内取得の旧版表示は[後続確認記録](../podcast-mode/README.md#registration-history)へ進みます。10月12日のDotsによる新参照・本文一致の[後続報告](../../records/2026/10/2026-10-12.jsonl)と、10月14日のRadio退役作業でVoiceを範囲外とした事実を区別します。保存成功、会話での取得、UI選択、自然発動、実際の音声対話や長期効果は別々です。

<a id="voice-cutover-current"></a>

### 旧Voice配置の退役 — 2026-10-15

**Voice旧配置の退役（2026-10-15）。**dot-0000: 初穂はHumanの四パス計画への実行承認を受け、旧Voice JSONLを現役配置から除去した。三lessonは集約先に同一行で保持し、Voice本文・登録先は変更していない。登録本文の新たな全文一致を確認し、別の読取経路での取得不能と区別する。現在の確認範囲・保存後検証・復元条件は[STR-015第8節](../../control-center/changes/STR-015-skills-lessons-consolidation.md#voice-cutover-current)へ。[Podcast側の10月14日記録](../podcast-mode/README.md#registration-history)にあるVoice範囲外は当時のRadio実行範囲であり、現在の未完了項目へ戻さない。

この節と共同形成記録は[移管前Hubの固定版](https://github.com/yusukefujiijp/ai-project/blob/369b5f1f287d212848def6121a2ad374aa3e2d77/skills/README.md#skills-lessons-migration)を根拠に、2026-10-20に各SkillのREADMEへ移しました。形成の保存・参照整理は、Voice内直接呼出しや実生活効果の追加検証ではありません。
