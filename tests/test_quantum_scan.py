import json,os,runpy
os.environ['METHOD']='hf'
runpy.run_path('scripts/quantum_scan.py')
x=json.load(open('data/generated/quantum_hf.json',encoding='utf-8'))
assert x['converged'] and x['method']=='hf' and x['lumo_hartree']>x['homo_hartree'] and x['gap_hartree']>0 and len(x['geometry_angstrom'])==3
os.environ['SYSTEM']='c2'
runpy.run_path('scripts/quantum_scan.py')
y=json.load(open('data/generated/quantum_c2_hf.json',encoding='utf-8'))
assert y['converged'] and y['system']=='C2' and len(y['geometry_angstrom'])==2
os.environ['SYSTEM']='ring6'
runpy.run_path('scripts/quantum_scan.py')
z=json.load(open('data/generated/quantum_ring6_hf.json',encoding='utf-8'))
assert z['converged'] and len(z['geometry_angstrom'])==6
