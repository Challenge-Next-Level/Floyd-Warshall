N, M = map(int, input().split())

A_board = [list(map(int, input().split())) for _ in range(N)]

# 방향
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

# 위치 - N-1, 1
cloud_list = [[N-2, 0], [N-1, 0], [N-2, 1], [N-1, 1]]

for _ in range(M):
    d, s = map(int, input().split())

    # 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    old_cloud = [[0 for _ in range(N)] for _ in range(N)]

    # 2) 에서 물이 증가한칸
    water_add = set()

    # 1) 모든 구름이 di 방향으로 si칸 이동한다.
    for cloud in cloud_list:
        n_y, n_x = (cloud[0] + dy[d] * s) % N, (cloud[1] + dx[d] * s) % N
        old_cloud[n_y][n_x] = 1
        # 2) 물이 증가한다.
        A_board[n_y][n_x] += 1
        water_add.add((n_y, n_x))

    new_board = [item[:] for item in A_board]

    cloud_list = list()

    # 4) 물 복사 버그
    for water_copy in water_add:
        add_water = 0
        # 2, 4, 6, 8 대각선 방향
        for d in range(2, 10, 2):
            copy_y, copy_x = water_copy[0] + dy[d], water_copy[1] + dx[d]

            # 범위 벗어나는지 확인
            if not (0 <= copy_y < N) or not (0 <= copy_x < N):
                continue

            if A_board[copy_y][copy_x] > 0:
                add_water += 1

        new_board[water_copy[0]][water_copy[1]] += add_water

    A_board = [item[:] for item in new_board]

    # 5) cloud 생성
    for _y in range(N):
        for _x in range(N):
            # 물의 양이 2 이상인 칸
            if A_board[_y][_x] >= 2:
                if old_cloud[_y][_x] != 1:
                    cloud_list.append([_y, _x])
                    A_board[_y][_x] -= 2

result = 0
for b in A_board:
    result += sum(b)

print(result)
