# 인접 하다. - 동서남북

N = int(input())

# 인접 - 동, 서, 남, 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

board = [[0] * N for _ in range(N)]

shark_dict = dict()
shark_list = list()
for _ in range(N ** 2):
    temp = list(map(int, input().split()))
    shark_dict[temp[0]] = temp[1:]
    shark_list.append(temp[0])


# 학생 자리 배치
for i in shark_list:
    # 주변에 좋아하는 친구, 비어 있는 칸, 행, 열
    seat = [0, 0, N, N]
    # 비어 있는 칸 확인
    for y in range(N):
        for x in range(N):
            now_friends = 0
            now_empty = 0
            # 현재 자리가 비어있는지 확인
            if board[y][x] == 0:
                # 4 방향 확인하여 좋아하는 친구 있는지 확인
                for j in range(4):
                    n_y, n_x = y + dy[j], x + dx[j]

                    if not (0 <= n_y < N) or not (0 <= n_x < N):
                        continue

                    if board[n_y][n_x] in shark_dict[i]:
                        now_friends += 1
                    elif board[n_y][n_x] == 0:
                        now_empty += 1

                # 비교해서 자리 설정
                if seat[0] < now_friends:
                    seat = [now_friends, now_empty, y, x]
                elif seat[0] == now_friends:
                    if seat[1] < now_empty:
                        seat = [now_friends, now_empty, y, x]
                    elif seat[1] == now_empty:
                        if seat[2] > y:
                            seat = [now_friends, now_empty, y, x]
                        elif seat[2] == y:
                            if seat[3] > x:
                                seat = [now_friends, now_empty, y, x]

    board[seat[2]][seat[3]] = i

# 호감도 확인
result = 0
for y in range(N):
    for x in range(N):
        friends_num = 0
        # 4 방향 확인
        for d in range(4):
            n_y, n_x = y + dy[d], x + dx[d]

            if not (0 <= n_y < N) or not (0 <= n_x < N):
                continue

            if board[n_y][n_x] in shark_dict[board[y][x]]:
                friends_num += 1

        if friends_num == 1:
            result += 1
        elif friends_num == 2:
            result += 10
        elif friends_num == 3:
            result += 100
        elif friends_num == 4:
            result += 1000

print(result)


