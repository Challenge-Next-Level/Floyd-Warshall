n = int(input())
wine_list = list()
wine_list.append(0)

for _ in range(n):
    wine_list.append(int(input()))

dp = list()
dp.append(0)
dp.append(wine_list[1])
if n > 1:
    dp.append(wine_list[1] + wine_list[2])
for i in range(3, n+1):
    # 현재꺼 안마심, 1번 전 안마심, 2번 전 안마심
    temp_max = max(dp[i-1], dp[i-2] + wine_list[i], dp[i-3] + wine_list[i-1] + wine_list[i])
    dp.append(temp_max)

print(dp[n])
