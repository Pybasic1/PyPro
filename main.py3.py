#homework6

#1
import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height

    def square(self):
        return 0.5 * self.base * self.height


class Parallelogram(Rectangle):
    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def square(self):
        return self.width * self.height


class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        return '\n'.join(str(f) for f in self._figures)


r = Rectangle(0, 0, 10, 20)
c = Circle(10, 0, 10)
p = Parallelogram(1, 2, 20, 30, 45)

scene = Scene()
scene.add_figure(r)
scene.add_figure(c)
scene.add_figure(p)

print("Total square:", scene.total_square())

#2

import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __contains__(self, point):
        distance_squared = (point.x - self.x) ** 2 + (point.y - self.y) ** 2
        return distance_squared <= self.radius ** 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

c1 = Circle(1, 2, 10)
p1 = Point(1, 2)

print(Point(1, 2) in Circle(1, 2, 10))
print(p1 in c1)