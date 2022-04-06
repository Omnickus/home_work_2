# Родитель для классов фигур
try:
    from Figure import Figure
except:
    from .Figure import Figure

class Square(Figure):

    __name = "Квадрат"

    def __init__(self, width):
        self.width = width

    @property
    def get_name(self):
        return self.__name

    def area(self):
        return self.width * self.width

    @property
    def perimeter(self):
        return self.width * 4


