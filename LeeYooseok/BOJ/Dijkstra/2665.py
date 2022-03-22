"""
최소 힙을 사용하기 때문에, DFS에서 appendleft와 동일한 방식으로 적용 된다.
- 벽을 덜 부수고 이동 할 수 있는 경우가 먼저 나오기 때문에
"""

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

heap = []

graph = list()

for _ in range(n):
    graph.append(list(input().split()[-1])) # 엔터 입력 방지

# 방문 X : -1, 방문 O : 0
visited = [[-1] * n for _ in range(n)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def Dijkstra():
    # 가중치, 현재 위치
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        w, now_x, now_y = heapq.heappop(heap)
        visited[now_x][now_y] = 0

        if now_x == n - 1 and now_y == n - 1:
            return w

        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            # 벽 벗어남
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue

            # 방문하지 않았다면
            if visited[new_x][new_y] == -1:
                # 이동할 수 있다면
                if graph[new_x][new_y] == '1':
                    heapq.heappush(heap, (w, new_x, new_y))

                # 이동할 수 없다면
                if graph[new_x][new_y] == '0':
                    heapq.heappush(heap, (w + 1, new_x, new_y))


print(Dijkstra())
