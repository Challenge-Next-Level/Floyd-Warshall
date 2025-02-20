from collections import deque

R, C = map(int, input().split())
board = list()
start_x, start_y = 0, 0
fire_list = []
for y in range(R):
    x_board = list(input())
    for x in range(C):
        if x_board[x] == "J":
            start_x, start_y = x, y
        if x_board[x] == "F":
            fire_list.append((x, y))
    board.append(x_board)

visited = [[False for _ in range(C)] for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

deq = deque()
deq.append([start_x, start_y, 0])

while deq:
    now_x, now_y, move_cnt = deq.popleft()

    if (now_x == 0 or now_x == C - 1 or now_y == 0 or now_y == R - 1) and board[now_y][now_x] != "F":
        print(move_cnt + 1)
        exit()

    # 이동
    for i in range(4):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not(0 <= new_x < C) or not(0 <= new_y < R):
            continue

        if visited[new_y][new_x]:
            continue

        if board[new_y][new_x] != ".":
            continue

        visited[new_y][new_x] = True
        deq.append([new_x, new_y, move_cnt + 1])

    # 불 옮기기 필요 여부 -> 현재 move_cnt 가 다 끝났으면
    if deq and deq[0][2] > move_cnt:
        # 불 옮기기
        new_fire_list = set()
        for fire_x, fire_y in fire_list:
            for i in range(4):
                new_fire_x, new_fire_y = fire_x + dx[i], fire_y + dy[i]

                if not (0 <= new_fire_x < C) or not (0 <= new_fire_y < R):
                    continue

                if board[new_fire_y][new_fire_x] != ".":
                    continue

                board[new_fire_y][new_fire_x] = "F"
                new_fire_list.add((new_fire_x, new_fire_y))
        # fire_list 갱신 -> 기존의 불은 더이상 번질 이유가 없기 때문에, 새로 번진 불만 넣어준다.
        fire_list = list(new_fire_list)

print("IMPOSSIBLE")
