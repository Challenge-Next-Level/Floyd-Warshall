cost = int(input())

INF = float('inf')
if cost == 1 or cost == 3: # 기본 거스름돈(1 ~ 3원)일 때는 따로 처리
    print(-1)
elif cost == 2:
    print(1)
else: # 4원 이상 부터 계산하여 구할 수 있음
    dp = [INF] * (cost + 1)
    dp[2] = 1
    idx = 4
    while idx <= cost:
        if idx % 5 == 0:  # 5원으로 나눠 떨어지는 것
            dp[idx] = idx // 5
        else: # 그렇지 않은 것, dp를 통해 계산
            for i in range(idx - 1, 1, -1):
                if dp[i] != INF and dp[idx - i] != INF:
                    dp[idx] = dp[i] + dp[idx - i]
                    break
        idx += 1
    if dp[cost] == INF:
        print(-1)
    else:
        print(dp[cost])