def manhattan_maboul0(m, jours, n):
    jours.sort()
    max_score = 0
    for i in range(max(jours) + m):
        count = 0
        for a in jours:
            if (a >= i and a <= i + m):
                count += 1

        if (count > max_score):
            max_score = count

    print(max_score)

(n, m) = list(map(int, raw_input().split()))
jours = list(map(int, raw_input().split()))
manhattan_maboul0(m, jours, n)
