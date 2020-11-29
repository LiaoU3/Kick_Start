T = int(input())
for case in range(1, T + 1):
    N = int(input())
    As = list(map(int, input().split()))
    h = 0
    point = ""
    citations = [0] * (N + 1)
    new_citations = 0
    for A_i in As:
        if A_i > h:
            if A_i >= len(citations):
                citations[N] += 1
            else:
                citations[A_i] += 1
            if new_citations == citations[h]:
                h += 1
                new_citations = 0
            else:
                new_citations += 1
        point += ' ' + str(h)
    print("Case #{}:{}".format(case, point))