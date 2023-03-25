N, T = map(int, input().split())

class_list = list()

for _ in range(N):
    class_list.append(list(map(int, input().split())))

dp = [[0] * (T + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, T + 1):
        time, score = class_list[i - 1]

        # 해당 과목을 공부할 수 없으면
        if j < time:
            dp[i][j] = dp[i - 1][j]
        # 해당 과목을 공부할 수 있으면
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - time] + score)

print(dp[N][T])
