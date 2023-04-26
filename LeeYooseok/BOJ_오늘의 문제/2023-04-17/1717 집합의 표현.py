import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
rank = [0 for _ in range(N + 1)]


def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    node1 = find(node1)
    node2 = find(node2)
    if rank[node1] > rank[node2]:
        parent[node2] = node1
    else:
        parent[node1] = node2
        if rank[node1] == rank[node2]: rank[node2] += 1


for _ in range(M):
    o, a, b = map(int, input().split())
    if o == 0:
        union(a, b)
    else:
        if find(a) != find(b):
            print("NO")
        else:
            print("YES")
