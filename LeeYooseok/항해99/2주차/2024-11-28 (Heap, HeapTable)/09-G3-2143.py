import sys

input = sys.stdin.readline

import bisect

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_prefix_sum = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    if i == 0:
        for j in range(i, n):
            if j == 0:
                A_prefix_sum[i][j] = A[0]
            else:
                A_prefix_sum[i][j] = (A_prefix_sum[i][j - 1] + A[j])
    else:
        for j in range(i, n):
            if j == i:
                A_prefix_sum[i][j] = A[i]
            else:
                A_prefix_sum[i][j] = (A_prefix_sum[i][j - 1] + A[j])

# A의 부분배열로 나올 수 있는 모든 경우의 수
A_part_sum = list()
for i in range(n):
    for j in range(i, n):
        A_part_sum.append(A_prefix_sum[i][j])

B_prefix_sum = [[0 for _ in range(m)] for _ in range(m)]
for i in range(m):
    if i == 0:
        for j in range(i, m):
            if j == 0:
                B_prefix_sum[i][j] = B[0]
            else:
                B_prefix_sum[i][j] = (B_prefix_sum[i][j - 1] + B[j])
    else:
        for j in range(i, m):
            if j == i:
                B_prefix_sum[i][j] = B[i]
            else:
                B_prefix_sum[i][j] = (B_prefix_sum[i][j - 1] + B[j])

# B의 부분배열로 나올 수 있는 모든 경우의 수
B_part_sum = list()
for i in range(m):
    for j in range(i, m):
        B_part_sum.append(B_prefix_sum[i][j])

# 2 배열의 값을 조합해서 T를 만들 수 있는 경우의 수가 정답임
A_part_sum.sort()
B_part_sum.sort()

answer = 0
for i in range(len(A_part_sum)):
    A_value = A_part_sum[i]
    # B_part_sum 에서 (T-A_value) 의 시작값과 끝 값을 찾으면 되는 문제
    # bisect_left : list 에서 value 가 가장 처음 나오는 곳의 index 반환
    # 리스트 내에 값이 없으면 해당 값보다 큰 첫 번째 위치를 반환합니다.
    start = bisect.bisect_left(B_part_sum, T-A_value)
    # bisect_right : list 에서 value 가 가장 마지막 나오는 곳의 index + 1 반환
    # 리스트 내에 값이 없으면 해당 값보다 작은 마지막 위치의 바로 다음을 반환합니다.
    end = bisect.bisect_right(B_part_sum, T-A_value)

    # 즉, 찾고자 하는 값이 없으면, start 와 end 는 동일한 값을 반환한다.
    answer += (end - start)