import sys

n, m = map(int, sys.stdin.readline().split())
board = []
safe = 0
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    for b in board[i]:
        if b == 0:
            safe += 1
answer = float('inf')
go = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def dfs(y, x, visited):
    stack = [[y, x]]
    cnt = 0
    while stack:
        ny, nx = stack.pop()
        for g in go:
            gy, gx = ny + g[0], nx + g[1]
            if 0 <= gy < n and 0 <= gx < m and board[gy][gx] == 0 and visited[gy][gx] == 0:
                cnt += 1
                visited[gy][gx] = 1
                stack.append([gy, gx])
    return cnt


for i in range(n * m - 2): # 벽 3개를 놓는 경우를 모두 따짐(완전 탐색)
    if board[i // m][i % m] != 0:
        continue
    for j in range(i + 1, n * m - 1):
        if board[j // m][j % m] != 0:
            continue
        for k in range(j + 1, n * m):
            if board[k // m][k % m] != 0:
                continue
            visit = [[0] * m for _ in range(n)] # board는 따로 수정을 하지 않고 싶어 visit에 벽 정보를 담음
            visit[i // m][i % m] = visit[j // m][j % m] = visit[k // m][k % m] = 1
            total = 0
            for idx in range(n * m): # 바이러스가 퍼지는 칸을 카운트
                if board[idx // m][idx % m] == 2:
                    total += dfs(idx // m, idx % m, visit)
            answer = min(answer, total)

print(safe - answer - 3)
