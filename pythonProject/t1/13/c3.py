from math import sqrt
from shape import Shape


class C3(Shape):
    def __init__(self, x, y, param1):
        super().__init__(x, y)
        self.param1 = param1

    def square(self):
        return (self.param1**2)/5 * sqrt(25+10*sqrt(5))

    def perimeter(self):
        return self.param1 * 5


    def additionalMethod1(self):
        pass

    def additionalMethod2(self):
        pass
