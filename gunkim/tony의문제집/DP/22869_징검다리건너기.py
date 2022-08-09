# python3 는 시간초과 발생, pypy3로 제출해야함
import sys
n, k = map(int, sys.stdin.readline().split())
A = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n+1)]
dp[1] = 1 # 시작 위치는 갈 수 있음

for i in range(1, n): # 해당 위치에서 갈 수 있는 곳 탐색
    if dp[n] == 1:
        break
    if dp[i] == 1: # 우선 이곳으로 올 수 있는지 체크
        for j in range(i+1, n+1):
            if dp[n] == 1:
                break
            if dp[j] == 1:
                continue
            if (j-i) * (1+abs(A[i]-A[j])) <= k: # 최대 에너지를 초과하지 않는 이동이라면 체크
                dp[j] = 1

if dp[n] == 1:
    print('YES')
else:
    print('NO')