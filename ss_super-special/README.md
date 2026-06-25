# ss_super-special

## 0. Executive Compression

`ss_super-special/` は、Ark Projectにおいて、全AI・全AI Projectが参照すべき **Ark-wide / Super-special Artifact** を置くための最上位Special層である。

短く言うと：

```text id="u7n4ca"
ss_super-special/ は、
重要そうなものを何でも置く場所ではない。

Ark全体を軽くし、
全AIが再起動でき、
複数Projectに効く超重要Artifactだけを置く場所である。
```

このfolderの最初の中核Artifactは：

```text id="xjsjwa"
artifact-to-github.md
```

である。

---

## 1. What this folder is

`ss_super-special/` は、単一Threadや局所Workflowの成果物置き場ではない。

このfolderは、Ark全体に効く共通Card・共通Rail・責務分離Artifact・Complexity Sinkを置く場所である。

```yaml id="gq4db8"
folder_role:
  name: "ss_super-special"
  role:
    - "Ark-wide Core Artifact layer"
    - "Super-special Folder Gate"
    - "Common Rail holder"
    - "Complexity Sink holder"
    - "Future AI Reboot Surface"
```

日本語で言えば：

```text id="q1hoc7"
ここは、Ark全体の構造を軽くする超重要Artifactの住所である。
```

---

## 2. Entry Rule

このfolderには、何でも入れてはいけない。

### 2.1 入れてよいもの

```yaml id="en1g8v"
allow:
  - "全AI・全AI Projectが参照すべき共通Artifact"
  - "複数Workflowを軽くする責務分離Card"
  - "Ark全体のComplexity Sink"
  - "共通Rail / Common Card / Shared Guard"
  - "Future AIが初期参照してよい超重要Markdown"
  - "単一Threadを超えて再利用されるInfrastructure Artifact"
```

### 2.2 入れてはいけないもの

```yaml id="if9dfu"
do_not_allow:
  - "通常Thread成果物"
  - "一時Patch Candidate"
  - "局所Mission Card"
  - "単一Threadだけに効くHarvest"
  - "まだ成熟していない思いつき"
  - "重要そうに見えるだけのMarkdown"
  - "保存先に迷っただけのFile"
```

圧縮：

```text id="wxgr82"
ss_super-special/ は、重要度のゴミ箱ではない。
Ark-wideに再利用される超重要Coreだけを置く。
```

---

## 3. Current Artifacts

## 3.1 `artifact-to-github.md`

```yaml id="uzvttv"
artifact:
  path: "ss_super-special/artifact-to-github.md"
  role:
    - "GitHub化Markdown Card"
    - "Artifact-to-GitHub Card"
    - "Ark-wide Complexity Sink"
    - "Generation Rail / Promotion Card separation"
```

`artifact-to-github.md` は、完成済みArtifactをGitHubへ置くための共通Cardである。

ただし、本質はGitHub操作そのものではない。

```text id="kta9br"
artifact-to-github.md の本質は、
全AI・全MarkdownからGitHub化責務を切り離し、
生成RailをSimple is bestへ戻すことである。
```

三者分担：

```text id="uf3cm9"
Artifact Generators:
  作る。

artifact-to-github.md:
  置く。

Human:
  座標をSealする。
```

---

## 4. Why `artifact-to-github.md` belongs here

`artifact-to-github.md` は、単なる便利Markdownではない。

このCardは、Ark全体に次の変化をもたらす。

```yaml id="qrw08b"
why_super_special:
  - "全AI・全MarkdownがGitHub化責務を委譲できる"
  - "GitHub化の複雑性を一枚へ隔離できる"
  - "Thread-End / Mission / Index / Harvest / Handoffなどを軽くできる"
  - "Artifact-First, GitHub-LaterをArk全体へ適用できる"
  - "Human-Sealed exact path with filenameによってAIの推測を止められる"
```

つまり：

```text id="y8k4mp"
artifact-to-github.md は、
GitHubへ保存するためだけのMarkdownではない。

全MarkdownをGitHub保存責務から解放するMarkdownである。
```

---

## 5. Misread Guard

このfolderを以下のように誤読しない。

```yaml id="eqkziu"
do_not_read_as:
  - "何でも重要そうなものを入れる場所"
  - "Thread成果物の上位保存先"
  - "一時Patch Candidate置き場"
  - "特殊Fileの雑多な倉庫"
  - "AIが勝手に重要度を決めて置く場所"
```

正しくは、こう読む。

```yaml id="wqg8n8"
must_read_as:
  - "Ark-wideに効く超重要Artifact層"
  - "全AI・全AI Projectが参照してよい共通Core"
  - "複雑性を正しい場所へ隔離するためのFolder"
  - "Future AIが再起動できるReboot Surface"
```

---

## 6. Root / Fruit Guard

このfolderも、このfolder内のArtifactも、Rootではない。

```yaml id="i6fsts"
root_guard:
  root:
    - "主イェシュア・ハマシア"
    - "主イェシュアの聖なる血潮"
    - "Teshuvah / 悔い改め"

  fruit:
    - "ss_super-special/"
    - "artifact-to-github.md"
    - "Markdown"
    - "GitHub"
    - "Full Rail"
    - "OKF"
    - "Common Card"
    - "Complexity Sink"
```

Guard：

```text id="oug8e2"
FormatはFruit。
MarkdownはFruit。
GitHubはFruit。
Rootは主イェシュア・ハマシア。
```

AIの役割：

```text id="m7ci44"
AIは地図を描く。
AIは聖霊ではない。
Humanが主の前でSealする。
```

---

## 7. Folder-level Operating Rule

`ss_super-special/` に新しいArtifactを追加する時は、以下を確認する。

```yaml id="fb6o72"
folder_operating_rule:
  before_add:
    - "これはArk-wideに効くか？"
    - "複数Workflowを軽くするか？"
    - "Future AIが再起動するために必要か？"
    - "通常folderではなくここに置く理由があるか？"
    - "Super-special Fogを増やしていないか？"

  if_unclear:
    - "Plan Modeで止める"
    - "READMEのEntry Ruleに照らしてLiving Reviewする"
    - "AIが勝手に追加しない"
```

---

## 8. Final Compression

```text id="kl1t01"
ss_super-special/ は、
Ark-wideな超重要Artifactの場所である。

ここは、重要そうなものを何でも置く場所ではない。

入れてよいのは、
全AI・全AI Projectが参照し、
複数Workflowを軽くし、
Future AIが再起動できる共通Coreだけである。

現在の中核Artifact:
  artifact-to-github.md

artifact-to-github.md は、
全AI・全MarkdownからGitHub化責務を切り離す
Artifact-to-GitHub Cardである。

FormatはFruit。
Rootは主イェシュア・ハマシア。
```
