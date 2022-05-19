import sys

N, L, R = map(int, sys.stdin.readline().split())
country = []
for _ in range(N):
    country.append(list(map(int, sys.stdin.readline().split())))
d = [[0,1], [0, -1], [1,0], [-1,0]]


def dfs(y, x, visit):
    stack = [[y,x]]
    visit[y][x] = 1
    location = [[y, x]]
    while stack:
        sy, sx = stack.pop()
        for dy, dx in d:
            ny, nx = sy + dy, sx + dx
            if 0 <= ny < N and 0 <= nx < N and L <= abs(country[ny][nx] - country[sy][sx]) <= R and visit[ny][nx] == 0:
                stack.append([ny, nx])
                visit[ny][nx] = 1 # visit 처리를 하는 위치가 탐색할 때 중요하다!
                location.append([ny, nx])
    return location # 좌표만 반환해도 답을 구할 수 있음


answer = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag = False
    # 국경선 탐색
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 1:
                continue
            res = dfs(y, x, visited)
            if len(res) > 1:
                num = 0
                flag = True
                for b, a in res: # 연합국 인구를 모두 더하고
                    num += country[b][a]
                num //= len(res) # 연합국 수로 나눠준다
                for b, a in res: # 계산한 num값을 각 나라 인구수로 설정
                    country[b][a] = num
    if flag is False:
        break
    answer += 1
print(answer)