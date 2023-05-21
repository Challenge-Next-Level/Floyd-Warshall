while True:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        exit()

    board = [list(map(int, input().split())) for _ in range(N)]

    answer = 0

    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for _y in range(1, N + 1):
        for _x in range(1, M + 1):
            if board[_y - 1][_x - 1] == 1:
                dp[_y][_x] = min(dp[_y - 1][_x - 1], dp[_y - 1][_x], dp[_y][_x - 1]) + 1
                answer = max(answer, dp[_y][_x])

    print(answer)
