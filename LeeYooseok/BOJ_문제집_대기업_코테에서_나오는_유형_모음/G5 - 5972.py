import heapq
from collections import defaultdict

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])
    graph[e].append([s, c])

distance = [1e9 for _ in range(N + 1)]
heap = list()

start_node = 1
distance[start_node] = 0
heapq.heappush(heap, [0, start_node])

while heap:
    now_distance, now_node = heapq.heappop(heap)

    if distance[now_node] < now_distance:
        continue

    for next_node, cost in graph[now_node]:
        if distance[next_node] <= now_distance + cost:
            continue

        distance[next_node] = now_distance + cost
        heapq.heappush(heap, [distance[next_node], next_node])

print(distance[N])
