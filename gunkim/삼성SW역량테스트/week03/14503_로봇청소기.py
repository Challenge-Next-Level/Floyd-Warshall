import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

direct = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 북,동,남,서
visited = [[0] * m for _ in range(n)] # 청소유무 저장
answer = 1
visited[r][c] = 1

while True:
    flag = 0 # 이동유무 체크
    for i in range(4):
        d = (d - 1 + 4) % 4 # 왼쪽으로 방향 전환
        nr, nc = r + direct[d][0], c + direct[d][1]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0 and visited[nr][nc] == 0:
            r, c = nr, nc
            visited[r][c] = 1
            answer += 1
            flag = 1
            break # 여기에 continue 작성하고 에러 찾느라 개고생함
    if flag == 1:
        continue
    nr, nc = r + direct[(d + 2) % 4][0], c + direct[(d + 2) % 4][1]
    if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
        break
    r, c = nr, nc

print(answer)