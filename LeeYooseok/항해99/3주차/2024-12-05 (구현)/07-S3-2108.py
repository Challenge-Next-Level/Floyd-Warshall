import sys

input = sys.stdin.readline

from collections import defaultdict

N = int(input())
number_list = [int(input()) for _ in range(N)]
number_list.sort()

answer = list()

# 산술평균, 소수점 이하 첫째 자리에서 반올림한값
answer.append(str(round(sum(number_list) / N)))

# 중앙값, N은 홀수이므로
answer.append(str(number_list[N // 2]))

# 최빈값, 여러 개 있을 때에는 최빈값 중 두번째로 작은값을 출력
count_dict = defaultdict(int)
for number in number_list:
    count_dict[number] += 1

max_count = max(count_dict.values())
max_number = list()
for number in count_dict.keys():
    if count_dict[number] == max_count:
        max_number.append(number)

if len(max_number) > 1:
    answer.append(str(max_number[1]))
else:
    answer.append(str(max_number[0]))

# 범위, N개의 수들 중 최댓값과 최솟값의 차이
answer.append(str(number_list[-1] - number_list[0]))

print("\n".join(answer))
