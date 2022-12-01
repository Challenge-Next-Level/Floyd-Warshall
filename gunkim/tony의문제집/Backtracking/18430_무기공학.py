# 반복문을 돌 때 범위 조정을 통해 시간 초과를 개선 -> 이 부분이 백트래킹의 일종이지!
import sys

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
# 부메랑 만드는 4가지 경우
dir = [[[-1,0],[0,-1]],[[1,0],[0,-1]],[[-1,0],[0,1]],[[1,0],[0,1]]]
visit = [[False] * m for _ in range(n)]
answer = 0


def dfs(index, visited, total_cur):
    global answer
    if total_cur > answer:
        answer = total_cur
    for i in range(index, n): # 범위 조정으로 시간 개선
        for j in range(m):
            if visited[i][j]:
                continue
            for k in range(4):
                ny1, nx1 = i + dir[k][0][0], j + dir[k][0][1]
                ny2, nx2 = i + dir[k][1][0], j + dir[k][1][1]
                if 0 <= ny1 < n and 0 <= nx1 < m and 0 <= ny2 < n and 0 <= nx2 < m and not visited[ny1][nx1] and not visited[ny2][nx2]:
                    visited[ny1][nx1], visited[ny2][nx2], visited[i][j] = True, True, True
                    total = board[ny1][nx1] + board[ny2][nx2] + (board[i][j] * 2)
                    dfs(i, visited, total_cur+total)
                    visited[ny1][nx1], visited[ny2][nx2], visited[i][j] = False, False, False
    return


for i in range(n//2+1): # 범위 조정으로 시간 개선
    for j in range(m):
        for k in range(4):
            ny1, nx1 = i+dir[k][0][0], j+dir[k][0][1]
            ny2, nx2 = i+dir[k][1][0], j+dir[k][1][1]
            if 0<=ny1<n and 0<=nx1<m and 0<=ny2<n and 0<=nx2<m:
                visit[ny1][nx1], visit[ny2][nx2], visit[i][j] = True, True, True
                total = board[ny1][nx1] + board[ny2][nx2] + (board[i][j]*2)
                dfs(i, visit, total)
                visit[ny1][nx1], visit[ny2][nx2], visit[i][j] = False, False, False


print(answer)