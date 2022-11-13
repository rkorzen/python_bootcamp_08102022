from main import spalanie, koszt


def test_spalanie():
    assert spalanie(spalanie_na_100=5, dystans=0) == 0
    assert spalanie(spalanie_na_100=5, dystans=100) == 5
    assert spalanie(spalanie_na_100=5, dystans=200) == 10


def test_koszt():
    assert koszt(0, 5) == 0
    assert koszt(5, 0) == 0
    assert koszt(0, 0) == 0
    assert koszt(5, 5) == 25
    assert koszt(10, 5.85) == 58.50
