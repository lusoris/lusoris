#!/usr/bin/env python3
"""Render the upstream section of README.md from upstream.json, so the page and the data cannot drift.

Usage: render.py            rewrite the section between the two markers
       render.py --check    exit 1 when README.md differs from what the data gives, or the total is wrong
       render.py selftest
A project links to its own page, never to a single pull request: a link to one would post a reference into that
project's thread.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- upstream:start -->", "<!-- upstream:end -->"
GREEN = "2ea44f"
SINGLE_ITEM_RE = re.compile(r"/(?:pulls?|issues?)/\d+")


def single_item(project):
    return any(bool(SINGLE_ITEM_RE.search(project.get(k) or "")) for k in ("url", "merged_url"))


def badge(project):
    label, message = quote(project["name"].replace("-", "--"), safe=""), quote(f"{project['merged']} merged", safe="")
    logo = f"?logo={project['logo']}&logoColor=white" if project.get("logo") else ""
    return f"[![{project['name']}: {project['merged']} merged](https://img.shields.io/badge/{label}-{message}-{GREEN}{logo})]({project.get('merged_url', '')})"


def section(data):
    rows = "\n".join(f"| [{p['name']}]({p['url']}) | [{p['merged']}]({p.get('merged_url', '')}) |" for p in data["projects"])
    return f"{START}\n| Project | Merged |\n| :-- | --: |\n{rows}\n{END}"


def problems(data):
    out = []
    if sum(p["merged"] for p in data["projects"]) != data["merged_total"]:
        out.append("merged_total is not the sum of the projects")
    out += [f"{p['name']}: missing merged_url" for p in data["projects"]
            if not p.get("merged_url")]
    out += [f"{p['name']}: link names a single pull request or issue" for p in data["projects"]
            if single_item(p)]
    return out


def replace(text, block):
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) > text.index(END):
        raise SystemExit("README.md needs exactly one start marker before one end marker")
    return text[:text.index(START)] + block + text[text.index(END) + len(END):]


def selftest():
    data = {"merged_total": 3, "projects": [{"name": "A-b", "url": "https://example.org/a", "merged_url": "https://example.org/a/pulls?q=is%3Amerged", "merged": 1, "logo": "x"},
                                            {"name": "C d", "url": "https://example.org/c", "merged_url": "https://example.org/c/pulls?q=is%3Amerged", "merged": 2, "logo": ""}]}
    page = f"top\n{START}\nold\n{END}\nbottom\n"
    done = replace(page, section(data))
    cases = [
        ("section is replaced, rest kept", done.startswith("top\n") and done.endswith("\nbottom\n") and "old" not in done),
        ("a dash in a name is escaped for the badge", "/badge/A--b-1%20merged-" in badge(data["projects"][0])),
        ("a space in a name is encoded", "/badge/C%20d-2%20merged-" in badge(data["projects"][1])),
        ("no logo, no logo parameter", "C%20d-2%20merged-2ea44f)" in badge(data["projects"][1])),
        ("rendering twice changes nothing", replace(done, section(data)) == done),
        ("a wrong total is found", problems(dict(data, merged_total=4)) == ["merged_total is not the sum of the projects"]),
        ("good data has no problem", problems(data) == []),
        ("a row renders name->url and count->merged_url", "| [A-b](https://example.org/a) | [1](https://example.org/a/pulls?q=is%3Amerged) |" in section(data)),
        ("a badge links merged_url", "](https://example.org/a/pulls?q=is%3Amerged)" in badge(data["projects"][0])),
        ("a missing merged_url is a problem", "X: missing merged_url" in problems({"merged_total": 1, "projects": [{"name": "X", "url": "https://example.org/x", "merged": 1}]})),
        ("/pulls?q=... passes", problems({"merged_total": 1, "projects": [{"name": "X", "url": "https://example.org/x", "merged_url": "https://github.com/o/r/pulls?q=is%3Amerged", "merged": 1}]}) == []),
        ("/pull/12 and /pulls/12 fail", "X: link names a single pull request or issue" in problems({"merged_total": 1, "projects": [{"name": "X", "url": "https://example.org/x", "merged_url": "https://github.com/o/r/pull/12", "merged": 1}]})
                                     and "X: link names a single pull request or issue" in problems({"merged_total": 1, "projects": [{"name": "X", "url": "https://example.org/x", "merged_url": "https://github.com/o/r/pulls/12", "merged": 1}]})),
    ]
    bad = [name for name, ok in cases if not ok]
    if bad:
        raise SystemExit(f"selftest failed: {bad}")
    print(f"selftest ok: {len(cases)} cases")
    return 0


def main(argv):
    if argv[1:] == ["selftest"]:
        return selftest()
    data = json.loads((ROOT / "upstream.json").read_text(encoding="utf-8"))
    found = problems(data)
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    wanted = replace(text, section(data))
    if argv[1:] == ["--check"]:
        if wanted != text:
            found.append("README.md is not what upstream.json gives; run tools/render.py")
        for line in found:
            print(line)
        return 1 if found else 0
    if argv[1:]:
        print(__doc__.strip())
        return 2
    if found:
        raise SystemExit("; ".join(found))
    readme.write_text(wanted, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
