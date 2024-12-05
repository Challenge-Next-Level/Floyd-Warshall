import sys

input = sys.stdin.readline

from collections import defaultdict

T = int(input())
for _ in range(T):
    n = int(input())
    cloth_dict = defaultdict(list)
    for _ in range(n):
        cloth_name, cloth_type = input().split()
        cloth_dict[cloth_type].append(cloth_name)

    for key in cloth_dict.keys():
        cloth_dict[key].append("-1")

    answer = 1
    for cloth_name_list in cloth_dict.values():
        answer *= len(cloth_name_list)

    print(answer - 1)

