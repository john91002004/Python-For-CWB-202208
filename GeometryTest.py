from math import pi
import unittest
from Geometry import Circle

class CircleTest(unittest.TestCase):

    def setUp(self) -> None:
        self.c = Circle(3)
        return super().setUp()

    def testCircleArea(self):
        area = 9 * pi
        self.assertEqual(area, self.c.area)

    def testCirclePerimeter(self):
        perimeter = 6 * pi 
        self.assertEqual(perimeter, self.c.perimeter)


if __name__ == '__main__':
    unittest.main(verbosity=4)