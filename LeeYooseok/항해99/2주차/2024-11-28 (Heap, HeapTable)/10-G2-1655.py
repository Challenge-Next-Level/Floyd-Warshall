import sys

input = sys.stdin.readline

import heapq

N = int(input())

# 중간값 보다 작은 값거나 같은 값들은 leftHeap(최대힙) 에 넣어준다.
left_heap = list()
# 중간값 보다 큰 값들은 rightHeap(최소힙) 에 넣어준다.
right_heap = list()

for _ in range(N):
    x = int(input())

    # left_heap 에 먼저 넣어준다.
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -1 * x)
    else:
        heapq.heappush(right_heap, x)

    if right_heap and right_heap[0] < -1 * left_heap[0]:
        left_value = -1 * heapq.heappop(left_heap)
        right_value = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -1 * right_value)
        heapq.heappush(right_heap, left_value)

    # 중간값 출력
    print(-1 * left_heap[0])