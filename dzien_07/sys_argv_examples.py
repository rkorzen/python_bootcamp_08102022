import os
import sys

print(os.getcwd())

print(sys.argv)  # to jest lista w której sa argumenty.

a = 1
b = 2
print("Hello world!")

with open(sys.argv[1]) as in_f:
    data = in_f.read()
print(data)