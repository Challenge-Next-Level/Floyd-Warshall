N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]
answer = -1


def find_start():
    for _y in range(N):
        for _x in range(M):
            if not visited[_y][_x]:
                return [_x, _y]
    return False


def get_piece(now_x, now_y, temp, value, axis):
    global answer

    visited[now_y][now_x] = True
    temp = temp + board[now_y][now_x]

    if (axis == 'row' or axis == 'both') and 0 <= now_x + 1 < M and not visited[now_y][now_x + 1]:
        get_piece(now_x + 1, now_y, temp, value, 'row')

    if (axis == 'column' or axis == 'both') and 0 <= now_y + 1 < N and not visited[now_y + 1][now_x]:
        get_piece(now_x, now_y + 1, temp, value, 'column')

    next_start = find_start()

    if next_start:
        next_x, next_y = next_start
        get_piece(next_x, next_y, '', value + int(temp), 'both')
    else:
        answer = max(answer, value + int(temp))

    visited[now_y][now_x] = False


get_piece(0, 0, '', 0, 'both')

print(answer)
