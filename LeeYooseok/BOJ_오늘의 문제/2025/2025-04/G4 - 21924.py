import sys

input = sys.stdin.readline

N, M = map(int, input().split())

edge_list = list()
total_cost = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    edge_list.append([c, a, b])
    total_cost += c

edge_list.sort()

parent = [i for i in range(N + 1)]


def find(node):
    if parent[node] != node:
        return find(parent[node])
    return node


def union(node_1, node_2):
    node_1 = find(node_1)
    node_2 = find(node_2)

    if node_1 < node_2:
        parent[node_2] = node_1
    else:
        parent[node_1] = node_2


answer = 0
for c, a, b in edge_list:
    if find(a) != find(b):
        union(a, b)
        answer += c
answer = total_cost - answer
root_parent = parent[1]
for other_parent in parent[2: N + 1]:
    if root_parent != find(other_parent):
        answer = -1

print(answer)
