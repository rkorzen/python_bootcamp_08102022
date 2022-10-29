# napisz rozwiązanie poniższych testów

def suma():
    pass

# v1
assert suma(1) == 1
assert suma(1, 2, 3) == 6

# v2
assert suma(1, [1, 1], [1, 2], {1: 2, 2: 3}) == 11

# v3
assert suma(1, [1, 1], [1, 2], {1: 2, 2: 3}, a={1, 2, 3}) == 11