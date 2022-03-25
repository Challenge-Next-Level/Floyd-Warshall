# 다익스트라로 풀이 시도를 했는데 70%로 에서 막힌다. 이유를 모르겠다.
# 임의로 bfs 풀이를 보고 풀었다.
from collections import deque
import sys


W, H = map(int, sys.stdin.readline().split())
board, location = [], []
for i in range(H):
    board.append(list(sys.stdin.readline())[:-1])
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            location.append([i, j])

visited = [[float("inf")] * W for _ in range(H)]
go = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동서남북


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 0
    while queue:
        cur_y, cur_x = queue.popleft()
        for go_y, go_x in go: # 동서남북 이동
            ny, nx = cur_y + go_y, cur_x + go_x
            while True: # 한 방향으로 쭉 탐색해본다
                # 1. 범위가 벗어날 때
                # 2. 벽을 만날 때
                # 3. 방문을 이미 한곳인데 더 적은 거울을 이미 사용할 수 있는 곳이라면
                # 바로 break 하고 다른 방향 탐색을 진행
                if not (0 <= ny < H and 0 <= nx < W):
                    break
                if board[ny][nx] == "*":
                    break
                if visited[ny][nx] < visited[cur_y][cur_x] + 1:
                    break
                queue.append((ny, nx)) # 유효하게 이동한 곳이면 queue에 모두 추가
                visited[ny][nx] = visited[cur_y][cur_x] + 1 # cur_y, cur_x 좌표의 visited 값에서 1을 더하는 것 유의
                # 같은 방향 한 칸 이동 갱신
                ny += go_y
                nx += go_x


bfs(location[0][0], location[0][1])
print(visited[location[1][0]][location[1][1]] - 1) # 첫 출발은 거울 없이 모든 방향 이동 가능하기에 1을 빼도 된다