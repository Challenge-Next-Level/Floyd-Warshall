N, M = map(int, input().split())
stone_list = [int(input()) for _ in range(M)]

# dp[i][j] -> i : 현재 위치, j : 현재 속도
# (2*N) ** 0.5 = 마지막에 있는 돌까지 가장 빠르게 갈 수 있는 돌들의 수의 합
# 불필요한 연산을 막기 위한 범위 제한 -> j를 아무 방해없이 갈 수 있는 가장 빠른 속도 까지 제한을 둔다.
# 1, 2, 3, ..., j -> 다 더했을 경우 N
# j(j + 1) / 2 <= N -> j^2 + j <= 2 * N -> j <= sqrt(2 * N)
dp = [[float('inf') for _ in range(int((2 * N) ** 0.5) + 2)] for _ in range(N + 1)]
dp[1][0] = 0

for i in range(2, N + 1):
    # i번째 돌이 작은 돌이면, 못 밟음.
    if i in stone_list:
        continue

    # 속도 : 1 부터 최대 속도 까지
    for j in range(1, int((2 * i) ** 0.5) + 1):
        # dp[i][j] = min(i 번째 돌에 j 의 속도로 올수 있는 경우의 수 들의 값) + 1
        # j - 1 -> j, j -> j, j + 1 -> j
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))
