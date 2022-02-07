# 가장 큰 접근이 틀렸었다.
# 아파트를 탐색하는게 아니라 아파트가 아닌 곳을 탐색하면서 아파트의 외벽 갯수를 세는게 포인트다.

# 그리고 이때 배열의 바깥 부분만 dfs 탐색을 한다.
# 이유1: 바깥 부분만 dfs탐색을 해도 안의 배열 탐색 가능
# 이유2: 아파트로 둘러 쌓인 곳은 탐색 안하게 됨
#
# 이렇게 탐색을 하게 되면 계산 안되는 외벽이 있는데 따로 '추가 탐색'을 해야 한다.
import sys

W, H = list(map(int, sys.stdin.readline().split()))

building = [[] for _ in range(H)] # 아파트 여부 입력
for i in range(H):
    building[i] = list(map(int, sys.stdin.readline().split()))

odd_go = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, 0], [1, 1]] # 홀수번 째 라인에서 연결되는 경로
even_go = [[-1, -1], [-1, 0], [0, -1], [0, 1], [1, -1], [1, 0]] # 짝수번 째 라인에서 연결되는 경로
visit = [[0] * W for _ in range(H)]
window = 0


def calculate_window(y, x): # 인접 노드가 아파트라면 창문 +1
    for k in range(6):
        if y % 2 == 0:
            ny, nx = y + odd_go[k][0], x + odd_go[k][1]
        else:
            ny, nx = y + even_go[k][0], x + even_go[k][1]
        global window
        if 0 <= nx < W and 0 <= ny < H and building[ny][nx] == 1:
            window += 1


def calculate_additional_window(y, x): # 최외각 창문은 따로 계산을 한다.
    global window
    # 맨 오른쪽, 맨 왼쪽 창문 계산
    if y % 2 == 0: # 홀수 번째 줄
        if x == W - 1: # 맨 오른쪽
            window += 3
        elif x == 0: # 맨 왼쪽
            window += 1
    else: # 짝수 번째 줄
        if x == 0: # 맨 왼쪽
            window += 3
        elif x == W - 1: # 맨 오른쪽
            window += 1
    # 맨 위, 맨 아래 창문 계산
    if y == 0: # 맨 윗줄
        if x == W - 1: # 맨 오른쪽
            window += 1
        else: # 그 외
            window += 2
    elif y == H - 1: # 맨 아랫줄
        if x == 0: # 맨 왼쪽
            window += 1
        else: # 그 외
            window += 2
    return


def dfs(i, j):
    if visit[i][j] == 1:
        return
    if building[i][j] == 1:
        calculate_additional_window(i, j)
        return
    build = [[i, j]]
    while build:
        y, x = build.pop()
        if visit[y][x] == 1:
            continue
        visit[y][x] = 1
        calculate_window(y, x)
        for k in range(6):
            if y % 2 == 0:
                ny, nx = y + odd_go[k][0], x + odd_go[k][1]
            else:
                ny, nx = y + even_go[k][0], x + even_go[k][1]
            if 0 <= nx < W and 0 <= ny < H and building[ny][nx] == 0:
                build.append([ny, nx])
    return


# 최외각 배열 노드만 탐색을 한다.
for a in range(H):
    for b in range(W):
        if a == 0 or a == H - 1 or b == 0 or b == W - 1:
            dfs(a, b)
print(window)