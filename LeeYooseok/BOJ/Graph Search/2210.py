"""
Brute-Force 풀이법
"""

graph = [list(input().split()) for _ in range(5)]

result = set()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, word, depth):
    if depth == 6:
        result.add(word)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, word + graph[ny][nx], depth + 1)


for i in range(5):
    for j in range(5):
        dfs(j, i, graph[i][j], 1)

print(len(result))
