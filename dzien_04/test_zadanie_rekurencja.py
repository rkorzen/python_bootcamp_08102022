from zadanie_rekurencja import splaszcz

# def test_foo():
#     assert False

def test_splaszcz_pusta_lista():
    assert splaszcz([]) == []

def test_splaszcz_plaska_lista():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]

def test_splaszcz_zagniezdzona_lista():
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]
    # assert zadanie_rekurencja.splaszcz([1, [[2, 3]]]) == [1, 2, 3]
    assert splaszcz([1, [[2, 3]]]) == [1, 2, 3]
