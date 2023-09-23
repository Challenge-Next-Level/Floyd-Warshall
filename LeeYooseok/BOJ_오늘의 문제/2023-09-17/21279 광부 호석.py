from collections import defaultdict
import heapq
N, C = map(int, input().split())

x_index = defaultdict(list)
for _ in range(N):
    x, y, v = map(int, input().split())
    x_index[x].append([x, y, v])

answer = 0

queue = list()
current_v = 0
for x in sorted(x_index.keys()):
    for _x, _y, _v in x_index[x]:
        current_v += _v
        heapq.heappush(queue, [-1 * _y, _x, _v])

    while queue and len(queue) > C:
        now_y, now_x, now_v = heapq.heappop(queue)
        now_y = -1 * now_y
        prev_top = now_y
        current_v -= now_v

        while queue and (-1 * queue[0][0]) == prev_top:
            next_y, next_x, next_v = heapq.heappop(queue)
            next_y = -1 * next_y
            current_v -= next_v

    answer = max(answer, current_v)

print(answer)