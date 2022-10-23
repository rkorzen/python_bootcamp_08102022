import sys                 # dodaje sys do bieżącego zasięgu
from sys import path       # dodaje path do bieżącego zasięgu

from sys import path as p  # alias
from sys import *

print(sys.path)
from A import x, foo
from B import x as xb, foo as fb

foo()
print(x)

fb()
print(xb)