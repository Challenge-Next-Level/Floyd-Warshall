# dfs로 풀이 가능
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

visited = [([0] * m) for _ in range(n)]

# 동, 서, 남, 북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

result = 0


def dfs(x, y, cnt, total):
    global result
    if cnt == 4:
        result = max(result, total)
        return
    else:
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]

            if not (0 <= new_x < m) or not (0 <= new_y < n):
                continue

            if visited[new_y][new_x] == 0:
                # ㅗ 모양 처리
                if cnt == 2:
                    visited[new_y][new_x] = 1
                    dfs(x, y, cnt + 1, total + board[new_y][new_x])
                    visited[new_y][new_x] = 0
                visited[new_y][new_x] = 1
                dfs(new_x, new_y, cnt + 1, total + board[new_y][new_x])
                visited[new_y][new_x] = 0


for r in range(n):
    for c in range(m):
        visited[r][c] = 1
        dfs(c, r, 1, board[r][c])
        visited[r][c] = 0
print(result)
