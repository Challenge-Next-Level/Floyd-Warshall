import sys

input = sys.stdin.readline

N = int(input())

time = [0 for _ in range(N + 1)]

for idx in range(1, N + 1):
    user_input = list(map(int, input().split()))
    require_time = user_input[0]
    M = user_input[1]
    if M >= 1:
        prior_task_list = user_input[2:]
        min_start_time = 0
        for prior_task in prior_task_list:
            min_start_time = max(min_start_time, time[prior_task])
        time[idx] = min_start_time + require_time
    else:
        time[idx] = require_time

print(max(time))

