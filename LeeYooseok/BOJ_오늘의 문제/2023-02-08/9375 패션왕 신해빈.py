import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answer = 1
    N = int(input())
    cloth_dict = defaultdict(int)
    for n in range(N):
        name, type = input().split()
        cloth_dict[type] += 1

    for cloth_cnt in cloth_dict.values():
        answer *= (cloth_cnt + 1)

    print(answer - 1)