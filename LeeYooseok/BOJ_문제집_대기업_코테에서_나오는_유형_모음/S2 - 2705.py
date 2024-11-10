import sys

input = sys.stdin.readline

import heapq

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

heap = list()
for _x in range(N):
    heapq.heappush(heap, [-1 * board[N - 1][_x], _x, N - 1])

answer = 0
for _ in range(N):
    now_num, now_x, now_y = heapq.heappop(heap)

    answer = -1 * now_num

    if now_y > 0:
        heapq.heappush(heap, [-1 * board[now_y - 1][now_x], now_x, now_y - 1])

print(answer)