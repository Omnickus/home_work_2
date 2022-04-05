import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def test_name_circle():
    assert Circle(1).name == 'Круг'

def test_area_circle():
    assert round(Circle(10).area()) == round(314.159)
    assert round(Circle(5).area()) == round(78.539816)

def test_perimetr_circle():
    assert round(Circle(10).perimeter) == round(62.83185307179586)
    assert round(Circle(5).perimeter) == round(31.41592653589793)


def test_sum_area():
    assert round(Circle(10).add_area(Square(10))) == round(414.159)
    assert round(Circle(10).add_area(Rectangle(10, 5))) == round(364.159)
    assert round(Circle(10).add_area(Triangle(10, 5, 10))) == round(364.159)

def test_perimetr_circle_with_fixture(area_for_all_figure):
    assert round(area_for_all_figure[0].perimeter) == round(area_for_all_figure[1])