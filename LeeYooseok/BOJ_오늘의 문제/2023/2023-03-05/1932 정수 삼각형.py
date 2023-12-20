n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for _y in range(1, n):
    for _x in range(_y + 1):
        if _x == 0:
            dp[_y][_x] += dp[_y - 1][_x]
        elif _x == _y:
            dp[_y][_x] += dp[_y - 1][_x - 1]
        else:
            dp[_y][_x] += max(dp[_y - 1][_x - 1], dp[_y - 1][_x])

print(max(dp[n - 1]))

