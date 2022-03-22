"""
안풀린다...시간초과
graph x, y 위치 신경 써야함
"""

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

M, N = map(int, input().split())

heap = []

graph = list()

for _ in range(N):
    graph.append(list(input().split()[-1])) # 엔터 입력 방지


dp = [[INF] * M for _ in range(N)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def Dijkstra():
    dp[0][0] = 0
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        w, now_x, now_y = heapq.heappop(heap)

        if dp[now_y][now_x] < w:
            continue

        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            # 벽 확인
            if 0 <= new_x < M and 0 <= new_y < N:

                t_w = w

                # 이동할 수 없다면
                if graph[new_y][new_x] == '1':
                    t_w += 1

                # 어쨌든 이동
                if dp[new_y][new_x] > t_w:
                    dp[new_y][new_x] = t_w
                    heapq.heappush(heap, (t_w, new_x, new_y))



Dijkstra()
print(dp[-1][-1])