import math
import time

processed = []
debug = False

def la_meilleure_ville0(villes, n, lignes, m, gares, g):
    start = time.time()
    for ville in range(1, n + 1):
        average = 0
        nb = 0
        if (debug):
            print("Ville", ville)
        for target in range(1, n + 1):
            if (target != ville):
                if (debug):
                    print("Target", target)
                t = get_fastest_path(ville, target, [])
                #print(ville, target, t)
                if (t != -1):
                    average += t
                    nb += 1
        if (nb > 0):
            print(int(math.floor(average / nb)))
        else:
            print(-1)
    #print("Ended in", round(time.time() - start, 3), "seconds")

def get_fastest_path(a, b, avoid=[]):

    """
    #print(avoid)
    for p in processed:
        #avoid.sort()
        if (set(p['avoid']) == set(avoid) and p['from'] == a and p['to'] == b):
            #print(a, b, p['result'], avoid, "mem")
            return p['result']
    """
    # Direct
    direct = get_direct(a, b)
    if (direct != -1):
        direct += get_retard(a)

    # 1 intermédiaire gare routière
    smaller_gare = -1
    for i in range(1, n + 1):
        if (i != a and i != b and not (i in avoid)):
            a_i = get_direct_gare(a, i)
            i_b = get_direct(i, b)
            if (a_i != -1 and i_b != -1):
                if (smaller_gare == -1):
                    smaller_gare = get_retard(a) + a_i + i_b
                elif (get_retard(a) + a_i + i_b < smaller_gare):
                    smaller_gare = get_retard(a) + a_i + i_b

    # Par plusieurs intermédiaire
    smaller_inter = -1
    for i in range(1, n + 1):
        if (i != a and i != b and not (i in avoid)):
                filtre = avoid
                if (not (a in avoid)):
                    filtre.append(a)
                if (not (b in avoid)):
                    filtre.append(b)
                a_i = get_fastest_path(a, i, filtre)
                if (a_i != -1):
                    i_b = get_fastest_path(i, b, filtre)
                    if (i_b != -1):
                        if (smaller_inter == -1):
                            smaller_inter = a_i + i_b
                        elif (a_i + i_b < smaller_inter):
                            smaller_inter = a_i + i_b


    results = []
    if (direct != -1):
        results.append(direct)
    if (smaller_gare != -1):
        results.append(smaller_gare)
    if (smaller_inter != -1):
        results.append(smaller_inter)

    if (len(results) > 0):
        if (debug):
            print(a, b, min(results), avoid)
        """
        processed.append({
            'from': a,
            'to': b,
            'result': min(results),
            'avoid': avoid
        })
        """
        return min(results)
    else:
        if (debug):
            print(a, b, '-1', avoid)
        """
        processed.append({
            'from': a,
            'to': b,
            'result': -1,
            'avoid': avoid
        })
        """
        return -1

def has_ligne_from(a, b):
    for line in lignes:
        if (line["depart"] == b and line['arrivee'] == a):
            return True
    return False

def get_retard(a):
    return villes[a - 1]

def get_direct(a, b):
    res = []
    for line in lignes:
        if (line["depart"] == a and line['arrivee'] == b):
            res.append(line["temps"])
    if (len(res) > 0):
        return min(res)
    else:
        return -1

def get_direct_gare(a, b):
    res = []
    for line in gares:
        if (line["depart"] == a and line['arrivee'] == b):
            res.append(line["temps"])
    if (len(res) > 0):
        return min(res)
    else:
        return -1


(n, m, g) = list(map(int, input().split()))
villes = [None] * n
for i in range(0, n):
    villes[i] = int(input())
lignes = [None] * m
for j in range(0, m):
    (depart, arrivee, temps) = list(map(int, input().split()))
    trajet = {"depart":depart, "arrivee":arrivee, "temps":temps}
    lignes[j] = trajet
gares = [None] * g
for k in range(0, g):
    (dep, arr, tmp) = list(map(int, input().split()))
    traj = {"depart":dep, "arrivee":arr, "temps":tmp}
    gares[k] = traj
la_meilleure_ville0(villes, n, lignes, m, gares, g)
