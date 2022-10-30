"""

Zaimplementuj klasę `Vector` dostarczającą funkcjonalność wektora
swobodnego na dwuwymiarowej płaszczyźnie.
Wektory powinny
mieć możliwość dodawania, odejmowania, mnożenia (przez inny
wektor i przez liczbę), porównywania (po długości) oraz powinny
posiadać czytelną reprezentację napisową.
Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2

"""
import pytest

# korzeniewski@gmail.com

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) == int:
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    # def

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


class TestVector:

    def test_init(self):
        v = Vector(x=1, y=2)
        assert str(v) == "Vector(1, 2)"

    def test_equality_of_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 3)
        v3 = Vector(2, 3)

        assert v1 != v2
        assert v2 == v3

    def test_sum_of_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 3)
        v3 = Vector(3, 5)

        assert v1 + v2 == v3

    def test_sum_of_two_vectors(self):
        v1 = Vector(1, 2)
        v2 = Vector(2, 3)
        v3 = Vector(-1, -1)

        assert v1 - v2 == v3

    def test_multiply_vector_by_scalar(self):
        v = Vector(3, 5)
        assert v * 5 == Vector(15, 25)
        assert 5 * v == Vector(15, 25)

    def test_multiply_vector_by_vector(self):
        v1 = Vector(3, 5)
        v2 = Vector(3, 5)
        with pytest.raises(TypeError):
            v1 * v2

    @pytest.mark.skip("We will decide what should be returned in that situation")
    def test_multiply_vector_by_vector_expected_failure(self):
        v1 = Vector(3, 5)
        v2 = Vector(3, 5)
        v3 = Vector(0, 0)
        assert v1 * v2 == v3

    def test_vectors_comparission(self):
        v1 = Vector(1, 1)
        v2 = Vector(1, 2)
        v3 = Vector(1, 1)
        assert v2 > v1
        assert v2 >= v1
        assert not v1 > v2
        assert not v1 >= v2

        assert not v2 < v1
        assert not v2 <= v1

        assert v1 < v2
        assert v1 <= v2

        assert v1 <= v3
        assert v3 >= v1

    def test_length(self):
        v = Vector(3, 4)
        assert v.length() == 5
