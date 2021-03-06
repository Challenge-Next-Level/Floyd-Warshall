"""
- 0 부터 n 마리까지, 가둘 수 있음 (끝에 닿는거( = 이전단계 이전개수 끝에 안닿는거 * 2 + 이전단계 이전개수 끝에 닿는거) + 끝에 안닿는거(이전단계 동일개수))
    - 2*0 = 1(0+1)
    - 2*1 = 1(0+1) + 2
    - 2*2 = 1 + 4(2 + 2) + 2 = 1 + 6
    - 2*3 = 1 + 6(2 + 4) + 8(6(4 + 2) + 2) + 2 = 1 + 16
    - 2*4 = 1 + 8(2 + 6) + 18(10(8 + 2) + 8) + 12(10 + 2) + 2 = 41
    - 2*5 = 1 + 10(2 + 8) + 32(14(6*2 + 2) + 18) + 38(26(8*2 + 10)+12) + 16(14+2) + 2
"""

n = int(input())

# (n+1) X (n+1) 매트릭스
dp = [[[0, 0]] * (n + 1) for _ in range(n + 1)]


for i in range(n + 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = [0,1]
        elif j == i:
            dp[i][j] = [2, 0]
        else:
            dp[i][j] = [dp[i - 1][j - 1][1] * 2 + dp[i - 1][j - 1][0], sum(dp[i - 1][j])]
            # dp[i][j][0] = dp[i - 1][j - 1][1] * 2 + dp[i - 1][j - 1][0]
            # dp[i][j][1] = sum(dp[i - 1][j])

    print(dp[i])

result = 0

for d in dp[n]:
    result += sum(d)

print(result)
