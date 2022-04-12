import math


def get_area(radius):
    # Hint: ou can access the value of pi through the import math module.
    # For this just have to type 'math.pi'
    if radius < 0:
        raise ValueError
    area = math.pi * radius ** 2
    return area


def get_circumference(radius):
    if radius < 0:
        raise ValueError
    area = 2 * math.pi * radius
    return area
