import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())

    graph[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue

            if graph[i][k] != 0 and graph[k][j] != 0:
                graph[i][j] = 1

# 자신에게 올 수 있는 노드의 수 : 자신보다 키가 작은 사람의 수
# 자신에서 갈 수 있는 노드의 수 : 자신보다 키가 큰 사람의 수
answer = 0
for i in range(1, N + 1):
    known_node_count = sum(graph[i])
    for j in range(1, N + 1):
        known_node_count += graph[j][i]

    if known_node_count == N - 1:
        answer += 1

print(answer)
