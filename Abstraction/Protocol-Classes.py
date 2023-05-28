from typing import Protocol, List, Union

class Drawable(Protocol):
    def draw(self) -> None:
        """Draws the object on the screen"""

class Circle:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self) -> None:
        print(f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius}")

class Rectangle:
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self) -> None:
        print(f"Drawing a rectangle at ({self.x}, {self.y}) with dimensions {self.width} x {self.height}")

def draw_shapes(shapes: List[Drawable]) -> None:
    for shape in shapes:
        shape.draw()

circle = Circle(10, 20, 5)
rectangle = Rectangle(30, 40, 15, 25)

draw_shapes([circle, rectangle])  # Works fine, as both Circle and Rectangle implement Drawable

class Square:
    def __init__(self, side_length: float):
        self.side_length = side_length

    @property
    def area(self) -> float:
        return self.side_length ** 2

class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    @property
    def area(self) -> float:
        return 0.5 * self.base * self.height

class Draggable(Protocol):
    def drag(self, x: float, y: float) -> None:
        """Drags the object to a new location"""

def perform_actions(shape: Union[Drawable, Draggable]) -> None:
    shape.draw()
    shape.drag(10, 20)
