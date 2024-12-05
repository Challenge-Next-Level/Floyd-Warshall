import sys

input = sys.stdin.readline

import heapq

N = int(input())

min_heap = list()

for _ in range(N):
    x = int(input())
    heapq.heappush(min_heap, x)

answer = 0
while len(min_heap) > 1:
    y = heapq.heappop(min_heap)
    z = heapq.heappop(min_heap)

    answer += (y + z)

    heapq.heappush(min_heap, (y + z))

print(answer)