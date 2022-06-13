import sys
from collections import deque

r, c, k = map(int, sys.stdin.readline().split())
board = [[[0,0,0] for _ in range(c)] for _ in range(r)] # [현재온도, 들어온 온도, 나간 온도]
aircon = []
target = []
for i in range(r):
    li = list(map(int, sys.stdin.readline().split()))
    for j in range(c):
        if li[j] == 5: # 조사 지점 좌표 저장
            target.append([i, j])
        elif li[j] == 1: # 온풍기 위치, 방향 저장
            aircon.append([i, j, 1])
        elif li[j] == 2:
            aircon.append([i, j, 3])
        elif li[j] == 3:
            aircon.append([i, j, 0])
        elif li[j] == 4:
            aircon.append([i, j, 2])

w = int(sys.stdin.readline().split()[0])
wall = [[[False]*4 for _ in range(c)] for _ in range(r)]
for _ in range(w):
    sy, sx, d = map(int, sys.stdin.readline().split())
    sy -= 1
    sx -= 1
    if d == 0: # 현재좌표의 북쪽, 현재 위 좌표의 남쪽 체크
        wall[sy][sx][0] = wall[sy-1][sx][2] = True
    elif d == 1: # 현재좌표의 동쪽, 현재 오른쪽 좌표의 서쪽체크
        wall[sy][sx][1] = wall[sy][sx+1][3] = True

dir = [[-1,0], [0,1], [1,0], [0,-1]] # 북동남서
visit = [[0 for _ in range(c)] for _ in range(r)]
visited_num = 0


def wind():
    global visited_num, visit, board

    for ay, ax, num in aircon:
        ny, nx = ay + dir[num][0], ax + dir[num][1]
        queue = deque([[ny, nx]])
        visited_num += 1
        visit[ny][nx] = visited_num
        board[ny][nx][0] += 5

        for heat in range(4, 0, -1):
            if not queue:
                break
            q_len = len(queue)
            for idx in range(q_len):
                y, x = queue.pop()

                # 왼쪽 대각선 방향 진행
                qy = y + dir[num][0] + dir[(num + 3) % 4][0]
                qx = x + dir[num][1] + dir[(num + 3) % 4][1]
                if can_wind(qy, qx, (num + 2) % 4) and not wall[y][x][(num + 3) % 4]:
                    board[qy][qx][0] += heat
                    visit[qy][qx] = visited_num
                    queue.appendleft([qy, qx])
                # 현재 방향 진행
                qy = y + dir[num][0]
                qx = x + dir[num][1]
                if can_wind(qy, qx, (num + 2) % 4):
                    board[qy][qx][0] += heat
                    visit[qy][qx] = visited_num
                    queue.appendleft([qy, qx])
                # 오른쪽 대각선 방향 진행
                qy = y + dir[num][0] + dir[(num + 1) % 4][0]
                qx = x + dir[num][1] + dir[(num + 1) % 4][1]
                if can_wind(qy, qx, (num + 2) % 4) and not wall[y][x][(num + 1) % 4]:
                    board[qy][qx][0] += heat
                    visit[qy][qx] = visited_num
                    queue.appendleft([qy, qx])


# flag는 wind() 함수에서 사용할 때 visit여부를 보기 위해 사용
# set_temperature()에서는 visit을 보지 않기 때문에 False를 넣어 사용
def can_wind(y, x, di, flag=True):
    global visited_num

    if not (0 <= y < r and 0 <= x < c):
        return False
    if wall[y][x][di]:
        return False
    if flag and visit[y][x] == visited_num:
        return False
    return True


def set_temperature():
    global board
    for y in range(r): # 두 칸의 온도차를 계산하여 정보로 저장
        for x in range(c):
            if board[y][x][0] == 0:
                continue
            for di in range(4):
                ny, nx = y + dir[di][0], x + dir[di][1]
                if can_wind(ny, nx, (di + 2) % 4, False) and board[y][x][0] > board[ny][nx][0]:
                    temp = (board[y][x][0] - board[ny][nx][0]) // 4
                    board[ny][nx][1] += temp
                    board[y][x][2] += temp

    for y in range(r): # 계산된 정보로 현재 온도 갱신
        for x in range(c):
            board[y][x][0] += board[y][x][1] - board[y][x][2]
            board[y][x][1] = board[y][x][2] = 0

    for y in range(r): # 제일 외각인 곳 온도 감소
        for x in range(c):
            if x == 0 or y == 0 or y == r - 1 or x == c - 1:
                if board[y][x][0] > 0:
                    board[y][x][0] -= 1


def check_target():
    for ty, tx in target:
        if board[ty][tx][0] < k:
            return False
    return True


answer = 0 # 초콜릿
while True:
    # 1. 모든 온풍기에서 바람이 한 번 나옴
    wind()
    # 2. 온도가 조절됨
    # 3. 가장 바깥 쪽 칸의 온도는 1씩 감소
    set_temperature()
    # 4. 초콜릿 먹기
    answer += 1
    # 5. 모든 칸의 온도가 k 이상이면 중단 or 1부터 다시 시작
    if answer > 100:
        print(answer)
        break
    if check_target():
        print(answer)
        break