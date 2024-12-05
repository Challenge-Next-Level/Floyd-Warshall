import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]

dx = {"-": 1, "|": 0}
dy = {"-": 0, "|": 1}


def DFS(x, y, floor_type):
    new_x, new_y = x + dx[floor_type], y + dy[floor_type]

    if not (0 <= new_x < M) or not (0 <= new_y < N):
        return

    if board[new_y][new_x] != floor_type:
        return

    visited[new_y][new_x] = True
    DFS(new_x, new_y, floor_type)


answer = 0

for _y in range(N):
    for _x in range(M):
        if not visited[_y][_x]:
            answer += 1
            visited[_y][_x] = True
            DFS(_x, _y, board[_y][_x])

print(answer)