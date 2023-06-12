"""
Operator overloading is a feature of Python that allows you to define the behavior of built-in operators (+, -, *, /, etc.) for custom classes. 
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Output: <__main__.Vector object at 0x7fc7f1033cd0>
print(v1 - v2)  # Output: <__main__.Vector object at 0x7fc7f1033f40>

v1 = Vector(1, 2)
print(v1 * 2)  # Output: <__main__.Vector object at 0x7fc7f1033cd0>
