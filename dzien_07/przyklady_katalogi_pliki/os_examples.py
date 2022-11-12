import logging

import os
from pathlib import Path



print(os.getcwd())
print(os.listdir())

os.chdir("/Users/rkorzen/PycharmProjects/szkolenia/python_bootcamp_08102022/dzien_07/")

print(os.getcwd())
print(os.listdir())

print(help(os.listdir))

print(dir(os))


base_path = Path(os.getcwd())
x = base_path / "xxx"

print(x.exists())
x.mkdir(exist_ok=True)

f = x / "text.txt"

print(f)
print(dir(f))

with f.open("w") as fp:
    fp.write("cos tam")

print(f.read_text())
f.write_text("zmieniam zawartosc pliku")

print(list(f.parent.parent.glob("*.py")))



