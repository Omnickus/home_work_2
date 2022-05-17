# Родитель для классов фигур
from .Figure import Figure

class Rectangle(Figure):

    __name = "Прямоугольник"

    def __new__(cls, *args, **kwargs):
        """
        Разрешается создать объект класса, только в том случае, 
        если будет передано два аргумента и их тип число.
        """
        try:
            if len(kwargs) != 0 or kwargs != {}:
                return None

            if len(args) == 2:
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

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def get_name(self):
        return self.__name

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * ( self.width + self.height )
