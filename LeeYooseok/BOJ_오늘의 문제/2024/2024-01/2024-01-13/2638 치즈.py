from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 공기 탐색
def air_bfs(_x, _y):
    q = deque()
    q.append([_x, _y])
    visited[_y][_x] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not(0 <= nx < M) or not(0 <= ny < N):
                continue

            # 다음 진행이 공기면(큐 추가, 방문처리)
            if visited[ny][nx] == 0 and board[ny][nx] == 0:
                q.append([nx, ny])
                visited[ny][nx] = 1
            # 다음 진행이 치즈면(방문정보 업데이트)
            elif board[ny][nx] == 1:
                visited[ny][nx] = visited[ny][nx] + 1


answer = 0
while True:
    visited = [[0 for _ in range(M)] for _ in range(N)]

    air_bfs(0, 0)
    # 탐색 한바퀴 끝나면 시간+1
    answer += 1

    # 두면이상 공기랑 닿으면, 빈칸 처리
    for _y in range(N):
        for _x in range(M):
            if visited[_y][_x] >= 2:
                board[_y][_x] = 0

    # 공기 카운트
    block_cnt = 0
    for _y in range(N):
        for _x in range(M):
            if board[_y][_x] == 0:
                block_cnt += 1
    # 탐색 한번 하고 난 그래프의 공기수가 배열의 크기랑 같으면 break
    if block_cnt == (N * M):
        break

print(answer)
