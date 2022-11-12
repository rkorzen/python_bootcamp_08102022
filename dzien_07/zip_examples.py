
col_1 = 1
col_2 = 2
m1_row_1 = [1, 2]
m1_row_2 = [3, 4]

m1 = [
    m1_row_1,
    m1_row_2
]

m2_row_1 = [5, 6]
m2_row_2 = [7, 8]

m2 = [
    m2_row_1,
    m2_row_2
]


for row in m1:
    print(row)
    for col in row:
        print(col)

for row in m2:
    print(row)
    for col in row:
        print(col)

print("==========")


for row_z_m1, row_z_m2 in zip(m1, m2):
    print(row_z_m1, "wiersz z m1")
    print(row_z_m2, "wiersz z m2")
    print("-------")

    for col_z_m1, col_z_m2 in zip(row_z_m1, row_z_m2):
        print(col_z_m1, "col z m1 z wiersza", row_z_m1)
        print(col_z_m2, "col z m2 z wiersza", row_z_m2)
        print("++++++++++++++++")

