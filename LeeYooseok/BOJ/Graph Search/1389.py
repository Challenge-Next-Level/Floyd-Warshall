n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())

    if e not in graph[s]:
        graph[s].append(e)
    if s not in graph[e]:
        graph[e].append(s)


def bfs(x) -> int:
    ans = 0
    visited = [0] * (n + 1)

    temp = list()
    temp.append([x, 0])  # 현재 노드 및 현재 노드 까지 오는데 걸린 수

    while temp:
        now, path = temp.pop(0) # bfs 로 문제 풀어야 함 ? -> 앞에꺼 먼저 꺼내야 함 -> 트리 구조 생각해 보면 될듯?
        if visited[now] == 1:
            continue
        visited[now] = 1

        ans += path

        for j in range(len(graph[now])):
            temp.append([graph[now][j], path + 1])

    return ans


result = list()

for i in range(1, n + 1):
    result.append(bfs(i))

min_val = min(result)
print(result.index(min_val)+1)
