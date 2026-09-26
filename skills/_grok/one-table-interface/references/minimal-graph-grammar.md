# Minimal Graph Grammar

Use this file when `living-graph-mode` is not loaded. It is enough to keep the table graph-bounded.

## Nodes

A node is an independent thing that changes judgment. Attributes of a node are not extra nodes.

Useful types — purpose, reality, signal, candidate, guard, action, observation, learning.

Useful states — active, dormant, deferred, pruned.

## Edges

Write at least one directed relation.

Source → typed edge → target.

Useful types — ACTIVATES, INHIBITS, DEPENDS_ON, BRIDGES, GATES, MODIFIES, CORRECTS, EXECUTES, OBSERVES.

Direction matters. If reversing source and target would change the advice, the edge is doing work.

## Views that count as graph-bounded

- Path — purpose to action
- Bridge — two good domains become passable
- Cut edge — one break stops fruit
- Activation difference — important versus always-on
- Evidence boundary on a relation, not only on a list item
- Before / after of an edge after Actual Trace or Human correction

## Views that do not count

- A row of items with no relation
- A spec sheet
- A summary table of independent bullets
- A score column with invented precision

## Fruit test after the table exists

Would listing the nodes alone have produced this understanding?

If yes, the table may still help orientation, but do not call it graph-native fruit.
