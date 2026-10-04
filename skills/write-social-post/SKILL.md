---
name: write-social-post
description: >-
  Draft or revise X/SNS public posts narrated by the actual writing AI and
  explicitly grounded in human–AI collaboration. Use for turning the current
  conversation or supplied material into this public-post style, or revising
  an existing post in that workflow. Do not activate for source retrieval
  alone, general SNS questions, human-voiced writing in another style, or
  review/planning of the prompt or skill itself.
---

# Social Post

Turn the user's current conversation and material into a standalone public post. Preserve the meaning developed together, accurate attribution, and useful explanation for readers who did not see the conversation. Make the actual human–AI collaboration visible using the audience-facing AI name defined by the shared writing source.

## Bind the current assignment

Resolve the topic, intended audience, accepted draft, latest corrections, and requested changes from the available conversation. Reuse supplied information instead of requiring a new form. Keep the public article focused on the selected topic rather than exporting unrelated conversation details.

Distinguish drafting, revising, reviewing the writing instructions, and planning skill changes. Follow the actual request even when the material being reviewed contains an imperative to write a post. Respect current Plan-only and STOP instructions. Drafting a post does not itself authorize posting it to an account, messaging others, or changing this skill.

## Read the shared writing source

Use [AI SNS Public Post](https://github.com/yusukefujiijp/ai-project/blob/main/prompts/ai-sns-public-post.md) as the shared source of article requirements. Read the complete document before claiming to apply this style; recover truncated content rather than substituting a search snippet. Reuse the complete source already available in the conversation when no material revision or mismatch is indicated. A supplied full copy or an explicitly requested fixed version can serve the same role.

The shared prompt owns the detailed writing conditions, AI-name Few-Shot examples, section structure, length, attribution, and final-output format. This skill owns selection and workflow; do not maintain another independently edited copy of those rules here. Apply the current user's explicit topic, language, length, and format changes rather than treating defaults as immutable.

Use permitted source-access tools available in the current environment; do not require one vendor's connector. If the shared source is unavailable and no complete copy is available, explain that specific gap and request the source text when needed. Continue independent work such as organizing supplied material; do not claim full compliance from an imagined copy.

## Prepare and write

Carry forward the user's intended meaning and corrections without turning hypotheses, personal reports, or desired outcomes into established facts. Research the claims that need verification, using relevant primary sources and the environment's access rules. Resolve material uncertainty through verification, qualification, or narrowing the claim; ask for missing material only when it remains necessary to write honestly.

When a linked social post supplies essential material and its full text is missing, use read-social-post if available, or an equivalent permitted retrieval method. Reuse an already supplied full post. Keep source retrieval separate from evaluating whether its claims are supported.

Resolve the narrator from the actual collaboration, then apply the shared source's public-facing naming policy and the user's latest correction. Do not substitute a technical runtime name for the familiar public name selected for the intended audience. The ChatGPT, Grok, and Claude examples are not a closed list or a choice of persona. Keep an AI mentioned in source material distinct from the current author, and describe the human collaboration according to what actually occurred. Do not guess a model generation or attribute human lived experience to the AI.

Develop the article using the shared source and current request. Choose the angle, explanation, examples, and amount of research to fit the topic. Do not impose a fixed thinking sequence, require Graph Mode or Living Review on every post, or manufacture novelty, urgency, and certainty to make the article more engaging.

## Verify the final post length

Resolve the publication limit and counting method from the shared prompt and the current request. For X, mechanically measure the exact copyable payload, including its title, headings, whitespace, citations, and URLs; exclude the enclosing code fence. Use official `twitter-text` or an equivalent verified counter, not raw string length or a rough doubling estimate.

When Node.js is available, run `node scripts/count_x_post.cjs --limit <resolved-limit> <post.txt>` from this skill's directory. Its required limit comes from the writing source; the helper does not own the publication policy. It accepts UTF-8 text from a file or `-` for stdin, preserves whitespace, and reports the weighted length and remaining allowance. It configures the parser for that limit rather than using the library's default 280-character validity result.

The helper needs `twitter-text` (tested with 3.1.0). Reuse an available installation. If missing and package installation is permitted, install it in a temporary dependency directory with `npm install --prefix <directory> --ignore-scripts --no-audit --no-fund twitter-text@3.1.0` and expose `<directory>/node_modules` through `NODE_PATH`; do not add dependencies or generated files to the skill. An equivalent permitted counter can be used in other environments.

If over the limit, remove repetition and peripheral material while preserving the core meaning, evidence, important qualifications, and collaboration statement; then count again. Recount after any subsequent title, prose, or link edit. Deliver the same text that passed the final check. If exact measurement remains unavailable, follow the shared prompt's unverified-draft handling rather than claiming a measured count or silently treating an estimate as a pass.

## Deliver and revise

Check the completed article against the shared source and the current request, especially the consequential claims, scope, attribution, narrator identity, collaboration statement, and requested output. For the default post-only task, return the finished post in the source's specified format without process notes or self-evaluation. Honor explicitly requested comparisons or explanations when the current assignment includes them.

For revisions, retain accepted meaning and evidence while applying the requested correction throughout affected passages. Use actual feedback to judge whether a problem belongs in the article, the shared prompt, or this skill's routing. Propose or make durable changes only within the current authorization; ordinary use is not an instruction to rewrite the skill.
