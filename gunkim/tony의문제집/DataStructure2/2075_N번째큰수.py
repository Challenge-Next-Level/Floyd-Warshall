# 처음에 '메모리 초과'가 발생해서 heapq에 모든 값을 넣으면 안되겠다 싶어서
# 크기가 n을 유지하는 heap 자료구조를 유지시켰다.
import sys
import heapq

n = int(input())
heap = []
for _ in range(n):
    for b in list(map(int, sys.stdin.readline().split())):
        heapq.heappush(heap, b)
        if len(heap) > n:
            heapq.heappop(heap)
print(heapq.heappop(heap))