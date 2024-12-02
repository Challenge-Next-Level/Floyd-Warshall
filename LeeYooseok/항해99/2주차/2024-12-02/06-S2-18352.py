import sys

input = sys.stdin.readline

from collections import defaultdict, deque

N, M, K, X = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

visited = [False for _ in range(N + 1)]
queue = deque(list())

queue.append([X, 0])
visited[X] = True

answer = list()
while queue:
    now_node, move_cnt = queue.popleft()
    if move_cnt == K:
        answer.append(now_node)

    for next_node in graph[now_node]:
        if visited[next_node]:
            continue

        visited[next_node] = True
        queue.append([next_node, move_cnt + 1])

if answer:
    print("\n".join(list(map(str, sorted(answer)))))
else:
    print(-1)