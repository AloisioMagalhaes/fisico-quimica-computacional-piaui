import json,os,runpy
os.environ['METHOD']='hf'
runpy.run_path('scripts/quantum_scan.py')
x=json.load(open('data/generated/quantum_hf.json',encoding='utf-8'))
assert x['converged'] and x['method']=='hf'
