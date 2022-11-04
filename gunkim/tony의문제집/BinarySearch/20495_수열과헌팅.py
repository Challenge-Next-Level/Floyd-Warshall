# 아이디어가 떠오르지 않아 다른 분의 코드(java)를 참고
# 완전탐색이 아닌 이분탐색으로 위치를 찾는 것!
import sys

n = int(input())
low, high = [], [] # 최솟값, 최댓값의 경우 저장
numbers = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    numbers.append([a,b])
    low.append(a-b)
    high.append(a+b)
# 정렬
low.sort()
high.sort()


# 가장 큰 원소들 중에서 num(최솟값)의 위치
def lower_bound(num):
    left, right = 0, n-1
    result = n
    while left <= right:
        mid = (left + right) // 2
        if num > high[mid]:
            left = mid + 1
        else:
            right = mid - 1
            result = min(result, mid)
    return result


# 가장 작은 원소들 중에서 num(최댓값)의 위치
def upper_bound(num):
    left, right = 0, n-1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if num < low[mid]:
            right = mid - 1
        else:
            left = mid + 1
            result = max(result, mid)
    return result


for i in range(n):
    lowIdx = lower_bound(numbers[i][0]-numbers[i][1])
    highIdx = upper_bound(numbers[i][0]+numbers[i][1])
    print(lowIdx+1, highIdx+1, sep=' ')