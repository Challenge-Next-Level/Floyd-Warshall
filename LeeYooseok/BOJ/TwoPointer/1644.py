n = int(input())

prime_nums = list()

a = [False, False] + [True] * (n-1)

for i in range(2, n+1):
    if a[i]:
        prime_nums.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

result = 0

start = 0
end = 0

while end <= len(prime_nums):
    total = sum(prime_nums[start:end])

    if total == n:
        result += 1
        end += 1

    elif total < n:
        end += 1

    elif total > n:
        start += 1

print(result)
