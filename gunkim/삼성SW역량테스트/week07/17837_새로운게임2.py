# 그래도 첫 제출에 바로 정답을 맞췄다. 살짝 놓쳤던 부분은
# 1. (반대 방향이 영역 안 + 파란색이 아니라면 이동) 이라고 적은 것에서 영역 조건을 처음에 빠트렸다
# 2. 그 뒤로 빨간 영역이 나올 수 있다는 조건도 생각하지 못했었다.
import sys


n, k = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split()))) # 0:흰,1:빨,2:파
location = [[[] for _ in range(n)] for _ in range(n)] # 말들을 좌표에 넣어줌


dir = [[0,1], [1,0], [0,-1], [-1,0]]
def check_dir(d): # 내 방식대로 방향 index 재정의
    # 기존 동서북남 순서
    if d == 1:
        return 0
    elif d == 2:
        return 2
    elif d == 3:
        return 3
    elif d == 4:
        return 1

chess = []
for num in range(k): # k개의 체스들의 좌표와 방향을 저장
    y, x, d = map(int, sys.stdin.readline().split())
    chess.append([y - 1, x - 1, check_dir(d)])
    location[y - 1][x - 1].append(num + 1)

turn = 1
while True:
    if turn > 1000: # 턴이 1000번을 넘는다면 -1 출력
        print(-1)
        exit()
    for i in range(k): # k개의 체스들을 이동시킨다
        y, x, d = chess[i]
        ny, nx = y + dir[d][0], x + dir[d][1]
        if not (0 <= ny < n and 0 <= nx < n) or board[ny][nx] == 2: # 영역 밖 or 파란색
            d = (d + 2) % 4
            ny, nx = y + dir[d][0], x + dir[d][1]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 2: # 반대 방향이 영역 안 + 파란색이 아니라면 이동
                idx = location[y][x].index(i + 1)
                length = len(location[y][x][idx:])
                for j in range(idx, idx + length):
                    chess[location[y][x][j] - 1][0], chess[location[y][x][j] - 1][1] = ny, nx
                if board[ny][nx] == 1: # 빨간 영역이면 역순으로 이동
                    location[ny][nx] += reversed(location[y][x][idx:])
                else: # 흰색이면 그대로 이동
                    location[ny][nx] += location[y][x][idx:]
                if len(location[ny][nx]) >= 4:
                    print(turn)
                    exit()
                location[y][x] = location[y][x][:idx]
            chess[i][2] = d
        else: # 영역 안 and (흰색 or 빨간색)
            idx = location[y][x].index(i + 1)
            length = len(location[y][x][idx:])
            for j in range(idx, idx + length):
                chess[location[y][x][j] - 1][0], chess[location[y][x][j] - 1][1] = ny, nx
            if board[ny][nx] == 1:  # 빨간 영역이면 역순으로 이동
                location[ny][nx] += reversed(location[y][x][idx:])
            else:  # 흰색이면 그대로 이동
                location[ny][nx] += location[y][x][idx:]
            if len(location[ny][nx]) >= 4:
                print(turn)
                exit()
            location[y][x] = location[y][x][:idx]
    turn += 1