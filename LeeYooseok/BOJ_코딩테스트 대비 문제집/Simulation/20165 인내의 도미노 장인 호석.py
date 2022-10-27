from collections import deque

N, M, R = map(int, input().split())  # 행, 열, 라운드
board = [list(map(int, input().split())) for _ in range(N)]
domino_board = [['S' for _ in range(M)] for _ in range(N)]

dir_dict = {"E": [1, 0], "W": [-1, 0], "S": [0, 1], "N": [0, -1]}
answer = 0
for _ in range(R):
    # 공격수 행동
    A_X, A_Y, A_D = input().split()
    A_X, A_Y = int(A_X), int(A_Y)
    dx, dy = dir_dict[A_D]
    drop_que = deque()
    drop_que.append([A_X - 1, A_Y - 1])
    while drop_que:
        # A_D 방향으로 board[now_y, now_x] 만큼 엎어짐
        now_y, now_x = drop_que.popleft()
        height = board[now_y][now_x]

        # 현재 도미노가 안엎어져있다면,
        if domino_board[now_y][now_x] == 'S':
            answer += 1
            domino_board[now_y][now_x] = 'F'
            for h in range(1, height):
                new_y, new_x = now_y + dy * h, now_x + dx * h

                if (0 <= new_x < M) and (0 <= new_y < N):
                    drop_que.append([new_y, new_x])
                else:
                    continue

    # 수비수 행동
    D_X, D_Y = map(int, input().split())
    domino_board[D_X - 1][D_Y - 1] = 'S'


print(answer)
for d in domino_board:
    print(" ".join(d))

