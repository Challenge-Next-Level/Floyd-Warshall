import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coin_list = [0] + list(map(int, input().split()))
    M = int(input())

    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        coin = coin_list[i]
        if coin > M:
            continue
        dp[i][coin] = dp[i - 1][coin] + 1  # coin 1개로 현재 Money 를 만들 수 있을 때 -> 이전 coin 으로 Money 를 만들 수 있는 방법의 수 + 1
        for money in range(coin + 1, M + 1):
            # dp[i[[money] = i - 1 번째 코인까지 고려했을 시, money를 만들 수 있는 방법의 수 + i 번째 코인까지 고려했을 시, (money - coin) 을 만들 수 있는 방법의 수
            dp[i][money] = dp[i - 1][money] + dp[i][money - coin]

    print(dp[N][M])
