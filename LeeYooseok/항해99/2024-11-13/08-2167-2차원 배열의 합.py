import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

prefix_sum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for _y in range(N):
    for _x in range(M):
        prefix_sum[_y + 1][_x + 1] = prefix_sum[_y][_x + 1] + prefix_sum[_y + 1][_x] + board[_y][_x] - prefix_sum[_y][_x]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())

    answer = prefix_sum[x][y] - prefix_sum[i - 1][y] - prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1]
    print(answer)