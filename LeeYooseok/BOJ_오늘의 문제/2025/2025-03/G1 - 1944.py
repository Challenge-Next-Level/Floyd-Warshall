from collections import deque

N, M = map(int, input().split())

board = list()
point_list = list()
for _y in range(N):
    x_board = list(input())
    for _x in range(N):
        if x_board[_x] == 'S' or x_board[_x] == 'K':
            x_board[_x] = len(point_list)
            point_list.append([_x, _y])
    board.append(x_board)

graph = list()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(idx):
    x, y = point_list[idx]
    visited = [[False for _ in range(N)] for _ in range(N)]

    queue = deque([[x, y, 0]])
    visited[y][x] = True

    while queue:
        now_x, now_y, cnt = queue.popleft()

        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not (0 <= new_x < N) or not (0 <= new_y < N):
                continue

            if visited[new_y][new_x]:
                continue

            if board[new_y][new_x] == '1':
                continue

            queue.append([new_x, new_y, cnt + 1])
            visited[new_y][new_x] = True
            if board[new_y][new_x] != '0':
                graph.append([cnt + 1, idx, board[new_y][new_x]])


for i in range(len(point_list)):
    bfs(i)

# MST (Kruskal Algorithm)
parent = [i for i in range(len(point_list))]


def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True


graph.sort()
ans = 0
num = 0
for dist, s, e in graph:
    if union(s, e):
        ans += dist
        num += 1
    if num >= len(point_list) - 1:
        break

print(ans if num == len(point_list) - 1 else -1)
