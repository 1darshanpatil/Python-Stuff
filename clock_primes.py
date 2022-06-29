import sympy as smp
import numpy as np

def form(h, m):
    h, m = str(h), str(m)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    return f'{h}:{m}'
        
hr = np.arange(25)
mn = np.arange(1, 60, 2)
ls = []
for h in hr:
    for m in mn:
        if smp.isprime(int(str(h) + str(m))):
            ls.append(form(h, m))
print(np.array(ls))