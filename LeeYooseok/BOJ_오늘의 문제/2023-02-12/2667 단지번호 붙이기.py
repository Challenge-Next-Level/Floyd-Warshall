from collections import deque

N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []


def count(x, y):
    cnt = 1
    visited[y][x] = True
    dq = deque(list([[x, y]]))

    while dq:
        now_x, now_y = dq.popleft()

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < N) or not (0 <= new_y < N):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == 1:
                cnt += 1
                visited[new_y][new_x] = True
                dq.append([new_x, new_y])

    answer.append(cnt)


for _y in range(N):
    for _x in range(N):
        if visited[_y][_x]:
            continue
        if board[_y][_x] == 1:
            count(_x, _y)

answer.sort()
print(len(answer))
for a in answer:
    print(a)