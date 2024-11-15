import heapq

N, K = map(int, input().split())

MAX = 100000
visited = [False for _ in range(MAX + 1)]

min_heap = list()
heapq.heappush(min_heap, [0, N])
visited[N] = True

while min_heap:
    now_time, now_loc = heapq.heappop(min_heap)
    if now_loc == K:
        print(now_time)
        break

    for next_loc, next_time in ([now_loc * 2, now_time], [now_loc + 1, now_time + 1], [now_loc - 1, now_time + 1]):
        if 0 <= next_loc <= MAX and not visited[next_loc]:
            visited[next_loc] = True
            heapq.heappush(min_heap, [next_time, next_loc])