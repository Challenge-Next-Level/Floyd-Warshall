# 체스판의 크기 N, 말의 개수 K
N, K = map(int, input().split())

# 0은 흰색, 1은 빨간색, 2는 파란색
board = [list(map(int, input().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 말의 정보 : 행, 열의 번호, 이동 방향(동, 서, 북, 남)
player = dict()
player_board = [[[] for _ in range(N)] for _ in range(N)]
for k in range(K):
    y, x, d = map(int, input().split())
    player[k + 1] = [y - 1, x - 1, d - 1]
    player_board[y-1][x-1].append(k+1)

for t in range(1, 1001):
    # 각 말 이동
    _k = 0
    for p in player:
        _k += 1
        y, x, d = p
        new_x, new_y = x + dx[d], y + dy[d]

        # 흰색일 경우 : _k 부터 이동
        if board[new_y][new_x] == 0:
            new_player_board = list()
            is_k = False
            for _p in player_board[y][x]:
                if _p == _k or is_k:
                    is_k = True
                    player_board[new_y][new_x].append(_p)
                    player[_p] = [new_y, new_x, d]
                else:
                    new_player_board.append(_p)
            player_board[y][x] = new_player_board

        # 빨강색일 경우
        if board[new_y][new_x] == 1:
            new_player_board = list()
            is_k = False
            for _p in player_board[y][x][::-1]:
                if not is_k:
                    player_board[new_y][new_x].append(_p)
                    player[_p] = [new_y, new_x, d]
                    if _p == _k:
                        is_k = True
                else:
                    new_player_board.append(_p)
            new_player_board.reverse()
            player_board[y][x] = new_player_board

            # 파랑색 또는 벽일 경우
        if board[new_y][new_x] == 2 or not(0 <= new_x < N) or not(0 <= new_y < N):
            # 방향 뒤집음
            if d == 0 or d == 2:
                new_d = d + 1
            else:
                new_d = d - 1
            new_new_x, new_new_y = x + dx[new_d], y + dy[new_d]
            # 새로 간 곳이 파랑이거나 벽일 경우
            if board[new_new_y][new_new_x] == 2 or not(0 <= new_new_y < N) or not(0 <= new_new_x < N):
                player[_p] = [y, x, new_d]
            else:
                # 새로 간곳이 흰색일 경우
                player_board[_p] = []

