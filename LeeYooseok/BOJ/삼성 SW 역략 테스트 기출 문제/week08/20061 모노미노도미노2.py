import sys
input = sys.stdin.readline

# x는 행, y는 열
score = 0
# 초록색 보드
green_board = [[0] * 4 for _ in range(6)]
# 파랑색 보드
blue_board = [[0] * 4 for _ in range(6)]


# 블럭을 놓는다.
def put_block(t, block, board):
    if t == 1:
        block_x, block_y = block[0][1], block[0][0]
        for j in range(2, 6):
            if board[j][block_x] == 1:
                board[j - 1][block_x] = 1
                break
            else:
                if j == 5:
                    board[j][block_x] = 1
    elif t == 2:
        block_x, block_y = block[0][1], block[0][0]
        for j in range(2, 6):
            if board[j][block_x] == 1 or board[j][block_x + 1] == 1:
                board[j - 1][block_x] = 1
                board[j - 1][block_x + 1] = 1
                break
            else:
                if j == 5:
                    board[j][block_x] = 1
                    board[j][block_x + 1] = 1
    elif t == 3:
        block_x, block_y = block[0][1], block[0][0]
        for j in range(2, 6):
            if board[j][block_x] == 1:
                board[j - 2][block_x] = 1
                board[j - 1][block_x] = 1
                break
            else:
                if j == 5:
                    board[j][block_x] = 1
                    board[j - 1][block_x] = 1
    return board


# 한줄 또는 2줄을 확인하여 지운다.
def get_score(board):
    global score
    for j in range(5, 1, -1):
        if sum(board[j]) == 4:
            if sum(board[j - 1]) == 4:
                score += 2
                return [[0, 0, 0, 0], [0, 0, 0, 0]] + board[:j - 1] + board[j + 1:]
            else:
                score += 1
                return [[0, 0, 0, 0]] + board[:j] + board[j+1:]
    return board

# 연한 부분확인
def white(board):
    if sum(board[1]) > 0:
        if sum(board[0]) > 0:
            return [[0, 0, 0, 0], [0, 0, 0, 0]] + board[:4]
        else:
            return [[0, 0, 0, 0]] + board[:5]
    else:
        return board

N = int(input())
for _ in range(N):
    t, y, x = map(int, input().split())

    block = [[y, x]]
    green_board = put_block(t, block, green_board)

    block = [[3 - x, 3 - y]]
    if t == 2:
        t = 3
        block = [[3 - x - 1, 3 - y]]
    elif t == 3:
        t = 2
        block = [[3 - x, 3 - y - 1]]
    blue_board = put_block(t, block, blue_board)

    green_board = get_score(green_board)
    blue_board = get_score(blue_board)

    green_board = white(green_board)
    blue_board = white(blue_board)


print(score)
num_block = 0
for j in range(2, 6):
    num_block += sum(green_board[j])
    num_block += sum(blue_board[j])
print(num_block)

