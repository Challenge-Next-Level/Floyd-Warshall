from collections import deque

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False] * C for _ in range(R)]
answer = [0, 0]
def bfs(x, y):
    o_cnt, v_cnt = 0, 0

    visited[y][x] = True
    dq = deque([[x, y]])
    while dq:
        now_x, now_y = dq.popleft()
        if board[now_y][now_x] == 'o':
            o_cnt += 1
        elif board[now_y][now_x] == 'v':
            v_cnt += 1

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not(0 <= new_x < C) or not(0 <= new_y < R):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == '#':
                continue

            visited[new_y][new_x] = True
            dq.append([new_x, new_y])

    if o_cnt > v_cnt:
        answer[0] += o_cnt
    else:
        answer[1] += v_cnt

for _y in range(R):
    for _x in range(C):
        if visited[_y][_x]:
            continue
        if board[_y][_x] == '#':
            continue
        bfs(_x, _y)

print(*answer)