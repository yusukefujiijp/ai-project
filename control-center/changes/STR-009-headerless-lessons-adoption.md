---
title: "STR-009 — 管理行なしlesson JSONLの実運用採用"
canonical_path: "control-center/changes/STR-009-headerless-lessons-adoption.md"
version: "v001"
record_date: "2026-10-03"
record_date_utc: "2026-10-02"
status: "human-authorized production format migration"
repository: "yusukefujiijp/ai-project"
branch: "main"
base_commit: "02e9779fc628dbfe7ee9ed08275c6b839407ef0e"
implementation_actor: "dot-0000 / Dot00:00; 初穂"
scope: "Ten-path shared lesson format and contract migration; no new lesson, Skill, ingestion, or outreach"
expected_eof: "EOF::STR_009_HEADERLESS_LESSONS_ADOPTION::v001"
---

# STR-009 — 全行がlessonである蓄積へ

Dotsの共有する現行lessonを、管理行なしJSONLへ採用・移設する。既存の二つの学びの意味・根拠・限界を変えず、全行を同じlessonとして扱い、新規採番の共有counterを外すことが目的である。新しい学びを増やす作業、Actor別台帳化、Save Skill実装ではない。

## 1. 形成順序とHumanの採用判断

最初の[STR-007](STR-007-dots-lessons-foundation.md)は単一JSON、schema 1、next_idを用いた。次の[凍結比較](../../dots/lessons/experiments/json-vs-jsonl/README.md)では、元JSONとheader付きJSONLの全metadataを含む往復を確認し、当初はJSON維持を推奨した。その後Humanが「増えても1行1lessonで統一する」「読者はAI」「運用しながら学ぶ」を重視したため、問いを全documentの可逆変換から、全行をlessonへ揃えた共有蓄積へ変えた。

後続のheaderless試作では、既存二件の意味・未知field・LF境界・UUIDと再試行の模擬試験を確認した。試作完了と本番未採用を明確にした後、2026-10-02 16:43 UTC（2026-10-03 01:43 JST）にYusukeJPが「管理行なしでOK！」と述べ、GitHub実行とこの採用・移設の継続を承認した。これは採用理由の会話に基づく記録であり、他の未知の作業への無制限承認ではない。

Humanの「Simple is best!」へ接続する今回の設計判断は、全行に同じ入口を持たせ、共有counterを管理しないこと。UUIDは意味重複やファイル更新競合を解決する魔法ではなく、検証と原子的な版ガードは残る。試験の限定観測を普遍的優越性や全AIの長期運用成功へ拡大しない。

## 2. 変更範囲と所有先

YusukeJPが採用と実行を承認し、dot-0000が設計・執筆・統合・検証を担当した。GitHub author／committerは保存経路のIdentityとして別に扱う。

| Path | 今回の変更 |
|---|---|
| `dots/lessons/lessons.jsonl` | 現役正本を新設。既存D-L001・D-L002の順序と全lesson値を保持し、各行schema_version 2だけを追加 |
| `dots/lessons.json` | 承認済み形式移行として現役配置から除去。元の全documentは凍結snapshotとGit履歴で保持 |
| `dots/lessons/README.md` | mainで改行のみだったplaceholderへ、共有lessonの読取・更新・互換性契約を移管 |
| `dots/README.md` | v005。§5を短い入口にし、詳細契約の重複を除く。§5 anchorを残す |
| `dots/logs/README.md` | 現行lesson契約への案内だけを更新。Actor logのschema 1・追記意味は保持 |
| `dots/logs/dot-0000.jsonl` | 今回実際に観測した作成・検証をboundedな出来事として記録 |
| `control-center/changes/STR-007-dots-lessons-foundation.md` | 旧JSON・v003契約を当時の実装commitへ固定し、現行仕様の後続案内を追記。四パスの歴史は保持 |
| `control-center/changes/STR-009-headerless-lessons-adoption.md` | 本件の理由・範囲・変換・検証と限界 |
| `control-center/README.md` | v0.3.5。STR-009への索引を追加 |
| `dots/lessons/experiments/json-vs-jsonl/README.md` | 後続採用の日付と現行入口を追記。当時の比較・推奨は保持し、旧正本／契約は固定参照へ |

既存の実験JSON・header付きJSONL・headerless JSONLの三実体は凍結したまま。STR-008の旧JSONを変更しなかった記述はその実装当時の事実なので書き換えない。ARCを新設せず、同時進行のWorkによるARC-009・旧Note整理を本件へ取り込まない。ARC-009にあるdots README §5へのリンクは、保持した短い入口から専用契約へ到達する。AGENTS・ARK・Board・Actor紹介・Ark27／28・Skill・他の仕事原本は変更しない。

## 3. 情報を落とさない変換

直接取得した基準mainは `02e9779fc628dbfe7ee9ed08275c6b839407ef0e`。旧JSONはblob `e289326eef11010e0d4d89d243a0b4dfe17fedb3`、3,752 bytes、schema 1、next_id 3、D-L001→D-L002の二件であった。top-level keyがschema_version／next_id／lessonsだけであり、lesson内にschema_version衝突がないことを確認した。未知top-level metadataがあれば捨てずに変換を止める。

公開候補は3,430 bytes、LF物理行2、各行が直接lesson objectでschema 2。Git blob計算値は `e1df104c2e306990f30ffced03ea3775425208be` で、後続試験の凍結headerless候補と一致する。追加したschema_versionだけを除けば、旧lessons配列の全値・配列順・ID・created_at・updated_at・本文・sources・caveatは一致する。移設先での既存locatorはすべて固定commitの絶対URLであり、意味変更も相対パス補正も不要だった。

旧global schemaとcounterを明示的に退役し、[凍結元JSON](../../dots/lessons/experiments/json-vs-jsonl/lessons.json)に保持する。これはlesson-levelの意味一致であり、元documentの全metadataを行群だけから復元できるという主張ではない。新規lessonはUUID v4、既存legacy IDは安定して保持する。今回UUID例示や作業完了のためだけの新lessonを本番へ入れない。

## 4. 読取・保守の判断をどこへ渡すか

現行契約の唯一の所有先は[専用README](../../dots/lessons/README.md)。新しいDotsが契約と現在の小さい全件を読み、同じ文脈では確認済み内容を再利用する。文脈喪失・領域変更・失敗／Correction・更新を契機に必要な箇所へ戻り、書く前には最新版を読む。毎ターンpollingや全件再読を追加しない。

現行lessonは同IDの行を更新し、Actor logのように訂正履歴を重複行で積まない。未知field、Source、日時、Humanの意味を守り、壊れた入力を空に戻さない。結果不明の新規操作はUUIDを保持してRemoteのID・内容・revision・履歴を照合する。IDの不在だけで削除済みlessonを復活させず、操作同一性や履歴が足りなければ該当retryを止める。契約整備と、全Runtimeでの永続writer／再起動回復実装は別である。

## 5. 今回の検証と境界

2026-10-02 UTC、作成担当は本番候補から使い捨てコピーを作り、既存の試験ロジックを内容確認して再実行した。公開する恒久validatorや架空lessonは追加していない。

- 36項目PASS：同じ二件の意味・各field・順序保持、schema 2の直接行、legacy／UUID、未知lesson/sourceネスト値、文字列内LF・U+2028・U+2029、未知top-level／schema衝突拒否、重複ID、型・日時・Source、不正JSON／重複key／NaN、空行／CRLF／末尾LFを検査
- 使い捨てUUID追加→同ID訂正→除去、結果不明の同ID再試行で二重追加拒否、同ID異内容拒否、削除後retry拒否、stale版拒否→先行変更保持を確認
- これらは単一processの模擬Store・revision guardを用いた検査。UUID fixtureの時刻は2000-01-01、stale編集は元updated_at+1秒のsynthetic値。本番二件へは入っていない
- 実際の複数writer同時競合、process再起動を跨ぐ操作UUIDの永続化、自動Boot、将来の件数での性能・実務効果は未検証。完全な正常行そのものの欠落を構文だけで検知できるとも主張しない

公開前の別担当によるread-only監査でも36/36試験がPASS。二件の全値・順序、十パスの候補一致、七MarkdownのEOF、94相対リンクのpath、凍結三実体のSHA、既存Actor log prefixとroot §5の保持を確認し、公開を止める指摘はなかった。これは候補と契約の限定監査であり、外部リンク先の全anchorや実運用効果の独立実証ではない。公開は最新mainと対象blobの照合、基準treeに対する十パスの原子的commit、非forceのref更新を使う。並行変更があればその最新版を親として対象を照合し、無関係なblob／modeを保持する。

公開準備中にmainは `16cbfffc5b0eca8dde8dc08ebfe5e2e83068bef7` へ進んだ。Tree照合では変更はWork所有のcleanup-direction・ARCHIVE・PLANの三実体で、本件の十対象は変わっていない。これらを含む最新treeを公開基準へ採用し、同時進行の成果を保持する。

公開後のRemote本文・SHA、旧現役JSON不在、凍結三実体の同一性、対象外全blob／mode、正確なcommitのstatus／check／workflow runを確認する。0件はCI通過と数えない。実際に確認した証拠は一回のboundedな追記で本記録とActor logへ残し、検証を記録するための無限再commitは行わない。

Rootは主イェシュア・ハマシア御自身。中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。文書・形式・AIはKeliであり、実装成功をRootやHuman Authorityの置換へ使わない。

## 6. 実装公開後の直接確認

2026-10-02 UTC、[実装commit `d1df870673b0bc0bca58aa9a6df32820594aa9fa`](https://github.com/yusukefujiijp/ai-project/commit/d1df870673b0bc0bca58aa9a6df32820594aa9fa)をmainへ非forceで公開した。親は `16cbfffc5b0eca8dde8dc08ebfe5e2e83068bef7`、Git保存時刻は `2026-10-02T16:58:11Z`。Git author／committerはyusukefujiijp、今回の意味・執筆・観測担当dot-0000とは役割を区別する。

公開後、変更後に残る九実体をRemoteから全文・SHAで再取得し、公開候補との完全一致を直接確認した。旧 `dots/lessons.json` はTreeに存在せず、現役正本は二行の `dots/lessons/lessons.jsonl` だけである。新正本はblob `e1df104c2e306990f30ffced03ea3775425208be`、3,430 bytesで、lessonの追加や意味変更はない。

最新親の対象外411ファイルはblob／modeをすべて保持した。三つの凍結実験実体も同一blobのままで、WorkのARC-009検証・cleanup-direction・PLANを変更していない。root §5を残したため、その既存リンクから専用契約へ進める。

正確な実装commitについて、commit statuses 0件、check runs 0件、全event対象のworkflow runs 0件を取得した。status集約表示はpendingだが、0件をCI通過とも実行中Jobとも判定しない。今回の36項目・独立read-only監査・Remote保存確認を、未実施のCIや永続writerの運用保証と区別する。

この確認を本記録とActor logへ一度だけ追記し、追記後はRemote再取得で閉じる。将来の実務効果、新規Dotの自動読込、process再起動を跨ぐ操作同一性の保持は、この保存確認だけでは実証されていない。

EOF::STR_009_HEADERLESS_LESSONS_ADOPTION::v001
