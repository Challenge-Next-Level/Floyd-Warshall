from collections import deque

N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

dir = {'U': [0, -1], 'R': [1, 0], 'D': [0, 1], 'L': [-1, 0]}

visited = [[-1] * M for _ in range(N)]

answer = 0


def escapable(x, y):
    global path

    que = deque()
    que.append([x, y])
    visited[y][x] = 2

    while que:
        now_x, now_y = que.pop()
        now_dir = dir[board[now_y][now_x]]
        new_x, new_y = now_x + now_dir[0], now_y + now_dir[1]

        # 탈출 확인
        if not (0 <= new_x < M) or not (0 <= new_y < N):
            return True

        if visited[new_y][new_x] == 1:  # 이미 탈출 가능한 곳
            return True
        elif visited[new_y][new_x] == 0:  # 이미 탈출 불가능한 곳
            return False
        elif visited[new_y][new_x] == 2:  # 이번 방문때 또 방문하면 -> 탈출 불가능
            return False
        else:
            visited[new_y][new_x] = 2
            path.append([new_x, new_y])
            que.append([new_x, new_y])


for _x in range(M):
    for _y in range(N):
        if visited[_y][_x] == -1:
            path = [[_x, _y]]
            if escapable(_x, _y):
                for able_x, able_y in path:
                    visited[able_y][able_x] = 1
            else:
                for disable_x, disable_y in path:
                    visited[disable_y][disable_x] = 0

answer = 0
for v in visited:
    answer += sum(v)
print(answer)
