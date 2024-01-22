N, M = map(int, input().split())

board = list()
stack = list()
for _y in range(N):
    x_board = input()
    for _x in range(M):
        if x_board[_x] == 'I':
            stack.append([_x, _y])
    board.append(x_board)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(M)] for _ in range(N)]
visited[stack[0][1]][stack[0][0]] = True

answer = 0
while stack:
    now_x, now_y = stack.pop()

    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < M) or not(0 <= new_y < N):
            continue

        if visited[new_y][new_x]:
            continue

        if board[new_y][new_x] == 'X':
            continue

        if board[new_y][new_x] == 'P':
            answer += 1

        visited[new_y][new_x] = True
        stack.append([new_x, new_y])

if answer == 0:
    print("TT")
else:
    print(answer)
