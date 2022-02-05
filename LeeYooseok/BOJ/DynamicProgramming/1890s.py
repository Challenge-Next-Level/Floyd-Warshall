"""
- 단순하게 해답 함수 작성 후, 재귀 활용 -> 시간초과 뜸
"""
import sys

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
result = 0


# 현재 좌표 (i,j)
def solution(i, j):
    global result
    num = matrix[i][j]
    # 오른쪽 방향 확인
    if j + num < n:  # 범위 벗어나는지 확인
        next_num = matrix[i][j + num]
        if next_num == 0:
            result += 1
            return
        else:
            solution(i, j + num)

    # 아래쪽 방향 확인
    if i + num < n:
        next_num = matrix[i + num][j]
        if next_num == 0:
            result += 1
            return
        else:
            solution(i + num, j)

    return


solution(0, 0)

print(result)