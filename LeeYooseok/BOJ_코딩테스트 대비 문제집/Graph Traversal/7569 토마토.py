M, N, H = map(int, input().split())

box = list()

answer = 0

ikeun_tomato = 0
ikeun_list = set()
for z in range(H):
    box_y = list()
    for y in range(N):
        box_x = list(map(int, input().split()))
        box_y.append(box_x)

        for x in range(M):
            if box_x[x] == 1:
                ikeun_list.add((x, y, z))
            if box_x[x] != 0:
                ikeun_tomato += 1
    box.append(box_y)
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    global ikeun_tomato, box, ikeun_list
    new_ikeun_list = set()
    if not ikeun_list:
        print(-1)
        exit()
    for _x, _y, _z in ikeun_list:
        for i in range(6):
            new_x, new_y, new_z = _x + dx[i], _y + dy[i], _z + dz[i]

            if not (0 <= new_x < M) or not (0 <= new_y < N) or not(0 <= new_z < H):
                continue

            if box[new_z][new_y][new_x] == 0:
                box[new_z][new_y][new_x] = 1
                ikeun_tomato += 1
                new_ikeun_list.add((new_x, new_y, new_z))

    ikeun_list = new_ikeun_list


while not (ikeun_tomato == M * N * H):
    answer += 1
    bfs()

print(answer)
