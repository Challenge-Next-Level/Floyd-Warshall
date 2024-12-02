import sys

input = sys.stdin.readline

from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def bfs(start, end):
    visited = [False for _ in range(N + 1)]

    stack = deque([[start, 0]])
    visited[start] = True

    while stack:
        now_node, now_cost = stack.popleft()

        if now_node == end:
            return now_cost

        for next_node, cost in graph[now_node]:
            if visited[next_node]:
                continue

            visited[next_node] = True
            stack.append([next_node, now_cost + cost])


for _ in range(M):
    u, v = map(int, input().split())

    print(bfs(u, v))
