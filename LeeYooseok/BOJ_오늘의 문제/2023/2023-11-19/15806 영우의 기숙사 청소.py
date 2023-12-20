from collections import deque

N, M, K, t = map(int, input().split())

dust_loc = deque([])
visited = [[[False] * 2 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    M_x, M_y = map(int, input().split())
    dust_loc.append([M_x - 1, M_y - 1, 0])
    visited[M_y - 1][M_x - 1][0] = True

check = list()
for _ in range(K):
    K_x, K_y = map(int, input().split())
    check.append([K_x - 1, K_y - 1])
# 8군데 증식
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

while dust_loc:

    now_x, now_y, now_t = dust_loc.popleft()
    if now_t >= t:
        continue
    # 바이러스가 퍼질 수 있는지 확인
    v_c = False

    for i in range(8):
        new_x, new_y = now_x + dx[i], now_y + dy[i]

        if not (0 <= new_x < N) or not (0 <= new_y < N):
            continue

        # 홀수, 짝수 번째에 해당 구역을 방문했으면,
        if visited[new_y][new_x][(now_t + 1) % 2]:
            continue

        v_c = True
        visited[new_y][new_x][(now_t + 1) % 2] = True
        dust_loc.append([new_x, new_y, now_t + 1])

    if not v_c:
        visited[now_y][now_x][now_t % 2] = False

c = t % 2
for cx, cy in check:
    if visited[cy][cx][c]:
        print("YES")
        exit(0)

print("NO")
