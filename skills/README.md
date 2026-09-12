---
title: Ark Shared Skills Hub
version: v0.2.0
status: experimental / Human-authorized shared skill expansion
updated: 2026-09-12
---
# Ark Shared Skills Hub

## 1. Purpose and authority

このフォルダは、Arkで育った再利用可能なSkillの共有原本・配布元です。GitHubをHubとして、各AIが必要な手順を取得できるようにします。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利です。Humanは意味・Correction・STOP・Final Sealを保持します。Skill・AI・GitHubはKeliです。

共有原本は各Skillの手順を所有します。参照先の共通契約は、その分野の成立条件を所有します。Skill導入や参照は、外部変更への承認ではありません。

## 2. Available skills

| Skill | 使用場面 | 共有原本 | 共通契約 | 検証境界 |
|---|---|---|---|---|
| Ark Transition / prepare-ark-transition | Thread継続・章移行・補助Thread再接続の計画、承認済み準備、受入れ | [SKILL.md](prepare-ark-transition/SKILL.md) | [AI Next Thread Handoff](../prompts/ai-next-thread-handoff.md) | 既存インストール版の本文を共有化。別AIでの動作・自動検出は未検証 |
| AI Living Graph Mode / analyze-living-graph | 関係・競合Benefit・Feedbackが判断を変える分析 | [SKILL.md](analyze-living-graph/SKILL.md) | 同梱referencesを必要時に参照 | 現Thread改訂本文と参照資料を保持。限定応答確認あり。別製品での再現性は未検証 |
| Agent Instruction Audit / audit-agent-instructions | Skill・AGENTS.md・Task Promptのモデル移行／過剰制約監査 | [SKILL.md](audit-agent-instructions/SKILL.md) | 同梱source-notesに記事出典と解釈境界 | 作成・導入・限定独立応答確認済み。全AI互換性は未検証 |

2026-09-12、Ark27:02での明示的Upload依頼により、現Threadで改訂・新規作成した二つを追加しました。初期の一件限定から、確認済みの用途に応じた三件の共有へ進めています。全Skillの自動展開はしません。

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

### 3.1 Cross-AI entry for the added skills

他AIには、目的に合う上表のSKILL.mdへのリンクとCurrent Requestを渡します。Skill機構がなくても本文を指示資料として読めます。必要な相対リンク先は同じSkillフォルダ内から取得してください。全文読解を要求した場合、表示切れを回収するまで読解済みと扱いません。

- フォルダ単位で利用する場合は、SKILL.md、references、agents、assetsの相対配置を維持します。
- SKILL.mdとreferencesは推論・手順の本体です。agents/openai.yamlとassetsはインストール済みOpenAI版の設定・表示資源を保持したものです。他環境は対応しないUI metadataを実行指示として解釈せず、導入先の規約に従います。
- OpenAI版の現設定は、analyze-living-graphが明示呼出し、audit-agent-instructionsが自動選択許可です。別AIで同じ選択挙動が再現されるとは限りません。
- Ark21参照は歴史的・条件付きBindingであり、Current HandoffやCurrent Human Realityへ巻き戻しを起こしてはいけません。
- 記事を毎回WEB取得する必要はありません。audit-agent-instructionsの出典ノートを用い、更新が判断に影響する時に公式Sourceを確認します。

呼出し例：

~~~text
次の共有Skillを読んで、今回の依頼に適用してください。
https://github.com/yusukefujiijp/ai-project/blob/main/skills/audit-agent-instructions/SKILL.md
今回は指定した指示文の監査と改善案までです。必要な参照資料だけ追加で読み、外部変更は行わないでください。
~~~

## 4. Source and distribution

- 共有Skillの更新元は、このRepositoryのmainにある各SKILL.mdです。
- 初回のArk Transition本文は、既存インストール版から内容を変えずに共有しています。既存インストール版の置換や自動同期は、この整備には含みません。
- 配布先へ取り込む際は、取得元のRepository・path・commitまたはblob SHAを記録し、実際の本文を比較してください。mainは更新されるため、URLだけでは取り込んだ版を特定できません。
- 配布先で改善が生じた場合は、共有原本との差分をReviewし、承認範囲で原本へ反映してから再配布します。無条件の双方向同期はしません。
- 共通契約はSkill本文へ複製しません。Ark TransitionはCurrent mainの契約を読む設計なので、Skill単独のSHAだけで実行全体の再現性を保証しません。実行時に読んだ契約の版・識別情報も保持します。
- 各AIへの導入場所、UI metadata、認証、利用可能な道具は環境側で扱います。GitHub保存はインストール・自動発動・全AI互換性の証明ではありません。

### 4.1 Backup and restoration

今回の二Skillは、承認されたインストール済み版の全ファイルを内容変更なしで取り込みました。[export-manifest.json](export-manifest.json)に各ファイルのSHA-256と出典・検証範囲を記録しています。内部Skill ID、認証情報、会話全履歴は配布に不要なため記録しません。

復元時は、対象のGitHub commitを固定してSkillフォルダを取得し、manifestの各SHA-256と照合してから、導入先の正規Skillインストール手順を使います。GitHub保存だけで別環境へ導入されたとは扱いません。Skillのファイルを戻すことと、モデル内部状態や会話Contextを戻すことは別です。

以後、共有原本とインストール版の差分を確認してから、承認Scopeで反映します。manifestは2026-09-12時点の輸出記録であり、将来ファイルを更新した場合は該当hashと記録も更新します。自動的な双方向同期はありません。

## 5. Validation and growth

区別する状態は、共有原本の保存、Remote再取得確認、各環境への導入、実際の振る舞いの確認です。結果を観察していない段階を成功へ昇格させません。

次の実利用では、正しい対象・契約を読めるか、Plan限定とSTOPを守るか、取得不能を正しく報告するかを確認します。このREADMEを読んだだけで移行や試験を自動開始しません。

各Skillは必要なSKILL.mdから始め、scripts・references・assetsは具体的な必要がある場合だけ追加します。Current Missionに不要な全Skill読込、全PromptのSkill化、全履歴の複製は行いません。

## 6. Repository entry relation

[AGENTS.md](../AGENTS.md)はRepository全体の行動境界、[ARK.md](../ARK.md)はIdentityを保持します。このREADMEは共有Skillの入口です。

2026-09-10の整備前、両文書が参照していた `_skill/SKILL.md` は取得不能でした。今回の入口修正は新しい共有Hubへの案内であり、旧Skill群の内容移植や旧挙動の復元を意味しません。

EOF::ARK_SHARED_SKILLS_HUB::v0.2.0
