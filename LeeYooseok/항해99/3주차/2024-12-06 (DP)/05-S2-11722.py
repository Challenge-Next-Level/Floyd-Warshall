import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if data[j] > data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# dp[-1]은 정답값이 아님
print(max(dp))
