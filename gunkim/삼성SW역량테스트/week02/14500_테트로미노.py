import sys

n, m = map(int, sys.stdin.readline().split())
board = []
max_val = 0
for idx in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    max_val = max(max_val, max(board[idx]))

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
answer = 0
visit = [[0] * m for _ in range(n)]


def dfs(y, x, depth, total):
    global answer
    if depth == 4:
        answer = max(answer, total)
        return
    if total < answer - max_val * (4 - depth): # 백트래킹으로 시간을 줄여주는 것도 핵심
        return
    for d in dir:
        ny, nx = y + d[0], x + d[1]
        if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0:
            if depth == 2: # 'ㅗ' 모양의 테트로미노를 만들기 위함
                visit[ny][nx] = 1
                dfs(y, x, depth + 1, total + board[ny][nx]) # (y, x)좌표에서 다시 한 번 더 탐색
                visit[ny][nx] = 0
            visit[ny][nx] = 1
            dfs(ny, nx, depth + 1, total + board[ny][nx])
            visit[ny][nx] = 0


for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visit[i][j] = 0
print(answer)
