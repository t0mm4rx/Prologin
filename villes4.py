import math

inf = 99999999

def la_meilleure_ville0(villes, n, lignes, m, gares, g):
    format_gares()
    for ville in range(1, n + 1):
        av = 0
        nb = 0
        for target in range(1, n + 1):
            if (ville != target):
                t = get_shortest_path(ville, target)
                if (t != -1):
                    av += t
                    nb += 1
        if (nb > 0):
            print(str(int(math.floor(av / nb))))
        else:
            print('-1')

def get_shortest_path(a, b):
    # Cities from 0 to n - 1
    visited = []
    last_node = [0] * n
    cost = [inf] * n

    cost[a - 1] = 0

    current = a - 1


    while (current + 1 != b):
        min = inf
        for i in range(n):
            if (cost[i] < min and not (i in visited)):
                min = i
        if (min == inf):
            #print('Fin')
            break
        current = min
        #print(visited)
        #print(current)

        # Neighbours
        voisins = get_voisins(current + 1)
        for voisin in voisins:
            if (not (voisin in visited)):
                new_cost = cost[current] + voisin['temps']
                i = voisin['ville'] - 1
                if (cost[i] > new_cost):
                    cost[i] = new_cost
                    last_node[i] = current

        visited.append(current)
    #print("Result cost", cost)
    #print("Result path", last_node)
    if (cost[b - 1] == inf):
        return -1
    else:
        return cost[b - 1]

def get_min_pq(arr):
    min = arr[0]
    for a in arr:
        if (a['cost'] < min['cost']):
            min = a
    return min


def get_cost(arr, ville):
    for a in arr:
        if (a['ville'] == ville):
            return a['cost']

def get_cost_object(arr, ville):
    for a in arr:
        if (a['ville'] == ville):
            return a

def set_cost(arr, ville, cost, f):
    for a in arr:
        if (a['ville'] == ville):
            a['cost'] = cost
            a['from'] = f

# On convertit les lignes avec gares routières en lignes normales
def format_gares():
    for l in gares:
        voisins_arr = get_voisins_lignes(l['arrivee'])
        for v in voisins_arr:
            lignes.append({'depart': l['depart'], 'arrivee': v['arrivee'], 'temps': v['temps'] + l['temps']})

def get_trajet(a, b):
    for c in get_voisins(a):
        if (c['ville'] == b):
            return c['temps']
    return None

def get_voisins(ville):
    result = []
    for res in get_voisins_lignes(ville):
        a = False
        for prev in result:
            if (prev['ville'] == res['arrivee']):
                if (prev['temps'] > get_retard(ville) + res['temps']):
                    result.remove(prev)
                    result.append({ 'ville': res['arrivee'], 'temps': get_retard(ville) + res['temps'] })
                    a = True
                    break
                else:
                    break
        if (not a):
            result.append({ 'ville': res['arrivee'], 'temps': get_retard(ville) + res['temps'] })
    return result

def get_retard(ville):
    return villes[ville - 1]

def get_voisins_lignes(ville):
    result = []
    for l in lignes:
        if (l['depart'] == ville and l['depart'] != l['arrivee']):
            result.append(l)
    return result




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
