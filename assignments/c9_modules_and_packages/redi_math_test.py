# Exercise:
# Write a package with modules so that all tests work
# Hint: You can copy the functions for computing areas and circumferences from Lesson 7

import math
import pytest
import redi_math.geometry.rectangle
from redi_math.geometry.circle import get_circumference, get_area
import redi_math.arithmetics.basic as basic


def test_get_rectangle_area():
    test_width = 20
    test_height = 10
    expected_area = 200
    # Check whether the calculated area of the function matches our expected area
    assert(redi_math.geometry.rectangle.get_area(test_height, test_width) == expected_area)


def test_get_rectangle_area_value_error():
    test_width = -10
    test_height = -5
    with pytest.raises(ValueError):
        redi_math.geometry.rectangle.get_area(test_height, test_width)


def test_get_circle_area():
    """Check that calculation of circle area with valid input yields expected result."""
    radius = 3
    expected_area = math.pi * 9
    calculated_area = get_area(radius)

    assert calculated_area == expected_area


def test_get_circle_area_invalid_input():
    """Check that calculation of circle area fails for negative radius."""
    with pytest.raises(ValueError):
        get_area(radius=-2.)


def test_get_circle_circumference():
    """Check that calculation of circle circumference with valid input yields expected result."""
    radius = 3
    expected_circumference = 2. * math.pi * 3

    calculated_circumference = get_circumference(radius)

    assert calculated_circumference == expected_circumference


def test_get_circle_circumference_invalid_input():
    """Check that calculation of circle circumference fails for negative radius."""
    with pytest.raises(ValueError):
        get_circumference(radius=-2.)


def test_add():
    """Check that two numbers are correctly added."""
    assert basic.add(1, -5) == -4


def test_multiply():
    """Check whether two numbers are correctly multiplied."""
    assert basic.multiply(3, 4) == 12
