---
title: "Codex — 目的と経験から再開する協働の入口"
canonical_path: "agents/codex/README.md"
version: "v001"
created: "2026-10-31"
updated: "2026-10-31"
date_basis: "UTC; activity records use their own Asia/Tokyo placement contract"
role: "Codex collaboration entry; route to runtime, experience and shared method owners"
expected_eof: "EOF::ARK_CODEX_HOME::v001"
---

# Codex

YusukeJPとCodexの協働を、元の会話を知らないCodexや他AIが引き継ぐための入口。今回の目的に応じて、確認済みの実行条件、共有Skill、関連する反応・学び・成功を選び、根拠と後続の訂正を読んで判断へつなげる。Humanによる長い再説明や初回設定の繰り返しを減らし、経験を次の仕事に生かすことを目指す。

最初の対象は、保存済みプロフィールを使うChatGPT接続の再現性と、その協働で得た経験。成果物はそれぞれの専門領域、共通方法は共有Skillに保つ。Codexが制作したという理由だけで、成果物全体をここへ集めない。

## 今回の仕事から読む

| 今したいこと | 読む先と判断 |
|---|---|
| 本人のChatGPTへ接続・再接続する | [実行条件](runtime.md)で環境差と確認範囲を把握し、[connect-chatgpt](https://github.com/yusukefujiijp/ai-project/blob/main/skills/connect-chatgpt/SKILL.md)へ。接続操作は現在の依頼に従う |
| 同じ問題やHumanの違和感を繰り返したくない | [References](references/README.md)から関連するFeedback・lessonと後続訂正を読む |
| 成功した方法を別の環境や機会へ持ち込む | [成功事例の入口](references/success-cases/README.md)から、成果の意味・成立条件・未確認へ戻る |
| Codexの構成や案内を改善する | 本書の分担、[構造変更記録](../../control-center/changes/STR-025-codex-home-and-reference-pillars.md)、関連する[構成へのFeedback](references/feedback/README.md)を比較する |
| 新しい経験を残す・訂正する | [Referencesの更新先](references/README.md#戻す先を選ぶ)を選び、現在の保存範囲と共有save契約に従う |

すべてを毎回読む必要はない。指定された必須Sourceと読取条件を守り、今回の判断に効く記録の本文・出典・限界まで進む。読めなかったものを「記録なし」とせず、未確認の範囲を示す。

## 役割と原本の住所

| 原本 | 所有するもの |
|---|---|
| このREADME | Codex領域の目的、仕事から読む経路、原本の分担 |
| [runtime.md](runtime.md) | Codexで再開する際に確認する実行条件と、この初版で確認した範囲。接続固有の実績詳細は既存Skill READMEへ参照する |
| [references/](references/README.md) | Codex固有の協働経験、条件、読む場面、更新先 |
| [共有Skills](../../skills/README.md) | 再利用する方法。接続手順は既存のconnect-chatgptを使う |
| [共有References](../../references/README.md) | AIや領域を越える経験と共通契約 |
| [records](../../records/README.md)／[構造変更記録](../../control-center/changes/STR-025-codex-home-and-reference-pillars.md) | 日付から辿る活動／この初版の理由・変更・検証 |

共通指示は[AGENTS](../../AGENTS.md)、Ark全体の意味と入口は[Home](../../README.md)が所有する。本書の配置は、全Threadへの自動読込・Skill登録・操作権限の証明ではない。局所のAGENTSや製品設定は今回追加していない。

## 現在の到達点と継承する訂正

保存済みプロフィールから本人のChatGPTへの再接続は、既存記録で成立している。新規Threadの自然なSkill選択、別Runtimeでの同じプロフィール利用、長期安定性は未確認で、詳細と根拠は[runtime](runtime.md)から辿る。

Humanは複雑になったアーカイブ作業を停止し、ログイン成功の継承と再現性を最重要へ変更した。「復元しない」も保持する。過去の10件承認から再開しない。Gmailへの展開は将来のVisionとして残り、現在の操作承認ではない。

この初版の実行範囲は文書・経験・案内・変更記録の整備とGitHub保存確認。接続試験、ChatGPT操作、Skill登録、設定変更、別AIへの送信、予定・継続運用は含めていない。後続の仕事はその時点の依頼・Correction・STOPから判断する。

Humanが用意した改行のみのREADMEを基準点とし、入口・実行条件・経験の三本柱へ育てた。初期の配置と実記録、GitHub保存と受け手の理解・実利用効果を区別する。Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah。HumanのMeaning・Correction・STOPを保持し、AIとこの入口はKeliとして協働を支える。

EOF::ARK_CODEX_HOME::v001
