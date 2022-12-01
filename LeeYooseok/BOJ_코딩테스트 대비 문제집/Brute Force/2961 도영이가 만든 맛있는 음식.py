from itertools import combinations
import sys

N = int(input())

ingredient_list = [list(map(int, input().split())) for _ in range(N)]

answer = sys.maxsize

for n in range(1, N + 1):
    food_list = combinations(ingredient_list, n)

    for food in food_list:
        a = 1
        b = 0
        for _a, _b in food:
            a *= _a
            b += _b
        food_taste = abs(a - b)
        answer = min(answer, food_taste)

print(answer)