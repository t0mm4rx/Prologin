#coding; utf-8

import math

def la_meilleure_ville0(villes, n, lignes, m, gares, g):

    for villeA in range(1, len(villes)+1):
        score = -1
        connexion_n = 0

        # Pour chacune des autres villes
        for villeB in range(1, len(villes) + 1):
            if (villeA != villeB):
                # On regarde le moyen le plus court de s'y rendre
                # On regarde si il y a une ligne directe
                if (get_ligne(lignes, villeA, villeB) != -1):
                    direct = get_ligne(lignes, villeA, villeB)['temps'] + get_retard(villes, villeA)
                else:
                    direct = -1
                # Sinon on regarde en passant par une autre ville
                indirect = -1
                for villeI in range(1, len(villes) + 1):
                    if (villeI != villeA and villeI != villeB):
                        if (get_ligne(lignes, villeA, villeI) != -1 and get_ligne(lignes, villeI, villeB) != -1):
                            indirect = get_retard(villes, villeA) + get_ligne(lignes, villeA, villeI)['temps'] + get_retard(villes, villeI) + get_ligne(lignes, villeI, villeB)['temps']

                # On regarde maintenant pour les gares routieres
                routieres = -1
                for villeI in range(1, len(villes) + 1):
                    if (villeI != villeA and villeI != villeB):
                        if (get_ligne2(gares, villeA, villeI) != -1 and get_ligne(lignes, villeI, villeB) != -1):
                            routieres = get_retard(villes, villeA) + get_ligne2(gares, villeA, villeI)["temps"] + get_ligne(lignes, villeI, villeB)["temps"]

                min = 0
                if (indirect == -1 and direct != -1):
                    min = direct
                if (direct == -1 and indirect != -1):
                    min = indirect
                if (direct != -1 and indirect != -1 and direct <= indirect):
                    min = direct
                if (direct != -1 and indirect != -1 and direct > indirect):
                    min = indirect

                if (routieres != -1 and min == 0):
                    min = routieres
                if (routieres != -1 and min != -1 and routieres < min):
                    min = routieres

                if (min != 0):
                    connexion_n += 1
                    score += min

        if (connexion_n == 0):
            moy = -1
        else:
            moy = (score + 1) / connexion_n
        print(str(int(math.floor(moy))))


def get_ligne(lignes, a, b):
    for ligne in lignes:
        if (ligne['depart'] == a and ligne['arrivee'] == b):
            return ligne
    return -1

def get_ligne2(gares, a, b):
    for ligne in gares:
        if (ligne['depart'] == a and ligne['arrivee'] == b):
            return ligne
    return -1

def get_retard(villes, ville):
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
