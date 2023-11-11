def sum(x,y):
    return x+y
def minus(x,y):
    return x-y

a=[sum,minus]
print(a[0](2,1))
class c:
    __slots__ = ('i','f')#ограничение полей, не работает с __dict__
    def __init__(self,x,y):
        self.x=x
        self.y=y

