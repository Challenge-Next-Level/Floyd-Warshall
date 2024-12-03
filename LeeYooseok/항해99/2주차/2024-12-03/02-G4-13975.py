import sys

input = sys.stdin.readline

import heapq

T = int(input())
answer_list = list()
for _ in range(T):
    N = int(input())
    number_heap = list(map(int, input().split()))
    heapq.heapify(number_heap)

    answer = 0
    while len(number_heap) >= 2:
        a_book = heapq.heappop(number_heap)
        b_book = heapq.heappop(number_heap)

        next_book = a_book + b_book
        answer += (next_book)
        heapq.heappush(number_heap, next_book)

    answer_list.append(str(answer))

print("\n".join(answer_list))
