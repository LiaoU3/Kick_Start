def main():
    T = int(input())
    for i in range(1, T + 1):
        # I didn't use the variable N
        N, B = map(int, input().split())
        prices = list(map(int, input().split()))
        sorted_prices = sorted(prices)
        cnt = 0
        for price in sorted_prices:
            B -= price
            if B < 0 :
                break
            cnt += 1
        print('Case #' + str(i) + ': ' + str(cnt))
    

if __name__ == '__main__':
    main()