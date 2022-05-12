n, m = map(int, input().split())

r, c, d = map(int, input().split())

# 북, 동, 남, 서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

board = [list(map(int, input().split())) for _ in range(n)]

# 로봇 청소기가 청소한 칸의 개수
result = 0

def do(x, y, d):
    global result
    # 1. 현재 위치를 청소한다.
    if board[y][x] == 0:
        board[y][x] = 2
        result += 1

    for _ in range(4):
        # 2-a. 이때, 왼쪽은 현재 바라보는 방향을 기준으로 한다.
        # 현재 위치의 바로 왼쪽에
        if d == 0:
            left = 3
        else:
            left = d - 1
        left_x, left_y = x + dx[left], y + dy[left]

        # 아직 청소하지 않은 빈 공간이 존재한다면,
        if board[left_y][left_x] == 0:
            # 왼쪽 방향으로 회전한 다음 한 칸을 전진하고 1번으로 돌아간다.
            do(left_x, left_y, left)
            return
        # 그렇지 않을 경우, 왼쪽 방향으로 회전한다.
        d = left
    back = (d + 2) % 4
    back_x, back_y = x + dx[back], y + dy[back]
    if board[back_y][back_x] == 1:
        return
    do(back_x, back_y, d)

do(c, r, d)

print(result)