# 탐색 방향에 대한 고민과 값을 어떻게 바꿔야 하는지가 중요했음.
import sys
from collections import deque

n, m = map(int, input().split())
board = []
count = 0
for _ in range(n):
    b = list(map(int, sys.stdin.readline().split()))
    board.append(b)
    for cheese in b:
        if cheese == 1:
            count += 1
result = [count]
time = 0

dir = [[1,0], [-1,0], [0,1], [0,-1]]


while count > 0: # 치즈를 다 녹일 때 까지
    visit = [[False for _ in range(m)] for _ in range(n)]
    time += 1
    dq = deque([])
    dq.append([0,0])
    visit[0][0] = True
    cnt = 0
    while dq:
        y, x = dq.popleft()
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0<=ny<n and 0<=nx<m and visit[ny][nx] is False:
                visit[ny][nx] = True
                if board[ny][nx] == 0: # deque에는 0인 공간만 추가한다. 바깥만 훑기 위함.
                    dq.append([ny,nx])
                else: # 1인 공간은 0으로 바꿔주기만 한다.
                    board[ny][nx] = 0
                    cnt += 1
    count -= cnt
    result.append(count)

print(time)
print(result[-2])