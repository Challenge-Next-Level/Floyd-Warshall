import sys

N, M = map(int, sys.stdin.readline().split())
ground = [[] for _ in range(N)] # 마당에 정보 입력(울타리, 양, 늑대)
for i in range(N):
    ground[i] = list(sys.stdin.readline()[:-1])

visit = [[0] * M for _ in range(N)] # 마당 방문 여부 체크
go = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동,서,남,북 이동
answer = [0, 0] # 양, 늑대 마리수 (정답)


def dfs(i, j): # 해당 노드를 dfs 탐색
    if visit[i][j] == 1 or ground[i][j] == '#': # 방문 or 울타리 라면 탐색 필요x
        return
    # 초기값 세팅(양, 늑대, 방문하는 노드)
    sheep, wolf = 0, 0
    fence = [[i, j]]
    while fence: # 진짜 dfs 탐색을 하는 곳
        y, x = fence.pop()
        if visit[y][x] == 1:
            continue
        visit[y][x] = 1 # 방문 체크
        if ground[y][x] == 'o': # 늑대, 양 인지 체크
            sheep += 1
        elif ground[y][x] == 'v':
            wolf += 1
        for k in range(4): # 동,서,남,북 이동
            ny, nx = y + go[k][0], x + go[k][1]
            if 0 <= ny < N and 0 <= nx < M and ground[ny][nx] != '#':
                fence.append([ny, nx]) # 이동할 수 있는 곳이면 append
    if sheep > wolf:
        answer[0] += sheep
    else:
        answer[1] += wolf
    return


for a in range(N):
    for b in range(M):
        dfs(a, b)

print(' '.join(map(str, answer)))