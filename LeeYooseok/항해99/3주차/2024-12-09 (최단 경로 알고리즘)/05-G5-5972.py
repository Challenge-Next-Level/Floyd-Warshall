import sys

input = sys.stdin.readline

import heapq
from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])
    graph[B].append([A, C])

min_heap = list()
distance_list = [1e9 for _ in range(N + 1)]

start_node = 1
heapq.heappush(min_heap, [0, start_node])
distance_list[start_node] = 0

while min_heap:
    now_cost, now_node = heapq.heappop(min_heap)

    if now_cost > distance_list[now_node]:
        continue

    for next_node, next_cost in graph[now_node]:
        if distance_list[next_node] > distance_list[now_node] + next_cost:
            distance_list[next_node] = distance_list[now_node] + next_cost
            heapq.heappush(min_heap, [distance_list[next_node], next_node])

print(distance_list[N])