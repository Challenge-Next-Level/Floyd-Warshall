import sys

input = sys.stdin.readline

from collections import defaultdict
import heapq

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])
    graph[B].append([A, C])

s, e = map(int, input().split())

max_heap = list()
visited = [1000000001 for _ in range(N + 1)]

# 현재 위치의 무게가 더 큰것을 먼저 탐색함
heapq.heappush(max_heap, [-1000000001, s])

while max_heap:
    now_weight, now_node = heapq.heappop(max_heap)

    # 종료 조건
    if now_node == e:
        print(-now_weight)
        break

    for next_node, next_weight in graph[now_node]:
        # 가능한 무게 = min(현재 출발지 무게, 도착지 무게)
        next_weight = max(-next_weight, now_weight)
        # 현재 도착지 무게 > 가능한 무게 -> 탐색할 가치가 없음
        if visited[next_node] <= next_weight:
            continue

        visited[next_node] = next_weight
        heapq.heappush(max_heap, [next_weight, next_node])