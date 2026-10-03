from pathlib import Path
import re
import sys

f=[Path("paper/main.log"),Path("poster/poster.log")]
x="\n".join(p.read_text(encoding="utf-8",errors="ignore") for p in f if p.exists())
p=re.compile(r"(?im)^.*(?:warning:|overfull|underfull|undefined|fatal error|emergency stop|no file .*\\.bbl).*$")
b=p.findall(x)
if b:
 print("\n".join(b))
 sys.exit(1)
if not all(p.exists() for p in f):
 print("logs ausentes")
 sys.exit(1)
