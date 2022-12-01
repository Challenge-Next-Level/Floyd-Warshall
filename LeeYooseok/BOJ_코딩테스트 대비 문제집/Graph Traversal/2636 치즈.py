from collections import deque

M, N = map(int, input().split())

board = list()

num_cheese = 0

for _ in range(M):
    y_board = list(map(int, input().split()))
    for x in y_board:
        if x == 1:
            num_cheese += 1
    board.append(y_board)

answer = list()
answer.append(num_cheese)

time = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while num_cheese > 0:
    visited = [[False for _ in range(N)] for _ in range(M)]
    time += 1

    que = deque()
    que.append([0, 0])
    visited[0][0] = True

    while que:
        now_x, now_y = que.popleft()
        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < N) or not (0 <= new_y < M):
                continue

            if visited[new_y][new_x]:
                continue

            visited[new_y][new_x] = True

            # deque에는 0인 공간만 추가한다. 바깥만 훑기 위함.
            if board[new_y][new_x] == 0:
                que.append([new_x, new_y])
            else:
                board[new_y][new_x] = 0
                num_cheese -= 1

    answer.append(num_cheese)

print(time)
print(answer[-2])
