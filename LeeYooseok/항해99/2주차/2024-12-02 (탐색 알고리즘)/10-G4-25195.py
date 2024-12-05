import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

# if not graph[node] -> node 는 끝 점 -> 이동 종료

# 방문 할 수 있는 지에 대한 여부 -> 방문 못하는 점이면, 사전에 방문 처리를 해준다.
visited = [False for _ in range(N + 1)]
S = int(input())
S_list = list(map(int, input().split()))
for s in S_list:
    visited[s] = True

stack = list()

start_node = 1
if not visited[start_node]:
    stack.append(start_node)
    visited[start_node] = True

answer = "Yes"
while stack:
    now_node = stack.pop()

    if not graph[now_node]:
        answer = "yes"
        break

    for next_node in graph[now_node]:
        if visited[next_node]:
            continue

        visited[next_node] = True
        stack.append(next_node)

print(answer)