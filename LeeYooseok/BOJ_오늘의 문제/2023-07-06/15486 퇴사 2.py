N = int(input())

t, p = [0], [0]
for _ in range(N):
    t_i, p_i = map(int, input().split())
    t.append(t_i)
    p.append(p_i)

dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = max(dp[i], dp[i - 1])  # 이전까지의 최댓값
    fin_date = i + t[i] - 1  # 당일 포함
    if fin_date <= N:  # 최종일 안에 일이 끝나는 경우
        # i일부터는 일을 해야하므로 i일에 얻을 수 있는 최댓값이 아닌 i-1일까지 얻을 수 있는 최댓값을 구한다
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + p[i])

print(max(dp))