import sys

input = sys.stdin.readline

import bisect

N = int(input())
number_list = [int(input()) for _ in range(N)]

LIS = [number_list[0]]

for i in range(1, N):
    now_number = number_list[i]
    if LIS[-1] < now_number:
        LIS.append(now_number)
    else:
        insert_index = bisect.bisect_left(LIS, now_number)
        LIS[insert_index] = now_number

print(N - len(LIS))