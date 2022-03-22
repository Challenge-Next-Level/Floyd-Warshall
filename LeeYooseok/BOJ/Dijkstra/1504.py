"""
1) start -> v1 -> v2 -> end
2) start -> v2 -> v1 -> end
"""

import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]


def Dijkstra(start):
    dp = [INF] * (N + 1)
    heap = []

    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, now = heapq.heappop(heap)

        if dp[now] < weight:
            continue

        for next_weight, next_node in graph[now]:
            new_weight = weight + next_weight
            if dp[next_node] > new_weight:
                dp[next_node] = new_weight
                heapq.heappush(heap, (new_weight, next_node))

    return dp


for _ in range(E):
    a, b, c = map(int, input().split())

    graph[a].append((c, b))
    graph[b].append((c, a))

v1, v2 = map(int, input().split())

dp_v0 = Dijkstra(1)
dp_v1 = Dijkstra(v1)
dp_v2 = Dijkstra(v2)

result = min((dp_v0[v1] + dp_v1[v2] + dp_v2[N]), (dp_v0[v2] + dp_v2[v1] + dp_v1[N]))

if result < INF:
    print(result)
else:
    print(-1)
