import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_name_square():
    assert Square(1).get_name == 'Квадрат'

def test_area_square():
    assert round(Square(10).area()) == round(100)
    assert round(Square(5).area()) == round(25)

def test_perimeter_square():
    assert round(Square(10).perimeter) == round(40)
    assert round(Square(5).perimeter) == round(20)


def test_sum_area():
    assert round(Square(10).add_area(Square(10))) == round(200)
    assert round(Square(10).add_area(Rectangle(10, 5))) == round(150)
    assert round(Square(10).add_area(Triangle(10, 5, 10))) == round(150)
    