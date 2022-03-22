# 앞서 푼 2665_미로만들기 와 완벽히 같은 유형의 문제. 무난하게 풀었다
import sys
import heapq

m, n = map(int, sys.stdin.readline().split()) # 가로, 세로
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(sys.stdin.readline().split()[-1])

dp = [[float('inf')] * m for _ in range(n)]
heap = []
go = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동서남북 이동


def dijkstra(y, x):
    dp[y][x] = 0
    heapq.heappush(heap, [0, y, x])
    while heap:
        cur_weight, cur_y, cur_x = heapq.heappop(heap)
        if dp[cur_y][cur_x] < cur_weight:
            continue
        for go_y, go_x in go:
            ny = cur_y + go_y
            nx = cur_x + go_x
            if 0 <= ny < n and 0 <= nx < m:
                total_weight = cur_weight
                if board[ny][nx] == '1':
                    total_weight += 1
                if dp[ny][nx] > total_weight:
                    dp[ny][nx] = total_weight
                    heapq.heappush(heap, [total_weight, ny, nx])


dijkstra(0, 0)
print(dp[-1][-1])