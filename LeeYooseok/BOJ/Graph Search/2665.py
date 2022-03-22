"""
이동할 수 있는 공간일 때 appendleft를 해야하는 이유 : 이동할 수 있는 공간이라면, 벽을 뚫지 않고도 이동할 수 있으므로 해당 공간의 우선순위를 높게 해주기 위해서, 큐의 헤드 부분에 넣어준다.
"""

from collections import deque

n = int(input())

graph = list()

for _ in range(n):
    graph.append(list(input()))

# 방문 X : -1, 방문 O : 0
visited = [[-1] * n for _ in range(n)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    start_x, start_y = 0, 0
    target_x, target_y = n - 1, n - 1

    temp = deque()
    # 현재 위치, 부신 벽의 개수
    temp.append([start_x, start_y, 0])

    while temp:
        x, y, curr = temp.popleft()
        visited[x][y] = 0

        if x == target_x and y == target_y:
            return curr

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            # 벽 벗어남
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue

            # 방문하지 않았다면
            if visited[new_x][new_y] == -1:
                # 이동할 수 있다면
                if graph[new_x][new_y] == '1':
                    temp.appendleft([new_x, new_y, curr]) # 그냥 append 하면 7, appendleft 하면 2

                # 이동할 수 없다면
                if graph[new_x][new_y] == '0':
                    temp.append([new_x, new_y, curr + 1])


print(bfs())
