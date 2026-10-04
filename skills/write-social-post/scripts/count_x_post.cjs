#!/usr/bin/env node
"use strict";

// Count the exact UTF-8 publication payload. The caller supplies the policy limit.
const fs = require("node:fs");
const { TextDecoder } = require("node:util");

function main() {
  const args = process.argv.slice(2);
  if (args.length !== 3 || args[0] !== "--limit" || !/^[1-9][0-9]*$/.test(args[1])) {
    throw new Error("Usage: node count_x_post.cjs --limit <positive-integer> <file|->");
  }
  const limit = Number(args[1]);
  if (!Number.isSafeInteger(limit)) throw new Error("Limit must be a safe positive integer.");

  let twitterText;
  try {
    twitterText = require("twitter-text");
  } catch (error) {
    if (error.code !== "MODULE_NOT_FOUND") throw error;
    throw new Error("twitter-text is unavailable. See the skill's dependency instructions or use a verified equivalent counter.");
  }

  const bytes = fs.readFileSync(args[2] === "-" ? 0 : args[2]);
  // Do not trim, normalize newlines, strip a BOM, or remove code fences silently.
  const text = new TextDecoder("utf-8", { fatal: true, ignoreBOM: true }).decode(bytes);
  const result = twitterText.parseTweet(text, {
    ...twitterText.configs.defaults,
    maxWeightedTweetLength: limit,
  });
  const withinLimit = result.weightedLength <= limit;
  process.stdout.write(JSON.stringify({
    weightedLength: result.weightedLength,
    limit,
    remaining: limit - result.weightedLength,
    withinLimit,
    validForConfiguredLimit: result.valid,
    parser: "twitter-text",
    parserVersion: require("twitter-text/package.json").version,
  }, null, 2) + "\n");
  // This checks parser validity and length, not account permissions or publication.
  process.exitCode = result.valid ? 0 : 1;
}

try {
  main();
} catch (error) {
  process.stderr.write(error.message + "\n");
  process.exitCode = 2;
}
