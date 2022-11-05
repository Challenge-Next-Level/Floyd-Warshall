# 5 개수 세기

M = int(input())

start, end = 1, M * 5
answer = -1
while start <= end:
    mid = (start + end) // 2

    temp = 0
    num_copy = mid
    while num_copy >= 5:
        temp += num_copy // 5  # 몫
        num_copy //= 5  # 25 -> + 2

    if temp < M:
        start = mid + 1
    elif temp > M:
        end = mid - 1
    else:
        # 정확히 M 개 이어야지만, 정답값 갱신
        end = mid - 1
        answer = mid

print(answer)
