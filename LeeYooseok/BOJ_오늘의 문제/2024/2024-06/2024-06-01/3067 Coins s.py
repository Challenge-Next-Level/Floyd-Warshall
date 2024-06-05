T = int(input())
for _ in range(T):
    N = int(input())
    coin_list = [0] + list(map(int, input().split()))
    M = int(input())
    DP = [0 for _ in range(M + 1)]

    for coin in coin_list:
        if coin > M:
            continue
        DP[coin] += 1  # coin 방법 수 + 1
        for i in range(coin + 1, M + 1):  # coin + 다른 동전으로 만드는 경우의 수
            DP[i] += DP[i - coin]

    print(DP[M])