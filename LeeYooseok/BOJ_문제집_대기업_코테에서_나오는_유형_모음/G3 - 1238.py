import heapq

N, M, X = map(int, input().split())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

to_x_distance = [1e9 for _ in range(N + 1)]

heap = list()
heapq.heappush(heap, (0, X))
to_x_distance[X] = 0

while heap:
    now_cost, now_node = heapq.heappop(heap)

    if to_x_distance[now_node] < now_cost:
        continue

    for next_node in range(1, N + 1):
        if graph[next_node][now_node] != 0:
            next_cost = graph[next_node][now_node]
            next_cost += now_cost

            if next_cost < to_x_distance[next_node]:
                to_x_distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))

from_x_distance = [1e9 for _ in range(N + 1)]

heap = list()
heapq.heappush(heap, (0, X))
from_x_distance[X] = 0

while heap:
    now_cost, now_node = heapq.heappop(heap)

    if from_x_distance[now_node] < now_cost:
        continue

    for next_node in range(1, N + 1):
        if graph[now_node][next_node] != 0:
            next_cost = graph[now_node][next_node]
            next_cost += now_cost

            if next_cost < from_x_distance[next_node]:
                from_x_distance[next_node] = next_cost
                heapq.heappush(heap, (next_cost, next_node))

answer = 0
for i in range(1, N + 1):
    answer = max(answer, to_x_distance[i] + from_x_distance[i])

print(answer)