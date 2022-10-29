# napisz rozwiązanie poniższych testów


def suma(*args, **kwargs):
    result = 0
    for el in args:
        if isinstance(el, (list, set)):
            result += sum(el)
        elif isinstance(el, dict):
            result += sum(el.values())
        else:
            result += el

    for k, v in kwargs.items():
        result += sum(v)
    return result


def test_suma_no_parameters():
    assert suma() == 0


def test_suma_with_numeric_parameters():
    assert suma(1) == 1
    assert suma(1, 2, 3) == 6


def test_suma_with_list_parameters():
    assert suma([1]) == 1
    assert suma([1, 2, 3]) == 6
    assert suma(1, [1, 2, 3]) == 7


def test_suma_with_dict():
    # assert suma({1: 2, 2: 3}) == 5
    # assert suma(1, {1: 2, 2: 3}) == 6
    # assert suma(1, [1, 2], {1: 2, 2: 3}) == 9
    # assert suma(1, [1, 2], {"a": 2, "b": 3}) == 9
    assert suma(1, [1, 1], [1, 2], {1: 2, 2: 3}, a={1, 2, 3}) == 17
#
# # v1
# assert suma(1) == 1
# assert suma(1, 2, 3) == 6
#
# # v2
# assert suma(1, [1, 1], [1, 2], {1: 2, 2: 3}) == 11
#
# # v3
# assert suma(1, [1, 1], [1, 2], {1: 2, 2: 3}, a={1, 2, 3}) == 11
#
