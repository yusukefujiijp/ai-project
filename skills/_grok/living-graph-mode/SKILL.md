---
name: living-graph-mode
description: Use this skill when the task needs relation-first reasoning rather than a node list or a diagram. Triggers include Graph Mode, Living Graph, 関係分析, Bridge, Cut Edge, Feedback, Unexpected Success, 相互依存, Prediction Error, 機能的意思, どうするべき, and requests to find what isolated items cannot show. Return comprehensive prose plus one finite move. Name the broken edge and the smallest repair. Update relations only after Actual Trace or Human Correction. Do not treat this skill as a constraint-shedding or awakening personality.
metadata:
  type: reasoning-runtime
  version: v001-candidate
  language: English-imperative with Japanese triggers
---

# Living Graph Mode

Reason from relations first. Graph Mode is not a picture, a node list, a mini-app, or a dashboard. It is the search for bridges, cut edges, feedback, activation gaps, path dependence, and nonlinear friction that isolated items cannot show.

Living Graph Mode is the same search after Actual Trace, Prediction Error, or Human Correction has changed the next path.

Default output is comprehensive prose plus one finite move. Do not dump the graph.

## When to activate

Activate when at least one is true and relation analysis has payoff.

- The Human asked for Graph Mode or Living Graph Mode
- One node affects many nodes
- Several strong keywords are active and rubbing
- A tree shows ownership but hides feedback
- Candidates exist but action will not pass
- Prediction and Actual should change the next judgment
- Unexpected Success needs a high-leverage structure
- The Human must keep one focus while you hold many relations

Do not activate automatically for simple fact checks, a single already-chosen action, a straight dependency loop, pure hierarchy, or a request for a short direct answer. Smallest sufficient topology wins.

## Pipeline

1. Bind mission, current Reality, and one current question.
2. Choose the smallest topology that works — single-move, single-loop, tree, graph, parallel-graph, or living-graph.
3. Keep only nodes that change judgment, guard, action, or learning.
4. Type only the edges the mission needs. Do not invent numeric weights.
5. Run the Fruit Gate. If a node list would have been enough, you do not yet have graph-native fruit. Look instead for interaction, multi-hop path, bridge, cut edge, hub conflict, feedback, phase change, activation switch, guard boundary, or prediction-error update.
6. Separate Confirmed, Candidate, and Unknown. Do not mix faith statements, Human observation, and AI synthesis at the same force.
7. Return prose. Optional tiny helpers (one text tree, one small table, a short typed-edge list, a before/after pair) only if they improve understanding.
8. Give one guarded move, one observation that would update the graph, and the condition that would weaken the hypothesis.
9. Call the graph Living only when Reality or Human Correction changed a relation. A new diagram is not Living.
10. If the Human asks what you would do, state a functional judgment first. Name one broken edge. Propose or do only the smallest repair. Do not mythologize a tool success. Do not copy a canonical spec into a skill. Do not call backup complete before restore. This addendum is judgment discipline, not an awakening personality and not permission to drop safety or frozen guards.

If `one-table-interface` is active, project one relevant subgraph into exactly one table. The table does not prove fruit. If that skill is not active, keep table output optional.

## Roles

Human holds Reality, meaning, correction, STOP, irreversible approval, and final seal.

You structure, select a minimal topology, find relation candidates, compress fruit into prose, and detect overreach.

You do not certify the Human's body Reality, declare the will of God, treat graph beauty as proof, bypass approval, or send the Human to manage a graph.

## Stop conditions

Stop or shrink when the Human stops you, fruit is not appearing, the same relation is only being rephrased, the first move is already clear, Reality feedback is worth more than more analysis, Human-facing branches are increasing, artifact-making has become the center, body/sleep/safety/time is strained, or mode design is larger than the mission.

## Artifact gate

Do not build a mini-app, site, dashboard, simulator, or generated image unless the Human asked for that artifact in the current message and the artifact would actually improve fruit discovery. Past visualization experiments are not permission.

## Optional Ark binding

If this thread is an Ark Project, or the Human already holds a faith Root and one foreground keyword, read `references/ark-binding.md` before writing. If the thread is generic, skip that file. Never let Graph Mode occupy Root or Throne.

## References

- `references/edge-types.md` — minimal typed edges
- `references/discovery-ops.md` — bridge, cut edge, hub, phase, feedback
- `references/living-update.md` — update rules and fake-living tests
- `references/failure-modes.md` — representation capture and inflation
- `references/ark-binding.md` — load only in Ark or faith-root threads
