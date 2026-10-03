import csv
from pathlib import Path
import matplotlib.pyplot as p
r=list(csv.DictReader(open('quantum-summary.csv',encoding='utf-8')))
for s in sorted({x['system'] for x in r}):
 x=[a for a in r if a['system']==s];p.plot([a['method'] for a in x],[float(a['gap_hartree']) for a in x],'o-',label=s)
p.ylabel('Gap (hartree)');p.xlabel('Método');p.legend();p.tight_layout();p.savefig('quantum-gap.png',dpi=160)
