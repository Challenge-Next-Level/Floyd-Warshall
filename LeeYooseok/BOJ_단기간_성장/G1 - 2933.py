from collections import deque

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

N = int(input())
height_list = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_drop_cluster():
    visited = [[False for _ in range(C)] for _ in range(R)]

    queue = deque()
    for _x in range(C):
        if board[R - 1][_x] == 'x':
            queue.append([_x, R - 1])

    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not(0 <= new_x < C) or not(0 <= new_y < R):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == 'x':
                visited[new_y][new_x] = True
                queue.append([new_x, new_y])

    drop_cluster = list()
    for _y in range(R - 1, -1, -1):
        for _x in range(C):
            if board[_y][_x] == 'x' and not visited[_y][_x]:
                drop_cluster.append([_x, _y])

    return drop_cluster, visited

def change_board(drop_cluster, visited):
    global board

    min_drop_count = 1e9
    for _x, _y in drop_cluster:
        drop_count = 0
        for i in range(_y + 1, R):
            if board[i][_x] == '.':
                drop_count += 1
            if board[i][_x] == 'x' and visited[i][_x]:
                break
        min_drop_count = min(min_drop_count, drop_count)

    for _x, _y in drop_cluster:
        board[_y][_x] = '.'
        board[_y + min_drop_count][_x] = 'x'

for idx in range(N):
    height = R - height_list[idx]

    # 부숴지는 블럭 위치 찾기
    target_loc = [-1, -1]
    # 짝수이면, 왼쪽에서 오른쪽으로
    if idx % 2 == 0:
        for _x in range(C):
            if board[height][_x] == 'x':
                board[height][_x] = '.'
                break
    else:
        for _x in range(C-1, -1, -1):
            if board[height][_x] == 'x':
                board[height][_x] = '.'
                break

    # 떨어지는 클러스터 확인
    drop_cluster, visited = find_drop_cluster()
    if drop_cluster:
        change_board(drop_cluster, visited)

for b in board:
    print("".join(b))