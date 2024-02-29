import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A_prefix_sum = list(map(int, input().split()))
for i in range(1, M):
    A_prefix_sum[i] += A_prefix_sum[i - 1]

for _ in range(N):
    B = int(input())

    if B <= A_prefix_sum[0]:
        print(1)
        continue
    if B > A_prefix_sum[-1]:
        print("Go away!")
        continue

    left = 0
    right = M - 1

    answer = 0
    while left <= right:
        mid = (left + right) // 2

        if A_prefix_sum[mid] >= B:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    print(answer + 1)