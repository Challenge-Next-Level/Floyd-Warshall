import sys

input = sys.stdin.readline

from itertools import combinations

N, M = map(int, input().split())

# x, y 좌표
house_list = []
chicken_list = []

for _y in range(N):
    x_board = list(map(int, input().split()))
    for _x in range(N):
        if x_board[_x] == 1:
            house_list.append([_x, _y])
        elif x_board[_x] == 2:
            chicken_list.append([_x, _y])

answer = 1e9


# 도시의 치킨 거리 확인
def check_distance():
    global answer
    temp_answer = 0
    for h in house_list:
        temp_chicken_distance = 1e9

        for c in chicken_list:
            chicken_distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
            temp_chicken_distance = min(temp_chicken_distance, chicken_distance)
        temp_answer += temp_chicken_distance
    answer = min(answer, temp_answer)


chicken_combinations = list(combinations(chicken_list, M))
for combination in chicken_combinations:
    chicken_list = combination
    check_distance()

print(answer)
