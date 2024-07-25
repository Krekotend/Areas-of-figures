from dataclasses import dataclass
import math


# Базовый класс площади
@dataclass
class Shape:
    def area(self):
        pass


@dataclass
class Circle(Shape):
    radius: float

    def area(self):
        return math.pi * self.radius ** 2


@dataclass
class Triangle(Shape):
    a: float
    b: float
    c: float

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)


# Создание фигуры
class ShapeFactory:

    @staticmethod
    def create_shape(shape_type, *args):
        shapes = {'circle': Circle,
                  'triangle': Triangle}
        return shapes[shape_type](*args)

# Пример
# circle = ShapeFactory.create_shape('circle', 7)
# print(circle.area())
# triangle = ShapeFactory.create_shape('triangle',3,4,5)
# print(triangle.area())
# print(triangle.is_right_angle())