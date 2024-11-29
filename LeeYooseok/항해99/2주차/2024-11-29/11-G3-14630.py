import sys

input = sys.stdin.readline

import heapq

N = int(input())

robot_list = [input().rstrip() for _ in range(N)]
robot_len = len(robot_list[0])

distance = [1e9 for _ in range(N)]

s, e = map(int, input().split())

heap = list()
heapq.heappush(heap, (0, s - 1))
distance[s - 1] = 0

while heap:
    now_cost, now_node = heapq.heappop(heap)

    if distance[now_node] < now_cost:
        continue

    for next_node in range(N):
        if now_node == next_node:
            continue

        next_cost = now_cost
        for i in range(robot_len):
            next_cost += (int(robot_list[now_node][i]) - int(robot_list[next_node][i])) ** 2

        if next_cost < distance[next_node]:
            distance[next_node] = next_cost
            heapq.heappush(heap, (next_cost, next_node))

print(distance[e - 1])