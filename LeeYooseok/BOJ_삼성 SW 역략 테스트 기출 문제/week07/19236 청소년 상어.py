# x - 행 번호, y - 열 번호
# 한 칸에는 한 마리의 물고기, 번호 : 1 ~ 16
# 방향 : 상하좌우, 대각선 1 ~ 8
# 0,0 에서 시작
import copy

result = 0

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

# 물고기 번호만 입력
board = list()
# 방향 , 좌표(x, y) - 죽으면 방향 -1 로 바꿈
fish_list = [[0, 0, 0] for _ in range(17)]
for j in range(4):
    _input = list(map(int, input().split()))
    temp = list()
    for i in range(0, 8, 2):
        temp.append(_input[i])
        fish_list[_input[i]] = [_input[i + 1] - 1, i // 2, j]
    board.append(temp)


# shark - [방향, x 좌표, y 좌표]
def dfs(_board, shark, size, _fish_list):
    global result
    # shark 의 위치에 있는 물고기 잡아 먹음
    size += _board[shark[2]][shark[1]]
    result = max(size, result)
    # 먹을 물고기 번호
    eat_fish = _board[shark[2]][shark[1]]
    # 물고기 리스트에서 해당 물고기 먹음
    _fish_list[eat_fish] = [-1, 0, 0]
    # 보드판에서 지움
    _board[shark[2]][shark[1]] = 0

    # 물고기 이동
    for i in range(1, 17):
        # 물고기 이동 방향
        fish_d = _fish_list[i][0]

        # 물고기 먹혔으면 다음 물고기
        if fish_d == -1:
            continue

        # 현재 물고기 위치
        fish_x, fish_y = _fish_list[i][1], _fish_list[i][2]

        # 다음 물고기 위치
        fish_new_x, fish_new_y = fish_x + dx[fish_d], fish_y + dy[fish_d]
        # 이동할 수 있을 때 까지 반시계 방향으로 회전
        while not (0 <= fish_new_x < 4) or not (0 <= fish_new_y < 4) or ([fish_new_x, fish_new_y] == shark[1:]):
            fish_d = (fish_d + 1) % 8
            fish_new_x, fish_new_y = fish_x + dx[fish_d], fish_y + dy[fish_d]

        # 이동하는 곳의 물고기 번호
        fish_num = _board[fish_new_y][fish_new_x]

        # 물고기가 있다면
        if fish_num > 0:
            # 방향, x, y 좌표
            _fish_list[i] = [fish_d, fish_new_x, fish_new_y]
            _fish_list[fish_num] = [_fish_list[fish_num][0], fish_x, fish_y]
            _board[fish_new_y][fish_new_x], _board[fish_y][fish_x] = i, fish_num
        # 빈 곳으로 이동
        else:
            _fish_list[i] = [fish_d, fish_new_x, fish_new_y]
            _board[fish_new_y][fish_new_x], _board[fish_y][fish_x] = i, fish_num

    # 상어 이동
    shark_d, shark_x, shark_y = shark
    new_shark_x, new_shark_y = shark_x + dx[shark_d], shark_y + dy[shark_d]
    for _ in range(4):
        if 0 <= new_shark_x < 4 and 0 <= new_shark_y < 4 and _board[new_shark_y][new_shark_x] != 0:
            new_shark = [_fish_list[_board[new_shark_y][new_shark_x]][0], new_shark_x, new_shark_y]
            dfs(copy.deepcopy(_board), new_shark, size, copy.deepcopy(_fish_list))
        new_shark_x, new_shark_y = new_shark_x + dx[shark_d], new_shark_y + dy[shark_d]


dfs(board, [fish_list[board[0][0]][0], 0, 0], 0, fish_list)
print(result)
