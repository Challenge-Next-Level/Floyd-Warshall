"""
2665와 비슷한 유형이었다.
이동 방법 설정하고, 기본 Dijkstra 알고리즘 작성 후, 버튼 누르는 기능만 구현해주면 됨
근데 시간초과 - Dijkstra 로 해결 시, 시간초과가 뜬다는 블로그 찾음 이유는 고민해봐야함
- DP로 해결하면 안뜬다 함
"""

import sys, heapq

INF = sys.maxsize
input = sys.stdin.readline

n = int(input())

heap = []

dp = [[INF] * n for _ in range(n)]

maze = [list(map(int, input().split())) for _ in range(n)]

# 하, 우
dx = [0, 1]
dy = [1, 0]


def Dijkstra(x, y):
    dp[y][x] = 0
    heapq.heappush(heap, (0, x, y))

    while heap:
        w, now_x, now_y = heapq.heappop(heap)

        if dp[now_y][now_x] < w:
            continue

        for i in range(2):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]

            # 벽 안에 있다면
            if 0 <= new_x < n and 0 <= new_y < n:
                total_w = w

                # 버튼 누르는 거
                if maze[new_y][new_x] >= maze[now_y][now_x]:
                    total_w += maze[new_y][new_x] - maze[now_y][now_x] + 1

                # 어쨌든 이동
                if dp[new_y][new_x] > total_w:
                    dp[new_y][new_x] = total_w
                    heapq.heappush(heap, (total_w, new_x, new_y))


Dijkstra(0, 0)

print(dp[-1][-1])
