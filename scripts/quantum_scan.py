import json,os
from pathlib import Path
from pyscf import gto,dft,scf

method=os.getenv('METHOD','hf').lower(); system=os.getenv('SYSTEM','h2o').lower()
atoms={'h2o':'O 0 0 0; H 0 0 0.757; H 0.586 0 -0.379','c2':'C 0 0 0; C 1.242 0 0','c4':'C 0 0 0; C 1.28 0 0; C 2.56 0 0; C 3.84 0 0','ring6':'C 1.40 0 0; C 0.70 1.212 0; C -0.70 1.212 0; C -1.40 0 0; C -0.70 -1.212 0; C 0.70 -1.212 0','tetra4':'C 0 0 0; C 1.54 0 0; C 0.513 1.451 0; C 0.513 0.484 1.368'}
mol=gto.M(atom=atoms[system],basis='sto-3g',unit='Angstrom',verbose=0)
if method=='hf':
 r=scf.RHF(mol);r.max_cycle=200;r=r.run()
else:
 r=dft.RKS(mol);r.xc=method;r.max_cycle=200;r=r.run()
e=list(r.mo_energy);n=mol.nelectron//2
homo=e[n-1];lumo=e[n];
try:
 _,pop=r.mulliken_pop(verbose=0);charges=[float(x) for x in pop]
except Exception:charges=[]
Path('data/generated').mkdir(parents=True,exist_ok=True)
o={'system':system.upper(),'method':method,'basis':'sto-3g','energy_hartree':float(r.e_tot),'converged':bool(r.converged),'homo_hartree':float(homo),'lumo_hartree':float(lumo),'gap_hartree':float(lumo-homo),'charges':charges,'geometry_angstrom':[[float(v) for v in mol.atom_coord(i)] for i in range(mol.natm)]}
Path(f'data/generated/quantum_{system}_{method}.json').write_text(json.dumps(o,indent=2),encoding='utf-8')
assert o['converged']
print(json.dumps(o))
