# 상하 반전
T = int(input())

board = []
for _ in range(T):
    H, W = map(int, input().split())
    for _ in range(H):
        board.append(input())

    for h in range(H - 1, -1, -1):
        print(board[h])
