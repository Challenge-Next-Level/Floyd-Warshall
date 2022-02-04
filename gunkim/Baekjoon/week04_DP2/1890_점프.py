import sys

N = int(input())
m = []
answer = [[0] * N for _ in range(N)]
for i in range(N):
    m.append(list(map(int, sys.stdin.readline().split())))

answer[0][0] = 1 # 시작 지점을 1(한 가지의 경우)로 초기화
for i in range(N): # 각 지점에서 갈 수 있는 곳에 경로를 더해준다.
    for j in range(N):
        if i == N - 1 and j == N - 1: # 도착지점에 오면 종료
            break
        jump = m[i][j]
        if i + jump < N:
            answer[i + jump][j] += answer[i][j]
        if j + jump < N:
            answer[i][j + jump] += answer[i][j]
print(answer[N - 1][N - 1])