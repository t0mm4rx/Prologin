def arnaque_aerienne0(prix_initial, billets, n):
    count = 0
    for billet in billets:
        if (billet < prix_initial):
            count += 1
    if (count >= 3):
        print("ARNAQUE !")
    else:
        print("Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos !")

prix_initial = int(input())
n = int(input())
billets = list(map(int, raw_input().split()))
arnaque_aerienne0(prix_initial, billets, n)
