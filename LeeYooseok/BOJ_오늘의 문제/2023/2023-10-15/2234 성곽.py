from collections import deque

N, M = map(int, input().split())

# wall information
def wall(info):
    return format(info, 'b').zfill(4)

# 서, 북, 동, 남
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

board = [list(map(int, input().split())) for _ in range(M)]

visited = [[False for _ in range(N)]  for _ in range(M)]

def get_size(s_x, s_y):
    dq = deque([[s_x, s_y]])
    visited[s_y][s_x] = True

    size = 0

    while dq:
        now_x, now_y = dq.popleft()
        size += 1
        able_dir = wall(board[now_y][now_x])[::-1]

        for i in range(4):
            if able_dir[i] == '0':
                next_x, next_y = now_x + dx[i], now_y + dy[i]

                if not(0 <= next_x < N) or not(0 <= next_y < M):
                    continue

                if visited[next_y][next_x]:
                   continue

                visited[next_y][next_x] = True
                dq.append([next_x, next_y])

    return size

# 벽을 제거하지 않고 얻을 수 있는 방 개수, 가장 큰 방 넓이
max_size = -1
room_count = 0
for _y in range(M):
    for _x in range(N):
        if not visited[_y][_x]:
            max_size = max(get_size(_x, _y), max_size)
            room_count += 1

# 벽을 제거한 후, 얻을 수 있는 가장 큰 방의 넓이
after_max_size = -1
for _y in range(M):
    for _x in range(N):
        able_dir = wall(board[_y][_x])[::-1]
        for i in range(4):
            # i 방향에 벽이 있다면,
            if able_dir[i] == "1":
                # 벽을 허물고, 탐색 시작
                visited = [[False for _ in range(N)] for _ in range(M)]
                board[_y][_x] -= 2 ** i
                after_max_size = max(get_size(_x, _y), after_max_size)
                board[_y][_x] += 2 ** i

print(room_count)
print(max_size)
print(after_max_size)