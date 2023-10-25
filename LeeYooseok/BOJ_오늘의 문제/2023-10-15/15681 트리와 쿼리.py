import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, R, Q = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

# 초기화, 리프 노드의 서브트리 개수 -> 1개
dp = [0 for _ in range(N + 1)]

def dfs(node):
    dp[node] = 1
    # node 와 인접한 노드를 방문한다.
    for next_node in graph[node]:
        # 이미 방문한 곳은 가지 않도록 한다.
        if dp[next_node]:
            continue
        # 리프 노드부터 탐색하여, 각 노드의 서브 트리 개수를 확인한다.
        dp[node] += dfs(next_node)
    return dp[node]


dfs(R)

for _ in range(Q):
    U = int(input())
    print(dp[U])
