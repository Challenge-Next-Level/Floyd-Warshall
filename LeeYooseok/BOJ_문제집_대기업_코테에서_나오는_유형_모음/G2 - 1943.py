import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())

    coin_list = list()
    total_money = 0

    for _ in range(N):
        value, count = map(int, input().split())

        coin_list.append([value, count])
        total_money += (value * count)

    if total_money % 2 == 1:
        print(0)
        continue

    total_money //= 2
    dp = [True] + [False] * total_money

    answer = 0
    for i in range(N):
        value, count = coin_list[i]

        for n in range(total_money, value - 1, -1):
            if dp[n - value]:
                for j in range(count):
                    if n + value * j <= total_money:
                        dp[n + value * j] = True
                    else:
                        break

        if dp[-1]:
            answer = 1
            break

    print(answer)