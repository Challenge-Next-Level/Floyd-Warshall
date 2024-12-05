import sys

input = sys.stdin.readline

from collections import defaultdict

N = int(input())
graph = defaultdict(list)

# 묶음 리스트
bundle_list = list()


def DFS(node, parent):
    # 더 깊이가 깊은 노드 부터 탐색
    # 자식을 사용해서 타고타고 들어감

    # graph 가 변경되기 때문에, 뒤에서부터 탐색하고, 탐색하는 index 맞춰주어야 함
    now_idx = len(graph[node])
    while now_idx >= 1:
        now_idx -= 1
        while now_idx >= len(graph[node]):
            now_idx -= 1
        next_node = graph[node][now_idx]

        # 부모와, 리프 노드는 탐색 X
        if next_node == parent or len(graph[next_node]) == 1:
            continue

        if not DFS(next_node, node):
            return False

    # 자식이 나랑 끊었을 수도 있기 때문에 대수 다시 세야함
    parent_leaf = list()
    leaf_list = list()

    for next_node in graph[node]:
        if next_node == parent:
            continue

        # 현재 노드와 연결된 리프 노드
        if len(graph[next_node]) == 1:
            leaf_list.append(next_node)

        # 이중 진자?
        # next_node : 현재 노드와 연결된 다음 노드
        # next_node 의 엣지가 2개면 -> [현재 노드, (형제 노드 or 조부모 노드)]
        elif len(graph[next_node]) == 2:
            node1 = graph[next_node][0]
            node2 = graph[next_node][1]
            # if node1 == 현재 노드:
            if node1 == node:
                # node2 = (형제 노드 or 조부모 노드)
                # node2 와 node2의 부모 관계를 끊으면, node2 는 리프노드가 된다.
                if len(graph[node2]) == 1:
                    parent_leaf.append(next_node)

    # 잎이 3개 이상인 경우
    if len(leaf_list) >= 3:
        return False

    # 잎이 2개인 경우
    if len(leaf_list) == 2:
        # 간선 제거
        for next_node in graph[node]:
            graph[next_node].remove(node)

        bundle_list.append([node, leaf_list[0], leaf_list[1]])
        return True

    # 잎이 1개인 경우
    if len(parent_leaf) == 1:
        # 간선 제거
        for next_node in graph[node]:
            graph[next_node].remove(node)

        bundle_list.append([node, parent_leaf[0], graph[parent_leaf[0]][0]])
        return True
    return True


for _ in range(N - 1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

DFS(1, 0)

if len(bundle_list) == N // 3:
    print("S")
    for bundle in bundle_list:
        print(*bundle)
else:
    print("U")
