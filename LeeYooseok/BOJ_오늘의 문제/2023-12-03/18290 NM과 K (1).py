N, M, K = map(int, input().split())
board = []

max_num = -1e9

for _ in range(N):
    y_board = list(map(int, input().split()))
    max_num = max(max_num, max(y_board))
    board.append(y_board)

visited = [[False for _ in range(M)] for _ in range(N)]

answer = -1e9


def brute_force(_visited, total, cnt):
    global answer

    if cnt == K:
        answer = max(answer, total)
        return
    else:
        # back-tracking
        if total + max_num * (K - cnt) <= answer:
            return

    for _y in range(N):
        for _x in range(M):
            if visited[_y][_x]:
                continue

            if _y - 1 >= 0 and visited[_y - 1][_x]:
                continue

            if _x - 1 >= 0 and visited[_y][_x - 1]:
                continue

            if _y + 1 < N and visited[_y + 1][_x]:
                continue

            if _x + 1 < M and visited[_y][_x + 1]:
                continue

            visited[_y][_x] = True
            brute_force(visited, total + board[_y][_x], cnt + 1)
            visited[_y][_x] = False

for _y in range(N):
    for _x in range(M):
        visited[_y][_x] = True
        brute_force(visited, board[_y][_x], 1)
        visited[_y][_x] = False

print(answer)