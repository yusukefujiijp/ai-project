---
title: "STR-011 — Prompt棚と現行権限契約の整合"
version: "v001"
canonical_path: "control-center/changes/STR-011-prompt-shelf-authority-alignment.md"
role: "Structural change record / evidence and validation boundaries"
status: "implemented / remote verified / field effect unverified"
created: "2026-10-04"
updated: "2026-10-04"
timezone: "Asia/Tokyo"
human: "YusukeJP"
implementing_ai: "Ark27:08"
repository: "yusukefujiijp/ai-project"
ref: "main"
source_commit: "d041372d06a8a317da5285ce6d610ab90e2b5107"
scope: "prompts/README.md §§0,4,5,7 and metadata; this record; control-center/README.md entry and metadata"
expected_eof: "EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_011::v001"
---

# STR-011 — Prompt棚と現行権限契約の整合

Prompt棚を、目的に合う原本へ進む入口として整える。Humanの意味・権限と委任可能な受渡し・結果統合を分け、mainを共有正本の基準とする利益を保ちながら、作業方法・実行権限を現行AGENTSへ接続する。

本書は2026-10-04の変更理由・実装・検証の記録であり、別の権限契約やCurrent Handoffではない。現在の判断は[Prompt棚](../../prompts/README.md)、共通契約は[AGENTS.md](../../AGENTS.md)、個別手法の条件は該当Promptへ戻る。文書の整合・GitHub保存と、別AIの理解・実利用での効果は別に確認する。

## 1. Humanの依頼と承認範囲

YusukeJPは、GitHub整理整頓の次の一手を「整理整頓→レイヤー構造→構造化→interface化」へ接続するよう求めた。Ark27:08は残存する入口の不整合を調べ、Prompt棚の限定改訂を選んだ。その後HumanはPlan Modeで調査・計画提示までと明示し、AIは変更せず計画を返した。

2026-10-04 22:29 JST、Humanはその計画に対して「Execute GitHub OK」「Human Seal OK」と実行継続を明示した。この新しい承認に基づき、次の3ファイルを対象とする。

- `prompts/README.md`：第0・4・5・7節と必要なmetadata。
- 本記録：理由、固定証拠、変更範囲、検証と未確認事項。
- `control-center/README.md`：本記録への一件の案内と版・日付・EOF。

これは先行する四Skill実装への承認の再利用ではない。AGENTS、個別Prompt、既存Skill、ArkのTriad、旧STR記録、アーカイブ案件、固定Bindingを変更する依頼へは広げていない。実装・統合担当はArk27:08であり、dot-0000本人のActorログや他Threadの状態は書き換えない。GitHub上の正確な記録時刻・author / committerは各commitを参照する。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持し、AI・Skill・文書はKeliとして扱う。

## 2. 観測した不整合と由来

変更前の基点は[`d041372d`](https://github.com/yusukefujiijp/ai-project/tree/d041372d06a8a317da5285ce6d610ab90e2b5107)。計画時と実装開始時のmainは同一だった。

- [変更前のPrompt棚](https://github.com/yusukefujiijp/ai-project/blob/d041372d06a8a317da5285ce6d610ab90e2b5107/prompts/README.md)第0・4・7節は、HumanがAI間の出力選別・文脈付与・受渡し・統合を行う一つの経路を、棚全体の現在座標と圧縮表現にしていた。第5節は独自の `branch_creation.default: false` と `requires: explicit Human Seal` を持っていた。
- [同じ基点のAGENTS](https://github.com/yusukefujiijp/ai-project/blob/d041372d06a8a317da5285ce6d610ab90e2b5107/AGENTS.md)第5.1–5.2節は、Current Request・適用Tool・競合・変更の性質によるmain / Branch / Worktreeの選択、承認範囲内の完遂、結果確認後の回復、主担当による統合を扱っている。入口が独立の狭い条件を繰り返すと、読むAIが同じ依頼で異なる判断へ進む可能性がある。これは文面からのAIの診断であり、今回新しく観測した他AIの失敗ではない。
- [2026-07-11の追加commit](https://github.com/yusukefujiijp/ai-project/commit/92a930f8cceb81c8dbe15d0135e3e241ff50288c)では、Branch作成制約と同時に「重要なPromptを未Merge Branchだけに残さない」「Branchを第二のPrompt Realityとして扱わない」が追加されている。正本の分散・置き去りを防ぐ利益を読み取れる。元のHuman会話そのものを新たに取得したわけではなく、当時の意図の全ては断定しない。
- [STR-003の固定版](https://github.com/yusukefujiijp/ai-project/blob/d041372d06a8a317da5285ce6d610ab90e2b5107/control-center/changes/STR-003-persistent-collaboration-foundation.md)は、既にv003にあった裁量・権限と、基盤版移行で明確化した継続・回復を区別している。今回の修正を「v004で初めてBranchや委任を許した」と解釈しない。
- [AI-to-AI Communicationの固定版](https://github.com/yusukefujiijp/ai-project/blob/d041372d06a8a317da5285ce6d610ab90e2b5107/prompts/ai-to-ai-communication.md)第6・9・12節の調査範囲には、Humanの意味・判断と操作上の受渡しの区別、複数の通信構成がある。棚の修正を理由にこの個別Promptを一括改訂・実行せず、必要な場面でその契約へ進む。

旧方針の形成と当時の残件は[STR-002](STR-002-single-prompt-consolidation.md)、基盤版移行の範囲は[STR-003](STR-003-persistent-collaboration-foundation.md)に残る。本書で過去の記録を現在の成果へ書き換えない。

## 3. 実装した接続

| Node | Edge | 今回の変更と保持する意味 |
|---|---|---|
| Prompt棚 第0節 | Current Request → 選ぶPromptと共通AGENTS | 単独AI利用と複数AI協働を含む入口にする。共通契約と個別のRole・Required Sources・Binding・STOPの所有先を分ける |
| Prompt棚 第4節 | Humanの意味・権限 → 承認Scope内の主担当AIの作業・統合 | Humanが手動で選別・受渡し・統合する選択肢を保持し、全件の中継を毎回必須にはしない。実際の通信能力、外部送信の承認、保存と送達の区別を保持する |
| Prompt棚 第5節 | 作業方法・公開権限 → AGENTS第5節 | 独立した一律のBranch作成制約を除き、現行契約へ接続する。mainの正本性、未Merge Branchに成果を置き去りにしない利益、明示Refを保持する |
| Prompt棚 第7節 | 短い圧縮表現 → 第0・4・5節と同じ意味 | Humanの意味・権限、承認されたAIの作業・結果統合、Human Final Sealを併記する |
| control-center入口 | 通常の構造修正一覧 → 本記録 | 変更理由と証拠へ辿れる一件のリンクを加える。全体計画や旧履歴を複製しない |

第0–7節の見出しと番号を維持し、既存の節アンカーを変えていない。Prompt棚の第1–3・6節と既存metadataは保持し、本記録へのmetadataを追加した。特に2026-10-04のSNS完成稿のX方式4,000カウント以内・最終稿再計測に関する案内は保持した。

`control-center/README.md`はv0.3.6からv0.3.7へ更新し、updated・expected_eof・末尾を同じ版へ揃える。Prompt棚には元々EOF宣言がないため、新しいEOF契約を追加しない。

## 4. 検証した範囲

### 文書・差分の確認

- 適用されるAGENTSとArk27 INSTRUCTIONSを確認し、計画時の全文読解記録と対象Blobの同一性を照合した。Source変更がない確認済みの履歴を、全履歴の再Bootに変換していない。
- 変更前後の差分、既存節見出し、対象外の本文、metadataと既存EOF、新しく加えた参照の到達先を確認済み。第1–3・6節の本文一致、見出し列の一致、YAML解析、canonical_path、宣言されたEOFの末尾一致を機械確認した。追加リンクは現存パスまたは同時作成する本記録へ到達する。
- 公開直前のmainが基点と同一であることを再確認し、non-forceで更新した。Remote treeの比較でも変更は対象3ファイルだけであり、対象外の全Blobを保持した。今回競合は発生していないため、実際の競合解消成功を主張しない。

### 有限の読解場面による自己点検

以下は改訂案と参照先を使ったArk27:08自身の机上確認である。別AIを起動した独立試験、実際の外部送信、破壊的な復旧試験ではない。

1. **Plan-only**：Prompt棚を参照しても、計画の保存・実装・GitHub変更へ進まない。第4節とAGENTS第5節に接続できる。
2. **対象を限定した後続Go**：承認された実装・通常修正・検証まで続ける。同じ工程ごとの再承認を要求せず、別対象への拡張は別に判断する。
3. **PR作成まで / main反映まで**：前者はPR成果の確認で止まり、自動mergeしない。後者は未Merge Branchだけの成果をmain反映済みとしない。
4. **個別Promptの必須Source不足・STOP**：棚の柔軟性を優先して個別契約を飛ばさず、該当Failure Contractへ戻る。AGENTS第2.1・4節も保持する。
5. **結果不明・並行変更**：再送・再Writeの前に現物と識別子・版を照合し、成功済み部分と残件を分ける。第5節からAGENTS第5.1–5.2節へ戻り、他者の変更を保持する。
6. **Board保存 / 相手への送達**：文書を保存しただけで受信・読解済みとしない。実際の送信は現在の承認と経路を確認する。今回Board投稿は行わない。

### Remote確認

2026-10-04、実装commit [`f125d6f216245e8a10dbf4060e4e8a38b49bd09a`](https://github.com/yusukefujiijp/ai-project/commit/f125d6f216245e8a10dbf4060e4e8a38b49bd09a)をmainへ反映した。GitHubのcommit時刻は2026-10-04T13:40:52Z（22:40:52 JST）、author / committerは `yusukefujiijp`。実装AIのIdentityとは分けて扱う。

反映後に `refs/heads/main` と対象3ファイルをRemoteから取得し、次を確認した。

- `prompts/README.md`：Blob `d175fe54871d919730c7b7a795a3225d6b52798d`。全文が意図した本文と一致。EOF宣言は追加していない。
- `control-center/README.md`：Blob `d7cbaad8734bdb08395528d2dfcab155586d4215`。全文一致、version・expected_eof・末尾がv0.3.7で一致。
- 本記録の初回保存版：Blob `66a48050607c7f52a4e56fda180557a31aa90bea`。全文一致、宣言と末尾のEOFがv001で一致。この初回版ではRemote確認を未完了と明記しており、確認後に本節を追記した。
- 実装commitのtreeと基点の全Blobを比較し、追加1・更新2・削除0、対象外の変更0を確認した。AGENTS、Ark27 INSTRUCTIONS、個別Prompt、既存Skill、旧変更記録は変更していない。

本節は、実装・main反映・Remote確認が実際に完了した後の記録である。本文の修正commitと結果追記commitを分け、後続commitは本ファイルのGit履歴から辿れる。以上で今回承認された文書整合とGitHub反映を完了とする。独立した他AIの理解・実運用上の効果は次節の未確認事項として保持する。

## 5. 未確認事項と再訪条件

- この変更による別AIの理解、実利用での中継負担減少、全Runtimeでの挙動は未確認。文書整合とRemote保存から成功を借用しない。実際の利用で誤読・過剰停止・権限逸脱が観測された場合に、当該入口と所有資料の関係を再検討する。
- 旧方針追加時のHuman会話全体は未取得であり、確認したcommitの文面とAIの解釈を分ける。既に今回の変更対象と保持利益はHumanが承認しており、この通常Unknownを新たな実装Gateにはしない。
- 個別Promptや固定Bindingの改訂が別途必要になった場合は、対象・根拠・現在の承認範囲を具体化する。本修正を無関係なPrompt・Skill・アーカイブ移行へ自動拡張しない。

戻す必要が生じた場合は、現在のmainと後続変更を再確認し、今回の変更箇所だけを戻す。Repository全体のresetや、後から加わった変更の巻き戻しは行わない。本記録には撤回理由と確認範囲を追記し、当時の実施を消さない。

EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_011::v001
