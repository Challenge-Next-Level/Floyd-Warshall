"""
특정 수 1개를 골라서 그 수를 검사한다.
"""

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

result = 0

for i in range(n):
    temp_nums = nums[:i] + nums[i+1:]
    target = nums[i]

    start = 0
    end = n-1

    while start < end:
        total = nums[start] + nums[end]
        if total == target:
            result += 1
            break

        if total < target:
            start += 1

        if total > target:
            end -= 1

print(result)
