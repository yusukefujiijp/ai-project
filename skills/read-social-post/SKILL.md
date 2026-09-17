---
name: read-social-post
description: Retrieve the complete text of an X/Twitter or other social-media post from its URL with minimal user copying and tool overhead. Use when a linked post must be read, summarized, verified, or rewritten; skip when its complete text is already supplied.
---

# Read Social Post

Accept one post URL as sufficient input. Retrieve the target post's complete body before treating retrieval as successful. Reduce retrieval overhead, not source coverage.

## Choose a permitted route

- Reuse complete source text already obtained in the current context unless a fresh version is required.
- Prefer an applicable connector under the host's routing rules. Perform any required public web search first; reuse a lookup already made for this URL. One focused URL or post-ID lookup is normally enough. Do not keep rephrasing queries to assemble snippets.
- If search or a retrieval tool fails or returns incomplete text, consider another promising, permitted route before asking the user to copy the post. Where allowed, ordinary HTTP retrieval of the public post page can expose the body in HTML or embedded structured data without a browser. Prefer extracting the target body from that page over probing many mirrors or embed endpoints.
- Distinguish a tool-specific retrieval failure, a site access refusal, and successful retrieval of truncated content. A failed tool does not establish that every route is unavailable. Do not switch methods to evade access controls, an approval rejection, or an explicit non-retryable restriction; respect the affected boundary.
- Use browser interaction when eligible and necessary, such as expanding the target's own collapsed body. Follow the host's browser eligibility rules; search failure alone does not authorize browser fallback. Read the current browser skill and required documentation once, then reuse valid guidance and the session. Never bypass a plugin fallback restriction.

Choose by available evidence and capabilities, not a fixed endpoint sequence. Do not hard-code runtime paths, selectors, credentials, or a promise that one API or HTML tag always contains the full post.

## Extract and verify the target body

Identify the author and post ID or canonical URL. Inspect the actual response or DOM before selecting the extraction method. Preserve paragraph order, links, and meaningful inline text; exclude navigation, replies, and recommendations. In HTML, isolate the target body or associated structured data rather than dumping the whole page into context. Use available parsing tools; do not make an optional parser dependency a prerequisite for retrieval.

HTTP 200, a matching author, a preview, or a final sentence alone does not prove completeness. Metadata descriptions, oEmbed text, and syndication responses may truncate long posts even when the full body exists elsewhere on the public page. Check for unresolved collapse, truncated tool output, missing long-form fields, or a body ending mid-sentence. Treat ellipses in context: they may be the author's punctuation rather than truncation.

Verify coverage across the beginning, intervening paragraphs, and ending. Recover only missing portions; compare another representation when completeness remains uncertain, not as a mandatory duplicate fetch. Keep quoted posts, threads, images, and video separate. A quoted post's “Show more” does not make a complete target body incomplete. Inspect additional material only when the request needs it; never imply that reading the body verified attached media or independently proved the author's claims.

## Finish or state the blocker

Stop retrieval once target-body coverage is established. Continue the requested analysis or writing within the current scope; preserve plan-only and STOP boundaries. If only retrieval was requested, report success briefly. Reproduce full text only when requested and allowed by applicable copyright rules.

If coverage remains incomplete, continue only while a distinct permitted route has a concrete prospect of recovering the missing text. Avoid repeating unchanged failures or exploring endpoints indefinitely. When those routes are exhausted or unavailable, state “全文取得未達”, identify the missing scope and specific blocker, and offer the least burdensome viable next step. Do not fill gaps from memory or make user transcription the default first fallback. Use the host's secure authentication flow when login is necessary; never request passwords in chat.

Report body and media status separately: for example, a media access refusal does not undo verified body retrieval. Success through public HTML or a browser is an observed result, not a guarantee for every post, account, environment, or SNS.
