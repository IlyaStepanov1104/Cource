from abc import ABC, abstractmethod
from math import ceil, pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return ceil(pi * self.radius ** 2)
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
        

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return ceil(0.5 * self.base * self.height)
    
    @classmethod
    def from_sides(cls, a, b, c):
        p = (a + b + c) / 2
        area = ceil((p * (p - a) * (p - b) * (p - c)) ** 0.5)
        h = 2 * area / a
        return cls(a, h)

shapes = [Circle(5), Rectangle(4, 6), Square(5), Triangle(4, 6), Triangle.from_sides(3, 4, 5)]
for s in shapes:
    print(s.area())