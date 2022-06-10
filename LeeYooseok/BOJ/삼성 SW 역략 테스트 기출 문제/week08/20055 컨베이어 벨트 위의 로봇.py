N, K = map(int, input().split())

# 내구도
A_board = list(map(int, input().split()))

# 올리는 위치
up = 0
# if up == -1: up = 2N - 1
# down = (up + N - 1) % 2N

# 올라간 로봇
robot_list = list()
# 로봇이 올라간 위치
visited = [0] * (2 * N)

step = 0
while True:
    step += 1

    # 한칸 회전한다.
    up -= 1
    if up == -1:
        up = 2 * N - 1

    # down 확인
    down = (up + N - 1) % (2 * N)
    if visited[down] == 1:
        visited[down] = 0
        robot_list.remove(down)

    rm_idx = -1
    # 로봇이 이동한다.
    for i in range(len(robot_list)):
        robot = robot_list[i]
        next_robot = robot + 1
        if next_robot == 2 * N:
            next_robot = 0
        # 이동할 수 있는지 확인
        if not (visited[next_robot] == 1) and not(A_board[next_robot] < 1):
            # 이동한다.
            visited[robot] = 0
            robot_list[i] = next_robot
            visited[next_robot] = 1

            # 내구도 감소
            A_board[next_robot] -= 1

        # 내릴 수 있는지 확인
        now_idx = robot_list[i]
        if down == now_idx:
            robot_list[i] = -1
            rm_idx = i
            visited[now_idx] = 0
    if rm_idx != -1:
        robot_list.pop(rm_idx)

    # 올릴 수 있는지 확인
    if not(A_board[up] == 0) and not(visited[up] == 1):
        robot_list.append(up)
        A_board[up] -= 1
        visited[up] = 1

    # 내구도 확인
    if A_board.count(0) >= K:
        print(step)
        break
