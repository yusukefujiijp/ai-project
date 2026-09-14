---
name: read-social-post
description: Retrieve the complete text of an X/Twitter or other social-media post from its URL with minimal user copying and tool overhead. Use when a linked post must be read, summarized, verified, or rewritten; skip when its complete text is already supplied.
---

# Read Social Post

Accept one post URL as sufficient input. Retrieve the target post's complete body before treating retrieval as successful. Reduce retrieval overhead, not source coverage.

## Take the shortest supported route

- Reuse complete source text already obtained in the current context unless a fresh version is required.
- Prefer an applicable connector under the host's routing rules. For public web lookup, perform the required web search first; reuse a successful search already made for this URL. One focused URL or post-ID lookup is normally enough. Do not keep rephrasing queries to assemble snippets.
- When search succeeds but lacks the full body, use the supported browser to inspect the actual post. Read the current browser skill and its required documentation once, then reuse the live browser/session and already-read guidance while valid. Do not hard-code runtime paths, selectors, or credentials in this skill.
- Search failure alone is not authorization for browser fallback. Follow the host's browser eligibility rules; never use it to recover a failed or unavailable applicable plugin.

## Read the post, not the surrounding feed

Open the target URL and identify its author and post identity. Use the rendered page/DOM and expand the target's own “Show more” if needed. Extract the body through its ending, preserving paragraph order, links, and meaningful inline text. Ground selectors in the observed page. Prefer a focused post read over repeated full-page snapshots; exclude navigation, replies, and recommendations.

Verify that the target body has no unresolved collapse, ellipsis from truncation, missing loaded section, or truncated tool output. Recover only the missing portion. An ending sentence alone does not prove that intervening text was captured. Stop retrieval once coverage is established.

Keep quoted posts, threads, images, and video separate from the target body. Inspect them when the user's task requires them; never imply that reading the body also verified attached media or the truth of its claims.

## Finish or state the blocker

Continue the requested analysis or writing after retrieval; do not stop at a success announcement when more work was requested. If only retrieval was requested, report success briefly. Reproduce the full text only when requested and allowed by applicable copyright rules.

If the full body cannot be obtained through the available permitted route, state “全文取得未達” and the specific blocker. Snippets are not partial success against a full-text requirement. Do not fill gaps from memory or ask for copying as the default next step. Use the host's secure authentication flow if login is necessary; never request passwords in chat. Respect site blocks and bounded recovery rules.

This method requires a permitted retrieval tool. A successful public X browser read without login is an observed example, not a guarantee for every post, account, or SNS.
