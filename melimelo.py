def meli_melo_temporel0(lieux, n, etapes, v):
    #print(lieux)
    #print(etapes)
    a = 0
    b = 0
    for etape in etapes:
        if (etape["voyageur"] == 1):
            a = get_decalage(lieux, etape["destination"])
        else:
            b = get_decalage(lieux, etape["destination"])
        print(str(absolute(b - a)))

def get_decalage(lieux, id):
    for lieu in lieux:
        if (lieu["id"] == id):
            return lieu["decalage"]

def absolute(x):
    if (x < 0):
        return x * -1
    return x

n = int(input())
liste_p = [None] * n
for i in range(0, n):
    (id, decalage) = list(map(int, raw_input().split()))
    lieux_i = {"id":id, "decalage":decalage}
    liste_p[i] = lieux_i
v = int(input())
liste_e = [None] * v
for j in range(0, v):
    (voyageur, destination) = list(map(int, raw_input().split()))
    etape_i = {"voyageur":voyageur, "destination":destination}
    liste_e[j] = etape_i
meli_melo_temporel0(liste_p, n, liste_e, v)
