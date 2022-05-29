# A_board = 미세먼지의 양
import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())

A_board = list()

machine = list()

for j in range(R):
    temp = list(map(int, input().split()))
    if temp[0] == -1:
        machine.append(j)
    A_board.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    new_A_board = [item[:] for item in A_board]

    # 1) 미세먼지 확산
    for _j in range(R):
        for _i in range(C):
            if A_board[_j][_i] > 0:

                spread_dust = int(A_board[_j][_i] / 5)

                # 확산된 방향 확인
                for i in range(4):
                    new_i, new_j = _i + dx[i], _j + dy[i]

                    # 해당 방향으로 확산
                    if 0 <= new_i < C and 0 <= new_j < R:
                        if A_board[new_j][new_i] == -1:
                            continue
                        new_A_board[new_j][new_i] += spread_dust
                        new_A_board[_j][_i] -= spread_dust


    # 2) 공기청정기 작동
    # 공기청정기로 들어간 먼지는 사라짐
    # 윗쪽 공기청정기
    for u in range(machine[0] - 1, 0, -1):
        new_A_board[u][0] = new_A_board[u-1][0]

    new_A_board[0][:C-1] = new_A_board[0][1:]

    for u in range(1, machine[0] + 1):
        new_A_board[u - 1][-1] = new_A_board[u][-1]

    new_A_board[machine[0]][2:] = new_A_board[machine[0]][1:C-1]
    new_A_board[machine[0]][1] = 0

    for d in range(machine[1] + 2, R):
        new_A_board[d - 1][0] = new_A_board[d][0]

    new_A_board[-1][:C-1] = new_A_board[-1][1:]

    for d in range(R - 1, machine[1], -1):
        new_A_board[d][-1] = new_A_board[d - 1][-1]

    new_A_board[machine[1]][2:] = new_A_board[machine[1]][1:C-1]
    new_A_board[machine[1]][1] = 0

    A_board = new_A_board


result = 2

for b in A_board:
    result += sum(b)

print(result)
