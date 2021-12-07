import random

a = [random.randint(0, 9) for i in range(10)]
print(a)
a.append(5)
print(a)
a.insert(5, 99)
print(a)
print(max(a))
for f in range(len(a)):
    if f%2:
        print(a[f], end=" ")
