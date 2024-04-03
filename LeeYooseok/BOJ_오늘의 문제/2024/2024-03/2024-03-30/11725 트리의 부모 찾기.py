import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())

graph = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

parent_list = [0 for _ in range(N + 1)]


def bfs(node):
    queue = deque([node])

    while queue:
        now_node = queue.popleft()

        for next_node in graph[now_node]:
            if parent_list[next_node] == 0:
                parent_list[next_node] = now_node
                queue.append(next_node)


parent_list[1] = -1
bfs(1)
for parent in parent_list[2:]:
    print(parent)
