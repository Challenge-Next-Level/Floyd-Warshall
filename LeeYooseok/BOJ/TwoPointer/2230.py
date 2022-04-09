import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())

nums = [int(input()) for _ in range(n)]
nums.sort()

result = INF

start = 0
end = 1

while start < n and end < n:
    now_sub = nums[end] - nums[start]

    if now_sub == m:
        result = m
        break

    elif now_sub < m:
        end += 1

    elif now_sub >= m:
        if now_sub < result:
            result = now_sub
        start += 1

print(result)
