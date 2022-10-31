N, M = map(int, input().split())
staff_list = list(map(int, input().split()))

t_max = max(staff_list)
start, end = 0, t_max * M
answer = t_max * M
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