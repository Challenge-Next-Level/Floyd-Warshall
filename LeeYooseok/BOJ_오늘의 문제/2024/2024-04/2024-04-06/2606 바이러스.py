import sys
from collections import defaultdict, deque
input = sys.stdin.readline

C = int(input())

graph = defaultdict(list)

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(C + 1)]

queue = deque([1])
visited[1] = True
answer = 0
while queue:
    now_node = queue.popleft()
    answer += 1

    for next_node in graph[now_node]:
        if visited[next_node]:
            continue

        visited[next_node] = True
        queue.append(next_node)

print(answer - 1)