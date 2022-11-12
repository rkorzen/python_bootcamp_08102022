import argparse

# import sys
# dane_wejsciowe = sys.argv[1]
# v1:
# if len(sys.argv) > 2:
#     plik_wyjsciowy = sys.argv[2]
#
# v2
# try:
#     plik_wyjsciowy = sys.argv[2] = sys.argv[2]
# except IndexError:
#     plik_wyjsciowy = None


parser = argparse.ArgumentParser(
    prog='Read Logs',
    description='Zlicza czas',
    epilog='Zapraszamy do współpracy')

parser.add_argument('infile')  # positional argument
parser.add_argument('outfile', nargs="?", help="Optional output file")  # positional argument
# parser.add_argument("xxx", type=int, nargs="?")
# parser.add_argument("yyy", nargs="?" )

args = parser.parse_args()
dane_wejsciowe = args.infile
plik_wyjsciowy = args.outfile

# print(args.xxx, type(args.xxx))

user_total_time = {}
user_last_login = {}

with open(dane_wejsciowe) as f:
    for line in f:
        dane = line.strip().split(";")
        user = dane[0]
        action = dane[1]
        t = int(dane[2])

        # user, action, t = line.strip().split(";")
        # t = int(t)

        if action == "LOGIN":
            user_last_login[user] = t
        elif action == "LOGOUT":
            user_total_time[user] = user_total_time.get(user, 0) + t - user_last_login[user]


def to_numeric(pair):
    return int(pair[0][5:])


# dane = [1, [2, 3, [4, 5]]]
# print(dane[1])
# print(dane[1][2])
# print(dane[1][2][0])
#
# d1 = dane[1]
# d2 = d1[2]
# d3 = d2[0]
# print(d3)

def second(x):
    return x[1]


# print(user_total_time.items())
# print(sorted(user_total_time.items()))
print(sorted(user_total_time.items(), key=to_numeric))
# print(sorted(user_total_time.items(), key=lambda x: x[1], reverse=True))

if plik_wyjsciowy:
    with open(plik_wyjsciowy, "w") as f:
        f.write("Czas przebywania w systemie:\n")
        for user, time in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
            f.write(f" - {user:7}: {time}\n")
    print(f"Dane zapisano w {plik_wyjsciowy}")
else:
    print("Czas przebywania w systemie:")
    for user, time in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
        print(f" - {user:7}: {time}")
