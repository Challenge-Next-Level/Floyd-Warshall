T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    num_board = [list(map(int, input().split())) for _ in range(N)]
    answer_list = [[] for _ in range(2)] # 각 행의 합, 각 열의 합

    # 각 행의 합
    for i in range(N):
        answer_list[0].append(sum(num_board[i]))
    # 각 열의 합
    for i in range(N):
        answer_list[1].append(sum(num_board[m][i] for m in range(N)))

    for _ in range(M):
        r1, c1, r2, c2, v = map(int, input().split())

        # 각 행의 합 증가
        for r in range(r1 - 1, r2):
            answer_list[0][r] += (c2 - c1 + 1) * v

        # 각 열의 합 증가
        for c in range(c1 - 1, c2):
            answer_list[1][c] += (r2 - r1 + 1) * v

    for i in range(2):
        # 리스트 ' '로 연결
        print(*answer_list[i])
