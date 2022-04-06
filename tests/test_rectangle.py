import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_name_rectangle():
    assert Rectangle(1, 1).get_name == 'Прямоугольник'

def test_area_rectangle():
    assert round(Rectangle(10, 10).area()) == round(100)
    assert round(Rectangle(5, 7).area()) == round(35)
    assert round(Rectangle(7, 20).area()) == round(140)

def test_perimetr_rectangle():
    assert round(Rectangle(10, 15).perimeter) == round(50)
    assert round(Rectangle(5, 66).perimeter) == round(142)
    assert round(Rectangle(7, 17).perimeter) == round(48)

def test_sum_area():
    assert round(Rectangle(10, 10).add_area(Square(10))) == round(200)
    assert round(Rectangle(10, 10).add_area(Rectangle(10, 5))) == round(150)
    assert round(Rectangle(10, 10).add_area(Triangle(10, 5, 10))) == round(150)
    