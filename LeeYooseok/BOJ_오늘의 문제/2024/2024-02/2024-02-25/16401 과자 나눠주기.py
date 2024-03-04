M, N = map(int, input().split())
stick_list = list(map(int, input().split()))

left, right = 1, 1e9

answer = 0
while left <= right:
    mid = (left + right) // 2

    num = 0
    for stick in stick_list:
        num += (stick // mid)

    if num >= M:
        left = mid + 1
        answer = max(answer, int(mid))
    else:
        right = mid - 1

print(answer)
