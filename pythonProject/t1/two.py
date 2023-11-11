def step(k, x)->float:
   return 1/(k*(k+x))
def cntstep(k)->float:
    return (1/k) - (1/(k+1))
"""def series(n, x)->float:
    s = float(0)
    for k in range(1, n+1):
        s+=step(k, x)
    return s
def contseries(n):
    s = 0
    for k in range(1, n+1):
        s+=cntstep(k)
    return s"""
def resSerias(n,x)->float:
    s=0
    for k in range(1,n+1):
        s+=step(k,x)-cntstep(k)
    return s
"""def gen():
    x=0
    float(x)
    for i in range(10):
        x+=0.1
        yield x"""

x = [round(0.1*i, 1) for i in range(11)]
print(x)
n = int(input("n "))


for i in x:
    print (f"для {i} результат равен {resSerias(n,i)} \n")
