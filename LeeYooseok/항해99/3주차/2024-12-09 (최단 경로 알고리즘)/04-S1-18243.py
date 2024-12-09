import sys

input = sys.stdin.readline

N, K = map(int, input().split())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(K):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

max_distance = 0
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

answer = "Small World!"
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue
        if graph[i][j] == 0 or graph[i][j] > 6:
            answer = "Big World!"
            break
print(answer)