import sys
import heapq
N = int(sys.stdin.readline().split()[0])
M = int(sys.stdin.readline().split()[0])
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, cost = map(int, sys.stdin.readline().split())
    graph[A].append([B, cost])
start, end = map(int, sys.stdin.readline().split())

heap = []
INF = float('inf')
dp = [INF for _ in range(N + 1)]


def dijkstra(start_node): # 기본적인 다익스트라 문제. 이 기본 틀을 외워야 할 것 같다.
    dp[start_node] = 0
    heapq.heappush(heap, (0, start_node))
    while heap:
        cur_weight, cur_node = heapq.heappop(heap)
        if dp[cur_node] < cur_weight:
            continue
        for moved_node, weight in graph[cur_node]:
            total_weight = cur_weight + weight
            if dp[moved_node] > total_weight:
                dp[moved_node] = total_weight
                heapq.heappush(heap, [total_weight, moved_node])
    return


dijkstra(start)
print(dp[end])