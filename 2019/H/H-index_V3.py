import numpy as np

T = int(input())
case = 0
for _ in range(T):
    case += 1
    N = int(input())
    As = input()
    citations = np.array([int(num) for num in As.split()])

    point = 0
    scores = np.zeros(5, dtype=int)
    print("Case #{}: ".format(case), end = "")
    for i in range(len(citations)):
        if citations[i] > len(citations):
            scores += 1
        else :
            scores[:citations[i]] += 1
        if scores[point] > point :
            point += 1
        if i != len(citations) - 1:
            print(point, end = " ")
        else :
            print(point)