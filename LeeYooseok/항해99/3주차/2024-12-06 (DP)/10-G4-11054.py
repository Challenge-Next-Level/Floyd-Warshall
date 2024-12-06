import sys

input = sys.stdin.readline

import bisect

N = int(input())
number_list = list(map(int, input().split()))


LIS = [number_list[0]]
LIS_length = [1 for _ in range(N)]

LDS = [number_list[-1]]
LDS_length = [1 for _ in range(N)]

for i in range(1, N):
    now_number_for_LIS = number_list[i]
    if LIS[-1] < now_number_for_LIS:
        LIS.append(now_number_for_LIS)
    else:
        insert_index = bisect.bisect_left(LIS, now_number_for_LIS)
        LIS[insert_index] = now_number_for_LIS
    LIS_length[i] = len(LIS)

    now_number_for_LDS = number_list[N - i - 1]
    if LDS[-1] < now_number_for_LDS:
        LDS.append(now_number_for_LDS)
    else:
        insert_index = bisect.bisect_left(LDS, now_number_for_LDS)
        LDS[insert_index] = now_number_for_LDS
    LDS_length[N - i - 1] = len(LDS)

answer = 0
for i in range(N):
    answer = max(answer, LIS_length[i] + LDS_length[i] - 1)
print(answer)
