import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input()) for _ in range(M)]

visited = [[False for _ in range(N)] for _ in range(M)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, team):
    queue = deque([[x, y]])
    power = 0

    while queue:
        now_x, now_y = queue.popleft()
        power += 1

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < N) or not (0 <= new_y < M):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] != team:
                continue

            visited[new_y][new_x] = True
            queue.append([new_x, new_y])

    return power


blue_power = 0
white_power = 0

for _y in range(M):
    for _x in range(N):
        if visited[_y][_x]:
            continue

        now_team = board[_y][_x]
        visited[_y][_x] = True
        now_power = bfs(_x, _y, now_team)

        if now_team == 'W':
            white_power += pow(now_power, 2)
        else:
            blue_power += pow(now_power, 2)

print(white_power, blue_power)
