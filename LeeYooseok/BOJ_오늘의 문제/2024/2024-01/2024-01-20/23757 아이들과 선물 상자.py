import heapq

N, M = map(int, input().split())

present_list = list(map(int, input().split()))
present_heap = list()
for p in present_list:
    heapq.heappush(present_heap, -1 * p)

child_list = list(map(int, input().split()))

while child_list and present_heap:
    child = -1 * child_list.pop(0)
    present = heapq.heappop(present_heap)

    if child >= present:
        if child != present:
            heapq.heappush(present_heap, present - child)
    else:
        print(0)
        exit()

if child_list:
    print(0)
else:
    print(1)
