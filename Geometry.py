from math import pi, sqrt

class Circle: 

    def __init__(self, radius): 
        self.radius = radius
        self.calArea()
        self.calPerimeter()

    def calArea(self):
        self.area = pi * self.radius ** 2 

    def calPerimeter(self):
        self.perimeter = 2 * pi * self.radius 

class Square: 

    def __init__(self, side): 
        self.side = side 
        self.calArea() 
        self.calPerimeter() 

    def calArea(self): 
        self.area = self.side ** 2 

    def calPerimeter(self):
        self.perimeter = 4 * self.side 

class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length 
        self.calArea()
        self.calPerimeter()
    
    def calArea(self): 
        self.area = self.width * self.length 
    
    def calPerimeter(self):
        self.perimeter = 2 * (self.width + self.length)

class Triangle:

    def __init__(self, a, b, c):
        self.a = a 
        self.b = b 
        self.c = c
        self.calPerimeter()
        self.calArea()
    
    def calPerimeter(self): 
        self.perimeter = self.a + self.b + self.c 

    def calArea(self): 
        s = self.perimeter / 2 
        self.area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c) )
    