N, B = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


# 행렬 곱셈 함수
def mul(U, V):
    size = len(U)
    Z = [[0 for _ in range(size)] for _ in range(size)]

    for _y in range(size):
        for _x in range(size):
            value = 0
            for i in range(size):
                value += U[_y][i] * V[i][_x]
            Z[_y][_x] = value % 1000

    return Z


def square(board, B):
    size = len(board)
    if B == 1:
        for _y in range(size):
            for _x in range(size):
                board[_y][_x] %= 1000
        return board

    temp_board = square(board, B // 2)
    # B 가 짝수면
    if B % 2 == 0:
        return mul(temp_board, temp_board)
    else:
        return mul(mul(temp_board, temp_board), board)


answer = square(board, B)
for a in answer:
    print(*a)