"""
1 -> 건우 -> 도착 VS 1 -> 도착 비교
양방향 그래프이다.
"""

import sys, heapq

INF = sys.maxsize
input = sys.stdin.readline

V, E, P = map(int, input().split())

graph = [[] for _ in range(V + 1)]

heap = []


def Dijkstra(start):
    dp = [INF] * (V + 1)
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        now_weight, now_node = heapq.heappop(heap)

        if dp[now_node] > now_weight:
            continue

        for w, next_node in graph[now_node]:
            next_weight = now_weight + w

            if dp[next_node] > next_weight:
                dp[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))

    return dp



for _ in range(E):
    a, b, c = map(int, input().split())

    graph[a].append([c, b])
    graph[b].append([c, a])

dp_start = Dijkstra(1)
dp_p = Dijkstra(P)

if dp_start[V] >= dp_start[P] + dp_p[V]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
