n = int(input())

nums = [i for i in range(1, n+1)]

start = 0
end = 1

result = 0

while end < n+1:
    total = sum(nums[start:end])

    if total == n:
        result += 1
        end += 1

    if total < n:
        end += 1

    if total > n:
        start += 1

print(result)