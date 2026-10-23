#!/usr/bin/env python3
"""Build an Office viewing URL for a public GitHub PPTX; no network or writes."""

import argparse
import re
from urllib.parse import parse_qs, quote, unquote, urlsplit, urlunsplit

VIEWER_HOST = "view.officeapps.live.com"
VIEWER_PATH = "/op/view.aspx"


def direct_pptx_url(value: str) -> str:
    value = value.strip()
    if any(ord(c) < 32 for c in value):
        raise ValueError("Use one complete URL without control characters.")
    url = urlsplit(value)
    if url.scheme != "https" or url.netloc.lower() not in {
        "github.com", "raw.githubusercontent.com"
    }:
        raise ValueError("Use a public https GitHub PPTX file URL.")
    parts = url.path.lstrip("/").split("/")
    if len(parts) < 4 or any(not p or unquote(p) in {".", ".."} for p in parts):
        raise ValueError("Use a file URL, not a folder or repository URL.")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", parts[0]) or not re.fullmatch(
        r"[A-Za-z0-9_.-]+", parts[1]
    ):
        raise ValueError("Invalid owner or repository in URL.")
    owner, repo = parts[:2]
    tail = parts[2:]
    if url.netloc.lower() == "github.com":
        if tail[0] not in {"blob", "raw"}:
            raise ValueError("Use a GitHub blob or raw file URL.")
        tail = tail[1:]
        if tail[:2] == ["refs", "heads"]:
            tail = tail[2:]
    if len(tail) < 2 or not (
        tail[0] == "main" or re.fullmatch(r"[0-9a-fA-F]{40}", tail[0])
    ):
        raise ValueError("Use main or a full commit SHA; resolve other refs explicitly.")
    if not unquote(tail[-1]).lower().endswith(".pptx"):
        raise ValueError("The file must end in .pptx.")
    # Keep existing escapes; encode literal Unicode/spaces in path segments.
    if re.search(r"%(?![0-9a-fA-F]{2})", url.path):
        raise ValueError("Malformed percent escape in URL.")
    path = "/" + "/".join(quote(p, safe="%-._~") for p in [owner, repo, *tail])
    return urlunsplit(("https", "raw.githubusercontent.com", path, "", ""))


def viewer_url(value: str) -> str:
    value = value.strip()
    url = urlsplit(value)
    if url.scheme == "https" and url.netloc.lower() == VIEWER_HOST:
        if url.path != VIEWER_PATH:
            raise ValueError("Unsupported viewer path.")
        sources = parse_qs(url.query).get("src", [])
        if len(sources) != 1:
            raise ValueError("The viewer URL must have exactly one src.")
        value = sources[0]
    source = direct_pptx_url(value)
    return f"https://{VIEWER_HOST}{VIEWER_PATH}?src={quote(source, safe='')}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Public GitHub PPTX URL (main or full commit SHA)")
    args = parser.parse_args()
    try:
        print(viewer_url(args.url))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
