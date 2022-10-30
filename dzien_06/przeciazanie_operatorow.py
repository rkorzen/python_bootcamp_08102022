
# 1 + "1"

class MyInt:

    def __init__(self, value: int or str):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def __add__(self, other):
        # return MyInt(self.value + other.value)
        if type(other) == int:
            return self.__class__(self.value + other)
        if type(other) == str:
            return self.__class__(self.value + int(other))
        elif type(other) == self.__class__:
            return self.__class__(self.value + other.value)

        return NotImplemented

    def __eq__(self, other):
        if type(other) == int:
            return self.value == other
        elif type(other) == self.__class__:
            return self.value == other.value
        else:
            return False

    def __radd__(self, other):
        return self.__add__(other)
        # return MyInt.__add__(self, other)

    def __ne__(self, other): pass
    def __gt__(self, other): pass  # >
    def __ge__(self, other): pass  # >=



# print(MyInt(2) + 2)



def test_MyInt():
    assert MyInt(1)
    assert MyInt("2")

    assert MyInt(2) == 2
    # assert MyInt(2) == "2"



def test_add_to_MyInt_instances():
    assert MyInt(1) + MyInt(2) == MyInt(3)
    assert MyInt(2) + 2  == MyInt(4)
    assert MyInt(2) + "3" == MyInt(5)
    assert 2 + MyInt(2)== MyInt(4)

