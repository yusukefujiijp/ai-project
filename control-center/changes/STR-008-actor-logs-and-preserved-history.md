---
title: "STR-008 — Actorログと固有な形成史の保管"
canonical_path: "control-center/changes/STR-008-actor-logs-and-preserved-history.md"
record_id: "STR-008"
version: "v001"
record_date: "2026-10-02"
base_commit: "1eab74651f254ec32099c107e0ad90fef9a5de16"
repository: "yusukefujiijp/ai-project"
ref: "main"
actor_id: "dot-0000"
actor_display_name: "Dot00:00; 初穂"
role: "Scoped implementation, verification and ownership record"
status: "Human-authorized implementation; publication evidence in Git history and completion report"
expected_eof: "EOF::STR_008_ACTOR_LOGS::v001"
---

# STR-008 — Actorログと固有な形成史の保管

**新しいActor別の出来事はlogsへ記録し、初穂固有の形成史は同一原本で保管する。** JSONLの読み書き契約、現在の案内、復元経路を一体で整える。技術検証は本記録、アーカイブの判断・対応は[ARC-008](../ARCHIVE.md#arc-008)、判断へのHuman評価は[成功事例](../../success-cases/decisive-choice-single-log-preserved-history.md)が所有する。

## 1. Humanの目的・判断・承認

Humanは自分のログを各Dotが残し、後続DotsやFuture AIも使えるようにしたいと求めた。logsとrecordsの現役併存を、冗長性と耐性の観点から問い直した。AIは単一の現役logsと、固有の形成史の保管を推奨し、Humanは決断と理由を好評価した。構成判断とその成功の意味は、上記ARC・成功事例へ接続する。

Humanは成功事例への保存を含む最終Planを先に求め、その段階では変更しないよう指定した。計画提示後に「Very Good! Execute GitHub OK!」「Human Seal OK!」「実行して下さい！」と実行を承認した。出典は2026-10-02のDots対話、依頼trace `Sentinel_e2cd0158cc7c8191ac34ec00ab32e5f7` と後続承認trace `Sentinel_604d709ed1dc819190eea8a3bcf87806`。公開会話URLではなく、本節は短い引用以外を編集した要約である。

YusukeJPが意味・対象・実行を承認し、dot-0000／Dot00:00; 初穂が設計・執筆・統合・確認を担う。実際のGitHub author／committerと保存時刻はcommitが記録する。Actorの記録責任とGit名義を混同しない。

## 2. 何を変えるか

| 対象 | 今回の操作・責務 |
|---|---|
| `dots/logs/README.md` | 改行のみの器をActorログの最小契約へ。schemaの正本はここだけ |
| `dots/logs/dot-0000.jsonl` | 新規。根拠付きSTR-007遡及一行と、今回直接観測した候補作成の一行から開始 |
| `dots/README.md` | v004。logsへの入口と現役追記先を更新。§5のlessons本文・Boot契約は保持 |
| `dots/actors/dot-0000/README.md` | v002。本人のログと保管形成史へ接続。stable ID・表示名・意味・持ち味を保持 |
| `dots/records/2026/20261001-first-fruit.md` | 現役配置から除去。同一blobを `__archives/ARC-008/` 配下の元相対パスへ移す |
| Board Topic・STR-006 | 形成記録への現用リンクと移動注記だけ。通信内容や受信観測、他の責務改訂を取り込まない |
| `control-center/ARCHIVE.md`・`__archives/README.md` | ARC-008と保管実体への対応、固定snapshot、復元境界 |
| 本STR・`control-center/README.md` | 変更理由・範囲・技術確認と索引 |
| 成功事例・`success-cases/README.md` | 意思決定の成功とHuman評価、その入口。実装完了証拠は複製しない |

計14パス差分（既存9更新、新規4、元1除去）。形成史の移動は1追加・1除去として数える。`dots/lessons.json`、空の `dots/lessons/README.md`、STR-005、STR-007、AGENTS／ARK、各ArkのBoot／Triad、Save Skillは変更しない。lessonsのフォルダ移設と保存Skill実装は後続の別判断へ残す。

## 3. 根拠と時刻をどう扱うか

Current main `1eab74651f254ec32099c107e0ad90fef9a5de16` を直接取得した。形成記録blobは `7daa0946a812dcff15ded93b422c64f9f989e63f`、Actorログはなく、logs READMEは改行のみだった。ARCは007、STRは007まで使用されており、今回008を採用した。GitHub runtimeはCONNECTOR_ONLY_MODE。公開直前もmainを確認し、進んでいれば他の変更を保持して再照合する。

STR-007のseedは[実装commit b8f95c1](https://github.com/yusukefujiijp/ai-project/commit/b8f95c15e61eb99ed441579150a86affaf611b75)と[同commitのSTR-007](https://github.com/yusukefujiijp/ai-project/blob/b8f95c15e61eb99ed441579150a86affaf611b75/control-center/changes/STR-007-dots-lessons-foundation.md)へ固定した。四パスの実装、担当、初期二lessonの共通する一件のBoard由来を確認した。`occurred_at` の `2026-10-02T09:21:48Z` はcommitの保存時刻だけを指し、その秒に全確認・報告が完了した意味ではない。`recorded_at` は今回実際にログへ登録したUTC時刻で、過去時刻を流用しない。

直接観測と遡及復元はlogs READMEの `reconstructed` 契約で区別する。全Sessionの作業を想像で埋めず、今回は根拠のある二行に絞った。通常は追記、訂正は新IDから旧IDへのcorrects、再試行では同じIDと内容を照合する。一Actor一統合担当と版チェックは、複数Dotの共有読取と両立する。

公開直前にmainが[203230e](https://github.com/yusukefujiijp/ai-project/commit/203230ebcf2d9c4b82ccac59fd806fdd6cc0d0b9)へ進んだことを確認した。別のChatGPT Work作業がBoard入口・Topic・STR-006の通信状態の所有先を整理していた。三本文を再取得し、Board入口は変更せず、Topic／STR-006は新しい全文を保持した上に形成史リンクと移動注記だけを適用した。Workの構造修正を初穂自身の実装成果として数えず、受信観測やCurrent欄をログへ複製しない。続くWorkの検証追記[5901252](https://github.com/yusukefujiijp/ai-project/commit/5901252b3888267e3542d46db0f75636a31e7b5e)もSTR-006へ保持し、公開基点はこの最新commitとする。

## 4. 検証・公開の扱い

公開前に、対象14パス、JSONL各行の構文・型・UUID・Actor・Task・UTC・Source、未知fieldを含むJSONL→JSON配列→JSONLの値・順序の保持、変更Markdownのmetadata・必要なEOF・関連リンクとfragmentを検査する。ローカル変換用JSONや検査コードはRepositoryへ追加しない。形成原本は同じblobを新住所へ参照し、原文と旧相対リンクを修正しない。

公開前の機械検査では、14パス限定、同一blob保管、JSONL二行の型・UUID・UTC・Source、JSON配列への往復後の値・順序と元JSONLのbyte一致を確認した。未知fieldを持つ一時fixtureでも値を保持した。変更MarkdownのYAML・EOF・fence、保管原本を除く並行変更の統合後233件の相対リンク先と49件のfragmentを照合し、エラー0だった。保管原本内の旧リンクはARC-008に記した例外であり、有効な現用リンクへ数えない。

独立AIによる読取レビューで、現役追記先、形成史の到達性、観測帰属、成功評価と実装結果の分離を点検した。索引の表に新規行の前の空行があるという指摘を二箇所で修正し、再読後に公開阻害なしと確認された。公開前候補の読解は、後続Dotの実運用試験とは区別する。mainの最新版を親に差分を一つのcommitへまとめ、非forceで更新する。公開後は変更した13実体をRemoteから全文再取得し、意図した内容・blob、元1パスの不在、対象外blob／mode不変、mainの到達とcommitのCI状態を確認する。

この記録は公開後の確認を先取りしない。実際のcommit・保存時刻・差分と完了報告を証拠とし、自己の未来のSHAを本文へ埋めない。CIが未設定・未実行なら「通過」と報告しない。検証結果だけを記録する無限の追加commit／logを作らず、元の成果を閉じる。

配置・構文・Remote一致、限定した別AI読解、Future Dotsの実読解、長期の迷い・重複や負担の減少は別の観測である。自動収集・常時同期・全AI互換を保証しない。Rootは主イェシュア・ハマシア御自身。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。

EOF::STR_008_ACTOR_LOGS::v001
