import random
import time

n = 1000000
m = 5
a = int(n / m)

array1 = [0] * n
for i in range(n):
    array1[i] = random.randint(0, n)

array2 = [0] * a
for i in range(a):
    array2[i] = [0] * m
    for j in range(m):
        array2[i][j] = random.randint(0, n)

t = time.time()
array1.sort()
print(time.time() - t, "s")


t = time.time()
for i in range(a):
    array2[i].sort()
print(time.time() - t, "s")
