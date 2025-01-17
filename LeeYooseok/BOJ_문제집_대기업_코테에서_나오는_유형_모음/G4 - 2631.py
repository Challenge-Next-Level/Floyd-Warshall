import sys

input = sys.stdin.readline

import bisect

N = int(input())
child_list = [int(input()) for _ in range(N)]

answer = [child_list[0]]

for i in range(N):
    if child_list[i] > answer[-1]:
        answer.append(child_list[i])
    else:
        idx = bisect.bisect_left(answer, child_list[i])

        answer[idx] = child_list[i]

print(N - len(answer))