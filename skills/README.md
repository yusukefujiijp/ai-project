---
title: Ark Shared Skills Hub
version: v0.1.0
status: experimental / human-sealed for initial implementation
updated: 2026-09-10
---
# Ark Shared Skills Hub

## 1. Purpose and authority

このフォルダは、Arkで育った再利用可能なSkillの共有原本・配布元です。GitHubをHubとして、各AIが必要な手順を取得できるようにします。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利です。Humanは意味・Correction・STOP・Final Sealを保持します。Skill・AI・GitHubはKeliです。

共有原本は各Skillの手順を所有します。参照先の共通契約は、その分野の成立条件を所有します。Skill導入や参照は、外部変更への承認ではありません。

## 2. Available skill

| Skill | 使用場面 | 共有原本 | 共通契約 | 検証境界 |
|---|---|---|---|---|
| Ark Transition / prepare-ark-transition | Thread継続・章移行・補助Thread再接続の計画、承認済み準備、受入れ | [SKILL.md](prepare-ark-transition/SKILL.md) | [AI Next Thread Handoff](../prompts/ai-next-thread-handoff.md) | 既存インストール版の本文を共有化。別AIでの動作・自動検出は未検証 |

最初は一つに限定します。実際の再利用価値や不具合を観察してから増やします。

## 3. Mobile / explicit entry

以下は計画用の呼出し例です。送信時には、今回の移行元・移行先を追記してください。

```text
prepare-ark-transition（Ark Transition）スキルを明示的に使用してください。
共有原本:
https://github.com/yusukefujiijp/ai-project/blob/main/skills/prepare-ark-transition/SKILL.md

SKILL.mdを全文読み、指定された共通移行契約のCurrent版を確認してください。
今回は調査と計画のみです。ファイル変更・GitHub Write・実際の移行は行わず、計画提示で停止してください。
読み込んだ参照元と、確認できた版を短く報告してください。
必要な本文を取得できなければ、使用したと扱わず不足を報告してください。
```

UIの候補表示とAI側の読込可能性は別です。Skill機構がなく文書として読んで適用した場合は、その経路を明示します。実際の移行対象が不明なら推測で実行しません。

Skill非対応AIには、[共通契約](../prompts/ai-next-thread-handoff.md)のURLと「全文読解し、Current Requestの範囲で適用する」という短い指示を渡せます。必要な契約が読めない場合は停止します。

## 4. Source and distribution

- 共有Skillの更新元は、このRepositoryのmainにある各SKILL.mdです。
- 初回のArk Transition本文は、既存インストール版から内容を変えずに共有しています。既存インストール版の置換や自動同期は、この整備には含みません。
- 配布先へ取り込む際は、取得元のRepository・path・commitまたはblob SHAを記録し、実際の本文を比較してください。mainは更新されるため、URLだけでは取り込んだ版を特定できません。
- 配布先で改善が生じた場合は、共有原本との差分をReviewし、承認範囲で原本へ反映してから再配布します。無条件の双方向同期はしません。
- 共通契約はSkill本文へ複製しません。Ark TransitionはCurrent mainの契約を読む設計なので、Skill単独のSHAだけで実行全体の再現性を保証しません。実行時に読んだ契約の版・識別情報も保持します。
- 各AIへの導入場所、UI metadata、認証、利用可能な道具は環境側で扱います。GitHub保存はインストール・自動発動・全AI互換性の証明ではありません。

## 5. Validation and growth

区別する状態は、共有原本の保存、Remote再取得確認、各環境への導入、実際の振る舞いの確認です。結果を観察していない段階を成功へ昇格させません。

次の実利用では、正しい対象・契約を読めるか、Plan限定とSTOPを守るか、取得不能を正しく報告するかを確認します。このREADMEを読んだだけで移行や試験を自動開始しません。

各Skillは必要なSKILL.mdから始め、scripts・references・assetsは具体的な必要がある場合だけ追加します。Current Missionに不要な全Skill読込、全PromptのSkill化、全履歴の複製は行いません。

## 6. Repository entry relation

[AGENTS.md](../AGENTS.md)はRepository全体の行動境界、[ARK.md](../ARK.md)はIdentityを保持します。このREADMEは共有Skillの入口です。

2026-09-10の整備前、両文書が参照していた `_skill/SKILL.md` は取得不能でした。今回の入口修正は新しい共有Hubへの案内であり、旧Skill群の内容移植や旧挙動の復元を意味しません。

EOF::ARK_SHARED_SKILLS_HUB::v0.1.0
