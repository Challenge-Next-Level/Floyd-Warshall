import sys
import heapq

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])

heap = []


def dijkstra(start_node, dp): # 기본적인 다익스트라 구현
    dp[start_node] = 0
    heapq.heappush(heap, [0, start_node])
    while heap:
        cur_weight, cur_node = heapq.heappop(heap)
        if dp[cur_node] < cur_weight:
            continue
        for moved_node, weight in graph[cur_node]:
            total_weight = cur_weight + weight
            if dp[moved_node] > total_weight:
                dp[moved_node] = total_weight
                heapq.heappush(heap, [total_weight, moved_node])


go_to = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1): # 각 지점에서의 다익스트라 경로를 찾는다
    dijkstra(i, go_to[i])
answer = [float('inf')] * (n + 1)
for i in range(1, n + 1): # (내 집 -> x로 가는 값) + (x위치 -> 내 집으로 가는 값)
    answer[i] = go_to[i][x] + go_to[x][i]
print(max(answer[1:]))