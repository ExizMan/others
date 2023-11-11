from c1 import C1

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        pass

    def perimeter(self):
        pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def fill(self, color):
        self.color = color

    def compare(self, other):
        return self.square() == other.square()

    def is_intersect(self, other):
        pass

    def is_include(self, other):
        pass