import heapq

N = int(input())

left_heap = [] # 최대 힙
right_heap = [] # 최소 힙

for i in range(N):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -1 * num) # heapq 의 기본값은 최소 힙 이다.
    else:
        heapq.heappush(right_heap, num)

    if right_heap and -1 * left_heap[0] > right_heap[0]:
        left_num = heapq.heappop(left_heap)
        right_num = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -1 * right_num)
        heapq.heappush(right_heap, left_num)

    print(-1 * left_heap[0])