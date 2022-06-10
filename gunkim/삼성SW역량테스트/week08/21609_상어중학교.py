import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
dir = [[0,1], [0,-1], [1,0], [-1,0]]


def bfs(y, x, visited):
    num = board[y][x] # 탐색하는 일반 블록의 숫자
    queue = deque([[y, x]])
    rainbow = 0 # 무지개 블록 갯수
    size = 0 # 그룹 블록의 크기
    all_visit = [[0 for _ in range(n)] for _ in range(n)] # 현재 bfs가 0을 방문하는 경우 체크
    while queue:
        sy, sx = queue.popleft()
        if visited[sy][sx] == 1 or all_visit[sy][sx] == 1 or not(board[sy][sx] == 0 or board[sy][sx] == num):
            continue
        if board[sy][sx] == 0:
            all_visit[sy][sx] = 1
            rainbow += 1
        elif board[sy][sx] == num:
            visited[sy][sx] = 1
        size += 1
        for dy, dx in dir:
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < n and 0 <= nx < n:
                queue.append([ny, nx])
    return [size, rainbow]


def bfs_remove(y, x):
    queue = deque([[y, x]])
    num = board[y][x]
    while queue:
        sy, sx = queue.popleft()
        if not(board[sy][sx] == 0 or board[sy][sx] == num):
            continue
        board[sy][sx] = -2
        for dy, dx in dir:
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < n and 0 <= nx < n:
                queue.append([ny, nx])
    return


def gravity():
    for j in range(n):
        for i in range(n - 1, 0, -1):
            if board[i][j] == -2:
                for k in range(i - 1, -1, -1):
                    if board[k][j] == -1:
                        break
                    if board[k][j] >= 0:
                        board[i][j] = board[k][j]
                        board[k][j] = -2
                        break


# 블록 그룹: 일반 블록(1~m) 하나 이상 및 같은 색상, 검은(-1) 블록 x, 무지개 블록(0) 상관 x
answer = 0
while True:
    max_block = [0, -1, -1, -1] # 그룹 블록 크기, y, x좌표, 무지개 블록 수
    # 1. 가장 큰 블록 찾기
    visit = [[0 for _ in range(n)] for _ in range(n)] # 일반 블록에 대한 방문만 체크, 0은 체크하지 않음
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1 or board[i][j] == 0 or board[i][j] == -2 or visit[i][j] == 1:
                continue
            group_size = bfs(i, j, visit)
            if group_size[0] > max_block[0]: # 그룹 블록 사이즈가 크다면 갱신
                max_block = [group_size[0], i, j, group_size[1]]
            elif group_size[0] == max_block[0]:
                if group_size[1] > max_block[-1]: # 무지개 블록수가 많다면 갱신
                    max_block = [group_size[0], i, j, group_size[1]]
                elif group_size[1] == max_block[-1]:
                    if i > max_block[1]: # 행의 크기가 크다면 갱신
                        max_block = [group_size[0], i, j, group_size[1]]
                    elif i == max_block[1]:
                        if j > max_block[2]: # 열의 크기가 크다면 갱신
                            max_block = [group_size[0], i, j, group_size[1]]
    # 탈출 조건(찾은 그룹 블록의 최대 크기가 2보다 작을 때)
    if max_block[0] < 2:
        print(answer)
        break
    # 2. 블록 그룹 제거, 점수 획득
    answer += max_block[0] * max_block[0]
    bfs_remove(max_block[1], max_block[2])
    # 3. 중력 작용
    gravity()
    # 4. 반시계 방향 회전
    new_board = list(zip(*board))
    new_board.reverse()
    for i in range(n): # zip을 사용하면 리스트가 튜플로 저장되어 다시 리스트로 전환해준다.
        board[i] = list(new_board[i])
    # 5. 중력 작용2
    gravity()