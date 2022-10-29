import sys

r,c = map(int, sys.stdin.readline().split())
board = []
for _ in range(r):
    board.append(list(sys.stdin.readline()[:-1]))
dir = [[1,0], [-1,0], [0,1], [0,-1]]
answer = [['.' for _ in range(c)] for _ in range(r)]
minR, minC, maxR, maxC = float('inf'), float('inf'), 0, 0

# 모든 땅에 대해 잠기는 지 체크
for y in range(r):
    for x in range(c):
        if board[y][x] == 'X':
            check = 0
            for dy, dx in dir:
                ny, nx = y+dy, x+dx
                if not 0<=ny<r or not 0<=nx<c or board[ny][nx] == '.':
                    check += 1
            if check < 3:
                answer[y][x] = 'X'
# 최소 크기의 지도를 출력하기 위한 좌표 찾기
for i in range(r):
    for j in range(c):
        if answer[i][j] == 'X':
            if minR > i:
                minR = i
            if maxR < i:
                maxR = i
            if minC > j:
                minC = j
            if maxC < j:
                maxC = j
# 지도 출력
for i in range(minR, maxR+1):
    print(''.join(answer[i][minC:maxC+1]))
