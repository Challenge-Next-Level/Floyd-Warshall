# 5 개수 세기

M = int(input())

start, end = 1, M * 5
answer = 0
while start <= end:
    mid = (start + end) // 2

    temp = 0
    num_copy = mid
    while num_copy >= 5:
        temp += num_copy // 5
        num_copy //= 5

    if temp < M:
        start = mid + 1
    elif temp > M:
        end = mid - 1
    else:
        end = mid - 1
        answer = mid

if answer == 0:
    print(-1)
else:
    print(answer)