
def foo(a):
    print(a)
    if a == 100:
        return a
    return foo(a+1)

foo(1)

def silnia(n):
    if n < 0:
        raise ValueError("n musi byc wieksze od 0")
    if n == 0:
        return 1
    return n * silnia(n-1)

print(silnia(-5))
