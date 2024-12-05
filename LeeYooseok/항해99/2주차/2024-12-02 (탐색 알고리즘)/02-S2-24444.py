import sys

input = sys.stdin.readline

from collections import defaultdict, deque

N, M, R = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for node in graph:
    graph[node].sort()

queue = deque(list())
order = 0
answer = [0 for _ in range(N + 1)]

queue.append(R)

while queue:
    now_node = queue.popleft()
    if answer[now_node] != 0:
        continue
    order += 1
    answer[now_node] = order

    for next_node in graph[now_node]:
        if answer[next_node] != 0:
            continue

        queue.append(next_node)

print("\n".join(list(map(str, answer[1:]))))