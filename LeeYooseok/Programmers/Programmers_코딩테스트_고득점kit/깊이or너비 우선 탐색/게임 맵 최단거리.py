from collections import deque

def solution(maps):
    n, m = len(maps[0]), len(maps)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    visited = [[-1 for _ in range(n)] for _ in range(m)]

    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1

    while queue:
        now_x, now_y = queue.popleft()
        now_moving_cnt = visited[now_y][now_x]

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < n) or not (0 <= new_y < m):
                continue

            if maps[new_y][new_x] != 1:
                continue

            if visited[new_y][new_x] == -1:
                visited[new_y][new_x] = now_moving_cnt + 1
                queue.append([new_x, new_y])
            elif visited[new_y][new_x] > (now_moving_cnt + 1):
                visited[new_y][new_x] = now_moving_cnt + 1
                queue.append([new_x, new_y])

    return visited[-1][-1]