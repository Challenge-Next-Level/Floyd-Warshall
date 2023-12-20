from collections import defaultdict
import heapq

N, M, A, B, C = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dijkstra(k):  # 지나갈 수 있는 최대 수치심
    distance = [1e9 for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    distance[A] = 0
    visited[A] = True

    pq = list()
    heapq.heappush(pq, [distance[A], A])

    while pq:
        now_distance, now_node = heapq.heappop(pq)

        visited[now_node] = True

        if now_node == B:
            return distance[B] <= C

        for next_node, next_cost in graph[now_node]:
            if visited[next_node]:
                continue

            if next_cost > k:
                continue

            if distance[next_node] > now_distance + next_cost:
                distance[next_node] = now_distance + next_cost
                heapq.heappush(pq, [distance[next_node], next_node])
    return False


# 한 골목을 지나갈 때, 최대 수치심
start, end = -1, 21
while start + 1 < end:
    mid = (start + end) // 2

    if dijkstra(mid):
        end = mid
    else:
        start = mid

if end == 21:
    print(-1)
else:
    print(end)
