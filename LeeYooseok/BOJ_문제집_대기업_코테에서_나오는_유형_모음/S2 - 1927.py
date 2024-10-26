import heapq
import sys

input = sys.stdin.readline

N = int(input())

min_heap = list()
for _ in range(N):
    operator = int(input())

    if operator == 0:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, operator)