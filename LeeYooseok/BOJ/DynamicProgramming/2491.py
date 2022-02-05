import sys

n = int(input())

nums = list(map(int, sys.stdin.readline().split()))

dp_up, dp_down = [1] * n, [1] * n

for i in range(1, n):
    # 증가 수열 확인
    if nums[i] >= nums[i - 1]:
        dp_up[i] = dp_up[i - 1] + 1
    # 감소 수열 확인
    if nums[i] <= nums[i - 1]:
        dp_down[i] = dp_down[i - 1] + 1


print(max(max(dp_up), max(dp_down)))
