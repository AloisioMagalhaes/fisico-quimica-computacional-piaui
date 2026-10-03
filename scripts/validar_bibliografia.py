import csv,json,time,urllib.parse,urllib.request
from pathlib import Path

src=Path('data/bibliografia/shortlist-80.csv');out=Path('data/bibliografia/triagem-80.csv')
rows=[]
for x in csv.DictReader(src.open(encoding='utf-8')):
 d=x['doi'].replace('https://doi.org/','')
 u='https://api.crossref.org/works/'+urllib.parse.quote(d,safe='')
 y={'doi':d,'titulo_candidato':x['title'],'ano_candidato':x['year'],'tema':x['topic'],'url':f'https://doi.org/{d}','status':'erro','titulo_crossref':'','periodico':'','ano_crossref':'','tipo':'','acesso':'manual'}
 try:
  m=json.load(urllib.request.urlopen(u,timeout=20))['message'];t=' '.join(m.get('title',[]))
  y.update(titulo_crossref=t,periodico=(m.get('container-title') or [''])[0],ano_crossref=(m.get('published-print') or m.get('published-online') or {'date-parts':[['']]})['date-parts'][0][0],tipo=m.get('type',''),status='validado')
 except Exception as e:y['status']=f'falha:{type(e).__name__}'
 rows.append(y);time.sleep(.1)
with out.open('w',newline='',encoding='utf-8') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print('validos',sum(x['status']=='validado' for x in rows),'de',len(rows))
