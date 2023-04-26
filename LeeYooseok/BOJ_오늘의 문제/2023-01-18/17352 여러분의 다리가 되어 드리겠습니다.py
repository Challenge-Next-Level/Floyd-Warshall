# union-find 문제

N = int(input())
parent = [i for i in range(N + 1)]
def find(node):
    if parent[node] == node:
        return node

    parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(N - 2):
    u, v = map(int, input().split())
    union(u, v)

pivot = find(1)
for i in range(2, N+1):
    if pivot != find(i):
        print(pivot, i)
        exit()

