"""
- 현재 집을 특정 색으로 칠하는 최소 전체 비용 -> 이전 집을 특정 색을 제외한 색들로 칠할 수 있는 최소 비용 + 현재 집을 특정 색으로 칠하는 비용
"""
import sys

n = int(input())

# [[R,G,B], ...]
houses = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, len(houses)):
    houses[i][0] = min(houses[i-1][1], houses[i-1][2]) + houses[i][0]
    houses[i][1] = min(houses[i-1][0], houses[i-1][2]) + houses[i][1]
    houses[i][2] = min(houses[i-1][0], houses[i-1][1]) + houses[i][2]

print(min(houses[n-1]))

