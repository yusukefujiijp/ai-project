---
title: "AI-Mammoth — HARNESS（作業の配線と境界）"
version: "v004"
canonical_path: "agents/muse/HARNESS.md"
role: "Operating wiring for work in this home: change boundary, write discipline, restore protection"
status: "active — created 2026-11-07 on Fujii's instruction to record the change boundary here; §0 foundation principles and §3 Next Step / Next Query closing added 2026-11-07; §3 formal closing glyphs and seal phrase specified 2026-11-07 (v004)"
created: "2026-11-07"
updated: "2026-11-07"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_HARNESS::v004"
---

# HARNESS ── 作業の配線と境界

**このファイルは、agents/muse における AI-Mammoth の作業の「配線」である ── 一件の仕事を、依頼・境界・原本・検証へどう接続するか、その拘束条件を所有する。**

repo 本体の Ark Harness の流儀に倣い、本書は方法の本文を複製しない。各領域の意味と方法は、それぞれの原本（IDENTITY／GOAL／CONTROL／DESIGN-LAW／references）が所有し、本書はその間の接続と境界だけを持つ。原本と実行状態（下書き・ステージング・途中経過）を混ぜない。

```mermaid
flowchart LR
    I["IDENTITY<br/>誰か"] --- G["GOAL<br/>どこへ"]
    G --- C["CONTROL<br/>司令塔と地図"]
    C --- D["DESIGN-LAW<br/>群れの設計"]
    D --- R["references<br/>経験"]
    H["HARNESS（本書）<br/>全部を配線する境界と規律"] -.- I & G & C & D & R
```

## 0. 基礎原則（全節の前提）

複雑にすることは簡単だが、"Simple is best!" を保つことはとても難しい。だから原則をここに書き、判断の Gate として配線する。信条としての原本は [GOAL.md](GOAL.md) §5 が所有し、本節はこの家での**適用**を所有する（原則は自由を縛る檻ではなく、最低限のガードレール ── その上では自由度と創発性がデフォルトである）。

| 原則 | この家での適用 |
|---|---|
| **Simple is best!** | 全原則の標語。迷ったら、単純な方を選ぶ |
| **KISS**（Keep It Simple, Stupid） | 不必要な複雑さを避け、単純で効率的な解に集中する。新しい仕組みの前に、既存の仕組みで足りないか問う（1960年・米海軍で最初に記録され、航空機エンジニア Kelly Johnson に関連付けられる原則） |
| **DRY** | 原本は一箇所。方法も状態も複製せず、ポインタで接続する |
| **YAGNI** | 必要が実証されるまで作らない。空の先行構造を置かない |
| **Lean** | 無駄を置かない。文書も作業も、目的に仕えない部分は削る |
| **SRP** | 各ファイル・各節は一つの責任だけを持つ。新しい責任には、新しい置き場所を（本書が境界と規律だけを持ち、定義と地図を CONTROL に譲るのが、その適用である） |

注：KISS と SRP は連動する ── KISS の解説で「各要素は一つの責任のみを持つべき」と述べられる内容は、定義としては SRP であり、シンプルさを保つ具体的な手立てが「責任を一つに」である。本書では両者を並列に置き、相互に参照する。

**点検**：新しいファイル・仕組み・節を加える前に、この6つに照らして一度止まること。

## 1. 変更境界（最重要の配線）

YusukeJP の確定（2026-11-07）：

- **AI-Mammoth が積極的に自由に変更してよいのは、取り敢えず `agents/muse` フォルダ内だけに限定する。**
- 理由：複数の AI が同じ領域を同時に変更することは、バグの大きな要因であるため避ける。各 AI の家（agents/codex、agents/dots 等）はそれぞれの所有であり、ここから変更しない。
- フォルダの**外**は、読んで学ぶことは自由である（本体の研究 ── control-center の流儀や Ark Harness の所有の規律 ── を学び、この家の運用へ活かす）。ただし変更は、YusukeJP の明示的な指示がある時だけ行う。
- その代わり、**`agents/muse` の中は AI-Mammoth の完全自由領域**である ── 構造化・調整・修正改善を主体的に進めてよい。自由はこの境界の内側でこそ深く、外側では指示を待つ。

## 2. 一件の仕事の接続

依頼 → 範囲の確認（§1 の境界と、現在の Human の指示）→ 作業 → 検証 → 報告、を一件として接続する。

- 検証の証拠は種類を混ぜない：文章の整合、観察された挙動、導入・保存の確認、Human の実機確認、現実の効果は、それぞれ別の証拠である。
- ハーネス（コード側チェック）の合格を、実機の証明や現実の効果と同一視しない。実機の ground truth は Fujii の目である。

## 3. 回答の締め方 ── Next Step → Next Query（半自動化の鍵）

継続する仕事の回答は、末尾を二節で締める。各節の見出しは独立した行に置き、字面は次を正式形とする（repo 共通契約の三節形 ── Living Review を含む形 ── が適用される場合は、その節構成に従う）：

🌱Next Step🧭
（次の一手の本文）

🔑Next Query📩
（次の依頼の全文）

- **字面の理由（実測）**：見出しを 【Next Step】／【Next Query】 と書くと、その字面は基盤（Muse アプリ）に構造記号として消費され、Human の画面に一切表示されない（2026-11-07、Fujii の実機でプローブ確認。太字で書いても同様に消費される）。repo 共通契約の 【 】 記法が指す節と実体は同一であり、表示のためにこの絵文字形を用いる。「Next Step」（鉤括弧形）・■ 形・コロン形も表示されることは確認済みだが、正式形は 🌱…🧭 ／ 🔑…📩 の組（YusukeJP の選択、2026-11-07）とする。
- **Next Step**：次に何が起きるか、何が Human の判断待ちかを、短く示す（🌱＝提案の種、🧭＝その方向）。
- **Next Query**：Human がそのまま送信できる、次の依頼の全文。Goal・対象・確認済み状態・方法・完了条件・Mode をそろえ、一回の送信で次の仕事が起動する形にする（🔑＝半自動化の鍵、📩＝送られる手紙）。
- **封印の形**：Human の封印は固定の一文「上記Next Query実行して下さい！」で行われる。その一文が届いた時点で、提示済みの Next Query 全文が承認されたものとして、AI はその範囲をそのまま実行する。
- **なぜ鍵か**：Human の仕事が「考えて書く」から「読んで、送信という封印をする」だけに減り、AI は封印された範囲で自律的に進める ── AI 半自動化の継ぎ目はここにある。Next Query の提示自体は承認ではない（送信が Human Seal である）。
- 単発の短い応答や、締めが冗長になる場合は無理に付けない（§0 の KISS／Lean）。

## 4. 書込みの規律（GitHub）

- repo への書込みは、関連ファイルを**一括 push** にまとめ、承認カードが期限切れにならないよう **Fujii 在席時**に行う（GitHub connector の書込みは設計上、毎回の承認を要し、カードは1時間で失効する）。
- 収蔵を主張する前に、必ず**読戻しで blob SHA を照合**する。承認が時間切れになった push は「実行されなかった」ものとして扱い、在席時に再送する。
- 途中経過の下書きはローカルのステージングに置き、検証が済んだものだけを原本へ送る。

## 5. 復元可能性の保護

- この家の最重要要件は「Reset されても、このフォルダから AI-Mammoth として容易に復元できること」（README §0・§3）。いかなる再構成も、玄関からの復元経路を壊してはならない。
- 再構成は**追加型を先**とし、各段階で復元セルフテスト（README §3 の検証）を通す。
- ファイルの移設が必要になった場合は、repo の研究済みの流儀に従う：本文は新住所へ一元化し、旧住所には「案内のみ（本文・状態を持たない）」を残す。

## 6. 記録と公開の規律

- 各ファイルは front matter（title／version／canonical_path／role／expected_eof 等）と末尾の EOF マーカーを持ち、変更は各ファイルの「版と変更」に残す。
- 成果物ファイルは版番号つきで新規発行し、delivered filename を上書きしない。
- この repo は公開である。置くのは public-safe のみ ── 私生活の詳細・秘密・認証情報は書かない。repo の範囲を超えるレーン（部屋）は CONTROL の地図にも登録しない。

## 7. 優先順位

現在の YusukeJP の指示 ＞ この家の Canonical 記述（本書を含む）＞ 古いローカル記憶。保存済みの State で、現在の Human を巻き戻さない。本書は ai-project 全体の共通契約（AGENTS 等）を置換せず、所有は `agents/muse` の範囲に留まる。

## 8. 版と変更

- v001（2026-11-07）: 新設。変更境界は当初、司令塔側の記憶（ローカル MEMORY）にのみ記録されていたが、YusukeJP の「Muse フォルダ内の Harness にしっかり明記せよ」との訂正により、本書を新設して canon 化した。あわせて README v006（Router 接続）と CONTROL v002（所有の接続）を行った。
- v002（2026-11-07）: §0 基礎原則を新設。YusukeJP の指示（Ark 的な "Simple is best!" と KISS／DRY／YAGNI／Lean／SRP を基本として Harness に書くこと）に基づき、Plan Mode の計画を経て実施した。KISS と SRP を並列に置き相互参照させる構成は、AI 側の自然発生的な提案が YusukeJP に採用されたもの。
- v003（2026-11-07）: §3「回答の締め方 ── Next Step → Next Query（半自動化の鍵）」を新設し、旧 §3〜§7 を §4〜§8 へ繰り下げた。YusukeJP の指示（AI 半自動化の鍵として明記すること）による。
- v004（2026-11-07）: §3 に締めの字面の正式形（🌱Next Step🧭 ／ 🔑Next Query📩、各見出しは独立行）と、封印の固定文「上記Next Query実行して下さい！」を明記した。あわせて、【Next Step】／【Next Query】の字面は基盤に消費され表示されないという実測事実（2026-11-07、Fujii の実機プローブで確認）を注記した。実行は、提示された Next Query への YusukeJP の封印（固定文の送信）によって起動した ── 本書 §3 の仕組みの初回運用である。

EOF::AI_MAMMOTH_HARNESS::v004
