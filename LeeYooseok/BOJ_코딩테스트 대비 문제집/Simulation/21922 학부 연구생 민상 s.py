from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]


queue = deque()

graph = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 9:
            queue.append((i, j))
            visited[i][j] = 1
    graph.append(line)


def bfs(g, q):
    xd = [-1, 1, 0, 0]
    yd = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx, ny = xd[idx], yd[idx]
            r, c = x + nx, y + ny
            while 0 <= r < n and 0 <= c < m:
                visited[r][c] = 1
                if g[r][c] == 9: # 방문한 곳이 에어컨이 있다면 이미 처리했기 때문에 넘어감
                    break
                # 방문한 곳에 3, 4 번 아이템이 있다면, 방향 전환
                if g[r][c] == 3:
                    nx, ny = -ny, -nx
                elif g[r][c] == 4:
                    nx, ny = ny, nx
                # 방문한 곳이 되돌아 가는 길이라면 넘어감
                elif (g[r][c] == 1 and nx == 0) or (g[r][c] == 2 and ny == 0):
                    break
                # 에어컨 바람 하나를 끝까지 확인 하고 다음 바람으로 넘어감, 즉 que 에 다시 넣어줄 일이 없음...
                r += nx
                c += ny
    answer = 0
    for ans in visited:
        answer += ans.count(1)
    return answer


print(bfs(graph, queue))