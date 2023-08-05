N, K, M = map(int, input().split())

gimbap_list = list()

start = 1
end = 0
for _ in range(N):
    gimbap_size = int(input())

    if gimbap_size <= K:
        continue
    elif K < gimbap_size < 2 * K:
        gimbap_list.append(gimbap_size - K)
        end = max(end, gimbap_size - K)
    elif 2 * K <= gimbap_size:
        gimbap_list.append(gimbap_size - 2 * K)
        end = max(end, gimbap_size - 2 * K)

answer = -1
while start <= end:
    mid = (start + end) // 2

    total_cnt = 0
    for gimbap in gimbap_list:
        total_cnt += (gimbap // mid)

    if total_cnt >= M:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
