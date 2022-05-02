import sys
from collections import deque

n = int(sys.stdin.readline())
board = [[0] * n for _ in range(n)] # 보드 생성
k = int(sys.stdin.readline())
for _ in range(k): # 사과 위치 저장
    y, x = map(int, sys.stdin.readline().split())
    board[y - 1][x - 1] = 2

l = int(sys.stdin.readline())
time = []
for _ in range(l): # 방향 정보 저장
    time.append(sys.stdin.readline().split())
time.reverse()

# 방향 정보. d는 index 개념이다
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d = 0

cur_time = 0 # 현재 시간
snake = deque() # 뱀이 지나간 위치를 덱으로 기록
snake.append([0, 0])
board[0][0] = 1 # 뱀이 있는 곳은 1로 표시
while True:
    cur_time += 1
    if time and int(time[-1][0]) == cur_time - 1:
        moved_time = time.pop()
        if moved_time[1] == 'D':
            d = (d + 1) % 4
        else:
            d = (d + 4 - 1) % 4
    # 진행 방향 dir[d]
    ny, nx = snake[-1][0] + dir[d][0], snake[-1][1] + dir[d][1]
    if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1:
        if board[ny][nx] != 2:
            my, mx = snake.popleft()
            board[my][mx] = 0
        snake.append([ny, nx])
        board[ny][nx] = 1
    else:
        break
print(cur_time)