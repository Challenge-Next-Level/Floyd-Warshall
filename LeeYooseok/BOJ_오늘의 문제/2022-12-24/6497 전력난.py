# 크루스칼 알고리즘 활용 - 최소 스패닝 트리

# 루트 노드를 확인하여 같은 집합인지 확인한다.
def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node]) # node 의 부모는
    return parent[node]

# a 와 b 가 속한 집합을 합친다.
def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        exit()

    edges = list()
    parent = [i for i in range(m + 1)]
    ans = 0

    for _ in range(n):
        x, y, z = map(int, input().split())

        edges.append([x, y, z])

    # 거리 순으로 정렬
    edges.sort(key=lambda x:x[2])

    for x, y, z in edges:
        # 사이클이 이루어졌는지 확인
        if find(x) != find(y):
            # 사이클이 이루어지지 않았다면, 부모 노드 갱신
            union(x, y)
        else:
            # 사이클이 이루어졌다면, 해당 간선 제거
            ans += z

    print(ans)
