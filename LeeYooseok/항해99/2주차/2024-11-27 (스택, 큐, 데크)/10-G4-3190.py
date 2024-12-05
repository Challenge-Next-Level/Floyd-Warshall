N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

L = int(input())
rotation_time = ["" for _ in range(10001)]
for _ in range(L):
    X, C = input().split()
    rotation_time[int(X)] = C

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

snake = [[0, 0]]
now_dir = 2
time = 1

while True:
    # 머리를 다음칸에 위치한다.
    now_head = snake[0]
    new_head_x, new_head_y = now_head[0] + dx[now_dir], now_head[1] + dy[now_dir]

    if not (0 <= new_head_x < N) or not (0 <= new_head_y < N):
        break

    if [new_head_x, new_head_y] in snake:
        break

    snake.insert(0, [new_head_x, new_head_y])
    if board[new_head_y][new_head_x] != 1:
        snake.pop()
    else:
        board[new_head_y][new_head_x] = 0

    if rotation_time[time] == "L":
        now_dir = ((now_dir + 1) % 4)
    elif rotation_time[time] == "D":
        now_dir = ((now_dir - 1) % 4)

    time += 1

print(time)