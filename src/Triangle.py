# Родитель для классов фигур
from .Figure import Figure

class Triangle(Figure):
    """
    h - высота
    w - гипотенуза
    f - основание
    """
    
    __name = "Треугольник"

    def __new__(cls, *args, **kwargs):
        """
        Разрешается создать объект класса, только в том случае, 
        если будет передано три аргумента и их тип число.
        """
        try:
            if len(kwargs) != 0 or kwargs != {}:
                return None

            if len(args) == 3:
                for i in args:
                    if isinstance(i , int) or isinstance(i, float):
                        pass
                    else:
                        return None
                return super().__new__(cls)

            else:
                return None
        except Exception as e:
            Exception(f"Ошибка - {e}")
            return None

    def __init__(self, h, w, f):
        self.h = h
        self.w = w
        self.f = f

    @property
    def get_name(self):
        return self.__name

    @property
    def area(self):
        return 0.5 * (self.h * self.f)

    @property
    def perimeter(self):
        return self.h + self.w + self.f
