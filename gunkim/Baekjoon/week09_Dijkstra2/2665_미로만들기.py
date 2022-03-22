# 처음엔 뭐지? 했는데 아이디어가 떠올라 한 번에 패스했다. 리얼 기적...
import sys
import heapq

n = int(sys.stdin.readline().split()[0])
board = [[] for _ in range(n)]
for i in range(n):
    board[i] = list(sys.stdin.readline()[:-1])

dp = [[float('inf')] * n for _ in range(n)]
go = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 동서남북 이동
heap = []


def dijkstra(y, x): # 다익스트라 기본 틀이다.
    dp[y][x] = 0
    heapq.heappush(heap, [0, y, x])
    while heap:
        cur_weight, cur_y, cur_x = heapq.heappop(heap)
        if dp[cur_y][cur_x] < cur_weight:
            continue
        for go_y, go_x in go:
            ny = cur_y + go_y
            nx = cur_x + go_x
            if 0 <= ny < n and 0 <= nx < n: # 좌표의 범위가 유효한지 확인
                total_weight = cur_weight
                if board[ny][nx] == '0': # 검은 블록을 지나게 되면 weight 증가
                    total_weight += 1
                if dp[ny][nx] > total_weight: # 최소 weight가 되도록 갱신한다
                    dp[ny][nx] = total_weight
                    heapq.heappush(heap, [total_weight, ny, nx])


dijkstra(0, 0)
print(dp[-1][-1])