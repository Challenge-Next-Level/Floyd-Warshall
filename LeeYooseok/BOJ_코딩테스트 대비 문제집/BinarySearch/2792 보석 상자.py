import math
import sys

N, M = map(int, input().split())  # N : 학생 수, M : 색상의 수
item_list = [int(input()) for _ in range(M)]

start, end = 1, max(item_list)
answer = sys.maxsize
while start <= end:
    able_student = 0

    # 한 종류의 보물을 몇개씩 나누어 줄 것인가? : 최대한 다들 공평하게 나누어주기 위해
    mid = (start + end) // 2

    for item in item_list:
        able_student += math.ceil(item / mid)

    if able_student > N:  # 불가능한 경우
        start = mid + 1
    else:
        end = mid - 1
        answer = min(answer, mid)

print(answer)