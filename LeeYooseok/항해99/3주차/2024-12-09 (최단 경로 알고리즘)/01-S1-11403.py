import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][k] == 1 and board[k][j] == 1:
                board[i][j] = 1

for b in board:
    print(*b)