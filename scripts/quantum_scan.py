import json,os
from pathlib import Path
from pyscf import gto,dft,scf

method=os.getenv('METHOD','hf').lower()
mol=gto.M(atom='O 0 0 0; H 0 0 0.757; H 0.586 0 -0.379',basis='sto-3g',unit='Angstrom',verbose=0)
if method=='hf':
 r=scf.RHF(mol).run()
else:
 r=dft.RKS(mol);r.xc=method;r=r.run()
Path('data/generated').mkdir(parents=True,exist_ok=True)
o={'system':'H2O','method':method,'basis':'sto-3g','energy_hartree':r.e_tot,'converged':bool(r.converged)}
Path(f'data/generated/quantum_{method}.json').write_text(json.dumps(o,indent=2),encoding='utf-8')
assert o['converged']
print(json.dumps(o))
