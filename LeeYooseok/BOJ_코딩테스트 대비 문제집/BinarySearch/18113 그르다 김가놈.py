N, K, M = map(int, input().split())
length_list = [int(input()) for _ in range(N)]

answer = -1

start, end = 1, max(length_list)

while start <= end:
    mid = (start + end) // 2

    able_m = 0
    for gimbap in length_list:
        if gimbap >= 2 * K:
            able_m += (gimbap - (2 * K)) // mid
        elif K < gimbap < 2 * K:
            able_m += (gimbap - K) // mid
        else:
            continue

    if able_m < M:
        end = mid - 1
    else:
        start = mid + 1
        answer = max(mid, answer)
print(answer)