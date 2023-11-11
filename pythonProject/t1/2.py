"""def find(l):
    r=l[0]
    for i in l:
        if i<r:
            r=i
    return r
klass = list(map(int,input().split()))
print(find(klass))"""
a=int(input())
b=int(input())
c=int(input())
if a<b:
    if a<c:
        print(a)
    else:
        print(c)
else:
    if b<c:
        print(b)
    else:
            print(c)