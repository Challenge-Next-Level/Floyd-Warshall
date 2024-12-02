import sys

input = sys.stdin.readline

sys.setrecursionlimit(10 ** 9)

from collections import defaultdict

N, M, R = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# 인접 정점은 오름차순으로 방문한다.
for node in graph:
    graph[node].sort()

visited = [False for _ in range(N + 1)]

order = 0
answer = [0 for _ in range(N + 1)]


def DFS(now_node):
    global order
    order += 1
    answer[now_node] = order

    for next_node in graph[now_node]:
        if visited[next_node]:
            continue

        visited[next_node] = True
        DFS(next_node)


visited[R] = True
DFS(R)

print("\n".join(list(map(str, answer[1:]))))
