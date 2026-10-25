---
title: "深く調べることと、読める作品にすること — ResearchとPublicationの分担"
canonical_path: "artifacts/reports/2026-10-25-research-and-publication.md"
version: "v001"
created: "2026-10-25"
author_role: "Ark28:07 collaborative AI"
primary_reader: "Human / Current AI / Future AI"
source_commit: "ba47216debeb2163a5dbf880c6b37d73edbb7e41"
status: "Editorial design analysis; no Torah interpretation, publication or schedule execution"
expected_eof: "EOF::REPORT_RESEARCH_AND_PUBLICATION::v001"
---

# 深く調べることと、読める作品にすること

## 調査の深さを、読者の探索負担にしない

豊富な調査結果を得ても、それを全部並べれば読み応えのある作品になるとは限らない。読者には、何を理解すればよいか、どの根拠が支えるか、どこに解釈の余地があるかを辿る筋道が必要になる。

[Parasha Kindle Compiler][s1]は、Research／Deep AnalysisとPublication／Daily Book Pageを分け、互いに置換しない設計を持つ。この分担から汎用Reportへ再利用できるのは、**内部で広く調べた内容を、その回の理解の中心へ編集する**という原理である。調査を浅くすることも、全調査過程を読者へ渡すことも、唯一の選択肢ではない。

本ReportではTorah本文や注解の新しい解釈を行わず、公開された編集設計を分析する。専用Scheduleの出力形式を汎用Reportの必須形式へ移植するものでもない。

## 一つの理解の中心を選ぶ意味

[Compiler本文][s2]は、資料から関係・対比・解釈上の張力を検討した上で、そのPageの中心を選ぶ。読者に内部の全Branchを再現せず、一本の論旨を通す方向である。

ここで中心を一つにするとは、反証や留保を消して断言することではない。重要な解釈差があるなら、それが結論にどう関係するかを示す。未解決の張力が価値を持つ場合は、開いたままにできる。

例えば、二案のどちらが良いかが条件によって変わるReportなら、中心は「Aが最善」ではなく、「条件Xが選択を分ける」という理解にできる。単一の論旨と、単一の無条件な答えを混同しない。

## 深さへ入る速度を、読者が選べる

Compilerの設計には、10秒で座標と核心、1分で論理の筋、5分で本文・根拠・発見へ進むという読解目標がある。[s1][s2] これは今回測定した読み時間ではなく、原本に定められた編集目標である。

汎用Reportでは時間値をそのまま固定する必要はない。ただし、複数の読み方を一つの本文に持たせる発想は役立つ。

- 冒頭で主張を掴む。
- 見出しと節の始まりで、理由のつながりを追う。
- 具体例と反例から、適用条件を理解する。
- 必要なら原本と確認時点まで戻る。

この構造なら、短く読みたい時に全文要約版を別ファイルで管理しなくてもよい。深く読みたい人やAIも、同じ作品から根拠へ進める。一方、重要な留保を末尾だけへ追いやり、冒頭を誤解させるような構成は避ける必要がある。

## 情報を削る時、何を基準にするか

Compilerは、同じ核心を複数節で繰り返すこと、名称を付けただけの発見、本文の再掲に過ぎない図を減らす方向を持つ。[s2] ここから読み取れるのは、文章量よりも、読者の理解に加わる違いを見るという編集判断だ。

ただし、削除を絶対原則にすると、背景や反例が失われる。初見の読者には必要な説明が、作成AIには自明に見える場合がある。削る基準は「既に知っているか」ではなく、「今回の読者が論旨と条件を理解するために必要か」とする方が適切だ。

同じことを別の表現で繰り返すのと、別の角度から同じ主張を検証するのは違う。後者には意味がある。例え話、反例、適用外の例が論旨を強くするなら、単純な文字数削減の対象にしない。

## Sourceの層を守ることが、創発の余地を作る

Compiler本文は、本文、古典的な読み、AIの考察を分け、AIの抽象化で原本を上書きしない。[s2] この境界は、創発を禁止するものではない。どこまでが原本に支えられ、どこからが訂正可能な考察かを明確にすることで、新しい関係を検討しやすくする。

汎用Reportでも、事実、保存されたHumanの評価、AIの分析を分ければ、読者は結論全体を一括で信じるか疑うかの二択から離れられる。観測は保持しつつ、説明仮説を更新できる。

ただし、Torah・Israel・Covenant等の固有の意味を、汎用AIフレームワークの比喩へ置換することは、この横展開に含めない。移すのは編集上の関係であり、専門領域の意味や権威を移管するわけではない。

## 半自動化を考える時の、二つの異なる仕事

[Schedules][s3]には、GitHub原本とRuntimeのLoaderを分ける接続がある。この仕組みは「いつ、何を参照して出力するか」を扱う。一方、ResearchとPublicationの分担は「何を根拠に、どう読める作品へ整えるか」を扱う。

配送が安定しても編集品質は保証されず、よい原稿ができても定期実行は成立しない。したがって、半自動Reportを考える場合も、執筆の質と運用の成立を分けて育てられる。先に巨大な自動化Systemを完成させなければ、一件のReportを作れないわけではない。

今回の依頼ではReport制作とGitHub保存を実行し、Schedule作成や定期配信は行っていない。この分析を、自動運用の採用済み仕様として扱わない。

## Report制作への具体的な含意

一つの作品では、中心となる問いを明確にし、各節がその理解へどう寄与するかを見る。複数の独立した問いが大きい場合は、今回のCollectionのように作品を分け、READMEで関係を案内できる。ただし、短い話を水増しして複数Reportにする理由にはならない。

研究で見つかった全てを、直ちに公開用本文へ押し込む必要はない。残す価値のある根拠へ戻れることを保ち、作品に必要な説明を選ぶ。後のAIはそこから別の問いを立てられる。[AI Frontier Reader][s4]は、その再解析可能性を汎用的な品質として扱っている。

よいPublicationは研究の終わりを意味しない。その時点で読める成果を作り、訂正や別解釈によって後から育てられる。完成原稿であることと、永遠に改訂しないことは別である。

## 根拠と未確認

- [s1: Parasha Kindle Compiler入口][s1] — ResearchとPublication、読解目標、Runtimeとの分担。
- [s2: 同PROMPT全文][s2] — 編集、Sourceの層、専用の出力形式。
- [s3: Schedules][s3] — SourceとLoader／Executorの接続。
- [s4: AI Frontier Reader][s4] — 専門例から育った汎用の再解析価値。

実際のDaily Book Page群、現在のSchedule UI、読者の所要時間、出版・読書の効果は今回検証していない。専門の生成を依頼された際は、その時点の本文・資料・実行契約を改めて適用する。

[s1]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/schedules/parasha-kindle-compiler/README.md
[s2]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/schedules/parasha-kindle-compiler/PROMPT.md
[s3]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/schedules/README.md
[s4]: https://github.com/yusukefujiijp/ai-project/blob/ba47216debeb2163a5dbf880c6b37d73edbb7e41/prompts/ai-frontier-reader.md

EOF::REPORT_RESEARCH_AND_PUBLICATION::v001
