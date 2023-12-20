from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

cnt, max_size = 0, 0

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def check(y, x):
    que = [[y, x]]
    visited[y][x] = 1
    que = deque(que)
    size = 0

    while que:
        now_y, now_x = que.pop()
        size += 1

        for i in range(4):
            new_y, new_x = now_y + dy[i], now_x + dx[i]

            if not(0 <= new_y < N) or not(0 <= new_x < M):
                continue

            if board[new_y][new_x] == 1 and visited[new_y][new_x] == 0:
                visited[new_y][new_x] = 1
                que.append([new_y, new_x])
    return size

for _y in range(N):
    for _x in range(M):
        if board[_y][_x] == 1 and visited[_y][_x] == 0:
            cnt += 1
            max_size = max(max_size, check(_y, _x))

print(cnt)
print(max_size)