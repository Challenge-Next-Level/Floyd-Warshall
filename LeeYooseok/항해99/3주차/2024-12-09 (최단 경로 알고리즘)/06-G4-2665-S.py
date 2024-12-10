import sys
import heapq

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(_distance):
    min_heap = list()
    # 비용, 행, 열
    heapq.heappush(min_heap, [0, 0, 0])
    _distance[0][0] = 0

    while min_heap:
        now_distance, now_x, now_y = heapq.heappop(min_heap)

        if _distance[now_y][now_x] < now_distance:
            continue

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < n) or not (0 <= new_y < n):
                continue

            if board[new_y][new_x] == "0":
                temp_var = now_distance + 1

                if _distance[new_y][new_x] > temp_var:
                    _distance[new_y][new_x] = temp_var
                    heapq.heappush(min_heap, [temp_var, new_x, new_y])
            else:
                if _distance[new_y][new_x] > now_distance:
                    _distance[new_y][new_x] = now_distance
                    heapq.heappush(min_heap, [now_distance, new_x, new_y])


n = int(input())

board = [list(input()) for _ in range(n)]

distance = [[sys.maxsize for _ in range(n)] for _ in range(n)]

dijkstra(distance)

print(distance[n - 1][n - 1])
