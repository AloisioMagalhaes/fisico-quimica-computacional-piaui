from pathlib import Path
from pyscf import gto,scf
m=gto.M(atom='O 0 0 0; H 0 0 0.757; H 0.586 0.0 -0.379',basis='sto-3g',unit='Angstrom',verbose=0)
r=scf.RHF(m).run()
Path('data/generated').mkdir(parents=True,exist_ok=True)
Path('data/generated/agua_hf.txt').write_text(f'energia_hartree={r.e_tot}\nconvergente={r.converged}\n',encoding='utf-8')
print(r.e_tot)
