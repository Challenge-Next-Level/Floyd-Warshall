V, E = map(int, input().split())

graph = [[int(1e9) for _ in range(V + 1)] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())

    graph[a][b] = c

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 1e9
for i in range(1, V + 1):
    # 사이클은 결국 출발지와 도착지가 같은 경우이므로 i->i를 확인
    answer = min(answer, graph[i][i])

# 최소값이 없으면 -1, 있으면 최소값을 출력
if answer == 1e9:
    print(-1)
else:
    print(answer)
