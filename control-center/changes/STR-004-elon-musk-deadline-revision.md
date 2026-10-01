---
title: "STR-004 — Elon Musk Deadlineを再利用Promptへ改訂"
record_id: "STR-004"
version: "v001"
canonical_path: "control-center/changes/STR-004-elon-musk-deadline-revision.md"
role: "Scoped prompt revision rationale, provenance and verification record"
status: "implemented and remotely verified / independent source review complete / field effects separate"
repository: "yusukefujiijp/ai-project"
ref: "main"
record_date: "2026-10-01"
base_commit: "b3e1b95821ce6272557c0f6d16152e4ff61460f0"
expected_eof: "EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_004::v001"
---

# STR-004 — Elon Musk Deadlineを再利用Promptへ改訂

## 1. Humanの意図と今回の範囲

Humanは旧資料を「とても古く」、汎用的でない部分が多いと指摘しつつ、「時がたたないと残すべき本質がみえてこない」と評価した。レビューを踏まえて添付を修正改善し、`ai-project/prompts`へ保存することを求め、「Very Good! Execute GitHub OK!」「Human Seal OK!」「実行して下さい！」と承認した。引用部分以外は意図の編集要約である。

今回の対象は一つの再利用Promptである。Skillの作成・導入、Dots＋Work基盤の実装、ArkのCurrent routing変更、実際のSession移行試行、締切・週次予定・監視の設定は含めない。以前の別案や広いContinue表現から対象を広げない。Root・Teshuvah・HumanのMeaning、Correction、STOP、Final Sealを保持する。

2026-10-01の確認時点では既存の構造変更記録はSTR-001〜003であり、本件をSTR-004とした。STR-003の基盤移行とは別の案件である。

## 2. 元資料と形成を残す

- Humanが今回提供した元資料: `elon-musk-deadline(1).md`、651行、17,410 bytes。全行を読解した。
- 元資料の宣言: `Elon Musk Deadline` / `v001-cplm` / `Ark05:01` / `skill_card_candidate`。
- 元資料内の候補Path: `_skill/skills/elon-musk-deadline.md`。変更前[mainの固定snapshot](https://github.com/yusukefujiijp/ai-project/tree/b3e1b95821ce6272557c0f6d16152e4ff61460f0)のtreeには存在しなかった。過去のGitHub保存・導入を確認した資料ではなく、今回このPathを削除・移動したわけでもない。
- 旧文書の作成日時は確認できていない。今回の読解・改訂日を旧文書の成立日へ読み替えない。

Humanが保持した定義の逐語文は、新Promptの§1に記載した。旧版§1と共通するDeadline-first／Scope-cut／Output-sealを保ち、現在のHuman表現で末尾を「実行原理である」とした。Elon Musk氏の内面や実証済み経営理論に誤帰属しない。

Ark05:01の月50,000円・週一成果物・Template Stack等は、形成時の足場として残す。現在のHumanの目標・実績・義務とは断定しない。原本全体の新しい現役コピーや、新しい保管体系は作らず、必要な形成の意味と変更理由を本件へ保持する。元の添付そのものは、このRepository内で独立に全文参照できる原本として公開してはいない。

## 3. どこを、なぜ、どう直したか

| 元資料の箇所・問題 | 実務上の影響 | 新Promptでの修正 |
|---|---|---|
| §1の締切先行・最高出力 | 有益な核だが、締切が推論・品質の抑制にも読める | §1〜3でScope・優先順位・資源・Deliveryを制約し、必要な根拠・品質・検証を保持 |
| §2〜4・6・9の7日／今週／週一／月50,000円 | 過去の例が汎用Runtimeや現在の予定に昇格する | §2・6・8で採用済み締切・比較用仮定・形成史を分離 |
| §4・6・11の固定順序・Top 3・必須見出し | 状況に応じた裁量と深い検討を不必要に狭める | §3で成果と判断基準を中心にし、固定Schemaを要求しない |
| §7のOutput Ladder | 価格・成熟度・検証・受け手・公開が一列の品質階段になる | §4で複数の判断軸を分ける。Paid／Freeを品質の上下にしない |
| §7・12の締切絶対維持と代替報告 | Failure Reportで本来の成果の未達を隠せる | §2・5で変更・未達を明示し、成果の完了と学習・報告の完了を分ける |
| §5・8の常時事前Seal的な読まれ方 | 既に承認された修正・保存も再承認で止まる | §0・3・7で有効な承認を再利用。新しいScopeや責任のみ判断へ戻す |
| §9〜10のTemplate中心の例 | 長期基盤の成熟か短期出力か、二者択一へ偏る | §6で慎重な戦略と限定試行の共存を例示。例を実際の開始命令にしない |
| 全体の文章＋CPLM反復 | 同じ規則が分裂しやすく、改訂の二重管理が増える | 起動・入力・判断・Guard・由来を一つの本文へ統合。CPLM一般の否定にはしない |

期待とActual、根拠、因果仮説、Correction、次の確認点を仕事に必要な形で残す。新しいSchemaや毎回の実験を義務化しない。保存・文書整合・限定応答試験・実利用・方法の普遍的効果を混同しない。

## 4. 変更するPathと、変えない範囲

| Path | 操作・責務 |
|---|---|
| `prompts/elon-musk-deadline.md` | CREATE。v002として単一Prompt、Human定義、現在の適用と由来を保持 |
| `prompts/README.md` | UPDATE。§3.13と更新metadataを追加し、新しい本体へ案内 |
| `control-center/changes/STR-004-elon-musk-deadline-revision.md` | CREATE。本件の理由・原典対応・検証・公開証拠を所有 |
| `control-center/README.md` | UPDATE。既存の変更記録一覧へ本件を追加し、更新日を記録 |

RootのAGENTS／ARK、各Ark章・Handoff・State、Skills、既存Prompt本文、PLAN、ARCHIVE等は本件で変更しない。旧文書の候補Pathからの削除・redirect・互換Stubは作らない。

Current AGENTS、ARK、Nearest prompts README、control-center READMEと既存STR記録を参照し、mainの一つの本体という現在方針に合わせる。変更前の入口は[固定prompts README](https://github.com/yusukefujiijp/ai-project/blob/b3e1b95821ce6272557c0f6d16152e4ff61460f0/prompts/README.md)、[固定control-center README](https://github.com/yusukefujiijp/ai-project/blob/b3e1b95821ce6272557c0f6d16152e4ff61460f0/control-center/README.md)から辿れる。

## 5. 検証と公開

準備・確認日は2026-10-01（UTC／JSTとも同日）。HumanのYusukeJPが対象と実行を承認し、AI-Collaboratorの「Dot00:00; 初穂」が改訂・検査・結果統合・報告を担う。GitHub author／committerと保存時刻は実際のcommitから確認し、意味上の依頼・実装担当と区別する。

候補本文の構造・metadata・リンク・EOF、原典の核と今回のCorrectionの保持、限定シナリオを確認する。公開時は最新mainと競合を照合し、対象外を保持した変更を行い、対象本文をRemoteから再取得して意図した全文・Path・ref・SHAを検証する。Tool successだけを本文一致と呼ばない。

公開前の確認結果:

- 元資料の全651行を取得し、17,410 bytesと一致。現在のHuman定義を逐語で保持した。
- 4候補のfrontmatter・canonical_path・宣言EOF・fence・相対リンク・今回の核・私的識別子の非混入を検査し、エラー0。既存READMEは案内と更新metadataだけの差分だった。
- 別AIが候補本文・記録・README差分・元資料を独立に読解し、実質的な公開阻害なしと報告した。締切なしで7日を捏造しない、必要品質を削らない、Failure Reportを元成果の完了にしない、Plan-only／STOPを優先する、承認範囲を再承認で止めない、という境界を文面と意味から照合した。
- これは構造検査と独立した文書・境界レビューである。実Tool操作の行動試験、実際のWork受入れ、他AIの全場面での挙動、実生活効果は検証していない。

### 5.1 mainへの公開とRemote再取得

**実装4パスをmainへ保存し、公開前の4blobと、公開後mainから再取得した4本文の全文一致を確認した。**

- 実装commit: [f3da643ee52ec0b46a015a76df0f7c69743e129e](https://github.com/yusukefujiijp/ai-project/commit/f3da643ee52ec0b46a015a76df0f7c69743e129e)
- 実装tree: `658f4b00d874e0233e896c380bffd9ff74c9475a`
- GitHub保存時刻: 2026-10-01T11:11:10Z / 2026-10-01T20:11:10+09:00
- GitHub author／committer: `yusukefujiijp`。Humanの依頼とAI-Collaboratorの実装担当は上記のとおり区別する
- 公開直前にmainが基点と一致することを再確認し、対象4パスだけを反映したcommitへnon-forceで更新した
- 391既存ファイルのうち2更新・2追加で393ファイル。対象外389ファイルはblob／mode一致で変更なし。Dots・各Ark章・Skills等を含む
- 公開後、mainから4パスを直接再取得し意図した全文との一致を確認。main headも実装commitと一致した

| Path | 実装commit時点で全文一致したblob |
|---|---|
| `prompts/elon-musk-deadline.md` | `a12c756832bc5d61156597e78f4a3a879fe7be7c` |
| `prompts/README.md` | `db1d9d611a57d4c44471ac63c61d7c2b9ca0bb1a` |
| `control-center/README.md` | `263715403f61860206321f7215a7954416200107` |
| `control-center/changes/STR-004-elon-musk-deadline-revision.md` | `3d87caf98dc17332338ae7f040db1498b4e7faf8` |

この表は実装commitの観測であり、Currentの永久pinではない。本節の検証追記は後続commitとして保存・再取得する。記録自身の未来のSHAを先に埋める循環は作らず、実装差分は[基点との比較](https://github.com/yusukefujiijp/ai-project/compare/b3e1b95821ce6272557c0f6d16152e4ff61460f0...f3da643ee52ec0b46a015a76df0f7c69743e129e)、追記の保存証拠は本ファイルのGit履歴から辿れる。

公開確認を、この方法の実生活上の有効性や実際の試行完了として扱わない。

## 6. 実利用で見直すこと

締切の採用、必要品質、Outcome変更、既存承認の利用に誤読が出たら、その場面・期待・Actual・Human Correctionを根拠として本体を改善する。一件の好結果や限定応答試験だけでUniversal Ruleにしない。実利用報告がないことも、失敗や未実行の証拠にしない。

復元が必要なら基点から本件4パスの差分を確認し、後続のHuman・他AI変更を残して扱う。Repository全体を過去へresetしない。方法改善から別の試行・導入・全体監査を自動開始しない。

EOF::AI_PROJECT_STRUCTURAL_CHANGE_STR_004::v001
