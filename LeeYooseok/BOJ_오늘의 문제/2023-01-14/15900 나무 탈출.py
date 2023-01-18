from collections import defaultdict, deque

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance_list = [-1 for _ in range(N + 1)]  # 1번 부터 N번 노드 까지


def dfs(node):
    dq = deque()
    dq.append([node, 0])
    distance_list[node] = 0

    while dq:
        now_node, now_distance = dq.popleft()

        for next_node in graph[now_node]:
            # visited 처리
            if distance_list[next_node] != -1:
                continue

            distance_list[next_node] = now_distance + 1
            dq.append([next_node, now_distance + 1])

dfs(1)

total_distance = 0
# 리프 노드를 찾음 - 2 번 노드부터, graph[i] 의 길이가 1이면 리프 노드임
for i in range(2, N + 1):
    if len(graph[i]) == 1:
        total_distance += distance_list[i]

if total_distance % 2 == 0:
    print("No")
else:
    print("Yes")