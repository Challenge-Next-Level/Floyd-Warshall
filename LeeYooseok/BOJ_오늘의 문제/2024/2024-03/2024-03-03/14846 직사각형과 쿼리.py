import sys

input = sys.stdin.readline

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

count_matrix = [[[0 for _ in range(11)] for _ in range(N + 1)] for _ in range(N + 1)]

for _y in range(N):
    for _x in range(N):
        count_matrix[_y + 1][_x + 1][matrix[_y][_x]] = 1
        for num in range(1, 11):
            count_matrix[_y + 1][_x + 1][num] += count_matrix[_y][_x + 1][num]
            count_matrix[_y + 1][_x + 1][num] += count_matrix[_y + 1][_x][num]
            count_matrix[_y + 1][_x + 1][num] -= count_matrix[_y][_x][num]

Q = int(input())
for _ in range(Q):
    x_1, y_1, x_2, y_2 = map(int, input().split())

    answer = 0
    for num in range(1, 11):
        num_cnt = 0
        num_cnt += count_matrix[x_2][y_2][num]
        num_cnt -= count_matrix[x_2][y_1 - 1][num]
        num_cnt -= count_matrix[x_1 - 1][y_2][num]
        num_cnt += count_matrix[x_1 - 1][y_1 - 1][num]
        if num_cnt > 0:
            answer += 1

    print(answer)

