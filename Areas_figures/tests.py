import unittest
import math
from area import Circle,Triangle, ShapeFactory

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=3)
        self.assertAlmostEqual(circle.area(), math.pi * 9, places=5)

    def test_triangle_area(self):
        triangle = Triangle(a=3, b=4, c=5)
        s = (3 + 4 + 5) / 2
        expected_area = math.sqrt(s * (s - 3) * (s - 4) * (s - 5))
        self.assertAlmostEqual(triangle.area(), expected_area, places=5)

    def test_right_angle_triangle(self):
        triangle = Triangle(a=3, b=4, c=5)
        self.assertTrue(triangle.is_right_angle())

        triangle = Triangle(a=5, b=12, c=13)
        self.assertTrue(triangle.is_right_angle())

        triangle = Triangle(a=6, b=8, c=10)
        self.assertTrue(triangle.is_right_angle())

        triangle = Triangle(a=3, b=4, c=6)
        self.assertFalse(triangle.is_right_angle())

    def test_create_circle(self):
        shape = ShapeFactory.create_shape('circle', 5)
        self.assertIsInstance(shape, Circle)
        self.assertEqual(shape.radius, 5)

    def test_create_triangle(self):
        shape = ShapeFactory.create_shape('triangle', 3, 4, 5)
        self.assertIsInstance(shape, Triangle)
        self.assertEqual(shape.a, 3)
        self.assertEqual(shape.b, 4)
        self.assertEqual(shape.c, 5)
