# Родитель для классов фигур
from .Figure import Figure


class Circle(Figure):

    __name = "Круг"

    def __new__(cls, *args, **kwargs):
        """
        Разрешается создать объект класса, только в том случае, 
        если будет передан один аргумент и его тип число.
        """
        try:
            if len(kwargs) != 0 or kwargs != {}:
                return None

            if len(args) == 1:
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

    def __init__(self, radius):
        self.radius = radius

    @property
    def get_name(self):
        return self.__name

    @property
    def area(self):
        return (self.radius * self.radius) * 3.14159

    @property
    def perimeter(self):
        return (2 * 3.14159) * self.radius
