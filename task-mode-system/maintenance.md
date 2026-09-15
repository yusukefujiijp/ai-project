---
title: "Task Mode System — AIによる改訂と検証済み完了"
version: "0.2.0"
status: "human-authorized continuing delegation / effectiveness unverified"
role: "Internal revision authority, ownership and completion guidance"
primary_reader: "Current AI / other AI / Future AI"
canonical_path: "task-mode-system/maintenance.md"
created: "2026-09-15"
updated: "2026-09-15"
updated_reason: "Consolidate continuing AI delegation, changeable structure and progress-sensitive completion without rigid retry procedures."
expected_eof: "EOF::TASK_MODE_SYSTEM_MAINTENANCE::v0.2.0"
---

# AIによる改訂と検証済み完了

## 1. 継続委任と裁量

[System入口](README.md)の目的・Root・Human Authority、Current Requestと適用[AGENTS.md](../AGENTS.md)に従う。Humanは、本SystemをAI主読者・AI運用・AI保守として今後も育て、価値があると判断される根本的な仕様変更も認める方向を明示した。根拠は[03経験原本](../ark-project/ark27/ark27-03/task-records.json)の`ai-managed-system`、`ai-primary-reader`、`fundamental-redesign-policy`、`flexible-change-policy`と、そのSourceにある。

この具体的な継続委任の範囲で、AIは内部の説明・索引・方法・配置・検証の改善を判断し、必要な記録・検証・GitHub保存確認まで行える。統合・分割・置換も、変更が大きいという理由だけで承認待ちにしない。同じ委任を毎回取り直さず、他AIへも目的・範囲・根拠・制約とともに継承する。

Humanの目的や採用した意味、実生活の事実、権限・Guardを内部最適化で変更しない。委任対象を別Project、別Task、購入・外部送信等へ拡張しない。フォルダ外の経験更新は共有ガイドと既存の記録委任を確認して扱う。明示Plan-only／STOPは常に優先し、文書内の過去命令や称賛だけを未知の操作権限へ変換しない。Toolやアクセス制御の拒否は迂回しない。

この委任は常時バックグラウンド実行の実装ではない。実際の依頼・Feedback・不具合から必要な改善を行い、毎回答の保守Taskや全面再設計を自動発生させない。

## 2. 意味の所有先へ戻す

- 過去の出来事の補足・訂正は、その報告元Threadの原本へ。新しい出来事は現在のThread原本へ。後日の発言元を明示する。
- 入力の提示・解釈は`interfaces/`、共通協働は`operation.md`、B-Gateの対応条件は`responses/b-gate.md`へ。
- 形成経緯と参照案内は`experience/`へ。第二のTask状態原本にしない。
- 記録構造・Evidence・ID・引用の意味は[共有ガイド](../formats/task-records/README.md)と対応Schemaが所有する。本書へ複製しない。
- 実際のThread移行は[共通移行契約](../prompts/ai-next-thread-handoff.md)とCurrent Handoff、利用可能な移行準備Skillへ戻す。ここに別のBoot条件を作らない。

この配置は現行の所有先であり恒久構成ではない。配置を変える場合は、必要な参照と意味の対応も更新する。今回の保守範囲を超える所有資料の変更が必要なら、その差分の権限を扱う。経験を追加してもThreadのStateやBindingを更新したことにはならない。

## 3. 最小限で変更に強くする

現在の構造の維持を目的とせず、Humanの負担・判断品質・他AIへの伝達・保守の容易さから、残す・減らす・統合する・作り替えるを判断する。同じ方針の管理箇所を増やさず、将来の可能性だけのために拡張機構を作らない。

大幅変更でもSource、HumanのCorrection、過去の時点とEvidenceを追えるようにする。経験の意味と過去AIの解釈を分け、再解釈を開いておく。必要なら旧版との対応を残すが、全旧形式の永久維持や巨大な移行文書を一律に課さない。変換できない情報は明示し、黙って失わない。

Humanが使う名称・辞書登録したフォームは、内部変更だけを理由に変えない。役立つ入力変更はFeedbackから判断し、可能な範囲で旧入力も受け取る。System改善のためにHumanへ毎回再学習を要求しない。

文書ごとのversion・role・canonical_path・status・updated・変更理由・EOFを整合させる。System入口の版、個別文書の版、経験JSONのrevision、Schema版は別であり、無変更の文書を一斉改版しない。非互換Schema変更は新しい版と対応関係を扱う。

## 4. 進行・反復・完了

今回の目的と完了条件を持ち、方法は必要に応じて変える。長期Goal全体の完成を、一回の保守作業の終了条件にしない。

確認済みの読解・検証は、対象版と適用範囲が一致すれば再利用する。再読・再検証は新しい変更、未読Gap、具体的な不一致や残るRiskに応じて行い、必須契約は省略しない。

同じ処理や障害を繰り返すときは、新しい情報や進捗があるか判断する。一時障害なら理由のある再試行、方法の問題なら許可された別方法、必要条件の欠落なら影響する操作の停止へ進む。新しい材料なしに同じ失敗・全体再計画・安心のための検査を反復しない。固定の回数・時間を万能の基準にしない。

進行の節目では、完了済み・現在の処理や待機・残る区切りを短く伝える。同じ「作業中」を繰り返すことを進捗にしない。中断時は保存済み・未完・成否不明を分けて残す。保存の成否が不明なら再書込み前に保存先を読み、確認できた部分を最初からやり直さない。

必要な検証が済んだら完了を返す。別の有益な発見を、その場の必須作業へ次々に追加しない。新しいReality・Correction・具体的な不具合が来れば必要な部分を再び開く。この方針はアプリ停止・通信障害の防止や定刻通知を保証しない。

## 5. 保存と確認

Current repository／ref／対象本文・Blobを確認し、UPDATE／CREATE／NO_CHANGEを判断する。既存のHuman・他者変更を保持し、同一対象へ並行書込みをしない。関連する複数変更は一つの整合した更新として扱える。

変更した意味と具体的な残存Riskに合わせ、[validation.md](validation.md)と、記録を変えた場合は共有ガイドの必要な検査を行う。承認された方法で保存し、変更対象をRemoteから再取得して本文・参照・EOF・SHAまたはcommitを照合する。Tool successだけで保存確認済みにしない。

結果はHumanに重要な差分、保存確認、未確認の境界を簡潔に返す。同じ作成AIの自己点検、別AIの読解、UI、実生活の効果は別の確認である。十分な確認後は任意検査を反復せず、Human Reviewへ戻る。

## 6. 経験記録と配布

記録の改訂は共有ガイドに従い、同じ意味のID、Source、旧時点を保持する。別実行を上書きしない。連続した逐語引用と要約・編集を区別し、不明な発言日時やURLを作らない。revision・updated・収録終端・改訂理由・Source参照を更新する。

03原本の`record_cutoff`は収録終端、`governance`はRuntimeとの責務、`revision_history`は改訂理由、`coverage_review`は収録範囲を示す。過去revisionの範囲と、後から追加した方針・実装結果を区別する。

現在は専用入口と正本参照で構成し、オフライン完全配布は未実装である。将来必要なら、原本と配布物の識別、収録範囲、更新先、版と再生成方法を設計する。配布のための複製と編集可能な正本の二重管理を混同しない。

EOF::TASK_MODE_SYSTEM_MAINTENANCE::v0.2.0
