R, C, N = map(int, input().split())

board = list()

for _ in range(R):
    board.append(list(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

if N == 1:
    # 초기 상태
    result = [item[:] for item in board]
elif N % 2 == 0:
    # 전체 깔림
    result = [['O' for _ in range(C)] for _ in range(R)]
elif N > 1:

    bomb1 = [['O' for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'O':
                bomb1[r][c] = '.'
                for i in range(4):
                    new_r = r + dy[i]
                    new_c = c + dx[i]
                    if 0 <= new_c < C and 0 <= new_r < R:
                        bomb1[new_r][new_c] = '.'

    bomb2 = [['O' for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if bomb1[r][c] == 'O':
                bomb2[r][c] = '.'
                for i in range(4):
                    new_r = r + dy[i]
                    new_c = c + dx[i]
                    if 0 <= new_c < C and 0 <= new_r < R:
                        bomb2[new_r][new_c] = '.'

    if N % 4 == 1:
        # 2번 폭발
        result = [item[:] for item in bomb2]
    elif N % 4 == 3:
        # 1번 폭발
        result = [item[:] for item in bomb1]

for r in result:
    print("".join(r))
