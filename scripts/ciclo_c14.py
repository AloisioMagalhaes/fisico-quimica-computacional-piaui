import csv,math
from pathlib import Path

HL=5730.0
DT=10.0
Y=50000
lam=math.log(2)/HL
prod=1.0
turn=1/40
out=Path('data/generated');out.mkdir(parents=True,exist_ok=True)
n=prod/lam
rows=[]
for t in range(0,Y+1,10):
 a=n*math.exp(-lam*t)
 b=a*(1-math.exp(-turn*1))
 rows.append((t,a,b,a/n))
with (out/'ciclo_c14.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['tempo_anos','estoque_atmosferico_normalizado','incorporacao_biologica_normalizada','fracao_remanescente'])
 w.writerows(rows)
assert abs(math.log(2)/lam-HL)<1e-9
assert abs(rows[573][3]-.5)<.002
print(out/'ciclo_c14.csv')
