import sys

input = sys.stdin.readline

from collections import defaultdict

N, M, R = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# 인접 정점은 오름차순으로 방문한다. -> stack 을 사용하기 때문에 -> stack 에 들어간 순의 역순으로 탐색을 시작한다.
for node in graph:
    graph[node].sort(reverse=True)

visited = [False for _ in range(N + 1)]

stack = list()
stack.append(R)

now_order = 0
answer = [0 for _ in range(N + 1)]

while stack:
    now_node = stack.pop()
    if visited[now_node]:
        continue

    visited[now_node] = True
    now_order += 1
    answer[now_node] = now_order

    for next_node in graph[now_node]:
        if visited[next_node]:
            continue

        stack.append(next_node)

print("\n".join(list(map(str, answer[1:]))))
