import sys

r, c, m = map(int, sys.stdin.readline().split())
sharks = []
for _ in range(m):
    # r, c: 좌표 / s: 속력 / d: 이동방향 / z: 크기
    sr, sc, s, d, z = map(int, sys.stdin.readline().split())
    sharks.append([sr - 1, sc - 1, s, d, z, 1])  # 1: alive, 0: death
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def move(y, x, cnt, di): # cnt: 이동해야하는 칸 수
    if cnt <= 0:
        return [y, x, di]
    ny, nx = y + dir[di][0], x + dir[di][1]
    if 0 <= ny < r and 0 <= nx < c:
        return move(ny, nx, cnt - 1, di)
    else:
        d = (di + 2) % 4
        ny, nx = y + dir[d][0], x + dir[d][1]
        return move(ny, nx, cnt - 1, d)


def calculate_dir(di): # 내 방식대로 방향 계산하여 리턴
    if di == 1:
        return 0
    elif di == 2:
        return 2
    elif di == 3:
        return 1
    elif di == 4:
        return 3


length = len(sharks)
for i in range(length): # 내 방식대로 상어의 방향 설정 다시 해주기(계산하기 쉽게 하기 위해)
    sharks[i][3] = calculate_dir(sharks[i][3])

answer = 0
idx = 0 # 사람의 위치
while idx <= c:
    min_index = [r, -1]
    for i in range(length): # 해당 열에서 가장 가까운 상어 찾기
        if sharks[i][-1] == 1 and sharks[i][1] == idx and min_index[0] > sharks[i][0]:
            min_index = [sharks[i][0], i]
    if 0 <= min_index[0] < r: # 상어가 있다면 잡기
        answer += sharks[min_index[1]][-2]
        sharks[min_index[1]][-1] = 0

    idx += 1 # 사람 이동

    # 상어 이동
    location = [[[0, 0] for _ in range(c)] for _ in range(r)] # 사이즈, sharks 내 index
    for i in range(length):
        if sharks[i][-1] == 1:
            if sharks[i][3] == 0 or sharks[i][3] == 2: # 상어의 속력을 최대로 줄이기(재귀 깊이를 적게하기 위함)
                speed = sharks[i][2] % ((r - 1) * 2)
            else:
                speed = sharks[i][2] % ((c - 1) * 2)
            info = move(sharks[i][0], sharks[i][1], speed, sharks[i][3]) # 상어 이동
            sharks[i][0], sharks[i][1], sharks[i][3] = info[0], info[1], info[2] # 상어 좌표, 방향 수정
            if location[sharks[i][0]][sharks[i][1]][0] < sharks[i][-2]: # 같은 장소에 있는 상어 고려
                if location[sharks[i][0]][sharks[i][1]][0] != 0:
                    sharks[location[sharks[i][0]][sharks[i][1]][1]][-1] = 0
                location[sharks[i][0]][sharks[i][1]] = [sharks[i][-2], i]
            else:
                sharks[i][-1] = 0
print(answer)
