import sys

n = int(sys.stdin.readline())
case = []
for _ in range(n):
    case.append(list(map(int, sys.stdin.readline().split())))

blue = [[0 for _ in range(4)] for _ in range(6)] # 행렬 대치를 시킨 상태로 생각할 것이다
green = [[0 for _ in range(4)] for _ in range(6)]
answer = 0


def move(board, blk):
    for i in range(5, -1, -1): # 맨 아래부터 빈 곳을 우선 찾아본다.
        j = blk[0][1]
        flag = 0
        if board[i][j] == 0:
            for k in range(i - 1, -1, -1): # 블럭을 쌓는 것이기 때문에 위에 블럭이 없어야 쌓을 수 있음
                if board[k][j] == 1:
                    flag = 1
            if flag == 1:
                continue
            if len(blk) == 1: # 한 칸짜리 블럭은 여기서 바로 리턴
                board[i][j] = 1
                return
            # 여기서 부터 두 칸짜리 블럭을 고려한다
            ny, nx = blk[1][0] - blk[0][0], blk[1][1] - blk[0][1]
            ry, rx = i + ny, j + nx
            if 0 <= ry < 6 and 0 <= rx < 4 and board[ry][rx] == 0: # 범위 고려 및 빈 곳 찾기
                if abs(nx) == 1: # 가로 블럭에 대해 위에 블럭이 있었는지 나머지 하나에 대해 체크한다
                    for k in range(i - 1, -1, -1):
                        if board[k][rx] == 1:
                            flag = 1
                    if flag == 1:
                        continue
                board[i][j] = 1
                board[ry][rx] = 1
                return


def bingo(board):
    global answer
    for i in range(5, 1, -1):
        if sum(board[i]) == 4:
            if sum(board[i - 1]) == 4:
                answer += 2
                return [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] + board[:i - 1] + board[i + 1:]
            else:
                answer += 1
                return [[0, 0, 0, 0, 0, 0]] + board[:i] + board[i + 1:]
    return board


def over(board):
    if sum(board[1]) > 0:
        if sum(board[0]) > 0:
            return [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] + board[:4]
        else:
            return [[0, 0, 0, 0, 0, 0]] + board[:5]
    return board


for i in range(n):
    t, y, x = case[i]
    block = [] # 블럭 생성
    if t == 1:
        block = [[y,x]]
    elif t == 2:
        block = [[y,x], [y,x+1]]
    elif t == 3:
        block = [[y,x], [y+1,x]]
    # green 이동
    move(green, block)
    # blue 이동
    for i in range(len(block)):
        block[i] = [3 - block[i][1], 3 - block[i][0]]
    move(blue, block)
    # 한 줄이 채워진 곳은 삭제 및 이동
    green = bingo(green)
    blue = bingo(blue)
    # 오버해서 채워진 곳은 이동
    green = over(green)
    blue = over(blue)

print(answer)
total = 0
for i in range(2, 6):
    total += sum(green[i])
    total += sum(blue[i])
print(total)
