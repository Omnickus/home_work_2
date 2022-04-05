# Родитель для классов фигур
try:
    from Figure import Figure
except:
    from .Figure import Figure

class Rectangle(Figure):

    name = "Прямоугольник"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * ( self.width + self.height )