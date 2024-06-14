import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
K = int(input())

answer = 0

# 모든 행에 대해서 반복
for _y in range(N):
    # 0의 개수 세기
    zero_cnt = 0
    for num in board[_y]:
        if num == "0":
            zero_cnt += 1

    # 이 행과 똑같은 값을 가진 행의 개수 세기
    col_light_cnt = 0
    if zero_cnt <= K and zero_cnt % 2 == K % 2: # 이 행을 모두 킬 수 있다면
        for __y in range(N):
            if board[_y] == board[__y]:
                col_light_cnt += 1

    answer = max(answer, col_light_cnt)

print(answer)
