def sum(a,b,n):
    a*=n
    b*=n
    a+=b//100
    b%=100
    return a,b
n = int(input("kol-vo"))
a=int(input("cost a "))
b=int(input("cost b "))
print(*sum(a,b,n))
