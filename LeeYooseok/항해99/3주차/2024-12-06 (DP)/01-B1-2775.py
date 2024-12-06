import sys

input = sys.stdin.readline

T = int(input())

user_input_list = list()
max_k, max_n = 0, 0
for _ in range(T):
    k = int(input())
    n = int(input())
    max_k = max(max_k, k)
    max_n = max(max_n, n)
    user_input_list.append([k, n])

dp = [[i for i in range(max_n + 1)] for _ in range(max_k + 1)]

for _k in range(1, max_k + 1):
    for _n in range(1, max_n + 1):
        if _n == 1:
            dp[_k][_n] = dp[_k - 1][_n]
        else:
            dp[_k][_n] = (dp[_k][_n - 1] + dp[_k - 1][_n])

for k, n in user_input_list:
    print(dp[k][n])
