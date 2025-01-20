from collections import deque

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque(list())
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

queue.append([1, 0, 0, 0])
visited[0][0][0] = True

while queue:
    now_count, hit_count, now_x, now_y = queue.popleft()

    if now_x == M - 1 and now_y == N - 1:
        print(now_count)
        exit()

    for i in range(4):
        new_x = now_x + dx[i]
        new_y = now_y + dy[i]

        if not(0 <= new_x < M) or not(0 <= new_y < N):
            continue

        if visited[new_y][new_x][hit_count]:
            continue

        if board[new_y][new_x] == '0':
            visited[new_y][new_x][hit_count] = True
            queue.append([now_count + 1, hit_count, new_x, new_y])
        else:
            if hit_count == 1:
                continue

            visited[new_y][new_x][hit_count + 1] = True
            queue.append([now_count + 1, hit_count + 1, new_x, new_y])

print(-1)

