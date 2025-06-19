import math

class Polygon:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height    

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length 
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2 

# Driver code
t = Triangle(10, 5)
print("Triangle area:", t.area())

r = Rectangle(5, 10)
print("Rectangle area:", r.area())

s = Square(5)
print("Square area:", s.area())

c = Circle(7)
print("Circle area:", round(c.area(), 2))
