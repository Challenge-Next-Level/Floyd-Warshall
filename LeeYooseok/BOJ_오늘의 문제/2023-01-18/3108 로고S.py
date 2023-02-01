# BFS 풀이
# 예제 입력처럼 접점이 없는 사격형이 있지만 좌표상으로는 한 칸차이라서 bfs로 이동가능한 케이스가 존재한다
# 따라서 사각형의 모든 길이를 2배하면 간단하게 해결할 수 있다
from collections import deque

N = int(input())

board = [[0 for _ in range(2001)] for _ in range(2001)]
start_list = list()
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = 2 * (x1 + 500), 2 * (y1 + 500), 2 * (x2 + 500), 2 * (y2 + 500)
    start_list.append([x1, y1])

    for x in range(x1, x2 + 1):
        board[y1][x] = 1
        board[y2][x] = 1

    for y in range(y1, y2 + 1):
        board[y][x1] = 1
        board[y][x2] = 1
visited = [[0 for _ in range(2001)] for _ in range(2001)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    visited[y][x] = 1
    que = deque()
    que.append([x, y])

    while que:
        now_x, now_y = que.popleft()
        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x <= 2000) or not (0 <= new_y <= 2000):
                continue

            if board[new_y][new_x] == 0:
                continue

            if visited[new_y][new_x] == 1:
                continue

            visited[new_y][new_x] = 1
            que.append([new_x, new_y])


answer = 0
for s_x, s_y in start_list:
    if visited[s_y][s_x] == 0:
        bfs(s_x, s_y)
        answer += 1

if board[1000][1000] == 1:
    answer -= 1

print(answer)
