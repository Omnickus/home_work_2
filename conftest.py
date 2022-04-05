from random import random
import pytest
from src.Circle import Circle
import random

@pytest.fixture()
def area_for_all_figure():
    a = random.randint(1, 20)
    circle = Circle( a )
    right_answer = (2 * 3.14159) * a
    yield circle, right_answer
    del circle, right_answer
