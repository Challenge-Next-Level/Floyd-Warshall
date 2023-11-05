# DFS
R, C, K = map(int, input().split())

board = [list(input()) for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
visited = [[False for _ in range(C)] for _ in range(R)]

def dfs(x, y, distance):
    global answer

    if distance == K and x == C - 1 and y == 0:
        answer += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 백트래킹 한정 조건 : board[nx][ny] == '.'
            if 0 <= nx < C and 0 <= ny < R and board[ny][nx] == '.' and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(nx, ny, distance + 1)
                # 원래 상태로 돌려 놓아 다른 방향으로 다시 탐색하도록 한다.
                visited[ny][nx] = False


visited[R - 1][0] = True
dfs(0, R - 1, 1)
# 정답
print(answer)
