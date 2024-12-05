from collections import deque

N, M, K, X = map(int, input().split())

# graph 표현을 위한 인접 리스트 활용
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

# 거리를 위한 리스트
distance_list = [0 for _ in range(N + 1)]
# 방문 처리를 위한 리스트
visited = [False for _ in range(N + 1)]

# queue 를 이용하여 BFS 알고리즘 사용
queue = deque(list())
queue.append(X)

# BFS 구현
while queue:
    now_node = queue.popleft()
    visited[now_node] = True

    for next_node in graph[now_node]:
        if visited[next_node]:
            continue

        queue.append(next_node)
        visited[next_node] = True
        distance_list[next_node] = distance_list[now_node] + 1

# 정답 체크
check = False
for i in range(1, N + 1):
    if distance_list[i] == K:
        print(i)
        check = True

if not check:
    print(-1)