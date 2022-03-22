import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

heap = []

graph = list()

for _ in range(n):
    graph.append(list(input().split()[-1])) # 엔터 입력 방지

dp = [[INF] * n for _ in range(n)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def Dijkstra():
    dp[0][0] = 0
    # weight, x, y
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        w, now_x, now_y = heapq.heappop(heap)

        if dp[now_y][now_x] < w:
            continue

        for i in range(4):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            # 벽 확인
            if 0 <= new_x < n and 0 <= new_y < n:
                total_weight = w

                # 이동할 수 없다면
                if graph[new_y][new_x] == "0":
                    total_weight += 1

                # 어쨌든 이동
                if dp[new_y][new_x] > total_weight:
                    dp[new_y][new_x] = total_weight
                    heapq.heappush(heap, (total_weight, new_x, new_y))

Dijkstra()
print(dp[-1][-1])
