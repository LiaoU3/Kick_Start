T = int(input())
for x in range(T):
    number = []
    A = list(map(int, input().split()))
    for i in range(len(A)):
        for j in range(A[i]):
            number.append(i + 1)
    even = 0
    odd = 0
    for i in range(len(number)):
        if i %2 == 0:
            even += number[i]
        else:
            odd += number[i]
    if even - odd % 11 == 0:
        y = 'YES'
    else:
        y = 'NO'
    print("Case #{}: {}".format(x, y))
        