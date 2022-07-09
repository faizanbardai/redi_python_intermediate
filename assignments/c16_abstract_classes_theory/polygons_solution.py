from abc import ABC, abstractmethod


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(float(x), 1)
        self.y = round(float(y), 1)

    def add(self, vector: 'Vector') -> None:
        self.x += round(float(vector.x), 1)
        self.y += round(float(vector.y), 1)


class Polygon(ABC):
    @abstractmethod
    def calculate_area(self) -> None:
        pass

    @abstractmethod
    def shift_by(self) -> None:
        pass


class Rectangle(Polygon):
    def __init__(self, v1: Vector, v2: Vector):
        self.v1 = v1
        self.v2 = v2

    def calculate_area(self) -> float:
        return abs((self.v2.x - self.v1.x) * (self.v2.y - self.v1.y))

    def shift_by(self, shift_vector: Vector) -> None:
        self.v1.add(shift_vector)
        self.v2.add(shift_vector)

    def __str__(self) -> str:
        return f"Rectangle spanned by points [{self.v1.x}, {self.v1.y}] and [{self.v2.x}, {self.v2.y}]."


class RightTriangle(Polygon):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def calculate_area(self) -> float:
        return abs((self.v2.x - self.v1.x) * (self.v2.y - self.v1.y) / 2)

    def shift_by(self, shift_vector: Vector) -> None:
        self.v1.add(shift_vector)
        self.v2.add(shift_vector)

    def __str__(self) -> str:
        return f"Triangle spanned by points [{self.v1.x}, {self.v1.y}], [{self.v2.x}, {self.v2.y}] and [{self.v1.x}, {self.v2.y}]."
