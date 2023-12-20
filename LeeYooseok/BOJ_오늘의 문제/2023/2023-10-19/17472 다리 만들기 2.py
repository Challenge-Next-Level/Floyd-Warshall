from collections import deque

# 한 다리의 방향이 중간에 바뀌면 안된다. 또, 다리의 길이는 2 이상이어야 한다.

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 섬에 index 부여
visited = [[False for _ in range(M)] for _ in range(N)]
idx = 1


def dfs(s_x, s_y):
    stack = list()
    stack.append([s_x, s_y])
    visited[s_y][s_x] = True
    board[s_y][s_x] = idx

    while stack:
        now_x, now_y = stack.pop()

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < M) or not (0 <= new_y < N):
                continue

            if board[new_y][new_x] == 0:
                continue

            if visited[new_y][new_x]:
                continue

            stack.append([new_x, new_y])
            visited[new_y][new_x] = True
            board[new_y][new_x] = idx


for _y in range(N):
    for _x in range(M):
        if not visited[_y][_x] and board[_y][_x] == 1:
            dfs(_x, _y)
            idx += 1

# 각 섬의 점에서 상하좌우로 움직이며 섬을 이어주는 간선을 모두 구한다.
edge = set()


def getDist(x, y, now_idx):
    queue = deque()

    for i in range(4):
        queue.append([x, y, 0, i])

    while queue:
        now_x, now_y, cnt, dir = queue.popleft()

        if board[now_y][now_x] != 0 and board[now_y][now_x] != now_idx:
            # 다리의 길이가 2 이상이어야 한다.
            if cnt > 2:
                # cost, start_node, end_node
                edge.add((cnt - 1, now_idx, board[now_y][now_x]))
            continue

        new_x, new_y = now_x + dx[dir], now_y + dy[dir]

        if not (0 <= new_x < M) or not (0 <= new_y < N):
            continue

        if visited[new_y][new_x]:
            continue

        if board[new_y][new_x] == now_idx:
            continue

        queue.append([new_x, new_y, cnt + 1, dir])


for _y in range(N):
    for _x in range(M):
        if board[_y][_x] != 0:
            visited = [[False for _ in range(M)] for _ in range(N)]
            getDist(_x, _y, board[_y][_x])

edge = list(edge)
# 거리가 짧은 순 으로 정렬
edge.sort()


def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


parent = [i for i in range(idx)]

result = 0

num = 0  # 연결한 섬의 개수
for cost, a, b in edge:
    if find(parent, a) != find(parent, b):
        num += 1
        union(parent, a, b)
        result += cost

if result == 0 or num != idx - 2:  # 연결하지 못함
    print(-1)
else:
    print(result)
