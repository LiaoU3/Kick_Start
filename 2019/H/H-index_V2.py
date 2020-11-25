T = int(input())
case = 0
for _ in range(T):
    case += 1
    N = int(input())
    As = input()
    citations = [int(num) for num in As.split()]

    point = 0
    scores = [0]*N
    print("Case #{}: ".format(case), end = "")
    for i in range(len(citations)):
        if citations[i] > len(citations):
            for j in range(len(scores)):
                scores[j] += 1
        else :
            for j in range(citations[i]):
                scores[j] += 1
        if scores[point] > point :
            point += 1
        if i != len(citations) - 1:
            print(point, end = " ")
        else :
            print(point)