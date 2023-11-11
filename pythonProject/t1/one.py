import numpy as np
import math as m
pi = m.pi
def series(a,nn):
    s = 0
    for n in range(0, nn):
        s += (m.pow(-1,n)*m.pow(x, 2*n+1))/(m.factorial(n)*(2*n+1))
    return s

def rval(a,n):
    return 2/(m.sqrt(pi))*series(a,n)

#a = float(input('Введите a'))
x = float(input('Введите x \n'))
n = int(input('Введите n \n'))
res = rval(x, n)
print(f"res,,{x} m.erf(x)")
print("\n",res-m.erf(x))