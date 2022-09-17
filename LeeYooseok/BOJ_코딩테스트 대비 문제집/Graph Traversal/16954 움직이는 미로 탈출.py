from collections import deque

# 1초 동안 욱제의 캐릭터가 먼저 이동하고, 그 다음 벽이 이동한다.
# 벽이 캐릭터가 있는 칸으로 이동하면 더 이상 캐릭터는 이동할 수 없다.

# 벽을

board = list()
wall = list()
for y in range(8):
    y_board = list(input())

    for x in range(8):
        if y_board[x] == '#':
            wall.append([x, y])
    board.append(y_board)

visited = [[[] for _ in range(8)] for _ in range(8)]

dx = [0, -1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 0, -1, 1, -1, 1, -1, 1]

que = deque()
que.append([0, 7, 0]) # x, y, t
visited[0][7].append(0)

while que:
    now_x, now_y, now_t = que.popleft()
    if now_x == 7 and now_y == 0:
        print(1)
        exit()

    new_t = now_t + 1

    for i in range(9):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < 8) or not(0 <= new_y < 8):
            continue

        if new_t in visited[new_y][new_x]:
            continue

        if [new_x, new_y - now_t] in wall:
            continue

        if [new_x, new_y - new_t] in wall:
            continue

        visited[new_y][new_x].append(new_t)
        que.append([new_x, new_y, new_t])

print(0)