N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 상, 하, 좌, 우
dir_x = [0, 0, -1, 1]
dir_y = [-1, 1, 0, 0]

dir_list = [[[0, 0], [0, 0], [1, 0], [0, 1]], [[0, 0], [0, 0], [-1, 0], [0, 1]], [[0, 0], [0, 0], [1, 0], [0, -1]],
            [[0, 0], [0, 0], [-1, 0], [0, -1]]]
dir_dict = {0: [2, 3], 1: [0, 1], 2: [1, 3], 3: [0, 2]}

visited = [[False for _ in range(M)] for _ in range(N)]

answer = 0


def solve(_sum, x, y):
    global answer

    # 마지막 위치에 도달했다면,
    if x == 0 and y == N:
        answer = max(_sum, answer)
        return

    # 부메랑 제작 가능 여부 확인
    if visited[y][x]:
        check = [False for _ in range(4)]
    else:
        check = [True for _ in range(4)]  # ⌜⌝⌞⌟ -> d 번째 부메랑 제작 가능
        for d in range(4):
            if 0 <= x + dir_x[d] < M and 0 <= y + dir_y[d] < N:
                if visited[y + dir_y[d]][x + dir_x[d]]:
                    for _d in dir_dict[d]:
                        check[_d] = False
            else:
                for _d in dir_dict[d]:
                    check[_d] = False

    # 다음 무엇부터 확인할 지
    if x == M - 1:
        n_x, n_y = 0, y + 1
    else:
        n_x, n_y = x + 1, y

    # 부메랑 안만드는 경우
    solve(_sum, n_x, n_y)

    # 부메랑 만드는 경우
    for i in range(4):
        if check[i]:  # True 여야지 해당 부메랑 제작 가능
            temp_sum = _sum
            for dx, dy in dir_list[i]:
                visited[y + dy][x + dx] = True
                temp_sum += board[y + dy][x + dx]

            solve(temp_sum, n_x, n_y)

            for dx, dy in dir_list[i]:
                visited[y + dy][x + dx] = False



if N < 2 or M < 2:
    print(0)
    exit()

for i_y in range(N):
    for i_x in range(M):
        solve(0, i_x, i_y)

print(answer)
