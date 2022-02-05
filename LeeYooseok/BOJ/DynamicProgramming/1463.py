"""
n이 주어질때, 1을 뺀 경우, 2로 나누어 떨어지는 경우, 3으로 나누어 떨어지는 경우 중 가능한 경우의 수 중, 최솟값 + 1
"""
# 0,1,2,3의 결과
dp = [0, 0, 1, 1]

num = int(input())

for n in range(4, num + 1):
    if n % 2 == 0 and n % 3 != 0:
        dp.append(min(dp[n - 1], dp[n // 2]) + 1)
    elif n % 2 != 0 and n % 3 == 0:
        dp.append(min(dp[n - 1], dp[n // 3]) + 1)
    elif n % 2 == 0 and n % 3 == 0:
        dp.append(min(dp[n - 1], dp[n // 3], dp[n // 2]) + 1)
    else:
        dp.append(dp[n - 1] + 1)

print(dp[num])
