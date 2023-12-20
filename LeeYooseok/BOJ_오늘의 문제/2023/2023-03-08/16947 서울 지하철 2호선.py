import sys
from collections import deque

sys.setrecursionlimit(100000)

N = int(input())
graph = [[] for _ in range(N)]

# 순환역을 표시하는 것
cycle_station = [False] * N

# 정답 변수
answer = [-1] * N

# 역 구간 정보 입력받기
for _ in range(N):
    A, B = map(int, input().split())
    graph[A - 1].append(B - 1)
    graph[B - 1].append(A - 1)


# 순환선 확인 - dfs
def recursion_check_circulation(start, idx, cnt):
    # 종료 조건 : 방문한 곳 이 2곳 이상이고, 현재 역이 시작역으로 돌아온다면
    if cnt >= 2 and start == idx:
        cycle_station[start] = True
        return

    # 현재 역 방문 표시
    visited[idx] = True

    # 다음 방문
    for next_idx in graph[idx]:
        if not visited[next_idx]:
            recursion_check_circulation(start, next_idx, cnt + 1)
        elif next_idx == start and cnt >= 2:
            recursion_check_circulation(start, next_idx, cnt)

for i in range(N):
    # 방문 여부 표시 리스트
    visited = [False] * N
    # 순환선 탐색
    recursion_check_circulation(i, i, 0)

# 역 거리 확인 - bfs
def check_distance():
    que = deque()
    for n in range(N):
        if cycle_station[n]:  # 순환역
            answer[n] = 0
            que.append(n)

    while que:
        now = que.popleft()
        for next_idx in graph[now]:
            if answer[next_idx] == -1:  # 순환역이 아니라면
                que.append(next_idx)
                # 이동거리 구하기
                answer[next_idx] = answer[now] + 1


check_distance()
# 출력
print(*answer)
