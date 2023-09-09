import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())

    graph[a].append([b, c * 2])
    graph[b].append([a, c * 2])

def dik_fox():
    dist = [int(1e9) for _ in range(N + 1)]
    dist[1] = 0

    heap = list()
    heapq.heappush(heap, (0, 1)) # cost, node

    while heap:
        now_cost, now_node = heapq.heappop(heap)

        if dist[now_node] < now_cost:
            continue

        for next_node, next_cost in graph[now_node]:
            new_cost = now_cost + next_cost

            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap, [new_cost, next_node])

    return dist

def dik_wolf():
    # dist[i][0] 은 빠르게 도착, dist[i][1] 은 느리게 도착
    dist = [[int(1e9), int(1e9)] for _ in range(N + 1)]
    dist[1][1] = 0 # 출발할때는 빠르게
    heap = list()
    heapq.heappush(heap, (0, 1, False)) # 출발할때는 빠르게

    while heap:
        now_cost, now_node, now_speed = heapq.heappop(heap)

        if now_speed and dist[now_node][0] < now_cost:
            continue
        elif not now_speed and dist[now_node][1] < now_cost:
            continue

        for next_node, next_cost in graph[now_node]:
            if now_speed: # 빠르게 도착했다면, 느리게 출발
                new_cost = now_cost + (next_cost * 2)
                if new_cost < dist[next_node][1]:
                    dist[next_node][1] = new_cost
                heapq.heappush(heap, [new_cost, next_node, False])
            else:
                new_cost = now_cost + (next_cost // 2)
                if new_cost < dist[next_node][0]:
                    dist[next_node][0] = new_cost
                heapq.heappush(heap, [new_cost, next_node, True])

    return dist

fox_dist = dik_fox()
wolf_dist = dik_wolf()

answer = 0
for i in range(1, N + 1):
    if fox_dist[i] < min(wolf_dist[i][0], wolf_dist[i][1]):
        answer += 1

print(answer)

