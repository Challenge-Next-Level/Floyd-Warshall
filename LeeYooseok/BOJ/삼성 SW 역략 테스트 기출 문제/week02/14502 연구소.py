# back tracking 으로 경우의 수 만들기

from collections import deque

# 벽을 세울 수 있는 모든 경우의 수 확인
n, m = map(int, input().split())

board = list()
bugs = list()  # [y, x] 위치
for i in range(n):
    temp = list(map(int, input().split()))
    if temp.count(2) > 0:
        for j in range(temp.count(2)):
            bugs.append([i, temp.index(2, j)])

    board.append(temp)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


# 안전한 영역 확인 함수
def check():
    visited = [item[:] for item in board] # deepcopy 대신 해당 코드 사용 - 속도 향상

    for b in bugs:
        queue = deque()
        queue.append(b)

        while queue:
            now_y, now_x = queue.popleft()

            for i in range(4):
                new_y, new_x = now_y + dy[i], now_x + dx[i]

                if not (0 <= new_x < m) or not (0 <= new_y < n):
                    continue

                if visited[new_y][new_x] == 0:
                    queue.append([new_y, new_x])
                    visited[new_y][new_x] = 2
    result = 0
    for r in visited:
        result += r.count(0)

    return result


answer = 0


def makeWall(cnt):
    global answer
    if cnt == 3:
        answer = max(answer, check())
        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = 1
                makeWall(cnt + 1)
                board[i][j] = 0


makeWall(0)

print(answer)
