import sys
from collections import deque

N, M, K = map(int, input().split())

board = [list(map(int, list(input()))) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = sys.maxsize

visited = [[[-1] * (K + 1) for _ in range(M)] for _ in range(N)]

que = deque()
que.append([0, 0, K]) # 현재 위치, 이동 칸 수, 남아있는 k
visited[0][0][K] = 1

while que:
    now_x, now_y, remain_k = que.popleft()

    if now_x == M - 1 and now_y == N - 1:
        print(visited[now_y][now_x][remain_k])
        exit()

    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < M) or not(0 <= new_y < N):
            continue

        # 길이면
        if board[new_y][new_x] == 0:
            if visited[new_y][new_x][remain_k] == -1:
                visited[new_y][new_x][remain_k] = visited[now_y][now_x][remain_k] + 1
                que.append([new_x, new_y, remain_k])
        else:
            if remain_k > 0:
                if visited[new_y][new_x][remain_k - 1] == -1:
                    visited[new_y][new_x][remain_k - 1] = visited[now_y][now_x][remain_k] + 1
                    que.append([new_x, new_y, remain_k - 1])

print(-1)





