import sys

input = sys.stdin.readline

N = int(input())
str_list = list()
for _ in range(N):
    str_list.append(input().strip())


def get_sum(str):
    sum_result = 0
    for s in str:
        if s.isnumeric():
            sum_result += int(s)

    return sum_result


str_list.sort(key=lambda x: (len(x), get_sum(x), x))

for string in str_list:
    print(string)