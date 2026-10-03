import math,runpy
runpy.run_path('scripts/ciclo_c14.py')
assert abs(math.log(2)/(math.log(2)/5730)-5730)<1e-9
