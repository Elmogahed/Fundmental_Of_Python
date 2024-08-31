from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    def info(self): 
        return 'Shape Has a defind area'

class Square(Shape): 
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape): 
    def __init__(self, base, height) -> None:
        super().__init__()
        self.base = base 
        self.height = height

    def area(self):
        return (self.base * self.height) / 2
 

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


square = Square(4)
print(square.area())

triangel = Triangle(6 , 8)
print(triangel.area())

circle = Circle(5)
print(circle.area())

print(square.info())

class Point: 
    def __init__(self, x, y ,z) -> None:
        self.x = x
        self.y = y 
        self.z = z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y , self.z + other.z)
    
    def __str__(self): 
        return f'x: {self.x}, Y: {self.y}, Z: {self.z}'
    
    def __gt__(self, other):
        return self.x + self.y + self.z > other.x + other.y + other.z

pt1 = Point(3, 4, -5)
pt2 = Point(-4, 1, 3)
pt3 = pt1 + pt2

print('\n')
print('=' * 50)
print(pt2 > pt1)
print('\n')
print(pt3)

class Cart:
    def __init__(self, items) -> None:
        self.items = items
    def __getitem__(self, key): 
        return self.items[key]
    

order1 = Cart(['pen', 'pencil', 'notebook'])
print(order1.items[0]) 
print(order1[0])