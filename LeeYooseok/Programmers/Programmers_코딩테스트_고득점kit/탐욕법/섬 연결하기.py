def solution(n, costs):
    answer = 0

    parent = [0 for _ in range(n)]
    for i in range(n):
        parent[i] = i

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    edges = list()

    for start, end, cost in costs:
        edges.append([cost, start, end])

    edges.sort()

    for cost, start, end in edges:
        if find(start) != find(end):
            union(start, end)
            answer += cost

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))