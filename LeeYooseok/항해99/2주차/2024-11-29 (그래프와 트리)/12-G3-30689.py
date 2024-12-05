import sys

input = sys.stdin.readline

N, M = map(int, input().split())

direction = {
    "U": [0, -1],
    "D": [0, 1],
    "L": [-1, 0],
    "R": [1, 0]
}

board = [list(input()) for _ in range(N)]

cost = [list(map(int, input().split())) for _ in range(N)]

answer = 0
visited = [[False for _ in range(M)] for _ in range(N)]


def DFS(x, y):
    global answer
    # 현재 탐색에서 방문한 위치 - cycle 판별을 위해
    now_visited = set()  # 시간 초과 때문에, 방문 처리는 set
    now_visited_list = list()  # cycel 시작 위치 확인은 리스트
    # Stack for DFS
    stack = [[x, y]]
    # 현재 탐색에서 방문한 위치에 시작 위치 넣어줌
    now_visited.add((x, y))
    now_visited_list.append([x, y])
    # 만약, cycle 이 생긴다면, 점프대를 설치할 비용 -> min 으로 업데이트함
    cost_list = [cost[y][x]]
    cycle_start_idx = 0

    # 초기 상태 : 탈출 실패
    exit_able = False
    # stack 이 비어있으면, 반복 종료
    while stack:
        # 현재 위치 x, y
        now_x, now_y = stack.pop()
        # 현재 위치에서 움직일 방향
        now_dir = board[now_y][now_x]

        # 다음 위치
        next_x, next_y = now_x + direction[now_dir][0], now_y + direction[now_dir][1]

        # 탈출 가능 - 범위를 벗어나거나, 이전에 방문(탈출)한 기록이 있으면
        if not (0 <= next_x < M) or not (0 <= next_y < N) or visited[next_y][next_x]:
            # 탈출 가능 및 반복문 종료
            exit_able = True
            break

        # cycle 존재한다면
        if (next_x, next_y) in now_visited:
            cycle_start_idx = now_visited_list.index([next_x, next_y])
            # 반복문 종료
            break

        # DFS 탐색 진행
        # 현재 탐색에서 방문한 위치에 다음 위치 넣어줌
        now_visited.add((next_x, next_y))
        now_visited_list.append([next_x, next_y])
        # cycle 이 생긴다면, 점프대를 설치할 때 쓰는 비용 업데이트
        cost_list.append(cost[next_y][next_x])
        # stack 에 다음 위치 넣어줌
        stack.append([next_x, next_y])

    # 탈출에 실패하면, 정답에 현재 점프대 최소 설치 비용 더해줌
    if not exit_able:
        answer += min(cost_list[cycle_start_idx:])

    # 현재 탐색에서 방문한 위치 -> 전체 방문 처리
    for visited_x, visited_y in now_visited:
        visited[visited_y][visited_x] = True


# 모든 위치에 대해서 DFS 탐색
for _y in range(N):
    for _x in range(M):
        # 방문한 기록이 없으면
        if not visited[_y][_x]:
            DFS(_x, _y)

print(answer)
