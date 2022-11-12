from mathematica.algebra.matrices import add_matrices, sub_matrices



def test_add_matrices():
    m1 = [[1, 2]]
    m2 = [[2, 2]]
    assert add_matrices(m1, m2) == [[3, 4]]

    m1 = [
        [1, 2],
        [3, 4],
    ]
    m2 = [
        [2, 2],
        [2, 2]
    ]

    assert add_matrices(m1, m2) == [
        [3, 4],
        [5, 6]
    ]

def test_sub_matrices():
    m1 = [[1, 2]]
    m2 = [[2, 2]]
    assert sub_matrices(m1, m2) == [[-1, 0]]
