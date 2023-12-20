from collections import deque

board = [list(input()) for _ in range(12)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = 0


def puyo(y, x):
    global visited, chk
    now_item = board[y][x]
    cnt = 1
    que = deque([[x, y]])
    puyo_loc = list()
    visited[y][x] = True

    while que:
        now_x, now_y = que.popleft()
        puyo_loc.append([now_x, now_y])

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < 6) or not (0 <= new_y < 12):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == now_item:
                visited[new_y][new_x] = True
                cnt += 1
                que.append([new_x, new_y])

    if cnt >= 4:
        chk = True
        for puyo_x, puyo_y in puyo_loc:
            board[puyo_y][puyo_x] = '.'


def gravity():
    que = deque()
    for _x in range(6):
        for _y in range(11, -1, -1):
            if board[_y][_x] != '.':
                que.append(board[_y][_x])
        for _y in range(11, -1, -1):
            if que:
                board[_y][_x] = que.popleft()
            else:
                board[_y][_x] = '.'



while True:
    visited = [[False] * 6 for _ in range(12)]
    chk = False

    for _y in range(12):
        for _x in range(6):
            if board[_y][_x] != '.' and not visited[_y][_x]:
                puyo(_y, _x)

    if not chk:
        print(ans)
        exit()
    else:
        ans += 1
    gravity()
    

