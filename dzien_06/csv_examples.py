import csv

columns = ["A", "B", "C", "D", "E", "F"]
dane = [
    [1, 2, 3, 1, 2, 3],
    [12, 1, 3, 12,],
]

with open("dane.csv", "w") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(columns)
    # for row in dane:
    #     writer.writerow(row)
    writer.writerows(dane)