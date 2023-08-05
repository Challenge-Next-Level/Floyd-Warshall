K = int(input())
x, y = map(int, input().split())

board = [[0 for _ in range(pow(2, K))] for _ in range(pow(2, K))]
board[y-1][x-1] = -1

num = 0

# 해당 부분(x,y ~ x + size, y + size) 에 구멍이 있는지 확인
def check(size, x, y):
    for _x in range(x, x + size):
        for _y in range(y, y + size):
            if board[_x][_y] != 0:
                return False

    return True

def solution(size, x, y):
    global num
    num += 1


    half_size = size // 2
    if check(half_size, x, y): board[x+half_size-1][y+half_size-1] = num
    if check(half_size, x + half_size, y): board[x+half_size][y+half_size-1] = num
    if check(half_size, x, y + half_size): board[x+half_size-1][y+half_size] = num
    if check(half_size, x + half_size, y + half_size): board[x+half_size][y+half_size] = num

    if size == 2: return

    solution(half_size, x, y)
    solution(half_size, x + half_size, y)
    solution(half_size, x, y + half_size)
    solution(half_size, x + half_size, y + half_size)

solution(pow(2, K), 0, 0)

for b in board[::-1]:
    print(*b)
