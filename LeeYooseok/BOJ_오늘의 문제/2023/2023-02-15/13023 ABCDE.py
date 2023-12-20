N, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N


def dfs(start, depth):
    if depth >= 5:
        print(1)
        exit()

    for child in graph[start]:
        if not visited[child]:
            visited[child] = True
            dfs(child, depth + 1)
            visited[child] = False


for idx in range(N):
    visited[idx] = True
    dfs(idx, 1)
    visited[idx] = False

print(0)