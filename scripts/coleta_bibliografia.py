import csv,json,re,urllib.parse,urllib.request
from pathlib import Path

qs=[
 'diamond CVD growth methane hydrogen defects',
 'HPHT diamond graphite phase diagram synthesis',
 'density functional theory diamond carbon defects',
 'carbon isotope analysis biomass radiocarbon',
 'cremated bone carbon isotope analysis',
 'carbon 14 diamond betavoltaic battery',
 'betavoltaic nuclear battery semiconductor',
 'diamond radiation detector materials',
 'diamond molecular dynamics carbon sp3',
 'carbon materials battery electronic structure'
]
out=Path('data/bibliografia');out.mkdir(parents=True,exist_ok=True)
z={}
for q in qs:
 u='https://api.openalex.org/works?'+urllib.parse.urlencode({'search':q,'filter':'type:article,from_publication_date:1990-01-01','per-page':100,'mailto':'research@example.org'})
 try:
  d=json.load(urllib.request.urlopen(u,timeout=30))
 except Exception as e:
  print(q,e);continue
 for w in d.get('results',[]):
  doi=w.get('doi');loc=w.get('primary_location') or {};src=loc.get('source') or {}
  if not doi or src.get('type')!='journal':continue
  k=doi.lower();z[k]=dict(doi=doi,title=w.get('title',''),year=w.get('publication_year'),cited=w.get('cited_by_count',0),url=doi,topic=q,authors='; '.join(a.get('author',{}).get('display_name','') for a in w.get('authorships',[])[:8]))
 a=sorted(z.values(),key=lambda x:(-int(x.get('cited') or 0),-(x.get('year') or 0)))
 Path(out/'candidatos.json').write_text(json.dumps(a,ensure_ascii=False,indent=2),encoding='utf-8')
 with (out/'candidatos.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=['doi','title','year','cited','url','topic','authors']);w.writeheader();w.writerows(a)
 with (out/'candidatos.bib').open('w',encoding='utf-8') as f:
  for i,x in enumerate(a,1):
   k='oa'+str(i);au=x['authors'].replace('; ',' and ')
   f.write(f'@article{{{k},\n author={{{au}}},\n title={{{x["title"].replace("{","\\{").replace("}","\\}")}}},\n year={{{x["year"]}}},\n doi={{{x["doi"].removeprefix("https://doi.org/")}}},\n url={{{x["url"]}}}\n}}\n')
 s=[]
 for q in qs:
  s.extend([x for x in a if x['topic']==q][:8])
 s={x['doi'].lower():x for x in s}
 s=sorted(s.values(),key=lambda x:(-int(x.get('cited') or 0),-(x.get('year') or 0)))[:80]
 with (out/'shortlist-80.csv').open('w',newline='',encoding='utf-8') as f:
  w=csv.DictWriter(f,fieldnames=['doi','title','year','cited','url','topic','authors']);w.writeheader();w.writerows(s)
 print('shortlist',len(s))
 print(len(a))
