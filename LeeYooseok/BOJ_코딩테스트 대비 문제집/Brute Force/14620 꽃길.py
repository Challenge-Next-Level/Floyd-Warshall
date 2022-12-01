import sys

N = int(input())

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def solve(visited, cnt, flower_list):
    global answer, board

    if cnt == 3:
        fee = 0
        for f in flower_list:
            for i in range(5):
                fee += board[f[1] + dy[i]][f[0] + dx[i]]
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


answer = sys.maxsize

board = [list(map(int, input().split())) for _ in range(N)]
solve([[0 for _ in range(N)] for _ in range(N)], 0, [])
print(answer)