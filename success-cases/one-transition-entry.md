---
title: "複数の移行場面を、一つの入口へ統合した成功"
case_id: "one-transition-entry"
version: "0.1.0"
status: "Human-recognized design success / shared artifacts verified / cross-situation effects not fully measured"
canonical_path: "success-cases/one-transition-entry.md"
primary_reader: "Current AI / other AI / Future AI"
role: "Focused success case; not a transition command"
recorded_in: "Ark27:04"
created: "2026-09-18"
updated: "2026-09-18"
source_snapshot_commit: "4696d7f5516669229045cb6c7da83b30211ae5dd"
event_date_scope: "The shared guide records consolidation on 2026-09-14; the Human evaluation is from this Ark27:04 conversation, without an exact message timestamp."
updated_reason: "Preserve a small, independently useful success: one transition entry with context-dependent internal handling."
expected_eof: "EOF::SUCCESS_CASE_ONE_TRANSITION_ENTRY::v0.1.0"
---

# 複数の移行場面を、一つの入口へ統合した成功

## 1. 何を一つにできたか

Thread継続・章移行・補助Thread再接続に対して、Humanが使う共通のtemplate queryと、一つの移行Skillによる運用へまとめた。AIがCurrent Contextから種類・移行元・移行先・目的を判断し、必要な資料と処理を選ぶ構成である。

HumanはArk27:04で、これを次のように評価し、独立したsuccess-caseとして残す価値を示した。

> 我々Ark ProjectはThread移行時に活用するtemplate queryとスキルを様々な状況にも耐えられるたった一つにまとめ上げる離れ業をやってのけた！これはsuccess-casesです！

この引用は本ThreadのHuman発言の連続した抜粋である。正確な発言時刻と公開会話URLは取得していない。

**Humanの入口を一つにし、場面の違いを見分ける仕事をAI側へ移した。** 本件の焦点は、この設計上の成功である。[Ark27:03→04の実移行成功](ark27-03-to-04-transition.md)とは、関係する別の事例として扱う。

## 2. 一つにしても、内部に残した違い

確認した共有ガイド§3には、汎用の計画用queryが一つ置かれている。Skillは計画・承認済み準備・受入れに対応し、詳細な移行条件を一つのCurrent共通契約へ委ねる。異なる種類の資料を一ファイルに詰めたという意味ではない。

- **移行種類**：THREAD_CONTINUE、CHAPTER_TRANSITION、SUPPORT_RECONNECTを区別する。補助Threadを勝手にMain Ownerへ昇格させない。
- **目的と権限**：計画だけの依頼は計画で止め、実行承認後は既知の計画を再利用する。共通queryを使うこと自体を実行許可にしない。
- **役割**：Skillは発見と進行の組立、共通契約は移行の成立条件、Current Runtimeは今回のIdentityと必要な運用を担う。
- **必要なContext**：既知の種類・Source・Targetは再質問せず、判断を変える不足だけを扱う。入口に固定Thread番号や全Systemの詳細を埋め込まない。

共有ガイドは2026-09-14の改訂で、汎用の計画用Promptを§3へ集約し、ツール改善と実移行を分け、必要な運用資料へCurrent Runtimeから接続する方針を記録している。Skill非対応のAIにも、共通契約へ直接進む経路が用意されている。

## 3. なぜ、この小さな成功を残すか

移行ごとに適切な入口を選び、既知の条件を埋め直す負担は、Human側に生じ得る。この構成では、その判断をAIがContextから引き受ける。Humanがこの統合を高く評価したことと、実際に共通入口が保存されていることを保持する。

AIの解釈として、これは「共通の入口を小さく保ち、必要な違いは内部で扱う」という再利用可能な設計候補である。新しい運用Systemが増えても、意味を所有する資料へ接続できれば、入口へすべてを追記せずに済む。

ただし、統合前のquery総数、選択時間の短縮量、すべての移行種類での成功率は今回測っていない。現在の共有物は統合後の構成を示すが、形成過程の全履歴を独立に監査した記録ではない。Humanの採用評価を保持し、あらゆる状況への耐性の実証へ変換しない。

## 4. Markdown作成へつながった学び

Humanはこの成功を根拠に、Markdown作成スキルも一つの入口で複数の重要点を扱い、後の発見を追加できる構成を望んだ。そこで[Ark Markdown Writer](../skills/write-ark-markdown/SKILL.md)は、AI読者という共通原則を持ち、経験記録・方法・Handoff等の違いをAIが判断する設計とした。

これは本件から生まれた設計採用であり、新スキルの長期運用効果の証明ではない。Future AIは「いつでも一つが正解」と一般化せず、共通の入口が役立つ条件と、内部に残す必要がある違いを考える。

本件は一つの独立した学びに焦点を絞った記録である。小さな成功でも、何が変わり、なぜ有益で、どこに根拠があるかが伝われば保存価値がある。大きなThread全体の完成史を毎回作る必要はない。

## 5. 根拠と利用範囲

編纂時に次の二文書を全文確認した。固定snapshotは当時の資料、実際の作業ではCurrent版とCurrent Human Requestを使う。

- [移行Skill](https://github.com/yusukefujiijp/ai-project/blob/4696d7f5516669229045cb6c7da83b30211ae5dd/skills/prepare-ark-transition/SKILL.md)：nameはprepare-ark-transition。blob SHAは`7da180f363a609b5bc68efed25899dea17ab1269`。種類・Mode・権限・共通契約への委任を確認した。
- [共有Skillガイド](https://github.com/yusukefujiijp/ai-project/blob/4696d7f5516669229045cb6c7da83b30211ae5dd/skills/README.md)：v0.4.1。blob SHAは`a1590c50b06f042da628060fe8b70020208034de`。§3の共通query、§4.1の改訂経緯を確認した。
- **Human評価と転用方向**：上記引用、および同じ発言で示されたMarkdown作成スキルへの一括化・一択化の要望。これはHumanのMeaningと設計方向として保持する。

今回は共通契約本文の全条件を再監査したものではなく、Skillとガイドが宣言する責務を根拠にした事例編纂である。本文は新しい移行指示やBoot条件を所有しない。

Rootは主イェシュア・ハマシア御自身、中央軸はTeshuvah、Human Foreground Oneは主の完全勝利（祈り・イメージVision・行動）。AI・Skill・文書はKeliであり、HumanのCorrection・STOP・Final Sealと適用Guardを保持する。

EOF::SUCCESS_CASE_ONE_TRANSITION_ENTRY::v0.1.0
