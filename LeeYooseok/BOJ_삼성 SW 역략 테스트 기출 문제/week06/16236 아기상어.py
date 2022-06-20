# 한 칸에는 물고기가 1마리만 존재
# 처음 아기상어 크기 : 2
# 아기상어 이동 : 1칸 상하좌우
# 자기보다 작은 물고기만 먹을 수 있음 -> 먹으면 크기 1 증가
# 자기보다 작거나 같은 물고기가 있는 칸만 지나갈 수 있음
# 물고기 크기는 6이 최대이다.
import sys

input = sys.stdin.readline

N = int(input())

board = list()
flag = True

for j in range(N):
    temp = list(map(int, input().split()))
    if flag:
        for i in range(N):
            if temp[i] == 9:
                # 아기 상어 x, y 위치
                temp[i] = 0
                baby_shark = [i, j]
                flag = False
                break
    board.append(temp)


# 현재 아기 상어의 size
size = 2

# 현재 먹은 물고기
num_fish = 0

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0


def find_eat_fish():
    # board 를 탐험하며 먹을 물고기를 선택한다.
    visited = [[0] * N for _ in range(N)]

    # 현재 위치 이동 시간, x, y
    queue = [[0, baby_shark[0], baby_shark[1]]]
    visited[baby_shark[1]][baby_shark[0]] = 1

    # 이동 시간, y축 위치, x축 위치
    eat_fish = [sys.maxsize, N, N]

    while queue:
        until_time, now_x, now_y = queue.pop(0)

        for k in range(4):
            new_x, new_y = now_x + dx[k], now_y + dy[k]

            if not (0 <= new_x < N) or not (0 <= new_y < N):
                continue

            if board[new_y][new_x] > size:
                continue

            if visited[new_y][new_x] == 1:
                continue

            # 먹을 수 있는 물고기이다.
            if 0 < board[new_y][new_x] < size:
                if until_time + 1 < eat_fish[0]:
                    eat_fish = [until_time + 1, new_y, new_x]
                elif until_time + 1 == eat_fish[0]:
                    if new_y < eat_fish[1]:
                        eat_fish = [until_time + 1, new_y, new_x]
                    elif new_y == eat_fish[1]:
                        if new_x < eat_fish[2]:
                            eat_fish = [until_time + 1, new_y, new_x]

            # 최소 이동 시간 >= 다음 위치의 이동시간 일때만 이동
            if eat_fish[0] >= until_time + 1:
                visited[new_y][new_x] = 1
                queue.append([until_time + 1, new_x, new_y])

    if eat_fish[0] == sys.maxsize:
        return False
    else:
        return eat_fish


while True:
    _eat_fish = find_eat_fish()

    if not _eat_fish:
        print(result)
        break
    else:
        board[baby_shark[1]][baby_shark[0]] = 0
        baby_shark = [_eat_fish[2], _eat_fish[1]]

        num_fish += 1

        if num_fish == size:
            size += 1
            num_fish = 0

        result += _eat_fish[0]
