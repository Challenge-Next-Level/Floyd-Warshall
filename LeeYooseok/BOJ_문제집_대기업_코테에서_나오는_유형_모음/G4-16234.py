from collections import deque

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while True:
    old_board = [item[:] for item in board]

    visited = [[False for _ in range(N)] for _ in range(N)]

    for _y in range(N):
        for _x in range(N):
            if not visited[_y][_x]:
                # 연합 국가 확인
                queue = deque([[_x, _y]])
                visited[_y][_x] = True

                country_list = list()
                total_people = 0

                while queue:
                    now_x, now_y = queue.popleft()

                    country_list.append([now_x, now_y])
                    total_people += board[now_y][now_x]

                    for i in range(4):
                        new_x, new_y = now_x + dx[i], now_y + dy[i]

                        if not (0 <= new_x < N) or not (0 <= new_y < N):
                            continue

                        if visited[new_y][new_x]:
                            continue

                        diff_people = abs(board[now_y][now_x] - board[new_y][new_x])
                        if L <= diff_people <= R:
                            queue.append([new_x, new_y])
                            visited[new_y][new_x] = True

                new_people = total_people // len(country_list)
                for c_x, c_y in country_list:
                    board[c_y][c_x] = new_people
    if board == old_board:
        break
    else:
        answer += 1

print(answer)
