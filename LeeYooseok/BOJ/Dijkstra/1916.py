import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
dp = [INF] * (N + 1)
heap = []


def Dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, now = heapq.heappop(heap)

        if weight > dp[now]:
            continue

        for next_weight, next_node in graph[now]:

            new_weight = weight + next_weight

            if dp[next_node] > new_weight:
                dp[next_node] = new_weight
                heapq.heappush(heap, (new_weight, next_node))


for _ in range(M):
    s, e, w = map(int, input().split())
    # 가중치, 도착지 입력
    graph[s].append((w, e))

start, end = map(int, input().split())

Dijkstra(start)

print(dp[end])
