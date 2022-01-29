from circle_functions.radius_function import radius_length
from math import sqrt

def test_radius():
    assert radius_length(3, 4) == sqrt(3 ** 2 + 4 ** 2)
