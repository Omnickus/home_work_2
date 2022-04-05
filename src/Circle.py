# Родитель для классов фигур
try:
    from Figure import Figure
except:
    from .Figure import Figure

class Circle(Figure):

    name = "Круг"

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius * self.radius) * 3.14159

    @property
    def perimeter(self):
        return (2 * 3.14159) * self.radius


