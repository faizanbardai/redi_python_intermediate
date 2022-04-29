# 1. Create an Circle class that has one instance variable named “radius”.
# 2. Add a method to calculate and print the area of the circle.
#   a. The area of a circle is calculated by multiplying Pi by the square of the radius: Pi x r2
# 3. Rework your Circle class so that the area is calculated during initialization and stored in an “area” attribute.


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.area = self.calculate_area()  # not a good approach

    def calculate_area(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(5)
    print(circle.area)
    circle.radius = 6  # see, the circle area doesn't change even though radius is updated
    print(circle.area)
    print(circle.calculate_area())
