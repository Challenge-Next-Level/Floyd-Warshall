# 이분 탐색

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
score_list = [input().split() for _ in range(N)]
score_list.sort(key=lambda x: int(x[1]))

for _ in range(M):
    s = int(input())

    left, right = 0, N
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        if int(score_list[mid][1]) >= s:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(score_list[answer][0])