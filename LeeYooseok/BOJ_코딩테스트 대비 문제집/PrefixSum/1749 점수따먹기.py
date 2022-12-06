import sys

N, M = map(int, input().split())
num_board = [list(map(int, input().split())) for _ in range(N)]

prefix_sum_board = [[0 for _ in range(M + 1)] for _ in range(N+1)]

for _y in range(N):
    for _x in range(M):
        prefix_sum_board[_y + 1][_x + 1] = prefix_sum_board[_y][_x + 1] + prefix_sum_board[_y + 1][_x] - prefix_sum_board[_y][_x] + num_board[_y][_x]

answer = -1 * sys.maxsize
# x1, y1, x2, y2 의 부분행렬 합 구하기
for y1 in range(1, N + 1):
    for x1 in range(1, M + 1):
        for y2 in range(y1, N + 1):
            for x2 in range(x1, M + 1):
                total_sum = prefix_sum_board[y2][x2]
                left_sum = prefix_sum_board[y2][x1 - 1]
                upper_sum = prefix_sum_board[y1 - 1][x2]
                part_sum = prefix_sum_board[y1 - 1][x1 - 1]

                prefix_sum = total_sum - (left_sum + upper_sum) + part_sum

                answer = max(answer, prefix_sum)

print(answer)


