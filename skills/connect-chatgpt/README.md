---
title: ChatGPT接続 — connect-chatgpt
version: v0.1.0
status: shared-source / saved-profile reuse verified / distribution verification in progress
created: 2026-10-31
updated: 2026-10-31
expected_eof: EOF::CONNECT_CHATGPT_README::v0.1.0
---

# ChatGPT接続

一度成功したログイン経路を、次のAIが短い依頼から使えるようにするSkill。HumanがiPhoneで認証・保存したTinyFishプロフィールを再利用し、本人のChatGPTへ到達したことを確かめる。通常の接続と、認証が必要な時の復帰を扱う。

手順の原本は[SKILL.md](SKILL.md)。初回の長い試行錯誤とHumanの重要な訂正は[成功事例](https://github.com/yusukefujiijp/ai-project/blob/main/references/success-cases/success-cases.jsonl)のID `16ce6cbe-9b5e-48b5-9e76-8c57e86ab1c4`にある。

## 使う

登録されたSkillを利用できる場合：

> $connect-chatgpt を使って、保存済みプロフィールから私のChatGPTに接続して。

自然な入口は「ChatGPTに接続して」。自然選択の成立は、各環境で実際に呼び出されるかを確認する。

登録機構を使えない環境でも渡せる入口：

> 次のSKILL.mdを全文読んで適用し、保存済みプロフィールから私のChatGPTに接続して。https://github.com/yusukefujiijp/ai-project/blob/main/skills/connect-chatgpt/SKILL.md

この依頼は接続確認までを対象とする。別の作業を依頼する時は、その対象・範囲を同じ依頼に添えられる。計画だけが必要な時は「まだ接続せず、方法を確認して」と指定する。

## 成立する条件

実行する環境から、同じTinyFish接続と対象プロフィールを利用できることが必要。Skillは手順を渡し、プロフィールは認証済みのブラウザ状態を保持する。GitHub保存だけで、全ThreadへのSkill登録やログイン状態の永続性は成立しない。

同じ個人SkillをWork／Codexで利用できる場合は共用し、製品名を付けた別原本を増やさない。各環境での取得・呼出し・接続の結果は別に確認する。共有原本を取り込む時は、Repository・path・commitまたはblobと本文の一致を記録する。

通常の再利用に1Password連携・パスワード変更・デバイスコード認証を追加する必要は、この成功経路では確認されていない。セッションが失効した場合の再認証や、サイトが要求する本人確認は残る。

## 確認済みの成果と残る範囲

- **初回成功：** [TinyFish実行 3db96189](https://agent.tinyfish.ai/runs/3db96189-5485-4ca3-8227-fcb3a0176cb6)で、本人アカウントとの一致を確認した。
- **2026-10-31の再接続：** [TinyFish実行 ec0cd818](https://agent.tinyfish.ai/runs/ec0cd818-9a96-4295-aa78-5fd92e343fc6)は、同じプロフィールから36秒・7ステップで完了。結果は`logged_in=true`、`expected_account_match=true`、`conversation_list_available=true`、`human_auth_required=false`、`mutation_performed=false`。Humanの再ログインなしで再利用が成立した。実行報告には、一時的なCloudflare表示の後にページが表示されたことも含まれる。
- **観測の限界：** 以上はTinyFishのブラウザ観測結果。36秒を今後の応答時間として保証しない。別Threadでの自然なSkill選択、別Runtimeからの同じプロフィール利用、長期間・定期実行での安定性、失効後の完全無人復帰は未確認。
- **登録・導入：** 共有原本の制作と実行環境への導入確認を進めている段階。実際の導入先・読み込み確認は、観測後にこの節を更新する。

## この入口を作った理由

YusukeJPは、複雑になったアーカイブ作業を停止し、ログイン成功と再現性を最重要へ変更した。GitHubへの成果保存後、短い依頼から接続へ戻れるSkillと、その導入・限定的な再接続確認を承認した。現在もアーカイブ停止・復元しないという訂正を保持する。Gmailへの展開は将来のVisionである。

`load`は協働文脈の復元、`resolve-github-runtime`はGitHub操作経路の解決を担当する。このSkillは、ChatGPTの保存プロフィール選択・本人確認・再認証時の復帰を担当する。汎用的な判断規則や長い形成史をSkill本文へ重ねない。

標準のskill-creator／skill-installerと、共有Skills Hubのaudit-agent-instructionsによる設計基準を適用する。Skill原本、配布先への保存、会話での取得、実際の動作、Humanの負担軽減を別々の証拠として扱う。

EOF::CONNECT_CHATGPT_README::v0.1.0
