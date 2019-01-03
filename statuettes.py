#coding: utf-8

def get_indices(arr):
    indices = [0] * len(arr)
    sorted = list(arr)
    sorted.sort()

    for i in range(len(arr)):
        indices[i] = sorted.index(arr[i]) + 1

    return indices

def get_indices2(arr):
    indices = [0] * len(arr)

    for i in range(len(arr)):
        smaller = 1
        for j in range(len(arr)):
            if (i != j):
                if (arr[j] < arr[i]):
                    smaller += 1
        indices[i] = smaller

    return indices


def get_indices_image(arr):
    indices = [0] * len(arr)

    for i in range(1, len(arr) + 1):
        index = arr.index(i)
        indices[i - 1] = index + 1

    return indices

def statuettes0(motif, n, tailles, m):
    result = []

    if (len(motif) <= len(tailles)):
        target = get_indices_image(motif)
        for i in range(len(tailles) - len(motif) + 1):
            order = get_indices(tailles[i:i+len(motif)])
            if (order == target):
                result.append(str(i + 1))
            #print(str(i * 100 / float(len(tailles) - len(motif) + 1)) + "%")

    print(str(len(result)))
    print(" ".join(result))

(n, m) = list(map(int, raw_input().split()))
motif = list(map(int, raw_input().split()))
tailles = list(map(int, raw_input().split()))
statuettes0(motif, n, tailles, m)
