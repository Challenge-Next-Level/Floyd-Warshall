import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A_board = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B_board = [list(map(int, input().split())) for _ in range(M)]

answer = [[0 for _ in range(K)] for _ in range(N)]

for _y in range(N):
    for _x in range(K):
        value = 0
        for i in range(M):
            value += (A_board[_y][i] * B_board[i][_x])
        answer[_y][_x] = value

for a in answer:
    print(*a)