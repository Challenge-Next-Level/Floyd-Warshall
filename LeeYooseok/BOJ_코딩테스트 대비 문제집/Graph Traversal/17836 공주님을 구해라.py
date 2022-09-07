import sys
from collections import deque

N, M, T = map(int, input().split())

board = list()
for y in range(N):
    x_board = list(map(int, input().split()))

    for x in range(M):
        if x_board[x] == 2:
            gram = [x, y]
            x_board[x] = 0
    board.append(x_board)

answer = sys.maxsize

visited = [[False for _ in range(M)] for _ in range(N)]

que = deque()
que.append([0, 0, 0, False]) # 시간, x, y, gram 획득 여부

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while que:
    now_t, now_x, now_y, gram_able = que.popleft()

    if now_x == M-1 and now_y == N-1:
        answer = min(answer, now_t)

    if [now_x, now_y] == gram:
        gram_able = True
        # visited 초기화 (gram 을 얻고 목적지로 가는 경우)
        visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < M) or not(0 <= new_y < N):
            continue

        if visited[new_y][new_x]:
            continue

        if not gram_able and board[new_y][new_x] == 1:
            continue

        if now_t + 1 < answer:
            que.append([now_t + 1, new_x, new_y, gram_able])
            visited[new_y][new_x] = True

if answer > T:
    print("Fail")
else:
    print(answer)


