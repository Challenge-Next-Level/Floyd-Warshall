# 판 회전하는거 및 작은 판으로 쪼개서 회전하는거 꿀팁
# 해당 판을 추출하여 small_board 에 대입
# list(zip(*small_board[::-1])) - 회전
# 새로운 큰 판에 인덱스 맞춰서 값 넣어줌

import sys
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

A_board = [list(map(int, input().split())) for _ in range(2 ** N)]

# 0 <= l <= N
L_list = list(map(int, input().split()))

# 동, 서, 남, 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for l in L_list:
    # 회전 완료
    if l != 0:
        new_board = [[0] * (2 ** N) for _ in range(2 ** N)]
        for j in range(0, 2 ** N, 2 ** l):
            for i in range(0, 2 ** N, 2 ** l):
                # 회전할 작은 얼음 판
                rot_ice = list()
                for _y in range(j, j + 2**l):
                    rot_ice.append(A_board[_y][i:i + 2**l])

                # 시계 방향으로 90도 회전
                rot_ice = list(zip(*rot_ice[::-1]))

                for y in range(2 ** l):
                    for x in range(2 ** l):
                        new_board[j + y][i + x] = rot_ice[y][x]

        A_board = [item[:] for item in new_board]

    new_board = [item[:] for item in A_board]
    # 녹는 얼음 확인
    for y in range(2 ** N):
        for x in range(2 ** N):
            cnt = 0
            # 인접한 4방향 확인
            for d in range(4):
                new_y, new_x = y + dy[d], x + dx[d]

                if not(0 <= new_x < (2 ** N)) or not(0 <= new_y < (2 ** N)):
                    continue

                # 인접한 곳에 얼음이 있다면
                if A_board[new_y][new_x] > 0:
                    cnt += 1

            if cnt < 3 and new_board[y][x] >= 1:
                new_board[y][x] -= 1

    A_board = [item[:] for item in new_board]

# 남아 있는 얼음의 양의 합
sum_result = 0
for b in A_board:
    sum_result += sum(b)
print(sum_result)

def check(c_y, c_x):
    now_size = 0
    size_visited = [[0] * (2 ** N) for _ in range(2 ** N)]
    queue = deque([[c_y, c_x]])
    size_visited[c_y][c_x] = 1

    while queue:
        now_y, now_x = queue.popleft()
        now_size += 1

        for d in range(4):
            new_y, new_x = now_y + dy[d], now_x + dx[d]

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

