N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
node_list = list(map(int, input().split()))

parent = [i for i in range(N + 1)]


def find(node):
    if parent[node] != node:
        return find(parent[node])
    return node


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            union(i + 1, j + 1)


answer = "YES"
target_parent = find(parent[node_list[0]])

for path in node_list[1:]:
    if find(path) != target_parent:
        answer = "NO"
        break

print(answer)
