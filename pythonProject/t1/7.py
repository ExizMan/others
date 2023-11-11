def srchVal(listx,x):
    count=0
    for i in listx:
        count+=1
        if i==x:
            return count

s=list(map(int,input("введите список").split()))
x=int(input("введите рост пети"))
s.sort(reverse=True)

sn =s
sn.append(x)
sn.sort(reverse=True)


print(srchVal(sn,x))
