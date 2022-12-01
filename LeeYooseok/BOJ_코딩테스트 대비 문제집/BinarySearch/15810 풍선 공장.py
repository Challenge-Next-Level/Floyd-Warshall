N, M = map(int, input().split())
staff_list = list(map(int, input().split()))

t_min = min(staff_list)
start, end = 0, t_min * M
answer = t_min * M
while start <= end:
    mid = (start + end) // 2

    able_num = 0
    for s in staff_list:
        able_num += (mid // s)

    if able_num < M:
        start = mid + 1
    else:
        end = mid - 1
        answer = min(mid, answer)
print(answer)