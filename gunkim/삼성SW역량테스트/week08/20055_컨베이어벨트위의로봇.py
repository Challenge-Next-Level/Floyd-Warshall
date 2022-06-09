import sys

n, k = map(int, sys.stdin.readline().split())
A = [-1] + list(map(int, sys.stdin.readline().split()))

conveyor = 2 * n # 컨베이어 벨트의 끝 부분의 index
length = 2 * n + 1
robot = [0 for _ in range(length)]
time = 0
while True:
    if A.count(0) >= k:
        print(time)
        break
    # 컨베이어 벨트 한 칸 이동, 내리는 곳에 있는 로봇은 없앤다
    down = conveyor - (n + 1) # 내리는 곳 index
    if down <= 0:
        down += 2 * n
    if robot[down] == 1:
        robot[down] = 0
    conveyor -= 1 # 컨베이어 벨트 끝 부분 index 이동
    if conveyor == 0:
        conveyor = 2 * n
    # 로봇이 우측으로 스스로 이동한다, 내리는 곳에 있는 로봇은 없앤다
    for i in range(conveyor, conveyor - length, -1):
        index = i
        if index <= 0:
            index += 2 * n
        if robot[index] == 1:
            if index + 1 > 2 * n:
                if robot[1] == 0 and A[1] > 0:
                    robot[1] = 1
                    robot[index] = 0
                    A[1] -= 1
            else:
                if robot[index + 1] == 0 and A[index + 1] > 0:
                    robot[index + 1] = 1
                    robot[index] = 0
                    A[index + 1] -= 1
    if robot[down] == 1:
        robot[down] = 0
    # 로봇을 올린다
    idx = conveyor + 1
    if idx > 2 * n:
        idx = 1
    if robot[idx] == 0 and A[idx] > 0:
        robot[idx] = 1
        A[idx] -= 1
    time += 1