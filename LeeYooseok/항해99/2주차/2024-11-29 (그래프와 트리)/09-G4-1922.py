import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
edge_list = list()
for _ in range(M):
    a, b, c = map(int, input().split())
    # 비용을 기준으로 오름차순 정렬하기 위해, 비용을 가장 앞에 넣어준다.
    edge_list.append([c, a, b])

# 부모를 자기 자신으로 초기화
parent = [i for i in range(N + 1)]


def find(node):
    # 루트 노드까지 탐색
    if parent[node] != node:
        parent[node] = find(parent[node])
        return parent[node]
    return node


def union(node_a, node_b):
    parent_a = find(node_a)
    parent_b = find(node_b)

    # 부모가 다르면, 이어준다.
    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


# 엣지 리스트를 비용 기준으로 오름차순 정렬
edge_list.sort(key=lambda x: x[0])

answer = 0
for c, a, b in edge_list:
    # 부모가 다르면
    if find(a) != find(b):
        # 해당 엣지 사용
        union(a, b)
        answer += c

print(answer)
