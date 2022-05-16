import sys

n = int(sys.stdin.readline())
curves = []
for _ in range(n):
    curves.append(list(map(int, sys.stdin.readline().split())))

direct = [[1,0], [0,-1], [-1,0], [0,1]] # 예시를 그대로 반영하여 방향 생성
board = [[0] * 101 for _ in range(101)] # 보드 최대 크기로 초기화

for curve in curves:
    x, y, d, g = curve
    # 0세대 드래곤 커브 생성
    board[x][y] = board[x + direct[d][0]][y + direct[d][1]] = 1
    dragon = [[x, y], [x + direct[d][0], y + direct[d][1]]]
    cnt = 0
    while cnt < g: # g세대 까지 생성
        length = len(dragon)
        end_x, end_y = dragon[length-1][0], dragon[length-1][1] # 끝점 설정
        add_dragon = []
        for idx in range(length - 2, -1, -1):
            cur_x, cur_y = dragon[idx] # 회전하려는 현재 좌표
            nx, ny = end_x - (cur_y - end_y), end_y + (cur_x - end_x) # 좌표를 90회전시켰을 때 얻는 좌표
            board[nx][ny] = 1
            add_dragon.append([nx, ny])
        dragon += add_dragon
        cnt += 1

result = 0
for y in range(100):
    for x in range(100):
        if board[y][x] == 1 and board[y][x + 1] == 1 and board[y + 1][x] == 1 and board[y + 1][x + 1] == 1:
            result += 1
print(result)