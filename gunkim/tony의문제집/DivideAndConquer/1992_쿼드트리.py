# 2630(색종이 만들기)랑 완전 똑같은 문제. 그런데 문제 설명이 불친절하여 처음에 뭔말이지? 했던 문제.
import sys

n = int(input())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline())[:-1])


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

    if flag == 0: # 모두 같은 색이라면
        print(start, end='')
    else: # 하나라도 다른 색이라면 네 구역으로 분할 정복
        length = size//2
        print('(', end='')
        divide(y,x,length)
        divide(y,x+length,length)
        divide(y+length,x,length)
        divide(y+length,x+length,length)
        print(')', end='')
    return


divide(0, 0, n)