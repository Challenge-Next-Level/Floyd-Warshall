M, N = map(int, input().split())

board = list()
answer = 0

ikeun_tomato = 0
ikeun_list = set()
for y in range(N):
    x_list = list(map(int, input().split()))
    board.append(x_list)
    for x in range(M):
        if x_list[x] == 1:
            ikeun_list.add((x, y))
        if x_list[x] != 0:
            ikeun_tomato += 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global ikeun_tomato, board, ikeun_list
    new_ikeun_list = set()
    if not ikeun_list:
        print(-1)
        exit()
    for _x, _y in ikeun_list:
        for i in range(4):
            new_x, new_y = _x + dx[i], _y + dy[i]

            if not (0 <= new_x < M) or not (0 <= new_y < N):
                continue

            if board[new_y][new_x] == 0:
                board[new_y][new_x] = 1
                ikeun_tomato += 1
                new_ikeun_list.add((new_x, new_y))

    ikeun_list = new_ikeun_list


while not (ikeun_tomato == M * N):
    answer += 1
    bfs()

print(answer)
