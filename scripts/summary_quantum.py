import csv,glob,json
rows=[]
for p in glob.glob('data/quantum-*/*.json'):
 x=json.load(open(p,encoding='utf-8'));rows.append({k:x[k] for k in ['method','energy_hartree','homo_hartree','lumo_hartree','gap_hartree','converged']})
rows.sort(key=lambda x:x['method'])
with open('quantum-summary.csv','w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
assert len(rows)==3
