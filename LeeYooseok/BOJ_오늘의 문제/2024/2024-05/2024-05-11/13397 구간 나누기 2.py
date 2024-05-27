import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = list(map(int, input().split()))


def count(diff):
    cnt = 1

    min_num, max_num = num_list[0], num_list[0]
    for num in num_list:
        # 현재 구간의 최댓값
        if max_num < num:
            max_num = num

        # 현재 구간의 최솟값
        if min_num > num:
            min_num = num

        # 최대 - 최소 > 현재 설정한 차이의 최대값 -> 새로운 구간
        if max_num - min_num > diff:
            cnt += 1
            min_num, max_num = num, num

    return cnt


# 이분 탐색으로 찾고자 하는 수 : 구간에서의 최댓값 - 최소값
left, right = 0, max(num_list)
answer = right

while left <= right:
    mid = (left + right) // 2

    # 구간 개수가 M 개 이하이면, 차이의 최대값 늘리기
    if count(mid) <= M:
        right = mid - 1
        answer = min(answer, mid)
    else:
        left = mid + 1

print(answer)