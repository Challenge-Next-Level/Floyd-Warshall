import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

result = sys.maxsize
result_list = list()

for i in range(n):
    start = 0
    end = n-1

    while start < end:
        if start == i:
            start += 1
            continue

        if end == i:
            end -= 1
            continue

        value = nums[start] + nums[end] + nums[i]

        if result >= abs(value):
            result = abs(value)
            result_list = [nums[start], nums[end], nums[i]]

        if value > 0:
            end -= 1
        else:
            start += 1


result_list.sort()
print(' '.join(map(str, result_list)))