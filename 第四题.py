import random
a = [random.random() for i in range(10)]
print(a)
print(max(a))
print(min(a))
a.sort(reverse=True)
print(a)