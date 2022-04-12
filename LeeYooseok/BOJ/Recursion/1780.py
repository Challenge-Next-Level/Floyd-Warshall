import sys

input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

# -1, 0, 1
result = [0, 0, 0]


def solution(board, size):
    # 종이 크기가 1칸이라면,
    if size == 1:
        result[board[0][0] + 1] += 1
        return
    else:
        # 9칸으로 나눠서 확인
        for i in range(3):
            for j in range(3):
                chk_size = size // 3
                if chk_size == 1:
                    temp_board = [[board[i][j]]]
                    solution(temp_board, chk_size)
                else:
                    # i == 1, j == 0 -> 3 ~ 5, 0 ~ 2
                    temp_board = list()
                    for k in range(chk_size):
                        temp_board.append(board[i * chk_size + k][j * chk_size:(j + 1) * chk_size])

                    temp_result = set()
                    for c in temp_board:
                        temp_result.update(set(c))
                    if len(temp_result) == 1:
                        result[list(temp_result)[0] + 1] += 1
                        continue
                    else:
                        solution(temp_board, chk_size)


temp_result = set()
for c in paper:
    temp_result.update(set(c))
if len(temp_result) == 1:
    result[list(temp_result)[0] + 1] += 1
else:
    solution(paper, n)

for q in range(3):
    print(result[q])
