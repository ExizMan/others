from math import sqrt
class Point:
    def __init__(self, x=float(0) ,y=float(0)):
        self.x=x
        self.y=y
    def transport(self,tox,toy):
        self.x+=tox
        self.y+=toy

    def dist(self, point):
        sqrt(self.x**2-point.x**2)
class Shape:

    def __init__(self,point : Point, color="black"):
        self.point=point
        self.color=color

    def square(self):
        print("S=")

    def perimetr(self):
        print("P=")

    def move(self,transportX=0,transportY=0):
        self.point=self.point.transport(transportX,transportY)

    def fill(self,color):
        self.color=color

    def compare(self,x,y):
        print('Comparing')

    def include(self,x,y):
        print('is include')




class rectangl(Shape):

    def __init__(self,point, points:list):
        super().__init__(point)
        self.points = points

    def square(self):
        linever= self.points[0]-self.points[1]
        linevhor= self.points[1]-self.points[2]




