import sys

N, M = map(int, sys.stdin.readline().split())
virus = [[] for _ in range(N)]
for i in range(N):
    virus[i] = list(map(int, sys.stdin.readline().split()))
go = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(b, a, visit):
    if visit[b][a] == 1 or virus[b][a] == 1 or virus[b][a] == 0:
        return 0
    route = [[b, a]]
    count = 0
    while route:
        y, x = route.pop()
        if visit[y][x] == 1:
            continue
        visit[y][x] = 1
        if virus[y][x] == 0:
            count += 1
        for s in range(4):
            ny, nx = y + go[s][0], x + go[s][1]
            if 0 <= nx < M and 0 <= ny < N and virus[ny][nx] == 0:
                route.append([ny, nx])
    return count

answer = float('inf')
size = N * M
for i in range(1, size - 1):
    for j in range(i + 1, size):
        for k in range(j + 1, size + 1):
            a1, a2 = (i - 1) // M, (i - 1) % M
            b1, b2 = (j - 1) // M, (j - 1) % M
            c1, c2 = (k - 1) // M, (k - 1) % M
            if virus[a1][a2] == 0 and virus[b1][b2] == 0 and virus[c1][c2] == 0:
                virus[a1][a2], virus[b1][b2], virus[c1][c2] = 1, 1, 1
                visit = [[0] * M for _ in range(N)]
                changed = 0
                for p in range(N):
                    for q in range(M):
                        changed += dfs(p, q, visit)
                answer = min(answer, changed)
                virus[a1][a2], virus[b1][b2], virus[c1][c2] = 0, 0, 0

safe = 0
for i in range(N):
    for j in range(M):
        if virus[i][j] == 0:
            safe += 1
print(safe, answer)