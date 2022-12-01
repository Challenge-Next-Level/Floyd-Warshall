N, K = map(int, input().split())
level_list = [int(input()) for _ in range(N)]

answer = min(level_list)
start, end = answer, max(level_list) + K

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for l in level_list:
        if l < mid:
            temp += (mid - l)

    if temp <= K:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
