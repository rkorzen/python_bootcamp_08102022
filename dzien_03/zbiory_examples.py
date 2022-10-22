# pusty zbiór

pusty = set()

# tworzenie zbiorow
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# A = set([1, 2, 3, 4])
# B = set([3, 4, 5, 6])

print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(A ^ B)

# x = {[1, 2]}

print(dir(A))
#  'add', 'clear', 'copy', 'difference',
#  'difference_update', 'discard', 'intersection',
#  'intersection_update', 'isdisjoint',
#  'issubset', 'issuperset', 'pop',
#  'remove', 'symmetric_difference',
#  'symmetric_difference_update', 'union', 'update'

print(A | B)
print(A.intersection_update(B))
print(A)

A.add(10)
A.add(10)
A.add(10)
A.add(10)
A.add(10)
A.add(10)

print(A)


X = {5, 6}

print(B.issubset(X))
print(X.issubset(B))


print(B.issuperset(X))
print(X.issuperset(B))

Y = X = {5, 6}
print(Y.issubset(X))
print(X.issubset(Y))

range(10)  # od 0 do 9

range(2, 100) # od 2.. 99
print(set(range(1, 100, 2))) # 1, 3.., 99
print(len([1, 2, 3]))
print(len(range(100)))


x = frozenset([1,2 ,3])
print(x)


# wyrażenia listowe itp - idiomy pythonowe

[x for x in range(100) if x % 3 == 0]

lista = []
for x in range(100):
    if x % 3 == 0:
        lista.append(x)


print({x for x in range(100) if x % 3 == 0},
      {x:x**2 for x in range(100) if x % 3 == 0})

print((x for x in range(100) if x % 3 == 0))


