import sys

input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

zero, one = 0, 0


def solution(paper, length):
    global zero, one
    # 전체가 1개의 색으로 칠해져 있는지 확인
    temp_set = set()
    for r in paper:
        temp_set.update(set(r))

    if len(list(temp_set)) == 1:
        if list(temp_set)[0] == 0:
            zero += 1
        else:
            one += 1
        return

    # 전체를 나눠야 하는 경우
    next_length = int(length/2)
    # 제 1 사분면 : [0 : length / 2][length / 2 : ]
    temp_board = []
    for i in range(next_length):
        temp_board.append(paper[i][next_length:])
    solution(temp_board, next_length)
    # 제 2 사분면 : [0 : length / 2][0 : length / 2]
    temp_board = []
    for i in range(next_length):
        temp_board.append(paper[i][:next_length])
    solution(temp_board, next_length)
    # 제 3 사분면 : [length / 2 : ][0 : length / 2]
    temp_board = []
    for i in range(next_length):
        temp_board.append(paper[next_length + i][next_length:])
    solution(temp_board, next_length)
    # 제 4 사분면 : [length / 2 : ][length / 2 : ]
    temp_board = []
    for i in range(next_length):
        temp_board.append(paper[next_length + i][:next_length])
    solution(temp_board, next_length)


solution(paper, n)

print(zero)
print(one)
