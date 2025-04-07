N, M = map(int, input().split())
number_list = list(map(int, input().split()))

answer = 0
group = list()

# 이분탐색 : mid = 현재 그룹합의 최대값 기준
left = max(number_list)
right = sum(number_list)

while left <= right:
    mid = (left + right) // 2

    group_count = 0

    idx = 0
    group = list()
    while idx < N:
        sub_sum = 0
        sub_count = 0
        while idx < N and sub_sum + number_list[idx] <= mid:
            sub_sum += number_list[idx]
            sub_count += 1
            idx += 1

            # 남은 그룹의 갯수와 남은 구슬의 갯수가 같은 경우
            if M - group_count == N - (idx - 1):
                break
        group_count += 1
        group.append(sub_count)

    if group_count <= M:
        right -= 1
    else:
        left += 1

    answer = mid

print(answer)
print(*group)
