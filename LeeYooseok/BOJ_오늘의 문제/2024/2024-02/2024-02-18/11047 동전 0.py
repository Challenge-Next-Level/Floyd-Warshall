N, K = map(int, input().split())

coin_list = [int(input()) for _ in range(N)]

answer = 0
coin_idx = N - 1
while K != 0:
    coin = coin_list[coin_idx]

    if coin > K:
        coin_idx -= 1
        continue

    answer += (K // coin)
    K = K % coin

print(answer)