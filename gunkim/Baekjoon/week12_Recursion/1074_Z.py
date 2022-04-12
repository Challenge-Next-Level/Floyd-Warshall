import sys

go = [[0, 0], [0, 1], [1, 0], [1, 1]]
count = 0
N, r, c = map(int, sys.stdin.readline().split())


def Z_recursion(size, y, x):
    global count
    if y == r and x == c:
        print(count)
        return
    move = size // 2
    if move <= 0: # n==1일때 이동하는 경우
        count += 1
        return
    if not (y <= r < y + size and x <= c < x + size): # r, c가 예상 범위 안에 없다면 n * n 사이즈 만큼 이동 건너뛰기
        count += size * size
        return
    for g in go:
        ny, nx = y + g[0] * move, x + g[1] * move
        Z_recursion(move, ny, nx)


Z_recursion(2 ** N, 0, 0)