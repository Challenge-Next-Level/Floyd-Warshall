import sys
from collections import deque


def solution(grid, k):
    n = len(grid)
    m = len(grid[0])
    # 필요한 최소 야영 횟수
    answer = sys.maxsize

    # 상, 하, 좌, 우 - 인접한 평지 혹은 숲으로 만 이동
    # . 평지, F 숲, # 강
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    # 행, 열 위치, now root - 지금까지 온 경로 (숲인지 평지인지 저장)
    queue = deque([[0, 0, ['.']]])
    root_list = list()
    while queue:
        now_y, now_x, now_root = queue.popleft()
        if now_y == n - 1 and now_x == m - 1:
            root_list.append(now_root)
            continue

        for d in range(4):
            new_y, new_x = now_y + dy[d], now_x + dx[d]

            if not (0 <= new_y < n) or not (0 <= new_x < m):
                continue

            # 강이면 이동 불가능
            if grid[new_y][new_x] == '#':
                continue

            # 방문 했던 곳이라면 그리고 도착 지점이 아니라면
            if visited[new_y][new_x] == 1 and not (new_y == n - 1 and new_x == m - 1):
                continue

            visited[new_y][new_x] = 1
            queue.append([new_y, new_x, now_root + [grid[new_y][new_x]]])  # 마지막에 경로 추가 (평지인지 숲인지)

    # 하루에 최대 k칸 이동 가능
    # 야영은 평지에서만 가능
    for root in root_list:
        cnt_sleep = 0
        now_k = k
        # 시작 ~ 끝 - 1 까지 반복
        for r in range(len(root[1:])):
            # 평지이면
            if root[r] == '.':
                # 야영 결정 - 앞으로 남은 now_k칸에 . 이 없으면 또는 현재 체력이 0이면 야영을 한다.
                if '.' not in root[r + 1:r + now_k + 1] or now_k == 0:
                    cnt_sleep += 1
                    now_k = k
                # 아니면 앞으로 한칸 나아간다. - 체력 -1
                else:
                    now_k -= 1
            # 숲이면 앞으로 한칸 나아간다. - 체력 -1
            else:
                now_k -= 1
        # 최소 야영 횟수 확인
        answer = min(answer, cnt_sleep)
    return answer


# print(solution(["..FF", "###F", "###."], 4))
# print(solution(["..FF", "###F", "###."], 5))
print(solution([".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.",
     ".#...####F", "...#......"], 6))
