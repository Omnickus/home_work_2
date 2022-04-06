# Родитель для классов фигур
try:
    from Figure import Figure
except:
    from .Figure import Figure

class Triangle(Figure):
    """
    h - высота
    w - гипотенуза
    f - основание
    """
    
    __name = "Треугольник"

    def __init__(self, h, w, f):
        self.h = h
        self.w = w
        self.f = f

    @property
    def get_name(self):
        return self.__name

    def area(self):
        return 0.5 * (self.h * self.f)

    @property
    def perimeter(self):
        return self.h + self.w + self.f


