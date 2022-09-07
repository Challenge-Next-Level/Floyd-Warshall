# 실패한 내 시도
# 1. 칼을 먹었을 때 방문하는 리스트(visit)를 따로 만듦
# 2. dq에 좌표 값을 넣을 때 좌표, time, haveKnife 값을 넣어, haveKnife가 True/False 일 때 따로 생각해서 dq에 값을 넣음
# 다른 분의 쉬운 접근 -> 칼을 발견 하면 현재 좌표에서 목표 좌표까지 거리를 바로 계산해서 답을 갱신하다.
import sys
from collections import deque

n, m , t = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

visit = [[False for _ in range(m)] for _ in range(n)]
dir = [[1,0], [-1,0], [0,1], [0,-1]]


def bfs():
    answer = float('inf')
    dq = deque([[0,0,0]])
    visit[0][0] = True
    while dq:
        y, x, time = dq.popleft()
        if y == n-1 and x == m-1:
            answer = min(answer, time)
            continue
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0<=ny<n and 0<=nx<m and visit[ny][nx] is False and board[ny][nx] != 1:
                if board[ny][nx] == 2:
                    answer = min(answer, time + (n-ny-1) + (m-nx-1) + 1)
                else:
                    visit[ny][nx] = True
                    dq.append([ny, nx, time+1])
    return answer


result = bfs()
if result <= t:
    print(result)
else:
    print('Fail')