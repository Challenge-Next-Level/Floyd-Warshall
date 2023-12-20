# s -> e 로 가는 최단경로 찾기
import heapq
from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())

    graph[a].append([b, c])
    graph[b].append([a, c])

for n in range(N + 1):
    graph[n].sort()

s, e = map(int, input().split())


def Dijkstra(start, visited):
    distance = [1e9 for _ in range(N + 1)]
    distance[start] = 0

    heap = list()
    heapq.heappush(heap, [0, start])

    while heap:
        now_cost, now_node = heapq.heappop(heap)

        # 현재 노드까지의 거리 < 이전 노드 -> 현재 노드 cost
        if distance[now_node] < now_cost:
            continue

        for next_node, next_cost in graph[now_node]:
            # 이미 방문한 노드는 pass
            if visited[next_node]:
                continue

            if distance[next_node] > now_cost + next_cost:
                distance[next_node] = now_cost + next_cost
                heapq.heappush(heap, [now_cost + next_cost, next_node])

    return distance


e_visited = [False for _ in range(N + 1)]
e_distance = Dijkstra(e, e_visited) # end node 에서 다른 노드까지 가는 최단 경로

now_node = s
s_visited = [False for _ in range(N + 1)]
s_e_cost = 0

while now_node != e:
    for next_node, next_cost in graph[now_node]:
        # 최단 거리에 속한 노드라면,(s->now_node + now_node -> next_node + next_node -> e_node == s -> e_node)
        if s_e_cost + next_cost + e_distance[next_node] == e_distance[s]:
            s_e_cost += next_cost
            s_visited[next_node] = True
            now_node = next_node
            break

s_visited[e] = False # 다시 e 까지 방문해야하기 때문에 visited 변경
s_distance = Dijkstra(e, s_visited) # end node 에서 다른 노드까지 가는 최단 경로

print(s_e_cost + s_distance[s])
