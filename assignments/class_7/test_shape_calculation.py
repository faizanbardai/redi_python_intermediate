# 1. Go to 'File > Settings > Tools > Python Integrated Tools > Testing' in PyCharm and
# select 'pytest' as your default test runner.
#
# 2. You might need to install pytest to your python environment of this project.
# For this go to 'File > Settings > Project: ... > Python Interpreter'. There you will
# see a list of all installed packages. Press the '+' symbol in the bottom-left.
# In the popup window you should now type 'pytest' and install the selected package.
#
# 3. At this point you should be able to run pytest in .py files that start with
# 'test_' or end with '_test.py' by right-clicking the window and selecting
# 'Run pytest in test_shape_calculation.py'

import math
import pytest
import shape_calculation

# In pytest we write functions to test different aspects of our code.
# Running pytest then gives a report on which test functions passed
# and which failed.

# This a regular test, where you compare the expected result to the actual result.


def test_get_rectangle_area():
    test_width = 20
    test_height = 10
    expected_area = 200
    # Check whether the calculated area of the function matches our expected area
    assert(shape_calculation.get_rectangle_area(
        test_height, test_width) == expected_area)


def test_get_rectangle_area_value_error():
    test_width = -10
    test_height = -5
    with pytest.raises(ValueError):
        shape_calculation.get_rectangle_area(test_height, test_width)


def test_get_triangle_area():
    test_base = 5
    test_height = 4
    expected_area = 10
    assert(shape_calculation.get_triangle_area(
        test_base, test_height) == expected_area)


def test_get_triangle_area_value_error():
    test_base = -20
    test_height = 20
    with pytest.raises(ValueError):
        shape_calculation.get_triangle_area(test_base, test_height)


def test_get_circle_area():
    test_radius = 3
    expected_area = math.pi * 3 * 3
    assert(shape_calculation.get_circle_area(test_radius) == expected_area)


def test_get_circle_area_value_error():
    test_radius = -3
    with pytest.raises(ValueError):
        shape_calculation.get_circle_area(test_radius)


def test_get_circle_circumference():
    test_radius = 3
    expected_area = 2 * math.pi * 3
    assert(shape_calculation.get_circle_circumference(
        test_radius) == expected_area)


def test_get_circle_circumference_value_error():
    test_radius = -3
    with pytest.raises(ValueError):
        shape_calculation.get_circle_circumference(test_radius)
