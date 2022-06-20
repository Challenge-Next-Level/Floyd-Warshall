import sys

input = sys.stdin.readline

# N x N 땅의 크기, M개의 나무를 심음, K년이 지난 후 살아있는 나무의 개수를 구하라
N, M, K = map(int, input().split())

# A 배열 - 겨울에 추가되는 양분의 양
A_board = [list(map(int, input().split())) for _ in range(N)]

# 현재 남아있는 양분
eat_board = [[5] * N for _ in range(N)]

tree_board = [[[] for _ in range(N)] for _ in range(N)]

# 현재 심은 나무의 정보
for _ in range(M):
    # 위치 (x, y), 나무의 나이
    x, y, z = map(int, input().split())
    tree_board[x - 1][y - 1].append(z)

for _ in range(K):
    # 번식 나무
    growing_tree = []
    # 봄 - 양분을 먹음
    for i in range(N):
        for j in range(N):
            if tree_board[j][i]:
                tree_board[j][i].sort()
                length = len(tree_board[j][i])

                for t in range(length):
                    if eat_board[j][i] >= tree_board[j][i][t]:
                        eat_board[j][i] -= tree_board[j][i][t]
                        tree_board[j][i][t] += 1
                        if tree_board[j][i][t] % 5 == 0:
                            growing_tree.append([j, i, t])
                    else:
                        for idx in range(t, length):
                            eat_board[j][i] += (tree_board[j][i].pop() // 2)
                        break

    # 가을 - 나무 번식
    for g_tree in growing_tree:
        now_x, now_y = g_tree[1], g_tree[0]
        for dx, dy in [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]:
            # 범위 벗어나는지 확인
            new_x, new_y = now_x + dx, now_y + dy

            if not (0 <= new_x < N) or not (0 <= new_y < N):
                continue

            tree_board[new_y][new_x].append(1)

    # 겨울 - 양분 추가
    for i in range(N):
        for j in range(N):
            eat_board[j][i] += A_board[j][i]

result = 0
for t in tree_board:
    for s in t:
        result += len(s)

print(result)
