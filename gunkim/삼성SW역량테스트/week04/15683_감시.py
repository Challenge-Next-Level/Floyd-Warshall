import sys

n, m = map(int, sys.stdin.readline().split())
board = []
safe = 0
loc = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    for j in range(len(board[i])):
        if board[i][j] == 0: # 감시 받지 않는 공간
            safe += 1
        elif 1 <= board[i][j] <= 5: # 감시 카메라의 위치
            loc.append([i, j])

# 감시카메라의 감시 방향
number = [
    [],
    [[0], [1], [2], [3]],
    [[0,2], [1,3]],
    [[0,1], [1,2], [2,3], [3,0]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]
direction = [[-1,0], [0,1], [1,0], [0,-1]] # 위 number에 쓰인 0~3 숫자들의 의미 ex)0은 북쪽 이동
length = len(loc)
answer = 0


def search(y, x, direct, visited): # 새롭게 감시한 곳을 카운트하여 리턴
    count = 0
    for d in direct:
        ny, nx = y, x
        while True:
            ny, nx = ny + direction[d][0], nx + direction[d][1]
            if ny < 0 or ny >= n or nx < 0 or nx >= m or board[ny][nx] == 6:
                break
            if visited[ny][nx] == 0:
                visited[ny][nx] = -1 # 감시한 곳은 -1로 표시
                count += 1
    return count


def cctv(cnt, detect, visited): # 모든 감시카메라를 탐색하며 total값 체크
    global answer
    if cnt == length:
        answer = max(answer, detect)
        return
    y, x = loc[cnt]
    temp = [visit[:] for visit in visited] # board와 방문상태가 표시된 리스트를 깊은 복사
    for d in number[board[y][x]]:
        det = search(y, x, d, temp)
        cctv(cnt + 1, detect + det, temp)
        temp = [visit[:] for visit in visited] # 위에서 감시하기 전 상태로 되돌려 놓기


cctv(0, 0, board)
print(safe - answer)