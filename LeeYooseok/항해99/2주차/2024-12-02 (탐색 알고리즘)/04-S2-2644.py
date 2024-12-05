import sys

input = sys.stdin.readline

from collections import defaultdict, deque

N = int(input())

distance_list = [-1 for _ in range(N + 1)]

s, e = map(int, input().split())
distance_list[s] = 0

M = int(input())
graph = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque([[s, 0]])

while queue:
    now_node, now_distance = queue.popleft()
    if now_node == e:
        break

    for next_node in graph[now_node]:
        if distance_list[next_node] != -1:
            continue

        distance_list[next_node] = now_distance + 1
        queue.append([next_node, now_distance + 1])

print(distance_list[e])