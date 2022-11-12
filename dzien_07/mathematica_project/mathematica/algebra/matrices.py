
# def add_matrices(m1, m2):
#     result = []
#     for i_row in range(len(m1)):
#         row = []
#         for i_col in range(len(m1[i_row])):
#             row.append(m1[i_row][i_col] + m2[i_row][i_col])
#         result.append(row)
#     return result

def add_matrices(m1, m2):
    result = []
    for row_a, row_b in zip(m1, m2):
        row = []
        for col_a, col_b in zip(row_a, row_b):
            row.append(col_a + col_b)
        result.append(row)
    return result



lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
lista3 = [3, 4, 5, 6]

for a, b, c in zip(lista1, lista2, lista3):
    print(a + b + c)


def sub_matrices(m1, m2):
    pass