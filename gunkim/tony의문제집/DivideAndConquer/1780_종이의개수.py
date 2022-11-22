import sys

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
minusOne, zero, plusOne = 0, 0, 0


def divideAndConquer(y,x,size):
    global minusOne,zero,plusOne
    # 같은 종이로 되어있는지 확인
    start, flag = board[y][x], 0
    for i in range(size):
        if flag == 1:
            break
        for j in range(size):
            if board[y+i][x+j] != start:
                flag = 1
                break
    # 같은 종이라면
    if flag == 0:
        if start == -1:
            minusOne += 1
        elif start == 0:
            zero += 1
        else:
            plusOne += 1
    else: # 다른 종이라면
        divide = size//3
        divideAndConquer(y,x,divide)
        divideAndConquer(y,x+divide*1,divide)
        divideAndConquer(y,x+divide*2,divide)
        divideAndConquer(y+divide*1, x, divide)
        divideAndConquer(y+divide*1, x + divide * 1, divide)
        divideAndConquer(y+divide*1, x + divide * 2, divide)
        divideAndConquer(y + divide * 2, x, divide)
        divideAndConquer(y + divide * 2, x + divide * 1, divide)
        divideAndConquer(y + divide * 2, x + divide * 2, divide)
    return


divideAndConquer(0,0,n)
print(minusOne)
print(zero)
print(plusOne)