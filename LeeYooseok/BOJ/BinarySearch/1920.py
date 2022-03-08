n = int(input())
nums = list(map(int, input().split()))
nums.sort()

m = int(input())
target = list(map(int, input().split()))


def solution(t):
    left, right = 0, n-1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == t:
            return 1
        elif nums[mid] > t:
            right = mid - 1
        else:
            left = mid + 1
    return 0


for t in target:
    print(solution(t))
