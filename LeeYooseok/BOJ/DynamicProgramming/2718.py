t = int(input())

nums = list()
for _ in range(t):
    nums.append(int(input()))

max_num = max(nums)

# 0, 1, 2, 3, 4
dp = [0, 1, 5, ]