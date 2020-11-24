T = int(input())
case = 0
for _ in range(T):
    case += 1
    N = int(input())
    citation = input()
    citations = [int(num) for num in citation.split()]

    score = 0
    print("Case #{}: ".format(case), end = "")
    for i in range(len(citations)):
        cnt = 0
        for j in range(i+1):
            if citations[j] > score:
                cnt += 1
        if cnt > score :
            score += 1
        if i != len(citations) - 1:
            print(score, end = " ")
        else :
            print(score)