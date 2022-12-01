# 내 첫 풀이에서 visit 사용법을 바꿈
# visit을 bool 형이 아닌 int형으로 수정한 뒤 해당 좌표까지 k가 몇 번 남았는지를 최적의 값을 기록한다
# k값 최소로 사용하여 올 수 있다면 그 값을 visit에 갱신
import sys
from collections import deque

k = int(input())
w, h = map(int, sys.stdin.readline().split())
board = []
for _ in range(h):
    board.append(list(map(int, sys.stdin.readline().split())))

visit = [[-1 for _ in range(w)] for _ in range(h)]

near = [[0,1], [0,-1], [1,0], [-1,0]]
horse = [[-2,-1], [-1,-2], [-2,1], [-1,2], [1,-2], [2,-1], [1,2], [2,1]]


def bfs():
    dq = deque([[0,0,k,0]])
    visit[0][0] = k
    while dq:
        y, x, cnt, answer = dq.popleft()
        if y == h-1 and x == w-1:
            return answer
        if cnt > 0: # 말 이동 경우
            for dy, dx in horse:
                ny, nx = y + dy, x + dx
                if 0<=ny<h and 0<=nx<w and board[ny][nx] == 0:
                    if visit[ny][nx] == -1 or visit[ny][nx] < cnt-1:
                        visit[ny][nx] = cnt-1
                        dq.append([ny, nx, cnt-1, answer+1])
        for dy, dx in near: # 근접 이동 경우
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == 0:
                if visit[ny][nx] == -1 or visit[ny][nx] < cnt:
                    visit[ny][nx] = cnt
                    dq.append([ny, nx, cnt, answer + 1])
    return -1


print(bfs())