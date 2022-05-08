# 또 못 풀었다. dp를 떠올렸는 데 어떻게 비교를 해야할지 몰랐다
# 뒤에서 부터 dp를 알아내야 겠다 -> 근데 앞의 dp와 비교하려는 멍청한 생각이 있었다
import sys

n = int(sys.stdin.readline())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))

dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    x = i + schedule[i][0] # 오늘 맡은 상담을 하면 끝나는 날 계산
    if x <= n: # 퇴사하려는 날짜 안에 상담을 해야함
        dp[i] = max(dp[i + 1], schedule[i][1] + dp[x])
    else:
        dp[i] = dp[i + 1]
print(dp[0])