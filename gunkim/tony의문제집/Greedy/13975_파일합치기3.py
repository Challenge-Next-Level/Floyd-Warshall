import sys
import heapq


t = int(input())
for _ in range(t):
    k = int(sys.stdin.readline())
    novel = list(map(int, sys.stdin.readline().split()))
    heap = []
    for i in range(k):
        heapq.heappush(heap, novel[i])
    answer = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, a+b)
        answer += a + b
    print(answer)