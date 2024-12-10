import sys

input = sys.stdin.readline

from collections import defaultdict
import heapq

N, M, L = map(int, input().split())
value_list = [0] + list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(L):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dijkstra(start_node):
    global distance_list
    min_heap = list()

    distance_list[start_node] = 0
    heapq.heappush(min_heap, [distance_list[start_node], start_node])

    while min_heap:
        now_distance, now_node = heapq.heappop(min_heap)

        if distance_list[now_node] < now_distance:
            continue

        for next_node, next_distance in graph[now_node]:
            if distance_list[next_node] <= now_distance + next_distance:
                continue
            distance_list[next_node] = now_distance + next_distance
            heapq.heappush(min_heap, [distance_list[next_node], next_node])


answer = 0
for i in range(1, N + 1):
    distance_list = [1e9 for _ in range(N + 1)]
    dijkstra(i)
    now_value = 0
    for j in range(1, N + 1):
        if distance_list[j] <= M:
            now_value += value_list[j]

    answer = max(answer, now_value)
print(answer)
