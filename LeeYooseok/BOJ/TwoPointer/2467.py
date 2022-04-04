import sys

N = int(input())
nums = list(map(int, input().split()))

start = 0
end = N-1

result = sys.maxsize

result_start, result_end = 0, 0

while start < end:
    if abs(nums[start] + nums[end]) < result:
        result = abs(nums[start] + nums[end])

        result_start = nums[start]
        result_end = nums[end]

    # 더한 것이 0보다 작으면, start를 오른쪽으로 한칸 이동
    if nums[start] + nums[end] < 0:
        start += 1

    # 더한 것이 0 보다 크면, end를 왼쪽으로 한칸 이동
    else:
        end -= 1

print(result_start, result_end)
