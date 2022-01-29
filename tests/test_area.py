from circle_functions.area_function import circle_area
from math import pi

def test_area():
    assert circle_area(2) == 2 * 2 * pi
