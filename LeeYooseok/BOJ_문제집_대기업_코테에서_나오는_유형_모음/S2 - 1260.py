from collections import defaultdict, deque

N, M, V = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    graph[node].sort()

# DFS
visited = [False for _ in range(N + 1)]

visited[V] = True


def dfs(now_node):
    visited[now_node] = True
    print(now_node, end=' ')
    for next_node in graph[now_node]:
        if visited[next_node]:
            continue
        dfs(next_node)

dfs(V)
print()

# BFS
que = deque([V])
visited = [False for _ in range(N + 1)]
visited[V] = True
answer_of_bfs = [V]

while que:
    now_node = que.popleft()

    for next_node in graph[now_node]:
        if visited[next_node]:
            continue

        que.append(next_node)
        visited[next_node] = True
        answer_of_bfs.append(next_node)

print(" ".join(map(str, answer_of_bfs)))
