# 동, 남, 서, 북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

r1, c1, r2, c2 = map(int, input().split())

answer = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
size_of_board = (c2 - c1 + 1) * (r2 - r1 + 1)

x, y = 0, 0
now_value = 1
now_dir = 0

now_count = 0
dir_count = 1

max_value = 0
while size_of_board > 0:
    if c1 <= x <= c2 and r1 <= y <= r2:
        size_of_board -= 1
        answer[y - r1][x - c1] = now_value
        max_value = now_value

    x += dx[now_dir]
    y += dy[now_dir]

    now_value += 1
    now_count += 1

    if now_count == dir_count:
        now_count = 0
        now_dir = (now_dir + 3) % 4
        # 왼쪽으로 턴을 2번 할때마다, 움직이는 수가 한개 씩 증가한다.
        if now_dir == 0 or now_dir == 2:
            dir_count += 1

max_value_size = len(str(max_value - 1))
for _y in range(r2 - r1 + 1):
    for _x in range(c2 - c1 + 1):
        print(str(answer[_y][_x]).rjust(max_value_size), end=" ")
    if _y != (r2 - r1):
        print()
