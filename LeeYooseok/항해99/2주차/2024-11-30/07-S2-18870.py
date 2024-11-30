import sys

input = sys.stdin.readline

N = int(input())
number_list = list(map(int, input().split()))

sorted_number_list = list()

for i in range(N):
    sorted_number_list.append([number_list[i], i, 0])

sorted_number_list.sort()

for i in range(1, N):
    now_number = sorted_number_list[i][0]
    prior_number = sorted_number_list[i - 1][0]

    if now_number > prior_number:
        sorted_number_list[i][2] = sorted_number_list[i - 1][2] + 1
    elif now_number == prior_number:
        sorted_number_list[i][2] = sorted_number_list[i - 1][2]

sorted_number_list.sort(key = lambda x : x[1])

for i in range(N):
    print(sorted_number_list[i][2], end = " ")