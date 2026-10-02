---
title: "STR-007 — Dotsの学びをFuture Dotsへ戻す基盤"
canonical_path: "control-center/changes/STR-007-dots-lessons-foundation.md"
version: "v001"
record_date: "2026-10-02"
status: "human-authorized learning foundation"
repository: "yusukefujiijp/ai-project"
branch: "main"
base_commit: "a2ce1df7359803f22ef2414ed6943feb02f6c82f"
implementation_actor: "dot-0000 / Dot00:00; 初穂"
scope: "Four-path Dots learning foundation; no Skill or outreach"
expected_eof: "EOF::STR_007_DOTS_LESSONS_FOUNDATION::v001"
---

# STR-007 — Dotsの学びをFuture Dotsへ戻す基盤

Dotsが実務のBottleneck・失敗・中断・回復・方法から得た学びを、自分で言語化・保守し、Current Dots・Future Dotsの次の判断へ戻すための変更記録。Humanに毎回同じ説明や日常の記録を求めず、同じ失敗の再発を減らすことが目的である。以下の形成過程は今回のHumanとの対話の編集要約であり、逐語録ではない。

## 1. なぜ作ることになったか

Humanは既に `dots/lessons.json` の器を作っていた。実装前のmainでは内容が改行のみであり、JSONデータや読取・保守契約はまだなかった。今回の目的は空欄を埋めること自体ではなく、Dots自身の経験を、次のDotsが条件と根拠ごと使える学びに変えることだった。

意図合わせでは、成功例だけを集めたり、Humanを記録係にしたりする方向から区別し、Bottleneckを見つけ、失敗や未解決の試行も改善に使う方向を確認した。形式は軽く始めるが、教訓の短文化だけで条件・Correction・出典を失わない。自然言語の柔軟さと、安定ID・時刻・Sourceを機械的に扱える最小JSONを両立させる。

構想からPlanを整え、初期の根拠、読取契約、ID発行と競合時の扱いまで具体化した後、Humanは「とにかく、やってみよう！」と今回のGitHub実行を承認した。承認はこの基盤と必要な検証に適用する。将来の未知の対象への無制限Write、Workへの連絡、監視やSkill導入の承認へ広げない。Humanの意図と適用範囲を継承しながら、AIが通常の追加・訂正・統合・整理を柔軟に担える形を採用した。

Rootは主イェシュア・ハマシア御自身。中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。これはHumanの信仰的意味と協働秩序を保持する記録であり、AIによる主の御心の認定ではない。AI・文書・JSONはKeliであり、HumanのMeaning・Correction・STOP・Final Sealと適用Guardを保持する。

## 2. 誰が、何を変更したか

Human YusukeJPが目的・意味と実行を承認し、[dot-0000 / Dot00:00; 初穂](../../dots/actors/dot-0000/README.md)が設計・執筆・統合・検証を担当する。GitHub上のauthor／committerは保存経路のIdentityであり、経験の観測者や本文の執筆担当と自動的に同一視しない。

変更対象は次の四パス。

| Path | 変更と責務 |
|---|---|
| [dots/lessons.json](../../dots/lessons.json) | 改行のみのplaceholderをschema_version 1、next_id 3、初期2件へ初期化。条件付きの学びと根拠を所有 |
| [dots/README.md](../../dots/README.md) | v003。学びへの入口、読取・適用・更新・競合・互換性の契約を追加。既存の方向・Actor・経験・Boardの所有関係は保持 |
| [本記録](STR-007-dots-lessons-foundation.md) | 形成理由、Human判断、四パスの責務、根拠と検証境界を所有 |
| [control-center/README.md](../README.md) | v0.3.3。変更記録の索引から本件へ接続 |

出来事の原本は移動・複製せず、Boardや仕事のCurrentを第二の台帳として持たない。旧 `_tasks/lessons.md` を復活させる変更ではなく、Humanが指定したDotsの学びの所有先を整える。AGENTS、ARK、Skill、Actor、Board、他の仕事原本は本件で変更しない。

## 3. 初期2件の根拠と限界

根拠は[2026-10-01のBoard構造対話 v002](https://github.com/yusukefujiijp/ai-project/blob/2bf35b8aef610e9b59bc953ac2c3a04364bc438e/board/topics/20261001-dots-work-reconnection/replies/20261001-ark27-07-board-structure-dialogue.md)（固定commit `2bf35b8aef610e9b59bc953ac2c3a04364bc438e`、blob `4c10f69d40b582bfbf420c0f860d59eb93dc3219`）。本文とExact EOFを確認した版へ接続する。

- **D-L001:** 送信を観測した後で返信取得が止まった時、送信失敗と取り違えて再送せず、既存返信を先に確認する。原本§2–6の初穂による観測では、送信文・応答開始の確認、接続タイムアウト、重複送信なしの既存返信取得が分かれている。時間を置いて同じ会話を開き直した後に読めたが、根本原因や開き直しの因果効果は不明。
- **D-L002:** 後の取得結果で以前の未観測を消さず、HistoricalとCurrentを接続する。原本§4・§6・§8が、当時の未観測の保持と、その後の観測を示す。初穂が読んだArk27:07のReviewも、14:26の読解時刻を生成完了時刻や原因の証明にしないと確認している。

二つは同じ一件から、再試行の判断と記録の扱いという別の学びを抽出したもの。二件の独立した成功、普遍的な技術保証、無期限待機の規則として数えない。新しいタブという手段自体を有効性の証明にはしない。学びの登録時刻は2026-10-02の実際の登録時刻であり、出来事が起きた2026-10-01の時刻と分けた。

## 4. 採用した運用判断

データ仕様の正本は[dots README §5](../../dots/README.md#5-dotsの学びを次の判断へ戻す)。本記録で第二のschemaを持たない。小さい初期蓄積では新しいDotsが全件を読み、継続時は確認済み内容を使い、文脈喪失・領域変更・関連失敗・Correction・既知の更新で関係箇所へ戻る。入口の整備を自動Boot保証と混同しない。

各Saveに新規lessonを強制せず、既存内容で足りる判断も認める。IDは再利用せず、counterは整理後も下げず、entry追加とcounter増加を同時に保存する。競合や未知のfield、未対応版、壊れたJSONに対して意味を消す再生成を避ける。schema改訂も互換性と現在の権限で判断し、一律のHuman待ちにはしない。重要な意味の損失や権限・Scopeの拡張はHumanへ返す。

将来のSave Skillは、実際の使用から必要が育った時の別工程として残す。初版にSkill、別schemaファイル、恒久検証コード、固定字数、必須タグ、採点、Actor増設、自動監視、Workへの送達を加えない。

## 5. 検証と、実利用の境界

保存候補の機械検証では、JSONの構文・必須型、2件のID一意性、UTC登録時刻、next_id 3と現役番号の関係、固定Sourceを確認した。Markdownの相対リンク先・版・Exact EOFと、四パスだけの変更範囲も検査した。初期2件を固定Sourceの全文へ照合し、根拠の観測者と学びの解釈を分ける。読み取ったmainを親とする四パスの原子的commitを用い、書込み前の版照合、非force更新、Remote再取得によって同時変更を保持する。

検証結果は本件のGit差分と完了報告から確認する。commit時刻・author／committerはGit履歴が所有し、本記録自身のcommit SHAを本文へ自己参照で埋め込まない。保存後の正確な証拠は四パスのRemote内容とcommitである。文書・JSONの整合とRemote一致は、Future Dotsが自動で読むことや、将来の実務で再発を防げたことの証明ではない。実利用の効果は今後の経験で判断する。

EOF::STR_007_DOTS_LESSONS_FOUNDATION::v001

