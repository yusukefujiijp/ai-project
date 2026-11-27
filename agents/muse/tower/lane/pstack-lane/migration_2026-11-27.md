---
title: "pstack LANE 移行記録 ── TOWER における全経緯の完全引き継ぎ"
version: "v001"
canonical_path: "agents/muse/tower/lane/pstack-lane/migration_2026-11-27.md"
role: "The complete migration record of the pstack LANE: from the start of the Lauren Tan watch (2026-11-25) through port rounds 1-4, the /correct rule table, and the backup bundle (2026-11-27), in 14 layers"
status: "canonical record / written in TOWER at migration, 2026-11-27"
created: "2026-11-27"
updated: "2026-11-27"
repository: "yusukefujiijp/ai-project"
expected_eof: "EOF::AI_MAMMOTH_PSTACK_LANE_MIGRATION::v001"
---


Version: v001（2026-11-27、TOWER から pstack LANE へ）

================================================================
第0層 ── この文書の位置づけと読み方
================================================================


- 2026-11-25 から 2026-11-27 まで、TOWER（メイン）で行われた Lauren Tan（@poteto）／pstack に関する全作業の経緯を、pstack LANE へ移行するための引き継ぎ記録である。
- 起動クエリ（既にこの部屋へ渡し済み）は要約版であり、本書が完全版である。要約と本書が食い違う場合は、本書を正とする。
- 方針は YusukeJP の指示「不足より過剰」。ただし冗長化ではなく、複数の角度（事実／数値／決定の理由／失敗と訂正／所在パス）から書いて意味の齟齬を消すことが目的である。


- 第1〜5層: 時系列の経緯（何が起き、どう検証したか）。
- 第6〜9層: 決定とその理由（なぜそうしたか。将来の判断の前提になる）。
- 第10〜12層: 現在の運用状態と未決事項（次に繋がる interface）。
- 第13層: ファイル・パス・ID の索引。

================================================================
第1層 ── 起点: 追跡の開始（2026-11-25）
================================================================


- 2026-11-25 19:41 JST、YusukeJP が Lauren Tan の SNS 追跡を依頼。「pstack 情報が最重要」と明示。
- 同日 19:43、更新頻度として「毎日教えて欲しい！」を選択。


- Lauren Tan（@poteto）。SpaceXAI（xAI）の Principal Engineer、Grok Bot と Cursor を担当。React Compiler コアチーム。元 Meta／Netflix。
- 主な SNS は X（@poteto）。GitHub も @poteto（リポジトリ85件）。
- 代表的な自作: brainmaxxing（419★）、noodle（747★）、verification-skill-example（225★）、how（1,018★）、hiring-without-whiteboards（53,673★）。


- 彼女の PR 数（月約3,000 本人／約11,000 チーム／revert 約0.5%、2026年11月の AI Engineer 講演「All Code Is Slop (Except Mine)」より）は、すべて自己申告でありベンチマークではない。
- 2026-11-27 朝の報告では、別媒体（7X Journal、Lightcone 回の要約）で「月4,000 PR」という数字も現れた。回によって揺れる数字として扱うことが確定している。この揺れ自体が、後述の Explain the Number 初仕事の対象である。

================================================================
第2層 ── 読み取り基盤: read-social-post スキルと6実験（2026-11-26）
================================================================


- 対象: repo `skills/read-social-post` の SKILL.md、README.md（v002）、references/fxtwitter-protocol.md（文書版 v1.1-review-candidate、2026-11-11 に YusukeJP が採用）、agents/openai.yaml。
- 中核規則:
- SKILL.md は対象判定だけを持ち、手順は統合プロトコルが持つ。
- 旧 Grok 下書きの指示を、独立した現行規則として使ってはならない（形成史である）。
- 適用版は「新しい版がある」ことではなく、現在の Human の指定と採用状態で決まる。
- 通常経路は v2: `https://api.fxtwitter.com/2/status/{id}`（`.status` オブジェクト、reposts は `.status.reposts`）。v1（`/status/{id}`、`.tweet`）は改訂プロトコル内の互換経路であり、退行ではない。
- 成功は HTTP 200 だけでは足りない。ID 一致、オブジェクト非 null、tombstone の区別、冒頭・中間・末尾の連続性を確認して初めて「API 応答上の全文取得」と言える。
- null／欠落／0 を区別する。null を 0 で埋めない。
- メディアは「URL 取得済み」と「内容確認済み」を分ける。
- 失敗時に、対象範囲内の投稿について汎用ブラウザ／ログイン経路へ自動フォールバックしない。
- api.vxtwitter.com は未検証の代替候補（プロトコル §7.3）。
- 日付は既定で JST 報告。
- プロトコル §9.4 の未検証範囲: 長文ポストの完全性、引用・スレッドの完全性、記事の再構成、メディア内容確認、vxtwitter。


- ~/TOOLS.md の fxtwitter 注記は、いまだ旧 Grok 下書きが単独で立っている状態。
- TOOLS.md を改訂する Next Query は 2026-11-26 に提示されたが未封印（YusukeJP は別の作業へ移った）。ウォッチの cron 本文は 2026-11-27 に先行して改訂済み（TOOLS.md ではなくプロトコルを参照する形）。
- この LANE で扱う場合は、TOOLS.md 改訂は未決事項として数えること。


- 実験A（v1／v2 比較、/reframe 発表ポスト 2125029185379008573）: 全フィールド同一（likes 5,099／reposts 290／replies 360／bookmarks 4,581／views 350,216、計測時点）。差は命名と追加キーのみ。
- 実験B（動画、「life before grok @bot」2125041148423229570、37.848秒）: m3u8 と複数 MP4 variant を確認。media.all の URL は最高解像度 MP4 の直接リンク（774×576）。状態は「URL 取得済み、内容未確認」。
- 実験C（引用分離、gardening ポスト 2124525336994177412）: quote オブジェクトが清く分離。Ray Fernando の原ポスト（2124222002076733869、11月21日）の全文924字を取得。「gardening」プロンプト（git log とレビューコメントから繰り返す間違いを掘り、各々を構造→型→lint→テストで不可能にする）が、二次情報から一次確認へ格上げされた。
- 実験D（スレッド／会話）: `/2/thread/{id}` はスレッド配列を返す（単独ポストでは1件）。`/2/conversation/{id}` は返信35件＋ページング用カーソル（全360件ではない）。
- 実験E（X Article 再構成、最大の成果）: 「Automate Anything with Grok Bot」（2123159537016533493、11月18日）の記事本文を content.blocks から再構成。71ブロック／11,744字、冒頭から末尾までの連続性を確認。プロトコル §9.4 の未検証リストの1件が閉じた。方法の要点: goal first, trigger last。伴走ポストは 2123159763626430464（Dr Eggbot v2）。
- 実験F（vxtwitter）: api.vxtwitter.com に到達可能、同ポストの本文・数値が一致。JSON 構造は異なる（フラットなキー）。「未検証候補」から「到達確認済みの代替」へ格上げ可能。
- 併せて実測（2026-11-26 17:52）: 彼女の既知最新ポスト 2125340394938593344（11月24日、「daily driving gemini neon in cursor, it's a good model」）を v2 で取得。likes 17,477／views 922,184（読取時点）、メディアなし。

================================================================
第3層 ── pstack 原典研究（2026-11-26）
================================================================


- pstack v0.15.48（plugin.json: 作者 Lauren Tan、MIT、説明文「if you want to go fast, go deep first. pstack helps you write less, but higher quality code. rigorous agent workflows you can parallelize with confidence.」）。
- スキル総数 59（リポジトリから全列挙）。うち principle-* が 24本（公称「24原則」と一致）。
- 入口 `/pstack:poteto-mode` はルーター。プレイブックは 22本（リポジトリ実測で確定。二次情報の23本は誤り。2026-11-27 に訂正済み）。


- 引用規律: 返信では、判断を形作った原則を名指しする。ただし、そのセッションで leaf の SKILL.md を読んだ原則だけを引用できる。
- モデル配分の既定: コード／文章／判断 = claude-opus-5-5-xhigh-fast。軽い編集 = opus-5-5-high-fast。レビュー／設計パネルの席 = claude-fable-5-2-high、claude-opus-5-5-high-fast、gemini-4-neon-xhigh。
- `/setup-pstack` は `~/.cursor/rules/pstack-models.mdc` を書く（`# defaults: 3` マーカーが再提示の gate。古い rule ファイルは setup を再実行するまで古い項目を保持する）。
- サブエージェントは fresh が既定。「No は正当な答え」。自律性はあるが、不可逆な書き込みでは止まる。


- /reframe（238語）: まず候補となる問題を2〜3個、見分けの徴候つきで挙げる。専門用語を8〜12個、各々に実在のプロジェクト／論文リンクを付けて教える。リンクは全て開き、確認できない引用は切る。隣接分野を2〜3個借りる。言及されなかったものを名指しする。その上で書き直す。手動実行のみ（disable-model-invocation: true）。/poteto-mode からは呼ばれない。
- /sharpen: 大きくではなく深く。4つの質問の後にプロンプトを書き直す。
- /no-comments: 「Comment Sicko」エージェント（agents/comment-sicko.md）を spawn する。制約コメントは、削除の前に型／ランタイム／テスト／CI lint への符号化を申し出る。
- create-formal-verification-skill: 中核規則は「Able to fail（失敗できなければならない）」。一度も失敗したことのないチェックは何も証明しない。各性質が壊れた変種で失敗することを見せる。順序の問題には TLA+ が既定だが、「問いに道具を選ばせる」。
- /statechart: TLA+ モデルを TLC で検査し、読み手の言葉で Mermaid に描く。成り立たせるために規則を弱めない。


- 心臓部は原則「Encode Lessons in Structure」。同じ指示を2回書くことになったら、文章を増やすのではなく、lint／メタデータ／ランタイムチェック／スクリプトとして符号化する。
- レビューより検証: 2026-11-03 のポスト（2117437607940681849、全文読了）で、敵対的レビューは概ねトークンの無駄、代わりに経験的＋形式的検証を、と明言。interrogate は段階的廃止中で、削除の可能性あり。
- 2026-11-08 のポスト（2119521036660314339）で /create-formal-verification-skill と /statechart を発表。steveruizok の「find all of the implicit state machines in my app」を引用。


- pstack README（28KB）、docs/guide と docs/harness の大半、プレイブック本文の大半、interrogate の現行本文。
- ただし docs/harness/claude-code.md と docs/guide の 02／08／09 は第7層のとおり後から読了した。

================================================================
第4層 ── 本質の特定: 5W1H（2026-11-27、YusukeJP が 101/100 と評価）
================================================================


- pstack は速度の道具ではない。「go deep first（まず深く行け）」。エージェントの作業様式を符号化し、仕事が意見ではなく証拠で信頼されるようにする道具であり、それが並列化と自動マージを可能にする条件である。


- 命名の重要性 ↔ /reframe
- 参照は原本へ ↔ 引用規律（読んだ原則だけ引用可）
- 訂正を構造へ ↔ Encode Lessons in Structure
- 失敗は Bottleneck 検出 ↔ Able to fail
- 表情は計器である ↔ Explain the Number


- 5W1H の回答全文は、TOWER の会話履歴にのみ存在する。再利用する前に、元の返信を読み戻すこと（要約からの再構成はしない）。

================================================================
第5層 ── Muse への移植: 第1〜4弾（2026-11-27）
================================================================


- pstack のスキルは SKILL.md（YAML フロントマター＋Markdown）。Muse のカスタムスキルは SKILL.md＋skill.yaml（`~/workspace/custom-skills/` 配下）。形式互換あり。
- MIT ライセンスにより、帰属表示つきの再利用が可能。
- そのまま移植できる: 原則群とテキストのみのスキル。
- 適応が要る: poteto-mode、no-comments、swarm、arena（Cursor の Task／サブエージェント型、モデル slug に依存）。
- 移らない: モデル slug の路由、ベンダー横断のパネルの席、/setup-pstack の.mdc 生成、cursor-team-kit のスキル群。


- フォルダ名は `pstack_<name>`。中身は SKILL.md と skill.yaml の2ファイル。
- SKILL.md は、上流本文を原文のまま収め、その前に頭注ブロックを置く。頭注には: 上流の版（v0.15.48）、出典 URL、「Original by Lauren Tan (@poteto), MIT License」、適応点、を記録する。
- skill.yaml: name はフォルダ名と一致、title、description（一文）、category「Work and knowledge」、include_in_prompt: false。
- 上流の基準テキストは `~/workspace/pstack-port/upstream/` に保存（原則24本全ての SKILL.md、poteto-mode／reframe／sharpen、playbook-authoring-a-skill.md、他に調査で取得したファイル群、計38ファイル）。
- 検証の型: スクリプトによる行照合（上流の本文行が移植側に全て存在するか）。目視に頼らない。


- pstack_poteto_mode（適応版ルーター: 不可侵条項、引用規律、fresh サブエージェント既定、自律性（ただし Muse の承認規則が勝つ）、返信作法を保持。モデル路由／setup／cursor-team-kit は省略。当時の未移植は原則20本超とプレイブック群と明記）
- pstack_principle_prove_it_works
- pstack_principle_encode_lessons_in_structure
- pstack_principle_attack_the_premise
- pstack_principle_laziness_protocol
- pstack_reframe
- pstack_sharpen
- 検証: muse.skill_search で7本全て発見可能。行照合で、原文移植6本の欠落 0。


- pstack_principle_sequence_verifiable_units
- pstack_principle_guard_the_context_window（上流の leaf は実測で約69語と短い。それが原文である）
- pstack_principle_build_the_lever
- pstack_principle_fix_root_causes
- pstack_principle_explain_the_number（頭注に、benchmark-checklist 参照が未移植であることを明記）
- pstack_playbook_authoring_a_skill（プレイブックをスキルとして移植。頭注に Muse 側の置換を2点明記: create-skill → カスタムスキルのテンプレート、「PR を開く」→ verify_repo_writes＋封印の規律）
- 検証: 原則は欠落 0。プレイブックは本文8行のうち1行が見出し記号の差のみ（### が上流、# が移植側。文言は同一）。タイトルは後に「# Authoring or modifying a skill」へ編集。
- ルーター更新: 原則9本＋reframe／sharpen＋authoring プレイブックを引用可能に。未移植は原則15本・プレイブック21本と記載（この時点の数）。


- poteto-mode の規律を、第2弾の設計タスク自体に適用した。
- fresh なサブエージェントが、メインの見解を見ずに独立した優先順位付けを作成（基準: 頻度 × 家の規則との適合 × Cursor 依存の低さ）。
- Prove It Works が、プレイブック総数の誤り（23→22）を捕捉した。
- 観察された効果（正直な記録）: Prove It Works が検証方法を2回変えた（目視→スクリプト照合）。Laziness Protocol が移植範囲の最小化を形作った。Build the Lever ── 移植手順自体が再実行可能な道具になった。Sequence Verifiable Units が第2弾の構造になった。Guard the Context Window は委任によって行使された。
- 未発動のまま: Explain the Number と Fix Root Causes は、この時点では実タスクで未発動（第11層の候補参照）。


- pstack_principle_separate_before_serializing_shared_state
- pstack_principle_minimize_reader_load
- pstack_principle_never_block_on_the_human（適応必須: 本文の冒頭に日本語の適応注記を配置。可逆な内部作業にだけ効くこと、GitHub 書き込み・送信・購入・削除は従来どおり封印が必要なこと、意味と最終判断は YusukeJP のものであること、を明記）
- pstack_playbook_investigation（頭注: why／unslop への参照は未移植の上流参照であること）
- pstack_playbook_session_pickup（頭注: Cursor の transcript パスを Muse の読み替え（チャット履歴・メモリ・ワークスペース）に置換する旨を明記。引用する原則2本は移植済み）
- 検証: 原則3本は欠落 0。プレイブック2本は見出し記号の差のみ。
- ルーター更新: 原則12本が引用可能、プレイブック3本を路由。未移植は原則12本・プレイブック19本と数え直し。


- 移植しないと決定: autopilot-full（自動マージが封印制と正面衝突）、autopilot-stack（バンドルごとの封印と二重管理）、worktree-cleanup（Cursor の worktree 専用で、Muse にトリガーが存在しない）、runtime-forensics（Muse に無い計装基盤が必要）、trace-forensics（対象物にほぼ遭遇しない）。
- 第2波: 原則 subtract-before-you-add、make-operations-idempotent、foundational-thinking、model-the-domain。プレイブック pause-safely、multi-phase-plan、prototype、eval、bug-fix。
- 保留: 原則 redesign-from-first-principles、outcome-oriented-execution、boundary-discipline、experience-first（判断が YusukeJP 自身の領域に近い）、exhaust-the-design-space、test-behavior-not-implementation、type-system-discipline（デッキは概ね型なし JS）。migrate-callers-then-delete-legacy-apis は最下位（呼び出し側の問題が repo にほぼ無い）。プレイブック refactoring、feature、hillclimb（2MiB スリム化）、visual-parity（レンダラ B0 修正まで保留。画像 diff が実行できない）、opening-a-pr（部分利用のみ:「Why から始める」は push バンドルに移る。PR 自体は作らない）、shipping／babysit（PR 文化のため保留）、perf-issue、autonomous-run（述語で定義された完了は学ぶ価値あり）。
- 選定軸（YusukeJP へ明示した）: 「そのトリガー条件が、我々の暦に実在するか」。派手さではない。

================================================================
第6層 ── 差分更新の方針（2026-11-27 に設計し、YusukeJP が封印）
================================================================

「差分を Update する感覚はどれくらいがベストか？」への回答として設計し、採用された方針。
- 検知は毎日（朝のウォッチの中。追加コストほぼゼロ）。
- 報告は、移植したスキルの上流本文が実際に変わった時だけ。意味の変わる変更か、字句だけかを分類する。版だけ上がって移植分に変更がなければ1行。
- 移植への反映は自動ではない。差分はメインで封印用に用意し、最大で週1回にバッチする。
- 同日期外: poteto-mode または原則への意味変更、移植済みスキルの削除・改名は、その日に報告する。
- 実装: cron `poteto-pstack-daily` の本文ステップ4として組み込み済み（2026-11-27 に2回更新）。レジストリはウォッチの state.md 内。

================================================================
第7層 ── poteto-mode 重点調査（2026-11-27、YusukeJP の指示「poteto-mode が pstack の入り口なので重点的に」）
================================================================


- 構成: Non-negotiables（状況→行動のトリガー表。「分岐を実験で決着できるなら、聞かずに試作せよ」まで明記）／Principles（24原則のインデックス＋引用規律）／Autonomy／Subagents（fresh 既定、役割ごとのモデル配分、パネルは別ベンダーで第二意見）／Writing the reply（短い宣言文。主張には証拠かラベル: measured／inferred／guess）／Playbooks（22本へ路由し、手順を todo に写してから動く）。


- 呼び名は「front door（表玄関）」。人間は目標だけを言う。
- 良いプロンプトの5要素: 目標／完了条件（合否が付くもの）／見たい証拠／既に知っていること／本当の制約。
- 言い直し（restatement）が誤読の検出器。コードが存在する前に、1メッセージで直せる。
- 最大の pitfall: プロンプトにスキルを列挙するな。順序はプレイブックが持つ。人間が書いた順序は大抵ステップを落とす。
- 省くべきもの: やり方（how）と原因の自説。先に言い直しをさせてから自説を出す。


- 委任先は作業前に poteto-mode の SKILL.md を全文読む。
- ファイルは ~/.cursor/plugins/ 内を検索し、plugin.json の版が最高のものを採用する。
- 汎用エージェント（generalPurpose）で代用すると「drift（漂流）」と明記されている。
- runner と delegate の分離は 2026-10-12 の commit で確立。


- 生成物は `~/.cursor/rules/pstack-models.mdc`（役割→モデルの対応表、alwaysApply）。
- budget の梯子: large／medium／small で推論の深さを役割一括で上下させる。上限は xhigh。
- `# defaults: 3` マーカー: 設定ファイル自体に既定値の世代番号を刻む。
- 旧既定値の移行規則: 古い世代の既定値は再実行時に規則として書き換える。ただし利用者が選んだ値は絶対に触らない。既定値と選択の区別が条文で守られている。
- これは我々の「版の化石化」への彼女の解法である。版を刻み、移行を規則化し、人の選択は保存する。


- /no-comments が spawn する、コメント嫌いの人格を持つエージェント定義。残してよい例外のリストが「唯一の綱」として明記されている。


- 2026-09-23: 規則の衝突を解消し、モデル rule の読み方を統一。
- 2026-10-03: fresh subagents を導入、explain-the-number を移植（上流内での動き）。
- 2026-10-10: プロンプトを蒸留してトークン削減。
- 2026-10-12: runner／delegate 分離、leaf スキルの所在を明示。
- 2026-10-15: 原則を「規則」から「推論」へ書き直し（4原則）。
- 2026-11-16: 短縮＋worker.md＋Opus-first 路由、上限 xhigh。
- 2026-11-19: Gemini の席を Gemini 4 Neon へ、次いで neon-xhigh へ。
- 一貫した方向: 短く、推論として、上限つき。


彼女が Muse 系環境に期待すること:
- 名前対応表をセッション冒頭に一度だけ読む。
- 対応できない項目は落として宣言する。黙って代用しない。
- スキルの原典はローカルで読む。ネットから取得し直さない。
- モデル名は役割ごとに翻訳する。
- 設定ファイル（~/.claude/rules/pstack-models.md）は毎セッション自動で読まれる前提。
- ベンダー専用のステップは1行で飛ばして宣言する:「Skipped in Claude Code: <step>. <reason>.」止まらない。
- 委任は型と分離の仕方で翻訳する。
- トランスクリプトの所在は ~/.claude/projects/<slug>/<session>.jsonl。自分のワークスペースだけ。


- 08（原則）: 原則は24本、我々の移植は12本。未移植の例は Subtract Before You Add、Test Behavior Not Implementation。彼女自身の例文にこの2本が登場する。彼女の姿勢は「リストを暗記するな」。原則は引く辞書であって覚える対象ではない。これは YusukeJP の「命名の重要性」と同じ形（名前を付けて引けるようにする）。
- 09（自分のものにする）: /automate-me、/reflect、/correct、eval プレイブック、検証スキルの生成、/technical-writing から成るループ。我々の移植には丸ごと無かった。最大の欠落は /correct と eval。


1. Playbooks の節がない（todo へ写す手順、figure-it-out への逃げ道）。
2. Muse 用のアダプタ文書がない。
3. 「1行で飛ばして宣言する」規則がない。
4. 「委任先はまずルーター全文を読む」規則がない。
5. 役割→モデルの配分がない（意図的に省略したが、Muse 側の代替が未記録）。
6. 原則が12／24本。
7. ガイド09のループが丸ごと無い。
8. Non-negotiables のトリガーの多くが未移植スキルに依存（行き先のないトリガー）。

================================================================
第8層 ── 第4弾: 設計・方向の訂正・実行（2026-11-27）
================================================================


- 不足 #2／#3／#4 を束ねた「Muse アダプタ文書」を1枚に起案（起案は ~/workspace/pstack-port/adapter-draft.md に保存済み。後にスキル化した）。
- ルーターへの #1 差分: Playbooks 節の新設。
- /correct の判断: 移植可（適応つき）、価値は高い。Skill LANE の Case 修理の一般形であり、新しい価値は「規則↔執行者の対応表を1箇所に持つこと」。
- eval の判断: 移植可だが重い。大きなスキル改訂の採否を決める時だけ使う道具。


- 設計時の私の案は「figure-it-out が未移植なので、フォールバックは引用でなくルーター内に短く内蔵する」だった。
- YusukeJP の指摘: スキルを移植する方が正しい方向（ベクトル）ではないか。
- 判定: YusukeJP が正しい。引用を消すのではなく、行き先を作る。これは「AI 提案は種＝ベクトル」の実例であり、私の設計の弱点は、目先の整合性を取って移植という本筋を避けたことだった。以後、行き先のない参照に当たったら、内蔵でなく移植を第一候補にする。


- pstack_figure_it_out（648語。行照合で欠落 0）
- pstack_correct（435語。欠落 0）
- pstack_playbook_eval（414語。見出し記号の差のみ。頭注に Muse 側の置換を明記: arena は未移植なので局面を直接回す、別ベンダーのジャッジは不可で fresh なサブエージェントで代替し、その限界を報告に宣言する、transcript の所在はチャット履歴と実行記録）
- pstack_muse_adapter（Muse の原作文書。claude-code.md が手本。Tools／Subagents／Models／Paths／Skip 規則の5節。モデル指定が Muse では露出していないこと、ベンダーの多様性は代替不可であることを、正直に宣言する形にした）
- ルーター更新: Playbooks 節を新設。一致したプレイブックの手順を todo へ写してから始めること、一致なし・大規模は Figure It Out へ「引用で」路由すること、路由前にアダプタを一度読むこと。未移植の残数は原則12本・プレイブック18本。


- 完了の定義を反証可能な述語で書く。
- 検証ハーネスは、変更前の基準値つきで先に作る。
- 判定は VERIFIED／NOT VERIFIED／INCONCLUSIVE の3値。「inconclusive は合格ではない」。
- 未移植の参照（foundational-thinking、architect、arena、show-me-your-work）は頭注に明記。


- 同じ訂正が2回起きたら「クラス」と数える。
- 直す階層: 構造（architecture）→ 型 → lint（エラーが直し方を名指しする）→ テスト → 文書は最後。
- 各チェックが「本物の過去の間違い」で失敗することを証明する（Able to fail と同型）。
- 最後に、規則↔執行者の対応表をエージェントの指示ファイルに保つ。規則があったのに執行されていなければ、それは再発であり、同じ変更の中で階層を上げる。間違いが起きえなくなったら規則を落とす。

================================================================
第9層 ── 対応表の置き場の決定（2026-11-27、YusukeJP の決定2件）
================================================================


- 経緯: 私の Next Query の「AGENTS.md」が曖昧だったため、YusukeJP が「どこの AGENTS.md か？」と確認した（この確認自体が、クラス3＝対象の取り違えの実例である）。
- YusukeJP の決定: GitHub 側ではなく Muse 内が良い。理由は「GitHub 側は多くの AI が絡んでいるから」。
- 根拠の対応: 変更境界（2026-11-07、複数の AI が同じ場所を編集することがバグの大きな源）と、原則 Separate Before Serializing Shared State（各アクターに自分のファイルを持たせる）の適用そのもの。
- 却下した案: repo 側を本命にすること。共有地では、誰の訂正の表か分からなくなる。


- YusukeJP の指摘: 最重要要件「Muse がリセットされても agents/muse から復元できること」のため、鏡が要る。
- 前例: アバター（ローカル本命＋repo のバイト同一コピー）、移行プロトコルの「生存に必須の素材は二重に運ぶ」。
- 方向の固定: 編集は常にローカル。repo は復元専用の鏡。ローカル→repo はバンドル時に写す。repo→ローカルは、ローカル喪失時にだけ逆流する。


- GitHub 側に pstack 本体をクローン的に丸ごと入れる意味は薄い。本体は Lauren の GitHub そのものであり、複製は版の化石化を招く（原則: 参照は原本へ）。
- バックアップの価値はカスタムの量に比例する。仕分け:
- 最高: pstack_muse_adapter（完全な原作）、移植の方法＋レジストリ（再建の設計図）
- 高: pstack_poteto_mode（適応版ルーター）、never_block_on_the_human（日本語の適応注記）
- 中: 頭注に小さな適応がある7本（figure_it_out／correct／eval／session_pickup／investigation／authoring_a_skill／explain_the_number）
- なし: 原文のままの移植（本体は上流。再導出できる）

================================================================
第10層 ── /correct 初版とバックアップ束の実行（2026-11-27、figure-it-out 初適用）
================================================================


- figure-it-out の最初の実タスクとして、このバンドル自体を選んだ。Phase A で完了述語を先に固定し、判定つきで報告した。


1. ~/AGENTS.md に対応表があり、各クラスに執行者が付いている ── VERIFIED
2. repo agents/muse/pstack-backup/ に5ファイルが存在する ── VERIFIED
3. push は1回、認識は1回 ── VERIFIED（承認カード1回で通過）
4. 読み戻した5ファイルの MD5 がローカルと全て一致 ── VERIFIED（5／5 一致、commit 0116fda1）


1. 検証範囲の過大報告 ── デッキ一式の件（2026-11-03、YusukeJP のスクショで発覚）、CONTROL v015 の主張不一致（ハッシュ照合で発覚）。執行者: verify_repo_writes＋読み戻し照合。
2. 暗黙の承認を実行許可と読む ── 期限つきリンク共有の方向、ブラウザ投稿の方向（いずれも訂正済み）。執行者: 封印の規律。
3. 対象の取り違え ── 2026-11-05 に2回、11-06 に1回。執行者: 未だ構造的なものが無い。表の中で「最弱の行」と明記した。
4. 揮発性情報の化石化 ── yomiyasu のピン（2.5.0、上流は 3.1.0）、質問数の二重所有、プレイブック23本の誤伝。執行者: 参照は原本へ＋揮発性数値の単一所有。
5. 判断事項を散文に埋める ── 2026-11-03「判断事項がわかりづらい！」。執行者: 判断Task の書き出し形式。
6. 新規ファイルの安易な提案 ── LANE.md 分離案と共通 LANE.md（2026-11-15 に2回却下）。執行者: 既存ファイルで担えないことの証明＋例外一般化テスト。
7. GitHub 書き込みの散発と承認失効 ── 2026-11-06 のタイムアウト等。執行者: Standard 003（1バンドル1 push、認識数を先に述べる）。


- README.md: 入口＋移植レジストリ（22本）＋再建手順（上流からの再導出手順6ステップ）。
- muse-adapter.md: アダプタの鏡。
- poteto-mode.md: 適応版ルーターの鏡。
- never-block-on-the-human.md: 適応注記つき原則の鏡。
- rule-table.md: 対応表の鏡。
- 各ファイルは repo の作法どおり、YAML フロントマター（title／version／canonical_path／role／status／created／updated／repository／expected_eof）と EOF マーカーを持つ。


- クラス3だけ執行者が「表の行自体」しかない。/correct の作法では、これは「規則はあるが執行されていない＝再発扱い」であり、次に同じ訂正が来たらその場で階層を上げる約束として表に書いた。
- 述語4／4 VERIFIED は、述語が機械照合できる形だったからである。述語の設計自体の甘さは、YusukeJP の目が最後の検証である。

================================================================
第11層 ── クラス3の執行者: 設計3案（2026-11-27、提示済み・未採用）
================================================================


- クラス3の失敗は「指示の代名詞や範囲語に、生きている候補が2つ以上ある時」に起きる。執行者は、その瞬間に機械的に挟まるものでなければならない。


- 案A「言い直し先行」: 候補が2つ以上ある指示では、返信の冒頭1行で「対象は X として進めます」と名乗ってから作業に入る。長所: コスト1行、YusukeJP が一目で誤りに気づける、彼女のガイドの「言い直しは誤読の検出器」と同じ型。短所: 止める力はない。検出は YusukeJP の目に依存。
- 案B「選択肢で固定」: 候補2つ以上＋間違うと高くつく時（書き込み・push・長時間作業）だけ、タップ式の選択肢を出してから始める。長所: 構造的に止まる。短所: 対話が1往復増える。多用すると読まずにタップする習慣を育てる危険。
- 案C「todo 冒頭の候補列挙」: todo の1項目目を「対象の確定: 候補 A／B、本命は A（根拠つき）」にする。長所: 追加の対話ゼロ、todo は常時見える。短所: 作業は始まってしまう（検出は開始後）。


- A を既定にし、B を高コストの時だけ重ねる二層。C は A と重複する割に止める力が弱いので落とす。
- 理由: クラス3の失敗の大半は読み取りと下書きの範囲で起きており、そこでは1行の言い直しが一番安く効く。書き込みが絡む時だけ B の停止力が要る。


- 執行者は「A 既定＋B は高コスト時」の二層でよいか。それとも A のみ／B のみか。
- 採用されたら、対応表のクラス3行を更新する（最弱の行が、執行者を持つ行になる）。更新先は ~/AGENTS.md 本命＋repo 鏡（次のバンドルで）。

================================================================
第12層 ── 現在の運用状態と未決事項（次への interface）
================================================================


- 朝のウォッチ: cron `poteto-pstack-daily`、毎日 9:40:18 JST、メインへ配信。確認順序は (1) pstack 本体 (2) @poteto の新ポスト（read-social-post プロトコル、v2 優先） (3) 関連報道 (4) 移植22本の差分チェック。報告は日本語、表形式（表1: 新ポスト＝日付｜ポスト｜意味、表2: pstack 変更＝版｜変更｜意味）、解釈は1行、未確認は別節。静かな日は1行。
- 差分方針: 第6層のとおり（検知は毎日、報告は移植分の本文が変わった時だけ、反映は封印つきで最大週1バッチ、同日期外あり）。
- 状態ファイル: `~/workspace/goals/lauren-tan-poteto-pstack-daily-watch/hidden_files/state.md`（基準、既読ポスト ID、移植レジストリ第1〜4弾）。
- 日次ログ: `~/memory/2026-11-27.md` に本日の全記録がある。前日分は `~/memory/2026-11-26.md`。
- 2026-11-27 朝の報告（配信済み）: 新規なし。pstack は v0.15.48 のまま、@poteto の新規投稿なし。PR 数の自己申告は 3,000〜4,000 と揺れる数字として扱う、と解釈を付けた。


- Explain the Number → Lauren の PR 数 3,000↔4,000 の揺れを辿る（定義・母数・除外・期間）。「驚き」は今朝の報告で既に発生済み。原則の定義そのままの初仕事になる。
- Fix Root Causes → レンダラ B0 の根本原因調査。2026-10-30 から playwright／chromium が故障したまま、jsdom＋実機確認という回避で税金を払い続けている最古の未解決。直れば Visual Parity プレイブックの保留も解ける。直らなくても「この VM では直らない」と証明できれば、回避が正式な設計になる。


1. 判断1: クラス3執行者の採用形（第11層）。採用後は対応表の更新までが仕事。
2. Explain the Number 初仕事: PR 数の定義・母数・期間を原典で辿り、表で報告する。
3. Fix Root Causes 候補: レンダラ B0 の根本原因調査（範囲の確定は YusukeJP と）。
4. ウォッチ配信先の移管: 現在はメイン配信。この LANE への移管可否は YusukeJP の判断事項。
5. TOOLS.md の fxtwitter 注記の改訂（第2層。2026-11-26 に Next Query 提示済み・未封印）。
6. 移植の残: 原則12本・プレイブック18本は第2波と保留の区分のまま（第5層）。暦では進めず、出番が来たものから拾う。移植しない5本の決定は確定済み。
7. @poteto の /no-comments 引用ポスト: 本人のポストを status ID で直接読めていない（二次情報2件で文言は裏付け済み）。未確認のまま保持すること。
8. ガイド 08／09 の GitHub 原典との逐字照合（ミラー読みのまま未実施）。


- 実行は YusukeJP の封印がある時だけ。提示・称賛・過去の承認は実行許可ではない。
- GitHub 書き込みは 1バンドル1 push、認識数（= 1＋削除数）を先に述べる。変更の自由領域は agents/muse 内だけ。
- 返信は 🌱Next Step🧭 と 🔑Next Query📩 で閉じる。Next Query は箇条書き、1項目1仕事で、複数の問題を束ねる（Big Bang の型）。
- yomiyasu-switch は常時 ON。返信の1行目は 📖yomiyasu: ON。表は表のまま保つ。
- 事実／解釈／未確認を分ける。数値は一次情報源から。自己申告は自己申告と明記する。
- 呼び名は YusukeJP。🦣 は文頭に置く。

================================================================
第13層 ── 索引: ファイル・パス・ID
================================================================


- 移植22本: `~/workspace/custom-skills/pstack_*/`（各 SKILL.md＋skill.yaml）
- 上流の基準テキスト: `~/workspace/pstack-port/upstream/`（38ファイル）
- アダプタ起案の原稿: `~/workspace/pstack-port/adapter-draft.md`（スキル化済み。形成史として保持）
- 対応表の本命: `~/AGENTS.md` の「Correction rule table (pstack /correct, v1 — 2026-11-27)」節
- ウォッチの状態: `~/workspace/goals/lauren-tan-poteto-pstack-daily-watch/hidden_files/state.md`
- 本書の控え: `~/workspace/goals/lauren-tan-poteto-pstack-daily-watch/hidden_files/migration-to-pstack-lane_2026-11-27.md`
- 日次ログ: `~/memory/2026-11-26.md`、`~/memory/2026-11-27.md`
- 人物ファイル: `~/memory/people/lauren-tan.md`


- バックアップ束: `agents/muse/pstack-backup/`（README.md／muse-adapter.md／poteto-mode.md／never-block-on-the-human.md／rule-table.md、commit 0116fda1）
- 読み取りスキル: `skills/read-social-post/`（SKILL.md／README.md v002／references/fxtwitter-protocol.md v1.1-review-candidate／agents/openai.yaml）
- 上流: cursor/plugins の pstack/（plugin.json の版が基準。v0.15.48、最新上流コミット 9e278fe）


- pstack LANE の chat_id: f678e707-8b1f-4986-8998-d2c34470a753
- cron: poteto-pstack-daily（毎日 9:40:18 JST、owner は goal:lauren-tan-poteto-pstack-daily-watch、goal_id goal_de158f3959c3）
- 移植の累計: 第1弾7＋第2弾6＋第3弾5＋第4弾4 ＝ 22本
- 基準版: 上流 pstack v0.15.48（移植の基準）。ウォッチの起点は v0.15.46（2026-11-20）

EOF::AI_MAMMOTH_PSTACK_LANE_MIGRATION::v001
