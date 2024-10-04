from collections import deque


def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])  # [node, 1에서 부터 거리]
    while q:
        value = q.popleft()  # 제일 첫번째 원소 반환
        v = value[0]  # 첫번째 node
        count = value[1]  # 1에서 부터 첫번째 노드 까지의 거리
        if visited[v] == -1:  # 방문 안했을 시
            visited[v] = count  # count = 1에서 부터 이전 노드 까지의 거리
            count += 1
            for e in adj[v]:
                q.append([e, count])


def solution(n, edge):
    answer = 0

    adj = [[] for _ in range(n + 1)]
    for e in edge:
        src = e[0]
        dist = e[1]
        adj[src].append(dist)
        adj[dist].append(src)

    visited = [-1] * (n + 1)

    bfs(1, visited, adj)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer