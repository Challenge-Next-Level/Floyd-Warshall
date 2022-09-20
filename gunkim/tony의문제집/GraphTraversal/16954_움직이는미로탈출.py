# while dq 안에 반복문을 하나 더 생성하여 좌표 이동 턴과 벽 이동 턴을 나눠 작성해야 함
# 벽이 아직 남아있다면 visit은 매 턴 마다 계속 초기화 되어야 한다
import sys
from collections import deque

board = []
for _ in range(8):
    l = list(sys.stdin.readline())[:-1]
    board.append(l)

dir = [[0,0], [0,1], [0,-1], [1,0], [-1,0], [-1,-1], [1,1], [-1,1], [1,-1]]


def bfs():
    dq = deque([[7,0]])
    visit = set()
    wall = set()
    for i in range(8):
        for j in range(8):
            if board[i][j] == '#':
                wall.add((i, j))
    while dq: # 말 이동 -> 벽 이동
        # 말의 이동 경우를 한 사이클 돌린다
        for _ in range(len(dq)):
            y, x = dq.popleft()
            if (y, x) in wall: # 이동 후 벽이 해당 좌표로 온 경우
                continue
            if y == 0 and x == 7: # 도착
                return 1
            for dy, dx in dir:
                ny, nx = y + dy, x + dx
                if 0<=ny<8 and 0<=nx<8 and (ny,nx) not in wall and (ny,nx) not in visit:
                    visit.add((ny,nx))
                    dq.append((ny,nx))
        # 벽 이동을 한 사이클 돌린다
        if wall: # 벽이 모두 없어질 때 까지 visit은 계속 초기화 된다
            visit = set()
        wallNext = set()
        for y, x in wall:
            if y < 7:
                wallNext.add((y+1,x))
        wall = wallNext
    return 0


print(bfs())