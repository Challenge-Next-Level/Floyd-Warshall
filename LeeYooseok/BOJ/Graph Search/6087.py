"""
어렵다

"""
import sys
from collections import deque

INF = sys.maxsize

W, H = map(int, input().split())

board = []
points = []

for h in range(H):
    b = input()
    if b.count('C') > 0:
        for i in range(len(b)):
            if b[i] == 'C':
                points.append([i, h])
    board.append(b)

visited = [[INF] * W for _ in range(H)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    start_x, start_y = points[0][0], points[0][1]

    temp = deque()
    # 현재 위치
    temp.append([start_y, start_x])
    visited[start_y][start_x] = 0

    while temp:
        y, x = temp.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            while True: # 한 방향으로만 쭉 탐색

                # 범위가 벗어날 때
                if not (0<= nx <W and 0<= ny <H):
                    break

                # 벽을 만날 때
                if board[ny][nx] == "*":
                    break

                # 방문을 이미 한곳인데 더 적은 거울을 이미 사용할 수 있는 곳이라면
                if visited[ny][nx] < visited[y][x] + 1:
                    break

                # 유효하게 이동한 곳이면 queue에 모두 추가
                temp.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1 # 거울 하나 추가?

                # 같은 방향으로 한칸 더 이동
                ny += dy[i]
                nx += dx[i]

bfs()
print(visited[points[1][1]][points[1][0]] - 1)
