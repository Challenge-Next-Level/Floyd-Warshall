import sys

input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split())

visited = [False for _ in range(1000000)]
queue = deque(list())

queue.append([N, 0])
visited[N] = True

while queue:
    now_x, now_time = queue.popleft()

    if now_x == K:
        print(now_time)
        break

    for next_x in (now_x + 1, now_x - 1, now_x * 2):
        if not (0 <= next_x < 1000000):
            continue

        if visited[next_x]:
            continue

        visited[next_x] = True
        queue.append([next_x, now_time + 1])