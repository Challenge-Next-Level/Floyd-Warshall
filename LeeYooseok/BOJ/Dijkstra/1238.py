"""
각자 자기의 마을에서 시작 -> X -> 각자 자기의 마을로 도착
"""

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

def Dijkstra(start):
    heap = list()
    dp = [INF] * (N+1)

    dp[start] = 0
    heapq.heappush(heap, [0, start])

    while heap:
        weight, now = heapq.heappop(heap)

        if dp[now] < weight:
            continue

        for w, next_node in graph[now]:
            next_weight = weight + w
            if dp[next_node] > next_weight:
                dp[next_node] = next_weight
                heapq.heappush(heap, [next_weight, next_node])

    return dp

# 초기화
for _ in range(M):
    a, b, t = map(int, input().split())
    # 시간, 도착 지점
    graph[a].append([t, b])

target = Dijkstra(X)
result = [0]

for i in range(1, N+1):
    result.append(Dijkstra(i)[X] + target[i])

print(max(result))
