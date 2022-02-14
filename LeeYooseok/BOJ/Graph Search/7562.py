"""

"""
from collections import deque

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

n = int(input())


def bfs(x, y):
    temp = deque()
    temp.append([x, y, 0])
    visited = [[0]*l for _ in range(l)]

    while temp:
        x, y, curr = temp.popleft()

        # 방문 확인
        if visited[x][y] == 1:
            continue
        visited[x][y] = 1

        # 도착 확인
        if x == target_x and y == target_y:
            return curr

        for i in range(8):
            new_x = x + dx[i]
            new_y = y + dy[i]

            # 벽 벗어나는지 확인
            if new_x < 0 or new_x >= l or new_y < 0 or new_y >= l:
                continue

            # 이동 가능
            temp.append([new_x, new_y, curr + 1])


for _ in range(n):
    l = int(input())
    now_x, now_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    print(bfs(now_x, now_y))
