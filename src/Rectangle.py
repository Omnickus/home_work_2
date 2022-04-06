# Родитель для классов фигур
try:
    from Figure import Figure
except:
    from .Figure import Figure

class Rectangle(Figure):

    __name = "Прямоугольник"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def get_name(self):
        return self.__name

    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * ( self.width + self.height )
