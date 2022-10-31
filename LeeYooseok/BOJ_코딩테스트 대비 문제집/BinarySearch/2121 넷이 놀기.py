import sys

input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())

point_list = [list(map(int, input().split())) for _ in range(N)]

answer = 0


def find_point(_x, _y):
    start, end = 0, N - 1

    while start <= end:
        mid = (start + end) // 2

        if point_list[mid] == [_x, _y]:
            return True
        elif point_list[mid] > [_x, _y]:
            end = mid - 1
        else:
            start = mid + 1

    return False


point_list.sort(key=lambda x: [x[0], x[1]])
for p_x, p_y in point_list:
    if find_point(p_x + A, p_y) and find_point(p_x + A, p_y + B) and find_point(p_x, p_y + B):
        answer += 1

print(answer)
