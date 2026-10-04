import csv
from pathlib import Path
import subprocess,sys
subprocess.run([sys.executable,'scripts/triagem_cinzas.py'],check=True)
r=list(csv.DictReader(Path('data/generated/triagem_fases_cinzas.csv').open(encoding='utf-8')))
assert len(r)==6
assert {'calcita','quartzo','hidroxiapatita'}<={x['fase'] for x in r}
