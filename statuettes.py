#coding: utf-8

def get_indices(arr):
    indices = [0] * len(arr)
    sorted = list(arr)
    sorted.sort()

    for i in range(len(arr)):
        indices[i] = sorted.index(arr[i]) + 1

    return indices

def get_indices_image(arr):
    indices = [0] * len(arr)

    for i in range(1, len(arr) + 1):
        index = arr.index(i)
        indices[i - 1] = index + 1

    return indices

def sign(a):
    if (a < 0):
        return -1
    else:
        return 1

def statuettes0(motif, n, tailles, m):
    result = []


    if (len(motif) <= len(tailles)):
        target = get_indices_image(motif)
        #print(motif)
        #print(target)
        #print()
        #exit()
        for i in range(len(tailles) - len(motif) + 1):
            #print()
            #print(tailles[i:i+n])
            #print("i", i)
            for x in range(n - 1):
                if (sign(tailles[i + x + 1] - tailles[i + x]) == sign(motif[x + 1] - motif[x])):
                    j = 10
                    break

            j = 0
            while (j < n):
                smaller = 0
                current = i + j

                # Count smallers
                for x in range(n):
                    if (tailles[i + x] < tailles[current]):
                        smaller += 1
                index = n - smaller
                #print(smaller + 1)

                if (smaller + 1 != target[j]):
                    break
                j = j+1
            if (j == n):
                result.append(str(i + 1))




            """
            j = 0
            a = sign(target[j+1] - target[j])
            b = sign(tailles[i+j+1] - tailles[i+j])
            while (a == b):
                if (j == len(motif)):
                    order = get_indices(tailles[i:i+len(motif)])
                    if (order == target):
                        result.append(str(i + 1))

                    break
                j += 1
            """

            #order = get_indices(tailles[i:i+len(motif)])
            #if (order == target):
            #    result.append(str(i + 1))
            #print(str(i * 100 / float(len(tailles) - len(motif) + 1)) + "%")

    print(str(len(result)))
    print(" ".join(result))

(n, m) = list(map(int, input().split()))
motif = list(map(int, input().split()))
tailles = list(map(int, input().split()))
statuettes0(motif, n, tailles, m)
