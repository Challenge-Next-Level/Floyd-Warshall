n = int(input())
nums = list(map(int, input().split()))
nums.sort() # 정렬해도 2 수만 고르면, 1<= i <= j <= n 을 만족하기 때문

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