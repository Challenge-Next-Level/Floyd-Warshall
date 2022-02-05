"""
- 입력받은 수를 1,2 의 덧셈으로 나누어 표현하는 방식과 같은 문제
- n
"""
num = int(input())

dp = [0, 1, 2]

for n in range(3, num + 1):
    dp.append((dp[n - 1] + dp[n - 2]) % 10007)

print(dp[num])
