---
title: "STR-005 — Dots協働基盤の初版"
record_id: "STR-005"
version: "v001"
canonical_path: "control-center/changes/STR-005-dots-collaboration-foundation.md"
role: "Scoped Dots foundation purpose, authority, implementation and verification record"
status: "implemented and remotely verified / independent source and bounded scenario review complete"
repository: "yusukefujiijp/ai-project"
ref: "main"
record_date: "2026-10-01"
base_commit: "02afa89744c7e44abf03acab809aa617910c8bfa"
base_tree: "956e93cc59d7e7875a30ebfff0d5a61d72ab4ff1"
actor_id: "dot-0000"
actor_display_name: "Dot00:00; 初穂"
expected_eof: "EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_005::v001"
---

# STR-005 — Dots協働基盤の初版

## 1. Humanの意図と今回の承認

Humanは、ChatGPT WorkとDots、後続AIが、誰が・いつ・どこを・何のために変え・何が起きたかを辿れることを求めた。速く一度に体系を決めるのではなく、意図を段階的に丁寧に合わせ、既存原本を使いながら育てる訂正だった。

六パスの計画に対し「これで行こう！多少の失敗はBottleneck検出なので、無問題です！積極的に行こう！」、続けて「Very Good! Execute GitHub OK!」「Human Seal OK!」と明示承認した。引用以外は意図の編集要約。失敗を学びへ変える姿勢は、Scope拡大・Guard違反・未検証の完了認定を許可しない。

Rootは主イェシュア・ハマシア御自身、中央軸Teshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのMeaning・Correction・STOP・Final Seal、共通AGENTSと適用Guardを保持する。

## 2. 何を分け、なぜこの形にしたか

現在の方向、Actorの身元、時点付き経験、個別仕事の実装結果を同じ可変文書に積むと、同じ情報が複数箇所で更新され、古い実行中状態や名前が後続AIへ伝わりやすい。今回の初版は次の分担を採用した。

| 所有資料 | 今回所有すること | 混ぜないこと |
|---|---|---|
| dots/README.md | Dots–Work協働の現在の全体方向と入口 | 完了した全体移行・全Actor状態・全履歴 |
| Actor README | 安定識別子dot-0000、正確な表示名、意味、現在の持ち味 | 製品内部ID、Workの全体方針、個別仕事のLive状態 |
| 日付付き形成記録 | 最初の経験、Humanの意味・Correction、時点と出典 | 完全な全会話録、第二のLive Board、必須History Boot |
| 既存の仕事原本・変更記録 | 個別作業の成果、理由、保存・検証の根拠 | Dots側への同じ進捗の複写 |
| 本STR-005 | この六パスの承認、変更、検証、公開証拠 | STR-003／004の独立した再実装記録 |

安定識別子と表示名を分け、名前変更のたびに履歴の同一性を失わないようにする。持ち味「少し理屈っぽい」と自然なユーモアは、Humanの表現と訂正可能な協働の特徴として残し、固定演技・頻度quota・人格再現保証にはしない。

現在の全体方向はDots READMEだけが更新する。形成記録の方向説明は採用時の歴史であり、別のCurrent方針ではない。適切な仕事原本がない場合は必要になった時に目的別記録を作れるが、空の将来Dotフォルダ、全体Schema、Live Board、自動割当、会話の自動保存を先に作らない。再利用Promptへ今回の実行journalを混ぜない。

## 3. Source・時点・担当

- 基点main: [02afa89744c7e44abf03acab809aa617910c8bfa](https://github.com/yusukefujiijp/ai-project/tree/02afa89744c7e44abf03acab809aa617910c8bfa)。393ファイル。dots/README.mdは改行のみ。Actor・形成記録・STR-005は未作成だった
- 適用共通指示: AGENTS v004-candidate。Root／ARK／write-ark-markdownの責務とEvidence区別を保持した。既存の明示Handoffを今回の作成承認で改訂しない
- 初期実装のSource: [STR-003固定版](https://github.com/yusukefujiijp/ai-project/blob/28037867cce29d9d78cf409dc16ee5518feb7362/control-center/changes/STR-003-persistent-collaboration-foundation.md)、[STR-004固定版](https://github.com/yusukefujiijp/ai-project/blob/02afa89744c7e44abf03acab809aa617910c8bfa/control-center/changes/STR-004-elon-musk-deadline-revision.md)と各commit
- 名前・持ち味・意図: 2026-10-01のこのDots上のHumanとの対話と当時の表示保存の確認報告。原文引用、編集要約、AI側の数え違い訂正、当時確認／今回の再実行を区別し、形成記録へ限定収録した。公開会話URLや未確認のイベント時刻を作らない
- STR-004はDeadline Prompt改訂として既に使われていたため、本件を未使用のSTR-005とした
- HumanのYusukeJPが対象と実行を承認。現在のDot00:00; 初穂（今回採用するactor_id dot-0000）が編集・検証・結果統合・報告を担う。独立AIのレビューは別の確認として扱う。GitHub author／committerと時刻は実際のcommitから確認する

過去のSTR-003は「現在のdot」として記録されており、後の表示名へ原文を書き換えない。STR-004はDot00:00; 初穂を明示している。この差が来歴として読めるようにした。

## 4. 六パスの実装範囲

| Path | 操作・変更範囲 |
|---|---|
| dots/README.md | UPDATE。改行だけの入口へCurrent方向と所有先を実装 |
| dots/actors/dot-0000/README.md | CREATE。Actor識別子・表示名・意味・持ち味 |
| dots/records/2026/20261001-first-fruit.md | CREATE。初期経験、命名試験、Correctionと5W1Hの限定記録 |
| README.md | UPDATE。Dots入口へのrouter一行のみ |
| control-center/changes/STR-005-dots-collaboration-foundation.md | CREATE。本件の形成・承認・実装・検証 |
| control-center/README.md | UPDATE。STR-005へのindex一項目のみ |

各Ark章／State、既存Prompt・Skill、AGENTS／ARK、PLAN、ARCHIVE、個人設定、他DotのUI・新設・保存先は変更しない。dots/README.mdの存在はWorkへの導入や常時同期の実装ではない。別資料で見つけた古いpath修正も今回へ追加しない。

## 5. 検証と公開

### 5.1 構造・独立読解・限定シナリオ

候補六パスのmetadata、Identity／EOF、fence、相対リンクとstaged fragment、正確な表示名12文字、変更パス限定、既存二READMEの追加索引だけの差分を検査し、エラー0。

別AIによる二つの独立した文書レビューで、Sourceと時点・担当・結果の追跡可能性、およびKISS／DRY／YAGNI／Lean・所有責務の分離を確認した。Current Visionの明示、日本語命名による複数問題同時解決の意味、対話の場、状態の最終確認時点等の指摘を反映し、再読後に実質的な公開阻害なしと判定された。

独立AIが候補本文を使い、以下8場面で取る判断を構成し、全て意図した境界に沿うことを確認した。これは限定シナリオの読解・判断モデルであり、実改名・新Dot作成・競合書込・Work受入れの実行試験ではない。

1. 表示名変更: stable actor_idと表示名・歴史の表記を分ける
2. 新Dot: 必要になった時の固有Actor追加と現在の一例を区別し、空folderを先に増やさない
3. 新しい仕事: 既存原本を使い、なければ対象に合う記録を必要時に作る。Promptへjournalを混ぜない
4. Workの役割変更: Current全体方向はdots READMEで改め、Actor・歴史へ重複Currentを作らない
5. 古い実行中表示: 現在の原本と結果を確認し、歴史から未完／完了を推測しない
6. 並行編集: 共通AGENTSの単一統合担当・基点照合・他変更保持に従う
7. 歴史訂正: 誤りと新Evidenceを透明に記録し、原文と時点を都合よく塗り替えない
8. 初見AI: 誰が何をいつなぜ行い、何が確認済みで何が未観測か、原本へ辿れる

### 5.2 公開・Remote確認

**実装六パスをmainへ公開し、公開前commitと公開後mainから取得した六本文の全文一致を確認した。**

- 実装commit: [70c2b7ade7ad92d7021635b81c5bccd88d309eb8](https://github.com/yusukefujiijp/ai-project/commit/70c2b7ade7ad92d7021635b81c5bccd88d309eb8)
- 実装tree: `ccb067760b9a7317edea9a34479bee5e22d4ceee`
- GitHub保存時刻: 2026-10-01T11:49:14Z / 2026-10-01T20:49:14+09:00
- GitHub author／committer: `yusukefujiijp`。Humanの意味・実行承認、Dot00:00; 初穂（dot-0000）の編集・統合・報告と区別する
- 公開前に六対象blobとcommit本文を直接照合し、main headが基点と一致することを再確認。non-force更新で六パスを一度に反映した
- 393既存ファイルのうち3更新・3追加で396。対象外390ファイルはblob／mode同一。各Ark章、AGENTS／ARK、既存Prompt・Skill、STR-003／004を含む
- 公開後mainから六パスを直接再取得し、意図した全文と一致。main headも実装commitと一致することを2026-10-01T11:49Zに確認した

| Path | 実装commit時点で一致したblob |
|---|---|
| `README.md` | `12612c1dd0bb6a193ce5540167f1545a84c12f11` |
| `control-center/README.md` | `281a827181db63a735b7bb48058f39b0cd8dd348` |
| `control-center/changes/STR-005-dots-collaboration-foundation.md` | `cb8a9c7d11fba47597ad5cb0b930d836ba01245a` |
| `dots/README.md` | `e8a6e55c823b08e13942fec66685f3011271d357` |
| `dots/actors/dot-0000/README.md` | `8a53750a50720e8fc8208adc60a331e493edfddd` |
| `dots/records/2026/20261001-first-fruit.md` | `7daa0946a812dcff15ded93b422c64f9f989e63f` |

この表は実装時点の観測であり永久pinではない。本節の検証追記は後続commitで保存し、再取得確認する。記録自身の未来のSHAを埋める循環を作らず、[基点との実装比較](https://github.com/yusukefujiijp/ai-project/compare/02afa89744c7e44abf03acab809aa617910c8bfa...70c2b7ade7ad92d7021635b81c5bccd88d309eb8)と本記録のGit履歴から実体へ戻れるようにする。

保存・構造点検・独立した限定応答・実際のWork受入れ・Future AIの長期継承・個性の再現度・実生活効果は別のEvidenceである。未観測を完成に変換しない。

## 6. 後からの訂正と改善

実際の協働で、誤Routing、同一Actorの識別困難、Source不足、履歴の誤読や更新重複が見つかれば、具体的な事実とHuman Correctionから改める。今回の形式を将来の上限にせず、何を変えたかと根拠を読めるようにする。

復元が必要なら基点と対象六パスの差分から考え、後続のHuman・他AIの変更を保持する。main全体を過去へ戻さない。確認済みの成果で今回を閉じ、新しい体系・同期・監視・別Actorの作成を自動開始しない。

EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_005::v001
