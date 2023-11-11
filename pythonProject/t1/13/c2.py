from shape import Shape


class C2(Shape):
    def __init__(self, x, y, param1, param2):
        super().__init__(x, y)
        self.param1 = param1
        self.param2 = param2

    def square(self):
        return (self.param1 ** self.param2)/2

    def perimeter(self):
        return (self.param1 + self.param2)*2

    def additionalMethod1(self):
        pass

    def additionalMethod2(self):
        pass