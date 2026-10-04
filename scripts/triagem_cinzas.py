import csv,json,re
from pathlib import Path
e={'Ca':40.078,'C':12.011,'O':15.999,'Si':28.085,'K':39.098,'Cl':35.45,'S':32.06,'P':30.974,'H':1.008}
p=[('calcita','CaCO3','carbonato'),('quartzo','SiO2','silicato/óxido'),('hidroxiapatita','Ca5(PO4)3OH','fosfato'),('cal','CaO','óxido'),('cloreto_de_potassio','KCl','cloreto'),('sulfato_de_potassio','K2SO4','sulfato')]
def f(s):
 return {a:int(b or 1) for a,b in re.findall(r'([A-Z][a-z]?)(\d*)',s.replace('(', '').replace(')', ''))}
o=Path('data/generated');o.mkdir(parents=True,exist_ok=True);r=[]
for n,x,c in p:
 z=f(x);m=sum(e[k]*v for k,v in z.items());r.append({'fase':n,'formula':x,'classe':c,'massa_molar_g_mol':round(m,3),'elementos':','.join(z)})
with (o/'triagem_fases_cinzas.csv').open('w',newline='',encoding='utf-8') as q:
 w=csv.DictWriter(q,fieldnames=r[0]);w.writeheader();w.writerows(r)
(o/'triagem_fases_cinzas.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
assert len(r)==6 and all(x['massa_molar_g_mol']>0 for x in r)
print(o/'triagem_fases_cinzas.csv')
