n = int(input())

loc_list = list()
x_max, y_max = 0, 0
for _ in range(n):
    x, y = map(int, input().split())

    x_max = max(x_max, x + 10)
    y_max = max(y_max, y + 10)

    loc_list.append([x, y])

board = [[0 for _ in range(x_max)] for _ in range(y_max)]

for x, y in loc_list:
    for _x in range(x, x + 10):
        for _y in range(y, y + 10):
            board[y_max - _y - 1][_x] = 1

for _x in range(x_max):
    for _y in range(1, y_max):
        if board[_y][_x] == 1:
            board[_y][_x] = board[_y - 1][_x] + 1

answer = 0
for _y in range(y_max):
    for _x in range(x_max):
        h = y_max
        # (_x, _y) 를 기준으로 최소 높이를 구해가며 오른쪽으로 한칸씩 이동한다. (?)
        for k in range(_x, x_max):
            h = min(h, board[_y][k])
            if h == 0:
                break

            answer = max(answer, h * (k - _x + 1))

print(answer)