import sys
import heapq

n = int(input())
heap = []
for _ in range(n):
    question = int(sys.stdin.readline().split()[0])
    if question != 0:
        heapq.heappush(heap, -1 * question)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))