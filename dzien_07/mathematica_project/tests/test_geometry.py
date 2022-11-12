from mathematica.geometry.figures import square_area, triangle_area


def test_square_area():
    assert square_area(1) == 1
    assert square_area(10) == 100
    assert square_area(0) == 0


def test_triangle_area():
    assert triangle_area(2, 2) == 2
    assert triangle_area(5, 10) == 0.5 * 5 * 10
