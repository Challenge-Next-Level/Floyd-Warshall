import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

board = [[1 for _ in range(M + 1)] for _ in range(N + 1)]

for _y in range(1, N + 1):
    for _x in range(1, M + 1):
        if _x == 1 and _y == 1:
            continue

        new_num = max(board[_y - 1][_x], board[_y][_x - 1]) + 1

        if new_num > K:
            print("NO")
            exit()
        board[_y][_x] = new_num

print("YES")
for b in board[1:]:
    print(*b[1:])