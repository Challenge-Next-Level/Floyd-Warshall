"""
정렬해도 상관없음 - 이유 : 두 수의 합이기 때문에
"""

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

t = int(input())

start = 0
end = n-1

result = 0

while start < end:
    if nums[start] + nums[end] == t:
        result += 1
    # 더한 숫자가 목표보다 작으면
    elif nums[start] + nums[end] < t:
        start += 1
        continue

    # 더한 숫자가 목표보다 크거나, 목표값이 나왔을 때
    end -= 1

print(result)