import sys

input = sys.stdin.readline

# union & find 문제

N, M = map(int, input().split())

parent = [i for i in range(N + 1)]


def find(node):
    if parent[node] != node:
        return find(parent[node])
    return parent[node]


def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)

    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2


answer = 0

for _ in range(M):
    u, v = map(int, input().split())
    # union 하기 전에 부모가 같다면, cycle 이 존재하는 것.
    if find(u) == find(v):
        answer += 1  # edge 를 제거 -> 실제로는 제거하지 않은
    else:
        union(u, v)

parent_set = set()
for i in range(1, N + 1):
    parent_set.add(find(i))

print(answer + len(parent_set) - 1)
