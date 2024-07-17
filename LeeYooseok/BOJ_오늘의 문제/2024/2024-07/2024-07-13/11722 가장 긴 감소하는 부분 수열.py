import sys

input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

dp = [1 for _ in range(N)]  # dp[i] = i 인덱스 까지 확인했을 때, 가장 길이가 긴 감소하는 부분 수열의 길이

for i in range(N):
    for j in range(i):
        if num_list[j] > num_list[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))