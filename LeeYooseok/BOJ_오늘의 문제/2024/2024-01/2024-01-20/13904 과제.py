import heapq

N = int(input())

work_list = list(list(map(int, input().split())) for _ in range(N))
work_list.sort()

do_work = list()
for work in work_list:
    heapq.heappush(do_work, work[1])

    if len(do_work) > work[0]:
        heapq.heappop(do_work)

print(sum(do_work))

