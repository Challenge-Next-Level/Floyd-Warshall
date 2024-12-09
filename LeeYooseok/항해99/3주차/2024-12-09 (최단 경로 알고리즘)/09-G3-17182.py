import sys

input = sys.stdin.readline

N, K = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def solve(idx, count, cost):
    global answer

    if count == N:
        answer = min(answer, cost)
        return

    for next_idx in range(N):
        if not visited[next_idx]:
            visited[next_idx] = True
            solve(next_idx, count + 1, cost + graph[idx][next_idx])
            visited[next_idx] = False


# 노드를 백트래킹으로 탐색하여 모든 노드를 방문하여 최소 시간 구하기
visited = [False for _ in range(N)]
answer = 1e9
visited[K] = True
solve(K, 1, 0)
print(answer)
