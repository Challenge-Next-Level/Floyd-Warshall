from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽 부수기 사용안한 상태, 벽 부수기 사용한 상태
visited = [[[False, False] for _ in range(M)] for _ in range(N)]

# x, y, 움직임 횟수, 벽 부수기 사용 여부
deq = deque([[0, 0, 1, False]])
visited[0][0][0] = True

while deq:
    x, y, move_cnt, used = deq.popleft()

    if x == M - 1 and y == N - 1:
        print(move_cnt)
        exit()

    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]

        if not(0 <= next_x < M) or not(0 <= next_y < N):
            continue

        if visited[next_y][next_x][used]:
            continue

        if board[next_y][next_x] == "1" and not used:
            visited[next_y][next_x][1] = True
            deq.append([next_x, next_y, move_cnt + 1, True])

        if board[next_y][next_x] == "0":
            visited[next_y][next_x][used] = True
            deq.append([next_x, next_y, move_cnt + 1, used])
print(-1)