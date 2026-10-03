from math import exp,log
from pathlib import Path
L=5730.0
o=Path('data/generated');o.mkdir(parents=True,exist_ok=True)
with (o/'decaimento.csv').open('w',encoding='utf-8') as f:
 f.write('tempo_anos,fracao,atividade_relativa\n')
 for t in range(0,30001,100):
  a=exp(-log(2)*t/L);f.write(f'{t},{a:.12g},{log(2)/L*a:.12g}\n')
print(o/'decaimento.csv')
