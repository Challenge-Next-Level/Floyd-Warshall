from collections import defaultdict

import sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = defaultdict(list)
node_list = list(map(int, input().split()))
for node_idx in range(N - 1):
    graph[node_list[node_idx]].append(node_idx + 2)

skill_list = [0]
skill_list.extend(list(map(int, input().split())))

# 0 : 부모 노드와 시너지 형성 하지 않는 경우
# 1 : 부모 노드와 시너지 형성하는 경우
dp = [[-1, -1] for _ in range(N + 1)]


def dfs(now, isBind):
    if dp[now][isBind] != -1:
        return dp[now][isBind]

    dp[now][isBind] = 0

    # 현재 노드를 자식 노드와 연결하지 않는경우
    for next_node in graph[now]:
        # 자식 노드의 dp 값들을 모두 다 더해준다.
        dp[now][isBind] += dfs(next_node, 0)

    # 현재 노드가 부모 노드와 시너지를 형성하지 않은 경우
    if isBind == 0:
        value = dp[now][isBind]
        # 자식 노드와 시너지 형성 고려
        for next_node in graph[now]:
            num = value - dfs(next_node, 0)  # next_node 와 시너지를 맺으면 위에서 더한 자식의 dp 값을 우선 뺀다.
            num += dfs(next_node, 1) + (skill_list[now] * skill_list[next_node])  # 자식 노드와 시너지 형성값을 더한다.
            dp[now][isBind] = max(dp[now][isBind], num)

    return dp[now][isBind]


# 루트 노드는 부모가 없기 때문에, isBind 는 0으로 고정
print(dfs(1, 0))
