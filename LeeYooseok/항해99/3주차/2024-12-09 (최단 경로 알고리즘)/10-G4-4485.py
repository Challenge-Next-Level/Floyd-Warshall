import sys

input = sys.stdin.readline

import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

idx = 1
while True:
    N = int(input())
    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]

    min_heap = list()
    visited = [[1e9 for _ in range(N)] for _ in range(N)]

    heapq.heappush(min_heap, [board[0][0], 0, 0])
    visited[0][0] = board[0][0]

    answer = 1e9

    while min_heap:
        now_cost, now_x, now_y = heapq.heappop(min_heap)

        if now_x == N - 1 and now_y == N - 1:
            answer = min(answer, now_cost)

        if visited[now_y][now_x] < now_cost:
            continue

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < N) or not (0 <= new_y < N):
                continue

            if visited[new_y][new_x] > now_cost + board[new_y][new_x]:
                visited[new_y][new_x] = now_cost + board[new_y][new_x]
                heapq.heappush(min_heap, [visited[new_y][new_x], new_x, new_y])

    print(f'Problem {idx}: {answer}')
    idx += 1

