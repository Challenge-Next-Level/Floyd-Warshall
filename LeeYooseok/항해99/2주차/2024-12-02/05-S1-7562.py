import sys

input = sys.stdin.readline

from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

answer = list()

T = int(input())
for _ in range(T):
    l = int(input())

    visited = [[False for _ in range(l)] for _ in range(l)]

    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())

    queue = deque([[s_x, s_y, 0]])
    visited[s_y][s_x] = True

    while queue:
        now_x, now_y, move_cnt = queue.popleft()

        if now_x == e_x and now_y == e_y:
            answer.append(str(move_cnt))
            break

        for i in range(8):
            next_x, next_y = now_x + dx[i], now_y + dy[i]

            if not(0 <= next_x < l) or not(0 <= next_y < l):
                continue

            if visited[next_y][next_x]:
                continue

            visited[next_y][next_x] = True
            queue.append([next_x, next_y, move_cnt + 1])

print("\n".join(answer))