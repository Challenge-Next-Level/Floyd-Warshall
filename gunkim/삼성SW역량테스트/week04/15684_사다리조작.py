import sys


def check():
    for i in range(n): # 각 출발점에서의 결과 확인
        temp = i # 이동하는 세로선 위치
        for j in range(h): # 가로선을 한 칸씩 내리면서 이동 확인 (중요!)
            if graph[j][temp] == 1:  # 오른쪽 이동
                temp += 1
            elif temp > 0 and graph[j][temp - 1] == 1: # 왼쪽 이동
                temp -= 1
        if temp != i:
            return False
    return True


def dfs(cnt, y, x): # cnt: 가로선을 만든 횟수
    global ans
    if ans <= cnt: # 백트래킹: cnt가 현재 ans보다 크거나 같다면 빨리 return하고 최적의해를 다른 경우에서 찾는다
        return
    if check(): # 현재 사다리가 유효한지 확인
        ans = min(ans, cnt)
        return
    for i in range(y, h): # 세로 축 이동, 현재축(y,x)에서 내려갈 일 밖에 없기 때문에 [y:h]범위임
        if i != y:
            x = 0
        for j in range(x, n - 1): # 가로 축 이동, 현재축(y,x) 포함 및 이후로 다리를 놓는 경우를 따져야 하기 때문에 [k:n-1]범위
            if graph[i][j] == 0: # 0인 경우 가로줄 만들고, 연속된 가로선을 만들지 않기 위해 j + 2호출
                graph[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                graph[i][j] = 0


n, m, h = map(int, sys.stdin.readline().split())  # 세로, 다리를 잇는 다리 수, 가로
graph = [[0] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split()) # 다리의 좌표
    graph[a - 1][b - 1] = 1

ans = 4
dfs(0, 0, 0)

if ans <= 3:
    print(ans)
else:
    print(-1)