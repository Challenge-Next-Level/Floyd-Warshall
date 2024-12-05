import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]

answer = [0, 0]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def DFS(x, y):
    v_cnt, k_cnt = 0, 0

    stack = [[x, y]]
    visited[y][x] = True
    if board[y][x] == "v":
        v_cnt += 1
    elif board[y][x] == "k":
        k_cnt += 1

    while stack:
        now_x, now_y = stack.pop()
        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < C) or not (0 <= new_y < R):
                continue

            if board[new_y][new_x] == "#":
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == "v":
                v_cnt += 1
            elif board[new_y][new_x] == "k":
                k_cnt += 1
            visited[new_y][new_x] = True
            stack.append([new_x, new_y])

    if v_cnt >= k_cnt:
        k_cnt = 0
    else:
        v_cnt = 0
    return v_cnt, k_cnt


for _y in range(R):
    for _x in range(C):
        if board[_y][_x] != "#" and not visited[_y][_x]:
            v, k = DFS(_x, _y)
            answer[0] += k
            answer[1] += v

print(*answer)