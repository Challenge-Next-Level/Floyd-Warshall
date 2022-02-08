import sys

N, M = map(int, sys.stdin.readline().split())
virus = [[] for _ in range(N)]
for i in range(N): # 바이러스 분포 맵
    virus[i] = list(map(int, sys.stdin.readline().split()))
go = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동,서,남,북 이동
safe = 0 # 안전구역 수 계산
for i in range(N):
    for j in range(M):
        if virus[i][j] == 0:
            safe += 1


def dfs(b, a, visit):
    if visit[b][a] == 1 or virus[b][a] != 2: # 바이러스가 있는 곳에서 탐색을 해야한다
        return 0
    route = [[b, a]]
    count = 0
    while route:
        y, x = route.pop()
        if visit[y][x] == 1:
            continue
        visit[y][x] = 1
        if virus[y][x] == 0: # 전이된 곳을 카운트 +1
            count += 1
        for s in range(4):
            ny, nx = y + go[s][0], x + go[s][1]
            if 0 <= nx < M and 0 <= ny < N and virus[ny][nx] == 0:
                route.append([ny, nx])
    return count


answer = float('inf')
size = N * M
for i in range(1, size - 1): # 3개의 울타리를 놓는 모든 경우를 탐색
    for j in range(i + 1, size):
        for k in range(j + 1, size + 1):
            a1, a2 = (i - 1) // M, (i - 1) % M
            b1, b2 = (j - 1) // M, (j - 1) % M
            c1, c2 = (k - 1) // M, (k - 1) % M
            if virus[a1][a2] == 0 and virus[b1][b2] == 0 and virus[c1][c2] == 0: # 빈 공간에만 울타리를 놓는다
                virus[a1][a2], virus[b1][b2], virus[c1][c2] = 1, 1, 1 # 울타리 설치
                visit = [[0] * M for _ in range(N)] # 방문 배열을 탐색때 마다 새롭게 초기화
                changed = 0
                for p in range(N):
                    for q in range(M):
                        changed += dfs(p, q, visit) # dfs로 전이되는 바이러스 수 계산
                answer = min(answer, changed)
                virus[a1][a2], virus[b1][b2], virus[c1][c2] = 0, 0, 0 # 울타리 철수

print(safe - answer - 3) # 안전 구역 - 최소로 전이된 바이러스 수 - 울타리수