import sys

input = sys.stdin.readline

N = int(input())

graph = [[1e9 for _ in range(N + 1)] for _ in range(N + 1)]
while True:
    a, b = map(int, input().split())
    if a == - 1 and b == -1:
        break

    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                graph[i][j] = 0
            if graph[i][k] != 1e9 and graph[k][j] != 1e9:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_score = 1e9
answer_list = list()
for idx in range(1, N + 1):
    now_score = max(graph[idx][1:])
    if min_score > now_score:
        min_score = now_score
        answer_list = [idx]
    elif min_score == now_score:
        answer_list.append(idx)

print(min_score, len(answer_list))
print(*answer_list)

