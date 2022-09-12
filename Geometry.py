from math import pi


class Circle: 
    
    def __init__(self, radius): 
        self.radius = radius 
        self.calArea()
        self.calPerimeter()

    def calArea(self):
        self.area = pi * self.radius ** 2 

    def calPerimeter(self):
        self.perimeter = 2 * pi * self.radius