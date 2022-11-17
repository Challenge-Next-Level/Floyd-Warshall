# python3 는 시간초과, pypy3로 실행
import sys

board = []
zero = []
for i in range(9):
    nums = list(map(int, sys.stdin.readline().split()))
    board.append(nums)
    for j in range(9): # 0인 좌표 모두 저장
        if nums[j] == 0:
            zero.append([i, j])


def check_row(r, num):
    for i in range(9):
        if board[r][i] == num:
            return False
    return True


def check_col(c, num):
    for i in range(9):
        if board[i][c] == num:
            return False
    return True


def check_square(r, c, num):
    ny, nx = r//3*3, c//3*3
    for i in range(3):
        for j in range(3):
            if board[ny+i][nx+j] == num:
                return False
    return True


def dfs(idx): # 0인 좌표들에 대해 dfs로 알맞은 숫자들을 탐색하여 넣어준다.
    if idx >= len(zero): # 모두 채웠을 경우 출력 후 종료(답이 여러개 있을 수 있어서)
        for i in range(9):
            print(' '.join(map(str, board[i])))
        exit(0)
    y, x = zero[idx]
    for number in range(1,10):
        if check_row(y, number) and check_col(x, number) and check_square(y, x, number):
            board[y][x] = number
            dfs(idx+1)
            board[y][x] = 0
    return


dfs(0)



