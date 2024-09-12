"""
- DFS 로 문제 해결
- DFS 해결 방법은 Runtime Error (Recursion Error) 발생
    - 재귀 횟수 한도 초과
    - 즉, BFS 로 문제 해결해야 함 또는 스택_큐 활용
"""

r, c = map(int, input().split())

graph = list()

for _ in range(r):
    graph.append(list(input()))

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global total_o, total_v

    # 현재 위치의 늑대, 양 확인
    if graph[x][y] == "v":
        total_v += 1
    elif graph[x][y] == "o":
        total_o += 1

    # 현재 위치 방문 처리
    graph[x][y] = "#"

    # 이동
    for m in range(4):
        new_x = x + dx[m]
        new_y = y + dy[m]

        # 범위 벗어나지 않는지 확인
        if 0 <= new_x < r and 0 <= new_y < c:
            # 벽일 때
            if graph[new_x][new_y] == "#":
                continue

            else:
                dfs(new_x, new_y)

    # 모든 이동이 불가능 할때
    return


result_o, result_v = 0, 0

for i in range(r):
    for j in range(c):
        if graph[i][j] != "#":
            total_o, total_v = 0, 0
            dfs(i, j)
            if total_o > total_v:
                result_o += total_o
            else:
                result_v += total_v

print(result_o, result_v)
