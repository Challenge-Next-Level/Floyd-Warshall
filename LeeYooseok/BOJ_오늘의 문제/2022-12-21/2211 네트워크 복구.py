from collections import defaultdict, deque

N, M = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

def bfs(n):
    weight_list = [100000000 for _ in range(N + 1)]
    chk = [0 for _ in range(N+1)]
    que = deque([[n, 0]])

    while que:
        now_node, now_weight = que.popleft()

        for next_node, weight in graph[now_node]:
            next_weight = now_weight + weight

            if weight_list[next_node] > next_weight:
                que.append([next_node, next_weight])
                weight_list[next_node] = next_weight
                chk[next_node] = now_node

    return chk

answer = bfs(1)
print(N - 1)
for idx in range(2, N+1):
    print(idx, answer[idx])
