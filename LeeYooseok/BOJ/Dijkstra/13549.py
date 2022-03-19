"""
graph 생성 -> 범위 : 0 ~ 시작 지점 ~ 100,000
걷기 범위 : 0,1 ~ 99,999
순간이동 범우 : 1 ~ 50,000
"""

import sys
import heapq

INF = sys.maxsize

N, K = map(int, input().split())
# N >= K
if N >= K:
    print(N - K)
else:
    graph = [[] for _ in range(100000 + 1)]

    # 걷기 간선 입력 ( ~ 99,999)
    graph[0].append((1, 1))
    for i in range(1, 100000):
        # 가중치, 목적지 노드
        graph[i].append((1, i - 1))
        graph[i].append((1, i + 1))

    # 순간이동 간선 입력
    for j in range(1, 50000 + 1):
        # 가중치, 목적지 노드
        graph[j].append((0, j * 2))

    heap = []
    dp = [INF] * (100000 + 1)


    def Dijkstra(start):
        dp[start] = 0
        heapq.heappush(heap, (0, start))

        while heap:
            weight, now = heapq.heappop(heap)

            if dp[now] < weight:
                continue

            for w, next_node in graph[now]:
                next_weight = weight + w

                if dp[next_node] > next_weight:
                    dp[next_node] = next_weight
                    heapq.heappush(heap, (next_weight, next_node))


    Dijkstra(N)
    print(dp[K])
