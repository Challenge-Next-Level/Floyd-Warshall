import sys

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N

answer = sys.maxsize

def recur(target):

    # 모든 회사 인원을 사용하였을 때, 점수 계산 후 결과값 업데이트
    if target == N:
        score()
        return

    # 모든 경우 탐색
    visited[target] = True
    recur(target + 1)
    visited[target] = False
    recur(target + 1)

def score():
    global answer

    start = 0
    link = 0

    for i in range(N-1):
        for j in range(i + 1, N):
            if visited[i] and visited[j]:
                start += board[i][j] + board[j][i]
            elif not visited[i] and not visited[j]:
                link += board[i][j] + board[j][i]

    answer = min(answer, abs(start - link))

recur(0)
print(answer)