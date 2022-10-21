import sys

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dir = [[1,0], [-1,0], [0,1], [0,-1]]
answer = float('inf')


def dfs(sy, sx, vis, count, cost):
    if count >= 3: # 꽃 3개 이상을 심었다면 return
        global answer
        answer = min(answer, cost)
        return
    # 모든 경우에 대해 탐색
    for ny in range(sy, n-1):
        for nx in range(1, n-1):
            if vis[ny][nx]: # 씨앗 위치 사용된 장소라면 continue
                continue
            flag = 0
            totalCost = board[ny][nx]
            for dy, dx in dir:
                if vis[ny+dy][nx+dx]:
                    flag = 1
                    break
                totalCost += board[ny+dy][nx+dx]
            if flag == 1: # 꽃이 되는 장소가 사용된 장소라면 continue
                continue
            else: # 모두 사용할 수 있다면 dfs 탐색
                vis[ny][nx] = True
                for dy, dx in dir:
                    vis[ny + dy][nx + dx] = True
                dfs(ny, nx, vis, count+1, cost+totalCost)
                vis[ny][nx] = False
                for dy, dx in dir:
                    vis[ny + dy][nx + dx] = False


for i in range(1, n-1):
    for j in range(1, n-1):
        visit = [[False for _ in range(n)] for _ in range(n)]
        initialCost = board[i][j]
        visit[i][j] = True
        for dy, dx in dir:
            initialCost += board[i + dy][j + dx]
            visit[i + dy][j + dx] = True
        dfs(i,j,visit,1,initialCost)

print(answer)