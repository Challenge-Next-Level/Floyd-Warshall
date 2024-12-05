import sys

input = sys.stdin.readline

import heapq

N = int(input())

max_heap = list()

for _ in range(N):
    user_input = list(map(int, input().split()))

    a = user_input.pop(0)

    if a == 0:
        if max_heap:
            print(-1 * heapq.heappop(max_heap))
        else:
            print(-1)
    else:
        for value in user_input:
            heapq.heappush(max_heap, -1 * value)
