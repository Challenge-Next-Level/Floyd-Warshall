# 문제 - x, y 입력 반대로
# 첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1)

n, m, y, x, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

cmd = list(map(int, input().split()))

# 2, 4, 1, 3, 5, 6
dice = [0, 0, 0, 0, 0, 0]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for c in cmd:
    new_x = x + dx[c - 1]
    new_y = y + dy[c - 1]

    if not (0 <= new_x < m) or not (0 <= new_y < n):
        continue

    # 동 - 2, 1, 3, 6, 5, 4
    if c == 1:
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    # 서 - 2, 6, 4, 1, 5, 3
    elif c == 2:
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    # 북 - 6, 4, 2, 3, 1, 5
    elif c == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    # 남 - 1, 4, 5, 3, 6, 2
    elif c == 4:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]

    if board[new_y][new_x] == 0:
        board[new_y][new_x] = dice[2]
    else:
        dice[2] = board[new_y][new_x]
        board[new_y][new_x] = 0

    print(dice[5])

    x = new_x
    y = new_y

