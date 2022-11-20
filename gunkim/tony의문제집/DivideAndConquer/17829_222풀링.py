import sys

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))


def second_number(a,b,c,d):
    nums = [a,b,c,d]
    max_num = max(nums)
    nums.remove(max_num)
    return max(nums)


def pooling(result):
    length = len(result)//2
    new_result = [[] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            ny, nx = (i*2), (j*2)
            new_result[i].append(second_number(result[ny][nx], result[ny][nx+1], result[ny+1][nx], result[ny+1][nx+1]))
    if len(new_result) == 1:
        print(new_result[0][0])
    else:
        pooling(new_result)
    return


pooling(board)