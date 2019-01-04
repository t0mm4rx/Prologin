#coding; utf-8

import math

processed = []

def la_meilleure_ville0(villes, n, lignes, m, gares, g):

    for ville in range(1, n + 1):
        for to in range(1, n + 1):
            if (ville != to):
                get_fastest_path(ville, to, villes, lignes, gares)


    for ville in range(1, n+1):
        average = 0
        nb = 0
        for target in range(1, n+1):
            if (target != ville):
                tmps = get_fastest_path(ville, target, villes, lignes, gares)
                if (tmps != -1):
                    average += tmps
                    nb += 1
        if (nb > 0):
            print(int(math.floor(average / nb)))
        else:
            print('-1')


def get_fastest_path(a, b, villes, lignes, gares, exclude=[-1]):

    for p in processed:
        if (p['from'] == a and p['to'] == b and p['exclude'] == (-1 in exclude)):
            return p['tmps']

    # En direct
    direct = get_ligne(a, b, lignes)
    if (direct != -1):
        direct += get_retard(a, villes)

    # Avec un intermédiaire par gare routière
    indirect_gares = -1
    for i in range(1, len(villes) + 1):
        if (i != a and i != b):
            a_i = get_ligne(a, i, gares)
            i_b = get_ligne(i, b, lignes)
            if (a_i != -1 and i_b != -1):
                indirect_gares = get_retard(a, villes) + a_i + i_b

    # En passant par une ville intermédiaire, fn récursive
    min_indirect = -1
    for i in range(1, len(villes) + 1):
        if (i != a and i != b and not (i in exclude)):
            if (-1 in exclude):
                tmps_a_i = get_fastest_path(a, i, villes, lignes, gares, [a, b])
                tmps_i_b = get_fastest_path(i, b, villes, lignes, gares, [a, b])
            else:
                rule = exclude
                rule.append(i)
                tmps_a_i = get_fastest_path(a, i, villes, lignes, gares, rule)
                tmps_i_b = get_fastest_path(i, b, villes, lignes, gares, rule)

            if (tmps_a_i != -1 and tmps_i_b != -1):
                if (min_indirect != -1 and tmps_a_i + tmps_i_b < min_indirect):
                    min_indirect = tmps_a_i + tmps_i_b
                if (min_indirect == -1):
                    min_indirect = tmps_a_i + tmps_i_b

    results = []
    if (direct != -1):
        results.append(direct)
    if (min_indirect != -1):
        results.append(min_indirect)
    if (indirect_gares != -1):
        results.append(indirect_gares)
    if (len(results) == 0):
        processed.append({'from': a, 'to': b, 'tmps': -1, 'exclude': (-1 in exclude)})
        return -1
    else:
        processed.append({'from': a, 'to': b, 'tmps': min(results), 'exclude': (-1 in exclude)})
        return min(results)


# Ligne classique
def get_ligne(a, b, lignes):
    result = []
    for ligne in lignes:
        if (ligne['depart'] == a and ligne['arrivee'] == b):
            result.append(ligne['temps'])
    if (len(result) != 0):
        return min(result)
    else:
        return -1

def get_lignes_from(a, lignes):
    result = []
    for ligne in lignes:
        if (ligne['depart'] == a):
            result.append(ligne)
    if (len(result) != 0):
        return result
    else:
        return -1

def get_retard(ville, villes):
    return villes[ville - 1]


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
