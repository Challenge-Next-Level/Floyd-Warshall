# 구역을 5개의 선거구로 나누어야 한다.
# 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다.
import sys

input = sys.stdin.readline

N = int(input())
A_board = [[0] * (N + 1)]
A_board += [[0] + list(map(int, input().split())) for _ in range(N)]

result = sys.maxsize


def check(x, y, d_1, d_2):
    # x : 행, y : 열
    # 선거구 board
    vote_board = [[0] * (N + 1) for _ in range(N + 1)]
    # 각 선거구 지역
    cnt = [0] * 6

    # 5번 선거구 경계선
    for i in range(d_1 + 1):
        vote_board[x + i][y - i] = 5
        vote_board[x + d_2 + i][y + d_2 - i] = 5
    for i in range(d_2 + 1):
        vote_board[x + i][y + i] = 5
        vote_board[x + d_1 + i][y - d_1 + i] = 5

    # 5번 선거구 내부
    for i in range(x + 1, x + d_1 + d_2):
        is_5 = False
        for j in range(1, N + 1):
            if vote_board[i][j] == 5:
                is_5 = not is_5
            if is_5:
                vote_board[i][j] = 5

    # 선거구에 포함되는 지역
    for _x in range(1, N + 1):
        for _y in range(1, N + 1):
            # 1번 선거구
            if 1 <= _x < x + d_1 and 1 <= _y <= y and vote_board[_x][_y] == 0:
                vote_board[_x][_y] = 1
                cnt[1] += A_board[_x][_y]
            # 2번 선거구
            elif 1 <= _x <= x + d_2 and y < _y <= N and vote_board[_x][_y] == 0:
                vote_board[_x][_y] = 2
                cnt[2] += A_board[_x][_y]
            # 3번 선거구
            elif x + d_1 <= _x <= N and 1 <= _y < y - d_1 + d_2 and vote_board[_x][_y] == 0:
                vote_board[_x][_y] = 3
                cnt[3] += A_board[_x][_y]
            # 4번 선거구
            elif x + d_2 < _x <= N and y - d_1 + d_2 <= _y <= N and vote_board[_x][_y] == 0:
                vote_board[_x][_y] = 4
                cnt[4] += A_board[_x][_y]
            # 5번 선거구
            elif vote_board[_x][_y] == 5:
                cnt[5] += A_board[_x][_y]

    return max(cnt[1:]) - min(cnt[1:])


for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d_1 in range(1, N + 1):
            for d_2 in range(1, N + 1):
                if 1 <= x < x + d_1 + d_2 <= N and 1 <= y - d_1 < y < y + d_2 <= N:
                    result = min(result, check(x, y, d_1, d_2))

print(result)
