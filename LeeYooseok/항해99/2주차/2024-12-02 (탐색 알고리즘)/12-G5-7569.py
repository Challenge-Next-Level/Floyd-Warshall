import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

completed_tomato_list = list()
completed_tomato_cnt = 0
box = list()
for _h in range(H):
    h_box = list()

    for _y in range(N):
        x_box = list(map(int, input().split()))
        for _x in range(M):
            if x_box[_x] == 1:
                completed_tomato_list.append([_x, _y, _h])
            if x_box[_x] != 0:
                completed_tomato_cnt += 1
        h_box.append(x_box)
    box.append(h_box)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]


def BFS():
    global completed_tomato_list, completed_tomato_cnt, box

    new_completed_tomato_set = set()
    if not completed_tomato_list:
        print(-1)
        exit()

    for now_x, now_y, now_h in completed_tomato_list:
        for i in range(6):
            next_x, next_y, next_h = now_x + dx[i], now_y + dy[i], now_h + dh[i]

            if not (0 <= next_x < M) or not (0 <= next_y < N) or not (0 <= next_h < H):
                continue

            if box[next_h][next_y][next_x] == 0:
                box[next_h][next_y][next_x] = 1
                completed_tomato_cnt += 1
                new_completed_tomato_set.add((next_x, next_y, next_h))

    completed_tomato_list = list(new_completed_tomato_set)


answer = 0
while not (completed_tomato_cnt == M * N * H):
    answer += 1
    BFS()

print(answer)
