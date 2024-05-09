import sys
from collections import deque

input = sys.stdin.readline

# 주사위 전개도
# 1 이 윗면, 6 이 아랫면
dice = [[0, 2, 0],
        [4, 1, 3],
        [0, 5, 0],
        [0, 6, 0]]


# 주사위 굴리기
# 오른쪽
def turn_right():
    global dice
    next_dice = [d[:] for d in dice]

    # next_dice = [[0, 2, 0],
    #              [6, 4, 1],
    #              [0, 5, 0],
    #              [0, 3, 0]]

    next_dice[1][0] = dice[3][1]
    next_dice[1][1] = dice[1][0]
    next_dice[1][2] = dice[1][1]
    next_dice[3][1] = dice[1][2]

    dice = [nd[:] for nd in next_dice]


# 왼쪽
def turn_left():
    global dice
    next_dice = [d[:] for d in dice]

    # next_dice = [[0, 2, 0],
    #              [1, 3, 6],
    #              [0, 5, 0],
    #              [0, 4, 0]]
    next_dice[1][0] = dice[1][1]
    next_dice[1][1] = dice[1][2]
    next_dice[1][2] = dice[3][1]
    next_dice[3][1] = dice[1][0]

    dice = [nd[:] for nd in next_dice]


# 위쪽
def turn_up():
    global dice
    next_dice = [d[:] for d in dice]

    # next_dice = [[0, 1, 0],
    #              [4, 5, 3],
    #              [0, 6, 0],
    #              [0, 2, 0]]
    next_dice[0][1] = dice[1][1]
    next_dice[1][1] = dice[2][1]
    next_dice[2][1] = dice[3][1]
    next_dice[3][1] = dice[0][1]

    dice = [nd[:] for nd in next_dice]


# 아래쪽
def turn_down():
    global dice
    next_dice = [d[:] for d in dice]

    # next_dice = [[0, 6, 0],
    #              [4, 2, 3],
    #              [0, 1, 0],
    #              [0, 5, 0]]
    next_dice[0][1] = dice[3][1]
    next_dice[1][1] = dice[0][1]
    next_dice[2][1] = dice[1][1]
    next_dice[3][1] = dice[2][1]

    dice = [nd[:] for nd in next_dice]


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 동, 남, 서, 북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

score_board = [b[:] for b in board]
visited = [[False for _ in range(M)] for _ in range(N)]


def dfs(x, y):
    now_num = board[y][x]
    stack = deque([[x, y]])
    visited[y][x] = True
    cnt = 0
    visited_loc = []

    while stack:
        now_x, now_y = stack.pop()
        cnt += 1
        visited_loc.append([now_x, now_y])

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < M) or not (0 <= new_y < N):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == now_num:
                visited[new_y][new_x] = True
                stack.append([new_x, new_y])

    for visited_x, visited_y in visited_loc:
        score_board[visited_y][visited_x] = cnt * now_num


for _x in range(M):
    for _y in range(N):
        if not visited[_y][_x]:
            dfs(_x, _y)

answer = 0

now_x, now_y = 0, 0
now_dir = 0

for _ in range(K):
    # 다음 칸 확인
    next_x, next_y = now_x + dx[now_dir], now_y + dy[now_dir]

    # 범위 벗어 나는지 확인
    if not (0 <= next_x < M) or not (0 <= next_y < N):
        now_dir = (now_dir + 2) % 4
        next_x, next_y = now_x + dx[now_dir], now_y + dy[now_dir]

    now_x, now_y = next_x, next_y

    # 주사위 굴리기
    if now_dir == 0:
        turn_right()
    elif now_dir == 1:
        turn_down()
    elif now_dir == 2:
        turn_left()
    else:
        turn_up()

    # 도착한 칸의 점수 획득
    answer += score_board[now_y][now_x]

    # 다음 굴릴 방향 확인
    A = dice[3][1]
    B = board[now_y][now_x]

    if A > B:
        now_dir = (now_dir + 1) % 4
    elif A < B:
        now_dir = (now_dir - 1) % 4

print(answer)