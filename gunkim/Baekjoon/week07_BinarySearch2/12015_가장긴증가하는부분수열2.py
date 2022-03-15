# 우선 LIS라는 문제에 대한 지식이 있어야 하는 것 같음
# 해결법은 DP가 기본적으로 있고 시간초과 문제를 해결하기 위해서 Binary Search로 방향을 잡아야함.
import sys

N = int(sys.stdin.readline()) # 여기서도 코드 조금 더 썼다가 시간초과 발생함...;;
nums = list(map(int, sys.stdin.readline().split()))

LIS = [0]
for i in range(N):
    if nums[i] > LIS[-1]: # 이 조건이 LIS문제를 binary search로 해결하는데 주 역할을 함
        LIS.append(nums[i])
    else:
        left, right = 1, len(LIS) - 1
        while left < right:
            mid = (left + right) // 2
            if LIS[mid] < nums[i]:
                left = mid + 1
            else:
                right = mid
        LIS[right] = nums[i] # LIS의 중간 요소들의 변경도 핵심 역할
print(len(LIS) - 1)
