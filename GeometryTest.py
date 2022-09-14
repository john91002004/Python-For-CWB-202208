from math import pi
import unittest
from Geometry import Circle, Rectangle, Square, Triangle

class CircleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.c = Circle(5)
        return super().setUp()

    def testCircleArea(self):
        self.assertEqual(self.c.area, 25 * pi) 

    def testCirclePerimeter(self): 
        self.assertEqual(self.c.perimeter, 10 * pi)

class SquareTest(unittest.TestCase): 

    def setUp(self) -> None:
        self.s = Square(5) 
        return super().setUp()

    def testSquareArea(self): 
        self.assertEqual(self.s.area, 25)

    def testSquarePerimeter(self):
        self.assertEqual(self.s.perimeter, 20)

class RectangleTest(unittest.TestCase): 

    def setUp(self) -> None:
        self.r = Rectangle(3,2) 
        return super().setUp()

    def testRectangleArea(self): 
        self.assertEqual(self.r.area, 6)

    def testRectanglePerimeter(self): 
        self.assertEqual(self.r.perimeter, 10)

class TriangleTest(unittest.TestCase): 

    def setUp(self) -> None:
        self.t = Triangle(3,4,5)
        return super().setUp()

    def testTriangleArea(self):
        self.assertEqual(self.t.area, 6)

    def testTrianglePerimeter(self):
        self.assertEqual(self.t.perimeter, 12)


if __name__ == '__main__': 
    unittest.main(verbosity=4)
