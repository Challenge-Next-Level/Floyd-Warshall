from collections import deque

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]

v_total_cnt, k_total_cnt = 0, 0


def BFS(x, y):
    global v_cnt, k_cnt
    deq = deque(list())
    deq.append([x, y])
    visited[y][x] = True

    while deq:
        now_x, now_y = deq.popleft()

        if board[now_y][now_x] == "v":
            v_cnt += 1
        elif board[now_y][now_x] == "k":
            k_cnt += 1

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_x, new_y = now_x + dx, now_y + dy

            if (0 <= new_x < C) and (0 <= new_y < R) and not visited[new_y][new_x]:
                if not board[new_y][new_x] == "#":
                    deq.append((new_x, new_y))
                    visited[new_y][new_x] = True


for _y in range(R):
    for _x in range(C):
        if board[_y][_x] != "#" and not visited[_y][_x]:
            v_cnt, k_cnt = 0, 0
            BFS(_x, _y)

            if v_cnt < k_cnt:
                k_total_cnt += k_cnt
            else:
                v_total_cnt += v_cnt

print(k_total_cnt, v_total_cnt)
