def deluge(h, n, y):
    for i in y:
        if (i < h):
            return 1
    return 0


h = int(input())
n = int(input())
y = list(map(int, input().split()))
print(deluge(h, n, y))
