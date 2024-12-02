import sys

input = sys.stdin.readline

import bisect

N, M = map(int, input().split())

point_list = list(map(int, input().split()))
point_list.sort()
answer = list()
for _ in range(M):
    s, e = map(int, input().split())

    left_point = bisect.bisect_left(point_list, s)
    right_point = bisect.bisect_right(point_list, e)

    answer.append(str(right_point - left_point))

print("\n".join(answer))