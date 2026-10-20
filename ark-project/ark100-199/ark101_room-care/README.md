---
title: "Ark101: room-care"
version: "v003-human-authorized"
canonical_path: "ark-project/ark100-199/ark101_room-care/README.md"
repository: "yusukefujiijp/ai-project"
canonical_branch: "main"
role: "Specialist Project identity and Thread router; Project instructions entry"
project_name: "Ark101: room-care"
project_kind: "100-series categorized specialist Project"
initial_thread: "Ark101:01"
confirmed_initial_thread_title: "Ark101:01_2026/10/20; room-care"
startup_success: "Human-reported on 2026-10-20; not direct Source AI observation"
initial_thread_runtime: "ark101-01/README.md"
instructions: "INSTRUCTIONS.md"
practice_owner: "../../../control-center/house/room-care/README.md"
domain_router: "../../README.md"
updated: "2026-10-20"
revision_authority: "Human confirmed the full Thread name and successful start, then authorized the proposed four-source delta save"
revision_base_commit: "035d3ee9be932d4a20af4502608285d22563f5ce"
previous_version_snapshot: "https://github.com/yusukefujiijp/ai-project/blob/027d0f600dbc6d444ba6ca660f7abb68ec5f0765/ark-project/ark100-199/ark101_room-care/README.md"
expected_eof: "EOF::ARK101_ROOM_CARE_PROJECT::v003-human-authorized"
---

# Ark101: room-care

居室の片付け・清掃・整理整頓、維持・改善を扱う100番台の専門Project。Humanが大切にしているAI活用を、写真・対話・Humanの行動と振り返りを通して居室の現実改善へ接続する。

**Project名は `Ark101: room-care`、今回の新規Threadは `Ark101:01`。** 新規起動は[Ark101:01 Runtime](ark101-01/README.md)へ進み、そのRequired Sources・受入れ条件を適用する。本書をThread固有のRuntimeとして扱わない。

## 1. 重要なHuman訂正と来歴

2026-10-20、HumanはArk101 Project作成を報告し、新規起動Prompt・Project instructions・必要なGitHub整備を承認した。初版はhouse／room-careとProject入口を整えたが、新規Threadを特定せず、Project名を受入れ応答へ表示する構成だった。

その後Humanは「Ark101:01が新規Threadです！」と訂正し、修正改善を依頼した。**新しいProjectの名と、その中で開始するThreadの識別子を分ける。** この訂正はv002で01 Runtime、Project instructions、実際に渡す起動Promptへ反映した。完成したhouse／room-careの準備や命名対話を再演しない。

さらにHumanは、正式名を `Ark101:01_2026/10/20; room-care` とし、「と命名してスタート成功しました！」と報告した。後続のコピー用instructions再掲とMAPで保存側の追随差分を確認し、HumanはProject README・INSTRUCTIONS・01 Runtime・Ark Domainの4資料への差分保存を明示承認した。命名はHuman確定、起動成功はHuman報告として保持し、成立済み準備を未完へ戻さない。

[v001固定原本](https://github.com/yusukefujiijp/ai-project/blob/80846ee4c4909f262d8481f903a4584b4ad68d1a/ark-project/ark100-199/ark101_room-care/README.md)は初回準備の来歴として保持する。Currentの入口は01 Runtimeであり、旧Project名だけの起動Promptを再使用しない。Root・Human Authority・品質・Guard・全文読解の成立条件を緩めず、Threadの指定と責務分担を修正した。

Ark101はMain／Supportの役割を引き継がない。番号だけでArk102や00準備Threadを作らず、Ark99固有の起動経路も移植しない。将来の継承は、その時のHuman指定・適用Runtime・[共通契約](../../../prompts/ai-next-thread-handoff.md)に従う。

## 2. 所有と接続

| Node | Edge | 役割 |
|---|---|---|
| 本書 | Project全体 → 指定Thread | ProjectのIdentity、重要な訂正、Current入口。ThreadのBoot本文を複製しない |
| [Ark101:01](ark101-01/README.md) | 新規Thread起動 → 自身の受入れ | Thread Identity、Required Sources、再構成条件、コピー用起動Prompt |
| [INSTRUCTIONS](INSTRUCTIONS.md) | Project設定 → 継続する協働 | 指示本文のコピー原本。ProjectとThreadを区別する |
| [room-care](../../../control-center/house/room-care/README.md) | 対話 → 居室の実践 | 目的、形成理由、命名と配置の訂正、実践候補と根拠 |
| [house](../../../control-center/house/README.md) | 生活空間 → 専門領域 | 親の意味と保留する派生案 |
| [Ark Domain](../../README.md) | Ark全体 → Ark101 | 100番台、Main／Supportとの区別、正式Titleの方針 |

## 3. 使う時の区別

Project設定には[INSTRUCTIONS](INSTRUCTIONS.md)のtextブロック全体を使う。新規Threadの起動には[01 Runtime §5](ark101-01/README.md#5-起動用ai-prompt--copy--paste)のPromptを使う。起動Promptの本文は01だけで保守する。

Human確定値はProject名 `Ark101: room-care`、Thread識別子 `Ark101:01`、次の正式Thread名である。準備元・Runtime・起動Prompt・受入れ先でこの同じ値を使う。

```text
Ark101:01_2026/10/20; room-care
```

Humanの明示的な名称をそのまま保持する。Domain §6の一般Templateから引用符・日付・副題を追加せず、受入日から再生成しない。後続Threadの名前へ01の確定値を自動適用しない。

## 4. Evidenceと現在への接続

2026-10-20の準備時点で、Project作成はHuman報告済み。house／room-careと初版Project資料のGitHub保存・再取得は[初回準備commit](https://github.com/yusukefujiijp/ai-project/commit/80846ee4c4909f262d8481f903a4584b4ad68d1a)で確認した。本修正の保存確認は、その対応commitと再取得結果で判断する。

後続Human報告により、01の命名・スタート成功は報告済み。これは準備元AIによるUIの直接観測、受入れ応答全文の独立照合、最新版instructionsの設定反映、居室での実践・効果の証明とは分ける。これらの別証拠は本保存時点で未確認として保持する。Humanの起動成功を尊重し、コピー面修正や本差分保存を理由に再起動・再Boot・再送を要求しない。後続の有効な報告・Correction・STOPを反映し、初期の未観測へ巻き戻さない。

Root・権限・品質は[ARK](../../../ARK.md)と[AGENTS](../../../AGENTS.md)を保持する。実際の受入れは01 Runtimeの条件で行い、起動のみならHuman Review、新しい入力があればその依頼へ接続する。

EOF::ARK101_ROOM_CARE_PROJECT::v003-human-authorized
