from circle_functions.perimeter_function import circle_perimeter

def test_perimeter():
    assert circle_perimeter(3) == 2 * 3 * 3.14
