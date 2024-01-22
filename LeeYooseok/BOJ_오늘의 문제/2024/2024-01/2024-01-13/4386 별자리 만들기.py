import math

n = int(input())
star_list = [list(map(float, input().split())) for _ in range(n)]

edge_list = list()
for i in range(n - 1):
    for j in range(i + 1, n):
        cost = math.sqrt((star_list[i][0] - star_list[j][0]) ** 2 + (star_list[i][1] - star_list[j][1]) ** 2)
        edge_list.append([cost, i, j])

edge_list.sort()
parent = [i for i in range(n)]


def find(node):
    if parent[node] == node:
        return node

    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    parent1, parent2 = find(node1), find(node2)

    if parent1 < parent2:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2


answer = 0
for edge in edge_list:
    cost, x, y = edge

    if find(x) != find(y):
        union(x, y)
        answer += cost

print(round(answer, 2))
