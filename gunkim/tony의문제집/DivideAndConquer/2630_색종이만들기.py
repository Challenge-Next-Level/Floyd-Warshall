import sys

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
white, blue = 0, 0


def divide(y, x, size):
    start = board[y][x]
    flag = 0
    for i in range(y,y+size): # 할당받은 구역이 같은 색인지 확인
        if flag == 1:
            break
        for j in range(x,x+size):
            if board[i][j] != start:
                flag = 1
                break
    if flag == 0: # 모두 같은 색이라면 white, blue 카운트
        if start == 1:
            global blue
            blue += 1
        else:
            global white
            white += 1
    else: # 하나라도 다른 색이라면 네 구역으로 분할 정복
        length = size//2
        divide(y,x,length)
        divide(y,x+length,length)
        divide(y+length,x,length)
        divide(y+length,x+length,length)
    return


divide(0, 0, n)
print(white)
print(blue)