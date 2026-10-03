import json,os,runpy
os.environ['METHOD']='hf'
runpy.run_path('scripts/quantum_scan.py')
x=json.load(open('data/generated/quantum_hf.json',encoding='utf-8'))
assert x['converged'] and x['method']=='hf' and x['lumo_hartree']>x['homo_hartree'] and x['gap_hartree']>0 and len(x['geometry_angstrom'])==3
