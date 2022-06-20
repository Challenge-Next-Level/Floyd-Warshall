import sys
from collections import deque

M, S = map(int, input().split())

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 상어 방향 - 상, 좌, 하, 우
shark_d = [[], [-1, 0], [0, -1], [1, 0], [0, 1]]

# board 판 - 각 칸에 [[방향, ]]
fish_board = [[[] for _ in range(4)] for _ in range(4)]

# smell board 판 - 몇 번 연습에 생겼는지 표현한다.
smell_board = [[[] for _ in range(4)] for _ in range(4)]

# 물고기 현재 위치
fish_loc = set()

for _ in range(M):
    f_y, f_x, d = map(int, input().split())
    fish_board[f_y - 1][f_x - 1].append(d-1)
    fish_loc.add((f_y - 1, f_x - 1))
shark_y, shark_x = map(int, input().split())
shark_y, shark_x = shark_y - 1, shark_x - 1

def change_dict(way):
    return 100 * way[0] + 10 * way[1] + 1 * way[2]

def shark_move(s_y, s_x, input_board, input_loc, step):
    global smell_board, shark_y, shark_x
    # 먹은 물고기 수, 방법, y 위치, x 위치
    final_shark = [0, sys.maxsize, 0, 0]

    # 위치, 먹은 물고기 수, 방법, 방문 처리
    visited = [[0 for _ in range(4)] for _ in range(4)]
    queue = deque([[s_y, s_x, 0, [], visited]])

    while queue:
        now_y, now_x, now_fish, now_way, now_visited = queue.popleft()

        if len(now_way) == 3:
            if final_shark[0] < now_fish:
                final_shark = [now_fish, change_dict(now_way), now_y, now_x]
            elif final_shark[0] == now_fish:
                if final_shark[1] > change_dict(now_way):
                    final_shark = [now_fish, change_dict(now_way), now_y, now_x]
            continue

        for s_d in range(1, 5):
            new_y, new_x = now_y + shark_d[s_d][0], now_x + shark_d[s_d][1]

            if not(0 <= new_y < 4) or not(0 <= new_x < 4):
                continue

            new_visited = [item[:] for item in now_visited]

            if now_visited[new_y][new_x] == 1:
                queue.append([new_y, new_x, now_fish, now_way + [s_d], new_visited])
            else:
                new_visited[new_y][new_x] = 1
                new_fish = len(input_board[new_y][new_x])
                queue.append([new_y, new_x, now_fish + new_fish, now_way + [s_d], new_visited])
    # 죽은 물고기 냄새 남김
    n_y, n_x = s_y, s_x
    sub_loc = set()
    for m_d in str(final_shark[1]):
        n_y, n_x = n_y + shark_d[int(m_d)][0], n_x + shark_d[int(m_d)][1]
        if input_board[n_y][n_x]:
            sub_loc.add((n_y, n_x))
            for fish in input_board[n_y][n_x]:
                smell_board[n_y][n_x].append(step)
            input_board[n_y][n_x] = []
    input_loc -= sub_loc
    shark_y, shark_x = final_shark[2], final_shark[3]

    return input_board, input_loc


for s in range(S):
    # 새로운 물고기 board
    new_fish_board = [[[] for _ in range(4)] for _ in range(4)]
    # 새로운 물고기 위치
    new_fish_loc = set()
    # 1) 상어가 복제 마법을 시전한다.
    copy_fish_board = [item[:] for item in fish_board]
    copy_fish_loc = [item[:] for item in fish_loc]

    # 2) 모든 물고기가 이동한다.
    for fish_y, fish_x in fish_loc:
        for fish_d in copy_fish_board[fish_y][fish_x]:
            # 8 방향으로 이동한다.
            move_flag = False
            for d in range(8):
                # 불가능하면, 45도 반시계 방향으로 회전한다.
                new_d = (fish_d - d) % 8
                new_fish_y, new_fish_x = fish_y + dy[new_d], fish_x + dx[new_d]

                # 격자 범위 확인
                if not(0 <= new_fish_y < 4) or not(0 <= new_fish_x < 4):
                    continue

                # 냄새가 있는 칸
                if smell_board[new_fish_y][new_fish_x]:
                    continue

                # 상어가 있는 칸
                if new_fish_y == shark_y and new_fish_x == shark_x:
                    continue

                # 이동 한다.
                new_fish_board[new_fish_y][new_fish_x].append(new_d)
                new_fish_loc.add((new_fish_y, new_fish_x))
                move_flag = True
                break
            # 이동할 수 없다면 가만히 있는다.
            if not move_flag:
                new_fish_board[fish_y][fish_x].append(fish_d)
                new_fish_loc.add((fish_y, fish_x))

    # 3) 상어가 이동한다.
    new_fish_board, new_fish_loc = shark_move(shark_y, shark_x, new_fish_board, new_fish_loc, s)

    # 4) 두번 전 연습에서 생긴 물고기(상어)의 냄새가 격자에서 사라진다.
    if s >= 2:
        for _y in range(4):
            for _x in range(4):
                if len(smell_board[_y][_x]) > 0:
                    new_smell = list()
                    for smell in smell_board[_y][_x]:
                        if smell > s-2:
                            new_smell.append(smell)
                    smell_board[_y][_x] = new_smell

    # 5) 1에서 사용한 복제 마법
    for copy_fish_y, copy_fish_x in copy_fish_loc:
        new_fish_loc.add((copy_fish_y, copy_fish_x))
        for copy_fish_d in copy_fish_board[copy_fish_y][copy_fish_x]:
            new_fish_board[copy_fish_y][copy_fish_x].append(copy_fish_d)

    fish_board = new_fish_board
    fish_loc = new_fish_loc

result = 0
for __y, __x in fish_loc:
    result += len(fish_board[__y][__x])

print(result)