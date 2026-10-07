#!/usr/bin/env python3
"""Check an HTML fragment against the Moody style guide.

Usage: python3 check_moody_html.py fragment.html   (or pipe HTML on stdin)
Exit code 1 if any ERROR is found; WARNs are advisory.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

CATALOG = json.loads((Path(__file__).parent / "allowed_classes.json").read_text())
ALLOWED = set(CATALOG["classes"])
PREFIXES = CATALOG["breakpoint_prefixes"]
VAGUE_LINKS = {"click here", "here", "read more", "more", "learn more", "link", "this link"}
FORBIDDEN_TAGS = {"script", "style", "html", "head", "body"}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.issues = []
        self.last_heading = 1  # page title is the h1
        self.link_text = None
        self.link_line = 0

    def add(self, level, msg):
        self.issues.append((level, self.getpos()[0], msg))

    def check_class(self, cls):
        base = cls
        if ":" in cls:
            prefix, base = cls.split(":", 1)
            if prefix not in PREFIXES:
                return self.add("ERROR", f"unknown breakpoint prefix in '{cls}' (use {', '.join(PREFIXES)})")
            if not base.startswith("ut-"):
                return self.add("ERROR", f"'{cls}': breakpoint prefixes only apply to ut-* utilities")
        if base.startswith("ut-border-radius-") and base != "ut-border-radius-none":
            return self.add("ERROR", f"'{cls}': rounded corners are not part of the Moody brand")
        if base not in ALLOWED:
            self.add("ERROR", f"unknown class '{cls}' (not in the Moody style guide catalog)")

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in FORBIDDEN_TAGS:
            self.add("ERROR", f"<{tag}> not allowed in a body-field fragment")
        if "style" in a:
            self.add("ERROR", f"inline style on <{tag}>; use catalog classes instead")
        if any(k.startswith("on") for k in a):
            self.add("ERROR", f"inline event handler on <{tag}>")
        stripped = [k for k in a if k.startswith("data-") or (k == "aria-label" and tag in ("aside", "section", "div"))]
        if stripped:
            self.add("WARN", f"{', '.join(stripped)} on <{tag}> is stripped by the site's CKEditor")
        for cls in (a.get("class") or "").split():
            self.check_class(cls)
        if re.fullmatch(r"h[1-6]", tag):
            level = int(tag[1])
            if level == 1:
                self.add("WARN", "<h1> in body content; the page title is already the h1, start at h2")
            elif level > self.last_heading + 1:
                self.add("WARN", f"heading jumps from h{self.last_heading} to h{level}")
            self.last_heading = level
        if tag == "img":
            if "alt" not in a:
                self.add("ERROR", "<img> missing alt attribute (use alt=\"\" if decorative)")
            if not a.get("src") or a.get("src") in ("#", ""):
                self.add("WARN", "<img> has no real src; remind the editor to replace it")
        if tag == "a":
            self.link_text, self.link_line = "", self.getpos()[0]
            href = a.get("href")
            if href in (None, "", "#"):
                self.add("WARN", "link with placeholder href; flag it for the editor")
            if a.get("target") == "_blank":
                self.add("WARN", "target=_blank; avoid unless needed, and say so in the link text")
        if tag == "th" and "scope" not in a:
            self.add("WARN", "<th> without scope=\"col\"/\"row\"")
        if tag == "table" and "tablesaw" not in (a.get("class") or ""):
            self.add("WARN", "table without 'tablesaw tablesaw-stack'; it won't stack on mobile")

    def handle_data(self, data):
        if self.link_text is not None:
            self.link_text += data

    def handle_endtag(self, tag):
        if tag == "a" and self.link_text is not None:
            text = " ".join(self.link_text.split()).lower().rstrip(".")
            if not text:
                self.issues.append(("WARN", self.link_line, "link has no text (needs text or aria-label)"))
            elif text in VAGUE_LINKS:
                self.issues.append(("WARN", self.link_line, f"vague link text '{text}'; describe the destination"))
            self.link_text = None


def main():
    src = Path(sys.argv[1]).read_text() if len(sys.argv) > 1 else sys.stdin.read()
    c = Checker()
    c.feed(src)
    if not c.issues:
        print("OK: no issues found")
        return 0
    for level, line, msg in sorted(c.issues, key=lambda i: i[1]):
        print(f"{level} line {line}: {msg}")
    errors = sum(1 for i in c.issues if i[0] == "ERROR")
    print(f"\n{errors} error(s), {len(c.issues) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
