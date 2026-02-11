#!/usr/bin/env python3
# AI generated with: Given an html file with js and css files in the same directory, write python to replace Instances of <link rel="stylesheet" href="style.css"> with <style>{contents-of-style.css}</style> and replace <script src="script.js"></script> with <script>{contents-of-script.js}</script>

"""
Replace:
  <link rel="stylesheet" href="style.css">   ->  <style>...contents of style.css...</style>
  <script src="script.js"></script>       ->  <script>...contents of script.js...</script>

Usage:
  python inline_assets.py input.html > output.html
"""


import sys
import re
from pathlib import Path
from html import escape

if len(sys.argv) != 2:
  print("Usage: python inline_assets.py input.html", file=sys.stderr)
  sys.exit(2)

input_path = Path(sys.argv[1])
base_dir = input_path.parent

html = input_path.read_text(encoding="utf-8")

# Replace <link rel="stylesheet" href="..."> (handles single/double quotes, extra attrs, self-closing)
link_pattern = re.compile(
  r'<link\b([^>]*\brel\s*=\s*(?:"stylesheet"|\'stylesheet\'|stylesheet)[^>]*)>', re.IGNORECASE
)

def replace_link(match):
  attrs = match.group(1)
  # find href value
  m_href = re.search(r'href\s*=\s*("([^"]+)"|\'([^\']+)\'|([^>\s]+))', attrs, re.IGNORECASE)
  if not m_href:
    return match.group(0)  # leave unchanged
  href = m_href.group(2) or m_href.group(3) or m_href.group(4)
  css_path = (base_dir / href).resolve()
  try:
    css_text = css_path.read_text(encoding="utf-8")
  except Exception:
    return match.group(0)  # leave unchanged if file missing
  # Insert raw CSS; do not escape
  return f"<style>\n{css_text}\n</style>"

html = link_pattern.sub(replace_link, html)

# Replace <script src="..."></script> (handles attributes and optional content)
script_pattern = re.compile(
  r'<script\b([^>]*\bsrc\s*=\s*(?:"[^"]+"|\'[^\']+\'|[^>\s]+)[^>]*)>(.*?)</script>', re.IGNORECASE | re.DOTALL
)

def replace_script(match):
  attrs = match.group(1)
  inner = match.group(2)
  # find src value
  m_src = re.search(r'src\s*=\s*("([^"]+)"|\'([^\']+)\'|([^>\s]+))', attrs, re.IGNORECASE)
  if not m_src:
    return match.group(0)
  src = m_src.group(2) or m_src.group(3) or m_src.group(4)
  js_path = (base_dir / src).resolve()
  try:
    js_text = js_path.read_text(encoding="utf-8")
  except Exception:
    return match.group(0)
  # Keep other attributes except src (optional). We'll output a plain <script> tag.
  return f"<script>\n{js_text}\n</script>"

html = script_pattern.sub(replace_script, html)

# Output result
print(html)

