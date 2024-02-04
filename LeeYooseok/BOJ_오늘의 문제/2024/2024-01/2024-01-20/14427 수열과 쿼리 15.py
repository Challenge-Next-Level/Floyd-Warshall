import heapq
import sys

N = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
num_list = list()
for idx in range(N):
    num_list.append([input_list[idx], idx])

num_heap = num_list[:]
heapq.heapify(num_heap)

M = int(sys.stdin.readline())
for _ in range(M):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        num_list[query[1] - 1][0] = query[2]
        num_heap = num_list[:]
        heapq.heapify(num_heap)
    else:
        print(heapq.heappop(num_heap)[1] + 1)
