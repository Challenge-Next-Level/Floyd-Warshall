# 독립 집합 : 모든 정점쌍이 서로 인접하지 않으면
# 부모가 독립 집합에 포함되어 있는 경우, 부모가 독립 집합에 포함되어 있지 않은 경우

from collections import defaultdict

n = int(input())
weight_list = [0] + list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    if a < b:
        graph[a].append(b)
    else:
        graph[b].append(a)

# dp[n][0] = n을 루트로 하는 서브트리의 최대 독립집합 크기, n 포함 X
# dp[n][1] = n을 루트로 하는 서브트리의 최대 독립집합 크기, n 포함 O
dp = [[0, 0] for _ in range(n + 1)]

# path[n][0] = n을 루트로 하는 서브트리의 독립집합 원소, n 포함 X
# path[n][1] = n을 루트로 하는 서브트리의 독립집합 원소, n 포함 O
path = [[[] for _ in range(2)] for _ in range(n + 1)]

visited = [False] * (n + 1)
def dfs(node):
    visited[node] = True
    dp[node][1] += weight_list[node]
    path[node][1].append(node)

    for next_node in graph[node]:
        if not visited[next_node]:
            result = dfs(next_node)

            dp[node][0] += max(dp[next_node][0], dp[next_node][1])
            dp[node][1] += dp[next_node][0] # node 를 포함하려면, next_node는 포함 X

            if dp[next_node][0] > dp[next_node][1]:
                path[node][0] += result[0]
            else:
                path[node][0] += result[1]
            path[node][1] += result[0]

    return path[node]

p = dfs(1)
if dp[1][0] > dp[1][1]:
    print(dp[1][0])
    p[0].sort()
    print(*p[0])
else:
    print(dp[1][1])
    p[1].sort()
    print(*p[1])