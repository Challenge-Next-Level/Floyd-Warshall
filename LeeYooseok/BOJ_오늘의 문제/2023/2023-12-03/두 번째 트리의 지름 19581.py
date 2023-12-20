from collections import defaultdict

N = int(input())

graph = defaultdict(list)

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


# 트리의 정점
# 1. DFS를 통해 임의의 정점(x)으로부터 가장 먼 정점(y)을 구한다.
# 2. DFS를 통해 구해진 (y)정점으로부터 가장 먼 정점(z)를 구한다.
# 3. (y) 정점과 (z) 정점을 잇는 경로가 트리의 지름이 된다.

def dfs(node, except_node=0):
    visited = [False for _ in range(N + 1)]
    visited[except_node] = True

    most_far_node = node
    most_far_distance = 0

    stack = [[node, 0]]
    visited[node] = True

    while stack:
        now_node, now_distance = stack.pop()

        for next_node, next_distance in graph[now_node]:
            if visited[next_node]:
                continue

            if now_distance + next_distance > most_far_distance:
                most_far_node = next_node
                most_far_distance = now_distance + next_distance

            visited[next_node] = True
            stack.append([next_node, now_distance + next_distance])

    return most_far_node, most_far_distance


# 트리의 지름
a_node, a_distance = dfs(1)
b_node, b_distance = dfs(a_node)

# b_node를 제외한 a_node에서 가장 먼 거리
a_node_except_b, a_distance_except_b = dfs(a_node, b_node)
# a_node를 제외한 b_node에서 가장 먼 거리
b_node_except_a, b_distance_except_a = dfs(b_node, a_node)

print(max(a_distance_except_b, b_distance_except_a))
