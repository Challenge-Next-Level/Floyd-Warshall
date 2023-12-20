import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())

board = list()
trash_list = list()
for _y in range(N):
    y_board = list(input())
    for _x in range(M):
        if y_board[_x] == 'g':
            trash_list.append([_x, _y])
        elif y_board[_x] == 'S':
            s_x, s_y = _x, _y
    board.append(y_board)

for x, y in trash_list:
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if not(0 <= tx < M) or not(0 <= ty < N):
            continue

        if board[ty][tx] == '.':
            board[ty][tx] = '#'
que = []
heapq.heappush(que, [0, 0, s_x, s_y])
visited = [[False] * M for _ in range(N)]
visited[s_y][s_x] = True

while que:
    num_trash, num_trash_side, now_x, now_y = heapq.heappop(que)

    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < M) or not(0 <= new_y < N):
            continue

        if visited[new_y][new_x]:
            continue

        visited[new_y][new_x] = True
        if board[new_y][new_x] == '.':
            heapq.heappush(que, [num_trash, num_trash_side, new_x, new_y])
        elif board[new_y][new_x] == '#':
            heapq.heappush(que, [num_trash, num_trash_side + 1, new_x, new_y])
        elif board[new_y][new_x] == 'g':
            heapq.heappush(que, [num_trash + 1, num_trash_side, new_x, new_y])
        else:
            print(num_trash, num_trash_side)
            exit()
