import sys

board = [[] for _ in range(5)]
for i in range(5):
    board[i] = list(sys.stdin.readline().split())
go = [[0, 1], [0, -1], [1, 0], [-1, 0]] #동서남북 이동 가능
answer = set([]) # set으로 정답 자료형 생성


def dfs(y, x, word, depth):
    if depth == 6:
        answer.add(word)
        return
    for i in range(4):
        ny, nx = y + go[i][0], x + go[i][1]
        if 0 <= ny < 5 and 0 <= nx < 5:
            dfs(ny, nx, word + board[ny][nx], depth + 1) # 재귀로 dfs 탐색
    return


for i in range(5): # 모든 지점에서 경우 탐색
    for j in range(5):
        dfs(i, j, board[i][j], 1)

print(len(answer))