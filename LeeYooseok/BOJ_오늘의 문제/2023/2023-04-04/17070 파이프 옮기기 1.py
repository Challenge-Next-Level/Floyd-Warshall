N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 가로, 세로, 대각선
able_dir = [[0, 2], [1, 2], [0, 1, 2]]
dir = [[1, 0], [0, 1], [1, 1]]

# 긁으면 안되는 곳
disturb_dir = [[[1, 0]], [[0, 1]], [[1, 0], [1, 1], [0, 1]]]

answer = 0


def dfs(now_x, now_y, now_dir):
    global answer
    if now_x == N - 1 and now_y == N - 1:
        answer += 1
        return

    for next_dir in able_dir[now_dir]:
        new_x, new_y = now_x + dir[next_dir][0], now_y + dir[next_dir][1]

        if not (0 <= new_x < N) or not (0 <= new_y < N):
            continue

        flag = False
        for disturb in disturb_dir[next_dir]:
            disturb_x, disturb_y = now_x + disturb[0], now_y + disturb[1]

            if not (0 <= disturb_x < N) or not (0 <= disturb_y < N):
                continue

            if board[disturb_y][disturb_x] == 1:
                flag = True
                break

        if flag:
            continue

        dfs(new_x, new_y, next_dir)


dfs(1, 0, 0)
print(answer)