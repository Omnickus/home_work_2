import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle

"""
Triangle(h, w, f)
Где h-высота, w-гипотенуза, f-основание
"""

def test_name_triangle():
    assert Triangle(1, 1, 1).get_name == 'Треугольник'

def test_area_triangle():
    assert round(Triangle(1, 1, 1).area) == round(0.5)
    assert round(Triangle(10, 5, 10).area) == round(50)
    assert round(Triangle(7, 2, 5).area) == round(18)

def test_perimeter_triangle():
    assert round(Triangle(10, 10, 10).perimeter) == round(30)
    assert round(Triangle(5, 2, 7).perimeter) == round(14)


def test_sum_area():
    assert round(Triangle(10, 8, 4).add_area(Square(10))) == round(120)
    assert round(Triangle(10, 9, 3).add_area(Rectangle(10, 5))) == round(65)
    assert round(Triangle(10, 5, 3).add_area(Triangle(10, 5, 10))) == round(65)
    
def test_broken_object_triangle():
    assert Triangle('2') == None
    assert Triangle({}) == None
    assert Triangle([]) == None
    assert Triangle('gg') == None
    assert Triangle(1,2,'2') == None
    assert type(Triangle(2.2, 1, 45)) == type(Triangle(2.2, 5, 6.8))
    assert type(Triangle(2, 4.1, 5.3)) == type(Triangle(2, 4, 5))
