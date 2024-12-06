import sys

input = sys.stdin.readline

N = int(input())
number_list = list(map(int, input().split()))

dp = [number for number in number_list]

for i in range(1, N):
    now_number = number_list[i]
    for j in range(i):
        prior_number = number_list[j]

        # 증가하는 수열이라면, dp 갱신
        if now_number > prior_number:
            dp[i] = max(dp[i], dp[j] + now_number)

print(max(dp))