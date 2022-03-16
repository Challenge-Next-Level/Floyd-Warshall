import sys
import heapq

n, m = map(int, sys.stdin.readline().split()) # 정점, 간선 수
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
s, t = map(int, sys.stdin.readline().split())

dp = [float('inf') for _ in range(n + 1)]
heap = []


def dijsktra(start):
    dp[start] = 0
    heapq.heappush(heap, (start, 0))
    while heap:
        cur_node, cur_weight = heapq.heappop(heap)
        if cur_weight > dp[cur_node]:
            continue
        for node, weight in graph[cur_node]:
            total_weight = cur_weight + weight
            if dp[node] > total_weight:
                dp[node] = total_weight
                heapq.heappush(heap, (node, total_weight))


dijsktra(s) # 시작 지점 s를 넣어 다익스트라 탐색
print(dp[t]) # 종료 지점 t의 최적 간선 값 출력
