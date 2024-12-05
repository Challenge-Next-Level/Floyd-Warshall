import heapq
import sys

input = sys.stdin.readline

N, H, T = map(int, input().split())
max_heap = list()
for _ in range(N):
    heapq.heappush(max_heap, - 1 * int(input()))

use_count = 0
while use_count < T:
    max_height = -1 * heapq.heappop(max_heap)

    if max_height >= H:
        use_count += 1
        if max_height == 1:
            heapq.heappush(max_heap, -1)
        else:
            heapq.heappush(max_heap, -1 * (max_height // 2))
    else:
        heapq.heappush(max_heap, -1 * max_height)
        break

if -1 * max_heap[0] < H:
    print("YES")
    print(use_count)
else:
    print("NO")
    print(-1 * max_heap[0])