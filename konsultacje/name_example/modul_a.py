import time

a: int = 10

def hello_world():
    print("Hello World")


def long_calculations():
    print("Start calculations")
    time.sleep(0.5)
    print("End calculations")



# print(dir())
# print(globals())
print("Wartoś __name__", __name__)
if __name__ == "__main__":
    hello_world()
    long_calculations()