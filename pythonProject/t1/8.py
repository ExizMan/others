from math import sqrt
def dist(p1,p2)->float:
    xdif=pow(p2[0]-p1[0],2)
    ydif=pow(p2[1]-p1[1],2)
    return sqrt(xdif+ydif)


p1= list(map(float,input().split()))
p2= list(map(float,input().split()))
print(dist(p1,p2))
