import sys

board = []
for _ in range(19):
    board.append(list(map(int, sys.stdin.readline().split())))

dir = [[0,1], [1,1], [1,0], [1,-1]]
flag = 0


def dfs(sy, sx, color, count, direction, way):
    if count == 5:
        dy, dx = direction
        if not (0<=sy+dy<=18 and 0<=sx+dx<=18) or board[sy+dy][sx+dx] != color: # 다음 6목에 대해 검사
            checkY, checkX = way[0][0], way[0][1]
            # 이전 6목에 대해 검사
            if not (0<=checkY+(-dy)<=18 and 0<=checkX+(-dx)<=18) or (board[checkY+(-dy)][checkX+(-dx)] != color):
                print(color)
                way.sort(key=lambda x: (x[1], x[0]))
                print(way[0][0]+1, way[0][1]+1)
                global flag
                flag = 1
                return
    if direction is None:
        for dy, dx in dir:
            ny, nx = sy+dy, sx+dx
            if 0<=ny<=18 and 0<=nx<=18 and board[ny][nx] == color:
                way.append([ny,nx])
                dfs(ny, nx, color, count+1, [dy,dx], way)
    else:
        dy, dx = direction
        ny, nx = sy + dy, sx + dx
        if 0 <= ny <= 18 and 0 <= nx <= 18 and board[ny][nx] == color:
            way.append([ny, nx])
            dfs(ny, nx, color, count + 1, [dy, dx], way)


for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            dfs(i, j, board[i][j], 1, None, [[i,j]])

if flag == 0:
    print(0)