# Родитель для классов фигур
try:
    from Figure import Figure
    from Square import Square
except:
    from .Figure import Figure
    from .Square import Square



class Circle(Figure):

    __name = "Круг"

    def __init__(self, radius):
        self.radius = radius

    @property
    def get_name(self):
        return self.__name

    def area(self):
        return (self.radius * self.radius) * 3.14159

    @property
    def perimeter(self):
        return (2 * 3.14159) * self.radius

