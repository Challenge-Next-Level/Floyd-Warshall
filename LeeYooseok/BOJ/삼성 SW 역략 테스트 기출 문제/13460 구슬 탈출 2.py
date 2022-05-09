"""
겹쳤을 때, 이동 횟수가 더 많은 것이 한칸 뒤로
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = list()

# 현재 파랑, 빨강 공 위치
B_y, B_x, R_y, R_x = 0, 0, 0, 0

for i in range(n):
    ith = list(input())

    if 'B' in ith:
        B_y = i
        B_x = ith.index('B')

    if 'R' in ith:
        R_y = i
        R_x = ith.index('R')
    board.append(ith)

# blue, red visited
visited = {(B_y, B_x, R_y, R_x)}

temp = deque()
temp.append((0, B_y, B_x, R_y, R_x))

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def go(y, x, direct_y, direct_x):
    move_cnt = 0
    # 다음이 벽이 아니거나, 현재가 구멍이 아닐때 까지
    while board[y + direct_y][x + direct_x] != "#" and board[y][x] != 'O':
        x += direct_x
        y += direct_y
        move_cnt += 1

    return y, x, move_cnt


def bfs():
    while temp:
        depth, By, Bx, Ry, Rx = temp.popleft()

        if depth >= 10:
            return -1

        # 4 방향 이동
        for j in range(4):
            new_By, new_Bx, move_B_cnt = go(By, Bx, dy[j], dx[j])
            new_Ry, new_Rx, move_R_cnt = go(Ry, Rx, dy[j], dx[j])

            # 파랑 구슬과 빨강 구슬이 동시에 구멍에 떨어지면 실패
            if board[new_By][new_Bx] == 'O' and board[new_Ry][new_Rx] == 'O':
                continue

            # 파랑 구슬이 떨어지면 -> continue
            if board[new_By][new_Bx] == 'O':
                continue

            # 빨강 구슬이 떨어지면 -> return 현재 횟수
            if board[new_Ry][new_Rx] == 'O':
                return depth + 1

            # 겹친 경우
            if new_By == new_Ry and new_Bx == new_Rx:
                # 파란색이 더 적게 움직이면 -> 빨강색을 뒤로 한칸 이동
                if move_R_cnt > move_B_cnt:
                    new_Ry -= dy[j]
                    new_Rx -= dx[j]
                # 빨강색이 더 적게 움직이면 -> 파란색을 뒤로 한칸 이동
                else:
                    new_By -= dy[j]
                    new_Bx -= dx[j]

            # 모든 경우가 만족 안할 때 -> 그냥 움직임 (방문 여부 확인)
            if (new_By, new_Bx, new_Ry, new_Rx) not in visited:
                visited.add((new_By, new_Bx, new_Ry, new_Rx))
                temp.append((depth + 1, new_By, new_Bx, new_Ry, new_Rx))
    return -1


print(bfs())
