n = int(input())

board = [["*"] * n for _ in range(n)]

# 1, 2, 3, 4, 5, 6, 7
three_pow = [3, 9, 27, 81, 243, 729, 2187]
t = three_pow.index(n) + 1


def solution(start, end, t):
    global board
    # 3 * 3 이면 가운데 비우고 리턴
    if t == 1:
        board[start[0]+1][start[1]+1] = " "
        return
    else:
        for i in range(3):
            for j in range(3):
                # 가운데 비워줌
                if i == 1 and j == 1:
                    for k in range(3**(t-1)):
                        board[start[0] + 3**(t-1) + k] = board[start[0] + 3**(t-1) + k][:start[1] + 3**(t-1)] + [" "]*(3**(t-1)) + board[start[0] + 3**(t-1) + k][start[1] + 2*(3**(t-1)):]
                else:
                    solution([start[0] + i*(3**(t-1)), start[1] + j*(3**(t-1))],[start[0] + 3**(t-1) + i*(3**(t-1)) - 1, start[1] + 3**(t-1) + j*(3**(t-1)) - 1],t-1)


solution([0,0],[n-1,n-1],t)

for c in range(n):
    print("".join(board[c]))