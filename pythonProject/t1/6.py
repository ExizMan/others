#14
import copy
n=int(input('n'))
n-=2
x1,x2=1,1
a=[x1,x2]
temp=0
while(n!=0):
    print(f"{x1} + {x2}")
    a.append(x2 + x1)
    temp=x1+x2
    x1=copy.copy(x2)
    x2=temp
    n -= 1
print(a)