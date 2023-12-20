# 트리로 이루어진 도시들 사이에서 최적의 위치에 소방서가 건설되기 위해서는 트리의 지름을 구하고 그 중간의 위치에 소방서를 지어야한다.
# 트리의 지름이 딱 절반으로 나누어지면 몫을 출력하고 절반으로 나누었을때 나머지가 있다면 몫에 +1을 해준다.

# 트리의 지름을 구하기 위해서 임의의 한 지점에서 가장 먼 지점을 구하고 그 지점에서 가장 먼 지점까지의 거리를 구하면 트리의 지름을 구할 수 있다.

import sys
from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = sys.maxsize


def dfs(_n):
    global answer
    que = deque([[_n, 0]])  # node, 거리
    visited = [-1 for _ in range(N + 1)]
    visited[_n] = 0

    while que:
        node, dist = que.pop()
        for g in graph[node]:
            if visited[g] != -1:
                if visited[g] > dist + 1:
                    visited[g] = dist + 1
                    que.append([g, dist + 1])
            else:
                visited[g] = dist + 1
                que.append([g, dist + 1])

    # _n 에서 가장 먼 지점의 노드와 거리를 리턴한다.
    max_dist = max(visited)
    return visited.index(max_dist), max_dist


max_node, max_dist = dfs(1)
zirm_node, zirm_dist = dfs(max_node)
print((zirm_dist + 1) // 2)
