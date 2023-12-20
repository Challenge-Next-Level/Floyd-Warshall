N = int(input())

sum_board = [1 for _ in range(10)]

for n in range(1, N):
    for _x in range(1, 10):
        sum_board[_x] += sum_board[_x - 1]

print(sum(sum_board) % 10007)