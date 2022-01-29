from circle_functions.radius_function import radius_length

def test_radius():
    assert radius_length(3, 4) == (3 ** 2 + 4 ** 2) ** (1/2)
