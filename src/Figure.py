
class Figure:

    __name = "Фигура"

    def __init__(self):
        pass

    def add_area(self, a):
        sum_area = self.area + a.area
        return sum_area

    @property
    def get_name(self):
        return self.__name
