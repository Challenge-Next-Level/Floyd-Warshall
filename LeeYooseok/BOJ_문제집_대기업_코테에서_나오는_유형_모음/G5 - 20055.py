N, K = map(int, input().split())

A_board = list(map(int, input().split()))

robot_list = list()
visited = [0 for _ in range(2 * N)]

up = 0

step = 0
while True:
    step += 1

    # 한칸 회전한다.
    up -= 1
    if up == -1:
        up = 2 * N - 1

    down = (up + N - 1) % (2 * N)
    # 내릴 로봇이 있는지 확인한다.
    if visited[down] == 1:
        visited[down] = 0
        robot_list.remove(down)

    # 가장 먼저 벨트에 올라간 로봇부터,
    for robot_idx in range(len(robot_list)):
        robot = robot_list[robot_idx]
        # 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
        next_idx = robot + 1
        if next_idx == 2 * N:
            next_idx = 0

        # 이동할 수 있는지 확인
        if visited[next_idx] == 0 and A_board[next_idx] > 0:
            visited[robot] = 0
            robot_list[robot_idx] = next_idx
            visited[next_idx] = 1
            A_board[next_idx] -= 1

    # 내릴 로봇이 있는지 확인한다.
    if visited[down] == 1:
        visited[down] = 0
        robot_list.remove(down)

    # 로봇 올리기
    if visited[up] == 0 and A_board[up] > 0:
        visited[up] = 1
        robot_list.append(up)
        A_board[up] -= 1

    # 내구성 확인
    if A_board.count(0) >= K:
        print(step)
        exit()
