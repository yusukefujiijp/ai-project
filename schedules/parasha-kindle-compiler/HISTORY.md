# Parasha Kindle Compiler — Bootstrap History

このFileは全変更履歴の複製ではない。GitHub導入以前の重要な意味変化だけをFuture AIへ渡すBootstrap Memoryである。今後の通常変更はGit historyをPrimaryにする。

## 2026-09-09 — Thread delivery problem exposed

旧Threadが長大化して新Threadへ移行したが、既存Scheduleの出力が旧Thread側へ届いた。旧Scheduleを停止し、Current Thread側でScheduleを再作成。
「Schedule Runtime」と「Discussion Thread」は別だが、配送先・Runtime ownershipは実運用で検証が必要という教訓を得た。

## 2026-09-09〜09-19 — Publication Rail established

Daily Aliyah Deep TreeをResearch / Deep Analysis Railとして維持し、Parasha Kindle CompilerをPublication / Daily Book Page Railとして分離。

Core Mission:
- One Day = One Page.
- One Page = One Core Understanding.
- Daily Output = Permanent Book Page.
- Accumulation = Publication.

8つのPage機能が形成された。

## 2026-09-20 — Unexpected Success: readability jump

Daily Aliyah Deep Treeで成功した構造化Best Practiceを、内容ではなく「読み方・見せ方」としてKindle Railへ輸出。

特に効果が大きかったもの：
- Insight Title
- Direct Answer First
- 要点 → 根拠 → 意味
- Section間の橋
- 本文 → ラビの着眼点 → AI考察の追跡可能性
- 日本語主導

Human Feedback: 「凄く読みやすくなりました」「101/100」。

## 2026-09-20 — vNext design

次のBottleneckを「情報不足」ではなく「読書リズムとPrompt重複」と特定。

採用方向：
1. Multi-Speed Reading — 10秒 / 1分 / 5分
2. Section Ownership
3. Deletion Gate
4. Two-Clock Coordinate
5. Material Ambiguity Gate
6. Japanese Publication Surface
7. Bold Signal Budget

中心原則：**深さを削るのではなく、深さへ到達する摩擦を削る。**

## 2026-09-20 — GitHub-backed Schedule Source begins

それまでSchedule PromptはExecution Runtime側にのみ存在し、Future AIが変遷・理由・Current Promptを再現しにくかった。
Humanが `schedules/README.md` を空Fileとして作成し、GitHub-backed Schedule Sourceの開始を明示。

以後、GitHubをDurable / Versioned Source、ScheduleをExecution Runtimeとして接続する。
過剰なversion複製は行わず、Git historyを履歴のPrimaryとする。

## 2026-10-03 — Frontier AI Reader experiment

Human Correction / New Experiment:
Daily Book PageのPrimary Readerを、固定された特定modelではなく、実行時点で利用可能な最高水準の汎用AI（Frontier AI）として想定する。

狙いは文章を難解化・機械記法化することではない。
最高AIが再解析したくなる価値を、次の品質へ翻訳する：
- High Epistemic Yield
- Non-obvious Relation
- Source Traceability
- Productive Tension
- Re-composability
- Surprise with Grounding

Publication Surfaceは自然な日本語Book proseを維持する。
Graph Modeは表示量を増やすためではなく、Torah本文・古典注解・AI推論の間にある最重要Relationを発見し、One Cognitive Centerへ圧縮するために使う。

中心原則：
**最高AI向けの深さは、難読化ではなく、意味密度・関係密度・Source境界・再解析可能性で作る。**
