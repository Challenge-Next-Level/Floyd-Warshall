import sys

input = sys.stdin.readline

N, M, L = map(int, input().split())
value_list = [0] + list(map(int, input().split()))

graph = [[1e9 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(L):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                graph[i][j] = 0
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0
for i in range(1, N + 1):
    now_value = 0
    for j in range(1, N + 1):
        if graph[i][j] <= M:
            now_value += value_list[j]

    answer = max(answer, now_value)
print(answer)