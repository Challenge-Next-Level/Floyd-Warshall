import sys

input = sys.stdin.readline

from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dx = [1, 0]
dy = [0, 1]

queue = deque([[0, 0]])
visited[0][0] = True

answer = "Hing"

while queue:
    now_x, now_y = queue.popleft()

    if now_x == N - 1 and now_y == N - 1:
        answer = "HaruHaru"
        break

    jump_power = board[now_y][now_x]
    for i in range(2):
        new_x, new_y = now_x + jump_power * dx[i], now_y + jump_power * dy[i]

        if not(0 <= new_x < N) or not(0 <= new_y < N):
            continue

        if visited[new_y][new_x]:
            continue

        visited[new_y][new_x] = True
        queue.append([new_x, new_y])

print(answer)