import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            if graph[i][k] != 0 and graph[k][j] != 0:
                if graph[i][j] >= 1:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                else:
                    graph[i][j] = graph[i][k] + graph[k][j]

answer = sum(graph[1])
answer_node = 1
for n in range(2, N + 1):
    if answer > sum(graph[n]):
        answer = sum(graph[n])
        answer_node = n
print(answer_node)