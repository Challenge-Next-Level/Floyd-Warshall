n = int(input())
nums = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    item = 0
    for j in range(i - 1, -1, -1):
        if nums[j] < nums[i]:
            item = max(item, dp[j])

    dp[i] += item

print(max(dp))