print(dir())
import sys

# print(sys.path)
# sys.path.append("/Users/rkorzen/PycharmProjects/szkolenia/python_bootcamp_08102022/dzien_07")

# import modul_b
# print(dir(modul_b))
# # from .. import modul_c
#
# from subfolder import modul_c
# print(dir(modul_c))
# print(modul_c.__package__)
# # print(x)
# import subfolder.modul_c
# subfolder.modul_c.x
# print("Działa")

import modul_b

from modul_b import Osoba
# from modul_b import *
print(dir())