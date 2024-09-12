"""
DFS 로 풀이 - 재귀 활용 또는 스택_큐
- 건물로 둘러 쌓여 있으면 count 안함
- 방문 한 곳은 -1로 바꿈
-
"""

w, h = map(int, input().split())

graph = [list(map(int, input().split()))]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = 0


def dfs(x, y):
    global result

    temp = list()
    temp.append([x, y])

    # 현재 위치 확인


for i in range(w):
    for j in range(h):
        if graph[i][j] != 0 and graph[i][j] != -1:
            dfs(i, j)
