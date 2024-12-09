import sys

input = sys.stdin.readline

import heapq

N = int(input())

board = [list(input()) for _ in range(N)]

visited = [[1e9 for _ in range(N)] for _ in range(N)]
min_heap = list()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

heapq.heappush(min_heap, [0, 0, 0])
visited[0][0] = 0

while min_heap:
    now_count, now_x, now_y = heapq.heappop(min_heap)

    if visited[now_y][now_x] < now_count:
        continue

    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < N) or not(0 <= new_y < N):
            continue

        if board[new_y][new_x] != '1':
            new_count = now_count + 1
        else:
            new_count = now_count

        if visited[new_y][new_x] > new_count:
            visited[new_y][new_x] = new_count
            heapq.heappush(min_heap, [new_count, new_x, new_y])

print(visited[-1][-1])
