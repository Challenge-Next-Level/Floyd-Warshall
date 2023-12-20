from itertools import combinations
from collections import deque

N, M = map(int, input().split())

board = list()

loc_zero = list()
for _y in range(N):
    y_board = list(map(int, input().split()))

    for _x in range(M):
        if y_board[_x] == 0:
            loc_zero.append([_x, _y])
    board.append(y_board)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, visited):
    dq = deque()
    dq.append([y, x])
    visited[y][x] = True
    kill_count = 1

    flag = False

    while dq:
        now_y, now_x = dq.pop()
        for i in range(4):
            new_y, new_x = now_y + dy[i], now_x + dx[i]

            if not (0 <= new_y < N) or not (0 <= new_x < M):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == 0:
                flag = True

            if board[new_y][new_x] == 2:
                visited[new_y][new_x] = True
                kill_count += 1
                dq.append([new_y, new_x])

    if flag:
        return 0
    else:
        return kill_count


def baduk(stone):
    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for x, y in stone:
        board[y][x] = 1

    for c_y in range(N):
        for c_x in range(M):
            if board[c_y][c_x] == 2 and not visited[c_y][c_x]:
                cnt += bfs(c_x, c_y, visited)

    for x, y in stone:
        board[y][x] = 0

    return cnt


answer = 0
for comb in combinations(loc_zero, 2):
    answer = max(answer, baduk(comb))

print(answer)
