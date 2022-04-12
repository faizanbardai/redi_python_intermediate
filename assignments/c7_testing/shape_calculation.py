# Here we have some functions to calculate
# properties of different 2D shapes.

import math

# Functions related to rectangles


def get_rectangle_area(height, width):
    if height < 0 or width < 0:
        raise ValueError
    area = height * width
    return area


def get_rectangle_circumference(height, width):
    circumference = 2 * height + 2 * width
    return circumference

# Exercise: Functions related to triangles


def get_triangle_area(base, height):
    # Hint: the formula for a triangle with a base b and a height h
    # is b * h / 2 (see https://en.wikipedia.org/wiki/Triangle#Computing_the_area_of_a_triangle)
    if base < 0 or height < 0:
        raise ValueError
    area = 0.5 * base * height
    return area


# Homework: Functions related to circles
def get_circle_area(radius):
    # Hint: ou can access the value of pi through the import math module.
    # For this just have to type 'math.pi'
    if radius < 0:
        raise ValueError
    area = math.pi * radius ** 2
    return area


def get_circle_circumference(radius):
    if radius < 0:
        raise ValueError
    area = 2 * math.pi * radius
    return area
