from collections import defaultdict
from collections import deque

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(idx):
    _cnt = 1
    visited = [False for _ in range(N + 1)]
    visited[idx] = True

    que = deque()
    que.append(idx)

    while que:
        now = que.popleft()
        for v in graph[now]:
            if not visited[v]:
                que.append(v)
                visited[v] = True
                _cnt += 1

    return _cnt


answer = list()
max_cnt = 0

for i in range(1, N + 1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    answer.append([i, cnt])

for i, cnt in answer:
    if cnt == max_cnt:
        print(i, end=' ')
