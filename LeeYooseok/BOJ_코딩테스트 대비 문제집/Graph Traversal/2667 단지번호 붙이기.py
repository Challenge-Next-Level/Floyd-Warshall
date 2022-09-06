from collections import deque

N = int(input())

board = [list(map(int, input())) for _ in range(N)]

visited = [list(False for _ in range(N)) for _ in range(N)]

result = 0

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(_y, _x):
    que = deque()
    que.append([_y, _x])
    visited[_y][_x] = True
    cnt = 0

    while que:
        now_y, now_x = que.popleft()
        cnt += 1

        for i in range(4):
            new_y, new_x = now_y + dy[i], now_x + dx[i]

            if 0 <= new_x < N and 0 <= new_y < N:
                if not visited[new_y][new_x] and board[new_y][new_x] == 1:
                    visited[new_y][new_x] = True
                    que.append([new_y, new_x])
    return cnt


result_list = list()
for r in range(N):
    for c in range(N):
        if not visited[r][c] and board[r][c] == 1:
            result_list.append(dfs(r, c))
            result += 1

print(result)
for r in sorted(result_list):
    print(r)
