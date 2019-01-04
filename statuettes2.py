import time

def motif_indice(motif, i):
    return motif.index(i + 1) + 1

def motif_sign(motif, i):
    return sign(motif_indice(motif, i + 1) - motif_indice(motif, i))

def sign(a):
    if (a < 0):
        return -1
    else:
        return 1

def statuettes0(motif, n, tailles, m):
    start = time.time()
    result = []

    to_check_later = []

    # +/- sur tout le tableau
    for i in range(m - n + 1):
        x = 0
        while (sign(tailles[i + x + 1] - tailles[i + x]) == motif_sign(motif, x)):
            x += 1
            if (x == n - 1):
                to_check_later.append(i)
                break

    # On traite maintenant les données fitrées
    for i in to_check_later:
        for x in range(n):
            current = i + x
            # On calcul l'index à cet position
            smaller = 0
            for j in range(n):
                if (n != x):
                    if (tailles[i + j] < tailles[current]):
                        smaller += 1

            if (motif_indice(motif, x) != smaller + 1):
                break
            elif (motif_indice(motif, x) == smaller + 1 and n - 1 == x):
                result.append(str(i + 1))
    print(time.time() - start, "secondes verif")


    print(str(len(result)))
    print(" ".join(result))
    print(time.time() - start, "seconds")

(n, m) = list(map(int, input().split()))
motif = list(map(int, input().split()))
tailles = list(map(int, input().split()))
statuettes0(motif, n, tailles, m)
