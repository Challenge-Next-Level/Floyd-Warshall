import heapq

n, m, r = map(int, input().split())
item_list = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for _ in range(r):
    a, b, cost = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append([b, cost])
    graph[b].append([a, cost])


answer = 1

def dijkstra(start_node):
    distance_list[start_node] = 0
    min_que = list()
    heapq.heappush(min_que, [distance_list[start_node], start_node])

    while min_que:
        now_d, now_node = heapq.heappop(min_que)

        if distance_list[now_node] < now_d:
            continue

        for next_node, next_distance in graph[now_node]:
            distance = now_d + next_distance
            if distance < distance_list[next_node]:
                distance_list[next_node] = distance
                heapq.heappush(min_que, [distance, next_node])


for start_node in range(n):
    distance_list = [1e9 for _ in range(n)]
    dijkstra(start_node)

    get_item = 0
    for node in range(n):
        if distance_list[node] <= m:
            get_item += item_list[node]

    answer = max(answer, get_item)

print(answer)
