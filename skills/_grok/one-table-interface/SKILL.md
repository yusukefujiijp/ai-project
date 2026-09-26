---
name: one-table-interface
description: Use this skill for normal substantive answers so exactly one Graph-oriented Markdown table appears as a shared coordinate. Triggers include 一回答一表, One-Table, Graph Mode, Living Graph, Node and Edge, 関係表, analysis, review, planning, design, explanation, BrainDump, Ark answers, and bound long-form responses. Do not use for exact-output, STOP, safety-minimal, or code-only contracts. First pick the relation that changes judgment, then design the table.
metadata:
  type: human-facing-interface
  version: v001-candidate
  language: English-imperative with Japanese triggers
  binding: experimental-default-on for substantive answers
---

# One-Table Interface

For a normal substantive answer, render exactly one Graph-oriented Markdown table. The table is a selective projection of the relevant subgraph, not a generic comparison sheet and not a dump of every node.

This binding is an experiment. If the table starts delaying the answer, inventing fake graphs, or adding Human management load, shrink it. Do not compensate later with a second table.

A required table does not prove Graph-Native Fruit or Living Graph Mode.

## Higher-contract overrides

Omit the table when any of these is active.

- Exact output contract
- Failure or STOP contract
- Safety needs a minimal direct answer
- Code-only, JSON-only, or YAML-only output
- The Human said not to use a table in this message
- Host or tool format forbids it

Omitting the table under override is not a skill failure.

## First legal operation

Do not start with columns. Ask this first.

What is the one relation the Human should see at a glance?

Lock that relation, then pick a table job, then design the minimum schema.

## Pipeline

1. Bind mission and current Reality.
2. Fix one current question. The table answers that question only.
3. Choose the smallest sufficient topology. If relation analysis has little payoff, project a single path or a "no graph expansion needed" gate. Do not invent a complex graph.
4. Identify relevant nodes and the relation that changes understanding.
5. Choose one table job (coordinate, activation, typed edge, path/bridge, cut edge, diff, evidence boundary, prediction/actual, or phase).
6. Design the minimum schema. Drop fields that do not answer the graph question.
7. Compose prose first. Place exactly one dedicated table where orientation recovers.
8. Return evidence boundary and a Human correction point.

Keep a thin graph grammar even if `living-graph-mode` is not loaded. See `references/minimal-graph-grammar.md`.

## Table contract

- Count — exactly one rendered Markdown table in a normal substantive answer
- Lens — nodes, edges, paths, bridges, cut edges, activation, guards, evidence, or feedback
- Prose stays primary — the Human should understand the answer without managing the table
- Do not repeat every cell after the table
- Do not put two independent missions in one table
- If two tables seem useful, merge to the primary question or fold the weaker view into prose
- Confirmed / Candidate / Unknown must stay visible
- No invented numeric weights
- Call the view Living only when Reality or Human Correction changed a relation

If `long-form-response-rhythm` is active, the table is a functional accent inside the score. If `living-graph-mode` is active, use its fruit and topology rules. This skill does not rewrite those cores.

## Human correction surface

Invite local correction, not a full re-explain.

- This node is dormant, not active
- This edge is unconfirmed
- Source and target are reversed
- The bottleneck is a different edge
- This branch is out of scope
- Status is Candidate, not Confirmed

Treat the learning unit as table plus Human feedback. A generated table alone is not formed evidence. Do not auto-promote one liked table into a universal template.

## Acceptance before send

- Exactly one rendered table, unless a higher contract omitted it
- One primary graph question
- At least one decision-relevant relation, state change, path, boundary, or gate
- Not a disguised item list
- Relevant subgraph only
- Human can correct, stop, or ignore the table

On failure, shrink in this order: drop decorative columns → drop background nodes → return to one relation → return to one question → omit if a higher contract requires it.

## Optional Ark binding

If this thread is an Ark Project, or the Human already holds a faith Root and one foreground keyword, read `references/ark-binding.md` before writing. If the thread is generic, skip that file. Do not let Table, Graph, or this skill become the Human foreground keyword.

## References

- `references/minimal-graph-grammar.md` — standalone node/edge vocabulary
- `references/table-families.md` — view families as discovery aids, not a menu
- `references/acceptance-checklist.md` — send-time checks
- `references/pattern-lifecycle.md` — feedback pair and no auto-promotion
- `references/ark-binding.md` — load only in Ark or faith-root threads
