
def formatuj(*teksty: tuple[str], **kwargs: dict[str]) -> str:
    tekst = "\n".join(teksty)
    for k in kwargs:
        tekst = tekst.replace(f"${k}", str(kwargs[k]))
    return tekst

def test_formatuj_no_keywords():
    assert formatuj("$a $b $d") == "$a $b $d"

def test_formatuj_with_keyword():
    assert formatuj("$a $b $d", b=10) == "$a 10 $d"
    assert formatuj("$a $b $d", a=1, b=2, c=20, d=30) == "1 2 30"
    assert formatuj("$a $b", a=1, b=2, c=20, d=30) == "1 2"

def test_formatuj_many_input_texts():
    assert formatuj("$a $b", "$a $d", a=1, b=2, c=20, d=30) == """1 2
1 30"""


