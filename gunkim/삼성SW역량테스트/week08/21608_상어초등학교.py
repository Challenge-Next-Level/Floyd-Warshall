# 좋아하는 학생번호가 똑같은 사람이 입력이 될 수 있다. 그러면 나중에 만족도 계산시 그 수만큼 카운트가 되야함
import sys

n = int(sys.stdin.readline().split()[0])
student = [[[0 for _ in range(2)] for _ in range(n * n + 1)] for _ in range(n * n + 1)]
turn = []
for _ in range(n * n):
    num, n1, n2, n3, n4 = map(int, sys.stdin.readline().split())
    turn.append(num)
    student[num][n1][0] = student[num][n2][0] = student[num][n3][0] = student[num][n4][0] = 1
    student[num][n1][1] += 1
    student[num][n2][1] += 1
    student[num][n3][1] += 1
    student[num][n4][1] += 1
board = [[0 for _ in range(n)] for _ in range(n)]
dir = [[0,1], [0,-1], [1,0], [-1,0]]

for i in range(n * n):
    who = turn[i] # 자리를 정할 학생의 번호
    target = [0, float('inf'), float('inf'), 0] # 인접 칸 좋아 하는 학생 수, 좌표, 좌표 주위의 빈 칸 수
    for a in range(n):
        for b in range(n):
            count = empty = 0
            if board[a][b] == 0: # 1. 비어있는 칸 중에서
                for dy, dx in dir:
                    ny, nx = a + dy, b + dx
                    if 0 <= ny < n and 0 <= nx < n and student[who][board[ny][nx]][0] == 1:
                        count += 1
                    if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                        empty += 1

                if count > target[0]: # 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
                    target = [count, a, b, empty]
                elif count == target[0]:
                    if empty > target[-1]: # 2. 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
                        target = [count, a, b, empty]
                    elif empty == target[-1]:
                        if a < target[1]: # 3. 행의 번호가 가장 작은 칸으로
                            target = [count, a, b, empty]
                        elif a == target[1]:
                            if b < target[2]: # 열의 번호가 가장 작은 칸으로 자리를 정한다.
                                target = [count, a, b, empty]
    board[target[1]][target[2]] = who


answer = 0
for a in range(n):
    for b in range(n):
        num = board[a][b]
        count = 0
        for dy, dx in dir:
            ny, nx = a + dy, b + dx
            if 0 <= ny < n and 0 <= nx < n and student[num][board[ny][nx]][0] == 1:
                count += student[num][board[ny][nx]][1]
        if count == 4:
            answer += 1000
        elif count == 3:
            answer += 100
        elif count == 2:
            answer += 10
        elif count == 1:
            answer += 1
print(answer)