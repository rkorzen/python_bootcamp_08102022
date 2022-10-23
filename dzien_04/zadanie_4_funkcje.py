"""

Bez posługiwania się wbudowanymi funkcjami takimi jak max czy min

napisz funkcję (a może funkcje) która zwróci max z trzech liczb

"""

def max_of_two(a: int, b: int) -> int:
    if a > b:
        return a
    return b

def max_of_three(a: int, b: int, c: int) -> int:
    return max_of_two(a, max_of_two(b, c))

if __name__ == "__main__":
    assert max_of_three(1, 3, 2) == 3
    assert max_of_three(2, 6, -5) == 6
