"""
- BFS 로 문제 해결
"""

r, c = map(int, input().split())

graph = list()

for _ in range(r):
    graph.append(list(input()))

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    global o, v

    temp = list()
    temp.append([x, y])

    # 현재 위치의 늑대, 양 확인
    if graph[x][y] == "v":
        v += 1
    elif graph[x][y] == "o":
        o += 1

    # 현재 위치 방문 처리
    graph[x][y] = "#"

    while temp:
        x, y = temp.pop(0)
        # 이동
        for m in range(4):
            new_x = x + dx[m]
            new_y = y + dy[m]

            # 범위 벗어나지 않는지 확인
            if 0 <= new_x < r and 0 <= new_y < c and graph[new_x][new_y] != "#":
                if graph[new_x][new_y] == "v":
                    graph[new_x][new_y] = "#"
                    v += 1
                elif graph[new_x][new_y] == "o":
                    graph[new_x][new_y] = "#"
                    o += 1
                else:
                    graph[new_x][new_y] = "#"

                # 다음 경로 이동
                temp.append([new_x, new_y])

    # 모든 이동이 불가능 할때
    return


total_o, total_v = 0, 0

for i in range(r):
    for j in range(c):
        if graph[i][j] != "#":
            o, v = 0, 0
            bfs(i, j)
            if o > v:
                total_o += o
            else:
                total_v += v

print(total_o, total_v)
