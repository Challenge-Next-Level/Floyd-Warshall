from collections import deque

N, M = map(int, input().split())

board = [i for i in range(100)]
for _ in range(N):
    x, y = map(int, input().split())
    board[x - 1] = (y - 1)
for _ in range(M):
    u, v = map(int, input().split())
    board[u - 1] = (v - 1)

visited = [i for i in range(100)]

que = deque([[0, 0]])

while que:
    now_idx, cnt = que.popleft()

    if now_idx == 99:
        print(cnt)
        exit()

    # 주사위 던짐
    for i in range(1, 7):
        next_idx = now_idx + i
        if next_idx >= 100:
            continue
        # 사다리 또는 뱀이 있는 곳에 또 사다리 또는 뱀이 있는 경우
        while next_idx != board[next_idx]:
            next_idx = board[next_idx]

        if visited[next_idx] > cnt + 1:
            visited[next_idx] = cnt + 1
            que.append([next_idx, cnt + 1])