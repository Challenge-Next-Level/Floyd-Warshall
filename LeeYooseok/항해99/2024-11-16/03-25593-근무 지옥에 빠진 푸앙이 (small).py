import sys

input = sys.stdin.readline

from collections import defaultdict

N = int(input())

work_hour_list = [4, 6, 4, 10]

worker_dict = defaultdict(int)

for _ in range(N):
    for work_hour_idx in range(4):
        worker_list = input().split()

        for worker in worker_list:
            if worker != "-":
                worker_dict[worker] += work_hour_list[work_hour_idx]

if len(worker_dict) == 0:
    print("Yes")
else:
    max_work_hour = max(worker_dict.values())
    min_work_hour = min(worker_dict.values())

    # 시간 차이가 12시간 이하라면
    if max_work_hour - min_work_hour <= 12:
        print("Yes")
    else:
        print("No")