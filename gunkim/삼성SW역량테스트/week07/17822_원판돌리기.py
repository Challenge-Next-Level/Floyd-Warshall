import sys

n, m, t = map(int, sys.stdin.readline().split())
board = []
for _ in range(n): # 원판 입력
    board.append(list(map(int, sys.stdin.readline().split())))

case = []
for _ in range(t): # 회전하는 케이스 입력
    case.append(list(map(int, sys.stdin.readline().split())))

for i in range(t):
    num, d, cnt = case[i]
    cnt %= m
    plus = num
    while num <= n: # num 배수의 원판 회전
        if d == 0:
            temp = board[num - 1][:m - cnt]
            board[num - 1] = board[num - 1][m - cnt:] + temp
        elif d == 1:
            temp = board[num - 1][:cnt]
            board[num - 1] = board[num - 1][cnt:] + temp
        num += plus

    delete = [[0] * m for _ in range(n)]
    flag = 0 # 같은 숫자가 있는지 체크
    for a in range(n):
        for b in range(m):
            if board[a][b] == 0:
                continue
            if 0 < a < n: # 안 쪾이랑 비교
                if board[a][b] == board[a - 1][b]:
                    delete[a][b] = 1
                    flag = 1
                    continue
            if 0 <= a < n - 1: # 바깥 쪽이랑 비교
                if board[a][b] == board[a + 1][b]:
                    delete[a][b] = 1
                    flag = 1
                    continue
            if board[a][b] == board[a][b - 1] or board[a][b] == board[a][(b + 1) % m]: # 양 옆이랑 비교
                delete[a][b] = 1
                flag = 1
    if flag == 1: # 같은 수가 있다면 지우기
        for a in range(n):
            for b in range(m):
                if delete[a][b] == 1:
                    board[a][b] = 0
    else: # 같은 수가 없다면 평균 구하고 +-1 계산
        total = count = 0
        for a in range(n):
            for b in range(m):
                if board[a][b] != 0:
                    total += board[a][b]
                    count += 1
        if count != 0: # 모두 지워진 상태일 수도 있다(zero division 방지)
            avg = total / count
            for a in range(n):
                for b in range(m):
                    if board[a][b] != 0:
                        if board[a][b] > avg:
                            board[a][b] -= 1
                        elif board[a][b] < avg:
                            board[a][b] += 1
answer = 0
for i in range(n):
    answer += sum(board[i])
print(answer)