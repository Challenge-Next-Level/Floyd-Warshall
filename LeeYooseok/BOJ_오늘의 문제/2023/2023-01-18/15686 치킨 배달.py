import sys
from itertools import combinations

n, m = map(int, input().split())

board = []

result = sys.maxsize

# x, y 좌표
houses = []
chicken = []

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 1:
            houses.append([j, i])
        elif temp[j] == 2:
            chicken.append([j, i])


# 도시의 치킨 거리 확인
def check_distance():
    global result
    temp_result = 0
    for h in houses:
        temp_d_chicken = sys.maxsize
        for c in chicken:
            d_chicken = abs(h[0] - c[0]) + abs(h[1] - c[1])
            temp_d_chicken = min(temp_d_chicken, d_chicken)
        temp_result += temp_d_chicken

    result = min(result, temp_result)


pick_chickens = list(combinations(chicken, m))
for p in pick_chickens:
    chicken = p
    check_distance()

print(result)
