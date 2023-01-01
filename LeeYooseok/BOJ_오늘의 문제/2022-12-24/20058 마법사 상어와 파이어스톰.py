import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
A_board = [list(map(int, input().split())) for _ in range(2 ** N)]

# 동서남북
dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

def rotate(x_idx, y_idx, L):
    global A_board

    # 회전할 작은 얼음
    rot_ice = list()
    for _y in range(y_idx, y_idx + 2 ** L):
        rot_ice.append(A_board[_y][x_idx : x_idx + 2 ** L])


    # 시계 방향으로 90 도 회전
    # rot_ice = list(zip(*rot_ice[::-1]))

    # board 에 적용
    for _y in range(2 ** L):
        for _x in range(2 ** L):
            A_board[y_idx + _y][x_idx + _x] = rot_ice[2 ** L - _x - 1][_y]



L_list = list(map(int, input().split()))

for L in L_list:

    if L != 0:
        # 1) 격자 나눈 후, 시계방향으로 90도 회전
        for x_idx in range(0, 2 ** N, 2 ** L):
            for y_idx in range(0, 2 ** N, 2 ** L):
                rotate(x_idx, y_idx, L)

    temp_board = [item[:] for item in A_board]

    # 2) 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
    for y_idx in range(2 ** N):
        for x_idx in range(2 ** N):
            chk = 0
            for i in range(4):
                chk_x, chk_y = x_idx + dir_x[i], y_idx + dir_y[i]

                # 범위 확인
                if not(0 <= chk_x < 2 ** N) or not(0 <= chk_y < 2 ** N):
                    continue

                # 얼음 확인
                if A_board[chk_y][chk_x] > 0:
                    chk += 1

            if chk < 3 and temp_board[y_idx][x_idx] > 0:
                temp_board[y_idx][x_idx] -= 1

    A_board = [item[:] for item in temp_board]


# 결과 1) 남아있는 얼음의 합
sum_ans = 0
for a in A_board:
    sum_ans += sum(a)

print(sum_ans)

# 결과 2) 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수

def check(c_y, c_x):
    now_size = 0
    size_visited = [[0] * (2 ** N) for _ in range(2 ** N)]
    queue = deque([[c_y, c_x]])
    size_visited[c_y][c_x] = 1

    while queue:
        now_y, now_x = queue.popleft()
        now_size += 1

        for d in range(4):
            new_y, new_x = now_y + dir_y[d], now_x + dir_x[d]

            if not(0 <= new_y < (2 ** N)) or not(0 <= new_x < (2 ** N)):
                continue

            if A_board[new_y][new_x] == 0:
                continue

            if size_visited[new_y][new_x] != 1:
                queue.append([new_y, new_x])
                size_visited[new_y][new_x] = 1

    return now_size


size_result = 0
# 가장 큰 덩어리가 차지하는 영역의 개수
visited = [[0] * (2 ** N) for _ in range(2 ** N)]
for y in range(2 ** N):
    for x in range(2 ** N):
        if A_board[y][x] != 0 and visited[y][x] != 1:
            size = check(y, x)
            size_result = max(size, size_result)

print(size_result)
