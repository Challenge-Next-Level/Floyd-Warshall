import sys
from collections import deque

T = int(sys.stdin.readline().split()[0])
go = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]] # 나이트가 갈 수 있는 경로
for i in range(T):
    N = int(sys.stdin.readline().split()[0]) # 체스판 크기
    yStart, xStart = map(int, sys.stdin.readline().split()) # 시작 지점
    yGoal, xGoal = map(int, sys.stdin.readline().split()) # 도착 지점

    visit = [[0] * N for _ in range(N)]


    def bfs(b, a):
        loc = deque([[b, a, 0]])
        while loc:
            y, x, depth = loc.popleft()
            if visit[y][x] == 1:
                continue
            if y == yGoal and x == xGoal: # 목표 지점이라면 리턴
                return depth
            visit[y][x] = 1
            for g in range(8):
                ny, nx = y + go[g][0], x + go[g][1]
                if 0 <= ny < N and 0 <= nx < N:
                    loc.append([ny, nx, depth + 1])

    answer = bfs(yStart, xStart)
    print(answer)