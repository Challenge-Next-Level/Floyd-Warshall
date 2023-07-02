N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

answer = 1e9

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]


def solve(visited, cnt, flower_list):
    global answer
    if cnt == 3:
        fee = 0
        for flower in flower_list:
            for i in range(5):
                fee += board[flower[1] + dy[i]][flower[0] + dx[i]]
        answer = min(fee, answer)
        return

    for _y in range(1, N - 1):
        for _x in range(1, N - 1):
            check = True
            temp_board = [item[:] for item in visited]
            temp_list = flower_list[:]
            temp_list.append([_x, _y])
            for i in range(5):
                if visited[_y + dy[i]][_x + dx[i]] != 0:
                    check = False
                else:
                    temp_board[_y + dy[i]][_x + dx[i]] = 1

            if check:
                solve(temp_board, cnt + 1, temp_list)


solve([[0 for _ in range(N)] for _ in range(N)], 0, [])
print(answer)
