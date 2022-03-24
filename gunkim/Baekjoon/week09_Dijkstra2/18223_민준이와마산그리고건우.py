# 민준이가 목적지 까지 가는 길에 건우의 위치를 지나는지 '체크'해야 한다는 강박관념에 잡혀 중간에 실패가 나왔다
# 단순하게 최소거리의 합을 통해 비교를 하면 됐었다
import sys
import heapq

V, E, P = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph[a].append([b, cost])
    graph[b].append([a, cost])

heap = []
MJ = [float('inf')] * (V + 1) # 민준이가 목적지 까지 가는 최소거리
GW = [float('inf')] * (V + 1) # 건우가 목적지 까지 가는 최소거리


def dijkstra(start_node, dp):
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


dijkstra(1, MJ)
dijkstra(P, GW)
if MJ[P] + GW[-1] == MJ[-1]:
    print("SAVE HIM")
else:
    print("GOOD BYE")