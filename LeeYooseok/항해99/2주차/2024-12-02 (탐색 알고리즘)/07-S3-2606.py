import sys

input = sys.stdin.readline

from collections import defaultdict

N = int(input())
visited = [0 for _ in range(N + 1)]

M = int(input())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

stack = list()

stack.append(1)

while stack:
    now_node = stack.pop()
    if visited[now_node] == 1:
        continue

    visited[now_node] = 1

    for next_node in graph[now_node]:
        stack.append(next_node)

print(sum(visited) - 1)
