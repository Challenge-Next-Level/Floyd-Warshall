T = int(input())

for _ in range(T):
    N = int(input())
    stock_price_list = list(map(int, input().split()))

    max_price = 0
    answer = 0
    for i in range(N - 1, -1, -1):
        now_price = stock_price_list[i]

        if now_price > max_price:
            max_price = now_price
        else:
            answer += (max_price - now_price)

    print(answer)