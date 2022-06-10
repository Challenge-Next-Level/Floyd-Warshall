N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1, 2, 7, 5, 10
rate = {1: 0.01, 2: 0.02, 5: 0.05, 7: 0.07, 10: 0.1}

step = 0
d = -1
c_x, c_y = N // 2, N // 2

result = 0


def check(a_x, a_y):
    if (0 <= a_x < N) and (0 <= a_y < N):
        return True
    else:
        return False


def move(m_x, m_y, m_d):
    global result
    old_c_x, old_c_y = m_x - dx[m_d], m_y - dy[m_d]
    sand = board[m_y][m_x]
    temp = sand
    board[m_y][m_x] = 0

    # alpha
    x_a, y_a = m_x + dx[m_d], m_y + dy[m_d]

    # 5%
    x_5, y_5 = m_x + 2 * dx[m_d], m_y + 2 * dy[m_d]
    sub_sand = int(sand * rate[5])
    temp -= sub_sand
    if check(x_5, y_5):
        board[y_5][x_5] += sub_sand
    else:
        result += sub_sand

    m_d = (m_d + 1) % 4
    for _ in range(2):
        # 1%
        x_1, y_1 = old_c_x + dx[m_d], old_c_y + dy[m_d]
        sub_sand = int(sand * rate[1])
        temp -= sub_sand
        if check(x_1, y_1):
            board[y_1][x_1] += sub_sand
        else:
            result += sub_sand

        # 7%
        x_7, y_7 = m_x + dx[m_d], m_y + dy[m_d]
        sub_sand = int(sand * rate[7])
        temp -= sub_sand
        if check(x_7, y_7):
            board[y_7][x_7] += sub_sand
        else:
            result += sub_sand

        # 2%
        x_2, y_2 = m_x + 2 * dx[m_d], m_y + 2 * dy[m_d]
        sub_sand = int(sand * rate[2])
        temp -= sub_sand
        if check(x_2, y_2):
            board[y_2][x_2] += sub_sand
        else:
            result += sub_sand

        # 10%
        x_10, y_10 = x_a + dx[m_d], y_a + dy[m_d]
        sub_sand = int(sand * rate[10])
        temp -= sub_sand
        if check(y_10, x_10):
            board[y_10][x_10] += sub_sand
        else:
            result += sub_sand

        m_d = (m_d + 2) % 4

    # alpha
    sub_sand = temp
    if check(x_a, y_a):
        board[y_a][x_a] += sub_sand
    else:
        result += sub_sand


# 토네이도 이동 : 1 ~ N-2 까지 2번씩 방향 바꾸면서 이동, N-1 은 3번 이동
for _ in range(1, N):
    step += 1
    for _ in range(2):
        d = (d + 1) % 4
        for s in range(step):
            c_x, c_y = c_x + dx[d], c_y + dy[d]
            move(c_x, c_y, d)

d = (d + 1) % 4

for s in range(step):
    c_x, c_y = c_x + dx[d], c_y + dy[d]
    move(c_x, c_y, d)

print(result)
