# 시간 초과?

# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
# 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다.
import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

board = list()
virus_list = list()
b = 0

for j in range(N):
    temp = list(map(int, input().split()))
    for i in range(N):
        if temp[i] == 2:
            virus_list.append([j, i])
        if temp[i] != 1:
            b += 1
    board.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

try_list = list(combinations(virus_list, M))

# 모든 바이러스 활성하는데 최소 시간
result = sys.maxsize

for _try in try_list:
    visited = [[0] * N for _ in range(N)]
    cnt = [[-1] * N for _ in range(N)]

    queue = deque()
    for y, x in _try:
        visited[y][x] = 1
        cnt[y][x] = 0
        # x, y 위치
        queue.append([x, y])

    while queue:
        now_x, now_y = queue.popleft()
        for i in range(4):
            new_x, new_y = now_x + dx[i], now_y + dy[i]

            if not(0 <= new_x < N) or not(0 <= new_y < N):
                continue

            if visited[new_y][new_x] == 1:
                continue

            if board[new_y][new_x] == 1:
                continue

            visited[new_y][new_x] = 1
            queue.append([new_x, new_y])
            cnt[new_y][new_x] = cnt[now_y][now_x] + 1

    # 바이러스가 퍼진 곳 확인
    total_virus = 0
    for _visited in visited:
        total_virus += _visited.count(1)

    # 모든곳으로 다 퍼졌으면
    if b == total_virus:
        # 현재 경우 다 퍼질때 까지의 시간 확인
        max_n = 0
        for j in range(N):
            for i in range(N):
                if board[j][i] != 1 and [j, i] not in virus_list:
                    max_n = max(max_n, cnt[j][i])

        # 다 퍼질때까지의 최소 시간 확인
        result = min(result, max_n)

if result == sys.maxsize:
    print(-1)
else:
    print(result)

