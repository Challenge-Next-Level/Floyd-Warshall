import sys
import heapq

W, H = map(int, sys.stdin.readline().split())
board, location = [], []
for i in range(H):
    board.append(list(sys.stdin.readline())[:-1])
for i in range(H):
    for j in range(W):
        if board[i][j] == 'C':
            location.append([i, j])
heap = []
dp = [[float('inf')] * W for _ in range(H)]
go = [[0, 1], [0, -1], [1, 0], [-1, 0]] # 0:동,1:서,2:남,3:북


def dijkstra(y, x):
    dp[y][x] = 0
    for direction in range(4):
        heapq.heappush(heap, [0, y, x, direction])
    while heap:
        cur_weight, cur_y, cur_x, cur_dir = heapq.heappop(heap)
        if dp[cur_y][cur_x] < cur_weight:
            continue
        for moved in range(4):
            ny, nx = cur_y + go[moved][0], cur_x + go[moved][1]
            if 0 <= ny < H and 0 <= nx < W and board[ny][nx] != '*':
                total_weight = cur_weight
                if cur_dir != moved:
                    total_weight += 1
                if dp[ny][nx] > total_weight:
                    dp[ny][nx] = total_weight
                    heapq.heappush(heap, [total_weight, ny, nx, moved])


dijkstra(location[0][0], location[0][1])
print(dp[location[1][0]][location[1][1]])