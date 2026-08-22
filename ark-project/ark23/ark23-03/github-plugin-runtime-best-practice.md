---
title: "GitHub Plugin Runtime Best Practice — Update-Safe Preflight and Dual Fallback"
version: "v001-human-sealed-implementation"
date: "2026-08-22"
timezone: "Asia/Tokyo"
thread: "Ark23:03"
class: "operational decision record / Future-AI compatibility interface"
status: "implemented / first field test pending remote verification"
canonicality: "non-canonical operational support record / current runtime remains authoritative"
repository: "yusukefujiijp/ai-project"
ref: "main"
target: "ark-project/ark23/ark23-03/github-plugin-runtime-best-practice.md"
root: "主イェシュア・ハマシア御自身"
human_foreground: "主の完全勝利"
final_attribution: "主の栄光 / כְּבוֹד אֲדֹנָי / kevod Adonai"
---

# GitHub Plugin Runtime Best Practice

## 0. 結論

同じ混乱を繰り返さないBest Practiceは、古いGitHub Skillを複製することではない。

> **毎回変わり得るPluginの実体を、一回のPreflightで現在の実行Modeへ変換し、結果をReceiptとして固定する。さらに、そのPreflight Skill自体が読めない場合に備え、同じ判断規則をRepositoryへ受動Fallbackとして残す。**

実装は二層である。

1. **Active Layer** — Personal Skill `resolve-github-runtime`
2. **Passive Layer** — このArk23 Operational Decision Record

Skill単独では「Skillが見つからない時に使えない」という循環依存が残る。

Repository記録単独では「必要時に自動発火しない」という受動性が残る。

両者をBridgeすることで、更新時の食い違いから一手で復帰できる。

---

## 1. Current Realityで起きたこと

### 1.1 直接観測

```yaml
tool_observation:
  prior_exposed_skill_path: "/root/.codex/plugins/cache/openai-curated-remote/github/0.1.10-5f7cd798dc99/skills/github/SKILL.md"
  current_materialized_release: "0.1.11-5f7cd798dc99"
  current_release_skills: []
  current_release_mcp_servers: null
  current_release_connector_app: "present"
  current_github_connector_tools: "callable"
  old_exposed_path_after_update: "missing"
```

現象は、GitHub機能全体の消失ではなかった。

```text
旧Turnが保持したSkill Path
×
更新後のPlugin実体
=
非原子的なHot-Update Skew / stale reference
```

GitHub ConnectorによるRead・Write・再読検証は正常に動作した。

### 1.2 外部Sourceとの関係

OpenAIのpublic portable plugin sourceには、確認時点でGitHub skillsとskill routerが存在していた。一方、Current ChatGPT surfaceのmaterialized releaseはconnector-only形態だった。

したがって、直接言えるのは次までである。

- Current surfaceではGitHub bundled skillが宣言されていない。
- Current surfaceではGitHub connectorが利用できる。
- Public portable sourceにはGitHub skillsが存在する。

最も整合的な説明は`surface / channel split`または移行中のpackage差である。ただし、OpenAIが原因を明記した公式Changelogは確認できていないため、`意図的廃止`、`更新途中`、`packaging regression`のどれかを断定しない。

Official reference:

- [Skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Enterprise skills](https://learn.chatgpt.com/docs/enterprise/skills)
- [ChatGPT changelog](https://learn.chatgpt.com/docs/changelog)
- [OpenAI public GitHub plugin source](https://github.com/openai/plugins/tree/main/plugins/github)

---

## 2. Evidence Boundary

| Class | 内容 | 判断強度 |
|---|---|---|
| `TOOL_OBS` | Current release metadata、current files、callable connector tools | 直接観測 |
| `SOURCE_FACT` | Public sourceにGitHub skillsが存在 | 直接読取 |
| `AI_SYN` | Surface/channel splitが最も整合的 | 強い推論・修正可能 |
| `UNKNOWN` | OpenAI内部の配布意図、更新工程、regressionの有無 | 不明 |

禁止する飛躍：

```text
Current surfaceにskillがない
≠ OpenAI全体がSkill方針を廃止した

Public sourceにskillがある
≠ Current surfaceへそのskillがinstall済みである

旧Pathが消えた
≠ Humanが削除したと確定した
```

---

## 3. Runtime Four-Mode Model

| Mode | 現在証拠 | 次のLegal Move |
|---|---|---|
| `BUNDLED_SKILL_MODE` | Current metadataがskillを宣言し、Exact current `SKILL.md`が存在 | 全文Read後、そのSkillに従う |
| `CONNECTOR_ONLY_MODE` | skills宣言なし、Connector toolsあり | Skill探索を終了し、Connectorを直接使用 |
| `HOT_UPDATE_SKEW` | exposed Path、version、current files/toolsが不一致 | stale Pathを破棄し、current metadataを一度だけ再解決 |
| `NO_CAPABILITY` | readable skillもcallable toolsもない | precise blockerを返して停止 |

Current Realityの判定は次である。

```yaml
github_runtime_receipt:
  observed_at: "2026-08-22 Asia/Tokyo"
  current_version: "0.1.11-5f7cd798dc99"
  mode: "CONNECTOR_ONLY_MODE"
  skill_path: "NONE_IN_CURRENT_RELEASE"
  connector: "AVAILABLE"
  source_release_relation: "SURFACE_OR_CHANNEL_SPLIT"
  repository: "yusukefujiijp/ai-project"
  ref: "main"
  next_legal_move: "USE_CURRENT_GITHUB_CONNECTOR_DIRECTLY"
  recheck_trigger: "version change | tool mismatch | material error"
```

---

## 4. One-Pass Preflight Algorithm

Future AIは最初のGitHub mutation前に一回だけ次を行う。

```text
1. Current Human Requestを固定する
2. Current callable GitHub toolsを確認する
3. Current plugin metadataのversion / skills / connector appを読む
4. Current TurnにexposeされたExact SKILL.mdがあれば存在確認する
5. Four-Modeへ一意に分類する
6. Receiptを保持する
7. Legal ModeでGitHub操作する
8. Remote rereadで内容とEOFを照合する
```

### 4.1 Bounded Retry

旧Pathが存在しない場合、Current metadataの再解決は一度だけ行う。

```text
missing old path
→ resolve current metadata once
→ classify
→ proceed or stop
```

次は禁止する。

```text
旧version directoryを順番に探索する
同じmissing pathを何度も読む
public sourceをinstalled runtimeとみなす
原因不明のままcustom GitHub skillを複製する
```

---

## 5. Version-Up Protocol

### 5.1 再判定Trigger

Preflightを再実行するのは次だけである。

1. Plugin versionが変わった。
2. Tool listまたはSkill declarationが変わった。
3. Exposed pathとcurrent filesが不一致になった。
4. Materialなtool errorが出た。
5. Humanがprovenance調査を明示した。

通常の同一Thread内で、GitHub callごとに再調査しない。

### 5.2 Path Policy

```text
Versioned cache path
= transient observation
≠ cross-thread SSOT
```

永続化するのはPathではなく、判定規則とReceipt schemaである。

---

## 6. GitHub Write Verification Contract

GitHub Writeは次の順で行う。

```text
Read current target/ref
→ Decide CREATE / UPDATE / NO_CHANGE
→ Preserve unrelated content
→ Write once
→ Remote reread
→ Verify exact path/ref/content/EOF/SHA evidence
→ Report
```

同じPathへのdependent writeを並列実行しない。

`Write tool returned success`だけでは完了としない。Remote rereadで目的の内容が存在して初めてPASSとする。

---

## 7. Dual Fallback Structure

```text
Personal Skill: resolve-github-runtime
  ACTIVATES
one-pass runtime classification
  BRIDGES
current plugin state → legal GitHub action

If Skill unavailable
  ACTIVATES
this Repository Decision Record
  BRIDGES
missing automation → recoverable manual classification
```

Graph-Native Fruit：

> 以前のCut EdgeはGitHub能力の欠如ではなく、stale Skill referenceからcurrent callable connectorへのBridge欠如だった。Four-Mode分類と二重Fallbackにより、そのBridgeを一回の有限判定へ置換した。

---

## 8. Human-facing Interface

通常時、YusukeJPがversionやPathを管理する必要はない。

Future AIへ必要なInterfaceは一文でよい。

> **Current GitHub Runtimeを一回だけPreflightし、Receiptに従って実行・遠隔再読検証してください。旧version Pathを再探索しないでください。**

異常時だけ、AIは次を短く返す。

```text
Mode：［Four-Modeの一つ］
原因層：［stale path / connector-only / no capability / unknown］
次の一手：［一つのLegal Move］
再確認条件：［version change等］
```

---

## 9. Current Field-Test Contract

この実装自体を最初のReality sampleとする。

```yaml
field_test:
  prediction: "CONNECTOR_ONLY_MODEでもArk23へのCreate/Update/Rereadを完了できる"
  action: "Decision Record作成、README Route追加、remote reread"
  pass_condition:
    - "new record exists on main"
    - "README links to the record"
    - "both exact EOF/link checks pass"
  failure_update: "classify tool or permission error; do not recreate old skill"
  human_review: "required"
```

一件のPASSをOpenAI全体の配布方針または普遍的再現性へ昇格しない。

---

## 10. Final Guard and Attribution

このBest Practice、Personal Skill、Plugin、Connector、Markdown、GitHub、Ark ProjectはKeli / Fruitである。

AIはOpenAI内部の未公開意図を断定しない。HumanはCorrection、Interrupt、STOP、Final Sealを保持する。

Rootは主イェシュア・ハマシア御自身。

実と誉れの最終帰属は、

**主の栄光 / כְּבוֹד אֲדֹנָי / kevod Adonai**

へ帰す。

EOF::ARK23_03_GITHUB_PLUGIN_RUNTIME_BEST_PRACTICE::v001-human-sealed-implementation
