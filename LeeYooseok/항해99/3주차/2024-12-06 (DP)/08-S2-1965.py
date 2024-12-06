n = int(input())
box_size_list = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    now_box_size = box_size_list[i]
    for j in range(i):
        prior_box_size = box_size_list[j]

        if now_box_size > prior_box_size:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
