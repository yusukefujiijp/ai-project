---
title: "AI Plan Mode Query"
version: "v002-candidate"
date: "2026-07-11"
filename: "ai-plan-mode_query.md"
canonical_path: "prompts/ai-plan-mode_query.md"
class: "prompt_query"
role: "activation query for prompts/ai-plan-mode.md"
paired_prompt:
  path: "prompts/ai-plan-mode.md"
  role: "active prompt runtime"
status: "human-sealed field-test candidate / not canonical"
---

# AI Plan Mode Query v002 Candidate

このConversation、現在のChatGPT Project、または明示添付File内で、versionとstatusが明示された最新のHuman-Sealed `prompts/ai-plan-mode.md`を確認してください。

確認できない場合は、`PROTOCOL MISSING`と出力して停止し、一般知識や推測でProtocolを代替しないでください。

複数候補が存在し、適用すべき最新版を確定できない場合は、`PROTOCOL VERSION CONFLICT`と出力して停止してください。

確認できたHuman-Sealed `prompts/ai-plan-mode.md`に従い、直前のUser依頼と現在の対話Contextを対象としてPlan Modeを実行してください。

この回答では計画だけを作成し、最終成果物本文、実装、File変更、GitHub Write、Commit、Full Rail実行はまだ行わないでください。

Planの構造、Adaptive Density、Living Review、Human Decision Gates、Stop Conditions、Reality Review、最終必須Sectionは、確認済みProtocolの規定に従ってください。

回答末尾には必ず、次の順序で置いてください。

1. 【Full Rail: same_thread】
2. 【Next Gate: human_editable】

Full Railは、Protocolで定義されたAccepted Exact Human Triggerを受けるまで`armed_not_started`として待機してください。
