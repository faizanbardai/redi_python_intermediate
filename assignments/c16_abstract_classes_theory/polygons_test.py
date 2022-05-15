# change the import according to your module name
from polygons_solution import Rectangle, Vector, RightTriangle


def test_rectangle_area_calculation():
    v1 = Vector(0, 2)
    v2 = Vector(3, 0)
    r1 = Rectangle(v1, v2)
    assert 6.0 == r1.calculate_area()

    v3 = Vector(-1, 2)
    v4 = Vector(3, 0)
    r2 = Rectangle(v3, v4)
    assert 8.0 == r2.calculate_area()

    v5 = Vector(9, 9)
    v6 = Vector(9, 0)
    r3 = Rectangle(v5, v6)
    assert 0.0 == r3.calculate_area()


def test_rectangle_to_string():
    v1 = Vector(0, 10)
    v2 = Vector(7.77, 2)
    v3 = Vector(0, 2.222)
    v2.add(v3)
    r1 = Rectangle(v1, v2)
    assert "Rectangle spanned by points [0.0, 10.0] and [7.8, 4.2]." == str(r1)


def test_rectangle_shift_by_vector():
    v1 = Vector(0, 2)
    v2 = Vector(3, 0)
    r1 = Rectangle(v1, v2)
    shift_vector = Vector(-2, -1.5)
    r1.shift_by(shift_vector)
    assert "Rectangle spanned by points [-2.0, 0.5] and [1.0, -1.5]." == str(r1)


def test_triangle_area_calculation():
    v1 = Vector(0, 2)
    v2 = Vector(3, 0)
    t1 = RightTriangle(v1, v2)
    assert 3.0 == t1.calculate_area()

    v3 = Vector(-1, 2)
    v4 = Vector(3, 0)
    r2 = RightTriangle(v3, v4)
    assert 4.0 == r2.calculate_area()

    v5 = Vector(9, 9)
    v6 = Vector(9, 0)
    r3 = RightTriangle(v5, v6)
    assert 0.0 == r3.calculate_area()


def test_triangle_to_string():
    v1 = Vector(0, 10)
    v2 = Vector(7.77, 2)
    v3 = Vector(0, 2.222)
    v2.add(v3)
    t1 = RightTriangle(v1, v2)
    assert "Triangle spanned by points [0.0, 10.0], [7.8, 4.2] and [0.0, 4.2]." == str(t1)


def test_triangle_shift_by_vector():
    v1 = Vector(0, 2)
    v2 = Vector(3, 0)
    t1 = RightTriangle(v1, v2)
    shift_vector = Vector(-2, -1.5)
    t1.shift_by(shift_vector)
    assert "Triangle spanned by points [-2.0, 0.5], [1.0, -1.5] and [-2.0, -1.5]." == str(t1)
