import sys

input = sys.stdin.readline

from collections import defaultdict

N = int(input())

number_dict = defaultdict(int)

# 평균
number_sum = 0
for _ in range(N):
    number = int(input())
    number_sum += number
    number_dict[number] += 1

average = round(number_sum / N)
print(average)


# 중앙값
number_list = sorted(number_dict.keys())
idx = 0
for number in number_list:
    idx += number_dict[number]

    if idx >= (N // 2) + 1:
        print(number)
        break

# 최빈값
max_count = max(number_dict.values())
max_count_number_list = list()

for key, item in number_dict.items():
    if item == max_count:
        max_count_number_list.append(key)
if len(max_count_number_list) > 1:
    print(sorted(max_count_number_list)[1])
else:
    print(max_count_number_list[0])

# 범위
print(max(number_dict.keys()) - min(number_dict.keys()))