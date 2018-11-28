def la_meilleure_ville0(villes, n, lignes, m, gares, g):
    print(villes)
    print(lignes)
    print(gares)
    print("")

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
                for villeI in range(len(villes) - 1):
                    if (villeI != villeA and villeI != villeB):
                        if (get_ligne(lignes, villeA, villeI) != -1 and get_ligne(lignes, villeI, villeB) != -1):
                            indirect = get_ligne(lignes, villeA, villeI)['temps'] + get_retard(villes, villeI) + get_ligne(lignes, villeI, villeB)['temps']

                if (indirect == -1 and direct != -1):
                    score += direct
                    connexion_n += 1
                if (direct == -1 and indirect != -1):
                    score += indirect
                    connexion_n += 1

        if (connexion_n == 0):
            moy = -1
        else:
            moy = (score + 1) / connexion_n
        print("Score ville " + str(villeA) + " = " + str(moy))


def get_ligne(lignes, a, b):
    for ligne in lignes:
        if (ligne['depart'] == a and ligne['arrivee'] == b):
            return ligne
    return -1

def get_retard(villes, ville):
    return villes[ville - 1]

(n, m, g) = list(map(int, raw_input().split()))
villes = [None] * n
for i in range(0, n):
    villes[i] = int(input())
lignes = [None] * m
for j in range(0, m):
    (depart, arrivee, temps) = list(map(int, raw_input().split()))
    trajet = {"depart":depart, "arrivee":arrivee, "temps":temps}
    lignes[j] = trajet
gares = [None] * g
for k in range(0, g):
    (dep, arr, tmp) = list(map(int, raw_input().split()))
    traj = {"depart":dep, "arrivee":arr, "temps":tmp}
    gares[k] = traj
la_meilleure_ville0(villes, n, lignes, m, gares, g)
