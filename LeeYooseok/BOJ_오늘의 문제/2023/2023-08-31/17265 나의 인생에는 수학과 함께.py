from collections import deque

N = int(input())

board = [list(input().split()) for _ in range(N)]
visited = [[[-1e9, 1e9] for _ in range(N)] for _ in range(N)]
visited[0][0] = [int(board[0][0]), int(board[0][0])]

dx = [[1, 2], [1, 1], [0, 0], [0, 1]]
dy = [[0, 0], [0, 1], [1, 2], [1, 1]]

dq = deque()
dq.append([0, 0, board[0][0]])

while dq:
    now_x, now_y, now_val = dq.pop()

    for i in range(4):
        new_x, new_y = now_x + dx[i][1], now_y + dy[i][1]
        oper_x, oper_y = now_x + dx[i][0], now_y + dy[i][0]

        if not(0 <= new_x < N) or not(0 <= new_y < N) or not(0 <= oper_x < N) or not(0 <= oper_y < N):
            continue

        new_val = int(eval(now_val + board[oper_y][oper_x] + board[new_y][new_x]))

        if visited[new_y][new_x][0] >= new_val and visited[new_y][new_x][1] <= new_val:
            continue

        visited[new_y][new_x][0] = max(visited[new_y][new_x][0], new_val)
        visited[new_y][new_x][1] = min(visited[new_y][new_x][1], new_val)
        dq.append([new_x, new_y, str(new_val)])

print(*visited[N-1][N-1])